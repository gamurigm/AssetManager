"""
Use Case: Get Historical Data (SRP)
Orchestrates: DuckDB check → API fallback → Persist to DuckDB → Return.
Depends on abstractions only (DIP).
"""

from typing import List, Dict, Any
from ...domain.entities.market import Candle
from ...domain.interfaces.market_provider import IMarketDataProvider
from ...domain.interfaces.data_repository import IHistoricalRepository
from ...core.rate_limiter import get_bucket


class GetHistoricalUseCase:
    """
    Fetches historical OHLCV data.
    Priority: Local DB → API cascade → persist for next time.
    """

    def __init__(
        self,
        providers: List[IMarketDataProvider],
        repository: IHistoricalRepository,
    ):
        self._providers = providers
        self._repo = repository

    async def execute(self, symbol: str, limit: int = 300) -> Dict[str, Any]:
        """
        Historical data strategy:
        1. Check latest date in DuckDB.
        2. If data is old/missing, fetch from API (Bootstrap/Incremental).
        3. Save to DuckDB.
        4. Return requested limit from DuckDB.
        """
        latest_date = self._repo.get_latest_date(symbol)
        count = self._repo.get_count(symbol)
        
        # Determine if sync is needed
        sync_required = True
        if latest_date:
            from datetime import datetime
            is_today = latest_date >= datetime.now().strftime("%Y-%m-%d")
            # If we have today's data and enough bars to satisfy the request, don't sync
            if is_today and count >= min(limit, 500): 
                sync_required = False
            # Small edge case: if limit is huge (10k) but we only have few hundred, 
            # maybe it was a partial bootstrap. Let it retry if it's very low.
            if count < 100:
                sync_required = True

        if sync_required:
            print(f"[GetHistorical] 🦆 Syncing {symbol} (Latest: {latest_date}, Count: {count})...")
            # If we have very little data, treat it as a bootstrap (fetch max)
            fetch_start_date = latest_date if count > 100 else None
            
            for provider in self._providers:
                bucket = get_bucket(provider.name)
                if not bucket.can_request():
                    continue

                bucket.consume()
                # Fetch missing data (Bootstrap if fetch_start_date is None)
                candles = await provider.get_historical(symbol, limit=limit, start_date=fetch_start_date)
                
                if candles:
                    self._repo.upsert_candles(symbol, candles, source=provider.name)
                    break # Success

        # Always return from DB for consistency
        all_candles = self._repo.get_history(symbol, limit)
        
        if not all_candles:
            return {"error": f"Historical data unavailable for {symbol}."}

        return {
            "symbol": symbol,
            "historical": [c.to_dict() for c in all_candles],
            "source": "DuckDB (Synced)",
            "count": len(all_candles)
        }
