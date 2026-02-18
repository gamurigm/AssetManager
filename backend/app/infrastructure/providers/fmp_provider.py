"""
FMP (Financial Modeling Prep) Provider — Implements IMarketDataProvider.
High quality data, strict free-tier limits.
"""

import httpx
from typing import Optional, List
from ...domain.interfaces.market_provider import IMarketDataProvider
from ...domain.entities.market import Quote, Candle
from ...core.config import settings


class FMPProvider(IMarketDataProvider):
    BASE_URL = "https://financialmodelingprep.com/stable"
    V3_URL = "https://financialmodelingprep.com/api/v3"

    @property
    def name(self) -> str:
        return "fmp"

    def normalize_symbol(self, symbol: str) -> str:
        return symbol.replace("/", "").replace("=", "")

    async def get_quote(self, symbol: str) -> Optional[Quote]:
        try:
            fmp_sym = self.normalize_symbol(symbol)
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{self.BASE_URL}/quote",
                    params={"symbol": fmp_sym, "apikey": settings.FMP_API_KEY},
                )
                resp.raise_for_status()
                data = resp.json()

            if not data or not isinstance(data, list) or not data[0].get("price"):
                return None

            q = data[0]
            price = float(q["price"])
            prev = q.get("previousClose")
            if prev:
                prev = float(prev)
                change = price - prev
                pct = (change / prev) * 100 if prev != 0 else 0
            else:
                change = float(q.get("change", 0))
                pct = float(q.get("changesPercentage", 0))

            return Quote(
                symbol=symbol, price=price, change=change,
                change_percent=pct, volume=q.get("volume"),
                source="FMP (Real-time)",
            )
        except Exception as e:
            print(f"[FMPProvider] Error for {symbol}: {e}")
            return None

    async def get_historical(
        self, symbol: str, limit: int = 300, start_date: Optional[str] = None
    ) -> Optional[List[Candle]]:
        try:
            fmp_sym = self.normalize_symbol(symbol)
            params = {"apikey": settings.FMP_API_KEY}
            if start_date:
                params["from"] = start_date
            else:
                params["timeseries"] = limit

            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{self.V3_URL}/historical-price-full/{fmp_sym}",
                    params=params,
                )
                resp.raise_for_status()
                data = resp.json()

            if not data or "historical" not in data:
                return None

            return [
                Candle(
                    date=bar["date"], open=bar["open"], high=bar["high"],
                    low=bar["low"], close=bar["close"], volume=bar.get("volume", 0),
                )
                for bar in data["historical"]
            ]
        except Exception as e:
            print(f"[FMPProvider] Historical error for {symbol}: {e}")
            return None

    # --- FMP-specific methods (not part of interface — Open/Closed Principle) ---

    async def get_profile(self, symbol: str) -> Optional[dict]:
        """FMP-specific: company profile."""
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{self.BASE_URL}/profile",
                    params={"symbol": symbol, "apikey": settings.FMP_API_KEY},
                )
                resp.raise_for_status()
                data = resp.json()
            return data[0] if data and isinstance(data, list) else None
        except Exception:
            return None

    async def search_ticker(self, query: str, limit: int = 10) -> list:
        """FMP-specific: ticker search."""
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{self.BASE_URL}/search",
                    params={"query": query, "limit": limit, "apikey": settings.FMP_API_KEY},
                )
                resp.raise_for_status()
                return resp.json()
        except Exception:
            return []
