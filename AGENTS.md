# AssetManager — Agent Context

## Project Structure
- **Frontend**: `frontend/` — Next.js 16 + Turbopack + TailwindCSS, port **3309**
- **Backend**: `backend/` — FastAPI + Uvicorn + Socket.IO, port **8282**
- **Core Engine**: `core_engine/` — C++ modules (FIX protocol, bootstrap, etc.)
- **Data**: `backend/data/` — DuckDB databases for market data persistence

## ⚠️ CRITICAL: Python Virtual Environment
**ALL Python commands MUST use the venv.** Never use the system Python.

- **venv location**: `backend/venv/`
- **Python executable**: `backend/venv/Scripts/python.exe`
- **Pip executable**: `backend/venv/Scripts/pip.exe`
- **Activation (PowerShell)**: `& backend\venv\Scripts\Activate.ps1`

### Examples — ALWAYS do this:
```powershell
# Running the backend
& "c:\AssetManager\backend\venv\Scripts\python.exe" -m uvicorn app.main:sio_app --host 0.0.0.0 --port 8282 --reload

# Installing a package
& "c:\AssetManager\backend\venv\Scripts\pip.exe" install <package>

# Running a Python script
& "c:\AssetManager\backend\venv\Scripts\python.exe" script.py

# Running tests
& "c:\AssetManager\backend\venv\Scripts\python.exe" -m pytest tests/
```

### ❌ NEVER do this:
```powershell
python -m uvicorn ...        # Uses system Python, missing dependencies!
pip install ...              # Installs to system, not venv!
python script.py             # Wrong interpreter!
```

## Network Configuration
- **Backend**: `http://localhost:8282` (NEVER 8000)
- **Frontend**: `http://localhost:3309`
- **CORS Origins allowed**: `localhost:3309`, `127.0.0.1:3309`, `localhost:3000`, `127.0.0.1:3000`
- **Frontend dev command**: `npm run dev` (from `frontend/` directory)
- **Backend dev command**: see venv examples above

## Key Technologies
- **Backend**: FastAPI, Pydantic, DuckDB, Socket.IO, Logfire, yfinance
- **Frontend**: Next.js 16, React, TypeScript, TailwindCSS, Lucide icons, Recharts
- **AI/ML**: Pydantic-AI, NVIDIA NIM, Hidden Markov Models (hmmlearn)
- **C++ Engine**: Fix8 (FIX protocol), custom bootstrap resampling

## Data Providers (Priority Order)
1. **Yahoo Finance** — Primary (generous rate limits ~600 rpm)
2. **FMP** — Fallback only (strict limits)
3. **Twelve Data** — Fallback only

## Architecture Patterns
- **Façade Pattern**: `SimulationService` is the single entry point for all simulation operations
- **Strategy Pattern**: `StrategyFactory` + engine interfaces for pluggable strategies
- **Repository Pattern**: `DuckDBRepository` / `IntradayRepository` for data persistence
- **SOLID Principles**: All modules follow single responsibility and dependency inversion

## Important Files
| Purpose | Path |
|---------|------|
| Backend entry point | `backend/app/main.py` |
| API routes | `backend/app/api/routes/*.py` |
| Simulation route | `backend/app/api/routes/simulation.py` |
| Simulation service | `backend/app/services/simulation_service.py` |
| Strategy engine | `backend/app/agents/strategies/engine/` |
| Backtest runner | `backend/app/agents/strategies/backtest_runner.py` |
| Market data service | `backend/app/services/market_data.py` |
| Frontend trading page | `frontend/src/app/client/trading/page.tsx` |
| Config/settings | `backend/app/core/config.py` |
| Requirements | `backend/requirements.txt` |
