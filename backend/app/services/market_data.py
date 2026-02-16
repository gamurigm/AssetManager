from typing import Dict, Any, Optional, Union
from .fmp_service import fmp_service
from .twelve_data_service import twelve_data_service
from .alpha_vantage_service import alpha_vantage_service
from .polygon_service import polygon_service

# --- The Data Cascade Router --- #

class MarketDataService:
    @staticmethod
    async def get_price(symbol: str) -> Dict[str, Any]:
        """
        Unified method to get the BEST available price data.
        
        Strategy:
        1. US Stocks -> FMP (Fast, Unlimited)
        2. Crypto -> TwelveData (Best coverage)
        3. FMP Failover -> TwelveData -> Polygon
        """
        
        # --- CRYPTO ROUTE ---
        if "/" in symbol or "BTC" in symbol or "ETH" in symbol:
            print(f"[MarketData] Routing {symbol} to TwelveData (Crypto)")
            data = await twelve_data_service.get_price(symbol)
            if data: return data
            # Fallback to FMP for crypto
            return await fmp_service.get_quote(symbol.replace("/", ""))

        # --- STOCK ROUTE (Default) ---
        # 1. Primary: FMP
        print(f"[MarketData] Routing {symbol} to FMP (Primary)")
        quote = await fmp_service.get_quote(symbol)
        if quote and "price" in quote:
            return {
                "price": quote["price"],
                "change": quote.get("change"),
                "volume": quote.get("volume"),
                "source": "FMP (Real-time)"
            }
        
        # 2. Secondary: TwelveData (800 req/day)
        print(f"[MarketData] FMP Failed/Empty. Routing {symbol} to TwelveData")
        td_data = await twelve_data_service.get_price(symbol)
        if td_data:
            return td_data
            
        # 3. Fallback: Polygon (EOD / Previous Close)
        print(f"[MarketData] Live Data Failed. Fetching EOD from Polygon")
        poly_data = await polygon_service.get_previous_close(symbol)
        if poly_data:
            return {
                "price": poly_data["close"],
                "date": poly_data["date"],
                "source": "Polygon (EOD - Delayed)"
            }

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
        """Unified method for historical EOD data."""
        print(f"[MarketData] Fetching history for {symbol} from FMP")
        return await fmp_service.get_historical(symbol, limit)

market_data_service = MarketDataService()
