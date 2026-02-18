"""
Polygon Provider — Implements IMarketDataProvider.
EOD (End of Day) data, good for fallback.
"""

import httpx
from datetime import datetime
from typing import Optional, List
from ...domain.interfaces.market_provider import IMarketDataProvider
from ...domain.entities.market import Quote, Candle
from ...core.config import settings


class PolygonProvider(IMarketDataProvider):
    BASE_URL = "https://api.polygon.io"

    @property
    def name(self) -> str:
        return "polygon"

    def normalize_symbol(self, symbol: str) -> str:
        return symbol.replace("/", "").replace("=", "")

    async def get_quote(self, symbol: str) -> Optional[Quote]:
        """Polygon only provides previous close, not real-time on free tier."""
        try:
            poly_sym = self.normalize_symbol(symbol)
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{self.BASE_URL}/v2/aggs/ticker/{poly_sym}/prev",
                    params={"apiKey": settings.POLYGON_API_KEY},
                )
                if resp.status_code == 429:
                    return None
                data = resp.json()

            if data.get("status") != "OK" or data.get("resultsCount", 0) == 0:
                return None

            res = data["results"][0]
            return Quote(
                symbol=symbol,
                price=res["c"],
                change=0.0,
                change_percent=0.0,
                volume=int(res.get("v", 0)),
                source="Polygon (EOD)",
            )
        except Exception as e:
            print(f"[PolygonProvider] Error for {symbol}: {e}")
            return None

    async def get_historical(
        self, symbol: str, limit: int = 300, start_date: Optional[str] = None
    ) -> Optional[List[Candle]]:
        """Polygon historical — not implemented for free tier."""
        return None
