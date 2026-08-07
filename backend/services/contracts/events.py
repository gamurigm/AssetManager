"""Strict, versioned event contracts shared by service boundaries.

Only data contracts live here.  This module deliberately has no Kafka,
database, broker, or FastAPI dependencies.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal, Optional
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator


class EventEnvelope(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    event_id: str = Field(min_length=8, max_length=64)
    event_type: str = Field(min_length=3, max_length=64)
    schema_version: int = Field(ge=1)
    occurred_at: datetime
    source: str = Field(min_length=2, max_length=64)
    correlation_id: str = Field(min_length=3, max_length=128)
    causation_id: Optional[str] = Field(default=None, min_length=3, max_length=128)

    @field_validator("occurred_at")
    @classmethod
    def require_timezone(cls, value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("occurred_at must include a timezone")
        return value.astimezone(timezone.utc)

    @staticmethod
    def new_event_id() -> str:
        return uuid4().hex


class MarketTickV1(EventEnvelope):
    event_type: Literal["market.tick"] = "market.tick"
    schema_version: Literal[1] = 1
    symbol: str = Field(min_length=1, max_length=32)
    price: float = Field(gt=0)
    volume: float = Field(default=0, ge=0)
    observed_at: datetime

    @field_validator("symbol")
    @classmethod
    def normalize_symbol(cls, value: str) -> str:
        return value.strip().upper()

    @field_validator("observed_at")
    @classmethod
    def require_observed_timezone(cls, value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("observed_at must include a timezone")
        return value.astimezone(timezone.utc)

    @classmethod
    def create(
        cls,
        *,
        source: str,
        symbol: str,
        price: float,
        volume: float = 0,
        observed_at: datetime,
        correlation_id: Optional[str] = None,
        causation_id: Optional[str] = None,
    ) -> "MarketTickV1":
        event_id = cls.new_event_id()
        return cls(
            event_id=event_id,
            occurred_at=datetime.now(timezone.utc),
            source=source,
            correlation_id=correlation_id or event_id,
            causation_id=causation_id,
            symbol=symbol,
            price=price,
            volume=volume,
            observed_at=observed_at,
        )


class TradeSignalV1(EventEnvelope):
    event_type: Literal["trade.signal"] = "trade.signal"
    schema_version: Literal[1] = 1
    signal_id: str = Field(min_length=8, max_length=128)
    strategy: str = Field(min_length=2, max_length=64)
    symbol: str = Field(min_length=1, max_length=32)
    direction: Literal["LONG", "SHORT"]
    entry: float = Field(gt=0)
    stop: float = Field(gt=0)
    take_profit: float = Field(gt=0)
    position_size: float = Field(gt=0)
    confidence: str = Field(min_length=1, max_length=32)

    @field_validator("symbol", "strategy")
    @classmethod
    def normalize_uppercase(cls, value: str) -> str:
        return value.strip().upper()

    @classmethod
    def create(cls, **payload) -> "TradeSignalV1":
        event_id = cls.new_event_id()
        return cls(
            event_id=event_id,
            occurred_at=datetime.now(timezone.utc),
            **payload,
        )


class OrderCommandV1(EventEnvelope):
    event_type: Literal["order.command"] = "order.command"
    schema_version: Literal[1] = 1
    idempotency_key: str = Field(min_length=8, max_length=128)
    signal_id: str = Field(min_length=8, max_length=128)
    expert_id: str = Field(min_length=2, max_length=64)
    symbol: str = Field(min_length=1, max_length=32)
    side: Literal["BUY", "SELL"]
    volume: float = Field(gt=0)
    stop_loss: Optional[float] = Field(default=None, gt=0)
    take_profit: Optional[float] = Field(default=None, gt=0)

    @classmethod
    def from_signal(
        cls,
        signal: TradeSignalV1,
        *,
        source: str,
        expert_id: str,
    ) -> "OrderCommandV1":
        return cls(
            event_id=cls.new_event_id(),
            occurred_at=datetime.now(timezone.utc),
            source=source,
            correlation_id=signal.correlation_id,
            causation_id=signal.event_id,
            idempotency_key=signal.signal_id,
            signal_id=signal.signal_id,
            expert_id=expert_id,
            symbol=signal.symbol,
            side="BUY" if signal.direction == "LONG" else "SELL",
            volume=signal.position_size,
            stop_loss=signal.stop,
            take_profit=signal.take_profit,
        )


class DeadLetterEventV1(EventEnvelope):
    event_type: Literal["system.dead_letter"] = "system.dead_letter"
    schema_version: Literal[1] = 1
    destination_topic: str = Field(min_length=3, max_length=255)
    original_payload: str
    reason: str = Field(min_length=1, max_length=4_000)

    @classmethod
    def create(
        cls,
        *,
        destination_topic: str,
        original_payload: str,
        reason: str,
    ) -> "DeadLetterEventV1":
        event_id = cls.new_event_id()
        return cls(
            event_id=event_id,
            occurred_at=datetime.now(timezone.utc),
            source="kafka-message-processor",
            correlation_id=event_id,
            destination_topic=destination_topic,
            original_payload=original_payload,
            reason=reason,
        )
