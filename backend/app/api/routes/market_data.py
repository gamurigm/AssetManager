from fastapi import APIRouter, HTTPException, Query
from ...services.fmp_service import fmp_service
from typing import List, Dict, Any

router = APIRouter()

@router.get("/quote/{symbol}")
async def get_quote(symbol: str):
    """Get real-time quote for a specific symbol."""
    data = await fmp_service.get_quote(symbol)
    if not data:
        raise HTTPException(status_code=404, detail="Symbol not found")
    if "error" in data:
        raise HTTPException(status_code=500, detail=data["error"])
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
