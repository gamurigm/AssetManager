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
        # Do not replace '=' here, as Yahoo uses it for futures (e.g., GC=F)
        return symbol

    async def get_quote(self, symbol: str) -> Optional[Quote]:
        try:
            yf_sym = self.normalize_symbol(symbol)
            ticker = yf.Ticker(yf_sym)
            
            # Fetch 5 days to ensure we have previous close
            hist = ticker.history(period="5d")

            if hist.empty:
                return None
            
            latest = hist.iloc[-1]
            price = float(latest["Close"])
            
            # Calculate change without .info
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
        except Exception as e:
            print(f"[YahooProvider] Error for {symbol}: {e}")
            return None

    async def get_historical(
        self, symbol: str, limit: int = 300, start_date: Optional[str] = None
    ) -> Optional[List[Candle]]:
        try:
            yf_sym = self.normalize_symbol(symbol)
            ticker = yf.Ticker(yf_sym)
            
            if start_date:
                # Incremental sync: fetch from last date to now
                hist = ticker.history(start=start_date, interval="1d")
            else:
                # Bootstrap: fetch full history
                hist = ticker.history(period="max", interval="1d")

            if hist.empty:
                return None

            # Clean data: Replace NaNs with last valid value or 0
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
                    continue # Skip malformed rows
            
            print(f"[YahooProvider] {symbol} fetched {len(candles)} bars (Start: {candles[0].date if candles else 'N/A'})")
            return candles
        except Exception as e:
            print(f"[YahooProvider] Historical error for {symbol}: {e}")
            return None
