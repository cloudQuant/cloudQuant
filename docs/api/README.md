# API 文档

本目录包含 cloudQuant 项目的 API 文档和接口规范。

## 📋 API 概览

cloudQuant 项目通过 BMAD 框架提供多种 API 接口:

| 模块 | API 类型   | 描述                  |
| ---- | ---------- | --------------------- |
| Core | 工作流 API | BMAD 核心工作流接口   |
| TEA  | 测试 API   | 自动化测试生成和管理  |
| WDS  | 设计 API   | UI 组件和设计系统集成 |

## 🔌 外部项目 API

cloudQuant 维护的量化交易相关项目 API:

### 交易框架

- [backtrader](https://github.com/cloudQuant/backtrader) - 回测与实盘交易 API
- [bt_api_py](https://github.com/cloudQuant/bt_api_py) - 统一交易所接口 API

### 数据接口

- [akshare_web](https://github.com/cloudQuant/akshare_web) - 市场数据 API
- [pymt5](https://github.com/cloudQuant/pymt5) - MT5 Web Terminal API

### 分析工具

- [alphalens](https://github.com/cloudQuant/alphalens) - 因子分析 API
- [pyfolio](https://github.com/cloudQuant/pyfolio) - 组合分析 API

## 📖 API 设计原则

1. **RESTful 设计**: 遵循 REST 架构原则
2. **版本控制**: API 版本通过 URL 前缀管理
3. **错误处理**: 统一的错误响应格式
4. **文档化**: OpenAPI/Swagger 规范

## 🔐 认证

大多数 API 需要认证:

```python
# 示例：交易所 API 认证
import bt_api_py

api = bt_api_py.ExchangeAPI(
    api_key="your-api-key",
    secret="your-secret"
)
```

---

_最后更新: 2026-03-13_
