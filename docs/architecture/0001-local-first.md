# ADR 0001: Local-first modular monorepo

Status: accepted — 2026-08-05

OrganicFlow uses a React/TypeScript web client and a FastAPI service with versioned schemas. The first slice runs locally without cloud credentials. Provider adapters and state persistence remain behind stable API boundaries so PostgreSQL, Redis, workers, and Tauri can be added without changing workflow exports.

The product name and tagline are centralized in UI configuration as the repository grows. The current narrow slice intentionally favors demonstrable safety, workflow drafting, mock simulation, and contextual help over placeholder integrations.
