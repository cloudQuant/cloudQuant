# API Reference

This document provides a quick reference to all API-related documentation in the cloudQuant ecosystem.

## BMAD Framework APIs

### Core APIs

| API          | Description             | Location                |
| ------------ | ----------------------- | ----------------------- |
| Workflow API | BMAD workflow execution | `_bmad/core/workflows/` |
| Agent API    | AI agent configuration  | `_bmad/core/agents/`    |

### Module APIs

| Module | API Type | Description                     |
| ------ | -------- | ------------------------------- |
| BMM    | Workflow | Business methodology workflows  |
| CIS    | Workflow | Creative intelligence workflows |
| GDS    | Workflow | Game development workflows      |
| TEA    | Workflow | Test engineering workflows      |
| WDS    | Workflow | Web design system workflows     |

## External Project APIs

cloudQuant maintains several API libraries for quantitative trading:

### Trading APIs

| Project                                                | Language | Description                |
| ------------------------------------------------------ | -------- | -------------------------- |
| [bt_api_py](https://github.com/cloudQuant/bt_api_py)   | Python   | Multi-exchange unified API |
| [pymt5](https://github.com/cloudQuant/pymt5)           | Python   | MT5 Web Terminal API       |
| [ctp-python](https://github.com/cloudQuant/ctp-python) | Python   | CTP futures interface      |

### Data APIs

| Project                                                  | Language | Description       |
| -------------------------------------------------------- | -------- | ----------------- |
| [akshare_web](https://github.com/cloudQuant/akshare_web) | Python   | Market data tools |

### Analytics APIs

| Project                                              | Language | Description         |
| ---------------------------------------------------- | -------- | ------------------- |
| [alphalens](https://github.com/cloudQuant/alphalens) | Python   | Factor analysis     |
| [pyfolio](https://github.com/cloudQuant/pyfolio)     | Python   | Portfolio analytics |
| [empyrical](https://github.com/cloudQuant/empyrical) | Python   | Performance metrics |

## API Design Principles

1. **RESTful Design** - Follow REST architecture principles
2. **Versioning** - API versions via URL prefix
3. **Error Handling** - Consistent error response format
4. **Documentation** - OpenAPI/Swagger specifications

## Authentication

Most external APIs require authentication:

```python
from bt_api_py import ExchangeAPI

api = ExchangeAPI(
    api_key="your-api-key",
    secret="your-secret"
)
```

> ⚠️ **Security Note**: Never commit API keys to version control. Use environment variables.
