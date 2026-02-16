from fastapi import APIRouter, HTTPException, Query
from ...services.fmp_service import fmp_service
from ...services.market_data import market_data_service
from typing import List, Dict, Any

router = APIRouter()

@router.get("/quote/{symbol:path}")
async def get_quote(symbol: str):
    """Get real-time quote for a specific symbol using Unified Market Data Service."""
    data = await market_data_service.get_price(symbol)
    if not data or "error" in data:
        raise HTTPException(status_code=404, detail=data.get("error", "Data not found"))
    return data

@router.get("/historical/{symbol:path}")
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

# --- TradingView UDF (Universal Data Feed) Endpoints ---
# This allows any TradingView-compatible library to consume our data

@router.get("/udf/config")
async def udf_config():
    return {
        "supports_search": True,
        "supports_group_request": False,
        "supports_marks": False,
        "supports_timescale_marks": False,
        "supports_time": True,
        "exchanges": [{"value": "", "name": "All Exchanges", "desc": ""}],
        "symbols_types": [{"name": "All types", "value": ""}],
        "supported_resolutions": ["1", "5", "15", "30", "60", "1D", "1W", "1M"]
    }

@router.get("/udf/symbols")
async def udf_symbols(symbol: str):
    # Standard metadata for a symbol
    return {
        "name": symbol,
        "ticker": symbol,
        "description": f"{symbol} Asset",
        "type": "stock",
        "session": "24x7" if "/" in symbol else "0930-1600",
        "timezone": "America/New_York",
        "exchange": "Market",
        "minmov": 1,
        "pricescale": 100,
        "has_intraday": True,
        "supported_resolutions": ["1", "5", "15", "30", "60", "1D", "1W", "1M"],
        "volume_precision": 2,
        "data_status": "streaming"
    }

@router.get("/udf/history")
async def udf_history(
    symbol: str, 
    from_time: int = Query(..., alias="from"), 
    to_time: int = Query(..., alias="to"), 
    resolution: str = "D"
):
    """
    UDF History endpoint.
    Returns bars in the format: {s: "ok", t: [], o: [], h: [], l: [], c: [], v: []}
    """
    # Convert resolution to Yahoo Finance period/interval
    # For now, we simplify to Daily if not specified
    res_map = {"D": "1d", "1D": "1d", "W": "1wk", "M": "1mo"}
    interval = res_map.get(resolution, "1d")
    
    # We use our Yahoo Finance service
    yf_symbol = symbol.replace("/", "-")
    data = await yahoo_finance_service.get_historical(yf_symbol, period="max", interval=interval)
    
    if "error" in data or not data.get("historical"):
        return {"s": "no_data"}

    # Filter by time and format for UDF
    t, o, h, l, c, v = [], [], [], [], [], []
    import datetime
    
    for bar in data["historical"]:
        # Convert date "YYYY-MM-DD" to unix timestamp
        dt = datetime.datetime.strptime(bar["date"], "%Y-%m-%d")
        ts = int(dt.timestamp())
        
        if from_time <= ts <= to_time:
            t.append(ts)
            o.append(bar["open"])
            h.append(bar["high"])
            l.append(bar["low"])
            c.append(bar["close"])
            v.append(bar["volume"])

    if not t:
        return {"s": "no_data"}
        
    return {
        "s": "ok",
        "t": t, "o": o, "h": h, "l": l, "c": c, "v": v
    }

@router.get("/udf/time")
async def udf_time():
    import time
    return int(time.time())
