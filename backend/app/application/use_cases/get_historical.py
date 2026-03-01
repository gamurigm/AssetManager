"""
Use Case: Get Historical Data (SRP)
Orchestrates: Cache → DuckDB check → API fallback → Persist to DuckDB → Return.
Depends on abstractions only (DIP).

PERFORMANCE: In-memory TTL cache (5 min) for repeated requests.
"""

import time
from typing import List, Dict, Any
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
    Priority: RAM cache → Local DB → API cascade → persist for next time.
    """

    def __init__(
        self,
        providers: List[IMarketDataProvider],
        repository: IHistoricalRepository,
    ):
        self._providers = providers
        self._repo = repository

    async def execute(self, symbol: str, limit: int = 300) -> Dict[str, Any]:
        # 0. In-memory cache check (fastest path)
        cache_key = f"{symbol}_{limit}"
        now = time.time()
        if cache_key in _hist_cache:
            expiry, cached_result = _hist_cache[cache_key]
            if now < expiry:
                return cached_result

        # 1. Check DuckDB state
        latest_date = self._repo.get_latest_date(symbol)
        count = self._repo.get_count(symbol)
        last_sync = self._repo.get_last_sync_time(symbol)

        # 2. Determine if sync is needed
        sync_required = True
        if latest_date:
            from datetime import datetime
            
            is_today = latest_date >= datetime.now().strftime("%Y-%m-%d")
            seconds_since_sync = (now - last_sync) if last_sync else 999999
            
            # Skip sync if we already synced in the last 6 hours (21600s), OR if we have today's full candle
            if (seconds_since_sync < 21600 or is_today) and count >= min(limit, 500):
                sync_required = False
                
            if count < 100:
                sync_required = True

        # 3. Sync from API if needed
        if sync_required:
            print(f"[GetHistorical] 🦆 Syncing {symbol} (Latest: {latest_date}, Count: {count})...")
            fetch_start_date = latest_date if count > 100 else None

            for provider in self._providers:
                bucket = get_bucket(provider.name)
                if not bucket.can_request():
                    continue

                bucket.consume()
                candles = await provider.get_historical(symbol, limit=limit, start_date=fetch_start_date)

                if candles:
                    self._repo.upsert_candles(symbol, candles, source=provider.name)
                    break

        # 4. Always return from DB for consistency
        all_candles = self._repo.get_history(symbol, limit)

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
