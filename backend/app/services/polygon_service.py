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

    @staticmethod
    async def get_intraday(
        symbol: str, 
        interval: str, 
        start: str, 
        end: str
    ) -> Dict[str, Any]:
        """
        Fetch intraday candles from Polygon, automatically paginating large ranges.
        Respects the 5 requests/minute free tier limit using asyncio.sleep.
        """
        multiplier = "1" if interval == "1m" else "5"
        timespan = "minute"
        
        url = f"{PolygonService.BASE_URL}/v2/aggs/ticker/{symbol}/range/{multiplier}/{timespan}/{start}/{end}"
        params = {
            "adjusted": "true",
            "sort": "asc",
            "limit": "50000",
            "apiKey": settings.POLYGON_API_KEY
        }
        
        all_results = []
        current_url = url
        current_params = params
        
        import asyncio
        import pytz
        from datetime import timezone
        ny_tz = pytz.timezone('America/New_York')

        try:
            async with httpx.AsyncClient() as client:
                while current_url:
                    response = await client.get(current_url, params=current_params)
                    
                    if response.status_code == 429:
                        print("Polygon Rate Limit Hit, waiting 15s...")
                        await asyncio.sleep(15)
                        continue # Retry
                    if response.status_code == 403:
                        return {"error": "Polygon Auth/Plan Error (403)"}
                    if response.status_code != 200:
                        return {"error": f"Polygon Error: {response.status_code} - {response.text}"}
                        
                    data = response.json()
                    results = data.get("results", [])
                    all_results.extend(results)
                    
                    next_url = data.get("next_url")
                    if next_url:
                        # Prepare for next page
                        current_url = f"{next_url}&apiKey={settings.POLYGON_API_KEY}"
                        current_params = None  # URL already has all necessary baked params
                        print(f"Polygon Paginating: {len(all_results)} candles fetched. Waiting 13s for rate limits...")
                        # 5 req / minute = 1 req every 12 seconds. Sleep 13 to be perfectly safe.
                        await asyncio.sleep(13)
                    else:
                        break # Done
                
                if not all_results:
                    return {"error": f"No intraday data found for {symbol} on {start}-{end}"}
                
                candles = []
                for row in all_results:
                    ts_utc = datetime.fromtimestamp(row["t"] / 1000.0, tz=timezone.utc)
                    ts_ny = ts_utc.astimezone(ny_tz).replace(tzinfo=None)
                    
                    candles.append({
                        "timestamp": ts_ny.strftime("%Y-%m-%dT%H:%M:%S"),
                        "open":   float(row["o"]),
                        "high":   float(row["h"]),
                        "low":    float(row["l"]),
                        "close":  float(row["c"]),
                        "volume": int(row["v"]),
                    })
                    
                return {
                    "symbol": symbol,
                    "interval": interval,
                    "candles": candles,
                    "source": "Polygon.io (Intraday Paged Bulk)"
                }
        except Exception as e:
            return {"error": str(e)}

polygon_service = PolygonService()
