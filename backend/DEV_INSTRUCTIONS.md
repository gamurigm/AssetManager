# Developer Instructions & Guidelines

## 1. Network Configuration
- **Backend Port**: 8282 (NOT 8000)
  - The backend MUST run on port `8282`.
  - The frontend is hardcoded to fetch from `http://127.0.0.1:8282`.
  - If you see `404 Not Found` or `Failed to fetch`, CHECK THE PORT FIRST.

## 2. Rate Limiting Strategy
- **Yahoo Finance**: Primary provider. Generous limits (600 rpm).
- **FMP/Others**: Strict limits. Use as fallback only.
- **Wait Logic**: If Yahoo is limited, WAIT 1.5s instead of failing over to strict providers.

## 3. Logs
- **Logfire**: Pydantic instrumentation is DISABLED by default to avoid console spam.
  - To enable: Uncomment `logfire.instrument_pydantic()` in `app/main.py`.

## 4. Historical Data Sync (Market Data 2.0)
- **DuckDB**: Used as Primary Source for history.
- **Incremental Sync**:
  - `Bootstrap`: If no data exists, fetches `period="max"` from Yahoo.
  - `Incremental`: Fetches only from `latest_date` to Today.
  - **Optimization**: Avoids `ticker.info` and uses `ticker.history` for all OHLCV operations.

## 5. Parallel Processing
- Orchestrator uses `delegate_parallel_tasks` to run multiple agents concurrently.
- Do not revert to sequential execution unless debugging race conditions.
