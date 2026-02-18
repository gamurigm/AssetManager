"""
Interface: Market Data Provider (DIP — Dependency Inversion Principle)
All external market data sources MUST implement this contract.
The application layer depends on THIS interface, never on concrete providers.

Liskov Substitution: Any implementation can replace another without breaking behavior.
"""

from abc import ABC, abstractmethod
from typing import Optional, List
from ..entities.market import Quote, Candle


class IMarketDataProvider(ABC):
    """Contract for all market data providers (Yahoo, FMP, Polygon, etc.)."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Provider identifier (e.g., 'yahoo', 'fmp')."""
        ...

    @abstractmethod
    async def get_quote(self, symbol: str) -> Optional[Quote]:
        """Fetch a real-time quote. Returns None on failure."""
        ...

    @abstractmethod
    async def get_historical(
        self, symbol: str, limit: int = 300, start_date: Optional[str] = None
    ) -> Optional[List[Candle]]:
        """Fetch historical OHLCV data. Returns None on failure."""
        ...

    def normalize_symbol(self, symbol: str) -> str:
        """
        Translate a universal symbol to provider-specific format.
        Default: no transformation. Override in subclasses as needed.
        """
        return symbol
