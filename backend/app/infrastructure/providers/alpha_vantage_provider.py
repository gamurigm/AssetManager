"""
Alpha Vantage Provider — Technical Indicators only.
Does NOT implement IMarketDataProvider (different responsibility — SRP).
"""

import httpx
from typing import Optional, Dict, Any
from ...core.config import settings


class AlphaVantageProvider:
    """Specialized provider for technical indicators (RSI, MACD, SMA)."""
    BASE_URL = "https://www.alphavantage.co/query"

    @property
    def name(self) -> str:
        return "alphavantage"

    async def get_indicator(
        self, symbol: str, function: str = "RSI", interval: str = "daily"
    ) -> Optional[Dict[str, Any]]:
        params = {
            "function": function,
            "symbol": symbol,
            "interval": interval,
            "time_period": "14",
            "series_type": "close",
            "apikey": settings.ALPHA_VANTAGE_API_KEY,
        }
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(self.BASE_URL, params=params)
                resp.raise_for_status()
                data = resp.json()

            if "Note" in data:
                return None

            meta = f"Technical Analysis: {function}"
            if meta in data:
                series = data[meta]
                last_date = sorted(series.keys())[-1]
                return {
                    "indicator": function,
                    "date": last_date,
                    "value": series[last_date],
                    "source": "AlphaVantage",
                }
            return None
        except Exception as e:
            print(f"[AlphaVantageProvider] Error: {e}")
            return None
