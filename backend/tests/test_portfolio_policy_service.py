import os
import sys
from datetime import datetime, timedelta, timezone
from typing import Dict, List

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.domain.entities.market import Candle
from app.services.portfolio_policy_service import PortfolioPolicyService


def _build_candles(closes: List[float]) -> List[Candle]:
    candles: List[Candle] = []
    start_date = datetime.now(timezone.utc).date() - timedelta(days=len(closes) + 5)
    for idx, close in enumerate(closes):
        candle_date = start_date + timedelta(days=idx)
        candles.append(Candle(date=candle_date.isoformat(), open=close, high=close, low=close, close=close, volume=1000))
    return candles


class _FakeRepo:
    def __init__(self, history: Dict[str, List[Candle]], portfolio: List[dict], transactions: List[dict] | None = None) -> None:
        self._history = history
        self._portfolio = portfolio
        self._transactions = transactions or []

    def get_portfolio(self, portfolio_id: str = "main") -> List[dict]:
        return list(self._portfolio)

    def get_history_range(self, symbol: str, start_date: str, end_date: str) -> List[Candle]:
        return [
            candle
            for candle in self._history.get(symbol, [])
            if start_date <= candle.date <= end_date
        ]

    def get_transactions(self, portfolio_id: str = "main") -> List[dict]:
        return list(self._transactions)


def test_policy_overweights_stronger_asset() -> None:
    history = {
        "AAPL": _build_candles([100 + idx * 1.8 for idx in range(40)]),
        "MSFT": _build_candles([120 - idx * 0.9 for idx in range(40)]),
        "SPY": _build_candles([400 + idx * 0.8 for idx in range(40)]),
    }
    portfolio = [
        {"symbol": "AAPL", "name": "Apple", "shares": 10, "price": 129, "entryPrice": 100, "factor": 1.0, "sector": "Tech", "type": "stock"},
        {"symbol": "MSFT", "name": "Microsoft", "shares": 10, "price": 102, "entryPrice": 120, "factor": 1.0, "sector": "Tech", "type": "stock"},
    ]
    service = PortfolioPolicyService(repo=_FakeRepo(history, portfolio))

    snapshot = service.build_policy_snapshot(portfolio_id="main", lookback_days=60, risk_aversion=0.25)

    assert "error" not in snapshot
    allocations = {allocation["symbol"]: allocation for allocation in snapshot["allocations"]}
    assert allocations["AAPL"]["expected_return_pct"] > allocations["MSFT"]["expected_return_pct"]
    assert allocations["MSFT"]["target_weight_pct"] < allocations["MSFT"]["current_weight_pct"]
    assert snapshot["summary"]["rebalance_required"] is True
    assert snapshot["objective"]["target_expected_return_pct"] >= snapshot["objective"]["current_expected_return_pct"]


def test_policy_locks_assets_without_history() -> None:
    history = {
        "AAPL": _build_candles([100 + idx * 1.1 for idx in range(40)]),
        "SPY": _build_candles([400 + idx * 0.7 for idx in range(40)]),
    }
    portfolio = [
        {"symbol": "AAPL", "name": "Apple", "shares": 5, "price": 115, "entryPrice": 100, "factor": 1.0, "sector": "Tech", "type": "stock"},
        {"symbol": "XYZ", "name": "Unknown", "shares": 3, "price": 50, "entryPrice": 50, "factor": 1.0, "sector": "Other", "type": "stock"},
    ]
    service = PortfolioPolicyService(repo=_FakeRepo(history, portfolio, transactions=[{"realized_pnl": 40}, {"realized_pnl": -10}]))

    snapshot = service.build_policy_snapshot(portfolio_id="main", lookback_days=60)

    assert "error" not in snapshot
    allocations = {allocation["symbol"]: allocation for allocation in snapshot["allocations"]}
    assert allocations["XYZ"]["has_data"] is False
    assert allocations["XYZ"]["action"] == "LOCK"
    assert snapshot["objective"]["realized_trade_ev"] == 15.0