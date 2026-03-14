# Contributing Translations

We welcome translations of our documentation! This guide explains how to contribute translations.

## How to Translate

1. **Find the source file** - All documentation is in English in the `docs/` directory
2. **Create a translation file** - Use the same path with language suffix (e.g., `README.zh-CN.md`)
3. **Submit a PR** - Follow the standard contribution process

## Supported Languages

| Language              | Code    | Status         |
| --------------------- | ------- | -------------- |
| English               | `en`    | ✅ Complete    |
| Chinese (Simplified)  | `zh-CN` | ✅ Complete    |
| Chinese (Traditional) | `zh-TW` | 🔄 In Progress |
| Japanese              | `ja`    | ⏳ Planned     |

## File Naming Convention

```text
docs/
├── README.md           # English (default)
├── README.zh-CN.md     # Simplified Chinese
├── README.zh-TW.md     # Traditional Chinese
└── README.ja.md        # Japanese
```

## Translation Guidelines

1. **Keep formatting consistent** - Maintain the same Markdown structure
2. **Preserve links** - Keep all hyperlinks working
3. **Update dates** - Update the "Last updated" date
4. **Add language badge** - Add a language switcher at the top

## Example Language Switcher

```markdown
[English](README.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md)
```

Thank you for helping make cloudQuant accessible to more developers!
