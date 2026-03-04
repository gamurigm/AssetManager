"""
Market Data API Routes — Clean Architecture
Routes depend on Use Cases, NOT on concrete services.
"""

import asyncio
import datetime
from fastapi import APIRouter, HTTPException, Query, BackgroundTasks
from ...core.container import get_quote, get_historical, fmp_provider, yahoo_provider, duckdb_repo
from ...core.rate_limiter import get_all_statuses

router = APIRouter()

# Track symbols currently being prefetched to avoid duplicate work
_prefetching: set[str] = set()


async def _background_prefetch(symbol: str):
    """Background task: fetch + persist historical data into DuckDB."""
    if symbol in _prefetching:
        return  # Already in progress
    _prefetching.add(symbol)
    try:
        print(f"[Prefetch] ⚡ Starting background sync for {symbol}...")
        await get_historical.execute(symbol, limit=10000)
        print(f"[Prefetch] ✅ {symbol} persisted to DuckDB.")
    except Exception as e:
        print(f"[Prefetch] ❌ {symbol} failed: {e}")
    finally:
        _prefetching.discard(symbol)


@router.get("/system/status")
async def system_status():
    """Real-time monitoring: API rate limits + DuckDB stats."""
    return {
        "rate_limits": get_all_statuses(),
        "database": duckdb_repo.get_stats(),
        "prefetching": list(_prefetching),
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


@router.get("/intraday/{symbol:path}")
async def get_intraday_endpoint(
    symbol: str,
    interval: str = Query("1h", description="Candle interval: 5m, 15m, 1h, 4h"),
    period: str = Query("1mo", description="Lookback window: 5d, 1mo, 3mo, 6mo"),
):
    """Get intraday OHLCV candles (DuckDB-first, then Yahoo/Polygon fallback)."""
    from ...services.market_data import market_data_service
    data = await market_data_service.get_intraday(symbol, interval, period)
    if not data or "error" in data:
        raise HTTPException(status_code=404, detail=data.get("error", "Intraday data unavailable"))
    # Normalize output to match the historical endpoint shape
    candles = data.get("candles", [])
    historical = []
    for c in candles:
        row = c if isinstance(c, dict) else {
            "date": str(getattr(c, "ts", getattr(c, "date", ""))),
            "open": getattr(c, "open", 0),
            "high": getattr(c, "high", 0),
            "low": getattr(c, "low", 0),
            "close": getattr(c, "close", 0),
            "volume": getattr(c, "volume", 0),
        }
        # Ensure "date" key exists for dicts from DuckDB
        if isinstance(row, dict) and "date" not in row and "ts" in row:
            row["date"] = str(row["ts"])
        historical.append(row)
    return {"symbol": symbol, "historical": historical, "source": data.get("source", "intraday")}


@router.get("/profile/{symbol}")
async def get_profile(symbol: str):
    """Get company profile (FMP-specific)."""
    data = await fmp_provider.get_profile(symbol)
    if not data:
        raise HTTPException(status_code=404, detail="Symbol not found")
    return data


@router.get("/volume-profile/{symbol:path}")
async def get_volume_profile(symbol: str, days: int = Query(7, description="Number of days to analyze")):
    """Get Volume Profile (POC, VAH, VAL, HVNs) for a symbol based on recent intraday data."""
    from ...services.intraday_repository import intraday_repository
    from ...agents.strategies.engine.volume_profile import VolumeProfileCalculator
    from datetime import date, timedelta
    
    end_date = date.today()
    start_date = end_date - timedelta(days=days)
    
    try:
        # Fetch M5 candles to build the profile
        candles = await intraday_repository.fetch_intraday(symbol, "5m", start_date, end_date)
        if not candles:
            raise HTTPException(status_code=404, detail="No intraday data found for Volume Profile")
            
        calc = VolumeProfileCalculator(num_bins=50, value_area_pct=0.70, hvn_threshold_pct=0.5)
        res = calc.compute(candles)
        
        return {
            "symbol": symbol,
            "period_days": days,
            "poc": res.poc,
            "vah": res.vah,
            "val": res.val,
            "hvn_edges": [{"low": edge[0], "high": edge[1]} for edge in res.hvn_edges],
            "profile": [{"low": n.price_low, "high": n.price_high, "vol": n.volume} for n in res.profile]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Volume Profile error: {str(e)}")


@router.get("/search")
async def search_ticker(query: str, limit: int = 15, prefetch: bool = True):
    """Search for symbols globally. Auto-prefetches historical data for all results."""
    results = await yahoo_provider.search_ticker(query, limit)

    # Fire-and-forget: prefetch historical data for all search results in parallel
    if prefetch and results:
        symbols_to_prefetch = [r["symbol"] for r in results if r["symbol"] not in _prefetching]
        for s in symbols_to_prefetch:
            asyncio.ensure_future(_background_prefetch(s))

    return results


@router.post("/prefetch/{symbol:path}")
async def prefetch_symbol(symbol: str):
    """Manually trigger background historical data download for a single symbol."""
    if symbol in _prefetching:
        return {"status": "already_in_progress", "symbol": symbol}

    asyncio.ensure_future(_background_prefetch(symbol))
    return {"status": "started", "symbol": symbol}


@router.post("/prefetch-batch")
async def prefetch_batch(symbols: list[str]):
    """Trigger parallel historical data download for multiple symbols at once."""
    started = []
    skipped = []
    for s in symbols:
        if s in _prefetching:
            skipped.append(s)
        else:
            asyncio.ensure_future(_background_prefetch(s))
            started.append(s)

    return {"started": started, "skipped": skipped, "total": len(started)}


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
