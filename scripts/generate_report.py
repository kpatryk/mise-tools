#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict, OrderedDict
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib import error as urllib_error
from urllib import request as urllib_request

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
DEFAULT_TAXONOMY_PATH = SKILL_DIR / "references" / "taxonomy.json"
DEFAULT_MISE_REMOTE_URL = "https://github.com/jdx/mise.git"
CACHE_DIR_ENV = "MISE_REGISTRY_REPORT_CACHE_DIR"
CACHE_REPO_NAME = "jdx-mise"
LEGACY_CACHE_REPO_NAME = "jdx-mise.git"
CACHE_METADATA_NAME = "jdx-mise.metadata.json"
LEGACY_CACHE_STAMP_NAME = "jdx-mise.last_refresh"
CACHE_REFRESH_DAYS = 7
SUFFIX_PENALTIES = ("-cli", "-cmd", "-tool", "-sdk", "-core", "-bin")
NORMALIZE_RE = re.compile(r"[^a-z0-9]+")
DEFAULT_HISTORY_LOOKBACK_DAYS = 400
NEGATIVE_SCORE = -(10**9)


@dataclass(frozen=True)
class RegistryEntry:
    short: str
    backends: tuple[str, ...]
    description: str
    aliases: tuple[str, ...]


@dataclass
class CanonicalTool:
    name: str
    registry_names: list[str]
    aliases: list[str]
    description: str
    backends: list[str]
    raw_names_lower: set[str] = field(init=False, repr=False)
    normalized_names: set[str] = field(init=False, repr=False)
    name_blob: str = field(init=False, repr=False)
    text_blob: str = field(init=False, repr=False)
    name_blob_padded: str = field(init=False, repr=False)
    text_blob_padded: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        raw_names = [self.name, *self.registry_names, *self.aliases]
        self.raw_names_lower = {item.lower() for item in raw_names if item}
        self.normalized_names = {normalize_text(item) for item in raw_names if item}
        self.name_blob = normalize_text(" ".join(raw_names))
        self.text_blob = normalize_text(
            " ".join(raw_names + [self.description] + self.backends)
        )
        self.name_blob_padded = f" {self.name_blob} " if self.name_blob else " "
        self.text_blob_padded = f" {self.text_blob} " if self.text_blob else " "


@dataclass
class DeduplicationRecord:
    canonical: str
    collapsed_registry_rows: list[str]
    declared_aliases: list[str]


@dataclass(frozen=True)
class CompiledRule:
    exact_name_checks: tuple[tuple[str, str], ...]
    name_terms: tuple[str, ...]
    text_terms: tuple[str, ...]
    excluded_terms: tuple[str, ...]


@dataclass(frozen=True)
class CompiledSubcategory:
    label: str
    rule: CompiledRule


@dataclass(frozen=True)
class CompiledCategory:
    id: str
    label: str
    fallback_subcategory: str
    rule: CompiledRule
    subcategories: tuple[CompiledSubcategory, ...]


@dataclass(frozen=True)
class CompiledTaxonomy:
    categories: tuple[CompiledCategory, ...]
    fallback_category_id: str | None
    min_major_category_size: int


@dataclass(frozen=True)
class CachePaths:
    root: Path
    repo_path: Path
    metadata_path: Path
    legacy_repo_path: Path
    legacy_stamp_path: Path


@dataclass(frozen=True)
class CacheMetadata:
    refreshed_at: datetime | None
    since_date: date | None


class ReportError(RuntimeError):
    pass


def warn(message: str) -> None:
    print(f"warning: {message}", file=sys.stderr)


def normalize_text(text: str) -> str:
    return NORMALIZE_RE.sub(" ", text.lower()).strip()


def compile_search_terms(values: Iterable[str]) -> tuple[str, ...]:
    compiled: list[str] = []
    seen: set[str] = set()
    for value in values:
        normalized = normalize_text(str(value))
        if normalized and normalized not in seen:
            seen.add(normalized)
            compiled.append(f" {normalized} ")
    return tuple(compiled)


def compile_exact_name_checks(values: Iterable[str]) -> tuple[tuple[str, str], ...]:
    compiled: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for value in values:
        lowered = str(value).lower().strip()
        normalized = normalize_text(str(value))
        key = (lowered, normalized)
        if normalized and key not in seen:
            seen.add(key)
            compiled.append(key)
    return tuple(compiled)


def compile_rule(rule: dict[str, Any]) -> CompiledRule:
    return CompiledRule(
        exact_name_checks=compile_exact_name_checks(rule.get("exact_names", [])),
        name_terms=compile_search_terms(rule.get("name_keywords", [])),
        text_terms=compile_search_terms(rule.get("keywords", [])),
        excluded_terms=compile_search_terms(rule.get("excluded_keywords", [])),
    )


def compile_taxonomy(taxonomy: dict[str, Any]) -> CompiledTaxonomy:
    categories: list[CompiledCategory] = []
    for category in taxonomy["categories"]:
        subcategories = tuple(
            CompiledSubcategory(
                label=subcategory["label"],
                rule=compile_rule(subcategory),
            )
            for subcategory in category.get("subcategories", [])
        )
        categories.append(
            CompiledCategory(
                id=category["id"],
                label=category["label"],
                fallback_subcategory=category.get(
                    "fallback_subcategory", "General tools"
                ),
                rule=compile_rule(category),
                subcategories=subcategories,
            )
        )

    return CompiledTaxonomy(
        categories=tuple(categories),
        fallback_category_id=taxonomy.get("fallback_category_id"),
        min_major_category_size=int(taxonomy.get("min_major_category_size", 4)),
    )


def run_capture(command: list[str], cwd: Path | None = None) -> str:
    process = subprocess.run(
        command,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )
    if process.returncode != 0:
        stderr = process.stderr.strip() or process.stdout.strip()
        raise ReportError(
            f"command failed ({process.returncode}): {' '.join(command)}\n{stderr}"
        )
    return process.stdout


def default_cache_dir() -> Path:
    override = os.environ.get(CACHE_DIR_ENV)
    if override:
        return Path(override).expanduser()

    if sys.platform == "darwin":
        base_dir = Path.home() / "Library" / "Caches"
    elif os.name == "nt":
        default_local_appdata = Path.home() / "AppData" / "Local"
        base_dir = Path(os.environ.get("LOCALAPPDATA", str(default_local_appdata)))
    else:
        default_xdg_cache = Path.home() / ".cache"
        base_dir = Path(os.environ.get("XDG_CACHE_HOME", str(default_xdg_cache)))
    return base_dir / "mise-registry-report"


def cache_paths(cache_root: Path | None = None) -> CachePaths:
    root = (cache_root or default_cache_dir()).expanduser()
    return CachePaths(
        root=root,
        repo_path=root / CACHE_REPO_NAME,
        metadata_path=root / CACHE_METADATA_NAME,
        legacy_repo_path=root / LEGACY_CACHE_REPO_NAME,
        legacy_stamp_path=root / LEGACY_CACHE_STAMP_NAME,
    )


def read_cache_metadata(paths: CachePaths) -> CacheMetadata | None:
    if paths.metadata_path.exists():
        try:
            payload = json.loads(paths.metadata_path.read_text())
        except json.JSONDecodeError as exc:
            raise ReportError(
                f"cache metadata is invalid JSON: {paths.metadata_path}: {exc}"
            ) from exc
        if not isinstance(payload, dict):
            raise ReportError(
                f"cache metadata must be an object: {paths.metadata_path}"
            )

        refreshed_raw = payload.get("refreshed_at")
        since_raw = payload.get("since_date")
        refreshed_at = None
        since_date = None
        if isinstance(refreshed_raw, str) and refreshed_raw:
            refreshed_at = datetime.fromisoformat(refreshed_raw)
            if refreshed_at.tzinfo is None:
                refreshed_at = refreshed_at.replace(tzinfo=timezone.utc)
        if isinstance(since_raw, str) and since_raw:
            since_date = date.fromisoformat(since_raw)
        return CacheMetadata(refreshed_at=refreshed_at, since_date=since_date)

    if paths.legacy_stamp_path.exists():
        refreshed_at = datetime.fromtimestamp(
            paths.legacy_stamp_path.stat().st_mtime,
            tz=timezone.utc,
        )
        return CacheMetadata(refreshed_at=refreshed_at, since_date=None)

    return None


def write_cache_metadata(
    paths: CachePaths,
    *,
    refreshed_at: datetime,
    since_date: date,
) -> None:
    paths.metadata_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "refreshed_at": refreshed_at.astimezone(timezone.utc).isoformat(),
        "since_date": since_date.isoformat(),
    }
    paths.metadata_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def cache_covers_since_date(
    metadata: CacheMetadata | None,
    requested_since_date: date,
) -> bool:
    return bool(
        metadata and metadata.since_date and metadata.since_date <= requested_since_date
    )


def cache_is_stale(
    metadata: CacheMetadata | None,
    *,
    now: datetime | None = None,
    max_age_days: int = CACHE_REFRESH_DAYS,
) -> bool:
    if metadata is None or metadata.refreshed_at is None:
        return True
    current_time = now or datetime.now(timezone.utc)
    return current_time - metadata.refreshed_at >= timedelta(days=max_age_days)


def cache_needs_refresh(
    metadata: CacheMetadata | None,
    *,
    requested_since_date: date,
    now: datetime | None = None,
    max_age_days: int = CACHE_REFRESH_DAYS,
    force_refresh: bool = False,
) -> bool:
    if force_refresh:
        return True
    if cache_is_stale(metadata, now=now, max_age_days=max_age_days):
        return True
    if not cache_covers_since_date(metadata, requested_since_date):
        return True
    return False


def history_since_date_for_window(end_date: date, months: int) -> date:
    return earliest_month_start(end_date, months)


def fallback_history_since_date() -> date:
    return date.today() - timedelta(days=DEFAULT_HISTORY_LOOKBACK_DAYS)


def git_command_for_repo(repo_path: Path) -> list[str]:
    repo_path = repo_path.expanduser()
    if (repo_path / ".git").is_dir():
        return ["git", "-C", str(repo_path)]
    if (
        repo_path.is_dir()
        and (repo_path / "HEAD").exists()
        and (repo_path / "objects").is_dir()
    ):
        return ["git", f"--git-dir={repo_path}"]
    raise ReportError(f"git repository not found or not supported at: {repo_path}")


def git_repository_has_head(repo_path: Path) -> bool:
    try:
        run_capture(git_command_for_repo(repo_path) + ["rev-parse", "--verify", "HEAD"])
    except ReportError:
        return False
    return True


def clone_cached_history_repo(
    repo_path: Path, remote_url: str, since_date: date
) -> None:
    if repo_path.exists():
        shutil.rmtree(repo_path)
    repo_path.parent.mkdir(parents=True, exist_ok=True)
    shallow_command = [
        "git",
        "clone",
        "--filter=blob:none",
        "--no-checkout",
        "--single-branch",
        f"--shallow-since={since_date.isoformat()}",
        remote_url,
        str(repo_path),
    ]
    try:
        run_capture(shallow_command)
    except ReportError as exc:
        message = str(exc)
        if "no commits selected for shallow requests" not in message:
            raise
        if repo_path.exists():
            shutil.rmtree(repo_path)
        run_capture(
            [
                "git",
                "clone",
                "--filter=blob:none",
                "--no-checkout",
                "--single-branch",
                remote_url,
                str(repo_path),
            ]
        )


def sync_local_branch_with_origin(repo_path: Path) -> None:
    branch_name = run_capture(
        git_command_for_repo(repo_path) + ["symbolic-ref", "--short", "HEAD"]
    ).strip()
    if not branch_name:
        return
    remote_ref = f"refs/remotes/origin/{branch_name}"
    local_ref = f"refs/heads/{branch_name}"
    run_capture(git_command_for_repo(repo_path) + ["show-ref", "--verify", remote_ref])
    run_capture(git_command_for_repo(repo_path) + ["update-ref", local_ref, remote_ref])


def ensure_origin_url(repo_path: Path, remote_url: str) -> None:
    try:
        current_origin = run_capture(
            git_command_for_repo(repo_path) + ["remote", "get-url", "origin"]
        ).strip()
    except ReportError:
        return
    if current_origin != remote_url:
        run_capture(
            git_command_for_repo(repo_path)
            + ["remote", "set-url", "origin", remote_url]
        )


def refresh_cached_history_repo(repo_path: Path, since_date: date) -> None:
    run_capture(
        git_command_for_repo(repo_path)
        + [
            "fetch",
            "--prune",
            "--update-shallow",
            "--filter=blob:none",
            "--no-tags",
            f"--shallow-since={since_date.isoformat()}",
            "origin",
        ]
    )
    sync_local_branch_with_origin(repo_path)


def ensure_cached_mise_mirror(
    *,
    cache_root: Path | None = None,
    remote_url: str = DEFAULT_MISE_REMOTE_URL,
    requested_since_date: date | None = None,
    now: datetime | None = None,
    max_age_days: int = CACHE_REFRESH_DAYS,
    force_refresh: bool = False,
) -> Path:
    paths = cache_paths(cache_root)
    requested_since_date = requested_since_date or fallback_history_since_date()
    paths.root.mkdir(parents=True, exist_ok=True)

    active_repo_path = paths.repo_path
    if not paths.repo_path.exists() and paths.legacy_repo_path.exists():
        active_repo_path = paths.legacy_repo_path

    metadata = read_cache_metadata(paths)

    if not active_repo_path.exists():
        clone_cached_history_repo(paths.repo_path, remote_url, requested_since_date)
        write_cache_metadata(
            paths,
            refreshed_at=now or datetime.now(timezone.utc),
            since_date=requested_since_date,
        )
        return paths.repo_path

    git_command_for_repo(active_repo_path)
    if not cache_needs_refresh(
        metadata,
        requested_since_date=requested_since_date,
        now=now,
        max_age_days=max_age_days,
        force_refresh=force_refresh,
    ):
        return active_repo_path

    try:
        if active_repo_path == paths.repo_path:
            ensure_origin_url(paths.repo_path, remote_url)
            refresh_cached_history_repo(paths.repo_path, requested_since_date)
            refreshed_repo_path = paths.repo_path
        else:
            clone_cached_history_repo(paths.repo_path, remote_url, requested_since_date)
            refreshed_repo_path = paths.repo_path
        write_cache_metadata(
            paths,
            refreshed_at=now or datetime.now(timezone.utc),
            since_date=requested_since_date,
        )
        return refreshed_repo_path
    except ReportError as exc:
        if not git_repository_has_head(active_repo_path):
            raise ReportError(
                f"cached mise history at {active_repo_path} is unusable and refresh failed: {exc}"
            ) from exc
        warn(
            f"failed to refresh cached mise history at {active_repo_path}; using stale cache"
        )
        return active_repo_path


def load_registry_entries(registry_json_path: Path | None) -> list[RegistryEntry]:
    if registry_json_path is not None:
        payload = registry_json_path.read_text()
    else:
        payload = run_capture(["mise", "registry", "--json"])

    try:
        raw_entries = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise ReportError(f"could not parse registry JSON: {exc}") from exc

    if not isinstance(raw_entries, list):
        raise ReportError("registry JSON must be a list of tool entries")

    entries: list[RegistryEntry] = []
    for raw in raw_entries:
        if not isinstance(raw, dict):
            raise ReportError("registry entry must be an object")
        short = str(raw.get("short", "")).strip()
        if not short:
            raise ReportError("registry entry missing 'short'")
        backends = tuple(sorted({str(item) for item in raw.get("backends", [])}))
        description = str(raw.get("description") or "").strip()
        aliases = tuple(
            sorted({str(item) for item in raw.get("aliases", []) if str(item).strip()})
        )
        entries.append(
            RegistryEntry(
                short=short,
                backends=backends,
                description=description,
                aliases=aliases,
            )
        )
    return entries


def entry_fingerprint(entry: RegistryEntry) -> tuple[tuple[str, ...], str]:
    return entry.backends, normalize_text(entry.description)


def choose_canonical_name(
    group_names: Iterable[str], entries_by_short: dict[str, RegistryEntry]
) -> str:
    names = sorted(set(group_names))

    def candidate_key(name: str) -> tuple[int, int, int, int, str]:
        entry = entries_by_short[name]
        group_alias_hits = sum(
            1 for alias in entry.aliases if alias in names and alias != name
        )
        suffix_penalty = int(name.endswith(SUFFIX_PENALTIES))
        return (-group_alias_hits, suffix_penalty, -len(entry.aliases), len(name), name)

    return sorted(names, key=candidate_key)[0]


def build_canonical_tools(
    entries: list[RegistryEntry],
) -> tuple[list[CanonicalTool], list[DeduplicationRecord]]:
    entries_by_short = {entry.short: entry for entry in entries}
    grouped_by_fingerprint: dict[tuple[tuple[str, ...], str], list[str]] = defaultdict(
        list
    )
    for entry in entries:
        grouped_by_fingerprint[entry_fingerprint(entry)].append(entry.short)

    canonical_tools: list[CanonicalTool] = []
    transparency_records: list[DeduplicationRecord] = []

    for group_names in grouped_by_fingerprint.values():
        ordered_group = sorted(set(group_names))
        canonical_name = choose_canonical_name(ordered_group, entries_by_short)
        group_entries = [entries_by_short[name] for name in ordered_group]
        description = next(
            (entry.description for entry in group_entries if entry.description), ""
        )
        backends = sorted(
            {backend for entry in group_entries for backend in entry.backends}
        )
        explicit_aliases = sorted(
            {
                alias
                for entry in group_entries
                for alias in entry.aliases
                if alias and alias != canonical_name
            }
        )
        collapsed_rows = [name for name in ordered_group if name != canonical_name]
        aliases = sorted({*explicit_aliases, *collapsed_rows})

        canonical_tools.append(
            CanonicalTool(
                name=canonical_name,
                registry_names=ordered_group,
                aliases=aliases,
                description=description,
                backends=backends,
            )
        )

        if aliases:
            transparency_records.append(
                DeduplicationRecord(
                    canonical=canonical_name,
                    collapsed_registry_rows=collapsed_rows,
                    declared_aliases=[
                        alias
                        for alias in explicit_aliases
                        if alias not in collapsed_rows
                    ],
                )
            )

    canonical_tools.sort(key=lambda tool: tool.name)
    transparency_records.sort(key=lambda record: record.canonical)
    return canonical_tools, transparency_records


def load_taxonomy(path: Path) -> dict[str, Any]:
    try:
        taxonomy = json.loads(path.read_text())
    except FileNotFoundError as exc:
        raise ReportError(f"taxonomy file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ReportError(f"taxonomy file is invalid JSON: {exc}") from exc

    if not isinstance(taxonomy, dict) or "categories" not in taxonomy:
        raise ReportError("taxonomy file must contain a top-level 'categories' array")
    return taxonomy


def score_rule(tool: CanonicalTool, rule: CompiledRule) -> int:
    score = 0
    for lowered, normalized in rule.exact_name_checks:
        if lowered in tool.raw_names_lower or normalized in tool.normalized_names:
            score += 12

    for term in rule.name_terms:
        if term in tool.name_blob_padded:
            score += 5

    for term in rule.text_terms:
        if term in tool.text_blob_padded:
            score += 3

    for term in rule.excluded_terms:
        if term in tool.text_blob_padded:
            score -= 5

    return score


def categorize_tools(
    tools: list[CanonicalTool], taxonomy: CompiledTaxonomy
) -> OrderedDict[str, dict[str, Any]]:
    categories = taxonomy.categories
    grouped: OrderedDict[str, dict[str, Any]] = OrderedDict()
    category_lookup = {category.id: category for category in categories}
    for category in categories:
        grouped[category.id] = {
            "label": category.label,
            "subcategories": defaultdict(list),
            "fallback_subcategory": category.fallback_subcategory,
        }

    for tool in tools:
        best_category: CompiledCategory | None = None
        best_subcategory: CompiledSubcategory | None = None
        best_score = NEGATIVE_SCORE
        best_sub_score = NEGATIVE_SCORE

        for category in categories:
            category_score = score_rule(tool, category.rule)
            chosen_subcategory = None
            chosen_sub_score = NEGATIVE_SCORE
            for subcategory in category.subcategories:
                sub_score = score_rule(tool, subcategory.rule)
                if sub_score > chosen_sub_score:
                    chosen_sub_score = sub_score
                    chosen_subcategory = subcategory

            total_score = (category_score * 2) + max(chosen_sub_score, 0)
            if total_score > best_score:
                best_score = total_score
                best_sub_score = chosen_sub_score
                best_category = category
                best_subcategory = chosen_subcategory

        fallback_id = taxonomy.fallback_category_id
        if best_category is None or best_score <= 0:
            if not fallback_id or fallback_id not in category_lookup:
                raise ReportError("taxonomy fallback category is missing")
            best_category = category_lookup[fallback_id]
            best_subcategory = None
            best_sub_score = NEGATIVE_SCORE

        category_bucket = grouped[best_category.id]
        if best_subcategory is not None and best_sub_score > 0:
            sub_label = best_subcategory.label
        else:
            sub_label = category_bucket["fallback_subcategory"]
        category_bucket["subcategories"][sub_label].append(tool)

    fallback_id = taxonomy.fallback_category_id
    if fallback_id and fallback_id in grouped:
        fallback_bucket = grouped[fallback_id]
        small_category_ids = []
        for category_id, bucket in grouped.items():
            if category_id == fallback_id:
                continue
            total = sum(len(items) for items in bucket["subcategories"].values())
            if 0 < total < taxonomy.min_major_category_size:
                small_category_ids.append(category_id)
        for category_id in small_category_ids:
            bucket = grouped[category_id]
            merged_subcategory_name = f"Merged from {bucket['label']}"
            for tools_in_subcategory in bucket["subcategories"].values():
                fallback_bucket["subcategories"][merged_subcategory_name].extend(
                    tools_in_subcategory
                )
            grouped.pop(category_id)

    for bucket in grouped.values():
        for tools_in_subcategory in bucket["subcategories"].values():
            tools_in_subcategory.sort(key=lambda tool: tool.name)

    return grouped


def month_sequence(end_date: date, months: int) -> list[str]:
    if months < 1:
        raise ReportError("months must be at least 1")

    year = end_date.year
    month = end_date.month
    values: list[str] = []
    for _ in range(months):
        values.append(f"{year:04d}-{month:02d}")
        month -= 1
        if month == 0:
            month = 12
            year -= 1
    values.reverse()
    return values


def earliest_month_start(end_date: date, months: int) -> date:
    oldest = month_sequence(end_date, months)[0]
    year, month = [int(part) for part in oldest.split("-")]
    return date(year, month, 1)


def empty_history(months: list[str]) -> OrderedDict[str, dict[str, set[str]]]:
    return OrderedDict((month, {"added": set(), "removed": set()}) for month in months)


def tool_name_from_registry_path(path: str) -> str | None:
    if not path.startswith("registry/") or not path.endswith(".toml"):
        return None
    return Path(path).stem


def apply_history_change(
    history: OrderedDict[str, dict[str, set[str]]],
    month: str,
    added: Iterable[str] = (),
    removed: Iterable[str] = (),
) -> None:
    if month not in history:
        return
    history[month]["added"].update(item for item in added if item)
    history[month]["removed"].update(item for item in removed if item)


def parse_git_history_output(
    text: str, months: list[str]
) -> OrderedDict[str, dict[str, set[str]]]:
    history = empty_history(months)
    current_month: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("__DATE__ "):
            current_month = line.split(" ", 1)[1]
            continue
        if current_month is None or current_month not in history:
            continue
        parts = line.split("\t")
        status = parts[0]
        if status == "A" and len(parts) >= 2:
            tool = tool_name_from_registry_path(parts[1])
            apply_history_change(history, current_month, added=[tool] if tool else [])
        elif status == "D" and len(parts) >= 2:
            tool = tool_name_from_registry_path(parts[1])
            apply_history_change(history, current_month, removed=[tool] if tool else [])
        elif status.startswith("R") and len(parts) >= 3:
            old_tool = tool_name_from_registry_path(parts[1])
            new_tool = tool_name_from_registry_path(parts[2])
            apply_history_change(
                history,
                current_month,
                added=[new_tool] if new_tool else [],
                removed=[old_tool] if old_tool else [],
            )
    return history


def collect_history_from_git_repository(
    repo_path: Path, end_date: date, months: int
) -> OrderedDict[str, dict[str, set[str]]]:
    git_command = git_command_for_repo(repo_path)
    since_date = history_since_date_for_window(end_date, months)
    history_text = run_capture(
        git_command
        + [
            "--no-pager",
            "log",
            f"--since={since_date.isoformat()}",
            "--name-status",
            "--diff-filter=ADR",
            "--date=format:%Y-%m",
            "--pretty=format:__DATE__ %cd",
            "--",
            "registry",
        ]
    )
    return parse_git_history_output(history_text, month_sequence(end_date, months))


def history_from_json(
    path: Path, months: list[str]
) -> OrderedDict[str, dict[str, set[str]]]:
    try:
        payload = json.loads(path.read_text())
    except FileNotFoundError as exc:
        raise ReportError(f"history JSON not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ReportError(f"history JSON is invalid: {exc}") from exc

    history = empty_history(months)
    data = (
        payload.get("months")
        if isinstance(payload, dict) and "months" in payload
        else payload
    )

    if isinstance(data, dict):
        for month, values in data.items():
            if month not in history or not isinstance(values, dict):
                continue
            apply_history_change(
                history, month, values.get("added", []), values.get("removed", [])
            )
        return history

    if isinstance(data, list):
        for item in data:
            if not isinstance(item, dict):
                continue
            month = str(item.get("month", ""))
            apply_history_change(
                history, month, item.get("added", []), item.get("removed", [])
            )
        return history

    raise ReportError("history JSON must be a month map or a list of month records")


def http_api_json(endpoint: str) -> Any:
    url = endpoint
    if not endpoint.startswith("http://") and not endpoint.startswith("https://"):
        url = f"https://api.github.com/{endpoint.lstrip('/')}"

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "mise-registry-report",
    }
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib_request.Request(url, headers=headers)
    try:
        with urllib_request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib_error.URLError as exc:
        raise ReportError(f"https request failed for {url}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ReportError(
            f"https response was not valid JSON for {url}: {exc}"
        ) from exc


def github_api_json(endpoint: str) -> Any:
    gh_error: str | None = None
    if shutil.which("gh"):
        try:
            return json.loads(run_capture(["gh", "api", endpoint]))
        except (ReportError, json.JSONDecodeError) as exc:
            gh_error = str(exc)

    try:
        return http_api_json(endpoint)
    except ReportError as exc:
        if gh_error:
            raise ReportError(
                f"GitHub API failed via gh and HTTPS: {gh_error}; {exc}"
            ) from exc
        raise


def collect_history_from_github_api(
    end_date: date, months: int
) -> OrderedDict[str, dict[str, set[str]]]:
    since_date = (
        history_since_date_for_window(end_date, months).isoformat() + "T00:00:00Z"
    )
    months_list = month_sequence(end_date, months)
    history = empty_history(months_list)
    page = 1

    while True:
        endpoint = f"repos/jdx/mise/commits?path=registry&since={since_date}&per_page=100&page={page}"
        commits = github_api_json(endpoint)
        if not commits:
            break
        for commit in commits:
            sha = commit.get("sha")
            commit_date = commit.get("commit", {}).get("committer", {}).get("date", "")
            if not sha or len(commit_date) < 7:
                continue
            month = commit_date[:7]
            if month not in history:
                continue
            detail = github_api_json(f"repos/jdx/mise/commits/{sha}")
            added: list[str] = []
            removed: list[str] = []
            for file_info in detail.get("files", []):
                filename = file_info.get("filename", "")
                tool_name = tool_name_from_registry_path(filename)
                status = file_info.get("status")
                if status == "added" and tool_name:
                    added.append(tool_name)
                elif status == "removed" and tool_name:
                    removed.append(tool_name)
                elif status == "renamed":
                    previous_tool = tool_name_from_registry_path(
                        file_info.get("previous_filename", "")
                    )
                    if previous_tool:
                        removed.append(previous_tool)
                    if tool_name:
                        added.append(tool_name)
            apply_history_change(history, month, added, removed)
        if len(commits) < 100:
            break
        page += 1

    return history


def collect_history(
    *,
    history_json_path: Path | None,
    mise_repo_path: Path | None,
    end_date: date,
    months: int,
    skip_history: bool,
    cache_root: Path | None = None,
    cache_remote_url: str = DEFAULT_MISE_REMOTE_URL,
    cache_refresh_days: int = CACHE_REFRESH_DAYS,
    force_refresh_cache: bool = False,
) -> OrderedDict[str, dict[str, set[str]]]:
    months_list = month_sequence(end_date, months)
    if skip_history:
        return empty_history(months_list)
    if history_json_path is not None:
        return history_from_json(history_json_path, months_list)
    if mise_repo_path is not None:
        return collect_history_from_git_repository(mise_repo_path, end_date, months)

    cache_error: ReportError | None = None
    requested_since_date = history_since_date_for_window(end_date, months)
    try:
        cached_repo_path = ensure_cached_mise_mirror(
            cache_root=cache_root,
            remote_url=cache_remote_url,
            requested_since_date=requested_since_date,
            max_age_days=cache_refresh_days,
            force_refresh=force_refresh_cache,
        )
        return collect_history_from_git_repository(cached_repo_path, end_date, months)
    except ReportError as exc:
        cache_error = exc
        warn("cached local history unavailable; falling back to GitHub API")

    try:
        return collect_history_from_github_api(end_date, months)
    except ReportError as exc:
        if cache_error is not None:
            raise ReportError(
                f"could not use cached local history or GitHub API: {cache_error}; {exc}"
            ) from exc
        raise


def format_code_list(items: Iterable[str]) -> str:
    values = sorted(set(items))
    if not values:
        return "none"
    return ", ".join(f"`{item}`" for item in values)


def render_markdown(
    *,
    grouped_categories: OrderedDict[str, dict[str, Any]],
    transparency_records: list[DeduplicationRecord],
    history: OrderedDict[str, dict[str, set[str]]],
    registry_row_count: int,
    canonical_tool_count: int,
    generated_on: date,
) -> str:
    non_empty_categories = [
        (category_id, bucket)
        for category_id, bucket in grouped_categories.items()
        if sum(len(items) for items in bucket["subcategories"].values()) > 0
    ]

    lines: list[str] = [
        "# Mise registry report",
        "",
        f"Generated from `mise registry --json` on {generated_on.isoformat()}.",
        "",
        "## Executive summary",
        "",
        f"- Canonical tools in the main inventory: {canonical_tool_count}",
        f"- Registry rows processed: {registry_row_count}",
        f"- Collapsed duplicate or alias rows: {registry_row_count - canonical_tool_count}",
        f"- Major categories in the final report: {len(non_empty_categories)}",
        f"- Months covered in the history section: {len(history)}",
        "",
        "## Category overview",
        "",
        "| Major category | Tools | Sub-categories |",
        "| --- | ---: | ---: |",
    ]

    for _, bucket in non_empty_categories:
        total_tools = sum(len(items) for items in bucket["subcategories"].values())
        populated_subcategories = sum(
            1 for items in bucket["subcategories"].values() if items
        )
        lines.append(
            f"| {bucket['label']} | {total_tools} | {populated_subcategories} |"
        )

    lines.extend(["", "## Registry by major category", ""])

    for _, bucket in non_empty_categories:
        subcategory_items = [
            (label, items) for label, items in bucket["subcategories"].items() if items
        ]
        subcategory_items.sort(key=lambda item: (-len(item[1]), item[0]))
        total_tools = sum(len(items) for _, items in subcategory_items)
        lines.append("<details open>")
        lines.append(
            f"<summary><strong>{bucket['label']}</strong> ({total_tools} tools)</summary>"
        )
        lines.append("")
        for subcategory_label, tools in subcategory_items:
            lines.append(f"### {subcategory_label} ({len(tools)})")
            for tool in tools:
                description = tool.description or "No description supplied."
                alias_suffix = ""
                if tool.aliases:
                    alias_suffix = f" _(aliases: {format_code_list(tool.aliases)})_"
                lines.append(f"- `{tool.name}` — {description}{alias_suffix}")
            lines.append("")
        lines.append("</details>")
        lines.append("")

    lines.extend(["## Registry changes in the last 12 months", ""])
    for month in reversed(list(history.keys())):
        added = sorted(history[month]["added"])
        removed = sorted(history[month]["removed"])
        lines.append(f"### {month}")
        lines.append(f"- Added ({len(added)}): {format_code_list(added)}")
        lines.append(f"- Removed ({len(removed)}): {format_code_list(removed)}")
        lines.append("")

    lines.extend(["## Deduplicated and aliased tools", ""])
    if transparency_records:
        for record in transparency_records:
            details: list[str] = []
            if record.collapsed_registry_rows:
                details.append(
                    f"collapsed registry rows: {format_code_list(record.collapsed_registry_rows)}"
                )
            if record.declared_aliases:
                details.append(
                    f"declared aliases: {format_code_list(record.declared_aliases)}"
                )
            lines.append(f"- `{record.canonical}` — {'; '.join(details)}")
    else:
        lines.append("- No duplicate rows or aliases were collapsed.")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a categorized Markdown report from the current mise registry."
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Path to write the Markdown report. Defaults to stdout.",
    )
    parser.add_argument(
        "--taxonomy",
        type=Path,
        default=DEFAULT_TAXONOMY_PATH,
        help="Path to the taxonomy JSON file.",
    )
    parser.add_argument(
        "--registry-json",
        type=Path,
        help="Optional pre-fetched registry JSON. If omitted, the script runs `mise registry --json`.",
    )
    parser.add_argument(
        "--history-json",
        type=Path,
        help="Optional month-keyed history JSON used instead of live history collection.",
    )
    parser.add_argument(
        "--mise-repo",
        type=Path,
        help="Optional local clone of `jdx/mise` used for history extraction.",
    )
    parser.add_argument(
        "--history-cache-dir",
        type=Path,
        help="Override the user cache directory used for the automatic cached local history source.",
    )
    parser.add_argument(
        "--history-cache-refresh-days",
        type=int,
        default=CACHE_REFRESH_DAYS,
        help="Refresh cached local history when it is older than this many days.",
    )
    parser.add_argument(
        "--refresh-history-cache",
        action="store_true",
        help="Force a refresh of the automatic cached local history source before generating the report.",
    )
    parser.add_argument(
        "--months",
        type=int,
        default=12,
        help="Number of trailing months to summarize in the history section.",
    )
    parser.add_argument(
        "--end-date",
        default=date.today().isoformat(),
        help="Anchor date for the month window in YYYY-MM-DD format. Defaults to today.",
    )
    parser.add_argument(
        "--skip-history",
        action="store_true",
        help="Skip live history collection and render empty monthly history sections.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        end_date = date.fromisoformat(args.end_date)
    except ValueError as exc:
        raise SystemExit(f"invalid --end-date value: {args.end_date}") from exc

    try:
        entries = load_registry_entries(args.registry_json)
        canonical_tools, transparency_records = build_canonical_tools(entries)
        taxonomy = compile_taxonomy(load_taxonomy(args.taxonomy))
        grouped_categories = categorize_tools(canonical_tools, taxonomy)
        history = collect_history(
            history_json_path=args.history_json,
            mise_repo_path=args.mise_repo,
            end_date=end_date,
            months=args.months,
            skip_history=args.skip_history,
            cache_root=args.history_cache_dir,
            cache_refresh_days=args.history_cache_refresh_days,
            force_refresh_cache=args.refresh_history_cache,
        )
        markdown = render_markdown(
            grouped_categories=grouped_categories,
            transparency_records=transparency_records,
            history=history,
            registry_row_count=len(entries),
            canonical_tool_count=len(canonical_tools),
            generated_on=end_date,
        )
    except ReportError as exc:
        print(
            f"error: {exc}\n"
            "hint: the script automatically tries a cached local history source before GitHub API. "
            "You can also provide `--mise-repo /path/to/jdx/mise`, `--history-json path/to/history.json`, "
            "`--history-cache-dir /path/to/cache`, `--refresh-history-cache`, or `--skip-history`. "
            "Set `MISE_REGISTRY_REPORT_CACHE_DIR` to override the default cache location.",
            file=sys.stderr,
        )
        return 1

    if args.output:
        args.output.write_text(markdown)
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
