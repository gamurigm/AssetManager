"""Explicit feature ownership for the public API process."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Mapping


def _as_bool(value: str | None, *, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class APIRuntimePolicy:
    kafka_fanout_enabled: bool
    scheduler_enabled: bool
    broker_connections_enabled: bool

    @classmethod
    def from_mapping(cls, values: Mapping[str, str]) -> "APIRuntimePolicy":
        return cls(
            kafka_fanout_enabled=_as_bool(
                values.get("API_ENABLE_KAFKA_FANOUT"), default=True
            ),
            scheduler_enabled=_as_bool(
                values.get("API_ENABLE_SCHEDULER"), default=False
            ),
            broker_connections_enabled=_as_bool(
                values.get("API_ENABLE_BROKER_CONNECTIONS"), default=False
            ),
        )

    @classmethod
    def from_env(cls) -> "APIRuntimePolicy":
        return cls.from_mapping(os.environ)
