from datetime import date

import pytest

from app.agents.strategies.backtest_runner import BacktestConfig, BacktestRunner
from app.agents.strategies.engine.kpi_calculator import ORBKPICalculator
from app.agents.strategies.engine.models import TradeRecord, TradeSignal


def make_signal(signal_id: str, timestamp: str) -> TradeSignal:
    return TradeSignal(
        signal_id=signal_id,
        timestamp=timestamp,
        direction="LONG",
        orh=101.0,
        orl=99.0,
        fvg_top=100.2,
        fvg_bottom=99.8,
        entry=100.0,
        stop=99.0,
        tp=103.0,
        risk_pips=1.0,
        position_size=10.0,
        confidence="standard",
        atr_m1=0.5,
    )


class StaticStrategy:
    def __init__(self, signals):
        self.signals = signals

    def run_session(self, m5_candles, m1_candles, account_size, config):
        return self.signals


class RecordingExecutionModel:
    def __init__(self):
        self.calls = 0
        self.signals = []

    def simulate(self, signal, remaining_candles, pip_value, settings):
        self.calls += 1
        self.signals.append(signal)
        return TradeRecord(
            signal=signal,
            outcome="win_tp",
            exit_price=103.0,
            exit_timestamp="2026-01-02T09:40:00",
            pnl_r=3.0,
            pnl_usd=30.0,
            slippage_pips=0.0,
        )


def session():
    return {
        "date": date(2026, 1, 2),
        "m5": [{"timestamp": "2026-01-02T09:30:00"}],
        "m1": [
            {"timestamp": "2026-01-02T09:35:00"},
            {"timestamp": "2026-01-02T09:36:00"},
            {"timestamp": "2026-01-02T09:41:00"},
        ],
    }


def config(*, pip_value: float = 1.0) -> BacktestConfig:
    return BacktestConfig(
        symbol="AAPL",
        start_date="2026-01-01",
        end_date="2026-01-03",
        pip_value=pip_value,
    )


def test_single_position_flow_skips_overlapping_signal():
    signals = [
        make_signal("first", "2026-01-02T09:35:00"),
        make_signal("overlap", "2026-01-02T09:36:00"),
    ]
    execution = RecordingExecutionModel()
    runner = BacktestRunner(
        StaticStrategy(signals),
        repository=object(),
        kpi_calc=ORBKPICalculator(),
        execution_model=execution,
    )

    trades, _, _ = runner._run_session_loop(
        [session()],
        config().strategy_config(),
        config(),
    )

    assert execution.calls == 1
    assert [trade.signal.signal_id for trade in trades] == ["first"]


def test_runner_applies_instrument_value_before_execution():
    execution = RecordingExecutionModel()
    runner = BacktestRunner(
        StaticStrategy([make_signal("sized", "2026-01-02T09:35:00")]),
        repository=object(),
        kpi_calc=ORBKPICalculator(),
        execution_model=execution,
    )

    runner._run_session_loop(
        [session()],
        config(pip_value=5.0).strategy_config(),
        config(pip_value=5.0),
    )

    assert execution.signals[0].position_size == pytest.approx(10.0)


def test_missing_signal_timestamp_fails_instead_of_fabricating_a_fill():
    runner = BacktestRunner(
        StaticStrategy([make_signal("missing", "2026-01-02T09:37:00")]),
        repository=object(),
        kpi_calc=ORBKPICalculator(),
        execution_model=RecordingExecutionModel(),
    )

    with pytest.raises(ValueError, match="does not exist"):
        runner._run_session_loop(
            [session()],
            config().strategy_config(),
            config(),
        )
