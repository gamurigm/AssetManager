"""
Yahoo Finance Provider — Implements IMarketDataProvider.
Uses yfinance library. Most stable free source.
"""

import yfinance as yf
from typing import Optional, List
from ...domain.interfaces.market_provider import IMarketDataProvider
from ...domain.entities.market import Quote, Candle


class YahooProvider(IMarketDataProvider):

    @property
    def name(self) -> str:
        return "yahoo"

    def normalize_symbol(self, symbol: str) -> str:
        if symbol == "BTC/USD":
            return "BTC-USD"
        if symbol == "ETH/USD":
            return "ETH-USD"
        if "/" in symbol:
            fiat = ["EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "NZD"]
            if any(c in symbol for c in fiat):
                return symbol.replace("/", "") + "=X"
            return symbol.replace("/", "-")
        return symbol.replace("=", "-")

    async def get_quote(self, symbol: str) -> Optional[Quote]:
        try:
            yf_sym = self.normalize_symbol(symbol)
            ticker = yf.Ticker(yf_sym)
            hist = ticker.history(period="1d")

            if hist.empty:
                info = ticker.info
                price = info.get("regularMarketPrice") or info.get("currentPrice")
                if not price:
                    return None
                return Quote(
                    symbol=symbol,
                    price=float(price),
                    change=float(info.get("regularMarketChange", 0)),
                    change_percent=float(info.get("regularMarketChangePercent", 0)),
                    source="Yahoo Finance (Info)",
                )

            latest = hist.iloc[-1]
            prev_close = ticker.info.get("previousClose") or float(latest["Open"])
            price = float(latest["Close"])
            change = price - prev_close
            pct = (change / prev_close) * 100 if prev_close else 0

            return Quote(
                symbol=symbol,
                price=price,
                change=change,
                change_percent=pct,
                volume=int(latest["Volume"]),
                source="Yahoo Finance (Live)",
            )
        except Exception as e:
            print(f"[YahooProvider] Error for {symbol}: {e}")
            return None

    async def get_historical(self, symbol: str, limit: int = 300) -> Optional[List[Candle]]:
        try:
            yf_sym = self.normalize_symbol(symbol)
            ticker = yf.Ticker(yf_sym)
            hist = ticker.history(period="1mo", interval="1d")

            if hist.empty:
                return None

            return [
                Candle(
                    date=date.strftime("%Y-%m-%d"),
                    open=float(row["Open"]),
                    high=float(row["High"]),
                    low=float(row["Low"]),
                    close=float(row["Close"]),
                    volume=int(row["Volume"]),
                )
                for date, row in hist.iterrows()
            ]
        except Exception as e:
            print(f"[YahooProvider] Historical error for {symbol}: {e}")
            return None
