"""
Bybit Service — Standalone service layer for Bybit-specific functionality.
Provides methods beyond the IMarketDataProvider interface:
  - Intraday klines with crypto-specific intervals
  - Orderbook data
  - Instrument listing
"""

import httpx
from typing import Dict, Any, Optional, List
from ..core.config import settings


class BybitService:
    """Direct Bybit V5 REST API client for crypto market data."""

    BASE_URL = "https://api.bybit.com"

    # Map our interval notation to Bybit's
    INTERVAL_MAP = {
        "1m": "1",   "3m": "3",   "5m": "5",
        "15m": "15", "30m": "30", "1h": "60",
        "2h": "120", "4h": "240", "6h": "360",
        "12h": "720", "D": "D",   "W": "W",  "M": "M",
        # Also accept Bybit-native intervals
        "1": "1", "3": "3", "5": "5", "15": "15",
        "30": "30", "60": "60", "120": "120", "240": "240",
    }

    @staticmethod
    def _normalize_symbol(symbol: str) -> str:
        """Convert universal symbol to Bybit format."""
        sym = symbol.upper().replace("/", "").replace("-", "").replace("=", "")
        if sym.endswith("USD") and not sym.endswith("USDT") and not sym.endswith("USDC"):
            sym = sym + "T"
        return sym

    @staticmethod
    async def get_quote(symbol: str) -> Optional[Dict[str, Any]]:
        """Get real-time ticker data for a symbol."""
        normalized = BybitService._normalize_symbol(symbol)

        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{BybitService.BASE_URL}/v5/market/tickers",
                    params={"category": "spot", "symbol": normalized},
                )
                resp.raise_for_status()
                data = resp.json()

            if data.get("retCode") != 0:
                return {"error": f"Bybit API: {data.get('retMsg')}"}

            items = data.get("result", {}).get("list", [])
            if not items:
                return {"error": f"No ticker data for {symbol}"}

            t = items[0]
            last = float(t["lastPrice"])
            prev = float(t.get("prevPrice24h", last))
            change = last - prev if prev != 0 else 0
            pct = (change / prev) * 100 if prev != 0 else 0

            return {
                "price": last,
                "change": round(change, 4),
                "changePercentage": round(pct, 4),
                "volume": int(float(t.get("volume24h", 0))),
                "high24h": float(t.get("highPrice24h", 0)),
                "low24h": float(t.get("lowPrice24h", 0)),
                "turnover24h": float(t.get("turnover24h", 0)),
                "bid1": float(t.get("bid1Price", 0)),
                "ask1": float(t.get("ask1Price", 0)),
                "source": "Bybit (Spot)",
            }
        except Exception as e:
            return {"error": f"Bybit quote error: {e}"}

    @staticmethod
    async def get_klines(
        symbol: str,
        interval: str = "D",
        limit: int = 200,
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Fetch klines/candles with flexible intervals.
        Args:
            symbol: Trading pair (e.g., BTCUSDT, BTC/USD)
            interval: 1m,3m,5m,15m,30m,1h,2h,4h,6h,12h,D,W,M
            limit: Number of candles (max 1000)
            start: Start time in ms (optional)
            end: End time in ms (optional)
        """
        normalized = BybitService._normalize_symbol(symbol)
        bybit_interval = BybitService.INTERVAL_MAP.get(interval, interval)

        params = {
            "category": "spot",
            "symbol": normalized,
            "interval": bybit_interval,
            "limit": min(limit, 1000),
        }
        if start:
            params["start"] = start
        if end:
            params["end"] = end

        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{BybitService.BASE_URL}/v5/market/kline",
                    params=params,
                )
                resp.raise_for_status()
                data = resp.json()

            if data.get("retCode") != 0:
                return {"error": f"Bybit kline API: {data.get('retMsg')}"}

            items = data.get("result", {}).get("list", [])
            if not items:
                return {"error": f"No kline data for {symbol}"}

            candles = []
            for bar in items:
                # [startTime, open, high, low, close, volume, turnover]
                candles.append({
                    "timestamp": int(bar[0]),
                    "open": float(bar[1]),
                    "high": float(bar[2]),
                    "low": float(bar[3]),
                    "close": float(bar[4]),
                    "volume": float(bar[5]),
                    "turnover": float(bar[6]) if len(bar) > 6 else 0,
                })

            # Sort chronologically (Bybit returns newest first)
            candles.sort(key=lambda c: c["timestamp"])

            return {
                "symbol": normalized,
                "interval": interval,
                "candles": candles,
                "source": "Bybit (Klines)",
            }
        except Exception as e:
            return {"error": f"Bybit klines error: {e}"}

    @staticmethod
    async def get_orderbook(symbol: str, depth: int = 25) -> Dict[str, Any]:
        """Get orderbook for a symbol."""
        normalized = BybitService._normalize_symbol(symbol)

        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{BybitService.BASE_URL}/v5/market/orderbook",
                    params={
                        "category": "spot",
                        "symbol": normalized,
                        "limit": min(depth, 200),
                    },
                )
                resp.raise_for_status()
                data = resp.json()

            if data.get("retCode") != 0:
                return {"error": f"Bybit orderbook API: {data.get('retMsg')}"}

            result = data.get("result", {})
            return {
                "symbol": normalized,
                "bids": [[float(p), float(q)] for p, q in result.get("b", [])],
                "asks": [[float(p), float(q)] for p, q in result.get("a", [])],
                "timestamp": result.get("ts"),
                "source": "Bybit (Orderbook)",
            }
        except Exception as e:
            return {"error": f"Bybit orderbook error: {e}"}

    @staticmethod
    async def get_instruments(category: str = "spot") -> Dict[str, Any]:
        """List available instruments on Bybit."""
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{BybitService.BASE_URL}/v5/market/instruments-info",
                    params={"category": category, "limit": 1000},
                )
                resp.raise_for_status()
                data = resp.json()

            if data.get("retCode") != 0:
                return {"error": f"Bybit instruments API: {data.get('retMsg')}"}

            items = data.get("result", {}).get("list", [])
            instruments = [
                {
                    "symbol": i["symbol"],
                    "baseCoin": i.get("baseCoin", ""),
                    "quoteCoin": i.get("quoteCoin", ""),
                    "status": i.get("status", ""),
                }
                for i in items
            ]

            return {
                "category": category,
                "count": len(instruments),
                "instruments": instruments,
            }
        except Exception as e:
            return {"error": f"Bybit instruments error: {e}"}

    @staticmethod
    async def get_funding_rate(symbol: str, limit: int = 50) -> Dict[str, Any]:
        """Get funding rate history for a perpetual contract."""
        normalized = BybitService._normalize_symbol(symbol)
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{BybitService.BASE_URL}/v5/market/funding/history",
                    params={"category": "linear", "symbol": normalized, "limit": min(limit, 200)},
                )
                resp.raise_for_status()
                data = resp.json()
            if data.get("retCode") != 0:
                return {"error": f"Bybit funding API: {data.get('retMsg')}"}
            items = data.get("result", {}).get("list", [])
            return {
                "symbol": normalized,
                "funding_rates": [
                    {"timestamp": int(i["fundingRateTimestamp"]), "rate": float(i["fundingRate"])}
                    for i in items
                ],
                "source": "Bybit (Funding Rate)",
            }
        except Exception as e:
            return {"error": f"Bybit funding rate error: {e}"}

    @staticmethod
    async def get_open_interest(symbol: str, interval: str = "1h", limit: int = 50) -> Dict[str, Any]:
        """Get open interest history."""
        normalized = BybitService._normalize_symbol(symbol)
        interval_map = {"5m": "5min", "15m": "15min", "30m": "30min", "1h": "1h", "4h": "4h", "1d": "1d"}
        bybit_interval = interval_map.get(interval, interval)
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{BybitService.BASE_URL}/v5/market/open-interest",
                    params={"category": "linear", "symbol": normalized, "intervalTime": bybit_interval, "limit": min(limit, 200)},
                )
                resp.raise_for_status()
                data = resp.json()
            if data.get("retCode") != 0:
                return {"error": f"Bybit OI API: {data.get('retMsg')}"}
            items = data.get("result", {}).get("list", [])
            return {
                "symbol": normalized,
                "open_interest": [
                    {"timestamp": int(i["timestamp"]), "value": float(i["openInterest"])}
                    for i in items
                ],
                "source": "Bybit (Open Interest)",
            }
        except Exception as e:
            return {"error": f"Bybit open interest error: {e}"}

    @staticmethod
    async def get_long_short_ratio(symbol: str, period: str = "1h", limit: int = 50) -> Dict[str, Any]:
        """Get long/short ratio history."""
        normalized = BybitService._normalize_symbol(symbol)
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{BybitService.BASE_URL}/v5/market/account-ratio",
                    params={"category": "linear", "symbol": normalized, "period": period, "limit": min(limit, 500)},
                )
                resp.raise_for_status()
                data = resp.json()
            if data.get("retCode") != 0:
                return {"error": f"Bybit ratio API: {data.get('retMsg')}"}
            items = data.get("result", {}).get("list", [])
            return {
                "symbol": normalized,
                "ratios": [
                    {"timestamp": int(i["timestamp"]), "buyRatio": float(i["buyRatio"]), "sellRatio": float(i["sellRatio"])}
                    for i in items
                ],
                "source": "Bybit (Long/Short Ratio)",
            }
        except Exception as e:
            return {"error": f"Bybit long/short ratio error: {e}"}


bybit_service = BybitService()
