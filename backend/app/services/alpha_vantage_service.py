from ..core.config import settings
import httpx
from typing import List, Dict, Any, Optional

class AlphaVantageService:
    BASE_URL = "https://www.alphavantage.co/query"
    
    @staticmethod
    async def get_indicator(symbol: str, function: str = "RSI", interval: str = "daily") -> Optional[Dict[str, Any]]:
        """
        Get Technical Indicators (RSI, ADX, MACD).
        Limit: 25 req/day. Use ONLY when FMP/TwelveData fail or for specific studies.
        """
        params = {
            "function": function,
            "symbol": symbol,
            "interval": interval,
            "time_period": "14", # Standard period
            "series_type": "close",
            "apikey": settings.ALPHA_VANTAGE_API_KEY
        }
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(AlphaVantageService.BASE_URL, params=params)
                response.raise_for_status()
                data = response.json()
                
                # Check for standard API limit message
                if "Note" in data:
                    print("AlphaVantage Limit Reached")
                    return None
                    
                meta = f"Technical Analysis: {function}"
                if meta in data:
                    # Return just the latest data point to save context
                    series = data[meta]
                    last_date = sorted(series.keys())[-1]
                    return {
                        "indicator": function,
                        "date": last_date,
                        "value": series[last_date],
                        "source": "AlphaVantage"
                    }
                return None
        except Exception as e:
            print(f"AlphaVantage Error: {e}")
            return None

alpha_vantage_service = AlphaVantageService()
