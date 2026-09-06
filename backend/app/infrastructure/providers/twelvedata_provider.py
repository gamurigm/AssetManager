"""Twelve Data market-data provider."""

from datetime import datetime
from typing import List, Optional

import httpx
from app.infrastructure.http.api_server_client import ApiServerError, provider_get

from ...core.config import settings
from ...domain.entities.market import Candle, Quote
from ...domain.interfaces.market_provider import IMarketDataProvider


class TwelveDataProvider(IMarketDataProvider):
    BASE_URL = settings.TWELVE_DATA_BASE_URL

    @property
    def name(self) -> str:
        return "twelvedata"

    def normalize_symbol(self, symbol: str) -> str:
        return symbol  # Twelve Data uses BTC/USD natively.

    async def search_ticker(self, query: str, limit: int = 10) -> list[dict]:
        """Search Twelve Data's global instrument catalog."""
        try:
            async with httpx.AsyncClient(timeout=8) as client:
                response = await provider_get(
                    client, "twelvedata", "symbol_search",
                    params={
                        "symbol": query,
                        "outputsize": min(max(1, limit), 120),
                        "show_plan": "true",
                        "apikey": settings.TWELVE_DATA_API_KEY,
                    },
                )
                response.raise_for_status()
                data = response.json()
            if data.get("status") == "error":
                return []
            results = data.get("data", [])
            return results if isinstance(results, list) else []
        except ApiServerError:
            raise
        except Exception as exc:
            print(
                f"[TwelveDataProvider] Search error for '{query}': {type(exc).__name__}"
            )
            return []

    async def get_quote(self, symbol: str) -> Optional[Quote]:
        try:
            async with httpx.AsyncClient(timeout=20) as client:
                response = await provider_get(
                    client, "twelvedata", "quote",
                    params={
                        "symbol": self.normalize_symbol(symbol),
                        "apikey": settings.TWELVE_DATA_API_KEY,
                    },
                )
                data = response.json()

            if data.get("status") == "error" or data.get("code") == 429:
                return None

            raw_price = data.get("price") or data.get("close")
            if raw_price is None:
                return None

            return Quote(
                symbol=symbol,
                price=float(raw_price),
                change=float(data.get("change", 0) or 0),
                change_percent=float(data.get("percent_change", 0) or 0),
                volume=int(float(data["volume"])) if data.get("volume") else None,
                source="TwelveData",
            )
        except ApiServerError:
            raise
        except Exception as exc:
            print(f"[TwelveDataProvider] Error for {symbol}: {type(exc).__name__}")
            return None

    async def get_historical(
        self,
        symbol: str,
        limit: int = 300,
        start_date: Optional[str] = None,
    ) -> Optional[List[Candle]]:
        params = {
            "symbol": self.normalize_symbol(symbol),
            "interval": "1day",
            "outputsize": min(max(1, limit), 5_000),
            "apikey": settings.TWELVE_DATA_API_KEY,
        }
        if start_date:
            params["start_date"] = start_date

        try:
            async with httpx.AsyncClient(timeout=20) as client:
                response = await provider_get(
                    client, "twelvedata", "time_series",
                    params=params,
                )
                data = response.json()

            if data.get("status") == "error" or data.get("code") == 429:
                return None
            rows = data.get("values", [])
            if not rows:
                return None

            candles = [
                Candle(
                    date=datetime.fromisoformat(row["datetime"]).strftime("%Y-%m-%d"),
                    open=float(row["open"]),
                    high=float(row["high"]),
                    low=float(row["low"]),
                    close=float(row["close"]),
                    volume=int(float(row.get("volume", 0) or 0)),
                )
                for row in rows
            ]
            candles.sort(key=lambda candle: candle.date)
            return candles[-limit:]
        except ApiServerError:
            raise
        except Exception as exc:
            print(
                f"[TwelveDataProvider] Historical error for {symbol}: "
                f"{type(exc).__name__}"
            )
            return None
