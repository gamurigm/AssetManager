"""
Bybit Provider — Implements IMarketDataProvider
Uses Bybit V5 REST API (public endpoints, no auth required for market data).
Doc: https://bybit-exchange.github.io/docs/v5/intro
"""

import httpx
from datetime import datetime
from typing import Optional, List

from ...domain.interfaces.market_provider import IMarketDataProvider
from ...domain.entities.market import Quote, Candle


class BybitProvider(IMarketDataProvider):
    """
    Market Data Provider for Bybit Exchange (Crypto).
    Uses V5 public endpoints — no authentication needed for market data.
    """

    BASE_URL = "https://api.bybit.com"

    @property
    def name(self) -> str:
        return "bybit"

    def normalize_symbol(self, symbol: str) -> str:
        """
        Convert universal symbol format to Bybit format.
        BTC/USD  → BTCUSDT
        ETH/USD  → ETHUSDT
        BTCUSDT  → BTCUSDT  (passthrough)
        """
        sym = symbol.upper().replace("/", "").replace("-", "").replace("=", "")
        # If it ends with USD but NOT USDT/USDC, append T
        if sym.endswith("USD") and not sym.endswith("USDT") and not sym.endswith("USDC"):
            sym = sym + "T"
        return sym

    async def get_quote(self, symbol: str) -> Optional[Quote]:
        """Fetch real-time ticker from Bybit V5 API."""
        normalized = self.normalize_symbol(symbol)

        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{self.BASE_URL}/v5/market/tickers",
                    params={"category": "spot", "symbol": normalized},
                )
                resp.raise_for_status()
                data = resp.json()

            if data.get("retCode") != 0:
                print(f"[BybitProvider] API error: {data.get('retMsg')}")
                return None

            items = data.get("result", {}).get("list", [])
            if not items:
                return None

            ticker = items[0]
            last_price = float(ticker["lastPrice"])
            prev_price_24h = float(ticker.get("prevPrice24h", last_price))

            if prev_price_24h != 0:
                change = last_price - prev_price_24h
                change_pct = (change / prev_price_24h) * 100
            else:
                change = 0.0
                change_pct = 0.0

            volume = None
            vol_str = ticker.get("volume24h")
            if vol_str:
                volume = int(float(vol_str))

            return Quote(
                symbol=symbol,
                price=last_price,
                change=round(change, 4),
                change_percent=round(change_pct, 4),
                volume=volume,
                source="Bybit (Spot)",
            )
        except Exception as e:
            print(f"[BybitProvider] Quote error for {symbol}: {e}")
            return None

    async def get_historical(
        self, symbol: str, limit: int = 300, start_date: Optional[str] = None
    ) -> Optional[List[Candle]]:
        """Fetch historical daily klines from Bybit V5 API."""
        normalized = self.normalize_symbol(symbol)

        try:
            params = {
                "category": "spot",
                "symbol": normalized,
                "interval": "D",
                "limit": min(limit, 1000),  # Bybit max 1000 per request
            }

            if start_date:
                try:
                    dt = datetime.strptime(start_date, "%Y-%m-%d")
                    params["start"] = int(dt.timestamp() * 1000)
                except ValueError:
                    pass

            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{self.BASE_URL}/v5/market/kline",
                    params=params,
                )
                resp.raise_for_status()
                data = resp.json()

            if data.get("retCode") != 0:
                print(f"[BybitProvider] Kline API error: {data.get('retMsg')}")
                return None

            items = data.get("result", {}).get("list", [])
            if not items:
                return None

            candles = []
            for bar in items:
                # Bybit kline format: [startTime, open, high, low, close, volume, turnover]
                ts_ms = int(bar[0])
                date_str = datetime.fromtimestamp(ts_ms / 1000).strftime("%Y-%m-%d")
                candles.append(
                    Candle(
                        date=date_str,
                        open=float(bar[1]),
                        high=float(bar[2]),
                        low=float(bar[3]),
                        close=float(bar[4]),
                        volume=int(float(bar[5])),
                    )
                )

            # Bybit returns reverse chronological, sort ascending
            candles.sort(key=lambda c: c.date)
            return candles

        except Exception as e:
            print(f"[BybitProvider] Historical error for {symbol}: {e}")
            return None
