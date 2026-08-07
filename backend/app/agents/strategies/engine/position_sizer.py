"""Position sizing policy independent from signal detection and fill simulation."""

from __future__ import annotations


class FixedFractionPositionSizer:
    """Risk a fixed equity fraction using the instrument's price value."""

    def calculate(
        self,
        account_equity: float,
        risk_fraction: float,
        risk_price_distance: float,
        price_value_per_unit: float,
    ) -> float:
        if account_equity <= 0:
            raise ValueError("account_equity must be greater than zero")
        if not 0 < risk_fraction <= 1:
            raise ValueError("risk_fraction must be between zero and one")
        if risk_price_distance <= 0:
            raise ValueError("risk_price_distance must be greater than zero")
        if price_value_per_unit <= 0:
            raise ValueError("price_value_per_unit must be greater than zero")
        return (
            account_equity
            * risk_fraction
            / (risk_price_distance * price_value_per_unit)
        )
