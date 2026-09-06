"""
FMP (Financial Modeling Prep) Provider — Implements IMarketDataProvider.
High quality data, strict free-tier limits.
"""

import httpx
from app.infrastructure.http.api_server_client import ApiServerError, provider_get
from typing import Optional, List
from ...domain.interfaces.market_provider import IMarketDataProvider
from ...domain.entities.market import Quote, Candle
from ...core.config import settings


class FMPProvider(IMarketDataProvider):
    BASE_URL = settings.FMP_BASE_URL
    _shared_client: httpx.AsyncClient | None = None

    @classmethod
    def _client(cls) -> httpx.AsyncClient:
        """Reusable connection-pooled HTTP client (no TLS handshake per request)."""
        if cls._shared_client is None or cls._shared_client.is_closed:
            cls._shared_client = httpx.AsyncClient(
                timeout=10.0,
                limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
            )
        return cls._shared_client

    @property
    def name(self) -> str:
        return "fmp"

    def normalize_symbol(self, symbol: str) -> str:
        return symbol.replace("/", "").replace("=", "")

    async def get_quote(self, symbol: str) -> Optional[Quote]:
        try:
            fmp_sym = self.normalize_symbol(symbol)
            client = self._client()
            resp = await provider_get(
                client, "fmp", "quote",
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
        except httpx.HTTPStatusError as exc:
            print(f"[FMPProvider] HTTP {exc.response.status_code} for quote/{symbol}")
            return None
        except ApiServerError:
            raise
        except Exception as exc:
            print(f"[FMPProvider] Quote error for {symbol}: {type(exc).__name__}")
            return None

    async def get_historical(
        self, symbol: str, limit: int = 300, start_date: Optional[str] = None
    ) -> Optional[List[Candle]]:
        try:
            fmp_sym = self.normalize_symbol(symbol)
            params = {
                "symbol": fmp_sym,
                "apikey": settings.FMP_API_KEY,
            }
            if start_date:
                params["from"] = start_date

            client = self._client()
            resp = await provider_get(
                client, "fmp", "historical-price-eod/full",
                params=params,
            )
            resp.raise_for_status()
            data = resp.json()

            rows = data.get("historical", []) if isinstance(data, dict) else data
            if not isinstance(rows, list) or not rows:
                return None

            candles = [
                Candle(
                    date=bar["date"], open=bar["open"], high=bar["high"],
                    low=bar["low"], close=bar["close"],
                    volume=int(float(bar.get("volume", 0) or 0)),
                )
                for bar in rows
            ]
            candles.sort(key=lambda candle: candle.date)
            return candles[-limit:]
        except httpx.HTTPStatusError as exc:
            print(
                f"[FMPProvider] HTTP {exc.response.status_code} "
                f"for historical/{symbol}"
            )
            return None
        except ApiServerError:
            raise
        except Exception as exc:
            print(f"[FMPProvider] Historical error for {symbol}: {type(exc).__name__}")
            return None

    # --- FMP-specific methods (not part of interface — Open/Closed Principle) ---

    async def get_profile(self, symbol: str) -> Optional[dict]:
        """FMP-specific: company profile."""
        try:
            client = self._client()
            resp = await provider_get(
                client, "fmp", "profile",
                params={"symbol": symbol, "apikey": settings.FMP_API_KEY},
            )
            resp.raise_for_status()
            data = resp.json()
            return data[0] if data and isinstance(data, list) else None
        except ApiServerError:
            raise
        except Exception:
            return None

    async def search_ticker(self, query: str, limit: int = 10) -> list:
        """FMP-specific: ticker search."""
        try:
            client = self._client()
            resp = await provider_get(
                client, "fmp", "search-symbol",
                params={"query": query, "limit": limit, "apikey": settings.FMP_API_KEY},
            )
            resp.raise_for_status()
            return resp.json()
        except ApiServerError:
            raise
        except Exception as exc:
            print(f"[FMPProvider] search_ticker error for '{query}': {type(exc).__name__}")
            return []

    async def get_stock_list(self) -> list:
        """Fetch ALL stocks from FMP list."""
        try:
            client = self._client()
            resp = await provider_get(
                client, "fmp", "stock-list",
                params={"apikey": settings.FMP_API_KEY},
            )
            resp.raise_for_status()
            return resp.json()
        except ApiServerError:
            raise
        except Exception as exc:
            print(f"[FMPProvider] get_stock_list error: {type(exc).__name__}")
            return []
