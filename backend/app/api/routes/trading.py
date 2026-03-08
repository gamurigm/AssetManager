from typing import List, Dict, Any

from fastapi import APIRouter, Body, HTTPException
from datetime import datetime
from ...core.container import duckdb_repo, get_quote
from ...services.ibkr_order_parser import (
    IBKRCommandRequest,
    IBKROrderRequest,
    parse_ibkr_terminal_command,
)
from ...services.ibkr_service import ibkr_service

router = APIRouter()


async def _execute_ibkr_order(order: IBKROrderRequest) -> Dict[str, Any]:
    result = await ibkr_service.place_market_order(
        symbol=order.symbol,
        quantity=order.quantity,
        side=order.side,
        asset_type=order.asset_type,
        currency=order.currency,
        exchange=order.exchange,
        primary_exchange=order.primary_exchange,
        last_trade_date=order.last_trade_date,
    )

    if "error" in result:
        detail = str(result["error"])
        status_code = 503 if "Not connected" in detail or "reachable IBKR endpoint" in detail else 400
        raise HTTPException(status_code=status_code, detail=detail)

    executed_symbol = str(result.get("symbol") or order.symbol).upper()
    final_price = float(result.get("avgFillPrice", 0.0) or 0.0)
    success_record = False

    if order.record_trade:
        success_record = duckdb_repo.add_transaction(
            type_str=order.side.upper(),
            symbol=executed_symbol,
            shares=order.quantity,
            price=final_price,
            realized_pnl=0.0,
            custom_date=datetime.now().strftime("%Y-%m-%d"),
            portfolio_id=order.portfolio_id,
        )

        if success_record:
            _sync_portfolio_entry(executed_symbol, order.portfolio_id)

    return {
        "status": "success",
        "symbol": executed_symbol,
        "asset_type": result.get("asset_type", order.asset_type),
        "ibkr_result": result,
        "recorded": success_record,
        "recorded_price": final_price,
        "portfolio_id": order.portfolio_id,
    }

@router.post("/order/ibkr")
async def place_ibkr_order(order: IBKROrderRequest):
    """Place a real market order on IBKR TWS/Gateway and record it if successful."""
    try:
        return await _execute_ibkr_order(order)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/command/ibkr")
async def place_ibkr_order_from_command(body: IBKRCommandRequest):
    """Execute a live IBKR order from a terminal-style command string."""
    try:
        order = parse_ibkr_terminal_command(
            command=body.command,
            portfolio_id=body.portfolio_id,
            record_trade=body.record_trade,
        )
        result = await _execute_ibkr_order(order)
        result["parsed_order"] = {
            "symbol": order.symbol,
            "quantity": order.quantity,
            "side": order.side,
            "asset_type": order.asset_type,
            "currency": order.currency,
            "exchange": order.exchange,
            "primary_exchange": order.primary_exchange,
            "last_trade_date": order.last_trade_date,
        }
        return result
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status/ibkr")
async def get_ibkr_status():
    """Check connectivity status with IBKR."""
    return ibkr_service.get_status()

@router.post("/connect/ibkr")
async def connect_ibkr():
    """Explicitly trigger connection attempt to IBKR."""
    await ibkr_service.connect()
    return ibkr_service.get_status()

@router.get("/history")
async def get_trading_history(portfolio_id: str = "main"):
    """Retrieve full trade history from storage."""
    return duckdb_repo.get_transactions(portfolio_id)

@router.post("/record")
async def record_transaction(
    type_str: str = Body(...),
    symbol: str = Body(...),
    shares: float = Body(...),
    price: float = Body(0.0),
    realized_pnl: float = Body(0.0),
    date: str = Body(None),
    portfolio_id: str = Body("main")
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
        custom_date=date,
        portfolio_id=portfolio_id
    )

    if success:
        # Reconcile portfolio holdings for this symbol
        _sync_portfolio_entry(symbol, portfolio_id)

    return {"status": "success" if success else "failed", "market_price_used": final_price <= 0, "recorded_price": final_price}

def _sync_portfolio_entry(symbol: str, portfolio_id: str = "main"):
    """Update the 'portfolio' table entry for a symbol based on transaction history aggregate."""
    from ...services.intraday_repository import intraday_repository # or similar search
    
    # 1. Get aggregate position from transactions
    transactions = duckdb_repo.get_transactions(portfolio_id)
    symbol_txs = [t for t in transactions if t['symbol'] == symbol]
    
    total_shares = sum(t['shares'] if t['type'] == 'BUY' else -t['shares'] for t in symbol_txs)
    
    # Simple weighted average for entry price (BUYS only for entry cost)
    buy_txs = [t for t in symbol_txs if t['type'] == 'BUY']
    total_cost = sum(t['shares'] * t['price'] for t in buy_txs)
    buy_shares = sum(t['shares'] for t in buy_txs)
    avg_entry = total_cost / buy_shares if buy_shares > 0 else 0
    
    # 2. Get existing metadata if symbol exists in portfolio or use defaults
    current_portfolio = duckdb_repo.get_portfolio(portfolio_id)
    existing = next((h for h in current_portfolio if h['symbol'] == symbol), None)
    
    if total_shares == 0:
        # Liquidated - Remove from portfolio
        new_portfolio = [h for h in current_portfolio if h['symbol'] != symbol]
        duckdb_repo.save_portfolio(new_portfolio, portfolio_id)
        return

    if existing:
        # Update existing entry
        existing['shares'] = total_shares
        existing['entryPrice'] = avg_entry
        # Preserve other metadata (name, sector, factor, sl, tp)
        duckdb_repo.save_portfolio(current_portfolio, portfolio_id)
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
        duckdb_repo.save_portfolio(current_portfolio, portfolio_id)



