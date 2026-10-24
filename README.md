# Hi, I'm `cloudQuant`

<a id="english-version" name="english-version"></a>

[English](#english-version) | [中文](#chinese-version)

## English Version

Quant engineer building the infrastructure behind systematic trading: high-performance backtesting and analytics, market-data platforms, and multi-venue execution. Python first, with C++ / Rust / TypeScript where performance or tooling demands it.

## About Me

- Quant credentials: `CFA`, `FRM`, `CIIA`, `CFP`
- Market coverage: China A-shares, domestic futures, and cross-market multi-asset research
- Main interests:
  - Algorithmic trading and strategy research
  - Backtesting and strategy engineering
  - Portfolio, factor and risk analytics
  - Market-data engineering and data quality
  - High-performance systems (C++ / Rust / pybind11)
  - AI-assisted research and developer tooling

## What I've Been Working On Recently

Over the past two years, my GitHub work has centered on four project ecosystems:

- `backtrader` — a performance-optimized Backtrader fork (Python + C++), its web platform, and an AI-native strategy-development workflow
- `fincore` — unified quantitative performance, risk and factor analytics
- `opendata` — a multi-source financial data middle platform (ingestion → warehouse → REST / WebSocket services)
- `bt_api` — a standardized multi-venue trading API ecosystem (exchange adapters, broker plugins, gateway, execution and risk layers)

Recent active repositories: `opendata`, `backtrader`, `fincore`, `fincore_cpp`, `ai-for-investor`.

## Current Focus

- Building production-friendly Python SDKs and services for quant workflows
- Market-data infrastructure: multi-source ingestion, cross-source validation, and unified query services
- Researching and refining trading strategies across multiple market styles
- C++ / Rust / pybind11 acceleration paths for quant infrastructure
- Connecting research, backtesting, live execution and data tooling into a unified workflow
- Making quant systems easier to use with MCP / AI-native interfaces

## Strategy Interests

- Trend following (CTA)
- Multi-factor stock selection
- Mean reversion
- Momentum
- Statistical arbitrage
- Event-driven strategies
- Arbitrage and spread trading
- Market making
- High-frequency trading research

## Selected Projects

### Backtrader Ecosystem

**Core framework and platform**

- [`backtrader`](https://github.com/cloudQuant/backtrader) — high-performance Python backtesting & live-trading framework: vectorized and event-driven modes, multi-timeframe data, 50+ indicators, and pybind11-accelerated C++ wheels
- [`backtrader_cpp`](https://github.com/cloudQuant/backtrader_cpp) — C++ rewrite of the Backtrader engine
- [`ai-for-investor`](https://github.com/cloudQuant/ai-for-investor) — AI-driven quantitative research platform (Vue 3 + FastAPI): knowledge-base Q&A, Backtrader strategy authoring and versioning, data-quality pre-checks, backtests with robustness and parameter optimization, paper trading, and portfolio risk monitoring — the successor to `backtrader_web`

**AI-native workflow**

- [`backtrader-mcp`](https://github.com/cloudQuant/backtrader-mcp) — local-first MCP server for AI-assisted strategy development: immutable datasets, private drafts, and bounded subprocess backtests via 30 typed tools
- [`backtrader-skills`](https://github.com/cloudQuant/backtrader-skills) — offline author/review/test skills for AI coding agents (Claude Code, Codex, OpenCode)
- [`backtrader-agent`](https://github.com/cloudQuant/backtrader-agent) — offline-first strategy-authoring agent runtime: StrategySpec validation, static review, hash-bound approvals

### Fincore Ecosystem

- [`fincore`](https://github.com/cloudQuant/fincore) — quantitative performance & risk analytics: 150+ financial metrics, portfolio optimization, Monte Carlo simulation, and attribution — the actively maintained successor to empyrical, pyfolio, and alphalens
- [`fincore_cpp`](https://github.com/cloudQuant/fincore_cpp) — the C++ version of fincore

### Data Platform

- [`opendata`](https://github.com/cloudQuant/opendata) — multi-source financial data middle platform: scheduled ingestion from AKShare, OpenBB and THS, standardized storage in MySQL / PostgreSQL / DolphinDB, cross-source data-quality validation, and REST + WebSocket query services (successor to `akshare_web`)

### bt_api Ecosystem

One standardized API for market data, orders and account events across equities, futures, FX and digital-asset venues.

**Core packages**

- [`bt_api_py`](https://github.com/cloudQuant/bt_api_py) — Python SDK for multi-venue integration with a standardized API
- [`bt_api_base`](https://github.com/cloudQuant/bt_api_base) — base package shared by all adapters
- [`bt_api_gateway`](https://github.com/cloudQuant/bt_api_gateway) — middleware-neutral shared account gateway: market-data fan-out, account/order event routing, and strategy-scoped command delivery
- [`bt_api_execution`](https://github.com/cloudQuant/bt_api_execution) — durable, provider-neutral execution and order-management layer: risk-gated, recoverable parent/child orders
- [`bt_api_transport_zmq`](https://github.com/cloudQuant/bt_api_transport_zmq) — authenticated ZeroMQ transport primitives for bt_api gateways
- [`bt_api_risk`](https://github.com/cloudQuant/bt_api_risk) — unified risk controls
- [`bt_api_monitor`](https://github.com/cloudQuant/bt_api_monitor) — unified monitoring and metrics
- [`bt_api_security`](https://github.com/cloudQuant/bt_api_security) — unified security and compliance controls
- [`bt_api_cpp`](https://github.com/cloudQuant/bt_api_cpp) — the C++ version of bt_api
- [`btapi`](https://github.com/cloudQuant/btapi) — C++ API library: sync / async requests, WebSocket, and FIX

**Broker plugins (14)** — live connectivity for Indian, US and European retail brokers: Zerodha, Upstox, Angel One, Fyers, Dhan, Kotak, IIFL, 5paisa, AliceBlue, Shoonya, Motilal, Groww, Tradier, Saxo.

**Exchange adapters (64)** — including CTP for China futures, Interactive Brokers and MetaTrader 5, alongside major digital-asset venues such as Binance, OKX, Bybit, Coinbase and Kraken. The full registry lives in `bt_api_py`.

## Technical Interests

- Python quant libraries and services
- C++ strategy engines and bindings
- Rust for performance-critical systems
- Exchange / broker connectivity and market-data systems
- Data warehousing (MySQL, PostgreSQL, DolphinDB)
- Factor research, portfolio analytics and risk models
- CI/CD, cross-platform packaging and release engineering
- AI-native developer tooling (MCP, agent skills)

## Contact

- Email: `yunjinqi@gmail.com`

If you're building something around quant research, trading systems, analytics infrastructure, broker/exchange connectivity, or trading strategies, feel free to reach out.

---

<a id="chinese-version" name="chinese-version"></a>

## 中文版本

我是 `cloudQuant`，一名专注于系统化交易背后基础设施的量化工程师：高性能回测与分析、行情数据平台，以及多市场交易执行。以 Python 为主，在性能或工具链需要时使用 C++ / Rust / TypeScript。

## 关于我

- 量化相关资质：`CFA`、`FRM`、`CIIA`、`CFP`
- 主要市场覆盖：中国 A 股、国内期货，以及跨市场 / 多资产研究
- 主要兴趣方向：
  - 算法交易与策略研究
  - 回测系统与策略工程
  - 组合、因子与风险分析
  - 行情数据工程与数据质量
  - 高性能系统（C++ / Rust / pybind11）
  - AI 辅助研究与开发工具

## 近两年的主要工作方向

近两年我在 GitHub 上的工作主要集中在四个项目生态：

- `backtrader` — 性能优化的 Backtrader 分支（Python + C++）、其 Web 平台，以及 AI 原生策略开发工作流
- `fincore` — 统一的量化绩效、风险与因子分析库
- `opendata` — 多源金融数据中台（取数 → 数仓 → REST / WebSocket 服务）
- `bt_api` — 标准化多市场交易 API 生态（交易所适配器、券商插件、网关、执行与风控层）

近期活跃仓库：`opendata`、`backtrader`、`fincore`、`fincore_cpp`、`ai-for-investor`。

## 当前关注重点

- 构建更适合生产环境的 Python 量化 SDK 与服务
- 行情数据基础设施：多源采集、跨源校验与统一查询服务
- 研究和优化不同风格的交易策略
- 探索 C++ / Rust / pybind11 在量化基础设施中的加速路径
- 打通研究、回测、实盘执行和数据工具之间的完整工作流
- 让量化系统更容易与 MCP / AI 原生接口结合

## 感兴趣的策略方向

- 趋势跟踪（CTA）
- 多因子选股
- 均值回归
- 动量策略
- 统计套利
- 事件驱动策略
- 套利与价差交易
- 做市策略
- 高频交易研究

## 代表项目

### Backtrader 生态

核心框架与平台：

- [`backtrader`](https://github.com/cloudQuant/backtrader) — 高性能 Python 回测与实盘框架：向量化 / 事件驱动双模式、多周期数据、50+ 指标，并提供 pybind11 加速的 C++ wheel
- [`backtrader_cpp`](https://github.com/cloudQuant/backtrader_cpp) — Backtrader 引擎的 C++ 重写
- [`ai-for-investor`](https://github.com/cloudQuant/ai-for-investor) — AI 驱动的量化研究平台（Vue 3 + FastAPI）：知识库问答、Backtrader 策略编写与版本管理、数据质量预检、回测与稳健性 / 参数优化、模拟交易与组合风险观察 —— 后续替代 `backtrader_web`

AI 原生工作流：

- [`backtrader-mcp`](https://github.com/cloudQuant/backtrader-mcp) — 本地优先的 MCP Server：不可变数据集、私有草稿、受限子进程回测，30 个类型化工具
- [`backtrader-skills`](https://github.com/cloudQuant/backtrader-skills) — 面向 AI 编程代理（Claude Code、Codex、OpenCode）的离线策略编写 / 审查 / 测试技能
- [`backtrader-agent`](https://github.com/cloudQuant/backtrader-agent) — 离线优先的策略编写代理运行时：StrategySpec 校验、静态审查、哈希绑定审批

### Fincore 生态

- [`fincore`](https://github.com/cloudQuant/fincore) — 量化绩效与风险分析：150+ 金融指标、组合优化、蒙特卡洛模拟与归因分析，是 empyrical / pyfolio / alphalens 的活跃维护后继
- [`fincore_cpp`](https://github.com/cloudQuant/fincore_cpp) — C++ 版

### 数据平台

- [`opendata`](https://github.com/cloudQuant/opendata) — 多源金融数据中台：定时从 AKShare、OpenBB、同花顺等数据源采集，统一落库至 MySQL / PostgreSQL / DolphinDB，跨源校验数据质量，并以 REST + WebSocket 对外提供查询与订阅服务（前身为 `akshare_web`）

### bt_api 生态

一套标准化 API，覆盖行情、订单与账户事件，连接股票、期货、外汇与数字资产等多类交易场所。

核心包：

- [`bt_api_py`](https://github.com/cloudQuant/bt_api_py) — 多市场统一接口 Python SDK
- [`bt_api_base`](https://github.com/cloudQuant/bt_api_base) — 适配器共享基础包
- [`bt_api_gateway`](https://github.com/cloudQuant/bt_api_gateway) — 与中间件无关的统一账户网关：行情分发、账户 / 订单事件路由、按策略隔离的指令投递
- [`bt_api_execution`](https://github.com/cloudQuant/bt_api_execution) — 持久化、与通道无关的执行与订单管理层：风控闸门下的父子订单聚合与恢复
- [`bt_api_transport_zmq`](https://github.com/cloudQuant/bt_api_transport_zmq) — 带认证的 ZeroMQ 传输原语
- [`bt_api_risk`](https://github.com/cloudQuant/bt_api_risk) — 统一风控模块
- [`bt_api_monitor`](https://github.com/cloudQuant/bt_api_monitor) — 统一监控与指标模块
- [`bt_api_security`](https://github.com/cloudQuant/bt_api_security) — 统一安全与合规模块
- [`bt_api_cpp`](https://github.com/cloudQuant/bt_api_cpp) — C++ 版
- [`btapi`](https://github.com/cloudQuant/btapi) — C++ API 库：同步 / 异步请求、WebSocket、FIX

**券商插件（14 个）**：面向印度、美国与欧洲零售券商的实盘接入，包括 Zerodha、Upstox、Angel One、Fyers、Dhan、Kotak、IIFL、5paisa、AliceBlue、Shoonya、Motilal、Groww、Tradier、Saxo。

**交易所适配器（64 个）**：覆盖国内期货 CTP、Interactive Brokers、MetaTrader 5，以及 Binance、OKX、Bybit、Coinbase、Kraken 等数字资产交易场所。完整清单见 `bt_api_py` 的插件注册表。

## 技术兴趣

- Python 量化库与服务
- C++ 策略引擎与绑定
- Rust 高性能系统
- 券商与交易所接口集成、行情数据系统
- 数据仓库（MySQL、PostgreSQL、DolphinDB）
- 因子研究、组合分析与风险模型
- CI/CD、跨平台打包与发布工程
- AI 原生开发工具（MCP、Agent Skills）

## 联系方式

- Email: `yunjinqi@gmail.com`

如果你正在做量化研究、交易系统、分析基础设施、券商 / 交易所接口，或者交易策略相关项目，欢迎交流。
