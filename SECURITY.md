# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 6.1.x   | :white_check_mark: |
| < 6.1   | :x:                |

## Reporting a Vulnerability

We take the security of cloudQuant seriously. If you have discovered a security vulnerability, please report it to us.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to:

- **Email**: yunjinqi@gmail.com

You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

### What to Include

Please include the following information in your report:

1. **Description** of the vulnerability
2. **Steps to reproduce** the issue
3. **Potential impact** of the vulnerability
4. **Possible solutions** (if you have any)
5. **Your name/handle** (optional, for credit in security advisories)

### Disclosure Policy

- We will acknowledge your email within 48 hours
- We will confirm the vulnerability and determine its impact
- We will work on a fix and prepare a release
- We will publish a security advisory on GitHub

### Security Best Practices

When using cloudQuant:

1. **Keep dependencies updated** - Regularly update all dependencies
2. **Review configurations** - Ensure BMAD configurations don't expose sensitive data
3. **Use environment variables** - Never commit secrets or API keys
4. **Enable branch protection** - Require PR reviews for production branches

## Known Security Considerations

### API Keys and Secrets

- Never commit API keys, passwords, or secrets to the repository
- Use `.gitignore` to exclude sensitive files
- Use environment variables for configuration

### Third-Party Dependencies

- We use Dependabot to monitor dependencies
- Review dependency updates before merging

---

Thank you for helping keep cloudQuant secure!
