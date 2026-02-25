from fastapi import APIRouter, Body
from typing import List, Dict, Any
from ...services.report_service import report_service

from ...core.container import duckdb_repo
from ...services.equity_service import equity_service

INITIAL_HOLDINGS = [
    { "symbol": "^N225", "name": "Nikkei 225 Index", "shares": 0.1, "entryPrice": 29600, "price": 0, "factor": 0.4166, "change": 0, "changePercent": 0, "source": "Live", "sector": "Indices", "type": "cfd", "purchaseDate": "2023-05-15" },
    { "symbol": "AAPL", "name": "Apple Inc CFD", "shares": 10, "entryPrice": 188.50, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Technology", "type": "cfd", "purchaseDate": "2024-02-10" },
    { "symbol": "PLTR", "name": "Palantir Technologies CFD", "shares": 10, "entryPrice": 24.19, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Technology", "type": "cfd", "purchaseDate": "2024-03-01" },
    { "symbol": "GC=F", "name": "Gold Futures", "shares": 0.1, "entryPrice": 1980.30, "price": 0, "factor": 84.397, "change": 0, "changePercent": 0, "source": "Live", "sector": "Commodities", "type": "cfd", "purchaseDate": "2023-11-20" },
    { "symbol": "JPM", "name": "JPMorgan Chase & Co", "shares": 1.536, "entryPrice": 122.81, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Financials", "type": "stock", "purchaseDate": "2022-08-14" },
    { "symbol": "COIN", "name": "Coinbase Global Inc", "shares": 2.724, "entryPrice": 34.93, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Digital Assets", "type": "stock", "purchaseDate": "2023-01-05" },
    { "symbol": "GS", "name": "Goldman Sachs Group Inc", "shares": 0.164, "entryPrice": 345.54, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Financials", "type": "stock", "purchaseDate": "2023-12-12" },
    { "symbol": "LMT", "name": "Lockheed Martin Corp", "shares": 0.214, "entryPrice": 425.70, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Industrials", "type": "stock", "purchaseDate": "2022-06-30" },
    { "symbol": "NVDA", "name": "NVIDIA Corp", "shares": 0.54, "entryPrice": 58.15, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Technology", "type": "stock", "purchaseDate": "2024-01-20" },
    { "symbol": "CHFJPY=X", "name": "CHF/JPY", "shares": 0.5, "entryPrice": 172.071, "price": 0, "factor": 615.66, "change": 0, "changePercent": 0, "source": "Live", "sector": "Forex", "type": "cfd", "purchaseDate": "2024-05-02" },
    { "symbol": "ZT=F", "name": "US 2 Year T-Note", "shares": 0.1, "entryPrice": 101.57, "price": 0, "factor": 114.285, "change": 0, "changePercent": 0, "source": "Live", "sector": "Bonds", "type": "cfd", "purchaseDate": "2024-04-15" },
    { "symbol": "EURUSD=X", "name": "EUR/USD", "shares": -1.2, "entryPrice": 1.12519, "price": 0, "factor": 100000, "change": 0, "changePercent": 0, "source": "Live", "sector": "Forex", "type": "cfd", "purchaseDate": "2024-06-10" },
]

router = APIRouter()

@router.get("/")
async def get_portfolios():
    """Load persisted portfolio from DuckDB. Fallback to INITIAL_HOLDINGS if empty."""
    data = duckdb_repo.get_portfolio()
    if not data:
        # Save initials to DB so it persists from now on
        duckdb_repo.save_portfolio(INITIAL_HOLDINGS)
        return INITIAL_HOLDINGS
    return data

@router.post("/save")
async def save_portfolio(holdings: List[Dict[str, Any]] = Body(...)):
    """Persist current holdings to DuckDB."""
    success = duckdb_repo.save_portfolio(holdings)
    return {"status": "success" if success else "failed"}

@router.post("/report")
async def generate_portfolio_report(
    holdings: List[Dict[str, Any]] = Body(...),
    total_value: float = Body(...),
    total_pnl: float = Body(...)
):
    filename = report_service.generate_balance_sheet(holdings, total_value, total_pnl)
    report_url = f"http://localhost:8282/view-reports/{filename}"
    return {"url": report_url, "filename": filename}

@router.post("/snapshot-equity")
async def snapshot_equity(total_value: float = Body(..., embed=True)):
    """Record current total balance and realized balance."""
    success = duckdb_repo.record_equity_snapshot(total_value)
    return {"status": "success" if success else "failed"}

@router.get("/history")
async def get_equity_history():
    """Retrieve dynamic equity history (realized vs total) for charts."""
    return equity_service.get_historical_equity_curve(days=730)
