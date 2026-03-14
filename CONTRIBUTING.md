# 贡献指南 | Contributing Guide

[English](#english) | [中文](#chinese)

---

<a name="chinese"></a>

## 中文版本

感谢您有兴趣为 cloudQuant 项目做出贡献！

### 🚀 快速开始

1. **Fork 本仓库**

   ```bash
   git clone https://github.com/YOUR_USERNAME/cloudQuant.git
   cd cloudQuant
   ```

2. **创建分支**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **进行更改**
   - 遵循现有的代码风格和文档格式
   - 确保所有更改都有清晰的提交信息

4. **提交更改**

   ```bash
   git add .
   git commit -m "feat: 添加新功能描述"
   ```

5. **推送并创建 Pull Request**

   ```bash
   git push origin feature/your-feature-name
   ```

### 📝 提交信息规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat:` 新功能
- `fix:` 修复 bug
- `docs:` 文档更改
- `style:` 代码格式（不影响功能）
- `refactor:` 重构
- `test:` 添加或修改测试
- `chore:` 构建过程或辅助工具的变动

### 📂 项目结构

```text
cloudQuant/
├── _bmad/              # BMAD 框架核心模块
│   ├── core/           # 核心工作流和代理
│   ├── bmm/            # BMAD 方法论模块
│   ├── cis/            # 创意智能套件
│   ├── gds/            # 游戏开发套件
│   ├── tea/            # 测试工程架构
│   └── wds/            # Web 设计系统
├── docs/               # 项目文档
├── .github/            # GitHub 配置
└── README.md           # 项目说明
```

### 🔍 代码审查

所有 PR 都需要经过审查才能合并。请确保：

- [ ] 代码符合项目风格
- [ ] 文档已更新（如适用）
- [ ] 提交信息清晰描述更改内容
- [ ] PR 描述完整说明更改目的

### 📋 行为准则

- 尊重所有贡献者
- 保持建设性的讨论
- 欢迎不同观点和经验水平

### ❓ 获取帮助

如有问题，请：

- 创建 [Issue](https://github.com/cloudQuant/cloudQuant/issues)
- 发送邮件至 yunjinqi@gmail.com

---

<a name="english"></a>

## English Version

Thank you for your interest in contributing to cloudQuant!

### 🚀 Quick Start

1. **Fork this repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/cloudQuant.git
   cd cloudQuant
   ```

2. **Create a branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow existing code style and documentation format
   - Ensure all changes have clear commit messages

4. **Commit your changes**

   ```bash
   git add .
   git commit -m "feat: add new feature description"
   ```

5. **Push and create a Pull Request**

   ```bash
   git push origin feature/your-feature-name
   ```

### 📝 Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code formatting (no functionality change)
- `refactor:` Code refactoring
- `test:` Adding or modifying tests
- `chore:` Build process or auxiliary tool changes

### 📂 Project Structure

```text
cloudQuant/
├── _bmad/              # BMAD framework core modules
│   ├── core/           # Core workflows and agents
│   ├── bmm/            # BMAD methodology module
│   ├── cis/            # Creative Intelligence Suite
│   ├── gds/            # Game Dev Studio
│   ├── tea/            # Test Engineering Architecture
│   └── wds/            # Web Design System
├── docs/               # Project documentation
├── .github/            # GitHub configuration
└── README.md           # Project README
```

### 🔍 Code Review

All PRs require review before merging. Please ensure:

- [ ] Code follows project style
- [ ] Documentation is updated (if applicable)
- [ ] Commit messages clearly describe changes
- [ ] PR description explains the purpose of changes

### 📋 Code of Conduct

- Respect all contributors
- Keep discussions constructive
- Welcome different viewpoints and experience levels

### ❓ Getting Help

If you have questions:

- Create an [Issue](https://github.com/cloudQuant/cloudQuant/issues)
- Email yunjinqi@gmail.com
