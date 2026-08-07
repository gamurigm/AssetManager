# AssetManager service architecture

AssetManager uses four coarse-grained processes. The frontend only knows the
public API; internal topology is never exposed to UI components.

| Process | Port | Owns | Must not own |
|---|---:|---|---|
| API/BFF | 8282 | HTTP, Socket.IO fanout, UI-facing models | broker sessions, strategy loops, scheduled trading |
| Market Data | 8291 | provider cascade, ticks, market database, Kafka outbox | portfolios, orders, broker execution |
| Analysis | 8292 | candles in memory, strategies, signals | broker credentials, order submission, shared databases |
| Execution Gateway | 8293 | MT5 adapter, risk guards, idempotency journal, reconciliation | market ingestion, UI state, strategy generation |

## Event flow

```text
Providers -> Market Data -> market.ticks.v1 -> Analysis
                         \-> API/BFF Socket.IO

Analysis  -> trade.signals.v1 -> execution policy -> Execution Gateway -> MT5
```

Events use strict Pydantic contracts from `backend/services/contracts`. Every
event includes an ID, version, UTC timestamp, source, correlation ID and an
optional causation ID. Symbols are Kafka keys so the ordering of one symbol is
preserved within a partition.

Consumers disable auto-commit. An offset is committed only after successful
processing. Invalid payloads are delivered to a versioned DLQ before their
offset is committed. Transient failures retain and seek the same offset for
retry.

Market Data is the only writer of `market_data.duckdb`. A tick and its outbound
Kafka message are recorded in one transaction. Kafka delivery acknowledgement
marks the outbox row as published; after a restart, pending events are replayed.

## Running locally on Windows

All Python processes must use `backend/venv/Scripts/python.exe`.

```powershell
docker compose up -d kafka

Set-Location backend
& .\venv\Scripts\python.exe -m uvicorn services.market_data_gateway.main:app --port 8291
& .\venv\Scripts\python.exe -m uvicorn services.strategy_engine.main:app --port 8292
& .\venv\Scripts\python.exe -m uvicorn services.execution_gateway.main:app --host 127.0.0.1 --port 8293
& .\venv\Scripts\python.exe -m uvicorn app.main:sio_app --port 8282
```

`run_app.ps1` starts the same processes. MT5 intentionally runs on the Windows
host because it controls the locally installed terminal. Containerized API
instances reach it through `host.docker.internal:8293`.

The API defaults to embedded broker connections and its legacy scheduler being
disabled. They can only be restored explicitly through
`API_ENABLE_BROKER_CONNECTIONS` and `API_ENABLE_SCHEDULER` during migration.

## Shift-left checks

Before integration or deployment, run:

```powershell
Set-Location backend
& .\venv\Scripts\python.exe -m pytest tests
```

The architecture test set covers strict schemas, event trace propagation,
manual Kafka commits, poison-message DLQ handling, the market outbox, strategy
deduplication, API fanout groups and the execution-gateway boundary.
