"""
Market Data API Routes — Clean Architecture
Routes depend on Use Cases, NOT on concrete services.
"""

import datetime
from fastapi import APIRouter, HTTPException, Query
from ...core.container import get_quote, get_historical, fmp_provider, duckdb_repo
from ...core.rate_limiter import get_all_statuses

router = APIRouter()


@router.get("/system/status")
async def system_status():
    """Real-time monitoring: API rate limits + DuckDB stats."""
    return {
        "rate_limits": get_all_statuses(),
        "database": duckdb_repo.get_stats(),
    }


@router.get("/quote/{symbol:path}")
async def get_quote_endpoint(symbol: str):
    """Get real-time quote using the provider cascade."""
    data = await get_quote.execute(symbol)
    if not data or "error" in data:
        raise HTTPException(status_code=404, detail=data.get("error", "Data not found"))
    return data


@router.get("/historical/{symbol:path}")
async def get_historical_endpoint(symbol: str, limit: int = 300):
    """Get historical OHLCV data (DuckDB-first, then API fallback)."""
    data = await get_historical.execute(symbol, limit)
    if not data or "error" in data:
        raise HTTPException(status_code=404, detail=data.get("error", "Not found"))
    return data


@router.get("/profile/{symbol}")
async def get_profile(symbol: str):
    """Get company profile (FMP-specific)."""
    data = await fmp_provider.get_profile(symbol)
    if not data:
        raise HTTPException(status_code=404, detail="Symbol not found")
    return data


@router.get("/search")
async def search_ticker(query: str, limit: int = 10):
    """Search for symbols (FMP-specific)."""
    return await fmp_provider.search_ticker(query, limit)


# --- TradingView UDF Endpoints ---

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
        "supported_resolutions": ["1", "5", "15", "30", "60", "1D", "1W", "1M"],
    }


@router.get("/udf/symbols")
async def udf_symbols(symbol: str):
    return {
        "name": symbol, "ticker": symbol, "description": f"{symbol} Asset",
        "type": "stock",
        "session": "24x7" if "/" in symbol else "0930-1600",
        "timezone": "America/New_York", "exchange": "Market",
        "minmov": 1, "pricescale": 100, "has_intraday": True,
        "supported_resolutions": ["1", "5", "15", "30", "60", "1D", "1W", "1M"],
        "volume_precision": 2, "data_status": "streaming",
    }


@router.get("/udf/history")
async def udf_history(
    symbol: str,
    from_time: int = Query(..., alias="from"),
    to_time: int = Query(..., alias="to"),
    resolution: str = "D",
):
    """UDF History — routes through Clean Architecture use case."""
    data = await get_historical.execute(symbol, limit=1000)
    if not data or "error" in data or not data.get("historical"):
        return {"s": "no_data"}

    t, o, h, l, c, v = [], [], [], [], [], []
    for bar in data["historical"]:
        dt = datetime.datetime.strptime(bar["date"], "%Y-%m-%d")
        ts = int(dt.timestamp())
        if from_time <= ts <= to_time:
            t.append(ts)
            o.append(bar["open"])
            h.append(bar["high"])
            l.append(bar["low"])
            c.append(bar["close"])
            v.append(bar.get("volume", 0))

    if not t:
        return {"s": "no_data"}
    return {"s": "ok", "t": t, "o": o, "h": h, "l": l, "c": c, "v": v}


@router.get("/udf/time")
async def udf_time():
    import time
    return int(time.time())
