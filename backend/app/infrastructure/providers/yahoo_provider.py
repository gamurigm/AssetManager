"""
Yahoo Finance Provider — Implements IMarketDataProvider.
Uses yfinance library. Most stable free source.

PERFORMANCE: All yfinance calls run via asyncio.to_thread()
to avoid blocking the async event loop.
"""

import asyncio
import time
import yfinance as yf
from typing import Optional, List
from ...domain.interfaces.market_provider import IMarketDataProvider
from ...domain.entities.market import Quote, Candle


class YahooProvider(IMarketDataProvider):

    def __init__(self):
        self._search_cache: dict[str, tuple[float, list]] = {}

    @property
    def name(self) -> str:
        return "yahoo"

    def normalize_symbol(self, symbol: str) -> str:
        # Common Index mappings
        index_map = {
            "SPX": "^GSPC",
            "SP500": "^GSPC",
            "S&P 500": "^GSPC",
            "NASDAQ": "^IXIC",
            "NDX": "^NDX",
            "DOW": "^DJI",
            "DJIA": "^DJI",
            "VIX": "^VIX"
        }
        
        upper_sym = symbol.upper()
        if upper_sym in index_map:
            return index_map[upper_sym]
            
        if symbol == "BTC/USD":
            return "BTC-USD"
        if symbol == "ETH/USD":
            return "ETH-USD"
            
        fiat_currencies = ["EUR", "USD", "GBP", "JPY", "AUD", "CAD", "CHF", "NZD"]
        
        if "/" in symbol:
            if any(c in symbol for c in fiat_currencies):
                return symbol.replace("/", "") + "=X"
            return symbol.replace("/", "-")
            
        # Handle 6-letter fiat pairs sent without slashes (e.g. "EURGBP")
        if len(symbol) == 6 and symbol[:3] in fiat_currencies and symbol[3:] in fiat_currencies:
            return symbol + "=X"
            
        return symbol

    # ─── Blocking helpers (run in background thread) ──────────────────

    def _sync_get_quote(self, yf_sym: str):
        """Synchronous quote fetch — called via asyncio.to_thread."""
        ticker = yf.Ticker(yf_sym)
        return ticker.history(period="5d")

    def _sync_get_historical(self, yf_sym: str, start_date: Optional[str] = None):
        """Synchronous historical fetch — called via asyncio.to_thread."""
        ticker = yf.Ticker(yf_sym)
        if start_date:
            return ticker.history(start=start_date, interval="1d")
        else:
            try:
                return ticker.history(period="max", interval="1d")
            except Exception:
                try:
                    return ticker.history(period="5y", interval="1d")
                except Exception:
                    return ticker.history(period="1y", interval="1d")

    # ─── Async interface (non-blocking) ───────────────────────────────

    async def get_quote(self, symbol: str) -> Optional[Quote]:
        try:
            yf_sym = self.normalize_symbol(symbol)
            hist = await asyncio.to_thread(self._sync_get_quote, yf_sym)

            if hist is None or hist.empty:
                return None

            latest = hist.iloc[-1]
            price = float(latest["Close"])

            if len(hist) > 1:
                prev_close = float(hist.iloc[-2]["Close"])
                change = price - prev_close
                pct_change = (change / prev_close) * 100
            else:
                change = 0.0
                pct_change = 0.0

            return Quote(
                symbol=symbol,
                price=price,
                change=change,
                change_percent=pct_change,
                volume=int(latest["Volume"]),
                source=f"Yahoo Finance ({'Live' if len(hist)>1 else 'Snapshot'})",
            )
        except Exception as e:
            print(f"[YahooProvider] Error for {symbol}: {e}")
            return None

    async def get_historical(
        self, symbol: str, limit: int = 300, start_date: Optional[str] = None
    ) -> Optional[List[Candle]]:
        try:
            yf_sym = self.normalize_symbol(symbol)
            hist = await asyncio.to_thread(self._sync_get_historical, yf_sym, start_date)

            if hist is None or hist.empty:
                return None

            hist = hist.ffill().fillna(0)

            candles = []
            for date, row in hist.iterrows():
                try:
                    candles.append(Candle(
                        date=date.strftime("%Y-%m-%d"),
                        open=float(row["Open"]),
                        high=float(row["High"]),
                        low=float(row["Low"]),
                        close=float(row["Close"]),
                        volume=int(row["Volume"]),
                    ))
                except Exception:
                    continue

            print(f"[YahooProvider] {symbol} fetched {len(candles)} bars (Start: {candles[0].date if candles else 'N/A'})")
            return candles
        except Exception as e:
            print(f"[YahooProvider] Historical error for {symbol}: {e}")
            return None

    # ─── Yahoo-specific: Search (already async via httpx) ─────────────

    async def search_ticker(self, query: str, limit: int = 10) -> list:
        """Global search via Yahoo Finance API with in-memory TTL caching."""
        import httpx

        cache_key = f"{query.lower()}_{limit}"
        if cache_key in self._search_cache:
            expiry, cached_results = self._search_cache[cache_key]
            if time.time() < expiry:
                return cached_results
            else:
                del self._search_cache[cache_key]

        url = "https://query2.finance.yahoo.com/v1/finance/search"
        params = {"q": query, "quotesCount": limit, "newsCount": 0}
        headers = {"User-Agent": "Mozilla/5.0"}

        try:
            async with httpx.AsyncClient(timeout=5) as client:
                res = await client.get(url, params=params, headers=headers)
                if res.status_code == 200:
                    data = res.json()
                    results = []
                    for q in data.get("quotes", []):
                        if "symbol" in q:
                            results.append({
                                "symbol": q["symbol"],
                                "name": q.get("shortname", q.get("longname", q["symbol"])),
                                "type": q.get("quoteType", "EQUITY"),
                                "exchange": q.get("exchange", "Unknown"),
                            })

                    self._search_cache[cache_key] = (time.time() + 3600, results)
                    return results
                return []
        except Exception as e:
            print(f"[YahooProvider] Search error for '{query}': {e}")
            return []
