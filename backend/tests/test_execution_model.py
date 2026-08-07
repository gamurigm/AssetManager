import pytest

from app.agents.strategies.engine.execution_model import OHLCExecutionModel
from app.agents.strategies.engine.models import ExecutionSettings, TradeSignal


def make_signal(direction: str = "LONG") -> TradeSignal:
    if direction == "LONG":
        entry, stop, target = 100.0, 99.0, 103.0
    else:
        entry, stop, target = 100.0, 101.0, 97.0
    return TradeSignal(
        signal_id=f"test-{direction.lower()}",
        timestamp="2026-01-02T09:35:00",
        direction=direction,
        orh=101.0,
        orl=99.0,
        fvg_top=100.2,
        fvg_bottom=99.8,
        entry=entry,
        stop=stop,
        tp=target,
        risk_pips=1.0,
        position_size=10.0,
        confidence="standard",
        atr_m1=0.5,
    )


def candle(high: float, low: float, close: float = 100.0) -> dict:
    return {
        "timestamp": "2026-01-02T09:36:00",
        "open": 100.0,
        "high": high,
        "low": low,
        "close": close,
        "volume": 1_000,
    }


def test_ambiguous_candle_uses_conservative_stop_first_by_default():
    record = OHLCExecutionModel().simulate(
        make_signal(),
        [candle(high=104.0, low=98.0)],
        pip_value=1.0,
        settings=ExecutionSettings(),
    )

    assert record.outcome == "loss_sl"
    assert record.pnl_usd == pytest.approx(-10.0)
    assert "conservative" in record.execution_note


def test_optimistic_policy_is_explicit_and_auditable():
    record = OHLCExecutionModel().simulate(
        make_signal(),
        [candle(high=104.0, low=98.0)],
        pip_value=1.0,
        settings=ExecutionSettings(intrabar_fill_policy="optimistic"),
    )

    assert record.outcome == "win_tp"
    assert record.pnl_usd == pytest.approx(30.0)
    assert "optimistic" in record.execution_note


def test_slippage_and_commission_reduce_realized_pnl():
    record = OHLCExecutionModel().simulate(
        make_signal(),
        [candle(high=103.5, low=99.5)],
        pip_value=1.0,
        settings=ExecutionSettings(
            slippage_price=0.1,
            commission_per_trade=2.0,
        ),
    )

    assert record.entry_price == pytest.approx(100.1)
    assert record.exit_price == pytest.approx(102.9)
    assert record.gross_pnl_usd == pytest.approx(28.0)
    assert record.fees_usd == pytest.approx(2.0)
    assert record.pnl_usd == pytest.approx(26.0)
    assert record.pnl_r == pytest.approx(2.6)


def test_expired_position_is_marked_to_market():
    record = OHLCExecutionModel().simulate(
        make_signal(),
        [candle(high=101.0, low=99.5, close=100.5)],
        pip_value=1.0,
        settings=ExecutionSettings(),
    )

    assert record.outcome == "expired"
    assert record.pnl_usd == pytest.approx(5.0)
    assert record.is_win
    assert "marked to market" in record.execution_note


@pytest.mark.parametrize("direction", ["LONG", "SHORT"])
def test_stop_fill_is_adverse_for_both_directions(direction: str):
    signal = make_signal(direction)
    stop_candle = (
        candle(high=100.5, low=98.5)
        if direction == "LONG"
        else candle(high=101.5, low=99.5)
    )
    record = OHLCExecutionModel().simulate(
        signal,
        [stop_candle],
        pip_value=1.0,
        settings=ExecutionSettings(slippage_price=0.1),
    )

    assert record.pnl_usd == pytest.approx(-12.0)
    assert record.pnl_r == pytest.approx(-1.2)
