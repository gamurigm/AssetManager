from fastapi import APIRouter, HTTPException, Query
from ...services.fmp_service import fmp_service
from ...services.market_data import market_data_service
from typing import List, Dict, Any

router = APIRouter()

@router.get("/quote/{symbol}")
async def get_quote(symbol: str):
    """Get real-time quote for a specific symbol using Unified Market Data Service."""
    data = await market_data_service.get_price(symbol)
    if not data or "error" in data:
        raise HTTPException(status_code=404, detail=data.get("error", "Data not found"))
    return data

@router.get("/historical/{symbol}")
async def get_historical(symbol: str, limit: int = 30):
    """Get historical data (OHLC) for a symbol."""
    data = await market_data_service.get_historical(symbol, limit)
    if not data or "error" in data:
        raise HTTPException(status_code=404, detail=data.get("error", "Historical data not found"))
    return data

@router.get("/profile/{symbol}")
async def get_profile(symbol: str):
    """Get company profile."""
    data = await fmp_service.get_profile(symbol)
    if not data:
        raise HTTPException(status_code=404, detail="Symbol not found")
    if "error" in data:
        raise HTTPException(status_code=500, detail=data["error"])
    return data

@router.get("/search")
async def search_ticker(query: str, limit: int = 10):
    """Search for symbols."""
    return await fmp_service.search_ticker(query, limit)
