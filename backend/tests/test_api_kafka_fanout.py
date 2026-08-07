from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import patch

from app.services.kafka_consumer_service import KafkaConsumerService
from services.contracts.events import MarketTickV1


class FakeSocketServer:
    def __init__(self) -> None:
        self.emitted = []

    async def emit(self, name, payload, *, room):
        self.emitted.append((name, payload, room))


def test_each_api_replica_uses_an_independent_fanout_group() -> None:
    with patch.dict(
        "os.environ",
        {
            "API_INSTANCE_ID": "api-replica-a",
            "KAFKA_BOOTSTRAP_SERVERS": "kafka:9092",
        },
    ):
        service = KafkaConsumerService()

    assert service.config["group.id"] == "api-fanout-api-replica-a"
    assert service.config["enable.auto.commit"] is False
    assert service.config["bootstrap.servers"] == "kafka:9092"


def test_fanout_uses_validated_v1_event_and_symbol_room() -> None:
    service = KafkaConsumerService()
    socket = FakeSocketServer()
    service.sio = socket
    event = MarketTickV1.create(
        source="unit-test",
        symbol="SPY",
        price=550,
        volume=1,
        observed_at=datetime.now(timezone.utc),
    )

    asyncio.run(service.emit_tick(event))

    name, payload, room = socket.emitted[0]
    assert name == "price_update"
    assert room == "SPY"
    assert payload["eventId"] == event.event_id
    assert payload["price"] == 550
