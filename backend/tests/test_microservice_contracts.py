from __future__ import annotations

import asyncio
from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from services.contracts.events import MarketTickV1, OrderCommandV1, TradeSignalV1
from services.platform.health import ServiceHealth
from services.platform.kafka import KafkaSettings, ReliableMessageProcessor


class FakeMessage:
    def __init__(self, value: bytes) -> None:
        self._value = value

    def value(self) -> bytes:
        return self._value


class FakeConsumer:
    def __init__(self) -> None:
        self.committed: list[FakeMessage] = []

    def commit(self, *, message: FakeMessage, asynchronous: bool) -> None:
        assert asynchronous is False
        self.committed.append(message)


class FakeDeadLetterPublisher:
    def __init__(self) -> None:
        self.messages: list[tuple[str, bytes, str]] = []

    def publish(self, *, topic: str, payload: bytes, reason: str) -> None:
        self.messages.append((topic, payload, reason))


def make_tick() -> MarketTickV1:
    return MarketTickV1.create(
        source="unit-test",
        symbol="EURUSD",
        price=1.1,
        volume=25,
        observed_at=datetime.now(timezone.utc),
        correlation_id="corr-0001",
    )


def test_market_tick_contract_is_versioned_strict_and_serializable() -> None:
    event = make_tick()

    restored = MarketTickV1.model_validate_json(event.model_dump_json())

    assert restored == event
    assert restored.event_type == "market.tick"
    assert restored.schema_version == 1
    assert restored.symbol == "EURUSD"
    assert restored.occurred_at.tzinfo is not None

    with pytest.raises(ValidationError):
        MarketTickV1.model_validate({**event.model_dump(), "unexpected": True})


def test_signal_and_order_contracts_preserve_correlation_and_causation() -> None:
    signal = TradeSignalV1.create(
        source="analysis-worker",
        correlation_id="corr-0002",
        causation_id="tick-0002",
        signal_id="strategy:EURUSD:0002",
        strategy="ORB_FVG_ENGULFING",
        symbol="EURUSD",
        direction="LONG",
        entry=1.1,
        stop=1.095,
        take_profit=1.11,
        position_size=0.01,
        confidence="standard",
    )
    command = OrderCommandV1.from_signal(
        signal,
        source="execution-policy",
        expert_id="orb-v1",
    )

    assert command.correlation_id == signal.correlation_id
    assert command.causation_id == signal.event_id
    assert command.side == "BUY"
    assert command.idempotency_key == signal.signal_id


def test_kafka_defaults_protect_delivery_semantics() -> None:
    settings = KafkaSettings(
        bootstrap_servers="kafka:9092",
        client_id="contract-test",
    )

    producer = settings.producer_config()
    consumer = settings.consumer_config(group_id="storage-v1")

    assert producer["enable.idempotence"] is True
    assert producer["acks"] == "all"
    assert consumer["enable.auto.commit"] is False
    assert consumer["enable.auto.offset.store"] is False


def test_message_is_committed_only_after_successful_processing() -> None:
    consumer = FakeConsumer()
    message = FakeMessage(make_tick().model_dump_json().encode("utf-8"))
    handled: list[str] = []

    async def handler(event: MarketTickV1) -> None:
        handled.append(event.event_id)

    processor = ReliableMessageProcessor(
        consumer=consumer,
        event_model=MarketTickV1,
        handler=handler,
        dead_letter_topic="market.ticks.dlq.v1",
    )

    outcome = asyncio.run(processor.process(message))

    assert outcome == "processed"
    assert handled == [make_tick().model_validate_json(message.value()).event_id]
    assert consumer.committed == [message]


def test_failed_processing_is_not_committed_for_retry() -> None:
    consumer = FakeConsumer()
    message = FakeMessage(make_tick().model_dump_json().encode("utf-8"))

    async def failing_handler(_: MarketTickV1) -> None:
        raise RuntimeError("temporary database outage")

    processor = ReliableMessageProcessor(
        consumer=consumer,
        event_model=MarketTickV1,
        handler=failing_handler,
        dead_letter_topic="market.ticks.dlq.v1",
    )

    outcome = asyncio.run(processor.process(message))

    assert outcome == "retry"
    assert consumer.committed == []


def test_invalid_event_reaches_dlq_before_offset_is_committed() -> None:
    consumer = FakeConsumer()
    dlq = FakeDeadLetterPublisher()
    message = FakeMessage(b'{"schema_version":99}')

    async def handler(_: MarketTickV1) -> None:
        raise AssertionError("invalid messages must never reach the handler")

    processor = ReliableMessageProcessor(
        consumer=consumer,
        event_model=MarketTickV1,
        handler=handler,
        dead_letter_topic="market.ticks.dlq.v1",
        dead_letter_publisher=dlq,
    )

    outcome = asyncio.run(processor.process(message))

    assert outcome == "dead_lettered"
    assert dlq.messages[0][0] == "market.ticks.dlq.v1"
    assert consumer.committed == [message]


def test_readiness_requires_every_registered_dependency() -> None:
    health = ServiceHealth("analysis-worker")
    health.register_dependency("kafka")
    health.register_dependency("market-data")
    health.mark_started()

    assert health.liveness()["status"] == "alive"
    assert health.readiness()["status"] == "not_ready"

    health.set_dependency("kafka", ready=True)
    health.set_dependency("market-data", ready=True)

    assert health.readiness()["status"] == "ready"
