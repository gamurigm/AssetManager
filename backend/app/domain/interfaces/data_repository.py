"""
Interface: Historical Data Repository (DIP)
Abstracts the persistence layer for OHLCV data (DuckDB, SQLite, Postgres, etc.).
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from ..entities.market import Candle


class IHistoricalRepository(ABC):
    """Contract for historical data storage."""

    @abstractmethod
    def has_data(self, symbol: str, min_rows: int = 10) -> bool:
        """Check if sufficient data exists locally."""
        ...

    @abstractmethod
    def get_history(self, symbol: str, limit: int = 300) -> List[Candle]:
        """Retrieve stored candles for a symbol."""
        ...

    @abstractmethod
    def upsert_candles(self, symbol: str, candles: List[Candle], source: str = "unknown") -> int:
        """Insert or update candles. Returns count upserted."""
        ...

    @abstractmethod
    def get_stats(self) -> Dict[str, Any]:
        """Return storage statistics (total candles, symbols, size)."""
        ...
