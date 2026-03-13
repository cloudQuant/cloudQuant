# cloudQuant BMAD Framework

[![BMAD Version](https://img.shields.io/badge/BMAD-6.1.0-blue.svg)](https://github.com/bmad-code-org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#-license)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**AI-Powered Development Framework for Quantitative Trading Systems**

[English](#english) | [中文](#中文)

---

<a name="english"></a>

## Overview

cloudQuant is a BMAD (Breakthrough Method for AI Development) framework configuration repository designed for quantitative trading system development. This repository provides a structured, AI-assisted development methodology for building trading systems, research tools, and analytics infrastructure.

### What is BMAD?

BMAD is a modular AI development framework that provides:

- **Structured Workflows** - Step-by-step development processes
- **AI Agent Integration** - Pre-configured AI agents for different tasks
- **Multi-IDE Support** - Works with Claude Code, Cursor. OpenCode. Windsurf. and Codex
- **Domain-Specific Modules** - Specialized tools for different development scenarios

## 🚀 Quick Start

### Prerequisites

- Git 2.0+
- One of the supported IDEs:
  - [Claude Code](https://claude.ai/code)
  - [Cursor](https://cursor.sh)
  - [OpenCode](https://opencode.ai)
  - [Windsurf](https://codeium.com/windsurf)

### Installation

```bash
# Clone the repository
git clone https://github.com/cloudQuant/cloudQuant.git
cd cloudQuant

# Open in your preferred IDE
code .  # or cursor . or claude .
```

### First Steps

1. Read the [Quick Start Guide](docs/guides/quick-start.md)
2. Explore the [Architecture Documentation](docs/architecture/README.md)
3. Check out the [Contributing Guidelines](CONTRIBUTING.md)

## 📁 Project Structure

```text
cloudQuant/
├── .github/              # GitHub configurations (CI. templates)
├── _bmad/                # BMAD Framework Core
│   ├── core/             # Core workflows and agents
│   ├── bmm/              # Business Method Module
│   ├── cis/              # Creative Intelligence Suite
│   ├── gds/              # Game Dev Studio
│   ├── tea/              # Test Engineering Architecture
│   └── wds/              # Web Design System
├── _bmad-output/         # Generated outputs
├── docs/                 # Project documentation
│   ├── architecture/     # Architecture docs and ADRs
│   ├── api/              # API documentation
│   └── guides/           # Development guides
├── design-artifacts/     # Design-related artifacts
├── .editorconfig         # Editor configuration
├── .gitignore            # Git ignore rules
├── CHANGELOG.md          # Version history
├── CONTRIBUTING.md       # Contribution guidelines
└── README.md             # This file
```

## 🧩 BMAD Modules

| Module   | Version | Description                                            |
| -------- | ------- | ------------------------------------------------------ |
| **Core** | 6.1.0   | Core workflows and base agents                         |
| **BMM**  | 6.1.0   | Business methodology (PRD. architecture. epics)        |
| **CIS**  | 0.1.8   | Creative intelligence (brainstorming. design thinking) |
| **GDS**  | 0.1.10  | Game development workflows                             |
| **TEA**  | 1.6.0   | Test engineering and automation                        |
| **WDS**  | 0.3.0   | Web design system and UI components                    |

## 📚 Documentation

- [Architecture Overview](docs/architecture/README.md)
- [API Documentation](docs/api/README.md)
- [Development Guides](docs/guides/README.md)
- [Quick Start Guide](docs/guides/quick-start.md)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:

- How to submit issues
- How to submit pull requests
- Code style guidelines
- Documentation standards

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

cloudQuant maintains several quantitative trading related projects:

### Trading Frameworks

- [backtrader](https://github.com/cloudQuant/backtrader) - Quantitative trading framework
- [bt_api_py](https://github.com/cloudQuant/bt_api_py) - Multi-exchange API SDK
- [backtrader_web](https://github.com/cloudQuant/backtrader_web) - Web-based strategy management
- [fincore](https://github.com/cloudQuant/fincore) - Financial metrics toolkit

### Research & Analytics

- [alphalens](https://github.com/cloudQuant/alphalens) - Factor analysis
- [pyfolio](https://github.com/cloudQuant/pyfolio) - Portfolio analytics
- [empyrical](https://github.com/cloudQuant/empyrical) - Performance metrics

### Data & APIs

- [akshare_web](https://github.com/cloudQuant/akshare_web) - Market data tools
- [ctp-python](https://github.com/cloudQuant/ctp-python) - CTP futures interface

## 📧 Contact

- Email: yunjinqi@gmail.com
- GitHub: [@cloudQuant](https://github.com/cloudQuant)

---

<a name="中文"></a>

## 中文版

### 概述

cloudQuant 是一个 BMAD（AI 开发突破方法）框架配置仓库.专为量化交易系统开发设计。本仓库提供结构化的、AI 辅助的开发方法论.用于构建交易系统、研究工具和分析基础设施。

### 快速开始

```bash
# 克隆仓库
git clone https://github.com/cloudQuant/cloudQuant.git
cd cloudQuant
```

### 项目结构

| 目录                | 说明             |
| ------------------- | ---------------- |
| `_bmad/`            | BMAD 框架核心    |
| `docs/`             | 项目文档         |
| `.github/`          | GitHub 配置和 CI |
| `design-artifacts/` | 设计相关产物     |

### BMAD 模块

| 模块 | 版本   | 说明             |
| ---- | ------ | ---------------- |
| Core | 6.1.0  | 核心工作流和代理 |
| BMM  | 6.1.0  | 业务方法论       |
| CIS  | 0.1.8  | 创意智能套件     |
| GDS  | 0.1.10 | 游戏开发套件     |
| TEA  | 1.6.0  | 测试工程架构     |
| WDS  | 0.3.0  | Web 设计系统     |

### 贡献

欢迎贡献！请查看 [贡献指南](CONTRIBUTING.md) 了解详情。

### 联系方式

- 邮箱: yunjinqi@gmail.com
- GitHub: [@cloudQuant](https://github.com/cloudQuant)

---

_Last updated: 2026-03-13_
