"""Kafka defaults that favor durability and explicit processing semantics."""

from __future__ import annotations

import inspect
from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Optional, Protocol, Type

from pydantic import BaseModel, ValidationError


class ConsumerPort(Protocol):
    def commit(self, *, message: Any, asynchronous: bool) -> Any: ...


class DeadLetterPublisherPort(Protocol):
    def publish(self, *, topic: str, payload: bytes, reason: str) -> None: ...


@dataclass(frozen=True)
class KafkaSettings:
    bootstrap_servers: str
    client_id: str

    def producer_config(self) -> dict[str, Any]:
        return {
            "bootstrap.servers": self.bootstrap_servers,
            "client.id": self.client_id,
            "enable.idempotence": True,
            "acks": "all",
            "retries": 2_147_483_647,
            "delivery.timeout.ms": 30_000,
        }

    def consumer_config(self, *, group_id: str) -> dict[str, Any]:
        return {
            "bootstrap.servers": self.bootstrap_servers,
            "client.id": self.client_id,
            "group.id": group_id,
            "auto.offset.reset": "earliest",
            "enable.auto.commit": False,
            "enable.auto.offset.store": False,
        }


class ReliableMessageProcessor:
    """Validate, process, then commit; transient handler failures remain replayable."""

    def __init__(
        self,
        *,
        consumer: ConsumerPort,
        event_model: Type[BaseModel],
        handler: Callable[[Any], Any | Awaitable[Any]],
        dead_letter_topic: str,
        dead_letter_publisher: Optional[DeadLetterPublisherPort] = None,
    ) -> None:
        self._consumer = consumer
        self._event_model = event_model
        self._handler = handler
        self._dead_letter_topic = dead_letter_topic
        self._dead_letter_publisher = dead_letter_publisher

    async def process(self, message: Any) -> str:
        payload = message.value()
        try:
            event = self._event_model.model_validate_json(payload)
        except (ValidationError, ValueError, TypeError) as exc:
            if self._dead_letter_publisher is None:
                return "retry"
            self._dead_letter_publisher.publish(
                topic=self._dead_letter_topic,
                payload=payload,
                reason=str(exc),
            )
            self._consumer.commit(message=message, asynchronous=False)
            return "dead_lettered"

        try:
            result = self._handler(event)
            if inspect.isawaitable(result):
                await result
        except Exception:
            return "retry"

        self._consumer.commit(message=message, asynchronous=False)
        return "processed"


class KafkaPublishError(RuntimeError):
    pass


class KafkaJsonPublisher:
    """Synchronous acknowledgement boundary used by transactional outboxes."""

    def __init__(self, producer: Any, *, timeout_seconds: float = 10.0) -> None:
        self._producer = producer
        self._timeout_seconds = timeout_seconds

    def publish_event(self, *, topic: str, event: BaseModel, key: str) -> None:
        delivery_error: list[Any] = []

        def on_delivery(error: Any, _message: Any) -> None:
            if error is not None:
                delivery_error.append(error)

        self._producer.produce(
            topic=topic,
            key=key.encode("utf-8"),
            value=event.model_dump_json().encode("utf-8"),
            callback=on_delivery,
        )
        remaining = self._producer.flush(self._timeout_seconds)
        if remaining:
            raise KafkaPublishError(
                f"Kafka delivery timed out with {remaining} message(s) pending"
            )
        if delivery_error:
            raise KafkaPublishError(str(delivery_error[0]))


class KafkaDeadLetterPublisher:
    def __init__(self, publisher: KafkaJsonPublisher) -> None:
        self._publisher = publisher

    def publish(self, *, topic: str, payload: bytes, reason: str) -> None:
        from services.contracts.events import DeadLetterEventV1

        event = DeadLetterEventV1.create(
            destination_topic=topic,
            original_payload=payload.decode("utf-8", errors="replace"),
            reason=reason,
        )
        self._publisher.publish_event(topic=topic, event=event, key="invalid")
