# Threat model

OrganicFlow treats prompts, repositories, email, web pages, documents, and tool output as untrusted data—not governing instructions.

## Trust boundaries

- Browser to API: validate every request; UI approval alone is never authoritative.
- API to tools: use explicit permission scopes, working directories, timeouts, cancellation, allowlisted environment variables, and redacted structured events.
- Plugins and providers: least privilege; secrets are references backed by an OS keychain or server vault.

## Priority threats and controls

| Threat | Control |
|---|---|
| Prompt/tool-output injection | Separate instructions from content; never grant permissions from retrieved text |
| Shell injection | Argument arrays, command allowlists, no implicit shell, isolated workspace |
| Path traversal/symlinks | Resolve and verify paths remain beneath user-granted roots |
| SSRF/exfiltration | Deny network by default; validate protocols; domain allowlists |
| Secret/log leakage | Reference secrets; redact structured events and exports |
| Unsafe external writes | Backend-enforced approvals; high-impact actions always ask by default |
| Automation loops/duplicates | Runtime, step, retry, delegation, and idempotency limits |
| Malicious imports/plugins | JSON Schema validation, permission manifests, signatures where practical |

Residual risks and production hardening are tracked in the roadmap. This release does not claim OS-level sandboxing or encrypted persistence.
