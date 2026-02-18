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
        # 1. Local DB first (instant)
        if self._repo.has_data(symbol, min_rows=20):
            print(f"[GetHistorical] 🦆 DuckDB HIT for {symbol}")
            candles = self._repo.get_history(symbol, limit)
            return {
                "symbol": symbol,
                "historical": [c.to_dict() for c in candles],
                "source": "DuckDB (Local)",
            }

        # 2. API cascade
        print(f"[GetHistorical] 🦆 DuckDB MISS for {symbol}. Fetching...")
        for provider in self._providers:
            bucket = get_bucket(provider.name)
            if not bucket.can_request():
                continue

            bucket.consume()
            candles = await provider.get_historical(symbol, limit)
            if candles:
                # Persist for future instant access
                self._repo.upsert_candles(symbol, candles, source=provider.name)
                return {
                    "symbol": symbol,
                    "historical": [c.to_dict() for c in candles],
                    "source": f"{provider.name} → DuckDB",
                }

        return {"error": f"Historical data unavailable for {symbol}."}
