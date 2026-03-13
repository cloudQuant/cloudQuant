# 开发指南

本目录包含 cloudQuant 项目的开发指南和教程。

## 📚 指南列表

| 指南 | 描述 | 难度 |
|------|------|------|
| [快速开始](./quick-start.md) | 5 分钟上手 BMAD 框架 | 初级 |
| [模块开发](./module-development.md) | 如何开发 BMAD 模块 | 中级 |
| [工作流创建](./workflow-creation.md) | 创建自定义工作流 | 中级 |
| [最佳实践](./best-practices.md) | 开发最佳实践和规范 | 高级 |

## 🚀 快速开始

### 1. 环境准备

```bash
# 克隆仓库
git clone https://github.com/cloudQuant/cloudQuant.git
cd cloudQuant

# 查看目录结构
ls -la _bmad/
```

### 2. 选择 IDE

BMAD 支持多种 IDE:

- **Claude Code**: 使用 `.claude/` 目录
- **Cursor**: 使用 `.cursor/` 目录
- **OpenCode**: 使用 `.opencode/` 目录
- **Windsurf**: 使用 `.windsurf/` 目录

### 3. 运行第一个工作流

1. 打开你的 IDE
2. 导航到 `_bmad/core/workflows/`
3. 选择一个工作流开始

## 📖 学习路径

```
初学者 ──────────────────────────────────────────────────────► 专家
   │                                                    │
   │  1. 快速开始                                        │  4. 最佳实践
   │  2. 模块开发                                        │  5. 贡献代码
   │  3. 工作流创建                                       │
   ▼                                                    ▼
```

## 🎯 推荐学习顺序

1. **第一周**: 完成快速开始指南
2. **第二周**: 尝试修改现有模块
3. **第三周**: 创建自定义工作流
4. **第四周**: 参与项目贡献

---

*最后更新: 2026-03-13*
