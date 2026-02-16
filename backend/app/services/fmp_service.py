from ..core.config import settings
import httpx
from typing import List, Dict, Any

class FMPService:
    BASE_URL = "https://financialmodelingprep.com/stable"

    @staticmethod
    async def get_quote(symbol: str) -> Dict[str, Any]:
        """Get real-time quote for a symbol using stable API."""
        url = f"{FMPService.BASE_URL}/quote"
        params = {
            "symbol": symbol,
            "apikey": settings.FMP_API_KEY
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                if data and isinstance(data, list):
                    return data[0]
                return {}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def get_profile(symbol: str) -> Dict[str, Any]:
        """Get company profile using stable API."""
        url = f"{FMPService.BASE_URL}/profile"
        params = {
            "symbol": symbol,
            "apikey": settings.FMP_API_KEY
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                if data and isinstance(data, list):
                    return data[0]
                return {}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def get_historical(symbol: str, limit: int = 30) -> Dict[str, Any]:
        """Get historical price data (daily) using v3 API (Stable for historical)."""
        url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}"
        params = {
            "apikey": settings.FMP_API_KEY,
            "timeseries": limit
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params)
                response.raise_for_status()
                return response.json()
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def search_ticker(query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for tickers using stable API."""
        url = f"{FMPService.BASE_URL}/search"
        params = {
            "query": query,
            "limit": limit,
            "apikey": settings.FMP_API_KEY
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params)
                response.raise_for_status()
                return response.json()
        except Exception as e:
            return []

fmp_service = FMPService()
