"""
Bybit API Routes — Crypto-specific endpoints powered by Bybit V5 REST API.
"""

from fastapi import APIRouter, HTTPException, Query
from ...services.bybit_service import bybit_service

router = APIRouter()


@router.get("/tickers")
async def get_tickers(symbol: str = Query(..., description="Trading pair, e.g. BTCUSDT")):
    """Get real-time ticker (price, volume, bid/ask) from Bybit."""
    data = await bybit_service.get_quote(symbol)
    if not data or "error" in data:
        raise HTTPException(status_code=404, detail=data.get("error", "Ticker not found"))
    return data


@router.get("/klines/{symbol}")
async def get_klines(
    symbol: str,
    interval: str = Query("D", description="1m,5m,15m,1h,4h,D,W,M"),
    limit: int = Query(200, description="Number of candles (max 1000)"),
    start: int = Query(None, description="Start time in ms (optional)"),
    end: int = Query(None, description="End time in ms (optional)"),
):
    """Get historical klines/candles from Bybit."""
    data = await bybit_service.get_klines(symbol, interval, limit, start, end)
    if not data or "error" in data:
        raise HTTPException(status_code=404, detail=data.get("error", "Kline data not found"))
    return data


@router.get("/orderbook/{symbol}")
async def get_orderbook(
    symbol: str,
    depth: int = Query(25, description="Orderbook depth (max 200)"),
):
    """Get orderbook (bids/asks) from Bybit."""
    data = await bybit_service.get_orderbook(symbol, depth)
    if not data or "error" in data:
        raise HTTPException(status_code=404, detail=data.get("error", "Orderbook not found"))
    return data


@router.get("/instruments")
async def get_instruments(
    category: str = Query("spot", description="spot, linear, inverse"),
):
    """List available trading instruments on Bybit."""
    data = await bybit_service.get_instruments(category)
    if not data or "error" in data:
        raise HTTPException(status_code=500, detail=data.get("error", "Failed to fetch instruments"))
    return data
