# 快速开始指南

5 分钟快速上手 cloudQuant BMAD 框架。

## 📋 前置要求

- Git 2.0+
- 支持的 IDE 之一:
  - Claude Code
  - Cursor
  - OpenCode
  - Windsurf
  - Codex

## 🚀 快速开始

### 步骤 1: 克隆仓库

```bash
git clone https://github.com/cloudQuant/cloudQuant.git
cd cloudQuant
```

### 步骤 2: 了解目录结构

```
cloudQuant/
├── _bmad/           # BMAD 框架核心
│   ├── core/       # 核心模块
│   ├── bmm/        # 业务方法论
│   ├── cis/        # 创意智能套件
│   ├── gds/        # 游戏开发套件
│   ├── tea/        # 测试工程架构
│   └── wds/        # Web 设计系统
├── docs/           # 项目文档
└── README.md       # 项目说明
```

### 步骤 3: 配置你的 IDE

根据你使用的 IDE，配置文件位于:

| IDE | 配置目录 |
|-----|----------|
| Claude Code | `.claude/` |
| Cursor | `.cursor/` |
| OpenCode | `.opencode/` |
| Windsurf | `.windsurf/` |

### 步骤 4: 探索工作流

BMAD 框架通过工作流 (Workflow) 组织开发流程:

```bash
# 查看可用的工作流
ls _bmad/core/workflows/
ls _bmad/bmm/workflows/
```

### 步骤 5: 运行第一个工作流

1. 在你的 IDE 中打开项目
2. 打开 BMAD 技能面板
3. 选择一个工作流开始

## 🎓 下一步

- [模块开发指南](./module-development.md)
- [工作流创建指南](./workflow-creation.md)
- [最佳实践](./best-practices.md)

## ❓ 常见问题

### Q: BMAD 是什么?
BMAD (Breakthrough Method for AI Development) 是一种 AI 辅助的开发方法论框架。

### Q: 我需要安装什么?
只需要一个支持的 IDE，BMAD 配置已经包含在仓库中。

### Q: 如何贡献?
请阅读 [贡献指南](../../CONTRIBUTING.md)。

---

*最后更新: 2026-03-13*
