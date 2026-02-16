from ..core.config import settings
import httpx
from typing import List, Dict, Any, Optional

class TwelveDataService:
    BASE_URL = "https://api.twelvedata.com"
    
    @staticmethod
    async def get_price(symbol: str) -> Optional[Dict[str, Any]]:
        """
        Get real-time price (quote).
        Excellent coverage for Crypto and Forex.
        Limit: 800 req/day, 8 req/min.
        """
        url = f"{TwelveDataService.BASE_URL}/price"
        params = {
            "symbol": symbol,
            "apikey": settings.TWELVE_DATA_API_KEY
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params)
                data = response.json()
                print(f"[TwelveData] Response for {symbol}: {data}")
                response.raise_for_status()
                # TwelveData returns {'price': '...'} or error
                if "price" in data:
                    return {
                        "price": float(data["price"]),
                        "symbol": symbol,
                        "source": "TwelveData"
                    }
                return None
        except Exception as e:
            print(f"TwelveData Error: {e}")
            return None

    @staticmethod
    async def get_crypto_price(symbol: str = "BTC/USD") -> Optional[Dict[str, Any]]:
        """Wrapper specifically for Crypto pairs."""
        return await TwelveDataService.get_price(symbol)

twelve_data_service = TwelveDataService()
