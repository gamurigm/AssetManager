from fastapi import APIRouter, Body
from typing import List, Dict, Any
from ...core.container import duckdb_repo

router = APIRouter()

@router.get("/history")
async def get_trading_history():
    """Retrieve full trade history from storage."""
    return duckdb_repo.get_transactions()

from ...core.container import get_quote

@router.post("/record")
async def record_transaction(
    type_str: str = Body(...),
    symbol: str = Body(...),
    shares: float = Body(...),
    price: float = Body(0.0),
    realized_pnl: float = Body(0.0),
    date: str = Body(None)
):
    """Record a manually executed trade or liquidation. Fetches real market price if price <= 0."""
    final_price = price
    if final_price <= 0:
        quote_data = await get_quote.execute(symbol)
        if quote_data and "price" in quote_data:
            final_price = quote_data["price"]
        else:
            final_price = 1.0  # Fallback just in case

    success = duckdb_repo.add_transaction(
        type_str=type_str, 
        symbol=symbol, 
        shares=shares, 
        price=final_price, 
        realized_pnl=realized_pnl,
        custom_date=date
    )
    return {"status": "success" if success else "failed", "market_price_used": final_price <= 0, "recorded_price": final_price}
