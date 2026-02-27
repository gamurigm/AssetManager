"""
Crawler Service — Automated Data Pre-fetching
Slowly crawls a universe of symbols to ensure DuckDB is populated.
"""

import asyncio
import logging
from .market_data import market_data_service

logger = logging.getLogger("MMAM")

# Default Universe: Top assets to ensure instant dashboard/chart loads
DEFAULT_UNIVERSE = [
    # Megacaps
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA", "BRK.B", "JPM", "V",
    "UNH", "JNJ", "WMT", "MA", "PG", "HD", "HD", "DIS", "BAC", "VZ", "KO", "PFE",
    # Tech/Growth
    "AMD", "INTC", "CSCO", "ORCL", "CRM", "NFLX", "ADBE", "PYPL", "SQ", "SHOP",
    # Crypto (Yahoo uses -USD, MarketDataService handles translation)
    "BTC/USD", "ETH/USD", "SOL/USD", "BNB/USD", "XRP/USD", "ADA/USD", "DOT/USD",
    # Forex
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD", "USD/CHF", "NZD/USD",
    # Commodities/ETFs
    "SPY", "QQQ", "IWM", "GLD", "SLV", "USO", "UNG", "TLT"
]

class CrawlerService:
    def __init__(self, symbols=None):
        self.universe = symbols or DEFAULT_UNIVERSE
        self.is_running = False
        self._current_index = 0

    async def run_crawl_cycle(self):
        """
        Perform one full pass through the universe.
        Designed to be called periodically (e.g., once a day or every few hours).
        """
        if self.is_running:
            logger.info("⚠️ [Crawler] Cycle already in progress. Skipping.")
            return

        self.is_running = True
        logger.info(f"🕸️ [Crawler] Starting pre-fetch cycle for {len(self.universe)} symbols...")
        
        for symbol in self.universe:
            try:
                # Synchronize Daily History (1 year)
                # market_data_service.get_historical checks DuckDB first.
                await market_data_service.get_historical(symbol, limit=365)
                
                # Synchronize Intraday (5-day window for 5m)
                await market_data_service.get_intraday(symbol, interval="5m", period="5d")
                
                # Slow drip: 10 seconds between symbols to be extremely conservative
                await asyncio.sleep(10)
                
            except Exception as e:
                logger.error(f"[Crawler] Error syncing {symbol}: {e}")

        self.is_running = False
        logger.info("🕸️ [Crawler] Cycle complete.")

    async def crawl_single_step(self):
        """
        Fetch the next symbol in the universe.
        Designed to be called very frequently (e.g., every minute) to 'drip' data 24/7.
        """
        if self._current_index >= len(self.universe):
            self._current_index = 0
            logger.info("🕸️ [Crawler] Universe reached end. Restarting drip...")

        symbol = self.universe[self._current_index]
        try:
            # logger.info(f"🕸️ [Crawler] Drip-fetching {symbol}...")
            await market_data_service.get_historical(symbol, limit=365)
            await market_data_service.get_intraday(symbol, interval="5m", period="5d")
        except Exception as e:
            logger.error(f"[Crawler-Drip] Error for {symbol}: {e}")
        
        self._current_index += 1

crawler_service = CrawlerService()
