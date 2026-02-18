"""
TwelveData Provider — Implements IMarketDataProvider.
"""

import httpx
from typing import Optional, List
from ...domain.interfaces.market_provider import IMarketDataProvider
from ...domain.entities.market import Quote, Candle
from ...core.config import settings


class TwelveDataProvider(IMarketDataProvider):
    BASE_URL = "https://api.twelvedata.com"

    @property
    def name(self) -> str:
        return "twelvedata"

    def normalize_symbol(self, symbol: str) -> str:
        return symbol  # TwelveData uses BTC/USD natively

    async def get_quote(self, symbol: str) -> Optional[Quote]:
        try:
            td_sym = self.normalize_symbol(symbol)
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{self.BASE_URL}/quote",
                    params={"symbol": td_sym, "apikey": settings.TWELVE_DATA_API_KEY},
                )
                data = resp.json()

            if data.get("status") == "error" or data.get("code") == 429:
                return None

            if "price" not in data:
                return None

            return Quote(
                symbol=symbol,
                price=float(data["price"]),
                change=float(data.get("change", 0)),
                change_percent=float(data.get("percent_change", 0)),
                source="TwelveData",
            )
        except Exception as e:
            print(f"[TwelveDataProvider] Error for {symbol}: {e}")
            return None

    async def get_historical(
        self, symbol: str, limit: int = 300, start_date: Optional[str] = None
    ) -> Optional[List[Candle]]:
        """TwelveData historical — not implemented for free tier, returns None."""
        return None
