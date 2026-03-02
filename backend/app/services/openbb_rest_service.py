import httpx
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class OpenBBRestService:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url

    async def fetch(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generic HTTP GET request to the OpenBB FastAPI instance.
        Endpoint example: '/api/v1/equity/price/quote'
        """
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
            
        url = f"{self.base_url}{endpoint}"
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(url, params=params)
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as exc:
            logger.error(f"HTTP error {exc.response.status_code} while requesting {url}.")
            return {"error": f"HTTP {exc.response.status_code}", "detail": exc.response.text}
        except httpx.RequestError as exc:
            logger.error(f"An error occurred while requesting {exc.request.url!r}. OpenBB server might be offline.")
            return {"error": "Connection error", "detail": "Verify that uvicorn is running on port 8000"}
        except Exception as e:
            logger.error(f"Unexpected error in OpenBB Fetch: {e}")
            return {"error": "Unexpected error", "detail": str(e)}

    async def post(self, endpoint: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generic HTTP POST request to the OpenBB FastAPI instance.
        """
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
            
        url = f"{self.base_url}{endpoint}"
        
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(url, json=payload)
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as exc:
            return {"error": f"HTTP {exc.response.status_code}", "detail": exc.response.text}
        except Exception as e:
            return {"error": "Connection error", "detail": str(e)}


openbb_rest = OpenBBRestService()
