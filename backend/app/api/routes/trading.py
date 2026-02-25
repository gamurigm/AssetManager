from fastapi import APIRouter, Body
from typing import List, Dict, Any
from ...core.container import duckdb_repo

router = APIRouter()

@router.get("/history")
async def get_trading_history():
    """Retrieve full trade history from storage."""
    return duckdb_repo.get_transactions()

@router.post("/record")
async def record_transaction(
    type_str: str = Body(...),
    symbol: str = Body(...),
    shares: float = Body(...),
    price: float = Body(...),
    realized_pnl: float = Body(0.0)
):
    """Record a manually executed trade or liquidation."""
    success = duckdb_repo.add_transaction(type_str, symbol, shares, price, realized_pnl)
    return {"status": "success" if success else "failed"}
