"""Periodic broker-state reconciliation owned by the execution process."""

from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from typing import Any

from services.platform.health import ServiceHealth


class ExecutionGatewaySupervisor:
    def __init__(
        self,
        *,
        execution_service: Any,
        health: ServiceHealth,
        interval_seconds: float = 30.0,
        reconciliation_limit: int = 200,
    ) -> None:
        self.execution_service = execution_service
        self.health = health
        self.interval_seconds = max(1.0, interval_seconds)
        self.reconciliation_limit = max(1, min(reconciliation_limit, 500))
        self.last_reconciliation: dict[str, Any] | None = None
        self.last_error: str | None = None
        self._stop_event = asyncio.Event()

    async def run_once(self) -> dict[str, Any]:
        status = await asyncio.to_thread(
            self.execution_service.get_status,
            include_account=False,
        )
        package_available = bool(status.get("package_available"))
        self.health.set_dependency(
            "mt5-adapter",
            ready=package_available,
            detail="adapter available" if package_available else "adapter unavailable",
        )
        mode = str(status.get("execution_mode", "disabled"))
        if mode not in {"paper", "live"} or not status.get("connected"):
            return {"status": "idle", "mode": mode}

        result = await self.execution_service.reconcile_orders(
            self.reconciliation_limit
        )
        self.last_reconciliation = {
            **result,
            "at": datetime.now(timezone.utc).isoformat(),
        }
        self.last_error = None
        return result

    async def run(self) -> None:
        while not self._stop_event.is_set():
            try:
                await self.run_once()
            except Exception as exc:
                self.last_error = str(exc)
                self.health.set_dependency(
                    "mt5-adapter", ready=False, detail=self.last_error
                )
            try:
                await asyncio.wait_for(
                    self._stop_event.wait(), timeout=self.interval_seconds
                )
            except asyncio.TimeoutError:
                pass

    def stop(self) -> None:
        self._stop_event.set()
