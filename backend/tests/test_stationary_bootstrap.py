from app.agents.strategies.engine.models import TradeRecord, TradeSignal
from app.agents.strategies.engine.stationary_bootstrap import (
    StationaryBootstrap,
    recommend_block_length,
)


def make_trade(pnl: float, outcome: str) -> TradeRecord:
    signal = TradeSignal(
        "bootstrap-signal",
        "2024-01-01T09:35:00",
        "LONG",
        1.0,
        0.0,
        1.0,
        0.9,
        1.0,
        0.9,
        1.1,
        0.1,
        1.0,
        "standard",
        0.01,
    )
    return TradeRecord(
        signal,
        outcome,
        1.1 if outcome == "win_tp" else 0.9,
        "2024-01-01T10:00:00",
        3.0 if outcome == "win_tp" else -1.0,
        pnl,
        0.0,
    )


def test_stationary_bootstrap_is_reproducible():
    trades = [
        make_trade(50.0, "win_tp") if index % 3 else make_trade(-20.0, "loss_sl")
        for index in range(30)
    ]
    block_length = recommend_block_length(len(trades))

    first = StationaryBootstrap(block_length=block_length, seed=42).run(
        trades,
        10_000.0,
        iterations=500,
        return_samples=False,
    )
    second = StationaryBootstrap(block_length=block_length, seed=42).run(
        trades,
        10_000.0,
        iterations=500,
        return_samples=False,
    )

    assert block_length > 1
    assert first["method"] == "stationary_bootstrap"
    assert first["net_profit_95_ci"] == second["net_profit_95_ci"]
    assert first["max_drawdown_95_ci_pct"] == second["max_drawdown_95_ci_pct"]
