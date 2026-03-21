# mise-tools



[![Workflow Status](https://img.shields.io/github/actions/workflow/status/kpatryk/mise-tools/generate-registry-report.yml?label=report%20generation)](https://github.com/kpatryk/mise-tools/actions/workflows/generate-registry-report.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![pre-commit enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A comprehensive inventory and categorized analysis of the **mise registry** — transforming 900+ tools into an organized, deduplicated Markdown report with historical tracking.

## 📊 Latest Report

The **mise registry report** is automatically generated and updated **every Sunday at 2am UTC**. It organizes tools into 12 major categories with 60+ subcategories, includes monthly add/remove history, and provides full transparency on alias deduplication.

**[View the latest registry report →](registry-report.md)**

## Quick Links

- **📋 Registry Report**: [registry-report.md](registry-report.md) - The automatically generated inventory
- **🔄 Workflow Status**: [GitHub Actions](https://github.com/kpatryk/mise-tools/actions/workflows/generate-registry-report.yml)
- **📄 License**: [MIT License](LICENSE)

## How It Works

### Categorization System

The project uses a **taxonomy-based classification system** to organize tools from the mise registry into meaningful categories. Here's how it works:

- **Taxonomy Definition** (`references/taxonomy.json`): A structured ruleset that defines 12 major categories with 60+ subcategories. Each category includes:
  - **Keywords**: General terms matched against tool descriptions
  - **Name keywords**: Language/tool-specific identifiers (e.g., "python", "rust", "node")
  - **Exact names**: Precise tool name matches (e.g., "python", "cargo", "npm")

- **Scoring & Classification**: The `generate_report.py` script assigns each tool to a category based on matching rules:
  - Exact name matches score highest (12 points)
  - Name keyword matches score medium (5 points)
  - General keyword matches score lower (3 points)
  - Excluded keywords are penalized (-5 points)

- **Fallback Handling**: Tools that don't match any category rules are automatically placed in the **"Other cross-domain tools"** category, ensuring no tool is left uncategorized.

### Adding New Tools

When mise adds new tools to its registry:
- **No taxonomy updates required** — The report will still generate successfully
- **Unmatched new tools** are placed in the fallback category
- **Optional categorization** — To improve categorization for new tool types, update `references/taxonomy.json` with relevant keywords or exact names

The system is designed to handle a growing registry gracefully without breaking changes.

## Usage

### View the Latest Report (Recommended)

The report is automatically updated weekly and committed to the repository:

```bash
cat registry-report.md
```

Or view it directly on GitHub: [registry-report.md](registry-report.md)

### Generate a Report Manually

Generate a fresh report on your machine:

```bash
python scripts/generate_report.py --output registry-report.md
```

### Manual Trigger via GitHub Actions

You can manually trigger the workflow to generate a report immediately:

1. Go to [GitHub Actions](https://github.com/kpatryk/mise-tools/actions/workflows/generate-registry-report.yml)
2. Click "Run workflow"
3. The report will be generated and committed within a few minutes

### Dry Run (No History, Faster)

```bash
python scripts/generate_report.py --skip-history --output registry-report.md
```

For more options, see the [full skill documentation](https://github.com/kpatryk/mise-tools/blob/main/scripts/generate_report.py).

## What's Inside

- **📁 `scripts/`**: Core automation and report generation
  - **`generate_report.py`**: Main orchestrator that fetches the mise registry, applies taxonomic classification, deduplicates tools, collects history, and generates the markdown report

- **📁 `references/`**: Taxonomy and classification rules
  - **`taxonomy.json`**: Structured ruleset with 12 categories, 60+ subcategories, and keyword/name matching rules that drive tool classification

- **🔧 `.github/workflows/`**: CI/CD automation
  - **`generate-registry-report.yml`**: Scheduled workflow that runs every Sunday at 2am UTC, regenerates the report, and auto-commits changes

- **📋 `registry-report.md`**: The latest automatically generated tool inventory

## Key Features

- ✅ **Smart categorization** — Taxonomy-based matching with keyword scoring and fallback handling
- ✅ **Deduplicates aliases** — Collapses similar tool names and aliases into canonical entries
- ✅ **Organized categories** — 12 major categories with 60+ subcategories covering all tool types
- ✅ **Historical tracking** — Monthly add/remove statistics from mise repository git history
- ✅ **Transparent mapping** — Full deduplication records for verification and auditing
- ✅ **Auto-updated** — Weekly scheduled generation with automatic commits to main branch
- ✅ **Cacheable history** — Local git mirror caching for fast subsequent runs

## License

This project is licensed under the [MIT License](LICENSE).
