# Final validation report

Date: 2026-08-05 · Branch: `feature/openflow-vertical-slice`

This report is updated from actual commands during release validation. The current host provides Node 25.9.0, npm 11.12.1, Python 3.14.4, Codex CLI 0.147.0-alpha.1.2, and Docker 29.6.1. Rust/Tauri is unavailable.

## Scope

Validated: responsive web UI, workflow draft UI, mock email/reminder simulation API, backend approval enforcement, contextual help, schema, and Codex detection. Planned: durable database/queue, live provider credentials, Tauri packaging, full E2E matrix, and production deployment hardening.

## Commands and results

| Command/check | Result |
|---|---|
| `npm run typecheck` | Passed |
| `npm test` | 2 tests passed |
| `npm run build` | Passed; 209.12 kB JavaScript, 11.01 kB CSS |
| `.venv/bin/pytest -q` | 3 tests passed; one upstream TestClient deprecation warning |
| `npm audit --audit-level=high` | 0 vulnerabilities |
| Browser desktop check, 1440×900 | Passed |
| Browser mobile check, 390×844 | Passed; `scrollWidth === clientWidth === 390` |
| Natural-language workflow interaction | Passed; visual draft and permissions shown |
| Contextual help interaction | Passed; workspace help and documentation action shown |

## Screenshots

- `screenshots/home-dashboard.png`
- `screenshots/workflow-builder.png`
- `screenshots/mobile-home.png`
- `screenshots/contextual-help.png`

All screenshots use fictional/local UI data and contain no credentials, email addresses, tokens, or private filesystem paths.

## Known limitations

Docker services and Tauri packaging were not built: this narrow release has no durable database/queue and the host has no globally available Rust toolchain. Live Codex execution, external provider adapters, scheduling, complete docs-link crawling, formal WCAG automation, SBOM, secret scan, and the full 20-scenario E2E suite remain roadmap work. The browser’s primary workflow path and responsive layout were manually verified with browser automation.
