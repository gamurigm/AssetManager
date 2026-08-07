# Current Project State

## System Overview
- **Frontend**: Next.js, Tailwind CSS, Lucide icons.
- **Backend**: FastAPI, Socket.IO, DuckDB (local analytical DB).
- **Agents**: Pydantic-AI (Nvidia NIM), OpenClaw (Browser automation).
- **Data**: Bybit (Crypto), FMP/Yahoo (Global Equities).

## Last Tasks Completed
- Updated Sidebar width to 440px for full name visibility.
- Reduced loading gate to 4s.
- Integrated WebSocket streaming in `Watchlist.tsx`.
- Created `OpenClawService` and exposed `/api/v1/openclaw` routes.

## Pending Architecture Debt
- WebSocket broadcasting frequency is set to 5s. (Monitor for rate limits).
- OpenClaw is currently configured to port 3002.
