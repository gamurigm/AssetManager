"""
Finazon Provider — Implements IMarketDataProvider
Uses Finazon API to fetch US stock data.
"""

import httpx
from datetime import datetime
from typing import Optional, List
import logfire

from ...domain.interfaces.market_provider import IMarketDataProvider
from ...domain.entities.market import Quote, Candle
from ...core.config import settings

class FinazonProvider(IMarketDataProvider):
    """
    Market Data Provider for Finazon.
    Doc: https://finazon.io/dataset/us_stocks_essential/docs/api/latest
    """

    def __init__(self, api_key: str = settings.FINAZON_API_KEY, timeout: float = 10.0):
        self.api_key = api_key
        self.base_url = "https://api.finazon.io/latest/finazon/us_stocks_essential"
        self.timeout = timeout
        self.headers = {}
        # Finazon supports apikey query param, let's just use it or authorization via query

    @property
    def name(self) -> str:
        return "finazon"

    def normalize_symbol(self, symbol: str) -> str:
        """Finazon generally uses standard US tickers like AAPL."""
        return symbol.upper()

    def _build_url(self, endpoint: str) -> str:
        return f"{self.base_url}{endpoint}"

    async def get_quote(self, symbol: str) -> Optional[Quote]:
        if not self.api_key:
            logfire.error("Finazon API key missing.")
            return None

        normalized_symbol = self.normalize_symbol(symbol)
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                # url: /finazon/us_stocks_essential/price
                url = self._build_url("/price")
                # According to docs: { "p": 184.95 }
                rsp = await client.get(
                    url,
                    params={"ticker": normalized_symbol, "apikey": self.api_key}
                )
                
                if rsp.status_code != 200:
                    logfire.warn(f"[Finazon] HTTP {rsp.status_code} for {normalized_symbol}: {rsp.text}")
                    return None
                    
                data = rsp.json()
                if "p" not in data:
                    return None
                    
                price = float(data["p"])
                
                return Quote(
                    symbol=symbol,
                    price=price,
                    change=0.0,
                    change_percent=0.0,
                    source=self.name
                )
            except Exception as e:
                logfire.error(f"[Finazon] Quote error for {symbol}: {e}")
                return None

    async def get_historical(
        self, symbol: str, limit: int = 300, start_date: Optional[str] = None
    ) -> Optional[List[Candle]]:
        if not self.api_key:
            return None

        normalized_symbol = self.normalize_symbol(symbol)

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                # url: /finazon/us_stocks_essential/time_series
                url = self._build_url("/time_series")
                
                params = {
                    "ticker": normalized_symbol,
                    "interval": "1d",
                    "order": "desc",
                    "page_size": min(limit, 1000), # Max 1000 per page
                    "apikey": self.api_key
                }
                
                # If start_date is provided, we should ideally convert it to UNIX timestamp
                # start_at. The user input 'YYYY-MM-DD'.
                if start_date:
                    try:
                        dt = datetime.strptime(start_date, "%Y-%m-%d")
                        params["start_at"] = int(dt.timestamp())
                    except ValueError:
                        pass # Ignore and fetch without start_date if invalid

                rsp = await client.get(url, params=params)

                if rsp.status_code != 200:
                    logfire.warn(f"[Finazon] HTTP {rsp.status_code} for historical {normalized_symbol}: {rsp.text}")
                    return None

                data = rsp.json()
                if "data" not in data:
                    return None
                    
                items = data["data"]
                candles = []
                
                # { "t": 1675256340, "o": 145.35, "h": 145.49, "l": 145.13, "c": 145.46, "v": 1006162 }
                for item in items:
                    ts = float(item["t"])
                    date_str = datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                    # data is 'desc' ordered, our convention is that we return chronologically or it's sorted by the repository later.
                    # We will append them as they come.
                    candles.append(
                        Candle(
                            date=date_str,
                            open=float(item.get("o", 0.0)),
                            high=float(item.get("h", 0.0)),
                            low=float(item.get("l", 0.0)),
                            close=float(item.get("c", 0.0)),
                            volume=int(item.get("v", 0)),
                        )
                    )
                return candles
            except Exception as e:
                logfire.error(f"[Finazon] Historical error for {symbol}: {e}")
                return None
