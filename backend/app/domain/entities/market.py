"""
Domain Entities — Market Data
Pure data classes with no external dependencies (SRP).
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class Quote:
    """Represents a real-time price quote for any asset."""
    symbol: str
    price: float
    change: float = 0.0
    change_percent: float = 0.0
    volume: Optional[int] = None
    source: str = "unknown"

    def to_dict(self) -> dict:
        return {
            "price": self.price,
            "change": self.change,
            "changePercentage": self.change_percent,
            "volume": self.volume,
            "source": self.source,
        }


@dataclass(frozen=True)
class Candle:
    """Represents a single OHLCV bar."""
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int = 0

    def to_dict(self) -> dict:
        return {
            "date": self.date,
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume,
        }


@dataclass(frozen=True)
class AssetInfo:
    """Metadata about an asset (symbol, name, type, sector)."""
    symbol: str
    name: str = ""
    asset_type: str = "stock"  # stock, crypto, forex, commodity
    sector: str = ""
    exchange: str = ""
