# ADR-003: Documentation Structure

| Status   | Date       | Decision Makers |
| -------- | ---------- | --------------- |
| Accepted | 2026-03-13 | cloudQuant      |

## Context

The cloudQuant project requires a clear documentation structure to help users and contributors:

- Find relevant information quickly
- Understand the project architecture
- Contribute effectively
- Maintain documentation quality

## Decision

Adopt a **three-tier documentation structure**:

```text
docs/
├── README.md           # Documentation hub
├── architecture/       # Architecture & ADRs
│   ├── README.md
│   └── adr/
├── api/                # API documentation
│   └── README.md
└── guides/             # Development guides
    ├── README.md
    └── quick-start.md
```

### Tier 1: Root Documentation

```text
- README.md - Project overview
- CONTRIBUTING.md - Contribution guidelines
- CHANGELOG.md - Version history
- SECURITY.md - Security policy
- CODE_OF_CONDUCT.md - Community guidelines

### Tier 2: Structured Documentation

- docs/architecture/ - Architecture decisions and system design
- docs/api/ - API documentation and interfaces
- docs/guides/ - Development guides and tutorials

### Tier 3: Module Documentation

- _bmad/*/ - BMAD module-specific documentation

## Consequences

### Positive

- ✅ Clear separation of concerns
- ✅ Easy to find relevant documentation
- ✅ Scalable structure for future growth
- ✅ Follows industry best practices

### Negative

- ⚠️ Requires maintaining multiple README files
- ⚠️ Potential for documentation duplication

## References

- [Write the Docs](https://www.writethedocs.org/)
- [Documentation Systems](https://documentation.divio.com/)
```
