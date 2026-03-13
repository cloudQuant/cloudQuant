# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Project-level `.gitignore` for unified ignore rules
- `.editorconfig` for consistent editor settings
- `CONTRIBUTING.md` contribution guidelines (bilingual)
- `CHANGELOG.md` version history tracking
- `docs/` directory structure with architecture, API, and guides sections
- `.github/` directory with CI workflows and issue/PR templates
- ADR (Architecture Decision Record) index page
- Project badges in README
- `.pre-commit-config.yaml` with hooks for linting, formatting, and type checking

### Changed

- Rewritten `README.md` as a project documentation hub (previously a profile README)
- Consolidated IDE configuration references
- Cleaned up empty directories with placeholder content
- Updated `pyproject.toml` ruff configuration to new API format (`[tool.ruff.lint]`)
- Fixed `.prettierrc` by removing unsupported `markdown.singleQuote` option

### Fixed

- LICENSE copyright year corrected from 2026 to 2025

---

## [6.1.0] - 2026-03-13

### Added

- BMAD framework v6.1.0 core module
- CIS (Creative Intelligence Suite) module v0.1.8
- GDS (Game Dev Studio) module v0.1.10
- TEA (Test Engineering Architecture) module v1.6.0
- WDS (Web Design System) module v0.3.0
- Multi-IDE support (Claude Code, Cursor, Codex, OpenCode, Windsurf)

### Modules Installed

| Module | Version | Source                                   |
| ------ | ------- | ---------------------------------------- |
| core   | 6.1.0   | built-in                                 |
| bmm    | 6.1.0   | built-in                                 |
| cis    | 0.1.8   | bmad-creative-intelligence-suite         |
| gds    | 0.1.10  | bmad-game-dev-studio                     |
| tea    | 1.6.0   | bmad-method-test-architecture-enterprise |
| wds    | 0.3.0   | bmad-method-wds-expansion                |

---

## Version History Summary

| Version | Date       | Description                                   |
| ------- | ---------- | --------------------------------------------- |
| 6.1.0   | 2026-03-13 | Initial BMAD framework setup with all modules |

---

[Unreleased]: https://github.com/cloudQuant/cloudQuant/compare/v6.1.0...HEAD
[6.1.0]: https://github.com/cloudQuant/cloudQuant/releases/tag/v6.1.0
