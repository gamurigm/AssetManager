from ..core.config import settings
import httpx
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

class PolygonService:
    BASE_URL = "https://api.polygon.io"

    @staticmethod
    async def get_previous_close(symbol: str) -> Optional[Dict[str, Any]]:
        """
        Get Previous Close (EOD) Data.
        Limit: 5 req/min. Good for market overview but not real-time.
        """
        # Endpoint: /v2/aggs/ticker/{stocksTicker}/prev
        url = f"{PolygonService.BASE_URL}/v2/aggs/ticker/{symbol}/prev"
        params = {"apiKey": settings.POLYGON_API_KEY}
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params)
                # Polygon returns 429 often if hammered
                if response.status_code == 429:
                    print("Polygon Rate Limit")
                    return None
                    
                data = response.json()
                if data.get("status") == "OK" and data.get("resultsCount", 0) > 0:
                    res = data["results"][0]
                    return {
                        "date": datetime.fromtimestamp(res["t"]/1000).strftime('%Y-%m-%d'),
                        "close": res["c"],
                        "high": res["h"],
                        "low": res["l"],
                        "volume": res["v"],
                        "source": "Polygon"
                    }
                return None
        except Exception as e:
            print(f"Polygon Error: {e}")
            return None

polygon_service = PolygonService()
