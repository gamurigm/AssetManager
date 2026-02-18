"""
Domain Entities — Portfolio
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class HoldingSnapshot:
    """A point-in-time view of a single holding."""
    symbol: str
    quantity: float
    average_price: float
    current_price: float = 0.0

    @property
    def market_value(self) -> float:
        return self.quantity * self.current_price

    @property
    def pnl(self) -> float:
        return self.quantity * (self.current_price - self.average_price)

    @property
    def pnl_percent(self) -> float:
        if self.average_price == 0:
            return 0.0
        return ((self.current_price - self.average_price) / self.average_price) * 100


@dataclass
class PortfolioSnapshot:
    """Aggregated point-in-time view of the entire portfolio."""
    holdings: List[HoldingSnapshot] = field(default_factory=list)

    @property
    def total_value(self) -> float:
        return sum(h.market_value for h in self.holdings)

    @property
    def total_pnl(self) -> float:
        return sum(h.pnl for h in self.holdings)

    @property
    def pnl_percent(self) -> float:
        cost = self.total_value - self.total_pnl
        if cost == 0:
            return 0.0
        return (self.total_pnl / cost) * 100
