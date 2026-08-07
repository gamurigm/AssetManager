"""Application layer for Kafka-driven strategy evaluation."""

from __future__ import annotations

import asyncio
import logging
import os
from dataclasses import dataclass
from datetime import timezone
from typing import Any, Protocol

from confluent_kafka import TopicPartition
from pydantic import ValidationError

from app.agents.strategies.engine.models import StrategyConfig, TradeSignal
from services.contracts.events import MarketTickV1, TradeSignalV1
from services.platform.health import ServiceHealth
from services.platform.kafka import ReliableMessageProcessor


logger = logging.getLogger("assetmanager.analysis")


class StrategyEnginePort(Protocol):
    def run_session(
        self,
        *,
        m5_candles: list[dict[str, Any]],
        m1_candles: list[dict[str, Any]],
        account_size: float,
        config: StrategyConfig,
    ) -> list[TradeSignal]: ...


class SignalPublisherPort(Protocol):
    def publish_event(self, *, topic: str, event: TradeSignalV1, key: str) -> None: ...


@dataclass(frozen=True)
class AnalysisSettings:
    kafka_bootstrap_servers: str
    symbols: tuple[str, ...]
    strategy_name: str
    account_size: float
    consumer_group: str = "analysis-worker-v1"

    @classmethod
    def from_env(cls) -> "AnalysisSettings":
        return cls(
            kafka_bootstrap_servers=os.getenv(
                "KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"
            ),
            symbols=tuple(
                item.strip().upper()
                for item in os.getenv(
                    "ANALYSIS_SYMBOLS", "AAPL,MSFT,TSLA,SPY,BTC/USD"
                ).split(",")
                if item.strip()
            ),
            strategy_name=os.getenv(
                "ANALYSIS_STRATEGY", "ORB_FVG_ENGULFING"
            ).strip().upper(),
            account_size=max(
                1.0, float(os.getenv("ANALYSIS_ACCOUNT_SIZE", "10000"))
            ),
            consumer_group=os.getenv(
                "ANALYSIS_CONSUMER_GROUP", "analysis-worker-v1"
            ),
        )


class CandleAggregator:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol
        self._closed_m1: list[dict[str, Any]] = []
        self._closed_m5: list[dict[str, Any]] = []
        self._current_m1: dict[str, Any] | None = None
        self._current_m5: dict[str, Any] | None = None

    @staticmethod
    def _new_candle(
        symbol: str,
        timestamp,
        price: float,
        volume: float,
    ) -> dict[str, Any]:
        return {
            "symbol": symbol,
            "timestamp": timestamp.isoformat(),
            "open": price,
            "high": price,
            "low": price,
            "close": price,
            "volume": volume,
        }

    @staticmethod
    def _apply(candle: dict[str, Any], price: float, volume: float) -> None:
        candle["high"] = max(float(candle["high"]), price)
        candle["low"] = min(float(candle["low"]), price)
        candle["close"] = price
        candle["volume"] = float(candle["volume"]) + volume

    def update(self, event: MarketTickV1) -> None:
        timestamp = event.observed_at.astimezone(timezone.utc)
        m1_at = timestamp.replace(second=0, microsecond=0)
        m5_at = timestamp.replace(
            minute=(timestamp.minute // 5) * 5,
            second=0,
            microsecond=0,
        )
        self._current_m1 = self._update_interval(
            current=self._current_m1,
            closed=self._closed_m1,
            bucket=m1_at,
            event=event,
            retention=500,
        )
        self._current_m5 = self._update_interval(
            current=self._current_m5,
            closed=self._closed_m5,
            bucket=m5_at,
            event=event,
            retention=200,
        )

    def _update_interval(
        self,
        *,
        current: dict[str, Any] | None,
        closed: list[dict[str, Any]],
        bucket,
        event: MarketTickV1,
        retention: int,
    ) -> dict[str, Any]:
        bucket_text = bucket.isoformat()
        if current is None or current["timestamp"] != bucket_text:
            if current is not None:
                closed.append(current)
                if len(closed) > retention:
                    del closed[: len(closed) - retention]
            return self._new_candle(
                self.symbol,
                bucket,
                event.price,
                event.volume,
            )
        self._apply(current, event.price, event.volume)
        return current

    def context(self) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        m1 = [*self._closed_m1]
        m5 = [*self._closed_m5]
        if self._current_m1 is not None:
            m1.append(dict(self._current_m1))
        if self._current_m5 is not None:
            m5.append(dict(self._current_m5))
        return m1, m5


class StrategyRuntime:
    SIGNAL_TOPIC = "trade.signals.v1"

    def __init__(
        self,
        *,
        symbol: str,
        strategy_name: str,
        engine: StrategyEnginePort,
        config: StrategyConfig,
        publisher: SignalPublisherPort,
        account_size: float,
        min_m1_candles: int = 20,
        min_m5_candles: int = 4,
    ) -> None:
        self.symbol = symbol
        self.strategy_name = strategy_name
        self.engine = engine
        self.config = config
        self.publisher = publisher
        self.account_size = account_size
        self.min_m1_candles = max(1, min_m1_candles)
        self.min_m5_candles = max(1, min_m5_candles)
        self.aggregator = CandleAggregator(symbol)
        self._published_signal_ids: set[str] = set()

    def process_tick(self, event: MarketTickV1) -> int:
        self.aggregator.update(event)
        m1, m5 = self.aggregator.context()
        if len(m1) < self.min_m1_candles or len(m5) < self.min_m5_candles:
            return 0
        signals = self.engine.run_session(
            m5_candles=m5,
            m1_candles=m1,
            account_size=self.account_size,
            config=self.config,
        )
        published = 0
        for signal in signals or []:
            if signal.signal_id in self._published_signal_ids:
                continue
            try:
                contract = TradeSignalV1.create(
                    source="analysis-worker",
                    correlation_id=event.correlation_id,
                    causation_id=event.event_id,
                    signal_id=signal.signal_id,
                    strategy=self.strategy_name,
                    symbol=self.symbol,
                    direction=signal.direction,
                    entry=signal.entry,
                    stop=signal.stop,
                    take_profit=signal.tp,
                    position_size=signal.position_size,
                    confidence=signal.confidence,
                )
            except ValidationError as exc:
                logger.error(
                    "Rejected invalid strategy output %s for %s: %s",
                    signal.signal_id,
                    self.symbol,
                    exc,
                )
                continue
            self.publisher.publish_event(
                topic=self.SIGNAL_TOPIC,
                event=contract,
                key=self.symbol,
            )
            self._published_signal_ids.add(signal.signal_id)
            published += 1
        return published


class AnalysisWorker:
    TICK_TOPIC = "market.ticks.v1"
    DLQ_TOPIC = "market.ticks.dlq.v1"

    def __init__(
        self,
        *,
        consumer: Any,
        runtimes: dict[str, StrategyRuntime],
        health: ServiceHealth,
        dead_letter_publisher: Any = None,
    ) -> None:
        self.consumer = consumer
        self.runtimes = runtimes
        self.health = health
        self._stop_event = asyncio.Event()
        self.health.register_dependency("kafka")
        self.processor = ReliableMessageProcessor(
            consumer=consumer,
            event_model=MarketTickV1,
            handler=self._handle_tick,
            dead_letter_topic=self.DLQ_TOPIC,
            dead_letter_publisher=dead_letter_publisher,
        )

    async def _handle_tick(self, event: MarketTickV1) -> None:
        runtime = self.runtimes.get(event.symbol)
        if runtime is None:
            return
        await asyncio.to_thread(runtime.process_tick, event)

    async def run(self) -> None:
        self.consumer.subscribe([self.TICK_TOPIC])
        self.health.mark_started()
        self.health.set_dependency("kafka", ready=True)
        try:
            while not self._stop_event.is_set():
                message = await asyncio.to_thread(self.consumer.poll, 0.5)
                if message is None:
                    continue
                if message.error():
                    self.health.set_dependency(
                        "kafka", ready=False, detail=str(message.error())
                    )
                    await asyncio.sleep(1)
                    continue
                outcome = await self.processor.process(message)
                if outcome == "retry":
                    logger.warning("Tick processing failed; offset retained for retry")
                    self.consumer.seek(
                        TopicPartition(
                            message.topic(),
                            message.partition(),
                            message.offset(),
                        )
                    )
                    await asyncio.sleep(0.25)
                else:
                    self.health.set_dependency("kafka", ready=True)
        finally:
            self.consumer.close()
            self.health.mark_stopped()

    def stop(self) -> None:
        self._stop_event.set()
