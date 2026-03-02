"""
Finviz API Routes — Scraped data from Finviz.com
"""

from fastapi import APIRouter, HTTPException, Query
from ...services.finviz_service import finviz_service

router = APIRouter()


@router.get("/insider-trading")
async def get_insider_trading(
    filter: str = Query("latest", description="latest, top_week, top_owner_week"),
    tc: int = Query(7, description="Transaction filter (7=All)"),
):
    """
    Get insider trading data scraped from Finviz.
    Filters: latest, top_week (by value), top_owner_week (by ownership %).
    """
    data = await finviz_service.get_insider_trading(filter_type=filter, tc=tc)
    if "error" in data and not data.get("rows"):
        raise HTTPException(status_code=502, detail=data["error"])
    return data


@router.get("/scrape")
async def scrape_page(
    path: str = Query(..., description="Finviz page path, e.g. insidertrading.ashx?tc=7"),
):
    """
    Generic scraper: fetch and parse any Finviz table page.
    Returns raw table data as JSON.
    """
    data = await finviz_service.scrape_generic(path)
    if "error" in data and not data.get("rows"):
        raise HTTPException(status_code=502, detail=data["error"])
    return data


@router.get("/insider-trading/history")
async def get_insider_history(
    ticker: str = Query(None, description="Filter by ticker (optional)"),
    limit: int = Query(100, description="Number of records to return"),
):
    """
    Get historical insider trading data from local database.
    This shows all previously scraped records.
    """
    return await finviz_service.get_stored_insider_trades(ticker, limit)
