import asyncio
import os
import sys
from typing import Dict, List

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.domain.entities.market import Candle
from app.services.portfolio_backtest_service import PortfolioBacktestService


def _build_candles(symbol: str, closes: List[float]) -> List[Candle]:
    candles: List[Candle] = []
    for idx, close in enumerate(closes, start=1):
        date = f"2024-01-{idx:02d}"
        candles.append(Candle(date=date, open=close, high=close, low=close, close=close, volume=1_000))
    return candles


class _FakeRepo:
    def __init__(self, history: Dict[str, List[Candle]], portfolio: List[dict] | None = None) -> None:
        self._history = history
        self._portfolio = portfolio or []

    def get_latest_date(self, symbol: str):
        candles = self._history.get(symbol, [])
        return candles[-1].date if candles else None

    def get_count(self, symbol: str) -> int:
        return len(self._history.get(symbol, []))

    def get_history_range(self, symbol: str, start_date: str, end_date: str) -> List[Candle]:
        return [
            candle
            for candle in self._history.get(symbol, [])
            if start_date <= candle.date <= end_date
        ]

    def get_portfolio(self, portfolio_id: str = "main") -> List[dict]:
        return list(self._portfolio)


class _FakeMarketData:
    async def get_historical(self, symbol: str, limit: int = 300):
        return {"symbol": symbol, "historical": [], "source": "fake"}


def _make_service(history: Dict[str, List[Candle]], portfolio: List[dict] | None = None) -> PortfolioBacktestService:
    service = PortfolioBacktestService()
    service._repo = _FakeRepo(history, portfolio=portfolio)
    service._mds = _FakeMarketData()
    service._cpp_checked = True
    service._core_module = None
    service._cpp_engine_cls = None
    return service


def test_manual_buy_and_hold_portfolio_backtest() -> None:
    service = _make_service(
        {
            "AAPL": _build_candles("AAPL", [100, 102, 105, 108, 110, 112, 115, 117, 120, 123]),
            "MSFT": _build_candles("MSFT", [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]),
        }
    )

    result = asyncio.run(
        service.run_backtest(
            start_date="2024-01-01",
            end_date="2024-01-10",
            initial_cash=10_000,
            assets=[
                {"symbol": "AAPL", "weight": 0.6},
                {"symbol": "MSFT", "weight": 0.4},
            ],
            rebalance_frequency="none",
        )
    )

    assert "error" not in result
    assert result["engine"] == "python"
    assert result["kpis"]["final_equity"] > 10_000
    assert len(result["trades"]) == 2
    assert result["equity_curve"][0]["date"] == "2024-01-01"


def test_weekly_rebalance_generates_extra_trades() -> None:
    service = _make_service(
        {
            "AAPL": _build_candles("AAPL", [100, 104, 108, 112, 116, 120, 124, 128, 132, 136]),
            "MSFT": _build_candles("MSFT", [100, 98, 96, 94, 92, 90, 88, 86, 84, 82]),
        }
    )

    result = asyncio.run(
        service.run_backtest(
            start_date="2024-01-01",
            end_date="2024-01-10",
            initial_cash=10_000,
            assets=[
                {"symbol": "AAPL", "weight": 0.5},
                {"symbol": "MSFT", "weight": 0.5},
            ],
            rebalance_frequency="weekly",
        )
    )

    assert "error" not in result
    assert len(result["trades"]) > 2
    assert result["rebalance_frequency"] == "weekly"


def test_portfolio_holdings_are_converted_to_weights() -> None:
    service = _make_service(
        {
            "AAPL": _build_candles("AAPL", [100, 101, 102, 103, 104]),
            "MSFT": _build_candles("MSFT", [100, 100, 100, 100, 100]),
        },
        portfolio=[
            {"symbol": "AAPL", "name": "Apple", "shares": 2.0, "entryPrice": 100.0, "factor": 1.0},
            {"symbol": "MSFT", "name": "Microsoft", "shares": 1.0, "entryPrice": 100.0, "factor": 1.0},
        ],
    )

    result = asyncio.run(
        service.run_backtest(
            start_date="2024-01-01",
            end_date="2024-01-05",
            initial_cash=9_000,
            portfolio_id="main",
            rebalance_frequency="none",
        )
    )

    assert "error" not in result
    weights = sorted(asset["target_weight"] for asset in result["assets"])
    assert round(weights[0], 4) == 0.3333
    assert round(weights[1], 4) == 0.6667


def test_remote_execution_mode_requires_service_url() -> None:
    service = _make_service(
        {
            "AAPL": _build_candles("AAPL", [100, 101, 102, 103, 104]),
        }
    )
    service._remote_base_url = ""

    result = asyncio.run(
        service.run_backtest(
            start_date="2024-01-01",
            end_date="2024-01-05",
            initial_cash=5_000,
            assets=[{"symbol": "AAPL", "weight": 1.0}],
            execution_mode="remote",
        )
    )

    assert "error" in result
    assert "PORTFOLIO_CPP_SERVICE_URL" in result["error"]


def test_remote_execution_mode_uses_remote_engine() -> None:
    service = _make_service(
        {
            "AAPL": _build_candles("AAPL", [100, 101, 102, 103, 104]),
        }
    )
    service._remote_base_url = "http://127.0.0.1:9092"

    async def _fake_remote_engine(**_: object):
        return {
            "trades": [
                {
                    "date": "2024-01-01",
                    "symbol": "AAPL",
                    "side": "BUY",
                    "quantity": 50.0,
                    "price": 100.0,
                    "notional": 5_000.0,
                    "fee": 0.0,
                }
            ],
            "equity_curve": [
                {"date": "2024-01-01", "equity": 5_000.0, "cash": 0.0},
                {"date": "2024-01-05", "equity": 5_200.0, "cash": 0.0},
            ],
            "quantities": {"AAPL": 50.0},
        }

    service._run_remote_engine = _fake_remote_engine  # type: ignore[method-assign]

    result = asyncio.run(
        service.run_backtest(
            start_date="2024-01-01",
            end_date="2024-01-05",
            initial_cash=5_000,
            assets=[{"symbol": "AAPL", "weight": 1.0}],
            execution_mode="remote",
        )
    )

    assert "error" not in result
    assert result["engine"] == "cpp-remote"
    assert result["kpis"]["final_equity"] == 5200.0