from ..core.config import settings
import httpx
from typing import List, Dict, Any

class FMPService:
    BASE_URL = "https://financialmodelingprep.com/api/v3"

    @staticmethod
    async def get_quote(symbol: str) -> Dict[str, Any]:
        """Get real-time quote for a symbol."""
        url = f"{FMPService.BASE_URL}/quote/{symbol}"
        params = {"apikey": settings.FMP_API_KEY}
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                if data:
                    return data[0]
                return {}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def get_profile(symbol: str) -> Dict[str, Any]:
        """Get company profile."""
        url = f"{FMPService.BASE_URL}/profile/{symbol}"
        params = {"apikey": settings.FMP_API_KEY}
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                if data:
                    return data[0]
                return {}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def search_ticker(query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for tickers."""
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
