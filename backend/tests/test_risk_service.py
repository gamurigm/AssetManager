from datetime import datetime

import pandas as pd
import pytest

from app.services.math_core import math_core
from app.services.risk_service import RiskService


class FakeRiskDataSource:
    def __init__(self) -> None:
        dates = pd.date_range("2026-01-01", periods=30, freq="B")
        self.prices = {
            "AAPL": pd.Series(
                [100 + index + (index % 3) for index in range(30)],
                index=dates,
                dtype=float,
            ),
            "SPY": pd.Series(
                [500 + index * 0.8 for index in range(30)],
                index=dates,
                dtype=float,
            ),
        }

    def load_close_prices(self, symbols, start_date: datetime):
        return {
            symbol: self.prices[symbol]
            for symbol in symbols
            if symbol in self.prices
        }

    def get_transactions(self):
        return [
            {"realized_pnl": 100.0},
            {"realized_pnl": -40.0},
        ]


def test_var_does_not_report_losses_for_all_positive_returns():
    returns = [0.01, 0.02, 0.005, 0.03]

    assert RiskService.calculate_var(returns) == 0.0
    assert RiskService.calculate_cvar(returns) == 0.0
    assert RiskService.calculate_modified_var(returns) >= 0.0


def test_expected_shortfall_uses_at_least_one_tail_observation():
    returns = [-0.10, -0.04, 0.01, 0.02, 0.03]

    assert RiskService.calculate_var(returns, confidence_level=0.80) == pytest.approx(0.10)
    assert RiskService.calculate_cvar(returns, confidence_level=0.80) == pytest.approx(0.10)


def test_risk_service_uses_injected_data_source_and_reports_value_coverage():
    service = RiskService(data_source=FakeRiskDataSource())

    report = service.get_portfolio_risk_report(
        [
            {"symbol": "AAPL", "shares": 10, "price": 100},
            {"symbol": "MISSING", "shares": 5, "price": 100},
        ]
    )

    assert "error" not in report
    assert report["total_aum"] == 1_500.0
    assert report["covered_aum"] == 1_000.0
    assert report["coverage_percent"] == 50.0
    assert report["coverage_value_percent"] == pytest.approx(66.7)
    assert report["exposure"] == {"AAPL": 1.0}
    assert report["factor_analysis"]["AAPL"]["beta"] is not None


def test_risk_adjusted_return_is_dimensionless_and_not_aum_scaled():
    assert math_core.risk_adjusted_return(0.10, 0.20) == pytest.approx(0.5)
