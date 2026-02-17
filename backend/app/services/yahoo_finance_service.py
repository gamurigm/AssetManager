import yfinance as yf
import pandas as pd
from typing import List, Dict, Any, Optional

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

yahoo_finance_service = YahooFinanceService()
