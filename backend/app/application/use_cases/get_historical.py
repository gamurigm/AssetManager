"""
Use Case: Get Historical Data (SRP)
Orchestrates: Cache → DuckDB check → API fallback → Persist to DuckDB → Return.
Depends on abstractions only (DIP).

PERFORMANCE: In-memory TTL cache (5 min), bundled DB metadata lookups,
parallel provider racing for API sync.
"""

import asyncio
import time
from typing import List, Dict, Any, Optional
from ...domain.entities.market import Candle
from ...domain.interfaces.market_provider import IMarketDataProvider
from ...domain.interfaces.data_repository import IHistoricalRepository
from ...core.rate_limiter import get_bucket

# In-memory cache: {cache_key: (expiry_timestamp, result_dict)}
_hist_cache: Dict[str, tuple] = {}
HIST_CACHE_TTL = 300  # 5 minutes


class GetHistoricalUseCase:
    """
    Fetches historical OHLCV data.
    Priority: RAM cache → Local DB → Parallel API race → persist for next time.
    """

    def __init__(
        self,
        providers: List[IMarketDataProvider],
        repository: IHistoricalRepository,
    ):
        self._providers = providers
        self._repo = repository

    def _get_db_metadata(self, symbol: str) -> tuple:
        """Bundle 3 DB lookups into one blocking call (run via to_thread)."""
        latest_date = self._repo.get_latest_date(symbol)
        count = self._repo.get_count(symbol)
        last_sync = self._repo.get_last_sync_time(symbol)
        return latest_date, count, last_sync

    async def _try_provider(self, provider, symbol: str, limit: int, start_date: Optional[str]) -> Optional[list]:
        """Attempt a single provider; returns list of Candle on success, None on failure."""
        bucket = get_bucket(provider.name)
        if not bucket.can_request():
            return None
        bucket.consume()
        try:
            candles = await provider.get_historical(symbol, limit=limit, start_date=start_date)
            if candles:
                return (candles, provider.name)
        except Exception as e:
            print(f"[GetHistorical] ⚠️ {provider.name}: {e}")
        return None

    async def execute(self, symbol: str, limit: int = 300) -> Dict[str, Any]:
        # 0. In-memory cache check (fastest path — sub-microsecond)
        cache_key = f"{symbol}_{limit}"
        now = time.time()
        if cache_key in _hist_cache:
            expiry, cached_result = _hist_cache[cache_key]
            if now < expiry:
                return cached_result

        # 1. Bundled DB metadata lookup (single threaded call instead of 3 sequential)
        latest_date, count, last_sync = await asyncio.to_thread(self._get_db_metadata, symbol)

        # 2. Determine if sync is needed
        sync_required = True
        if latest_date:
            from datetime import datetime

            is_today = latest_date >= datetime.now().strftime("%Y-%m-%d")
            seconds_since_sync = (now - last_sync) if last_sync else 999999

            if (seconds_since_sync < 21600 or is_today) and count >= min(limit, 500):
                sync_required = False

            if count < 100:
                sync_required = True

        # 3. Parallel provider race for sync (if needed)
        if sync_required:
            print(f"[GetHistorical] 🦆 Syncing {symbol} (Latest: {latest_date}, Count: {count})...")
            fetch_start_date = latest_date if count > 100 else None

            RACE_SIZE = min(2, len(self._providers))
            tasks = [
                asyncio.create_task(self._try_provider(p, symbol, limit, fetch_start_date))
                for p in self._providers[:RACE_SIZE]
            ]

            winner = None
            for coro in asyncio.as_completed(tasks):
                result = await coro
                if result:
                    winner = result
                    for t in tasks:
                        t.cancel()
                    break

            if winner:
                candles, source_name = winner
                await asyncio.to_thread(self._repo.upsert_candles, symbol, candles, source=source_name)
            elif len(self._providers) > RACE_SIZE:
                # Sequential fallback for remaining providers
                for provider in self._providers[RACE_SIZE:]:
                    result = await self._try_provider(provider, symbol, limit, fetch_start_date)
                    if result:
                        candles, source_name = result
                        await asyncio.to_thread(self._repo.upsert_candles, symbol, candles, source=source_name)
                        break

        # 4. Always return from DB for consistency
        all_candles = await asyncio.to_thread(self._repo.get_history, symbol, limit)

        if not all_candles:
            return {"error": f"Historical data unavailable for {symbol}."}

        result = {
            "symbol": symbol,
            "historical": [c.to_dict() for c in all_candles],
            "source": "DuckDB (Synced)",
            "count": len(all_candles)
        }

        # 5. Cache in RAM for next request
        _hist_cache[cache_key] = (now + HIST_CACHE_TTL, result)

        return result

