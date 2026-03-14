# ADR-002: Multi-IDE Configuration Strategy

| Status | Date | Decision Makers |
|--------|------|-----------------|
| Accepted | 2026-03-13 | cloudQuant |

## Context

cloudQuant project needs to support multiple AI-powered IDEs for development:
- Claude Code
- Cursor
- OpenCode
- Windsurf
- Codex

Each IDE has its own configuration format and directory structure. Maintaining separate configurations could lead to:
- Configuration drift between IDEs
- Inconsistent behavior across development environments
- Increased maintenance burden

## Decision

Adopt a **multi-IDE parallel configuration strategy**:

1. **Separate directories for each IDE**: Each IDE maintains its own configuration directory (`.claude/`, `.cursor/`, `.opencode/`, `.windsurf/`)

2. **Shared BMAD core**: All IDE configurations reference the same `_bmad/` core framework

3. **Synchronized skill definitions**: Skills are duplicated across IDE directories to ensure compatibility

## Consequences

### Positive

- ✅ Developers can use their preferred IDE
- ✅ IDE-specific optimizations can be applied
- ✅ No single point of failure for configuration
- ✅ Easy to add support for new IDEs

### Negative

- ⚠️ Configuration duplication increases maintenance
- ⚠️ Risk of configuration drift if not synchronized
- ⚠️ Larger repository size due to duplicated files

### Alternatives Considered

1. **Single IDE focus**: Only support one IDE
   - Pros: Simpler maintenance
   - Cons: Limits developer choice, reduces adoption

2. **Configuration generation**: Generate IDE configs from a single source
   - Pros: Single source of truth
   - Cons: Requires build step, more complex setup

3. **Symlinks**: Use symbolic links to share configurations
   - Pros: No duplication
   - Cons: Cross-platform compatibility issues, Git limitations

## References

- [GitHub CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [EditorConfig](https://editorconfig.org/)
