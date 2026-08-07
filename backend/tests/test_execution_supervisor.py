from __future__ import annotations

import asyncio

from services.execution_gateway.supervisor import ExecutionGatewaySupervisor
from services.platform.health import ServiceHealth


class FakeService:
    def __init__(self, *, mode="paper", connected=True) -> None:
        self.mode = mode
        self.connected = connected
        self.reconciliations = 0

    def get_status(self, *, include_account=False):
        return {
            "package_available": True,
            "connected": self.connected,
            "execution_mode": self.mode,
        }

    async def reconcile_orders(self, limit):
        self.reconciliations += 1
        return {"checked": 1, "changed": 1, "limit": limit}


def test_supervisor_reconciles_connected_active_gateway() -> None:
    service = FakeService()
    supervisor = ExecutionGatewaySupervisor(
        execution_service=service,
        health=ServiceHealth("execution-gateway"),
        reconciliation_limit=50,
    )

    result = asyncio.run(supervisor.run_once())

    assert result["changed"] == 1
    assert service.reconciliations == 1
    assert supervisor.last_reconciliation is not None


def test_supervisor_does_not_connect_or_reconcile_disabled_gateway() -> None:
    service = FakeService(mode="disabled", connected=False)
    supervisor = ExecutionGatewaySupervisor(
        execution_service=service,
        health=ServiceHealth("execution-gateway"),
    )

    result = asyncio.run(supervisor.run_once())

    assert result["status"] == "idle"
    assert service.reconciliations == 0
