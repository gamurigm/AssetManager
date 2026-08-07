"""Thread-safe liveness and readiness state for long-running workers."""

from __future__ import annotations

from datetime import datetime, timezone
from threading import RLock
from typing import Optional


class ServiceHealth:
    def __init__(self, service_name: str) -> None:
        self.service_name = service_name
        self._started = False
        self._started_at: Optional[datetime] = None
        self._dependencies: dict[str, dict[str, object]] = {}
        self._lock = RLock()

    def register_dependency(self, name: str) -> None:
        with self._lock:
            self._dependencies.setdefault(
                name,
                {"ready": False, "detail": "not checked"},
            )

    def mark_started(self) -> None:
        with self._lock:
            self._started = True
            self._started_at = datetime.now(timezone.utc)

    def mark_stopped(self) -> None:
        with self._lock:
            self._started = False

    def set_dependency(self, name: str, *, ready: bool, detail: str = "") -> None:
        with self._lock:
            if name not in self._dependencies:
                self.register_dependency(name)
            self._dependencies[name] = {
                "ready": bool(ready),
                "detail": detail or ("ready" if ready else "unavailable"),
            }

    def liveness(self) -> dict[str, object]:
        with self._lock:
            return {
                "service": self.service_name,
                "status": "alive" if self._started else "starting",
                "started_at": self._started_at.isoformat() if self._started_at else None,
            }

    def readiness(self) -> dict[str, object]:
        with self._lock:
            ready = self._started and all(
                bool(item["ready"]) for item in self._dependencies.values()
            )
            return {
                "service": self.service_name,
                "status": "ready" if ready else "not_ready",
                "dependencies": {
                    key: dict(value) for key, value in self._dependencies.items()
                },
            }
