/**
 * Commitlint Configuration
 * Enforces Conventional Commits specification
 * @see https://conventionalcommits.org/
 */

export default {
  extends: ['@commitlint/config-conventional'],
  rules: {
    // Type enumeration
    'type-enum': [
      2,
      'always',
      [
        'feat',     // 新功能
        'fix',      // Bug 修复
        'docs',     // 文档更改
        'style',    // 代码格式（不影响功能）
        'refactor', // 重构
        'perf',     // 性能优化
        'test',     // 添加或修改测试
        'build',    // 构建系统或外部依赖更改
        'ci',       // CI 配置文件和脚本更改
        'chore',    // 其他不修改 src 或测试文件的更改
        'revert',   // 回退之前的 commit
        'wip',      // 工作进行中
        'release',  // 发布相关
      ],
    ],
    // Subject case
    'subject-case': [2, 'always', 'lower-case'],
    // Subject must not end with full stop
    'subject-full-stop': [2, 'never', '.'],
    // Header max length
    'header-max-length': [2, 'always', 100],
    // Body max line length
    'body-max-line-length': [2, 'always', 100],
    // Footer max line length
    'footer-max-line-length': [2, 'always', 100],
  },
  // Ignores merge commits and revert commits
  ignores: [
    (message) => /^Merge branch/.test(message),
    (message) => /^Revert/.test(message),
  ],
};
