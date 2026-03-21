# Mise registry report

Generated from `mise registry --json` on 2026-03-21.

## Executive summary

- Canonical tools in the main inventory: 924
- Registry rows processed: 967
- Collapsed duplicate or alias rows: 43
- Major categories in the final report: 12
- Months covered in the history section: 12

## Category overview

| Major category | Tools | Sub-categories |
| --- | ---: | ---: |
| Languages and runtimes | 127 | 7 |
| Package and dependency managers | 188 | 6 |
| Build, test, and code quality | 74 | 6 |
| Web, frontend, and API development | 21 | 6 |
| Data, databases, and observability | 41 | 5 |
| Cloud, infrastructure, and DevOps | 163 | 6 |
| CI/CD, release, and automation | 34 | 5 |
| Security, identity, and cyber | 40 | 6 |
| Developer environment and CLI productivity | 153 | 6 |
| Platform, mobile, and specialized tooling | 15 | 5 |
| AI and developer assistants | 7 | 2 |
| Other cross-domain tools | 61 | 1 |

## Registry by major category

<details open>
<summary><strong>Languages and runtimes</strong> (127 tools)</summary>

### General languages and runtimes (40)
- `cue` — The home of the CUE language! Validate and define text-based and dynamic configuration
- `d2` — Modern diagram scripting language that turns text to diagrams
- `dart` — An approachable, portable, and productive language for high-quality apps on any platform
- `djinni` — Command-line tool that generates gluecode from a djinni-IDL file
- `dome` — DOME is a framework for making 2D games using the Wren programming language which can be played across platforms
- `elm` — Compiler for Elm, a functional language for reliable webapps
- `emsdk` — Emscripten is a complete compiler toolchain to WebAssembly, using LLVM, with a special focus on speed, size, and the Web platform
- `flatc` — The main compiler for FlatBuffers is called flatc and is used to convert schema definitions into generated code files for a variety of languages
- `go-containerregistry` — Go library and CLIs for working with container registries
- `go-getter` — Package for downloading things from a string URL using a variety of protocols
- `go-jira` — simple jira command line client in Go
- `go-jsonnet` — This an implementation of Jsonnet in pure Go
- `go-junit-report` — Convert Go test output to JUnit XML
- `go-sdk` — Install go sdk
- `go-swagger` — Swagger 2.0 implementation for go
- `grain` — The Grain compiler toolchain and CLI. Home of the modern web staple
- `harper-ls` — harper-ls is the Language Server Protocol frontend for Harper
- `httpie-go` — httpie-like HTTP client written in Go
- `koka` — Koka language compiler and interpreter
- `mint` — 🍃 A refreshing programming language for the front-end web
- `neko` — The Neko Virtual Machine
- `numbat` — A statically typed programming language for scientific computations with first class support for physical dimensions and units
- `odin` — Odin Programming Language
- `onyx` — The compiler and developer toolchain for Onyx
- `php` — popular general-purpose scripting language that is especially suited to web development. Fast, flexible and pragmatic, PHP powers everything from your blog to the most popular websites in the world
- `pkl` — A configuration as code language with rich validation and tooling
- `pre-commit` — A framework for managing and maintaining multi-language pre-commit hooks
- `protoc-gen-connect-go` — The Go implementation of Connect: Protobuf RPC that works
- `protoc-gen-go` — protoc-gen-go is a plugin for the Google protocol buffer compiler to generate Go code
- `ruby` — Ruby language
- `smithy` — Smithy is a language for defining services and SDKs
- `solidity` — Solidity, the Smart Contract Programming Language
- `sui` — ui, a next-generation smart contract platform with high throughput, low latency, and an asset-oriented programming model powered by the Move programming language
- `tinymist` — Tinymist is an integrated language service for Typst.
- `tomcat` — The Apache Tomcat® software is an open source implementation of the Jakarta Servlet, Jakarta Pages, Jakarta Expression Language, Jakarta WebSocket, Jakarta Annotations and Jakarta Authentication specifications. These specifications are part of the Jakarta EE platform
- `unison` — A friendly programming language from the future
- `vlang` — The V Programming Language. Simple, fast, safe, compiled. For developing maintainable software
- `wasmer` — The leading WebAssembly Runtime supporting WASI and Emscripten
- `wasmtime` — A lightweight WebAssembly runtime that is fast, secure, and standards-compliant
- `wren` — A command line tool for the Wren programming language _(aliases: `wren-cli`)_

### Functional and scripting languages (24)
- `babashka` — Native, fast starting Clojure interpreter for scripting
- `cabal` — Cabal(haskell): Common Architecture for Building Applications and Libraries
- `carp` — Carp Language
- `chezscheme` — Chez Scheme is both a programming language and an implementation of that language, with supporting tools and documentation
- `chicken` — CHICKEN is a compiler for the Scheme programming language
- `cowsay` — cowsay is a configurable talking cow, originally written in Perl by Tony Monroe
- `crystal` — Crystal: A language for humans and computers
- `dhall` — Maintainable configuration files (haskell)
- `elixir` — Elixir is a dynamic, functional language for building scalable and maintainable applications
- `elixir-ls` — A frontend-independent IDE 'smartness' server for Elixir. Implements the 'Language Server Protocol' standard and provides debugger support via the 'Debug Adapter Protocol'
- `erlang` — erlang
- `esy` — Easy package management for native Reason, OCaml and more
- `ghc` — The Glorious Glasgow Haskell Compiler.
- `ghcup` — GHCup is an installer for the general purpose language Haskell
- `gleam` — A friendly language for building type-safe, scalable systems
- `julia` — The Julia Programming Language
- `lua` — Lua language
- `lua-language-server` — A language server that offers Lua language support - programmed in Lua
- `luajit` — a Just-In-Time Compiler for Lua
- `luau` — A fast, small, safe, gradually typed embeddable scripting language derived from Lua
- `opam` — (ocaml) opam is a source-based package manager. It supports multiple simultaneous compiler installations, flexible package constraints, and a Git-friendly development workflow
- `perl` — self-contained, portable perl binaries
- `purerl` — Erlang backend for the PureScript compiler
- `stack` — The Haskell Tool Stack

### Systems languages (20)
- `cargo-binstall` — Binary installation for rust projects
- `clang` — Clang is an 'LLVM native' C/C++/Objective-C compiler, which aims to deliver amazingly fast compiles, extremely useful error and warning messages and to provide a platform for building great source level tools
- `coreutils` — Cross-platform Rust rewrite of the GNU coreutils
- `doggo` — :dog: Command-line DNS Client for Humans. Written in Golang
- `dprint` — Pluggable and configurable code formatting platform written in Rust
- `dust` — A more intuitive version of du in rust
- `foundry` — Foundry is a blazing fast, portable and modular toolkit for Ethereum application development written in Rust
- `go` — go lang (Builtin plugin)
- `lychee` — Fast, async, stream-based link checker written in Rust. Finds broken URLs and mail addresses inside Markdown, HTML, reStructuredText, websites and more
- `mdbook` — Create book from markdown files. Like Gitbook but implemented in Rust
- `nancy` — A tool to check for vulnerabilities in your Golang dependencies, powered by Sonatype OSS Index
- `protoc-gen-go-grpc` — This tool generates Go language bindings of services in protobuf definition files for gRPC
- `rust` — Rust language
- `rust-analyzer` — A Rust compiler front-end for IDEs
- `rustic` — rustic - fast, encrypted, and deduplicated backups powered by Rust
- `tinygo` — Go compiler for small places. Microcontrollers, WebAssembly (WASM/WASI), and command-line tools. Based on LLVM
- `tlrc` — A tldr client written in Rust
- `zig` — Zig is a general-purpose programming language and toolchain for maintaining robust, optimal and reusable software
- `zigmod` — A package manager for the Zig programming language
- `zls` — A Zig language server supporting Zig developers with features like autocomplete and goto definition

### JVM and Java ecosystem (18)
- `ant` — Apache Ant is a Java library and command-line tool whose mission is to drive processes described in build files as targets and extension points dependent upon each other
- `asciidoctorj` — AsciidoctorJ is the official library for running Asciidoctor on the JVM. Using AsciidoctorJ, you can convert AsciiDoc content or analyze the structure of a parsed AsciiDoc document from Java and other JVM languages
- `cljstyle` — A tool for formatting Clojure code
- `clojure` — The Clojure Programming Language
- `conduit` — Conduit streams data between data stores. Kafka Connect replacement. No JVM required
- `graalvm` — An advanced JDK with ahead-of-time Native Image compilation
- `groovy` — A flexible and extensible Java-like language for the JVM
- `java` — jdk java
- `jbang` — Lets Students, Educators and Professional Developers create, edit and run self-contained source-only Java programs with unprecedented ease
- `ki` — Kotlin Language Interactive Shell
- `kotlin` — Kotlin is a modern but already mature programming language designed to make developers happier. It's concise, safe, interoperable with Java and other languages, and provides many ways to reuse code between multiple platforms for productive programming
- `kscript` — Scripting enhancements for Kotlin
- `leiningen` — for automating Clojure projects without setting your hair on fire
- `micronaut` — A modern, JVM-based, full-stack framework for building modular, easily testable microservice and serverless applications
- `mvnd` — Apache Maven Daemon
- `scala` — Scala language
- `scala-cli` — Scala CLI is a command-line tool to interact with the Scala language. It lets you compile, run, test, and package your Scala code (and more!)
- `zprint` — Executables, uberjar, and library to beautifully format Clojure and Clojurescript source code and s-expressions

### Native and platform runtimes (16)
- `danger-swift` — Stop saying 'you forgot to …' in code review
- `dotnet` — .NET SDK
- `dotnet-core` — .Net Core
- `mockolo` — Efficient Mock Generator for Swift
- `periphery` — A tool to identify unused code in Swift projects
- `sourcery` — Meta-programming for Swift, stop writing boilerplate code
- `swift` — Swift Lang (Core)
- `swift-package-list` — A command-line tool to get all used Swift Package dependencies
- `swiftformat` — A command-line tool and Xcode Extension for formatting Swift code
- `swiftgen` — The Swift code generator for your assets, storyboards, Localizable.strings, … — Get rid of all String-based APIs!
- `tuist` — A toolchain to generate Xcode projects from Swift packages
- `xchtmlreport` — Xcode-like HTML report for Unit and UI Tests
- `xcodegen` — A Swift command line tool for generating your Xcode project
- `xcodes` — The best command-line tool to install and switch between multiple versions of Xcode
- `xcresultparser` — Parse the binary xcresult bundle from Xcode builds and testruns
- `xcsift` — Swift tool to parse and format xcodebuild output for coding agents

### JavaScript and TypeScript (6)
- `bun` — Bun is a fast JavaScript all-in-one toolkit
- `deno` — A modern runtime for JavaScript and TypeScript (Builtin plugin)
- `node` — Node.js® is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web apps, command line tools and scripts (Builtin plugin)
- `orval` — Generate type-safe TypeScript clients from OpenAPI specifications provided by https://orval.dev
- `protoc-gen-js` — This directory contains the JavaScript Protocol Buffers runtime library
- `purescript` — A strongly-typed language that compiles to JavaScript

### Python runtimes (3)
- `cookiecutter` — Create projects swiftly from cookiecutters (project templates) with this command-line utility. Ideal for generating Python package projects and more
- `python` — python language
- `ty` — An extremely fast Python type checker and language server, written in Rust

</details>

<details open>
<summary><strong>Package and dependency managers</strong> (188 tools)</summary>

### Multi-language and tool managers (158)
- `amazon-ecr-credential-helper` — Automatically gets credentials for Amazon ECR on docker push/docker pull
- `aqua` — Declarative CLI Version manager written in Go. Support Lazy Install, Registry, and continuous update with Renovate. CLI version is switched seamlessly
- `assh` — make your ssh client smarter
- `awsls` — A list command for AWS resources
- `awsrm` — A remove command for AWS resources
- `awsweeper` — A tool for cleaning your AWS account
- `bpkg` — Lightweight bash package manager
- `cidr-merger` — A simple command line tool to merge ip/ip cidr/ip range, supports IPv4/IPv6
- `clarinet` — Write, test and deploy high-quality smart contracts to the Stacks blockchain and Bitcoin
- `cmctl` — the command line utility that makes cert-manager'ing easier
- `colima` — Container runtimes on macOS (and Linux) with minimal setup
- `coredns` — CoreDNS: DNS and Service Discovery
- `crane` — Go library and CLIs for working with container registries
- `dasel` — Select, put and delete data from JSON, TOML, YAML, XML and CSV files with a single tool. Supports conversion between formats and can be used as a Go package
- `deck` — decK: Configuration management and drift detection for Kong
- `difftastic` — a structural diff that understands syntax
- `dive` — A tool for exploring each layer in a docker image
- `docker-slim` — minT(oolkit): Mint awesome, secure and production ready containers just the way you need them! Don't change anything in your container image and minify it by up to 30x (and for compiled languages even more) making it secure too! (free and open source)
- `docuum` — Docuum performs least recently used (LRU) eviction of Docker images
- `draft` — A day 0 tool for getting your app on k8s fast
- `dt` — dt - duct tape for your unix pipes
- `duf` — Disk Usage/Free Utility - a better 'df' alternative
- `dyff` — A diff tool for YAML files, and sometimes JSON
- `dynatrace-monaco` — Monaco—This is the native Dynatrace Configuration as Code tool. Monaco is also the recommended tool for migrating from Dynatrace Managed to Dynatrace SaaS
- `earthly` — Repeatable builds
- `editorconfig-checker` — A tool to verify that your files are in harmony with your .editorconfig
- `envcli` — Don't install Node, Go, ... locally - use containers you define within your project. If you have a new machine / other contributors you just have to install docker and envcli to get started
- `etcd` — Distributed reliable key-value store for the most critical data of a distributed system
- `evans` — Evans: more expressive universal gRPC client
- `ffmpeg` — A complete, cross-platform solution to record, convert and stream audio and video
- `fillin` — fill-in your command and execute
- `flamingo` — Flux Subsystem for Argo
- `fluttergen` — The Flutter code generator for your assets, fonts, colors, … — Get rid of all String-based APIs
- `flyctl` — Command line tools for fly.io services
- `func-e` — func-e (pronounced funky) makes running Envoy® easy
- `fzf` — :cherry_blossom: A command-line fuzzy finder
- `gam` — command line management for Google Workspace
- `gcc-arm-none-eabi` — Arm GNU Toolchain
- `ghorg` — Quickly clone an entire org/users repositories into one directory - Supports GitHub, GitLab, Bitbucket, and more
- `ghq` — Remote repository management made easy
- `github-markdown-toc` — Easy TOC creation for GitHub README.md
- `gitleaks` — Find secrets with Gitleaks
- `gitsign` — Keyless Git signing using Sigstore
- `gofumpt` — A stricter gofmt
- `gojq` — Pure Go implementation of jq
- `gomplate` — A flexible commandline tool for template rendering. Supports lots of local and remote datasources
- `gopass` — The slightly more awesome standard unix password manager for teams
- `granted` — The easiest way to access AWS
- `grex` — A command-line tool and library for generating regular expressions from user-provided test cases
- `has` — checks presence of various command line tools and their versions on the path
- `haxe` — Haxe - The Cross-Platform Toolkit
- `hcl2json` — Convert hcl2 to json
- `helm-cr` — Hosting Helm Charts via GitHub Pages and Releases
- `helm-ct` — CLI tool for linting and testing Helm charts
- `helm-diff` — A helm plugin that shows a diff explaining what a helm upgrade would change
- `helm-docs` — A tool for automatically generating markdown documentation for helm charts
- `hostctl` — Your dev tool to manage /etc/hosts like a pro
- `hub` — A command-line tool that makes git easier to use with GitHub
- `hugo` — The world’s fastest framework for building websites
- `hwatch` — A modern alternative to the watch command, records the differences in execution results and can check this differences at after
- `hygen` — The simple, fast, and scalable code generator that lives in your project
- `imgpkg` — Store application configuration files in Docker/OCI registries
- `istioctl` — Istio configuration command line utility for service operators to debug and diagnose their Istio mesh
- `jib` — jib is a general-purpose command-line utility for building Docker or OCI container images from file system content as well as JAR files
- `jiq` — jid on jq - interactive JSON query tool using jq expressions
- `jless` — jless is a command-line JSON viewer designed for reading, exploring, and searching through JSON data
- `jnv` — interactive JSON filter using jq
- `jqp` — A TUI playground to experiment with jq
- `k0sctl` — A bootstrapping and management tool for k0s clusters
- `k3d` — Little helper to run CNCF's k3s in Docker
- `k3sup` — bootstrap K3s over SSH in < 60s
- `kafkactl` — Command Line Tool for managing Apache Kafka
- `kcctl` — A modern and intuitive command line client for Kafka Connect
- `kconf` — Manage multiple kubeconfigs easily
- `kubecm` — Manage your kubeconfig more easily
- `kubecolor` — Colorize your kubectl output
- `kubectx` — Faster way to switch between clusters and namespaces in kubectl
- `kubent` — Easily check your clusters for use of deprecated APIs
- `kubevela` — The Modern Application Platform
- `kubie` — A more powerful alternative to kubectx and kubens
- `lab` — Lab wraps Git or Hub, making it simple to clone, fork, and interact with repositories on GitLab
- `libsql-server` — server mode of libSQL, which is a fork of SQLite that is both Open Source, and Open Contributions
- `lima` — Linux virtual machines, with a focus on running containers
- `loki-logcli` — LogCLI is a command-line tool for querying and exploring logs in Grafana Loki
- `lsd` — The next gen ls command
- `mage` — a Make/rake-like dev tool using Go
- `make` — GNU Make is a tool which controls the generation of executables and other non-source files of a program from the program's source files
- `mark` — Sync your markdown files with Confluence pages
- `mc` — Unix like utilities for object store (minio)
- `mdbook-linkcheck` — A backend for `mdbook` which will check your links for you
- `melange` — build APKs from source code
- `melt` — Backup and restore Ed25519 SSH keys with seed words 🫠
- `minify` — Go minifiers for web formats
- `minio` — MinIO AIStor is a high-performance S3-compatible object store licensed under the MinIO Commercial License
- `minishift` — Run OpenShift 3.x locally
- `mitmproxy` — mitmproxy is a free and open source interactive HTTPS proxy
- `mkcert` — A simple zero-config tool to make locally trusted development certificates with any names you'd like
- `mockery` — A mock code autogenerator for Go
- `mongodb` — MongoDB
- `nfpm` — nFPM is Not FPM - a simple deb, rpm and apk packager written in Go
- `nomad` — Nomad is an easy-to-use, flexible, and performant workload orchestrator that can deploy a mix of microservice, batch, containerized, and non-containerized applications. Nomad is easy to operate and scale and has native Consul and Vault integrations
- `nsc` — Tool for creating nkey/jwt based configurations
- `om` — General command line utility for working with VMware Tanzu Operations Manager
- `opsgenie-lamp` — OpsGenie Lamp with Go SDK
- `pachctl` — Data-Centric Pipelines and Data Versioning
- `pandoc` — Universal markup converter
- `peco` — Simplistic interactive filtering tool
- `podman` — Podman: A tool for managing OCI containers and pods
- `powershell-core` — PowerShell for every system _(aliases: `powershell`)_
- `psc-package` — A package manager for PureScript based on package sets
- `qdns` — A tiny command line DNS client with support for UDP, TCP, DoT, DoH, DoQ and ODoH
- `qsv` — Blazing-fast Data-Wrangling toolkit
- `reckoner` — Declaratively install and manage multiple Helm chart releases
- `redo` — Redo is the ultimate tool to create reusable functions from your history in an interactive way
- `regctl` — Docker and OCI Registry Client in Go and tooling using those libraries
- `regsync` — regsync is a registry synchronization utility used to update mirrors of OCI compatible container registries
- `restic` — Fast, secure, efficient backup program
- `revive` — ~6x faster, stricter, configurable, extensible, and beautiful drop-in replacement for golint
- `richgo` — Enrich `go test` outputs with text decorations
- `scarb` — The Cairo package manager
- `scie-pants` — Protects your Pants from the elements
- `semver` — semver bash implementation
- `sinker` — A tool to sync images from one container registry to another
- `skate` — A personal key value store
- `sloth` — Easy and simple Prometheus SLO (service level objectives) generator
- `soft-serve` — The mighty, self-hostable Git server for the command line
- `sopstool` — SOPS multi-file wrapper
- `spago` — 🍝 PureScript package manager and build tool
- `spruce` — Standalone, daemon-less, unprivileged Dockerfile and OCI compatible container image builder
- `sshuttle` — sshuttle: where transparent proxy meets VPN meets ssh
- `sver` — Version generator based on source code
- `svu` — semantic version utility
- `tfenv` — Terraform version manager
- `tfstate-lookup` — Lookup resource attributes in tfstate
- `tinytex` — A lightweight, cross-platform, portable, and easy-to-maintain LaTeX distribution based on TeX Live
- `titan` — Titan is an open source project for developers to manage their data like code
- `tokei` — Count your code, quickly
- `tree-sitter` — An incremental parsing system for programming tools
- `tridentctl` — Storage orchestrator for containers
- `tsuru` — tsuru-client is a tsuru command line tool for application developers
- `updatecli` — A Declarative Dependency Management tool
- `upt` — Universal Package-management Tool for any OS
- `upx` — UPX - the Ultimate Packer for eXecutables
- `v` — V - https://vlang.io
- `vals` — Helm-like configuration values loader with support for various sources
- `velad` — Lightweight KubeVela that runs as Daemon in single node with high availability
- `vendir` — Easy way to vendor portions of git repos, github releases, helm charts, docker image contents, etc. declaratively
- `viddy` — A modern watch command. Time machine and pager etc
- `wasm4` — Build retro games using WebAssembly for a fantasy console
- `websocat` — Command-line client for WebSockets, like netcat (or curl) for ws:// with advanced socat-like functions
- `xcbeautify` — A little beautifier tool for xcodebuild
- `yamlfmt` — An extensible command line tool or library to format yaml files
- `yamlscript` — YS — YAML Done Wisely
- `youtube-dl` — Command-line program to download videos from YouTube.com and other video sites
- `yt-dlp` — A feature-rich command-line audio/video downloader
- `ytt` — YAML templating tool that works on YAML structure instead of text
- `zephyr` — Tree shaking breeze for PureScript CoreFn AST
- `zola` — A fast static site generator in a single binary with everything built-in. https://www.getzola.org

### JavaScript package managers (14)
- `cspell` — A Spell Checker for Code!
- `firebase` — The Firebase Command Line Tools
- `json5` — JSON5 is an extension to the popular JSON file format that aims to be easier to write and maintain by hand (e.g. for config files). It is not intended to be used for machine-to-machine communication. (Keep using JSON or other file formats for that. 🙂)
- `lefthook` — Fast and powerful Git hooks manager for any type of projects
- `markdownlint-cli2` — A fast, flexible, configuration-based command-line interface for linting Markdown/CommonMark files with the markdownlint library
- `ni` — ni - use the right package manager
- `npm` — the package manager for JavaScript
- `pnpm` — Fast, disk space efficient package manager
- `portless` — Replace port numbers with stable, named .localhost URLs. For humans and agents.
- `purty` — PureScript pretty-printer
- `serverless` — Serverless Framework
- `wrangler` — A command line tool for building Cloudflare Workers
- `yarn` — Yarn is a package manager that doubles down as project manager. Whether you work on simple projects or industry monorepos, whether you're an open source developer or an enterprise user, Yarn has your back
- `zbctl` — zbctl is a command line interface designed to create and read resources inside zeebe broker.

### Python package managers (7)
- `hatch` — Modern, extensible Python project management.
- `pdm` — A modern Python package and dependency manager supporting the latest PEP standards
- `pipenv` — Python Development Workflow for Humans
- `pipx` — No description supplied.
- `poetry` — Python packaging and dependency management made easy
- `rye` — a Hassle-Free Python Experience
- `uv` — An extremely fast Python package installer and resolver, written in Rust

### JVM and build artifact managers (4)
- `coursier` — Pure Scala Artifact Fetching
- `gradle` — Gradle is the open source build system of choice for Java, Android, and Kotlin developers
- `maven` — Apache Maven core
- `sbt` — sbt, the interactive build tool

### Ruby, PHP, and native ecosystem managers (3)
- `cocoapods` — CocoaPods is a dependency manager for Swift and Objective-C Cocoa projects
- `conan` — Decentralized, open-source (MIT), C/C++ package manager
- `jsonnet-bundler` — A jsonnet package manager _(aliases: `jb`)_

### General package and dependency managers (2)
- `micromamba` — Lightweight conda-compatible package manager
- `vfox` — A cross-platform and extendable version manager with support for Java, Node.js, Flutter, .Net & more

</details>

<details open>
<summary><strong>Build, test, and code quality</strong> (74 tools)</summary>

### Linters and formatters (34)
- `ast-grep` — A CLI tool for code structural search, lint and rewriting. Written in Rust
- `bibtex-tidy` — Cleaner and Formatter for BibTeX files
- `biome` — A toolchain for web projects, aimed to provide functionalities to maintain them. Biome offers formatter and linter, usable via CLI and LSP
- `black` — The uncompromising Python code formatter
- `cfn-lint` — Checks CloudFormation templates for practices and behaviour that could potentially be improved
- `checkmake` — experimental linter/analyzer for Makefiles
- `clj-kondo` — Static analyzer and linter for Clojure code that sparks joy
- `dockle` — Container Image Linter for Security, Helping build the Best-Practice Docker Image, Easy to start
- `dotenv-linter` — Lightning-fast linter for .env files. Written in Rust
- `ghalint` — GitHub Actions linter
- `golines` — A golang formatter that fixes long lines
- `hadolint` — Dockerfile linter, validate inline bash, written in Haskell
- `ktlint` — An anti-bikeshedding Kotlin linter with built-in formatter
- `ls-lint` — An extremely fast directory and filename linter - Bring some structure to your project filesystem
- `mago` — A blazing fast linter, formatter, and static analyzer for PHP, written in Rust
- `oxfmt` — This is the formatter for oxc.
- `oxlint` — This is the linter for oxc.
- `pint` — Prometheus rule linter/validator
- `protolint` — A pluggable linter and fixer to enforce Protocol Buffer style and conventions
- `regal` — Regal is a linter and language server for Rego, with the goal of making your Rego magnificent
- `ruff` — An extremely fast Python linter and code formatter, written in Rust
- `rumdl` — Markdown Linter and Formatter written in Rust
- `shellcheck` — ShellCheck, a static analysis tool for shell scripts
- `shfmt` — A shell parser, formatter, and interpreter with bash support; includes shfmt
- `spectral` — A flexible JSON/YAML linter for creating automated style guides, with baked in support for OpenAPI (v3.1, v3.0, and v2.0), Arazzo v1.0, as well as AsyncAPI v2.x
- `staticcheck` — Staticcheck - The advanced Go linter
- `stylua` — A Lua code formatter
- `superhtml` — HTML Validator, Formatter, LSP, and Templating Language Library
- `tflint` — A Pluggable Terraform Linter
- `tombi` — TOML Formatter / Linter / Language Server
- `typstyle` — Beautiful and reliable typst code formatter
- `vacuum` — vacuum is the worlds fastest OpenAPI 3, OpenAPI 2 / Swagger linter and quality analysis tool. Built in go, it tears through API specs faster than you can think. vacuum is compatible with Spectral rulesets and generates compatible reports
- `vale` — :pencil: A markup-aware linter for prose built with speed and extensibility in mind
- `yamllint` — A linter for YAML files

### Testing and QA (11)
- `allure` — Allure Report is a popular open source tool for visualizing the results of a test run
- `allurectl` — allurectl is the command line wrapper of Allure TestOps' API allowing you to upload the test results in real time from a build job, and managing entities on Allure TestOps side (test cases, launches, projects)
- `bats` — Bash Automated Testing System
- `cargo-insta` — A snapshot testing library for rust
- `ginkgo` — A Modern Testing Framework for Go
- `goconvey` — Go testing in the browser. Integrates with `go test`. Write behavioral tests in Go
- `goss` — Quick and Easy server testing/validation
- `gotestsum` — 'go test' runner with output optimized for humans, JUnit XML for CI integration, and a summary of the test results
- `kind` — Kubernetes IN Docker - local clusters for testing Kubernetes
- `shellspec` — A full-featured BDD unit testing framework for bash, ksh, zsh, dash and all POSIX shells
- `starknet-foundry` — Starknet testing framework (like Truffle, Hardhat and DappTools but for Starknet)

### Build systems and compilers (10)
- `bazel` — a fast, scalable, multi-language and extensible build system
- `bazelisk` — A user-friendly launcher for Bazel
- `buck2` — A fast, hermetic, multi-language build system
- `buildifier` — buildifier: For formatting BUILD, BUILD.bazel and BUCK files in a standard way
- `ccache` — ccache – a fast compiler cache
- `cmake` — CMake is a tool to manage building of source code. Originally, CMake was designed as a generator for various dialects of Makefile, today CMake generates modern buildsystems such as Ninja as well as project files for IDEs such as Visual Studio and Xcode
- `meson` — Meson is an open source build system meant to be both extremely fast, and, even more importantly, as user friendly as possible
- `ninja` — a small build system with a focus on speed
- `please` — High-performance extensible build system for reproducible multi-language builds
- `turbo` — Turborepo is a high-performance build system for JavaScript and TypeScript codebases.

### Code generation and schemas (7)
- `buf` — The best way of working with Protocol Buffers
- `clang-format` — format C/C++/Java/JavaScript/JSON/Objective-C/Protobuf/C# code
- `grpcurl` — Like cURL, but for gRPC: Command-line tool for interacting with gRPC servers
- `mssqldef` — Idempotent schema management for MsSQL and more
- `mysqldef` — Idempotent schema management for MySQL and more
- `protoc` — Protocol Buffers Compiler - Google's data interchange format _(aliases: `protobuf`)_
- `psqldef` — Idempotent schema management for PostgreSQL

### General build, test, and code quality tools (7)
- `container-structure-test` — validate the structure of your container images
- `golangci-lint` — Fast linters Runner for Go
- `golangci-lint-langserver` — golangci-lint language server
- `quarkus` — The quarkus command lets you create projects, manage extensions and do essential build and development tasks using the underlying project build tool
- `rebar` — Erlang build tool that makes it easy to compile and test Erlang applications and releases
- `trunk` — Trunk is a comprehensive code quality tool that runs linters, formatters, and security scanners to help maintain high-quality codebases (https://trunk.io)
- `zizmor` — Static analysis for GitHub Actions

### Benchmarking and profiling (5)
- `bombardier` — Fast cross-platform HTTP benchmarking tool written in Go
- `bottom` — Yet another cross-platform graphical process/system monitor
- `btrace` — BTrace - a safe, dynamic tracing tool for the Java platform
- `hyperfine` — A command-line benchmarking tool
- `k6` — A modern load testing tool, using Go and JavaScript

</details>

<details open>
<summary><strong>Web, frontend, and API development</strong> (21 tools)</summary>

### General web and API development (11)
- `harper-cli` — harper-cli is a small, experimental frontend for Harper. It can be used in any situation where you might need to check a large number of files automatically (like in continuous integration)
- `hurl` — Hurl, run and test HTTP requests with plain text
- `jmespath` — Command line interface to JMESPath - http://jmespath.org
- `nomad-pack` — Nomad Pack is a templating and packaging tool used with HashiCorp Nomad
- `oapi-codegen` — oapi-codegen is a command-line tool and library to convert OpenAPI specifications to Go code, be it server-side implementations, API clients, or simply HTTP models
- `oha` — Ohayou(おはよう), HTTP load generator, inspired by rakyll/hey with tui animation
- `pivnet` — CLI to interact with Tanzu Network API V2 interface
- `restish` — Restish is a CLI for interacting with REST-ish HTTP APIs with some nice features built-in
- `swag` — Automatically generate RESTful API documentation with Swagger 2.0 for Go
- `venom` — Manage and run your integration tests with efficiency - Venom run executors (script, HTTP Request, web, imap, etc... ) and assertions
- `xh` — Friendly and fast tool for sending HTTP requests

### GraphQL and API schemas (4)
- `apollo-router` — A configurable, high-performance routing runtime for Apollo Federation
- `apollo-rover` — The CLI for Apollo GraphOS
- `hasura-cli` — Hasura GraphQL Engine CLI
- `quicktype` — Generate types and converters from JSON, Schema, and GraphQL provided by https://quicktype.io

### HTTP and API tooling (3)
- `curlie` — The power of curl, the ease of use of httpie
- `glooctl` — The Cloud-Native API Gateway and AI Gateway
- `kiota` — OpenAPI based HTTP Client code generator

### Backend frameworks and web servers (1)
- `caddy` — Fast, multi-platform web server with automatic HTTPS

### Frontend frameworks (1)
- `astro` — CLI that makes it easy to create, test and deploy Airflow DAGs to Astronomer

### Web toolchains and styling (1)
- `prettier` — Prettier is an opinionated code formatter. It enforces a consistent style by parsing your code and re-printing it with its own rules that take the maximum line length into account, wrapping code when necessary

</details>

<details open>
<summary><strong>Data, databases, and observability</strong> (41 tools)</summary>

### Databases and data stores (22)
- `clickhouse` — ClickHouse® is a high-performance, column-oriented SQL database management system (DBMS) for online analytical processing (OLAP)
- `cloud-sql-proxy` — A utility for connecting securely to your Cloud SQL instances
- `cockroach` — A distributed SQL database designed for speed, scale, and survival
- `duckdb` — DuckDB is an analytical in-process SQL database management system
- `gomigrate` — Database migrations. CLI and Golang library
- `litestream` — Streaming replication for SQLite
- `mongosh` — The MongoDB Shell
- `mysql` — MySQL Database
- `octosql` — OctoSQL is a query tool that allows you to join, analyse and transform data from multiple databases and file formats using SQL
- `postgres` — PostgreSQL is a powerful, open source object-relational database system with over 35 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance
- `promtool` — The Prometheus monitoring system and time series database
- `redis` — Cache & in-memory datastore
- `schemacrawler` — Free database schema discovery and comprehension tool
- `skeema` — Declarative pure-SQL schema management for MySQL and MariaDB (Community Edition)
- `sqlc` — Generate type-safe code from SQL
- `sqlite` — SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world
- `sqlite3def` — The easiest idempotent SQLite3 Server schema management by SQL
- `supabase` — Supabase CLI. Manage postgres migrations, run Supabase locally, deploy edge functions. Postgres backups. Generating types from your database schema
- `tbls` — A CI-Friendly tool to document a database written in Go
- `tigerbeetle` — The financial transactions database designed for mission critical safety and performance.
- `trdsql` — CLI tool that can execute SQL queries on CSV, LTSV, JSON and TBLN. Can output to various formats
- `usql` — Universal command-line interface for SQL databases

### Monitoring, metrics, and tracing (9)
- `alp` — Access Log Profiler
- `cilium-hubble` — Hubble - Network, Service & Security Observability for Kubernetes using eBPF
- `ctop` — Top-like interface for container metrics
- `iamlive` — Generate an IAM policy from AWS calls using client-side monitoring (CSM) or embedded proxy
- `kubeshark` — The API traffic analyzer for Kubernetes providing real-time K8s protocol-level visibility, capturing and monitoring all traffic and payloads going in, out and across containers, pods, nodes and clusters. Inspired by Wireshark, purposely built for Kubernetes
- `lazyjournal` — TUI for journalctl, file system logs, as well Docker and Podman containers for quick viewing and filtering with fuzzy find, regex support (like fzf and grep) and coloring the output, written in Go with the gocui library
- `mimirtool` — Mimirtool is a command-line tool that operators and tenants can use to execute a number of common tasks that involve Grafana Mimir or Grafana Cloud Metrics
- `scorecard` — OpenSSF Scorecard - Security health metrics for Open Source
- `victoria-metrics` — VictoriaMetrics: fast, cost-effective monitoring solution and time series database

### Schema and migration tools (7)
- `atlas` — A modern tool for managing database schemas
- `atlas-community` — A modern tool for managing database schemas (Community Edition)
- `dbmate` — A lightweight, framework-agnostic database migration tool
- `flyway` — Flyway by Redgate • Database Migrations Made Easy
- `krab` — Krab is a migration and automation tool for PostgreSQL based on HCL syntax
- `liquibase` — Liquibase helps millions of developers track, version, and deploy database schema changes
- `tfmigrate` — A Terraform / OpenTofu state migration tool for GitOps

### General data, database, and observability tools (2)
- `elasticsearch` — Elasticsearch is an open source, distributed search and analytics engine built for speed, scale, and AI applications
- `spark` — Apache Spark - A unified analytics engine for large-scale data processing

### Data streaming and messaging (1)
- `redpanda-connect` — Fancy stream processing made operationally mundane _(aliases: `benthos`)_

</details>

<details open>
<summary><strong>Cloud, infrastructure, and DevOps</strong> (163 tools)</summary>

### Kubernetes and orchestration (92)
- `argo` — Argo Workflows CLI. Workflow engine for Kubernetes
- `argo-rollouts` — Progressive Delivery for Kubernetes
- `argocd` — Declarative continuous deployment for Kubernetes
- `aws-iam-authenticator` — A tool to use AWS IAM credentials to authenticate to a Kubernetes cluster
- `azure-kubelogin` — A Kubernetes credential (exec) plugin implementing azure authentication
- `binnacle` — An opinionated tool to interact with Kubernetes' Helm
- `brig` — Brigade CLI. Event-driven scripting for Kubernetes
- `calicoctl` — Cloud native networking and network security
- `cilium-cli` — CLI to install, manage & troubleshoot Kubernetes clusters running Cilium
- `clusterawsadm` — clusterawsadm provides helpers for bootstrapping Kubernetes Cluster API Provider AWS
- `clusterctl` — Home for Cluster API, a subproject of sig-cluster-lifecycle
- `copper` — A configuration file validator for Kubernetes
- `crictl` — crictl is a command-line interface for CRI-compatible container runtimes. You can use it to inspect and debug container runtimes and applications on a Kubernetes node
- `ctlptl` — Making local Kubernetes clusters fun and easy to set up
- `datree` — Prevent Kubernetes misconfigurations from reaching production (again  )! From code to cloud, Datree provides an E2E policy enforcement solution to run automatic checks for rule violations. See our docs: https://hub.datree.io
- `devspace` — DevSpace - The Fastest Developer Tool for Kubernetes  Automate your deployment workflow with DevSpace and develop software directly inside Kubernetes
- `flux2` — Open and extensible continuous delivery solution for Kubernetes. Powered by GitOps Toolkit
- `furyctl` — furyctl is the SIGHUP Distribution cluster lifecycle manager
- `gator` — Gatekeeper - Policy Controller for Kubernetes
- `grpc-health-probe` — A command-line tool to perform health-checks for gRPC applications in Kubernetes and elsewhere
- `helm` — The Kubernetes Package Manager
- `helm-ls` — Helm-ls is a helm language server protocol LSP implementation
- `helmfile` — Declaratively deploy your Kubernetes manifests, Kustomize configs, and Charts as Helm releases. Generate all-in-one manifests for use with ArgoCD
- `helmsman` — Helmsman is a Helm Charts (k8s applications) as Code tool which allows you to automate the deployment/management of your Helm charts from version controlled code
- `helmwave` — New  wave for @helm
- `jx` — Jenkins X provides automated CI+CD for Kubernetes with Preview Environments on Pull Requests using Cloud Native pipelines from Tekton
- `k2tf` — Kubernetes YAML to Terraform HCL converter
- `k3kcli` — K3k, Kubernetes in Kubernetes, is a tool that empowers you to create and manage isolated K3s clusters within your existing Kubernetes environment
- `k3s` — The certified Kubernetes distribution built for IoT & Edge computing
- `k9s` — Kubernetes CLI To Manage Your Clusters In Style
- `kapp` — kapp is a simple deployment tool focused on the concept of "Kubernetes application" — a set of resources with the same label
- `ko` — Build and deploy Go applications on Kubernetes
- `kompose` — Go from Docker Compose to Kubernetes
- `kops` — Kubernetes Operations (kops) - Production Grade K8s Installation, Upgrades, and Management
- `kpt` — Automate Kubernetes Configuration Editing
- `krew` — Find and install kubectl plugins
- `kube-capacity` — A simple CLI that provides an overview of the resource requests, limits, and utilization in a Kubernetes cluster
- `kube-controller-tools` — Tools to use with the controller-runtime libraries
- `kube-credential-cache` — Accelerator cache for kubernetes access
- `kube-linter` — KubeLinter is a static analysis tool that checks Kubernetes YAML files and Helm charts to ensure the applications represented in them adhere to best practices
- `kube-score` — Kubernetes object analysis with recommendations for improved reliability and security. kube-score actively prevents downtime and bugs in your Kubernetes YAML and Charts. Static code analysis for Kubernetes
- `kubebuilder` — Kubebuilder - SDK for building Kubernetes APIs using CRDs
- `kubeconform` — A FAST Kubernetes manifests validator, with support for Custom Resources
- `kubectl` — kubectl cli
- `kubectl-convert` — A plugin for Kubernetes command-line tool kubectl, which allows you to convert manifests between different API versions. This can be particularly helpful to migrate manifests to a non-deprecated api version with newer Kubernetes release
- `kubectl-kots` — KOTS provides the framework, tools and integrations that enable the delivery and management of 3rd-party Kubernetes applications, a.k.a. Kubernetes Off-The-Shelf (KOTS) Software
- `kubectl-kuttl` — Kubernetes Test TooL (kuttl) _(aliases: `kuttl`)_
- `kubectl-rolesum` — Summarize Kubernetes RBAC roles for the specified subjects _(aliases: `kubectl-bindrole`)_
- `kubefedctl` — kubefedctl controls a Kubernetes Cluster Federation
- `kubelogin` — kubectl plugin for Kubernetes OpenID Connect authentication (kubectl oidc-login)
- `kubemqctl` — Kubemqctl is a command line interface (CLI) for KubeMQ, Kubernetes Message Broker
- `kubeone` — Kubermatic KubeOne automate cluster operations on all your cloud, on-prem, edge, and IoT environments
- `kubergrunt` — Kubergrunt is a standalone go binary with a collection of commands to fill in the gaps between Terraform, Helm, and Kubectl. https://www.gruntwork.io
- `kubeseal` — A Kubernetes controller and tool for one-way encrypted Secrets
- `kubesec` — Security risk analysis for Kubernetes resources
- `kubespy` — Tools for observing Kubernetes resources in real time, powered by Pulumi
- `kubeval` — Validate your Kubernetes configuration files, supports multiple Kubernetes versions
- `kustomize` — Customization of kubernetes YAML configurations
- `kwokctl` — kwokctl is a CLI tool designed to streamline the creation and management of clusters, with nodes simulated by kwok
- `kwt` — Kubernetes Workstation Tools CLI
- `linkerd` — Ultralight, security-first service mesh for Kubernetes. Main repo for Linkerd 2.x
- `liqoctl` — Enable dynamic and seamless Kubernetes multi-cluster topologies
- `minikube` — Run Kubernetes locally
- `nelm` — Nelm is a Helm 4 alternative - it is a Kubernetes deployment tool that manages Helm Charts and deploys them to Kubernetes
- `nova` — Find outdated or deprecated Helm charts running in your cluster
- `okteto` — Develop your applications directly in your Kubernetes Cluster
- `omnictl` — CLI for Omni - SideroLabs' Kubernetes management platform for bare metal deployments
- `openshift-install` — Install an OpenShift 4.x cluster
- `operator-sdk` — SDK for building Kubernetes applications. Provides high level APIs, useful abstractions, and project scaffolding
- `pluto` — A cli tool to help discover deprecated apiVersions in Kubernetes
- `polaris` — Validation of best practices in your Kubernetes clusters
- `popeye` — A Kubernetes cluster resource sanitizer
- `rbac-lookup` — Easily find roles and cluster roles attached to any user, service account, or group name in your Kubernetes cluster
- `rke` — Rancher Kubernetes Engine (RKE), an extremely simple, lightning fast Kubernetes distribution that runs entirely within containers
- `setup-envtest` — This is a small tool that manages binaries for envtest. It can be used to download new binaries, list currently installed and available ones, and clean up versions
- `skaffold` — Easy and Repeatable Kubernetes Development
- `sonobuoy` — Sonobuoy is a diagnostic tool that makes it easier to understand the state of a Kubernetes cluster by running a set of Kubernetes conformance tests and other plugins in an accessible and non-destructive manner
- `starboard` — Kubernetes-native security toolkit
- `stern` — ⎈ Multi pod and container log tailing for Kubernetes -- Friendly fork of https://github.com/wercker/stern
- `talhelper` — A tool to help creating Talos kubernetes cluster
- `talosctl` — Talos is a modern OS for Kubernetes. talosctl is a CLI for out-of-band management of Kubernetes nodes created by Talos _(aliases: `talos`)_
- `tanka` — Flexible, reusable and concise configuration for Kubernetes
- `telepresence` — Local development against a remote Kubernetes or OpenShift cluster
- `terramate` — Open-source Infrastructure as Code (IaC) orchestration platform: GitOps workflows, orchestration, code generation, observability, drift detection, asset management, policies, Slack notifications, and more. Integrates with Terraform, OpenTofu, Terragrunt, Kubernetes, GitHub Actions, GitLab CI/CD, BitBucket Pipelines, and any other CI/CD platform
- `tilt` — Define your dev environment as code. For microservice apps on Kubernetes
- `timoni` — Timoni is a package manager for Kubernetes, powered by CUE and inspired by Helm
- `tonnage` — Tonnage is a small utility to summarize the resource capacity and allocation of a Kubernetes cluster
- `vcluster` — vCluster - Create fully functional virtual Kubernetes clusters - Each vcluster runs inside a namespace of the underlying k8s cluster. It's cheaper than creating separate full-blown clusters and it offers better multi-tenancy and isolation than regular namespaces
- `velero` — Backup and migrate Kubernetes applications and their persistent volumes
- `weave-gitops` — Command line utility for managing Kubernetes applications via GitOps
- `werf` — A solution for implementing efficient and consistent software delivery to Kubernetes facilitating best practices
- `zarf` — The Airgap Native Packager Manager for Kubernetes

### General cloud, infrastructure, and DevOps tools (28)
- `ansible-core` — ansible-core python package contains the core runtime and CLI tools, such as ansible and ansible-playbook _(aliases: `ansible-base`)_
- `bashbot` — A slack-bot written in golang for infrastructure/devops teams
- `consul` — Consul is a distributed, highly available, and data center aware solution to connect and configure applications across dynamic, distributed infrastructure
- `daytona` — Daytona is a Secure and Elastic Infrastructure for Running AI-Generated Code
- `depot` — Depot CLI, build your Docker images in the cloud
- `dotslash` — Simplified executable deployment
- `driftctl` — Detect, track and alert on infrastructure drift
- `dtm` — DevStream: the open-source DevOps toolchain manager (DTM)
- `ecspresso` — ecspresso is a deployment tool for Amazon ECS
- `hcloud` — A command-line interface for Hetzner Cloud
- `inlets` — Create inlets servers on the top cloud platforms
- `kbld` — kbld seamlessly incorporates image building and image pushing into your development and deployment workflows
- `kopia` — Kopia is a fast and secure open-source backup/restore tool that allows you to create encrypted snapshots of your data and save the snapshots to remote or cloud storage of your choice, to network-attached storage or server, or locally on your machine
- `kubefirst` — The Kubefirst CLI creates instant GitOps platforms that integrate some of the best tools in cloud native from scratch in minutes
- `levant` — An open source templating and deployment tool for HashiCorp Nomad jobs
- `mirrord` — Connect your local process and your cloud environment, and run local code in cloud conditions
- `oci` — Oracle Cloud Infrastructure CLI
- `powerpipe` — Powerpipe: Dashboards for DevOps. Visualize cloud configurations. Assess security posture against a massive library of benchmarks. Build custom dashboards with code
- `rclone` — "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Yandex Files
- `sccache` — sccache is ccache with cloud storage
- `sonar-scanner-cli` — Scanner CLI for SonarQube (Server, Cloud)
- `sst` — Build full-stack apps on your own infrastructure
- `teleport-community` — Teleport provides connectivity, authentication, access controls and audit for infrastructure (community version)
- `teleport-ent` — Teleport provides connectivity, authentication, access controls and audit for infrastructure (Enterprise version)
- `teller` — Cloud native secrets management for developers - never leave your command line for secrets
- `traefik` — The Cloud Native Application Proxy
- `vercel` — Build and deploy on the Vercel cloud
- `yor` — Extensible auto-tagger for your IaC files. The ultimate way to link entities in the cloud back to the codified resource which created it

### Infrastructure as code and provisioning (24)
- `ansible` — ansible python package contains the core runtime and CLI tools, such as ansible and ansible-playbook and extra modules, plugins, and roles
- `atmos` — Workflow automation tool for DevOps. Keep configuration DRY with hierarchical imports of configurations, inheritance, and WAY more. Native support for Terraform and Helmfile
- `checkov` — Prevent cloud misconfigurations and find vulnerabilities during build-time in infrastructure as code, container images and open source packages with Checkov by Bridgecrew
- `coder` — Provision remote development environments via Terraform
- `esc` — Pulumi ESC is a centralized, secure service for environments, secrets, and configuration management, optimized for multi-cloud infrastructures and applications
- `infracost` — Cloud cost estimates for Terraform in pull requests. Love your cloud bill
- `opentofu` — OpenTofu lets you declaratively manage your cloud infrastructure
- `packer` — Packer is a tool for creating identical machine images for multiple platforms from a single source configuration
- `pulumi` — Pulumi - Infrastructure as Code in any programming language
- `terradozer` — Terraform destroy without configuration files
- `terraform` — Terraform enables you to safely and predictably create, change, and improve infrastructure. It is an open source tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned
- `terraform-docs` — Generate documentation from Terraform modules in various output formats
- `terraform-ls` — Terraform Language Server
- `terraform-lsp` — Language Server Protocol for Terraform
- `terraform-validator` — A norms and conventions validator for Terraform
- `terraformer` — CLI tool to generate terraform files from existing infrastructure (reverse Terraform). Infrastructure to Code
- `terragrunt` — Terragrunt is a thin wrapper for Terraform that provides extra tools for working with multiple Terraform modules
- `terrascan` — Detect compliance and security violations across Infrastructure as Code to mitigate risk before provisioning cloud native infrastructure
- `tf-summarize` — A command-line utility to print the summary of the terraform plan
- `tfc-agent` — HCP Terraform Agents allow HCP Terraform to communicate with isolated, private, or on-premises infrastructure
- `tfctl` — A GitOps OpenTofu and Terraform controller for Flux
- `tfnotify` — A CLI command to parse Terraform execution result and notify it to GitHub
- `tfswitch` — A command line tool to switch between different versions of terraform (install with homebrew and more)
- `tfupdate` — Update version constraints in your Terraform configurations

### Cloud provider CLIs (11)
- `aks-engine` — AKS Engine deploys and manages Kubernetes clusters in Azure
- `aws-cli` — The AWS Command Line Interface (AWS CLI v2) is a unified tool that provides a consistent interface for interacting with all parts of Amazon Web Services _(aliases: `aws`, `awscli`)_
- `aws-copilot` — The AWS Copilot CLI is a tool for developers to build, release and operate production ready containerized applications on AWS App Runner, Amazon ECS, and AWS Fargate
- `aws-nuke` — Remove all the resources from an AWS account
- `awscli-local` — This package provides the awslocal command, which is a thin wrapper around the aws command line interface for use with LocalStack
- `azure` — azure-cli (az) _(aliases: `azure-cli`)_
- `doctl` — The official command line interface for the DigitalOcean API
- `gcloud` — GCloud CLI (Google Cloud SDK)
- `iam-policy-json-to-terraform` — Small tool to convert an IAM Policy in JSON format into a Terraform aws_iam_policy_document
- `okta-aws` — A CLI for having Okta as the IdP for AWS CLI operations _(aliases: `okta-aws-cli`)_
- `steampipe` — Use SQL to instantly query your cloud services (AWS, Azure, GCP and more). Open source CLI. No DB required

### Serverless and platform tooling (7)
- `aws-amplify` — The AWS Amplify CLI is a toolchain for simplifying serverless web and mobile development _(aliases: `amplify`)_
- `aws-sam` — CLI tool to build, test, debug, and deploy Serverless applications using AWS SAM _(aliases: `aws-sam-cli`)_
- `azure-functions-core-tools` — Command line tools for Azure Functions
- `balena` — The balena CLI is a Command Line Interface for balenaCloud or openBalena _(aliases: `balena-cli`)_
- `bosh` — The bosh CLI is the command line tool used for interacting with all things BOSH, from deployment operations to software release management
- `cf` — The official command line client for Cloud Foundry
- `fission` — Fast and Simple Serverless Functions for Kubernetes

### Ops automation and configuration (1)
- `chamber` — CLI for managing secrets

</details>

<details open>
<summary><strong>CI/CD, release, and automation</strong> (34 tools)</summary>

### General CI/CD, release, and automation tools (15)
- `committed` — Nitpicking commit history since beabf39
- `concourse` — Concourse is a container-based automation system written in Go
- `dagger` — A portable devkit for CI/CD pipelines
- `danger-js` — Danger runs during your CI process, and gives teams the chance to automate common code review chores
- `drone` — Command Line Tools for Drone CI
- `fly` — fly cli for concourse ci
- `imagemagick` — ImageMagick is a free, open-source software suite for creating, editing, converting, and displaying images. It supports 200+ formats and offers powerful command-line tools and APIs for automation, scripting, and integration across platforms
- `jreleaser` — Release projects quickly and easily with JReleaser
- `jsonschema` — The CLI for working with JSON Schema. Covers formatting, linting, testing, bundling, and more for both local development and CI/CD pipelines
- `lane` — lane is a task automation helper
- `pipectl` — The One CD for All {applications, platforms, operations}
- `release-plz` — Publish Rust crates from CI with a Release PR.
- `tiny` — rtx-tiny is mostly a fake plugin to check mise in CI
- `typos` — Source code spell checker
- `waypoint` — A tool to build, deploy, and release any application on any platform

### GitHub Actions and CI helpers (9)
- `act` — Run your GitHub Actions locally
- `action-validator` — Tool to validate GitHub Action and Workflow YAML files
- `actionlint` — :octocat: Static checker for GitHub Actions workflow files
- `auto-doc` — Github action that turns your reusable workflows and custom actions into easy to read markdown tables
- `entireio-cli` — Entire is a new developer platform that hooks into your git workflow to capture AI agent sessions on every push, unifying your code with its context and reasoning. _(aliases: `entire`)_
- `gemini-cli` — Gemini CLI, a command-line AI workflow tool that connects to your tools, understands your code and accelerates your workflows _(aliases: `gemini`)_
- `hledger-flow` — An hledger/ledger-cli workflow focusing on automated statement import and classification
- `pinact` — pinact is a CLI to edit GitHub Workflow and Composite action files and pin versions of Actions and Reusable Workflows. pinact can also update their versions and verify version annotations
- `specstory` — You don’t write prompts. You author intent. Enhance your AI development workflow with SpecStory

### Release automation and changelogs (6)
- `cargo-dist` — 📦 shippable application packaging
- `changie` — Automated changelog tool for preparing releases with lots of customization options
- `communique` — Editorialized release notes powered by AI
- `git-chglog` — CHANGELOG generator implemented in Go (Golang)
- `git-cliff` — A highly customizable Changelog Generator that follows Conventional Commit specifications
- `goreleaser` — Deliver Go binaries as fast and easily as possible

### Build pipelines and artifacts (2)
- `bazel-watcher` — Tools for building Bazel targets when source files change
- `buildpack` — CLI for building apps using Cloud Native Buildpacks _(aliases: `buildpacks`, `pack`)_

### Repository maintenance (2)
- `adr-tools` — Command-line tools for working with Architecture Decision Records
- `boilerplate` — A tool for generating files and folders ("boilerplate") from a set of templates

</details>

<details open>
<summary><strong>Security, identity, and cyber</strong> (40 tools)</summary>

### Secrets and identity (12)
- `1password` — Password manager developed by AgileBits Inc _(aliases: `1password-cli`, `op`)_
- `aws-sso` — A powerful tool for using AWS Identity Center for the CLI and web console
- `aws-vault` — A vault for securely storing and accessing AWS credentials in development environments
- `bitwarden` — Bitwarden CLI
- `bitwarden-secrets-manager` — CLI for interacting with the Bitwarden Secrets Manager
- `boundary` — Boundary enables identity-based access management for dynamic infrastructure
- `cloudflared` — cloudflared connects your machine or user identity to Cloudflare's global network
- `ggshield` — Detect and validate 500+ types of hardcoded secrets with advanced checks. Use it as a pre-commit hook, GitHub Action, or CLI for proactive secret detection and security.
- `gokey` — A simple vaultless password manager in Go
- `infisical` — The open source secret management platform: Sync secrets across your team/infrastructure and prevent secret leaks
- `ripsecrets` — A command-line tool to prevent committing secret keys into your source code
- `vault` — A tool for secrets management, encryption as a service, and privileged access management

### Cryptography and certificates (10)
- `age` — A simple, modern and secure encryption tool (and Go library) with small explicit keys, no config options, and UNIX-style composability
- `age-plugin-yubikey` — age-plugin-yubikey is a plugin for age clients like age and rage, which enables files to be encrypted to age identities stored on YubiKeys
- `agebox` — Age based repository file encryption gitops tool
- `borg` — Deduplicating archiver with compression and authenticated encryption
- `certstrap` — Tools to bootstrap CAs, certificate requests, and signed certificates
- `cfssl` — CFSSL: Cloudflare's PKI and TLS toolkit
- `cfssljson` — cfssljson: Takes the JSON output from Cloudflare's cfssl and multirootca programs and writes certificates, keys, CSRs, and bundles to disk.
- `cosign` — Code signing and transparency for containers and binaries
- `ejson` — EJSON is a small library to manage encrypted secrets using asymmetric encryption
- `sshi` — SSH CA Client/Server

### Vulnerability and policy scanning (10)
- `conform` — Policy enforcement for your pipelines
- `conftest` — Write tests against structured configuration data using the Open Policy Agent Rego query language
- `grype` — A vulnerability scanner for container images and filesystems
- `kyverno` — Cloud Native Policy Management
- `opa` — Open Policy Agent (OPA) is an open source, general-purpose policy engine
- `osv-scanner` — Vulnerability scanner written in Go which uses the data provided by https://osv.dev
- `semgrep` — Lightweight static analysis for many languages. Find bug variants with patterns that look like source code.
- `sentinel` — Sentinel is a policy as code tool that lets you control what users of HashiCorp products are allowed to do. It enforces policies proactively, preventing end users from deploying changes that are not allowed
- `tfsec` — Security scanner for your Terraform code
- `trivy` — Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more

### General security, identity, and cyber tools (4)
- `opengrep` — Static code analysis engine to find security issues in code
- `reg` — Docker registry v2 command line client and repo listing generator with security checks
- `snyk` — Snyk CLI scans and monitors your projects for security vulnerabilities
- `sops` — Simple and flexible tool for managing secrets

### Offensive security and reconnaissance (2)
- `amass` — In-depth attack surface mapping and asset discovery
- `chisel` — A fast TCP/UDP tunnel over HTTP

### Supply chain security (2)
- `apko` — Build OCI images from APK packages directly without Dockerfile
- `syft` — CLI tool and library for generating a Software Bill of Materials from container images and filesystems

</details>

<details open>
<summary><strong>Developer environment and CLI productivity</strong> (153 tools)</summary>

### General developer environment and CLI productivity (82)
- `amazon-ecs-cli` — The Amazon ECS CLI enables users to run their applications on ECS/Fargate using the Docker Compose file format, quickly provision resources, push/pull images in ECR, and monitor running applications on ECS/Fargate. _(aliases: `ecs-cli`)_
- `awsebcli` — The AWS Elastic Beanstalk Command Line Interface (EB CLI) is a tool that helps you deploy and manage your Elastic Beanstalk applications and environments. It also provides integration with Git
- `bosh-backup-and-restore` — BOSH Backup and Restore is a CLI utility for orchestrating the backup and restore of BOSH deployments and BOSH directors _(aliases: `bbr`)_
- `calendarsync` — Stateless CLI tool to sync calendars across different calendaring systems
- `cidrchk` — CLI tool for CIDR range operations (check, generate)
- `circleci` — Use CircleCI from the command line _(aliases: `circleci-cli`)_
- `codebuff` — Codebuff is a CLI tool that writes code for you
- `codefresh` — The Codefresh CLI provides a full and flexible interface to interact with Codefresh
- `codeql` — CodeQL CLI
- `copier` — A library and CLI app for rendering project templates
- `credhub` — CredHub CLI provides a command line interface to interact with CredHub servers
- `crossplane` — The Crossplane CLI extends kubectl with functionality to build, push, and install Crossplane packages _(aliases: `crossplane-cli`)_
- `cyclonedx` — CycloneDX CLI tool for SBOM analysis, merging, diffs and format conversions
- `dapr` — Command-line tools for Dapr
- `databricks-cli` — Databricks CLI
- `devcontainer-cli` — CLI for creating and configuring dev containers from devcontainer.json
- `docker-cli` — Docker CE CLI
- `doppler` — The official CLI for interacting with your Doppler secrets and configuration
- `dua` — View disk space usage and delete unwanted data, fast
- `eksctl` — The official CLI for Amazon EKS
- `envsubst` — Environment variables substitution for Go
- `fastfetch` — An actively maintained, feature-rich and performance oriented, neofetch like system information tool
- `flarectl` — A CLI application for interacting with a Cloudflare account. Powered by cloudflare-go
- `getenvoy` — historical CLI of getenvoy
- `gitconfig` — Cli to manage multiple gitconfigs with ease
- `github-cli` — GitHub’s official command line tool _(aliases: `gh`)_
- `glab` — gitlab cli
- `glen` — cli to export gitlab variables
- `glow` — Render markdown on the CLI, with pizzazz
- `graphite` — Code review for the age of AI
- `gwvault` — ansible-vault CLI reimplemented in go
- `hledger` — Robust, fast, intuitive plain text accounting tool with CLI, TUI and web interfaces
- `jfrog-cli` — Frog CLI is a client that provides a simple interface that automates access to the JFrog products
- `jj` — A Git-compatible VCS that is both simple and powerful _(aliases: `jujutsu`)_
- `jwt` — A super fast CLI tool to decode and encode JWTs built in Rust
- `kcl` — The KCL Command Line Interface (CLI)
- `kn` — Knative developer experience, docs, reference Knative CLI implementation
- `kpack` — A command line interface for interacting with kpack _(aliases: `kp`)_
- `localstack` — The LocalStack CLI packaged using pyinstaller
- `magika` — Fast and accurate AI powered file content types detection
- `mani` — CLI tool to help you manage repositories
- `marp-cli` — A CLI interface for Marp and Marpit based converters
- `mas` — Mac App Store command-line interface
- `nerdctl` — contaiNERD CTL - Docker-compatible CLI for containerd, with support for Compose, Rootless, eStargz, OCIcrypt, IPFS,
- `newrelic` — The New Relic Command Line Interface _(aliases: `newrelic-cli`)_
- `notation` — A CLI tool to sign and verify artifacts
- `oauth2c` — User-friendly OAuth2 CLI
- `oc` — OpenShift Client CLI (oc)
- `odo` — A fast, and iterative CLI tool for container-based application development
- `openfaas-cli` — Official CLI for OpenFaaS
- `opensearch-cli` — A full-featured command line interface (CLI) for OpenSearch
- `oras` — ORAS CLI
- `railway` — Railway CLI
- `rancher` — Rancher CLI
- `rpk` — Redpanda CLI and toolbox
- `saml2aws` — CLI tool which enables you to login and retrieve AWS temporary credentials using a SAML IDP
- `scaleway` — Command Line Interface for Scaleway _(aliases: `scaleway-cli`)_
- `scalingo-cli` — Command Line client for Scalingo PaaS
- `sd` — Intuitive find & replace CLI (sed alternative)
- `signadot` — Command-line interface for Signadot
- `slsa-verifier` — Verify provenance from SLSA compliant builders
- `soracom` — Provides `soracom` command, a command line tool for calling SORACOM APIs
- `spacectl` — Spacelift client and CLI
- `spin` — Spinnaker CLI
- `spring-boot` — Spring Boot CLI
- `step` — A zero trust swiss army knife for working with X509, OAuth, JWT, OATH OTP, etc
- `stripe` — A command-line tool for Stripe _(aliases: `stripe-cli`)_
- `tanzu` — The Tanzu Core CLI project provides the core functionality of the Tanzu CLI. The CLI is based on a plugin architecture where CLI command functionality can be delivered through independently developed plugin binaries
- `taplo` — A TOML toolkit written in Rust
- `tctl` — Temporal CLI
- `tekton` — A CLI for interacting with Tekton _(aliases: `tekton-cli`)_
- `temporal` — Temporal service and CLI
- `transifex` — The Transifex command-line client
- `typst` — A new markup-based typesetting system that is powerful and easy to learn
- `uaa` — CLI for UAA written in Go _(aliases: `uaa-cli`)_
- `upctl` — UpCloud command line client (upctl)
- `usage` — A specification for CLIs
- `vespa-cli` — The command-line tool for Vespa.ai.
- `vhs` — Your CLI home video recorder
- `vultr` — Official command line tool for Vultr services _(aliases: `vultr-cli`)_
- `wait-for-gh-rate-limit` — CLI to wait for github rate limits to reset if they are expired
- `yj` — CLI - Convert between YAML, TOML, JSON, and HCL. Preserves map order

### Shell and terminal UX (38)
- `atuin` — ✨ Magical shell history
- `bashly` — Bashly is a command line application (written in Ruby) that lets you generate feature-rich bash command line tools
- `carapace` — A multi-shell completion binary
- `codex` — Lightweight coding agent that runs in your terminal
- `crush` — The glamourous AI coding agent for your favourite terminal
- `desk` — A lightweight workspace manager for the shell
- `e1s` — E1S - Easily Manage AWS ECS Resources in Terminal(~k9s for ECS)
- `fx` — Command-line tool and terminal JSON viewer
- `gitui` — Blazing 💥 fast terminal-ui for git written in rust
- `gum` — A tool for glamorous shell scripts
- `heroku` — The Heroku Command Line Interface (CLI) is an essential part of using Heroku. With it, you can create and manage Heroku apps directly from the terminal _(aliases: `heroku-cli`)_
- `hishtory` — Your shell history: synced, queryable, and in context
- `jules` — Jules, the asynchronous coding agent from Google, in the terminal
- `lazygit` — simple terminal UI for git commands
- `lazyssh` — A terminal-based SSH manager inspired by lazydocker and k9s - Written in go
- `mermaid-ascii` — Render Mermaid graphs inside your terminal
- `neonctl` — Neon CLI tool. The Neon CLI is a command-line interface that lets you manage Neon Serverless Postgres directly from the terminal
- `oh-my-posh` — The most customizable and fastest prompt engine for any shell
- `opencode` — AI coding agent, built for the terminal
- `patat` — Terminal-based presentations using Pandoc
- `podman-tui` — Podman Terminal UI
- `powerline-go` — A beautiful and useful low-latency prompt for your shell, written in go
- `sampler` — Tool for shell commands execution, visualization and alerting. Configured with a simple YAML file
- `scooter` — Interactive find-and-replace in the terminal
- `shell2http` — Executing shell commands via HTTP server
- `starship` — The minimal, blazing-fast, and infinitely customizable prompt for any shell
- `superfile` — Pretty fancy and modern terminal file manager
- `tailpipe` — select * from logs! Tailpipe is an open source SIEM for instant log insights, powered by DuckDB. Analyze millions of events in seconds, right from your terminal
- `tirith` — Terminal security - catches homograph attacks, pipe-to-shell, ANSI injection
- `tmux` — tmux is a terminal multiplexer. It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal
- `trzsz-ssh` — trzsz-ssh ( tssh ) is an ssh client designed as a drop-in replacement for the openssh client. It aims to provide complete compatibility with openssh, mirroring all its features, while also offering additional useful features. Such as login prompt, batch login, remember password, automated interaction, trzsz, zmodem(rz/sz), udp mode like mosh, etc. _(aliases: `tssh`)_
- `ttyd` — Share your terminal over the web
- `wash` — wasmCloud Shell (wash)
- `wtfutil` — WTF is the personal information dashboard for your terminal
- `xxh` — 🚀 Bring your favorite shell wherever you go through the ssh. Xonsh shell, fish, zsh, osquery and so on.
- `yazi` — Blazing fast terminal file manager written in Rust, based on async I/O
- `zellij` — A terminal workspace with batteries included
- `zoxide` — A smarter cd command. Supports all major shells

### General CLI utilities (14)
- `ag` — The Silver Searcher: A code searching tool similar to ack, with a focus on speed
- `bat` — A cat(1) clone with wings
- `bat-extras` — Bash scripts that integrate bat with various command line tools
- `bfs` — Breadth-first search for your files
- `btop` — A monitor of resources
- `cheat` — cheat allows you to create and view interactive cheatsheets on the command-line. It was designed to help remind *nix system administrators of options for commands that they use frequently, but not frequently enough to remember
- `choose` — A human-friendly and fast alternative to cut (and sometimes awk)
- `delta` — A syntax-highlighting pager for git, diff, and grep output
- `eza` — A modern, maintained replacement for ls
- `fd` — A simple, fast and user-friendly alternative to 'find'
- `jq` — Command-line JSON processor
- `ripgrep` — ripgrep recursively searches directories for a regex pattern while respecting your gitignore _(aliases: `rg`)_
- `sentry` — A command line utility to work with Sentry _(aliases: `sentry-cli`)_
- `yq` — yq is a portable command-line YAML processor

### Task runners and automation (10)
- `air` — Live reload for Go apps
- `argc` — A Bash CLI framework, also a Bash command runner
- `cargo-make` — Rust task runner and build tool
- `cmdx` — Task runner. It provides useful help messages and supports interactive prompts and validation of arguments
- `jc` — CLI tool and python library that converts the output of popular command-line tools, file-types, and common strings to JSON, YAML, or Dictionaries. This allows piping of output to tools like jq and simplifying automation scripts
- `just` — Just a command runner
- `mask` — A CLI task runner defined by a simple markdown file
- `task` — A task runner / simpler Make alternative written in Go
- `watchexec` — Executes commands in response to file modifications
- `xc` — Markdown defined task runner

### Editors and IDE helpers (6)
- `bob` — A version manager for neovim
- `code` — Fast, effective, mind-blowing, coding CLI. Browser integration, multi-agents, theming, and reasoning control. Orchestrate agents from OpenAI, Claude, Gemini or any provider.
- `helix` — A post-modern modal text editor
- `marksman` — Write Markdown with code assist and intelligence in the comfort of your favourite editor
- `neovim` — Vim-fork focused on extensibility and usability
- `vim` — Vim is an advanced text editor that seeks to provide the power of the de-facto Unix editor 'Vi', with a more complete feature set. It's useful whether you're already using vi or using a different editor

### Dotfiles and environment management (3)
- `chezmoi` — Manage your dotfiles across multiple diverse machines, securely
- `direnv` — unclutter your .profile
- `dotenvx` — a secure dotenv–from the creator of `dotenv`

</details>

<details open>
<summary><strong>Platform, mobile, and specialized tooling</strong> (15 tools)</summary>

### Mobile and cross-platform development (6)
- `aapt2` — Android Asset Packaging Tool (aapt)
- `android-sdk` — Android Command-line tools
- `figma-export` — Command line utility to export colors, typography, icons and images from Figma to Xcode / Android Studio project
- `flutter` — Flutter is an open source framework for building beautiful, natively compiled, multi-platform applications from a single codebase
- `license-plist` — A license list generator of all your dependencies for iOS applications
- `maestro` — Painless E2E Automation for Mobile and Web

### Apple ecosystem (4)
- `apollo-ios` — Apollo iOS Code Generation _(aliases: `apollo-ios-cli`)_
- `carthage` — A simple, decentralized dependency manager for Cocoa
- `container` — A tool for creating and running Linux containers using lightweight virtual machines on a Mac.
- `swiftlint` — A tool to enforce Swift style and conventions

### Creative and specialized tooling (3)
- `blender` — Blender is a free and open-source 3D computer graphics software
- `godot` — Free and open source 2D and 3D game engine
- `resvg` — An SVG rendering library.

### Browsers and drivers (1)
- `chromedriver` — ChromeDriver is a standalone server that implements the W3C WebDriver and WebDriver BiDi standards

### Embedded, IoT, and hardware (1)
- `arduino` — Arduino command line tool _(aliases: `arduino-cli`)_

</details>

<details open>
<summary><strong>AI and developer assistants</strong> (7 tools)</summary>

### Chat and agent CLIs (4)
- `aichat` — Use GPT-4(V), Gemini, LocalAI, Ollama and other LLMs in the terminal
- `amp` — An agentic coding tool built by Sourcegraph
- `claude` — Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows -- all through natural language commands _(aliases: `claude-code`)_
- `ollama` — Get up and running with Llama 3.1, Mistral, Gemma 2, and other large language models

### General AI and assistant tooling (3)
- `claude-powerline` — Beautiful vim-style powerline statusline for Claude Code
- `claude-squad` — Manage multiple AI agents like Claude Code, Aider, Codex, and Amp. 10x your productivity
- `ksops` — KSOPS - A Flexible Kustomize Plugin for SOPS Encrypted Resources

</details>

<details open>
<summary><strong>Other cross-domain tools</strong> (61 tools)</summary>

### Miscellaneous tools (61)
- `cli53` — Command line tool for Amazon Route 53
- `cocogitto` — The Conventional Commits toolbox
- `container-use` — Development environments for coding agents. Enable multiple agents to work safely and independently with your preferred stack.
- `cpz` — A zippy alternative to cp, a tool to copy files and directories
- `croc` — Easily and securely send things from one computer to another 🐊 📦
- `dagu` — Yet another cron alternative with a Web UI, but with much more capabilities. It aims to solve greater problems
- `diffoci` — diff for Docker and OCI container images
- `docker-compose` — Define and run multi-container applications with Docker
- `dvc` — Data Versioning and ML Experiments
- `edit` — We all edit
- `fnox` — Fort Knox for your secrets
- `gallery-dl` — Command-line program to download image galleries and collections from several image hosting sites
- `gdu` — Fast disk usage analyzer with console interface written in Go
- `git-lfs` — Git extension for versioning large files
- `gitu` — A TUI Git client inspired by Magit
- `gitversion` — From git log to SemVer in no time
- `gocryptfs` — Encrypted overlay filesystem written in Go
- `gping` — Ping, but with a graph
- `gron` — Make JSON greppable
- `gup` — gup - Update binaries installed by "go install" with goroutines
- `hexyl` — A command-line hex viewer
- `hivemind` — Process manager for Procfile-based applications
- `hk` — git hook and pre-commit lint manager
- `htmlq` — Like jq, but for HTML
- `hugo-extended` — The world’s fastest framework for building websites
- `jaq` — A jq clone focussed on correctness, speed, and simplicity
- `jd` — JSON diff and patch
- `jjui` — Jujutsu UI (jjui) is a Text User Interface (TUI) designed for interacting with the Jujutsu version control system _(aliases: `jujutsu-ui`)_
- `jwtui` — A command line UI for decoding/encoding JSON Web Tokens
- `killport` — A command-line tool to easily kill processes running on a specified port
- `kubens` — Faster way to switch between clusters and namespaces in kubectl
- `kubeswitch` — The kubectx for operators
- `lazydocker` — The lazier way to manage everything docker
- `lnav` — Log file navigator
- `miller` — Miller is like awk, sed, cut, join, and sort for name-indexed data such as CSV, TSV, and tabular JSON
- `minisign` — A dead simple tool to sign files and verify digital signatures
- `mold` — Mold: A Modern Linker
- `mprocs` — Run multiple commands in parallel
- `mutagen` — Fast file synchronization and network forwarding for remote development
- `navi` — An interactive cheatsheet tool for the command-line
- `openbao` — OpenBao exists to provide a software solution to manage, store, and distribute sensitive data including secrets, certificates, and keys
- `overmind` — Process manager for Procfile-based applications and tmux
- `oxipng` — Oxipng is a multithreaded lossless PNG/APNG compression optimizer
- `oxker` — A simple tui to view & control docker containers
- `pitchfork` — Daemons with DX
- `pixi` — Package management made easy
- `porter` — CNAB bundle authoring and management tool
- `prek` — No description supplied.
- `process-compose` — Process Compose is a simple and flexible scheduler and orchestrator to manage non-containerized applications.
- `protoc-gen-validate` — Protocol Buffer Validation - Being replaced by github.com/bufbuild/protovalidate
- `ripgrep-all` — rga: ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, etc
- `rmz` — A zippy alternative to rm, a tool to remove files and directories
- `s5cmd` — Parallel S3 and local filesystem execution tool
- `starknet-foundry-sncast` — All-in-one tool for interacting with Starknet smart contracts, sending transactions and getting chain data
- `television` — The revolution will (not) be televised
- `topgrade` — Upgrade all the things
- `trufflehog` — No description supplied.
- `tusd` — Reference server implementation in Go of tus: the open protocol for resumable file uploads
- `ubi` — The Universal Binary Installer
- `vivid` — A themeable LS_COLORS generator with a rich filetype datebase
- `workmux` — git worktrees + tmux windows for zero-friction parallel dev

</details>

## Registry changes in the last 12 months

### 2026-03
- Added (9): `mysql-client`, `ormolu`, `pi`, `portless`, `tigerbeetle`, `tinygo`, `turbo`, `viteplus`, `workmux`
- Removed (0): none

### 2026-02
- Added (15): `cargo-dist`, `communique`, `entireio-cli`, `godot`, `mas`, `mermaid-ascii`, `mutagen`, `orval`, `oxfmt`, `podman-tui`, `porter`, `quicktype`, `release-plz`, `tirith`, `topgrade`
- Removed (0): none

### 2026-01
- Added (904): `1password`, `aapt2`, `act`, `action-validator`, `actionlint`, `adr-tools`, `ag`, `age`, `age-plugin-yubikey`, `agebox`, `aichat`, `air`, `aks-engine`, `allure`, `allurectl`, `alp`, `amass`, `amazon-ecr-credential-helper`, `amazon-ecs-cli`, `amp`, `android-sdk`, `ansible`, `ansible-core`, `ant`, `apko`, `apollo-ios`, `apollo-router`, `apollo-rover`, `aqua`, `arduino`, `argc`, `argo`, `argo-rollouts`, `argocd`, `asciidoctorj`, `assh`, `ast-grep`, `astro`, `atlas`, `atlas-community`, `atmos`, `atuin`, `auto-doc`, `aws-amplify`, `aws-cli`, `aws-copilot`, `aws-iam-authenticator`, `aws-nuke`, `aws-sam`, `aws-sso`, `aws-vault`, `awscli-local`, `awsebcli`, `awsls`, `awsrm`, `awsweeper`, `azure`, `azure-functions-core-tools`, `azure-kubelogin`, `babashka`, `balena`, `bashbot`, `bashly`, `bat`, `bat-extras`, `bats`, `bazel`, `bazel-watcher`, `bazelisk`, `bfs`, `bibtex-tidy`, `binnacle`, `biome`, `bitwarden`, `bitwarden-secrets-manager`, `black`, `blender`, `bob`, `boilerplate`, `bombardier`, `borg`, `bosh`, `bosh-backup-and-restore`, `bottom`, `boundary`, `bpkg`, `brig`, `btop`, `btrace`, `buck2`, `buf`, `buildifier`, `buildpack`, `bun`, `cabal`, `caddy`, `calendarsync`, `calicoctl`, `carapace`, `cargo-binstall`, `cargo-insta`, `cargo-make`, `carp`, `carthage`, `ccache`, `certstrap`, `cf`, `cfn-lint`, `cfssl`, `cfssljson`, `chamber`, `changie`, `cheat`, `checkmake`, `checkov`, `chezmoi`, `chezscheme`, `chicken`, `chisel`, `choose`, `chromedriver`, `cidr-merger`, `cidrchk`, `cilium-cli`, `cilium-hubble`, `circleci`, `clang`, `clang-format`, `clarinet`, `claude`, `claude-powerline`, `claude-squad`, `cli53`, `clickhouse`, `clj-kondo`, `cljstyle`, `clojure`, `cloud-sql-proxy`, `cloudflared`, `clusterawsadm`, `clusterctl`, `cmake`, `cmctl`, `cmdx`, `cockroach`, `cocoapods`, `cocogitto`, `code`, `codebuff`, `codefresh`, `codeql`, `coder`, `codex`, `colima`, `committed`, `conan`, `concourse`, `conduit`, `conform`, `conftest`, `consul`, `container`, `container-structure-test`, `container-use`, `cookiecutter`, `copier`, `copper`, `coredns`, `coreutils`, `cosign`, `coursier`, `cowsay`, `cpz`, `crane`, `credhub`, `crictl`, `croc`, `crossplane`, `crush`, `crystal`, `cspell`, `ctlptl`, `ctop`, `cue`, `curlie`, `cyclonedx`, `d2`, `dagger`, `dagu`, `danger-js`, `danger-swift`, `dapr`, `dart`, `dasel`, `databricks-cli`, `datree`, `daytona`, `dbmate`, `deck`, `delta`, `deno`, `depot`, `desk`, `devcontainer-cli`, `devspace`, `dhall`, `diffoci`, `difftastic`, `direnv`, `dive`, `djinni`, `docker-cli`, `docker-compose`, `docker-slim`, `dockle`, `doctl`, `docuum`, `doggo`, `dome`, `doppler`, `dotenv-linter`, `dotenvx`, `dotnet`, `dotnet-core`, `dotslash`, `dprint`, `draft`, `driftctl`, `drone`, `dt`, `dtm`, `dua`, `duckdb`, `duf`, `dust`, `dvc`, `dyff`, `dynatrace-monaco`, `e1s`, `earthly`, `ecspresso`, `edit`, `editorconfig-checker`, `ejson`, `eksctl`, `elasticsearch`, `elixir`, `elixir-ls`, `elm`, `emsdk`, `envcli`, `envsubst`, `erlang`, `esc`, `esy`, `etcd`, `evans`, `eza`, `fastfetch`, `fd`, `ffmpeg`, `figma-export`, `fillin`, `firebase`, `fission`, `flamingo`, `flarectl`, `flatc`, `flutter`, `fluttergen`, `flux2`, `fly`, `flyctl`, `flyway`, `fnox`, `foundry`, `func-e`, `furyctl`, `fx`, `fzf`, `gallery-dl`, `gam`, `gator`, `gcc-arm-none-eabi`, `gcloud`, `gdu`, `gemini-cli`, `getenvoy`, `ggshield`, `ghalint`, `ghc`, `ghcup`, `ghorg`, `ghq`, `ginkgo`, `git-chglog`, `git-cliff`, `git-lfs`, `gitconfig`, `github-cli`, `github-markdown-toc`, `gitleaks`, `gitsign`, `gitu`, `gitui`, `gitversion`, `glab`, `gleam`, `glen`, `glooctl`, `glow`, `go`, `go-containerregistry`, `go-getter`, `go-jira`, `go-jsonnet`, `go-junit-report`, `go-sdk`, `go-swagger`, `goconvey`, `gocryptfs`, `gofumpt`, `gojq`, `gokey`, `golangci-lint`, `golangci-lint-langserver`, `golines`, `gomigrate`, `gomplate`, `gopass`, `goreleaser`, `goss`, `gotestsum`, `gping`, `graalvm`, `gradle`, `grain`, `granted`, `graphite`, `grex`, `gron`, `groovy`, `grpc-health-probe`, `grpcurl`, `grype`, `gum`, `gup`, `gwvault`, `hadolint`, `harper-cli`, `harper-ls`, `has`, `hasura-cli`, `hatch`, `haxe`, `hcl2json`, `hcloud`, `helix`, `helm`, `helm-cr`, `helm-ct`, `helm-diff`, `helm-docs`, `helm-ls`, `helmfile`, `helmsman`, `helmwave`, `heroku`, `hexyl`, `hishtory`, `hivemind`, `hk`, `hledger`, `hledger-flow`, `hostctl`, `htmlq`, `httpie-go`, `hub`, `hugo`, `hugo-extended`, `hurl`, `hwatch`, `hygen`, `hyperfine`, `iam-policy-json-to-terraform`, `iamlive`, `imagemagick`, `imgpkg`, `infisical`, `infracost`, `inlets`, `istioctl`, `jaq`, `java`, `jbang`, `jc`, `jd`, `jfrog-cli`, `jib`, `jiq`, `jj`, `jjui`, `jless`, `jmespath`, `jnv`, `jq`, `jqp`, `jreleaser`, `json5`, `jsonnet-bundler`, `jsonschema`, `jules`, `julia`, `just`, `jwt`, `jwtui`, `jx`, `k0sctl`, `k2tf`, `k3d`, `k3kcli`, `k3s`, `k3sup`, `k6`, `k9s`, `kafkactl`, `kapp`, `kbld`, `kcctl`, `kcl`, `kconf`, `ki`, `killport`, `kind`, `kiota`, `kn`, `ko`, `koka`, `kompose`, `kopia`, `kops`, `kotlin`, `kpack`, `kpt`, `krab`, `krew`, `kscript`, `ksops`, `ktlint`, `kube-capacity`, `kube-controller-tools`, `kube-credential-cache`, `kube-linter`, `kube-score`, `kubebuilder`, `kubecm`, `kubecolor`, `kubeconform`, `kubectl`, `kubectl-convert`, `kubectl-kots`, `kubectl-kuttl`, `kubectl-rolesum`, `kubectx`, `kubefedctl`, `kubefirst`, `kubelogin`, `kubemqctl`, `kubens`, `kubent`, `kubeone`, `kubergrunt`, `kubeseal`, `kubesec`, `kubeshark`, `kubespy`, `kubeswitch`, `kubeval`, `kubevela`, `kubie`, `kustomize`, `kwokctl`, `kwt`, `kyverno`, `lab`, `lane`, `lazydocker`, `lazygit`, `lazyjournal`, `lazyssh`, `lefthook`, `leiningen`, `levant`, `libsql-server`, `license-plist`, `lima`, `linkerd`, `liqoctl`, `liquibase`, `litestream`, `lnav`, `localstack`, `loki-logcli`, `ls-lint`, `lsd`, `lua`, `lua-language-server`, `luajit`, `luau`, `lychee`, `maestro`, `mage`, `magika`, `mago`, `make`, `mani`, `mark`, `markdownlint-cli2`, `marksman`, `marp-cli`, `mask`, `maven`, `mc`, `mdbook`, `mdbook-linkcheck`, `melange`, `melt`, `meson`, `micromamba`, `micronaut`, `miller`, `mimirtool`, `minify`, `minikube`, `minio`, `minishift`, `minisign`, `mint`, `mirrord`, `mitmproxy`, `mkcert`, `mockery`, `mockolo`, `mold`, `mongodb`, `mongosh`, `mprocs`, `mssqldef`, `mvnd`, `mysql`, `mysqldef`, `nancy`, `navi`, `neko`, `nelm`, `neonctl`, `neovim`, `nerdctl`, `newrelic`, `nfpm`, `ni`, `ninja`, `node`, `nomad`, `nomad-pack`, `notation`, `nova`, `npm`, `nsc`, `numbat`, `oapi-codegen`, `oauth2c`, `oc`, `oci`, `octosql`, `odin`, `odo`, `oh-my-posh`, `oha`, `okta-aws`, `okteto`, `ollama`, `om`, `omnictl`, `onyx`, `opa`, `opam`, `openbao`, `opencode`, `openfaas-cli`, `opengrep`, `opensearch-cli`, `openshift-install`, `opentofu`, `operator-sdk`, `opsgenie-lamp`, `oras`, `osv-scanner`, `overmind`, `oxipng`, `oxker`, `oxlint`, `pachctl`, `packer`, `pandoc`, `patat`, `pdm`, `peco`, `periphery`, `perl`, `php`, `pinact`, `pint`, `pipectl`, `pipenv`, `pipx`, `pitchfork`, `pivnet`, `pixi`, `pkl`, `please`, `pluto`, `pnpm`, `podman`, `poetry`, `polaris`, `popeye`, `postgres`, `powerline-go`, `powerpipe`, `powershell-core`, `pre-commit`, `prek`, `prettier`, `process-compose`, `promtool`, `protoc`, `protoc-gen-connect-go`, `protoc-gen-go`, `protoc-gen-go-grpc`, `protoc-gen-js`, `protoc-gen-validate`, `protolint`, `psc-package`, `psqldef`, `pulumi`, `purerl`, `purescript`, `purty`, `python`, `qdns`, `qsv`, `quarkus`, `railway`, `rancher`, `rbac-lookup`, `rclone`, `rebar`, `reckoner`, `redis`, `redo`, `redpanda-connect`, `reg`, `regal`, `regctl`, `regsync`, `restic`, `restish`, `resvg`, `revive`, `richgo`, `ripgrep`, `ripgrep-all`, `ripsecrets`, `rke`, `rmz`, `rpk`, `ruby`, `ruff`, `rumdl`, `rust`, `rust-analyzer`, `rustic`, `rye`, `s5cmd`, `saml2aws`, `sampler`, `sbt`, `scala`, `scala-cli`, `scaleway`, `scalingo-cli`, `scarb`, `sccache`, `schemacrawler`, `scie-pants`, `scooter`, `scorecard`, `sd`, `semgrep`, `semver`, `sentinel`, `sentry`, `serverless`, `setup-envtest`, `shell2http`, `shellcheck`, `shellspec`, `shfmt`, `signadot`, `sinker`, `skaffold`, `skate`, `skeema`, `sloth`, `slsa-verifier`, `smithy`, `snyk`, `soft-serve`, `solidity`, `sonar-scanner-cli`, `sonobuoy`, `sops`, `sopstool`, `soracom`, `sourcery`, `spacectl`, `spago`, `spark`, `specstory`, `spectral`, `spin`, `spring-boot`, `spruce`, `sqlc`, `sqlite`, `sqlite3def`, `sshi`, `sshuttle`, `sst`, `stack`, `starboard`, `starknet-foundry`, `starknet-foundry-sncast`, `starship`, `staticcheck`, `steampipe`, `step`, `stern`, `stripe`, `stylua`, `sui`, `supabase`, `superfile`, `superhtml`, `sver`, `svu`, `swag`, `swift`, `swift-package-list`, `swiftformat`, `swiftgen`, `swiftlint`, `syft`, `tailpipe`, `talhelper`, `talosctl`, `tanka`, `tanzu`, `taplo`, `task`, `tbls`, `tctl`, `tekton`, `teleport-community`, `teleport-ent`, `telepresence`, `television`, `teller`, `temporal`, `terradozer`, `terraform`, `terraform-docs`, `terraform-ls`, `terraform-lsp`, `terraform-validator`, `terraformer`, `terragrunt`, `terramate`, `terrascan`, `tf-summarize`, `tfc-agent`, `tfctl`, `tfenv`, `tflint`, `tfmigrate`, `tfnotify`, `tfsec`, `tfstate-lookup`, `tfswitch`, `tfupdate`, `tilt`, `timoni`, `tiny`, `tinymist`, `tinytex`, `titan`, `tlrc`, `tmux`, `tokei`, `tombi`, `tomcat`, `tonnage`, `traefik`, `transifex`, `trdsql`, `tree-sitter`, `tridentctl`, `trivy`, `trufflehog`, `trunk`, `trzsz-ssh`, `tsuru`, `ttyd`, `tuist`, `tusd`, `ty`, `typos`, `typst`, `typstyle`, `uaa`, `ubi`, `unison`, `upctl`, `updatecli`, `upt`, `upx`, `usage`, `usql`, `uv`, `v`, `vacuum`, `vale`, `vals`, `vault`, `vcluster`, `velad`, `velero`, `vendir`, `venom`, `vercel`, `vespa-cli`, `vfox`, `vhs`, `victoria-metrics`, `viddy`, `vim`, `vivid`, `vlang`, `vultr`, `wait-for-gh-rate-limit`, `wash`, `wasm4`, `wasmer`, `wasmtime`, `watchexec`, `waypoint`, `weave-gitops`, `websocat`, `werf`, `wrangler`, `wren`, `wtfutil`, `xc`, `xcbeautify`, `xchtmlreport`, `xcodegen`, `xcodes`, `xcresultparser`, `xcsift`, `xh`, `xxh`, `yamlfmt`, `yamllint`, `yamlscript`, `yarn`, `yazi`, `yj`, `yor`, `youtube-dl`, `yq`, `yt-dlp`, `ytt`, `zarf`, `zbctl`, `zellij`, `zephyr`, `zig`, `zigmod`, `zizmor`, `zls`, `zola`, `zoxide`, `zprint`
- Removed (0): none

### 2025-12
- Added (0): none
- Removed (0): none

### 2025-11
- Added (0): none
- Removed (0): none

### 2025-10
- Added (0): none
- Removed (0): none

### 2025-09
- Added (0): none
- Removed (0): none

### 2025-08
- Added (0): none
- Removed (0): none

### 2025-07
- Added (0): none
- Removed (0): none

### 2025-06
- Added (0): none
- Removed (0): none

### 2025-05
- Added (0): none
- Removed (0): none

### 2025-04
- Added (0): none
- Removed (0): none

## Deduplicated and aliased tools

- `1password` — collapsed registry rows: `1password-cli`, `op`
- `amazon-ecs-cli` — collapsed registry rows: `ecs-cli`
- `ansible-core` — collapsed registry rows: `ansible-base`
- `apollo-ios` — collapsed registry rows: `apollo-ios-cli`
- `arduino` — collapsed registry rows: `arduino-cli`
- `aws-amplify` — collapsed registry rows: `amplify`
- `aws-cli` — collapsed registry rows: `aws`, `awscli`
- `aws-sam` — collapsed registry rows: `aws-sam-cli`
- `azure` — collapsed registry rows: `azure-cli`
- `balena` — collapsed registry rows: `balena-cli`
- `bosh-backup-and-restore` — collapsed registry rows: `bbr`
- `buildpack` — collapsed registry rows: `buildpacks`, `pack`
- `circleci` — collapsed registry rows: `circleci-cli`
- `claude` — collapsed registry rows: `claude-code`
- `crossplane` — collapsed registry rows: `crossplane-cli`
- `entireio-cli` — collapsed registry rows: `entire`
- `gemini-cli` — collapsed registry rows: `gemini`
- `github-cli` — collapsed registry rows: `gh`
- `heroku` — collapsed registry rows: `heroku-cli`
- `jj` — collapsed registry rows: `jujutsu`
- `jjui` — collapsed registry rows: `jujutsu-ui`
- `jsonnet-bundler` — collapsed registry rows: `jb`
- `kpack` — collapsed registry rows: `kp`
- `kubectl-kuttl` — collapsed registry rows: `kuttl`
- `kubectl-rolesum` — collapsed registry rows: `kubectl-bindrole`
- `newrelic` — collapsed registry rows: `newrelic-cli`
- `okta-aws` — collapsed registry rows: `okta-aws-cli`
- `powershell-core` — collapsed registry rows: `powershell`
- `protoc` — collapsed registry rows: `protobuf`
- `redpanda-connect` — collapsed registry rows: `benthos`
- `ripgrep` — collapsed registry rows: `rg`
- `scaleway` — collapsed registry rows: `scaleway-cli`
- `sentry` — collapsed registry rows: `sentry-cli`
- `stripe` — collapsed registry rows: `stripe-cli`
- `talosctl` — collapsed registry rows: `talos`
- `tekton` — collapsed registry rows: `tekton-cli`
- `trzsz-ssh` — collapsed registry rows: `tssh`
- `uaa` — collapsed registry rows: `uaa-cli`
- `vultr` — collapsed registry rows: `vultr-cli`
- `wren` — collapsed registry rows: `wren-cli`
