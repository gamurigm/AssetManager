from __future__ import annotations

from datetime import datetime, timezone

from app.agents.strategies.engine.models import StrategyConfig, TradeSignal
from services.contracts.events import MarketTickV1
from services.strategy_engine.service import CandleAggregator, StrategyRuntime


class FakeEngine:
    def __init__(self) -> None:
        self.calls = 0

    def run_session(self, *, m5_candles, m1_candles, account_size, config):
        self.calls += 1
        assert m5_candles
        assert m1_candles
        assert account_size == 10_000
        assert isinstance(config, StrategyConfig)
        return [
            TradeSignal(
                signal_id="orb:EURUSD:20260806:long",
                timestamp="2026-08-06T14:31:00+00:00",
                direction="LONG",
                orh=1.1,
                orl=1.09,
                fvg_top=1.099,
                fvg_bottom=1.098,
                entry=1.1,
                stop=1.095,
                tp=1.115,
                risk_pips=50,
                position_size=0.01,
                confidence="standard",
                atr_m1=0.001,
            )
        ]


class FakePublisher:
    def __init__(self) -> None:
        self.events = []

    def publish_event(self, *, topic, event, key) -> None:
        self.events.append((topic, event, key))


class InvalidSignalEngine(FakeEngine):
    def run_session(self, **kwargs):
        signals = super().run_session(**kwargs)
        signal = signals[0]
        return [
            TradeSignal(
                **{**signal.__dict__, "signal_id": "invalid-size-signal", "position_size": 0}
            )
        ]


def tick(at: datetime, price: float = 1.1, volume: float = 2) -> MarketTickV1:
    return MarketTickV1.create(
        source="unit-test",
        symbol="EURUSD",
        price=price,
        volume=volume,
        observed_at=at,
        correlation_id="corr-analysis-1",
    )


def test_candle_aggregator_uses_utc_buckets_and_accumulates_volume() -> None:
    aggregator = CandleAggregator("EURUSD")
    aggregator.update(tick(datetime(2026, 8, 6, 14, 31, 5, tzinfo=timezone.utc)))
    aggregator.update(
        tick(datetime(2026, 8, 6, 14, 31, 45, tzinfo=timezone.utc), 1.101, 3)
    )

    m1, m5 = aggregator.context()

    assert len(m1) == 1
    assert len(m5) == 1
    assert m1[0]["high"] == 1.101
    assert m1[0]["volume"] == 5
    assert m1[0]["timestamp"] == "2026-08-06T14:31:00+00:00"
    assert m5[0]["timestamp"] == "2026-08-06T14:30:00+00:00"


def test_strategy_runtime_publishes_each_signal_once_with_trace_context() -> None:
    publisher = FakePublisher()
    runtime = StrategyRuntime(
        symbol="EURUSD",
        strategy_name="ORB_FVG_ENGULFING",
        engine=FakeEngine(),
        config=StrategyConfig.default(),
        publisher=publisher,
        account_size=10_000,
        min_m1_candles=1,
        min_m5_candles=1,
    )
    event = tick(datetime(2026, 8, 6, 14, 31, 5, tzinfo=timezone.utc))

    runtime.process_tick(event)
    runtime.process_tick(event)

    assert len(publisher.events) == 1
    topic, signal, key = publisher.events[0]
    assert topic == "trade.signals.v1"
    assert key == "EURUSD"
    assert signal.correlation_id == event.correlation_id
    assert signal.causation_id == event.event_id
    assert signal.direction == "LONG"


def test_strategy_runtime_waits_for_warmup_without_rejecting_ticks() -> None:
    engine = FakeEngine()
    runtime = StrategyRuntime(
        symbol="EURUSD",
        strategy_name="ORB_FVG_ENGULFING",
        engine=engine,
        config=StrategyConfig.default(),
        publisher=FakePublisher(),
        account_size=10_000,
        min_m1_candles=20,
        min_m5_candles=4,
    )

    published = runtime.process_tick(
        tick(datetime(2026, 8, 6, 14, 31, 5, tzinfo=timezone.utc))
    )

    assert published == 0
    assert engine.calls == 0


def test_invalid_strategy_output_is_rejected_without_poisoning_tick_stream() -> None:
    publisher = FakePublisher()
    runtime = StrategyRuntime(
        symbol="EURUSD",
        strategy_name="ORB_FVG_ENGULFING",
        engine=InvalidSignalEngine(),
        config=StrategyConfig.default(),
        publisher=publisher,
        account_size=10_000,
        min_m1_candles=1,
        min_m5_candles=1,
    )

    published = runtime.process_tick(
        tick(datetime(2026, 8, 6, 14, 31, 5, tzinfo=timezone.utc))
    )

    assert published == 0
    assert publisher.events == []
