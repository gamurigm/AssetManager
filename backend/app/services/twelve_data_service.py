from ..core.config import settings
import httpx
from app.infrastructure.http.api_server_client import ApiServerError, provider_get
from typing import List, Dict, Any, Optional

class TwelveDataService:
    BASE_URL = settings.TWELVE_DATA_BASE_URL
    
    @staticmethod
    async def get_price(symbol: str) -> Optional[Dict[str, Any]]:
        """
        Get real-time quote.
        Limit: 800 req/day, 8 req/min.
        """
        url = f"{TwelveDataService.BASE_URL}/quote"
        params = {
            "symbol": symbol,
            "apikey": settings.TWELVE_DATA_API_KEY
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await provider_get(client, "twelvedata", "quote", params)
                data = response.json()
                print(f"[TwelveData] Quote for {symbol}: {data}")
                
                # Handling 429 and other API-level errors even if HTTP status is 200
                if data.get("status") == "error" or data.get("code") == 429:
                    print(f"[TwelveData] Rate limit or error for {symbol}: {data.get('message')}")
                    return None
                
                raw_price = data.get("price") or data.get("close")
                if raw_price is not None:
                    return {
                        "price": float(raw_price),
                        "change": float(data.get("change") or 0.0),
                        "changePercentage": float(data.get("percent_change") or 0.0),
                        "previousClose": float(data.get("previous_close") or 0.0),
                        "symbol": symbol,
                        "source": "TwelveData"
                    }
                return None
        except ApiServerError:
            raise
        except Exception as exc:
            print(f"TwelveData Error for {symbol}: {type(exc).__name__}")
            return None

    @staticmethod
    async def get_crypto_price(symbol: str = "BTC/USD") -> Optional[Dict[str, Any]]:
        """Wrapper specifically for Crypto pairs."""
        return await TwelveDataService.get_price(symbol)

twelve_data_service = TwelveDataService()
