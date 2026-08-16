# Hi, I'm `cloudQuant`

<a id="english-version" name="english-version"></a>

[English](#english-version) | [中文](#chinese-version)

## English Version

Quant focused on algorithmic trading systems, research tooling, broker and exchange integration, and performance-oriented engineering across Python, C++, Rust, and TypeScript.

## About Me

- Quant credentials: `CFA`, `FRM`, `CIIA`, `CFP`
- Main interests:
  - Algorithmic trading
  - Trading strategies and strategy research
  - Backtesting and strategy engineering
  - Portfolio and factor analytics
  - High-performance systems
  - AI-assisted research and developer tooling

## What I've Been Working On Recently

Over the last two years, my GitHub work has concentrated on three project ecosystems: the **backtrader** trading framework and its AI-native tooling, the **fincore** analytics family, and the **bt_api** multi-exchange SDK ecosystem.

Recent active contribution areas include:

- `backtrader` — framework maintenance, CI/CD, compatibility, documentation, and the AI-native workflow (MCP server, agent skills, web platform)
- `bt_api_py` — multi-exchange standardized API SDK, with 64 exchange adapters and 14 broker plugins
- `backtrader_web` — web-based strategy management and execution workflow
- `fincore` — unified quantitative performance & risk analytics toolkit

## Current Focus

- Building production-friendly Python SDKs for quant workflows
- Researching and refining trading strategies across multiple market styles
- Exploring C++ / Rust / pybind / swig acceleration paths for quant infrastructure
- Connecting research, backtesting, live trading, and data tooling into a unified workflow
- Making quant systems easier to use with MCP / AI-native interfaces

## Strategy Interests

- Trend following
- Mean reversion
- Momentum
- Breakout strategies
- Multi-factor stock selection
- Statistical arbitrage
- Market making
- Arbitrage and spread trading
- Event-driven strategies
- High-frequency trading research

## Selected Projects

### Backtrader Ecosystem

**Core framework and platform**

- [`backtrader`](https://github.com/cloudQuant/backtrader) — high-performance Python backtesting & live-trading framework: 45%+ faster than upstream, 50+ indicators, tick-to-daily strategies
- [`backtrader_web`](https://github.com/cloudQuant/backtrader_web) — "AI for Investor" web platform (Vue 3 + FastAPI): research, AI strategy generation, backtesting, paper trading, live execution, and market-data management

**AI-native workflow**

- [`backtrader-mcp`](https://github.com/cloudQuant/backtrader-mcp) — local-first MCP server for AI-assisted strategy development: immutable datasets, private drafts, and bounded subprocess backtests via 30 typed tools
- [`backtrader-skills`](https://github.com/cloudQuant/backtrader-skills) — offline author/review/test skills for AI coding agents (Claude Code, Codex, OpenCode)
- [`backtrader-agent`](https://github.com/cloudQuant/backtrader-agent) — offline-first strategy-authoring agent runtime: StrategySpec validation, static review, hash-bound approvals

**Performance rewrites and variants**

- [`back_trader`](https://github.com/cloudQuant/back_trader) — the C++ version of backtrader *(private)*

### Fincore Ecosystem

- [`fincore`](https://github.com/cloudQuant/fincore) — quantitative performance & risk analytics: 150+ financial metrics, portfolio optimization, Monte Carlo simulation, and attribution — the actively maintained successor to empyrical, pyfolio, and alphalens
- [`fincore_cpp`](https://github.com/cloudQuant/fincore_cpp) — the C++ version of fincore

### bt_api Ecosystem

**Core packages**

- [`bt_api_py`](https://github.com/cloudQuant/bt_api_py) — Python SDK for multi-exchange integration with a standardized API
- [`bt_api_base`](https://github.com/cloudQuant/bt_api_base) — base package shared by all adapters
- [`bt_api_cpp`](https://github.com/cloudQuant/bt_api_cpp) — the C++ version of bt_api
- [`btapi`](https://github.com/cloudQuant/btapi) — C++ API library: sync/async requests, WebSocket, and FIX
- [`bt_api_monitoring`](https://github.com/cloudQuant/bt_api_monitoring) — unified monitoring and metrics module
- [`bt_api_risk`](https://github.com/cloudQuant/bt_api_risk) — unified risk controls module
- [`bt_api_security`](https://github.com/cloudQuant/bt_api_security) — unified security controls and compliance module

**Exchange adapters (64)**

| | | | |
| --- | --- | --- | --- |
| [`bt_api_bequant`](https://github.com/cloudQuant/bt_api_bequant) | [`bt_api_bigone`](https://github.com/cloudQuant/bt_api_bigone) | [`bt_api_binance`](https://github.com/cloudQuant/bt_api_binance) | [`bt_api_bingx`](https://github.com/cloudQuant/bt_api_bingx) |
| [`bt_api_bitbank`](https://github.com/cloudQuant/bt_api_bitbank) | [`bt_api_bitfinex`](https://github.com/cloudQuant/bt_api_bitfinex) | [`bt_api_bitflyer`](https://github.com/cloudQuant/bt_api_bitflyer) | [`bt_api_bitget`](https://github.com/cloudQuant/bt_api_bitget) |
| [`bt_api_bithumb`](https://github.com/cloudQuant/bt_api_bithumb) | [`bt_api_bitinka`](https://github.com/cloudQuant/bt_api_bitinka) | [`bt_api_bitmart`](https://github.com/cloudQuant/bt_api_bitmart) | [`bt_api_bitrue`](https://github.com/cloudQuant/bt_api_bitrue) |
| [`bt_api_bitso`](https://github.com/cloudQuant/bt_api_bitso) | [`bt_api_bitstamp`](https://github.com/cloudQuant/bt_api_bitstamp) | [`bt_api_bitunix`](https://github.com/cloudQuant/bt_api_bitunix) | [`bt_api_bitvavo`](https://github.com/cloudQuant/bt_api_bitvavo) |
| [`bt_api_btbns`](https://github.com/cloudQuant/bt_api_btbns) | [`bt_api_btc_markets`](https://github.com/cloudQuant/bt_api_btc_markets) | [`bt_api_btcturk`](https://github.com/cloudQuant/bt_api_btcturk) | [`bt_api_buda`](https://github.com/cloudQuant/bt_api_buda) |
| [`bt_api_bydfi`](https://github.com/cloudQuant/bt_api_bydfi) | [`bt_api_bybit`](https://github.com/cloudQuant/bt_api_bybit) | [`bt_api_coinbase`](https://github.com/cloudQuant/bt_api_coinbase) | [`bt_api_coincheck`](https://github.com/cloudQuant/bt_api_coincheck) |
| [`bt_api_coindcx`](https://github.com/cloudQuant/bt_api_coindcx) | [`bt_api_coinex`](https://github.com/cloudQuant/bt_api_coinex) | [`bt_api_coinone`](https://github.com/cloudQuant/bt_api_coinone) | [`bt_api_coinspot`](https://github.com/cloudQuant/bt_api_coinspot) |
| [`bt_api_coinswitch`](https://github.com/cloudQuant/bt_api_coinswitch) | [`bt_api_cryptocom`](https://github.com/cloudQuant/bt_api_cryptocom) | [`bt_api_ctp`](https://github.com/cloudQuant/bt_api_ctp) | [`bt_api_dydx`](https://github.com/cloudQuant/bt_api_dydx) |
| [`bt_api_exmo`](https://github.com/cloudQuant/bt_api_exmo) | [`bt_api_foxbit`](https://github.com/cloudQuant/bt_api_foxbit) | [`bt_api_gateio`](https://github.com/cloudQuant/bt_api_gateio) | [`bt_api_gemini`](https://github.com/cloudQuant/bt_api_gemini) |
| [`bt_api_giottus`](https://github.com/cloudQuant/bt_api_giottus) | [`bt_api_gmx`](https://github.com/cloudQuant/bt_api_gmx) | [`bt_api_hitbtc`](https://github.com/cloudQuant/bt_api_hitbtc) | [`bt_api_htx`](https://github.com/cloudQuant/bt_api_htx) |
| [`bt_api_hyperliquid`](https://github.com/cloudQuant/bt_api_hyperliquid) | [`bt_api_ib_web`](https://github.com/cloudQuant/bt_api_ib_web) | [`bt_api_independent_reserve`](https://github.com/cloudQuant/bt_api_independent_reserve) | [`bt_api_korbit`](https://github.com/cloudQuant/bt_api_korbit) |
| [`bt_api_kraken`](https://github.com/cloudQuant/bt_api_kraken) | [`bt_api_kucoin`](https://github.com/cloudQuant/bt_api_kucoin) | [`bt_api_latoken`](https://github.com/cloudQuant/bt_api_latoken) | [`bt_api_localbitcoins`](https://github.com/cloudQuant/bt_api_localbitcoins) |
| [`bt_api_luno`](https://github.com/cloudQuant/bt_api_luno) | [`bt_api_mercado_bitcoin`](https://github.com/cloudQuant/bt_api_mercado_bitcoin) | [`bt_api_mexc`](https://github.com/cloudQuant/bt_api_mexc) | [`bt_api_mt5`](https://github.com/cloudQuant/bt_api_mt5) |
| [`bt_api_okx`](https://github.com/cloudQuant/bt_api_okx) | [`bt_api_phemex`](https://github.com/cloudQuant/bt_api_phemex) | [`bt_api_poloniex`](https://github.com/cloudQuant/bt_api_poloniex) | [`bt_api_ripio`](https://github.com/cloudQuant/bt_api_ripio) |
| [`bt_api_satoshitango`](https://github.com/cloudQuant/bt_api_satoshitango) | [`bt_api_swyftx`](https://github.com/cloudQuant/bt_api_swyftx) | [`bt_api_upbit`](https://github.com/cloudQuant/bt_api_upbit) | [`bt_api_valr`](https://github.com/cloudQuant/bt_api_valr) |
| [`bt_api_wazirx`](https://github.com/cloudQuant/bt_api_wazirx) | [`bt_api_yobit`](https://github.com/cloudQuant/bt_api_yobit) | [`bt_api_zaif`](https://github.com/cloudQuant/bt_api_zaif) | [`bt_api_zebpay`](https://github.com/cloudQuant/bt_api_zebpay) |

**Broker plugins (14)**

[`bt_api_5paisa`](https://github.com/cloudQuant/bt_api_5paisa) · [`bt_api_aliceblue`](https://github.com/cloudQuant/bt_api_aliceblue) · [`bt_api_angelone`](https://github.com/cloudQuant/bt_api_angelone) · [`bt_api_dhan`](https://github.com/cloudQuant/bt_api_dhan) · [`bt_api_fyers`](https://github.com/cloudQuant/bt_api_fyers) · [`bt_api_groww`](https://github.com/cloudQuant/bt_api_groww) · [`bt_api_iifl`](https://github.com/cloudQuant/bt_api_iifl) · [`bt_api_kotak`](https://github.com/cloudQuant/bt_api_kotak) · [`bt_api_motilal`](https://github.com/cloudQuant/bt_api_motilal) · [`bt_api_saxo`](https://github.com/cloudQuant/bt_api_saxo) · [`bt_api_shoonya`](https://github.com/cloudQuant/bt_api_shoonya) · [`bt_api_tradier`](https://github.com/cloudQuant/bt_api_tradier) · [`bt_api_upstox`](https://github.com/cloudQuant/bt_api_upstox) · [`bt_api_zerodha`](https://github.com/cloudQuant/bt_api_zerodha)

## Technical Interests

- Python quant libraries
- C++ strategy engines and bindings
- Rust for performance-critical systems
- Exchange and broker API integration
- Factor research and portfolio analytics
- Cross-platform automation and release engineering

## Contact

- Email: `yunjinqi@gmail.com`

If you're building something around quant research, trading systems, analytics infrastructure, broker/exchange connectivity, or trading strategies, feel free to reach out.

---

<a id="chinese-version" name="chinese-version"></a>

## 中文版本

我是 `cloudQuant`，一名专注于量化交易系统、研究工具、券商与交易所接口集成，以及 Python、C++、Rust、TypeScript 高性能工程实践的 `quant`。

## 关于我

- 量化相关资质：`CFA`、`FRM`、`CIIA`、`CFP`
- 主要兴趣方向：
  - 算法交易
  - 交易策略与策略研究
  - 回测系统与策略工程
  - 组合分析与因子研究
  - 高性能系统
  - AI 辅助研究与开发工具

## 近两年的主要工作方向

近两年我在 GitHub 上的工作主要集中在三大项目生态：**backtrader** 交易框架及其 AI 原生工具链、**fincore** 分析库系列，以及 **bt_api** 多交易所 SDK 生态。

近期比较活跃的仓库方向包括：

- `backtrader` — 框架维护、CI/CD、兼容性、文档，以及 AI 原生工作流（MCP Server、Agent 技能、Web 平台）
- `bt_api_py` — 多交易所统一接口 SDK，含 64 个交易所适配器与 14 个券商插件
- `backtrader_web` — 基于 Web 的策略管理与执行平台
- `fincore` — 统一的量化绩效与风险分析工具包

## 当前关注重点

- 构建更适合生产环境的 Python 量化 SDK
- 提升交易类库的跨平台可靠性与 CI/CD 质量
- 研究和优化不同风格的交易策略
- 探索 C++ / Rust / Cython 在量化基础设施中的加速路径
- 打通研究、回测、实盘执行和数据工具之间的完整工作流
- 让量化系统更容易与 MCP / AI 原生接口结合

## 感兴趣的策略方向

- 趋势跟踪
- 均值回归
- 动量策略
- 突破策略
- 多因子选股
- 统计套利
- 做市策略
- 套利与价差交易
- 事件驱动策略
- 高频交易研究

## 代表项目

### Backtrader 生态

核心框架与平台：

- [`backtrader`](https://github.com/cloudQuant/backtrader) — 高性能 Python 回测与实盘框架：比上游快 45%+，50+ 指标，支持从 tick 到日线策略
- [`backtrader_web`](https://github.com/cloudQuant/backtrader_web) — "AI for Investor" Web 平台（Vue 3 + FastAPI）：研究、AI 策略生成、回测、模拟盘、实盘执行与行情数据管理

AI 原生工作流：

- [`backtrader-mcp`](https://github.com/cloudQuant/backtrader-mcp) — 本地优先的 MCP Server：不可变数据集、私有草稿、受限子进程回测，30 个类型化工具
- [`backtrader-skills`](https://github.com/cloudQuant/backtrader-skills) — 面向 AI 编程代理（Claude Code、Codex、OpenCode）的离线策略编写 / 审查 / 测试技能
- [`backtrader-agent`](https://github.com/cloudQuant/backtrader-agent) — 离线优先的策略编写代理运行时：StrategySpec 校验、静态审查、哈希绑定审批

性能重写与变体：

- [`back_trader`](https://github.com/cloudQuant/back_trader) — C++ 版 *（私有）*


### Fincore 生态

- [`fincore`](https://github.com/cloudQuant/fincore) — 量化绩效与风险分析：150+ 金融指标、组合优化、蒙特卡洛模拟与归因分析，是 empyrical / pyfolio / alphalens 的活跃维护后继
- [`fincore_cpp`](https://github.com/cloudQuant/fincore_cpp) — C++ 版

### bt_api 生态

核心包：

- [`bt_api_py`](https://github.com/cloudQuant/bt_api_py) — 多交易所统一接口 Python SDK
- [`bt_api_base`](https://github.com/cloudQuant/bt_api_base) — 适配器共享基础包
- [`bt_api_cpp`](https://github.com/cloudQuant/bt_api_cpp) — C++ 版
- [`btapi`](https://github.com/cloudQuant/btapi) — C++ API 库：同步 / 异步请求、WebSocket、FIX
- [`bt_api_monitoring`](https://github.com/cloudQuant/bt_api_monitoring) — 统一监控与指标模块
- [`bt_api_risk`](https://github.com/cloudQuant/bt_api_risk) — 统一风控模块
- [`bt_api_security`](https://github.com/cloudQuant/bt_api_security) — 统一安全与合规模块

64 个交易所适配器与 14 个券商插件的完整清单，见上方英文部分的 [bt_api Ecosystem](#bt_api-ecosystem)。

## 技术兴趣

- Python 量化库
- C++ 策略引擎与绑定
- Rust 高性能系统
- 券商与交易所接口集成
- 因子研究与组合分析
- 跨平台自动化与发布工程

## 联系方式

- Email: `yunjinqi@gmail.com`

如果你正在做量化研究、交易系统、分析基础设施、券商 / 交易所接口，或者交易策略相关项目，欢迎交流。
