# ADR-005: 数据存储架构

## 状态

✅ 已采纳

## 上下文

量化交易平台需要处理多种类型的数据：

- 高频行情数据（每秒数万条）
- 历史回测数据（TB 级别）
- 用户配置和策略数据
- 交易记录和账户信息

需要考虑：

- 写入性能
- 查询效率
- 存储成本
- 数据一致性

## 决策

### 存储分层架构

```text
┌─────────────────────────────────────────────────────┐
│                    应用层                            │
├─────────────────────────────────────────────────────┤
│  Redis (缓存)    │  TimescaleDB (时序)  │  PostgreSQL │
│  - 实时行情      │  - K线数据          │  - 用户数据  │
│  - 会话状态      │  - Tick数据         │  - 策略配置  │
│  - 计算缓存      │  - 交易记录         │  - 系统配置  │
└─────────────────────────────────────────────────────┘
```

### 数据分布策略

| 数据类型  | 存储位置                 | 保留策略 |
| --------- | ------------------------ | -------- |
| 实时行情  | Redis                    | 1 天     |
| Tick 数据 | TimescaleDB              | 1 年     |
| K线数据   | TimescaleDB              | 永久     |
| 交易记录  | PostgreSQL + TimescaleDB | 永久     |
| 用户配置  | PostgreSQL               | 永久     |

### TimescaleDB 超级表设计

```sql
-- K线数据表
CREATE TABLE klines (
    time        TIMESTAMPTZ NOT NULL,
    symbol      VARCHAR(20) NOT NULL,
    interval    VARCHAR(10) NOT NULL,
    open        DECIMAL(20, 8),
    high        DECIMAL(20, 8),
    low         DECIMAL(20, 8),
    close       DECIMAL(20, 8),
    volume      DECIMAL(20, 8),
    PRIMARY KEY (time, symbol, interval)
);

SELECT create_hypertable('klines', 'time');
```

### 数据压缩策略

```sql
-- 自动压缩 7 天前的数据
SELECT add_compression_policy('klines', INTERVAL '7 days');
-- 自动删除 1 年前的 tick 数据
SELECT add_retention_policy('ticks', INTERVAL '1 year');
```

## 后果

### 正面影响

- TimescaleDB 自动分区，无需手动维护
- 压缩率可达 90%，节省存储成本
- Redis 缓存显著提升查询性能
- 清晰的数据分层，便于扩展

### 负面影响

- 需要维护多个数据库实例
- TimescaleDB 学习曲线
- 数据迁移复杂度

### 替代方案

| 方案          | 为何不选                     |
| ------------- | ---------------------------- |
| InfluxDB      | SQL 支持有限                 |
| MongoDB       | 时序查询性能不如 TimescaleDB |
| 纯 PostgreSQL | 超级表和压缩功能缺失         |

## 参考

- [TimescaleDB 最佳实践](https://docs.timescale.com/use-timescale/latest/compression/)
- [Redis 数据结构](https://redis.io/docs/data-types/)

---

_最后更新: 2026-03-13_
