from fastapi import APIRouter, Body
from typing import List, Dict, Any
from datetime import datetime
from ...core.container import duckdb_repo, get_quote

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

    if success:
        # Reconcile portfolio holdings for this symbol
        _sync_portfolio_entry(symbol)

    return {"status": "success" if success else "failed", "market_price_used": final_price <= 0, "recorded_price": final_price}

def _sync_portfolio_entry(symbol: str):
    """Update the 'portfolio' table entry for a symbol based on transaction history aggregate."""
    from ...services.intraday_repository import intraday_repository # or similar search
    
    # 1. Get aggregate position from transactions
    transactions = duckdb_repo.get_transactions()
    symbol_txs = [t for t in transactions if t['symbol'] == symbol]
    
    total_shares = sum(t['shares'] if t['type'] == 'BUY' else -t['shares'] for t in symbol_txs)
    
    # Simple weighted average for entry price (BUYS only for entry cost)
    buy_txs = [t for t in symbol_txs if t['type'] == 'BUY']
    total_cost = sum(t['shares'] * t['price'] for t in buy_txs)
    buy_shares = sum(t['shares'] for t in buy_txs)
    avg_entry = total_cost / buy_shares if buy_shares > 0 else 0
    
    # 2. Get existing metadata if symbol exists in portfolio or use defaults
    current_portfolio = duckdb_repo.get_portfolio()
    existing = next((h for h in current_portfolio if h['symbol'] == symbol), None)
    
    if total_shares == 0:
        # Liquidated - Remove from portfolio
        new_portfolio = [h for h in current_portfolio if h['symbol'] != symbol]
        duckdb_repo.save_portfolio(new_portfolio)
        return

    if existing:
        # Update existing entry
        existing['shares'] = total_shares
        existing['entryPrice'] = avg_entry
        # Preserve other metadata (name, sector, factor, sl, tp)
        duckdb_repo.save_portfolio(current_portfolio)
    else:
        # New entry - need some metadata. Try to find in Initial holdings or use placeholders
        from .portfolios import INITIAL_HOLDINGS
        match = next((h for h in INITIAL_HOLDINGS if h['symbol'] == symbol), None)
        
        new_entry = {
            "symbol": symbol,
            "name": match["name"] if match else symbol,
            "shares": total_shares,
            "entryPrice": avg_entry,
            "factor": match["factor"] if match else 1.0,
            "sector": match["sector"] if match else "Other",
            "type": match["type"] if match else "stock",
            "purchaseDate": datetime.now().strftime("%Y-%m-%d"),
            "sl": None,
            "tp": None
        }
        current_portfolio.append(new_entry)
        duckdb_repo.save_portfolio(current_portfolio)



