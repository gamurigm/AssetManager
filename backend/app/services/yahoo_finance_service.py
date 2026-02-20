import yfinance as yf
import pandas as pd
from typing import List, Dict, Any, Optional
from datetime import timezone

class YahooFinanceService:
    @staticmethod
    async def get_historical(symbol: str, period: str = "1mo", interval: str = "1d") -> Dict[str, Any]:
        """
        Fetch historical data using yfinance.
        period: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
        interval: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
        """
        try:
            # yfinance is synchronous, so we run it in a way that doesn't block if needed, 
            # though for simple calls it's fine in FastAPI
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period=period, interval=interval)
            
            if hist.empty:
                return {"error": f"No historical data found for {symbol}"}
            
            # Convert to standard OHLC format
            historical_data = []
            for date, row in hist.iterrows():
                historical_data.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "open": float(row["Open"]),
                    "high": float(row["High"]),
                    "low": float(row["Low"]),
                    "close": float(row["Close"]),
                    "volume": int(row["Volume"])
                })
            
            return {
                "symbol": symbol,
                "historical": historical_data
            }
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def get_quote(symbol: str) -> Dict[str, Any]:
        """Get current price info using yfinance. More robust than .info"""
        try:
            ticker = yf.Ticker(symbol)
            # Fetch the most recent 1-day bar
            hist = ticker.history(period="1d")
            
            if hist.empty:
                # Fallback to info if history fails
                info = ticker.info
                return {
                    "price": info.get("regularMarketPrice") or info.get("currentPrice"),
                    "change": info.get("regularMarketChange"),
                    "changePercentage": info.get("regularMarketChangePercent"),
                    "source": "Yahoo Finance (Info Fallback)"
                }
            
            latest = hist.iloc[-1]
            prev_close = ticker.info.get("previousClose") or latest["Open"]
            price = float(latest["Close"])
            change = price - prev_close
            pct_change = (change / prev_close) * 100 if prev_close else 0
            
            return {
                "price": price,
                "change": change,
                "changePercentage": pct_change,
                "volume": int(latest["Volume"]),
                "source": "Yahoo Finance (Live)"
            }
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def get_intraday(
        symbol: str,
        interval: str = "1m",
        period: str = "5d",
    ) -> Dict[str, Any]:
        """
        Fetch intraday OHLCV candles using yfinance.

        Args:
            symbol:   Ticker in Yahoo format (e.g. "AAPL", "BTC-USD", "EURUSD=X").
            interval: Candle size — "1m" (M1) or "5m" (M5).
                      yfinance supports: 1m,2m,5m,15m,30m,60m,90m,1h.
            period:   Lookback window — "1d","5d","1mo","3mo".
                      NOTE: 1m data is only available for the last 7 days from Yahoo Finance.

        Returns:
            {
                "symbol": str,
                "interval": str,
                "candles": [
                    { "timestamp": "2025-11-01T09:30:00",
                      "open": float, "high": float, "low": float,
                      "close": float, "volume": int }
                ],
                "source": "Yahoo Finance (Intraday)"
            }
        """
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period=period, interval=interval)

            if hist.empty:
                return {"error": f"No intraday data for {symbol} ({interval}, {period})"}

            candles: List[Dict[str, Any]] = []
            for ts, row in hist.iterrows():
                # Normalise timezone → UTC → naive ISO-8601 string
                if hasattr(ts, "tzinfo") and ts.tzinfo is not None:
                    ts_utc = ts.astimezone(timezone.utc).replace(tzinfo=None)
                else:
                    ts_utc = ts
                candles.append({
                    "timestamp": ts_utc.strftime("%Y-%m-%dT%H:%M:%S"),
                    "open":   float(row["Open"]),
                    "high":   float(row["High"]),
                    "low":    float(row["Low"]),
                    "close":  float(row["Close"]),
                    "volume": int(row["Volume"]),
                })

            return {
                "symbol":   symbol,
                "interval": interval,
                "candles":  candles,
                "source":   "Yahoo Finance (Intraday)",
            }
        except Exception as e:
            return {"error": str(e)}

yahoo_finance_service = YahooFinanceService()
