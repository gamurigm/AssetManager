"""Kafka-to-Socket.IO fanout owned by the public API/BFF."""

from __future__ import annotations

import asyncio
import os
import socket
from typing import Any

from confluent_kafka import Consumer, Producer, TopicPartition

from app.core.logging import logger
from services.contracts.events import MarketTickV1
from services.platform.kafka import (
    KafkaDeadLetterPublisher,
    KafkaJsonPublisher,
    KafkaSettings,
    ReliableMessageProcessor,
)


class KafkaConsumerService:
    TOPIC = "market.ticks.v1"
    DLQ_TOPIC = "market.ticks.dlq.v1"

    def __init__(self) -> None:
        instance_id = os.getenv("API_INSTANCE_ID", socket.gethostname()).strip()
        bootstrap_servers = os.getenv(
            "KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"
        )
        kafka = KafkaSettings(
            bootstrap_servers=bootstrap_servers,
            client_id=f"api-fanout-{instance_id}",
        )
        self.config = kafka.consumer_config(
            group_id=f"api-fanout-{instance_id}"
        )
        # WebSocket fanout is live state; historical ticks are hydrated via HTTP.
        self.config["auto.offset.reset"] = "latest"
        self._producer_config = kafka.producer_config()
        self.consumer: Consumer | None = None
        self.producer: Producer | None = None
        self.sio: Any = None
        self._running = False
        self._task: asyncio.Task | None = None
        self._processor: ReliableMessageProcessor | None = None
        self.last_error: str | None = None

    @property
    def is_running(self) -> bool:
        return self._running and self._task is not None and not self._task.done()

    def start(self, sio: Any) -> None:
        if self.is_running:
            return
        self.sio = sio
        self.consumer = Consumer(self.config)
        self.producer = Producer(self._producer_config)
        dead_letter = KafkaDeadLetterPublisher(KafkaJsonPublisher(self.producer))
        self._processor = ReliableMessageProcessor(
            consumer=self.consumer,
            event_model=MarketTickV1,
            handler=self.emit_tick,
            dead_letter_topic=self.DLQ_TOPIC,
            dead_letter_publisher=dead_letter,
        )
        self.consumer.subscribe([self.TOPIC])
        self._running = True
        self.last_error = None
        self._task = asyncio.get_running_loop().create_task(self._consume_loop())
        logger.info("[Kafka Fanout] Listening to %s", self.TOPIC)

    def stop(self) -> None:
        self._running = False
        if self._task:
            self._task.cancel()
        if self.consumer:
            self.consumer.close()
            self.consumer = None
        if self.producer:
            self.producer.flush(5)
            self.producer = None
        logger.info("[Kafka Fanout] Stopped")

    async def emit_tick(self, tick: MarketTickV1) -> None:
        if self.sio is None:
            return
        frontend_payload = {
            "eventId": tick.event_id,
            "correlationId": tick.correlation_id,
            "symbol": tick.symbol,
            "price": tick.price,
            "volume": tick.volume,
            "change": 0.0,
            "changePercent": 0.0,
            "timestamp": tick.observed_at.timestamp(),
            "source": f"{tick.source} -> Kafka",
            "live": True,
        }
        await self.sio.emit("price_update", frontend_payload, room=tick.symbol)

    async def _consume_loop(self) -> None:
        assert self.consumer is not None
        assert self._processor is not None
        while self._running:
            try:
                message = await asyncio.to_thread(self.consumer.poll, 0.5)
                if message is None:
                    continue
                if message.error():
                    self.last_error = str(message.error())
                    logger.warning("[Kafka Fanout] %s", message.error())
                    await asyncio.sleep(1)
                    continue

                outcome = await self._processor.process(message)
                if outcome == "retry":
                    self.last_error = "tick processing failed; retrying"
                    self.consumer.seek(
                        TopicPartition(
                            message.topic(),
                            message.partition(),
                            message.offset(),
                        )
                    )
                    await asyncio.sleep(0.25)
                else:
                    self.last_error = None
            except asyncio.CancelledError:
                break
            except Exception as exc:
                self.last_error = str(exc)
                logger.exception("[Kafka Fanout] Unexpected error: %s", exc)
                await asyncio.sleep(1)


kafka_consumer_service = KafkaConsumerService()
