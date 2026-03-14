# 模块开发指南

本指南介绍如何为 BMAD 框架开发自定义模块。

## 📋 概述

BMAD 模块是框架的基本组成单元，每个模块包含：

- **代理 (Agents)**: 执行特定任务的 AI 代理
- **工作流 (Workflows)**: 定义任务执行流程
- **任务 (Tasks)**: 可复用的原子操作
- **数据 (Data)**: 模块所需的参考数据

## 🏗 模块结构

```text
_bmad/
└── my-module/
    ├── agents/
    │   └── my-agent.md       # 代理定义
    ├── workflows/
    │   └── my-workflow.md    # 工作流定义
    ├── tasks/
    │   └── my-task.md        # 任务定义
    ├── data/
    │   └── reference.md      # 参考数据
    ├── config.yaml           # 模块配置
    └── README.md             # 模块说明
```

## 🚀 创建新模块

### 步骤 1: 初始化模块目录

```bash
mkdir -p _bmad/my-module/{agents,workflows,tasks,data}
```

### 步骤 2: 创建配置文件

```yaml
# _bmad/my-module/config.yaml
name: my-module
version: 1.0.0
description: 模块描述
author: Your Name
dependencies:
  - core # 依赖的核心模块
```

### 步骤 3: 定义代理

```markdown
# \_bmad/my-module/agents/my-agent.md

# My Agent

## 角色描述

描述代理的职责和能力

## 技能列表

- skill-1: 技能描述
- skill-2: 技能描述

## 工作流程

1. 步骤 1
2. 步骤 2
3. 步骤 3

## 输出格式

定义代理的输出格式
```

### 步骤 4: 定义工作流

```markdown
# \_bmad/my-module/workflows/my-workflow.md

# My Workflow

## 触发条件

- 条件 1
- 条件 2

## 步骤

1. **步骤 1**: 描述
   - 代理: my-agent
   - 输入: ...
   - 输出: ...

2. **步骤 2**: 描述
   - 代理: my-agent
   - 输入: ...
   - 输出: ...
```

### 步骤 5: 定义任务

```markdown
# \_bmad/my-module/tasks/my-task.md

# My Task

## 目标

任务的具体目标

## 输入

- input-1: 输入描述
- input-2: 输入描述

## 输出

- output-1: 输出描述

## 执行步骤

1. 步骤 1
2. 步骤 2
```

## ⚙️ 配置详解

### config.yaml 字段

| 字段         | 类型   | 必填 | 说明                   |
| ------------ | ------ | ---- | ---------------------- |
| name         | string | ✅   | 模块名称（唯一标识）   |
| version      | string | ✅   | 模块版本（语义化版本） |
| description  | string | ✅   | 模块描述               |
| author       | string | ❌   | 作者信息               |
| dependencies | array  | ❌   | 依赖的其他模块         |

### manifest.yaml 更新

安装模块后，需要在 `_bmad/_config/manifest.yaml` 中注册：

```yaml
modules:
  - name: my-module
    version: 1.0.0
    installDate: 2026-03-13T00:00:00.000Z
    source: local
```

## 🧪 测试模块

### 单元测试

```bash
# 运行模块测试
bmad test my-module
```

### 集成测试

```bash
# 测试模块与其他模块的集成
bmad test my-module --integration
```

## 📦 发布模块

### 1. 准备发布

```bash
# 验证模块结构
bmad validate my-module

# 运行所有测试
bmad test my-module --all
```

### 2. 发布到 NPM

```bash
# 构建模块包
bmad build my-module

# 发布
npm publish bmad-module-my-module
```

## 💡 最佳实践

1. **单一职责**: 每个模块专注于一个领域
2. **清晰命名**: 使用描述性的名称
3. **完整文档**: 提供详细的 README
4. **版本管理**: 遵循语义化版本
5. **依赖最小化**: 仅依赖必要的模块

## 🔗 相关资源

- [工作流创建指南](./workflow-creation.md)
- [最佳实践](./best-practices.md)
- [BMAD 核心模块](../../_bmad/core/)

---

_最后更新: 2026-03-13_
