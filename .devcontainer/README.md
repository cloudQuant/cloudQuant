# cloudQuant 开发环境

这个目录包含开发容器配置，用于在 Docker 容器中创建一致的开发环境。

## 快速开始

### 前置要求

- Docker Desktop
- VS Code + Dev Containers 扩展
- 至少 8GB 可用内存

### 启动开发容器

1. 在 VS Code 中打开项目
2. 按 `F1` 或 `Ctrl+Shift+P`
3. 选择 "Dev Containers: Reopen in Container"
4. 等待容器构建完成

### 服务端口

| 服务 | 端口 | 用途 |
|------|------|------|
| API Server | 8000 | FastAPI 服务 |
| Streamlit | 8501 | 数据可视化 |
| PostgreSQL | 5432 | 主数据库 |
| TimescaleDB | 5433 | 时序数据库 |
| Redis | 6379 | 缓存服务 |
| Kafka | 9092 | 消息队列 |

## 开发工具

### 已安装的工具

- Python 3.11
- Node.js 20
- Docker (Docker-in-Docker)
- GitHub CLI
- git

### VS Code 扩展

- Python + Pylance
- Prettier
- Markdown All in One
- markdownlint
- Even Better TOML
- YAML
- Docker
- GitHub Copilot

## 数据库初始化

容器启动后，运行以下命令初始化数据库：

```bash
# 创建 TimescaleDB 扩展
psql -h timescaledb -U cloudquant -d timeseries -c "CREATE EXTENSION IF NOT EXISTS timescaledb;"

# 运行迁移脚本
alembic upgrade head
```

## 故障排除

### 容器启动失败

```bash
# 清理并重建
docker-compose down -v
docker-compose up -d
```

### 端口冲突

修改 `docker-compose.yml` 中的端口映射。

### 内存不足

在 Docker Desktop 设置中增加内存限制。

---

*更多信息请参考 [开发指南](../docs/guides/README.md)*
