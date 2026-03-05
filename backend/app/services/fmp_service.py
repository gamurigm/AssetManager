from ..core.config import settings
import httpx
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

def _fmp_error(data: any) -> bool:
    """Return True if the payload is an FMP error (not real data)."""
    if not data:
        return True
    if isinstance(data, dict):
        return bool(data.get("Error Message") or data.get("message") or data.get("error"))
    if isinstance(data, list):
        if not data:
            return True
        return _fmp_error(data[0])
    return False

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
                if response.status_code in (402, 403, 429):
                    logger.warning(f"[FMP] {response.status_code} on quote/{symbol} — premium/rate limit, skipping.")
                    return {}
                response.raise_for_status()
                data = response.json()
                if _fmp_error(data):
                    logger.warning(f"[FMP] Error payload on quote/{symbol}: {str(data)[:120]}")
                    return {}
                if data and isinstance(data, list):
                    return data[0]
                return {}
        except httpx.HTTPStatusError as e:
            logger.warning(f"[FMP] HTTP error on quote/{symbol}: {e.response.status_code}")
            return {}
        except Exception as e:
            logger.debug(f"[FMP] quote/{symbol}: {e}")
            return {}

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
                if response.status_code in (402, 403, 429):
                    logger.warning(f"[FMP] {response.status_code} on profile/{symbol} — premium/rate limit, skipping.")
                    return {}
                response.raise_for_status()
                data = response.json()
                if _fmp_error(data):
                    logger.warning(f"[FMP] Error payload on profile/{symbol}: {str(data)[:120]}")
                    return {}
                if data and isinstance(data, list):
                    return data[0]
                return {}
        except httpx.HTTPStatusError as e:
            logger.warning(f"[FMP] HTTP error on profile/{symbol}: {e.response.status_code}")
            return {}
        except Exception as e:
            logger.debug(f"[FMP] profile/{symbol}: {e}")
            return {}

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
                if response.status_code in (402, 403, 429):
                    logger.warning(f"[FMP] {response.status_code} on historical/{symbol} — premium/rate limit, skipping.")
                    return {}
                response.raise_for_status()
                data = response.json()
                if _fmp_error(data):
                    logger.warning(f"[FMP] Error payload on historical/{symbol}: {str(data)[:120]}")
                    return {}
                return data
        except httpx.HTTPStatusError as e:
            logger.warning(f"[FMP] HTTP error on historical/{symbol}: {e.response.status_code}")
            return {}
        except Exception as e:
            logger.debug(f"[FMP] historical/{symbol}: {e}")
            return {}

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
                if response.status_code in (402, 403, 429):
                    return []
                response.raise_for_status()
                data = response.json()
                if _fmp_error(data):
                    return []
                return data if isinstance(data, list) else []
        except Exception as e:
            logger.debug(f"[FMP] search/{query}: {e}")
            return []

    @staticmethod
    async def _fetch_stable(endpoint: str, symbol: str, period: str = "annual", limit: int = 5) -> List[Dict[str, Any]]:
        """Generic fetcher for FMP stable-API list endpoints."""
        url = f"{FMPService.BASE_URL}/{endpoint}"
        params = {"symbol": symbol, "period": period, "limit": limit, "apikey": settings.FMP_API_KEY}
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params)
                if response.status_code in (402, 403, 429):
                    logger.warning(f"[FMP] {response.status_code} on {endpoint}/{symbol}")
                    return []
                response.raise_for_status()
                data = response.json()
                if _fmp_error(data):
                    return []
                return data if isinstance(data, list) else []
        except Exception as e:
            logger.debug(f"[FMP] {endpoint}/{symbol}: {e}")
            return []

    @staticmethod
    async def get_income_statement(symbol: str, period: str = "annual", limit: int = 5) -> List[Dict[str, Any]]:
        """Get income statements (annual or quarter)."""
        return await FMPService._fetch_stable("income-statement", symbol, period, limit)

    @staticmethod
    async def get_balance_sheet(symbol: str, period: str = "annual", limit: int = 5) -> List[Dict[str, Any]]:
        """Get balance sheet statements."""
        return await FMPService._fetch_stable("balance-sheet-statement", symbol, period, limit)

    @staticmethod
    async def get_key_metrics(symbol: str, period: str = "annual", limit: int = 5) -> List[Dict[str, Any]]:
        """Get key metrics (PE, EV/EBITDA, ROE, etc.)."""
        return await FMPService._fetch_stable("key-metrics", symbol, period, limit)

    @staticmethod
    async def get_financial_ratios(symbol: str, period: str = "annual", limit: int = 5) -> List[Dict[str, Any]]:
        """Get financial ratios (profitability, liquidity, solvency)."""
        return await FMPService._fetch_stable("ratios", symbol, period, limit)

fmp_service = FMPService()
