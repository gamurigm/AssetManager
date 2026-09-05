# AssetManager / Gravity Roadmap

Status: **SPEC-DRIVEN — P0 verification in progress**
Last reviewed: 2026-09-05

This file is the project-level roadmap used by the agent team. The detailed architecture analysis, ownership boundaries and acceptance criteria live in [docs/architecture/project-organization.md](docs/architecture/project-organization.md). `STATE.md` records the current session state; `PLAN.md` records the active execution plan.

## Product direction

AssetManager brings together portfolio monitoring, market data, quantitative research, simulation, risk review and controlled broker execution. The main product path is:

```text
Portfolio and instruments → trusted market data → analysis/simulation
→ risk review → controlled execution → reconciliation and monitoring
```

AI agents, OpenBB, Kafka, C++ and broker adapters support this path. They are implementation capabilities, not separate product goals.

## Milestone 1 — Live terminal foundation

Status: **completed**

- [x] Dark/glassmorphism interface.
- [x] Multiple portfolios.
- [x] WebSocket price streaming.
- [x] OpenBB terminal integration.
- [x] Next.js frontend and FastAPI API separated by ports 3309 and 8282.

## Milestone 2 — P0: verifiable base

Status: **in progress**

Goal: make local development, imports and tests deterministic before adding more features.

- [x] Organize documentation, assets, diagnostics and broker examples into responsibility-based directories.
- [x] Record the reorganization manifest and verification baseline.
- [x] Correct operational references from port 8000 to the API port 8282.
- [x] Frontend typecheck and critical lint pass.
- [x] Backend package import passes.
- [x] Isolate optional Kafka and scheduler initialization from `import app.main`.
- [x] Make the default backend collection run offline without broker, Kafka or provider credentials.
- [x] Classify legacy `test_*.py` files as deterministic tests, integration tests or manual diagnostics.
- [x] Document one supported start/check command per component.

Acceptance: the offline backend suite collects and runs without external accounts; frontend typecheck, lint, tests and build pass; the main API import has no network or broker side effects.

## Milestone 3 — P1: market data and contracts

Status: **planned**

Goal: make market data traceable, resilient and owned by one process.

- [ ] Keep Yahoo Finance as primary, with FMP and Twelve Data as explicit fallbacks.
- [ ] Separate provider adapters, cache policy, historical persistence and event publication behind interfaces.
- [ ] Keep Market Data as the only writer of market ticks and its transactional outbox.
- [ ] Add tests for fallback order, timeout, stale data, symbol normalization and outbox replay.
- [ ] Verify `market.ticks.v1` contracts and correlation metadata at process boundaries.

Acceptance: provider failures are visible and bounded; no second process writes market ticks; API and Socket.IO contracts remain compatible with the frontend.

## Milestone 4 — P1: simulation and risk

Status: **planned**

Goal: produce reproducible backtests and explainable risk results.

- [ ] Keep `SimulationService` as the single entry point.
- [ ] Separate data preparation, strategy execution and result presentation.
- [ ] Fix datasets, transaction costs, fills and temporal validation in test fixtures.
- [ ] Expose reproducible job status and result contracts to the frontend.
- [ ] Add portfolio correlation, factor and risk-report workflows after the base is stable.

Acceptance: the same dataset and configuration produce the same result; costs, fills, validation windows and failure states are covered by tests.

## Milestone 5 — P1: controlled execution

Status: **planned**

Goal: make execution safe, idempotent and auditable.

- [ ] Keep the Execution Gateway as the only order submission boundary.
- [ ] Validate signals against policy and risk limits before broker submission.
- [ ] Reject duplicate signals and recover the journal after restart.
- [ ] Test reconciliation with broker doubles before any live integration.
- [ ] Keep MT5, IBKR, Bybit and cTrader adapters disabled unless explicitly configured.

Acceptance: duplicate events do not duplicate orders; every accepted or rejected intent has a correlation ID and journal record; live execution requires explicit configuration.

## Milestone 6 — P2: product workflows

Status: **planned**

- [ ] Migrate frontend capabilities into feature modules beginning with portfolios.
- [ ] Consolidate API access and WebSocket subscriptions to avoid duplicate requests.
- [x] Add portfolio correlation heatmap, automated alpha reports and smart hedging after milestones 2–5.
- [ ] Add proactive alerts through OpenClaw only after delivery, authentication and rate limits are defined.
- [ ] Add Reddit/X sentiment scraping only after the source list, retention policy and provider limits are agreed.

Acceptance: each migrated workflow preserves navigation, error states, reconnect behavior and API contracts; alerts and scraping have explicit operational limits.

## Milestone 7 — P2: composition and delivery

Status: **planned**

- [ ] Initialize resources explicitly per process instead of at module import.
- [ ] Publish health/readiness checks for API, market data, analysis and execution.
- [ ] Inventory optional dependencies and document a clean-checkout setup.
- [ ] Keep `PLAN.md`, `ROADMAP.md` and `STATE.md` at the root until agent path configuration is migrated and tested.

Acceptance: the API starts without brokers, schedulers or Kafka unless enabled; each process reports readiness; CI validates the documented commands.

## Priority order

1. Finish Milestone 2 and remove import-time side effects.
2. Stabilize market-data ownership and contracts.
3. Make simulation and execution reproducible and auditable.
4. Improve frontend workflows and add advanced intelligence features.

Do not add another process or move a core package solely for naming consistency. Every structural change must preserve a working boundary, include an acceptance check and identify its data owner.
