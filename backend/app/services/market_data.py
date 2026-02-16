from typing import Dict, Any, Optional, Union
from .fmp_service import fmp_service
from .twelve_data_service import twelve_data_service
from .alpha_vantage_service import alpha_vantage_service
from .polygon_service import polygon_service
from .yahoo_finance_service import yahoo_finance_service

import time
import os
from diskcache import Cache

# Set up local cache directory
CACHE_DIR = os.path.join(os.path.dirname(__file__), "../../.cache")
cache = Cache(CACHE_DIR)

# --- The Data Cascade Router --- #

class MarketDataService:
    CACHE_QUOTE_TTL = 20    # 20 seconds for quotes
    CACHE_HIST_TTL = 3600   # 1 hour for historical data

    @staticmethod
    async def get_price(symbol: str) -> Dict[str, Any]:
        """
        Unified method to get the BEST available price data.
        Uses persistent disk cache to avoid hitting API limits.
        """
        cache_key = f"quote_{symbol}"
        cached = cache.get(cache_key)
        if cached:
            print(f"[MarketData] Serving {symbol} quote from PERSISTENT cache")
            return cached

        # --- CRYPTO ROUTE ---
        if "/" in symbol or "BTC" in symbol or "ETH" in symbol:
            print(f"[MarketData] Routing {symbol} to TwelveData (Crypto)")
            data = await twelve_data_service.get_price(symbol)
            if data: 
                cache.set(cache_key, data, expire=MarketDataService.CACHE_QUOTE_TTL)
                return data
            # Fallback to FMP for crypto
            fmp_crypto = await fmp_service.get_quote(symbol.replace("/", ""))
            if fmp_crypto:
                 cache.set(cache_key, fmp_crypto, expire=MarketDataService.CACHE_QUOTE_TTL)
                 return fmp_crypto
            return {"error": "No crypto data available."}

        # --- STOCK ROUTE (Default) ---
        # 1. Primary: FMP
        print(f"[MarketData] Routing {symbol} to FMP (Primary)")
        quote = await fmp_service.get_quote(symbol)
        if quote and "price" in quote:
            res = {
                "price": quote["price"],
                "change": quote.get("change"),
                "volume": quote.get("volume"),
                "source": "FMP (Real-time)"
            }
            cache.set(cache_key, res, expire=MarketDataService.CACHE_QUOTE_TTL)
            return res
        
        # 2. Secondary: TwelveData (800 req/day)
        print(f"[MarketData] FMP Failed/Empty. Routing {symbol} to TwelveData")
        td_data = await twelve_data_service.get_price(symbol)
        if td_data:
            cache.set(cache_key, td_data, expire=MarketDataService.CACHE_QUOTE_TTL)
            return td_data
            
        # 3. Fallback: Polygon (EOD / Previous Close)
        print(f"[MarketData] Live Data Failed. Fetching EOD from Polygon")
        poly_data = await polygon_service.get_previous_close(symbol)
        if poly_data:
            res = {
                "price": poly_data["close"],
                "date": poly_data["date"],
                "source": "Polygon (EOD - Delayed)"
            }
            cache.set(cache_key, res, expire=MarketDataService.CACHE_QUOTE_TTL)
            return res

        # 4. Final: Yahoo Finance
        print(f"[MarketData] Polygon Failed. Final attempt with Yahoo Finance")
        yf_data = await yahoo_finance_service.get_quote(symbol.replace("/", "-"))
        if yf_data and not "error" in yf_data:
            cache.set(cache_key, yf_data, expire=MarketDataService.CACHE_QUOTE_TTL)
            return yf_data

        return {"error": "No market data available from any provider."}

    @staticmethod
    async def get_technical_indicator(symbol: str, indicator: str) -> Dict[str, Any]:
        """
        Get Technical Analysis (RSI, MACD, etc.) using Alpha Vantage.
        """
        # Alpha Vantage is the specialist here
        print(f"[MarketData] Fetching {indicator} for {symbol} from Alpha Vantage")
        data = await alpha_vantage_service.get_indicator(symbol, indicator)
        if data:
            return data
            
        return {"error": "Technical indicator unavailable (Limit reached?)"}

    @staticmethod
    async def get_historical(symbol: str, limit: int = 30) -> Dict[str, Any]:
        """Unified method for historical EOD data. Prefer Yahoo Finance."""
        cache_key = f"hist_{symbol}"
        cached = cache.get(cache_key)
        if cached:
            print(f"[MarketData] Serving {symbol} history from PERSISTENT cache")
            return cached

        print(f"[MarketData] Fetching history for {symbol} from Yahoo Finance")
        
        # Yahoo Finance uses - instead of / for some pairs, but yfinance usually handles BTC-USD
        yf_symbol = symbol.replace("/", "-")
        data = await yahoo_finance_service.get_historical(yf_symbol)
        
        if data and "historical" in data:
            cache.set(cache_key, data, expire=MarketDataService.CACHE_HIST_TTL)
            return data
            
        print(f"[MarketData] Yahoo Finance failed for {symbol}. Falling back to FMP.")
        fmp_data = await fmp_service.get_historical(symbol, limit)
        if fmp_data:
            cache.set(cache_key, fmp_data, expire=MarketDataService.CACHE_HIST_TTL)
        return fmp_data

market_data_service = MarketDataService()
