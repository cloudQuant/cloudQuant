# 最佳实践

本文档收集了 cloudQuant 项目开发的最佳实践和规范。

## 📝 代码风格

### Python 代码规范

```python
# 使用类型注解
def calculate_returns(prices: list[float]) -> list[float]:
    """计算收益率序列"""
    return [prices[i] / prices[i - 1] - 1 for i in range(1, len(prices))]


# 使用 dataclass 或 Pydantic 模型
from dataclasses import dataclass

@dataclass
class Order:
    symbol: str
    side: str  # 'buy' | 'sell'
    quantity: float
    price: float | None = None
```

### TypeScript 代码规范

```typescript
// 使用接口定义类型
interface Strategy {
  id: string
  name: string
  execute(data: MarketData): Signal
}

// 使用 const enum 优化性能
const enum OrderSide {
  Buy = "BUY",
  Sell = "SELL",
}
```

## 📋 命名规范

### 文件命名

| 类型        | 规范       | 示例                 |
| ----------- | ---------- | -------------------- |
| Python 模块 | snake_case | `strategy_runner.py` |
| Python 类   | PascalCase | `StrategyRunner`     |
| TypeScript  | camelCase  | `strategyRunner.ts`  |
| 配置文件    | kebab-case | `docker-compose.yml` |
| 文档        | kebab-case | `quick-start.md`     |

### 变量命名

```python
# 好的命名
max_drawdown = 0.1
sharpe_ratio = 1.5
order_quantity = 100

# 不好的命名
md = 0.1
sr = 1.5
oq = 100
```

## 🔀 Git 提交规范

### Conventional Commits

```text
<type>(<scope>): <subject>

<body>

<footer>
```

### 类型定义

| 类型     | 描述      | 示例                             |
| -------- | --------- | -------------------------------- |
| feat     | 新功能    | feat(backtest): 添加多品种支持   |
| fix      | Bug 修复  | fix(order): 修复订单重复问题     |
| docs     | 文档更改  | docs(api): 更新 API 文档         |
| style    | 代码格式  | style: 格式化代码                |
| refactor | 重构      | refactor(strategy): 优化策略执行 |
| test     | 测试      | test(backtest): 添加单元测试     |
| chore    | 构建/工具 | chore: 更新依赖版本              |

### 提交示例

```bash
# 好的提交
feat(backtest): 添加多时间框架回测支持

- 支持 1m, 5m, 15m, 1h, 4h, 1d 时间框架
- 添加时间框架转换工具
- 更新相关测试

Closes #123

# 不好的提交
update backtest
```

## 🧪 测试规范

### 测试组织

```text
tests/
├── unit/              # 单元测试
│   ├── test_strategy.py
│   └── test_backtest.py
├── integration/       # 集成测试
│   └── test_api.py
└── e2e/              # 端到端测试
    └── test_workflow.py
```

### 测试命名

```python
# 测试函数命名: test_<被测函数>_<场景>_<预期结果>
def test_calculate_returns_normal_case_returns_positive():
    ...

def test_calculate_returns_empty_input_raises_error():
    ...
```

### 测试覆盖率

```python
# 目标覆盖率
# - 核心模块: 90%+
# - 工具模块: 80%+
# - API 层: 70%+
```

## 📚 文档规范

### Markdown 格式

````markdown
# 一级标题

## 二级标题

正文内容，使用**粗体**和*斜体*强调。

### 代码块

```python
def example():
    pass
```
````

### 列表

- 无序列表项 1
- 无序列表项 2

1. 有序列表项 1
2. 有序列表项 2

````markdown
# 示例文档

### 文档结构

每个文档应包含：

1. 标题和概述
2. 目录（长文档）
3. 正文内容
4. 示例代码
5. 相关链接
6. 最后更新日期

## 🔐 安全规范

### 敏感信息处理

```python
# 使用环境变量
import os

API_KEY = os.environ.get('API_KEY')

# 不要硬编码
# API_KEY = "sk-xxxxx"  # ❌ 错误
```
````

### 输入验证

```python
from pydantic import BaseModel, validator

class OrderRequest(BaseModel):
    symbol: str
    quantity: float

    @validator('quantity')
    def validate_quantity(cls, v):
        if v <= 0:
            raise ValueError('quantity must be positive')
        return v
```

## ⚡ 性能优化

### 数据处理

```python
# 使用向量化操作
import numpy as np

# 好的做法
returns = np.diff(prices) / prices[:-1]

# 不好的做法
returns = []
for i in range(1, len(prices)):
    returns.append(prices[i] / prices[i-1] - 1)
```

### 缓存策略

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_historical_data(symbol: str, date: str):
    """缓存历史数据查询"""
    ...
```

## 🤝 AI 协作最佳实践

### 提示词工程

```markdown
# 好的提示词

[CONTEXT]: 我正在开发一个量化回测系统
[GOAL]: 需要实现一个高效的订单撮合引擎

[CONSTRAINTS]:

- 支持限价单和市价单
- 考虑滑点模型
- 使用 Python + Numba 加速
```

### 代码审查要点

- [ ] 代码是否清晰易懂
- [ ] 是否有足够的类型注解
- [ ] 是否处理了边界情况
- [ ] 是否有对应的测试
- [ ] 文档是否完整

## 📊 项目结构规范

```text
cloudQuant/
├── src/                    # 源代码
│   ├── core/              # 核心模块
│   ├── strategies/        # 策略模块
│   ├── backtest/          # 回测引擎
│   └── api/               # API 服务
├── tests/                 # 测试代码
├── docs/                  # 文档
├── scripts/               # 脚本工具
├── configs/               # 配置文件
└── .github/               # GitHub 配置
```

## 🔗 相关资源

- [Python PEP 8](https://peps.python.org/pep-0008/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

---

_最后更新: 2026-03-13_
