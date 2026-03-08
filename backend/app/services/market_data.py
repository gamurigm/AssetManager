"""
MarketDataService - The Data Cascade Router
Now with Token Bucket Rate Limiting and DuckDB persistence.
"""

from typing import Dict, Any, Optional, Union
from datetime import date, datetime, timedelta
from .fmp_service import fmp_service
from .twelve_data_service import twelve_data_service
from .alpha_vantage_service import alpha_vantage_service
from .polygon_service import polygon_service
from .yahoo_finance_service import yahoo_finance_service
from .bybit_service import bybit_service
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
    CACHE_QUOTE_TTL = 90    # 90s cache — reduces provider calls significantly
    _INTRADAY_COVERAGE_HINT = (
        "Yahoo Finance only exposes about 7 days of 1m candles and about 1 month of 5m candles. "
        "Load longer intraday history into DuckDB first or use a provider like Polygon for the full range."
    )

    # Common crypto base symbols for auto-detection
    _CRYPTO_BASES = {
        "BTC", "ETH", "SOL", "XRP", "ADA", "DOT", "AVAX", "MATIC", "LINK",
        "UNI", "DOGE", "SHIB", "LTC", "BCH", "ATOM", "FIL", "APT", "ARB",
        "OP", "SUI", "SEI", "TIA", "NEAR", "FTM", "ALGO", "AAVE", "MKR",
        "CRV", "SNX", "COMP", "SAND", "MANA", "AXS", "ENJ", "GALA",
        "PEPE", "WIF", "BONK", "FLOKI", "INJ", "TRX", "BNB", "TON",
    }

    @staticmethod
    def _is_crypto(symbol: str) -> bool:
        """Detect if a symbol is a cryptocurrency pair."""
        sym = symbol.upper().replace("/", "").replace("-", "").replace("=", "")
        # Direct match: BTCUSDT, ETHUSDC, etc.
        for base in MarketDataService._CRYPTO_BASES:
            if sym.startswith(base):
                return True
        # Slash notation: BTC/USD, ETH/USDT
        if "/" in symbol:
            base = symbol.split("/")[0].upper()
            if base in MarketDataService._CRYPTO_BASES:
                return True
        return False

    # Known forex currency codes for auto-detection
    _FOREX_CODES = {
        "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "NZD", "HKD", "SGD",
        "SEK", "NOK", "DKK", "MXN", "CNY", "INR", "BRL", "ZAR", "TRY", "KRW",
        "THB", "PLN", "HUF", "CZK", "ILS", "CLP", "PHP", "IDR", "MYR", "RON",
    }

    @staticmethod
    def _is_forex(symbol: str) -> bool:
        """Detect 6-char forex pairs like USDMXN, EURUSD, CHFJPY."""
        sym = symbol.upper().replace("=X", "").replace("+", "")
        if len(sym) == 6:
            base, quote = sym[:3], sym[3:]
            return base in MarketDataService._FOREX_CODES and quote in MarketDataService._FOREX_CODES
        return False

    @staticmethod
    def _normalize_symbol(symbol: str, provider: str) -> str:
        """Helper to translate symbols based on provider requirements."""
        if provider == "yahoo":
            if symbol == "BTC/USD": return "BTC-USD"
            if symbol == "ETH/USD": return "ETH-USD"
            # Already has =X suffix
            if symbol.endswith("=X"): return symbol
            # Slash forex notation: EUR/USD → EURUSD=X
            if "/" in symbol:
                base, quote = symbol.split("/", 1)
                if base.upper() in MarketDataService._FOREX_CODES or quote.upper() in MarketDataService._FOREX_CODES:
                    return base.upper() + quote.upper() + "=X"
                return symbol.replace("/", "-")
            # 6-char bare forex: USDMXN → USDMXN=X
            if MarketDataService._is_forex(symbol):
                sym_clean = symbol.upper().replace("=X", "")
                return sym_clean + "=X"
            return symbol
        if provider == "twelve":
            return symbol
        if provider in ["fmp", "polygon"]:
            # Strip trailing =X (forex Yahoo suffix) cleanly, then remove remaining /=
            sym = symbol
            if sym.endswith("=X"):
                sym = sym[:-2]  # remove exactly "=X"
            return sym.replace("/", "").replace("=", "")
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

        # 0. Bybit (Crypto-native, fastest for crypto pairs)
        if MarketDataService._is_crypto(symbol):
            bybit_bucket = get_bucket("bybit")
            if bybit_bucket.can_request():
                bybit_bucket.consume()
                print(f"[MarketData] ✅ {symbol} → Bybit (Crypto)")
                bybit_data = await bybit_service.get_quote(symbol)
                if bybit_data and "price" in bybit_data and "error" not in bybit_data:
                    cache.set(cache_key, bybit_data, expire=MarketDataService.CACHE_QUOTE_TTL)
                    return bybit_data

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

        # ── Stale DuckDB fallback: return last known price rather than error ──
        if duckdb_store.has_data(symbol, min_rows=1):
            candles = duckdb_store.get_history(symbol, limit=1)
            if candles:
                last = candles[-1]
                stale_price = float(last.close) if hasattr(last, 'close') else float(last.get('close', 0))
                print(f"[MarketData] ⚠️ {symbol} → DuckDB stale fallback (all providers exhausted)")
                return {
                    "price": stale_price, "change": 0.0, "changePercentage": 0.0,
                    "source": "DuckDB (Stale)", "symbol": symbol,
                }

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
            print(f"[MarketData] [DuckDB] HIT for {symbol}")
            candles = duckdb_store.get_history(symbol, limit)
            return {"symbol": symbol, "historical": candles, "source": "DuckDB (Local)"}

        # --- API Fetch & Persist ---
        print(f"[MarketData] [DuckDB] MISS for {symbol}. Fetching from API...")

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
    def _validate_intraday_coverage(
        candles: list[dict],
        start: str,
        end: str,
        interval: str,
        tolerance_days: int = 7,
    ) -> dict:
        if not candles:
            raise ValueError(
                f"No {interval} candles available for {start} -> {end}."
            )

        requested_start = date.fromisoformat(start)
        requested_end = date.fromisoformat(end)
        available_start = datetime.fromisoformat(candles[0]["timestamp"].replace("Z", "")).date()
        available_end = datetime.fromisoformat(candles[-1]["timestamp"].replace("Z", "")).date()

        tolerance = timedelta(days=tolerance_days)
        starts_too_late = available_start > (requested_start + tolerance)
        ends_too_early = available_end < (requested_end - tolerance)

        if starts_too_late or ends_too_early:
            raise ValueError(
                f"Insufficient {interval} coverage for backfill {start} -> {end}. "
                f"Available {interval} data spans {available_start} -> {available_end}. "
                f"{MarketDataService._INTRADAY_COVERAGE_HINT}"
            )

        return {
            "available_start": available_start.isoformat(),
            "available_end": available_end.isoformat(),
        }

    @staticmethod
    async def backfill_intraday_range(
        symbol: str,
        start: str,
        end: str,
        intervals: Union[list[str], tuple[str, ...]] = ("1m", "5m"),
    ) -> dict:
        """
        Ensure long-range intraday history exists in DuckDB.

        This path is intentionally strict: it does not fall back to Yahoo because
        Yahoo can return recent-only slices for long ranges and poison yearly backtests.
        """
        normalized_intervals = tuple(dict.fromkeys(intervals))
        unsupported = [interval for interval in normalized_intervals if interval not in {"1m", "5m"}]
        if unsupported:
            raise ValueError(
                f"Unsupported intraday intervals for backfill: {', '.join(unsupported)}. Use 1m and/or 5m."
            )

        start_ts = f"{start} 00:00:00"
        end_ts = f"{end} 23:59:59"
        polygon_symbol = MarketDataService._normalize_symbol(symbol, "polygon")
        results: dict[str, dict[str, Any]] = {}

        for interval in normalized_intervals:
            candles = intraday_repository.get(symbol, interval, start_ts, end_ts)
            used_cache = False
            inserted = 0

            if candles:
                try:
                    coverage = MarketDataService._validate_intraday_coverage(candles, start, end, interval)
                    used_cache = True
                except ValueError:
                    candles = []

            if not candles:
                polygon_result = await polygon_service.get_intraday(
                    polygon_symbol,
                    interval,
                    start,
                    end,
                )
                if not polygon_result or "error" in polygon_result:
                    error_message = (
                        polygon_result.get("error", "Polygon returned no intraday data.")
                        if isinstance(polygon_result, dict)
                        else "Polygon returned no intraday data."
                    )
                    raise ValueError(
                        f"Polygon backfill failed for {symbol} {interval}: {error_message}"
                    )

                candles = polygon_result.get("candles", [])
                coverage = MarketDataService._validate_intraday_coverage(candles, start, end, interval)
                inserted = intraday_repository.save(symbol, interval, candles, source="polygon")

            results[interval] = {
                "status": "cached" if used_cache else "downloaded",
                "count": len(candles),
                "inserted": inserted,
                **coverage,
            }

        return {
            "symbol": symbol,
            "start_date": start,
            "end_date": end,
            "source": "DuckDB (Intraday Backfill)",
            "intervals": results,
        }

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
        # IMPORTANT: Use the actual start/end range to avoid false cache hits.
        # Compute the minimum expected candles for the interval so a 1-month
        # fetch doesn't satisfy a 6-month backtest request.
        _db_start = start or "2000-01-01"
        _db_end   = end   or "2099-01-01"

        # Estimate expected trading minutes in range to establish a coverage floor
        _min_candles_required = 10  # default for live/short queries
        if start and end:
            try:
                from datetime import date as _date
                _s = _date.fromisoformat(start)
                _e = _date.fromisoformat(end)
                _days = (_e - _s).days
                # ~6.5h × 60 min trading day; 5m interval = 78 candles/day
                _candles_per_day = 390 if interval == "1m" else 78
                # Require at least 50% coverage of expected candles
                _min_candles_required = max(10, int(_days * _candles_per_day * 0.5))
            except Exception:
                pass

        if intraday_repository.has_data(symbol, interval, _db_start, _db_end,
                                        min_count=_min_candles_required):
            print(f"[MarketData] DuckDB intraday HIT for {symbol} {interval} (≥{_min_candles_required} candles)")
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
