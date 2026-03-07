import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.services.portfolio_rebalance_service import PortfolioRebalanceService


class _FakeRepo:
    def __init__(self, portfolio):
        self.portfolio = portfolio
        self.transactions = []
        self.saved_portfolio = None

    def get_portfolio(self, portfolio_id: str = "main"):
        return list(self.portfolio)

    def add_transaction(self, **kwargs):
        self.transactions.append(kwargs)
        return True

    def save_portfolio(self, holdings, portfolio_id: str = "main"):
        self.saved_portfolio = list(holdings)
        return True


def test_apply_policy_rebalance_updates_holdings_and_records_transactions() -> None:
    repo = _FakeRepo([
        {"symbol": "AAPL", "name": "Apple", "shares": 10.0, "entryPrice": 100.0, "price": 120.0, "factor": 1.0, "sector": "Tech", "type": "stock", "purchaseDate": "2025-01-01"},
        {"symbol": "MSFT", "name": "Microsoft", "shares": 5.0, "entryPrice": 200.0, "price": 210.0, "factor": 1.0, "sector": "Tech", "type": "stock", "purchaseDate": "2025-01-01"},
    ])
    service = PortfolioRebalanceService(repo=repo)

    result = service.apply_policy_rebalance(
        portfolio_id="main",
        holdings=repo.portfolio,
        allocations=[
            {"symbol": "AAPL", "price": 120.0, "factor": 1.0, "target_notional": 720.0, "delta_shares": -4.0},
            {"symbol": "MSFT", "price": 210.0, "factor": 1.0, "target_notional": 1890.0, "delta_shares": 4.0},
        ],
    )

    assert "error" not in result
    assert result["transaction_count"] == 2
    assert len(repo.transactions) == 2
    saved = {holding["symbol"]: holding for holding in repo.saved_portfolio}
    assert round(saved["AAPL"]["shares"], 4) == 6.0
    assert round(saved["MSFT"]["shares"], 4) == 9.0


def test_apply_policy_rebalance_can_reverse_direction() -> None:
    repo = _FakeRepo([
        {"symbol": "TSLA", "name": "Tesla", "shares": 4.0, "entryPrice": 250.0, "price": 240.0, "factor": 1.0, "sector": "Auto", "type": "stock", "purchaseDate": "2025-01-01"},
    ])
    service = PortfolioRebalanceService(repo=repo)

    result = service.apply_policy_rebalance(
        portfolio_id="main",
        holdings=repo.portfolio,
        allocations=[
            {"symbol": "TSLA", "price": 240.0, "factor": 1.0, "target_notional": -480.0, "delta_shares": -6.0},
        ],
    )

    assert "error" not in result
    assert result["transaction_count"] == 2
    assert repo.transactions[0]["type_str"] == "SELL"
    assert repo.transactions[1]["type_str"] == "SELL"
    saved = {holding["symbol"]: holding for holding in repo.saved_portfolio}
    assert round(saved["TSLA"]["shares"], 4) == -2.0
    assert round(saved["TSLA"]["entryPrice"], 4) == 240.0