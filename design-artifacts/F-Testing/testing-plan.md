# 测试计划 (Testing Plan)

## 文档信息

| 字段 | 值 |
|------|-----|
| 项目 | cloudQuant |
| 版本 | 0.1.0 |
| 作者 | cloudQuant Team |
| 日期 | 2026-03-13 |

## 1. 测试概述

### 1.1 测试目标

- 确保核心功能按预期工作
- 验证性能指标达到要求
- 保证系统安全性和稳定性
- 提供质量信心

### 1.2 测试范围

| 模块 | 范围 | 优先级 |
|------|------|--------|
| 策略管理 | 创建、编辑、删除、版本管理 | 高 |
| 回测引擎 | 配置、执行、报告生成 | 高 |
| 实盘交易 | 连接、部署、监控 | 高 |
| 风险管理 | 止损止盈、仓位控制 | 中 |
| 数据服务 | 行情、历史数据 | 中 |

### 1.3 测试原则

1. **自动化优先**: 尽可能自动化测试
2. **测试左移**: 尽早开始测试
3. **持续测试**: 集成到 CI/CD
4. **风险驱动**: 优先测试高风险功能

## 2. 测试策略

### 2.1 测试金字塔

```text
        ┌─────────┐
        │   E2E   │  10%
        │  Tests  │
        ├─────────┤
        │集成测试  │  20%
        │         │
        ├─────────┤
        │单元测试  │  70%
        │         │
        └─────────┘
```

### 2.2 测试工具

| 类型 | 工具 | 用途 |
|------|------|------|
| 单元测试 | pytest | Python 单元测试 |
| 单元测试 | Vitest | TypeScript 单元测试 |
| 集成测试 | pytest + requests | API 测试 |
| E2E 测试 | Playwright | 端到端测试 |
| 性能测试 | Locust | 负载测试 |
| 覆盖率 | pytest-cov | 代码覆盖率 |

### 2.3 测试环境

| 环境 | 用途 | 配置 |
|------|------|------|
| 开发环境 | 开发阶段测试 | 本地 Docker |
| 测试环境 | CI 自动测试 | 云端 Kubernetes |
| 预生产环境 | 发布前验证 | 类生产配置 |
| 生产环境 | 监控和冒烟测试 | 生产配置 |

## 3. 单元测试

### 3.1 测试范围

| 模块 | 覆盖率目标 | 说明 |
|------|-----------|------|
| 核心引擎 | 90% | 回测引擎、订单撮合 |
| 策略模块 | 80% | 策略执行、信号生成 |
| 数据模块 | 80% | 数据获取、处理 |
| API 层 | 70% | 路由、验证 |
| 工具模块 | 60% | 辅助函数 |

### 3.2 测试用例示例

#### TC-001: 计算收益率

```python
def test_calculate_returns_normal_case():
    """测试正常收益率计算"""
    prices = [100, 110, 99, 105]
    expected = [0.10, -0.10, 0.0606]
    
    result = calculate_returns(prices)
    
    assert len(result) == 3
    for r, e in zip(result, expected):
        assert abs(r - e) < 0.0001

def test_calculate_returns_empty_input():
    """测试空输入"""
    with pytest.raises(ValueError):
        calculate_returns([])
```

#### TC-002: 订单撮合

```python
def test_order_match_limit_order():
    """测试限价单撮合"""
    order = Order(
        side='buy',
        type='limit',
        price=100,
        quantity=1
    )
    market_price = 99
    
    result = match_order(order, market_price)
    
    assert result.filled == True
    assert result.fill_price == 100

def test_order_match_market_order():
    """测试市价单撮合"""
    order = Order(
        side='buy',
        type='market',
        quantity=1
    )
    market_price = 100
    
    result = match_order(order, market_price)
    
    assert result.filled == True
    assert result.fill_price == 100
```

## 4. 集成测试

### 4.1 API 测试

#### TC-010: 创建策略 API

```python
def test_create_strategy_api(client, auth_headers):
    """测试创建策略 API"""
    data = {
        "name": "Test Strategy",
        "code": "def execute(data): pass",
        "parameters": {}
    }
    
    response = client.post(
        "/api/v1/strategies",
        json=data,
        headers=auth_headers
    )
    
    assert response.status_code == 201
    assert response.json()["name"] == "Test Strategy"
    assert "id" in response.json()
```

#### TC-011: 运行回测 API

```python
def test_run_backtest_api(client, auth_headers, sample_strategy):
    """测试运行回测 API"""
    data = {
        "strategyId": sample_strategy.id,
        "startDate": "2025-01-01",
        "endDate": "2025-12-31",
        "initialCapital": 100000
    }
    
    response = client.post(
        "/api/v1/backtest",
        json=data,
        headers=auth_headers
    )
    
    assert response.status_code == 202
    assert "jobId" in response.json()
```

### 4.2 数据库测试

```python
def test_strategy_crud(db_session):
    """测试策略 CRUD 操作"""
    # Create
    strategy = Strategy(name="Test", code="pass")
    db_session.add(strategy)
    db_session.commit()
    
    # Read
    found = db_session.query(Strategy).first()
    assert found.name == "Test"
    
    # Update
    found.name = "Updated"
    db_session.commit()
    
    # Delete
    db_session.delete(found)
    db_session.commit()
    assert db_session.query(Strategy).count() == 0
```

## 5. 回测引擎测试

### 5.1 历史数据验证

| 测试项 | 描述 | 预期结果 |
|--------|------|---------|
| 数据完整性 | 检查无缺失 | 无缺失数据 |
| 数据准确性 | 与源数据对比 | 误差 < 0.01% |
| 时间排序 | 确保时间有序 | 时间递增 |

### 5.2 性能基准测试

```python
def test_backtest_performance(benchmark, sample_data):
    """测试回测性能"""
    result = benchmark(run_backtest, sample_data)
    
    # 1000 条数据应在 1 秒内完成
    assert benchmark.stats.mean < 1.0
```

### 5.3 精度验证

```python
def test_backtest_accuracy():
    """测试回测精度"""
    # 使用已知结果的策略
    strategy = KnownResultStrategy()
    
    result = run_backtest(strategy, known_data)
    
    # 验证关键指标
    assert abs(result.total_return - expected_return) < 0.001
    assert abs(result.sharpe_ratio - expected_sharpe) < 0.01
```

## 6. 实盘交易测试

### 6.1 模拟交易测试

```python
@pytest.mark.integration
def test_paper_trading_order():
    """测试模拟交易下单"""
    client = PaperTradingClient()
    
    order = client.create_order(
        symbol="BTC/USDT",
        side="buy",
        type="market",
        quantity=0.01
    )
    
    assert order.status == "filled"
    assert order.filled_quantity == 0.01
```

### 6.2 订单执行测试

| 测试项 | 描述 | 预期结果 |
|--------|------|---------|
| 限价单 | 限价单执行 | 价格匹配 |
| 市价单 | 市价单执行 | 立即成交 |
| 止损单 | 触发止损 | 条件触发时执行 |
| 订单取消 | 取消未成交订单 | 订单取消成功 |

### 6.3 异常处理测试

```python
def test_order_timeout_handling():
    """测试订单超时处理"""
    with mock.patch('time.sleep') as mock_sleep:
        mock_sleep.side_effect = TimeoutError()
        
        with pytest.raises(OrderTimeoutError):
            execute_order(order)
```

## 7. 性能测试

### 7.1 负载测试

```python
# locustfile.py
class BacktestUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def run_backtest(self):
        self.client.post("/api/v1/backtest", json={
            "strategyId": "test-strategy",
            "startDate": "2025-01-01",
            "endDate": "2025-12-31"
        })
```

### 7.2 性能指标

| 指标 | 目标值 | 测试方法 |
|------|--------|---------|
| API 响应时间 | < 100ms (P95) | Locust |
| 并发用户 | 100 | Locust |
| 回测吞吐量 | 100/min | Locust |
| 数据库查询 | < 50ms | pgbench |

## 8. 安全测试

### 8.1 认证测试

```python
def test_api_authentication():
    """测试 API 认证"""
    # 无 Token
    response = client.get("/api/v1/strategies")
    assert response.status_code == 401
    
    # 无效 Token
    response = client.get(
        "/api/v1/strategies",
        headers={"Authorization": "Bearer invalid"}
    )
    assert response.status_code == 401
    
    # 有效 Token
    response = client.get(
        "/api/v1/strategies",
        headers=auth_headers
    )
    assert response.status_code == 200
```

### 8.2 授权测试

```python
def test_resource_authorization():
    """测试资源授权"""
    # 用户 A 不能访问用户 B 的资源
    user_a_headers = get_auth_headers(user_a)
    user_b_strategy = create_strategy(user_b)
    
    response = client.get(
        f"/api/v1/strategies/{user_b_strategy.id}",
        headers=user_a_headers
    )
    assert response.status_code == 403
```

### 8.3 安全检查清单

- [ ] SQL 注入防护
- [ ] XSS 防护
- [ ] CSRF 防护
- [ ] API Key 加密存储
- [ ] 敏感数据脱敏
- [ ] 请求频率限制

## 9. 测试用例索引

| ID | 名称 | 类型 | 优先级 | 状态 |
|----|------|------|--------|------|
| TC-001 | 计算收益率 | 单元 | 高 | ⬜ |
| TC-002 | 订单撮合 | 单元 | 高 | ⬜ |
| TC-003 | 策略验证 | 单元 | 高 | ⬜ |
| TC-010 | 创建策略 API | 集成 | 高 | ⬜ |
| TC-011 | 运行回测 API | 集成 | 高 | ⬜ |
| TC-020 | 回测性能 | 性能 | 中 | ⬜ |
| TC-021 | 负载测试 | 性能 | 中 | ⬜ |
| TC-030 | 认证测试 | 安全 | 高 | ⬜ |
| TC-031 | 授权测试 | 安全 | 高 | ⬜ |

## 10. 测试报告

### 10.1 每日报告

- 测试执行数量
- 通过/失败率
- 新增缺陷数
- 阻塞问题

### 10.2 发布报告

- 测试覆盖率
- 性能基准结果
- 安全扫描结果
- 缺陷统计

---

*最后更新: 2026-03-13*
