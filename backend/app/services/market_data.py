"""
MarketDataService - The Data Cascade Router
Now with Token Bucket Rate Limiting and DuckDB persistence.
"""

from typing import Dict, Any, Optional, Union
from .fmp_service import fmp_service
from .twelve_data_service import twelve_data_service
from .alpha_vantage_service import alpha_vantage_service
from .polygon_service import polygon_service
from .yahoo_finance_service import yahoo_finance_service
from .duckdb_store import duckdb_store
from .intraday_repository import intraday_repository, DuckDBIntradayRepository
from ..core.rate_limiter import get_bucket

import time
import os
from diskcache import Cache

# Set up local cache directory for hot quotes
CACHE_DIR = os.path.join(os.path.dirname(__file__), "../../.cache")
cache = Cache(CACHE_DIR)

# --- The Data Cascade Router --- #

class MarketDataService:
    CACHE_QUOTE_TTL = 60    # 1 minute for quotes to respect rate limits

    @staticmethod
    def _normalize_symbol(symbol: str, provider: str) -> str:
        """Helper to translate symbols based on provider requirements."""
        if provider == "yahoo":
            if symbol == "BTC/USD": return "BTC-USD"
            if symbol == "ETH/USD": return "ETH-USD"
            if "/" in symbol:
                if any(curr in symbol for curr in ["EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "NZD"]):
                    return symbol.replace("/", "") + "=X"
                return symbol.replace("/", "-")
            return symbol.replace("=", "-")
        if provider == "twelve":
            return symbol
        if provider in ["fmp", "polygon"]:
            return symbol.replace("/", "").replace("=", "")
        return symbol

    @staticmethod
    async def get_price(symbol: str) -> Dict[str, Any]:
        """
        Unified method with optimized cascade, rate limiting, and symbol translation.
        """
        cache_key = f"quote_{symbol.replace('/', '_')}"
        cached = cache.get(cache_key)
        if cached:
            print(f"[MarketData] Cache HIT for {symbol}")
            return cached

        # --- CASCADE WITH RATE LIMITING ---

        # 1. Yahoo Finance (Stable, generous limits)
        yf_bucket = get_bucket("yahoo")
        if yf_bucket.can_request():
            yf_bucket.consume()
            print(f"[MarketData] ✅ {symbol} → Yahoo Finance")
            yf_sym = MarketDataService._normalize_symbol(symbol, "yahoo")
            yf_data = await yahoo_finance_service.get_quote(yf_sym)
            if yf_data and "price" in yf_data and "error" not in yf_data:
                yf_data["source"] = "Yahoo Finance (Live)"
                cache.set(cache_key, yf_data, expire=MarketDataService.CACHE_QUOTE_TTL)
                return yf_data

        # 2. FMP (High quality, strict limits)
        fmp_bucket = get_bucket("fmp")
        if fmp_bucket.can_request():
            fmp_bucket.consume()
            print(f"[MarketData] ✅ {symbol} → FMP")
            fmp_sym = MarketDataService._normalize_symbol(symbol, "fmp")
            quote = await fmp_service.get_quote(fmp_sym)
            if quote and "price" in quote:
                price = float(quote["price"])
                prev_close = quote.get("previousClose")
                if prev_close:
                    prev_close = float(prev_close)
                    change = price - prev_close
                    pct_change = (change / prev_close) * 100 if prev_close != 0 else 0.0
                else:
                    change = float(quote.get("change") or 0.0)
                    pct_change = float(quote.get("changesPercentage") or 0.0)
                res = {
                    "price": price, "change": change, "changePercentage": pct_change,
                    "volume": quote.get("volume"), "source": "FMP (Real-time)"
                }
                cache.set(cache_key, res, expire=MarketDataService.CACHE_QUOTE_TTL)
                return res
        else:
            print(f"[MarketData] ⛔ FMP rate limited for {symbol}")

        # 3. TwelveData
        td_bucket = get_bucket("twelvedata")
        if td_bucket.can_request():
            td_bucket.consume()
            print(f"[MarketData] ✅ {symbol} → TwelveData")
            td_sym = MarketDataService._normalize_symbol(symbol, "twelve")
            td_data = await twelve_data_service.get_price(td_sym)
            if td_data and "price" in td_data:
                cache.set(cache_key, td_data, expire=MarketDataService.CACHE_QUOTE_TTL)
                return td_data
        else:
            print(f"[MarketData] ⛔ TwelveData rate limited for {symbol}")

        # 4. Polygon (EOD)
        poly_bucket = get_bucket("polygon")
        if poly_bucket.can_request():
            poly_bucket.consume()
            print(f"[MarketData] ✅ {symbol} → Polygon (EOD)")
            poly_sym = MarketDataService._normalize_symbol(symbol, "polygon")
            poly_data = await polygon_service.get_previous_close(poly_sym)
            if poly_data and "close" in poly_data:
                res = {
                    "price": poly_data["close"], "change": 0.0, "changePercentage": 0.0,
                    "source": "Polygon (EOD)"
                }
                cache.set(cache_key, res, expire=MarketDataService.CACHE_QUOTE_TTL)
                return res
        else:
            print(f"[MarketData] ⛔ Polygon rate limited for {symbol}")

        return {"error": f"All providers exhausted or rate limited for {symbol}."}

    @staticmethod
    async def get_historical(symbol: str, limit: int = 300) -> Dict[str, Any]:
        """
        Unified historical data with DuckDB persistence.
        1. Check DuckDB (instant, local)
        2. If missing, fetch from API and store in DuckDB
        """
        # --- DuckDB First (Local, instant) ---
        if duckdb_store.has_data(symbol, min_rows=20):
            print(f"[MarketData] 🦆 DuckDB HIT for {symbol}")
            candles = duckdb_store.get_history(symbol, limit)
            return {"symbol": symbol, "historical": candles, "source": "DuckDB (Local)"}

        # --- API Fetch & Persist ---
        print(f"[MarketData] 🦆 DuckDB MISS for {symbol}. Fetching from API...")

        # Yahoo Finance first (no strict limits for historical)
        yf_bucket = get_bucket("yahoo")
        if yf_bucket.can_request():
            yf_bucket.consume()
            yf_sym = MarketDataService._normalize_symbol(symbol, "yahoo")
            data = await yahoo_finance_service.get_historical(yf_sym)
            if data and "historical" in data:
                # Persist to DuckDB for future instant access
                duckdb_store.upsert_candles(symbol, data["historical"], source="yahoo")
                data["source"] = "Yahoo Finance → DuckDB"
                return data

        # FMP fallback
        fmp_bucket = get_bucket("fmp")
        if fmp_bucket.can_request():
            fmp_bucket.consume()
            fmp_sym = MarketDataService._normalize_symbol(symbol, "fmp")
            fmp_data = await fmp_service.get_historical(fmp_sym, limit)
            if fmp_data and "historical" in fmp_data:
                duckdb_store.upsert_candles(symbol, fmp_data["historical"], source="fmp")
                fmp_data["source"] = "FMP → DuckDB"
                return fmp_data

        return {"error": f"Historical data unavailable for {symbol}."}

    @staticmethod
    async def get_intraday(
        symbol: str,
        interval: str = "1m",
        period: str = "5d",
        start: str = None,
        end: str = None,
    ) -> dict:
        """
        Unified intraday OHLCV with DuckDB persistence.
        Cascade:  DuckDB (instant)  →  Yahoo Finance  →  persist to DuckDB
        Returns:
            { "symbol", "interval", "candles": [CandleRow], "source" }
        """
        # 1. Try local DuckDB (instant, free)
        if intraday_repository.has_data(symbol, interval,
                                        start or "2000-01-01",
                                        end or "2099-01-01"):
            print(f"[MarketData] DuckDB intraday HIT for {symbol} {interval}")
            candles = intraday_repository.get(symbol, interval, start, end)
            return {"symbol": symbol, "interval": interval, "candles": candles,
                    "source": "DuckDB (Intraday)"}

        # 2. Try Polygon (Bulk Download - 50k candles per request)
        print(f"[MarketData] DuckDB intraday MISS for {symbol} {interval}. Fetching from Polygon...")
        poly_bucket = get_bucket("polygon")
        if poly_bucket.can_request() and (start and end):
            poly_bucket.consume()
            poly_sym = MarketDataService._normalize_symbol(symbol, "polygon")
            poly_result = await polygon_service.get_intraday(poly_sym, interval, start, end)
            if poly_result and "candles" in poly_result:
                # Persist massive batch to DuckDB
                intraday_repository.save(symbol, interval, poly_result["candles"], source="polygon")
                poly_result["source"] = "Polygon.io -> DuckDB (Intraday Bulk)"
                return poly_result
            if poly_result and "error" in poly_result:
                print(f"[MarketData] Polygon intraday error for {symbol}: {poly_result['error']}")

        # 3. Fallback to Yahoo Finance (7-day max for M1)
        print(f"[MarketData] Falling back to Yahoo Finance for {symbol} {interval}...")
        yf_bucket = get_bucket("yahoo")
        if yf_bucket.can_request():
            yf_bucket.consume()
            yf_sym = MarketDataService._normalize_symbol(symbol, "yahoo")
            result = await yahoo_finance_service.get_intraday(yf_sym, interval, period)
            if result and "candles" in result:
                # Persist to DuckDB
                intraday_repository.save(symbol, interval, result["candles"], source="yahoo")
                result["source"] = "Yahoo Finance -> DuckDB (Intraday)"
                return result
            if "error" in result:
                print(f"[MarketData] Yahoo intraday error for {symbol}: {result['error']}")

        return {"error": f"Intraday data unavailable for {symbol} ({interval})."}


market_data_service = MarketDataService()
