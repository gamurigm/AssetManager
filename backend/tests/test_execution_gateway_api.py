from __future__ import annotations

import time

from fastapi.testclient import TestClient
from pydantic import ValidationError

from services.execution_gateway.main import ExecutionOrderRequest, create_app


class FakeExecutionService:
    execution_mode = "paper"

    def __init__(self) -> None:
        self.intents = []
        self.kill_switch = False

    def verify_gateway_token(self, candidate):
        return candidate == "test-token"

    def get_status(self, *, include_account=False):
        return {
            "connected": True,
            "package_available": True,
            "execution_mode": "paper",
            "account": {"login_masked": "***1234"} if include_account else None,
        }

    async def connect(self):
        return self.get_status(include_account=True)

    async def preview_order(self, intent):
        self.intents.append(intent)
        return {"state": "previewed", "signal_id": intent.signal_id}

    async def execute_order(self, intent):
        self.intents.append(intent)
        return {"state": "filled", "signal_id": intent.signal_id}

    async def positions(self):
        return []

    def recent_orders(self, limit):
        return []

    async def reconcile_orders(self, limit):
        return {"checked": 0, "changed": 0}

    def activate_kill_switch(self, reason):
        self.kill_switch = True
        return {"active": True, "reason": reason}

    def reset_kill_switch(self, *, confirm):
        assert confirm == "RESET"
        self.kill_switch = False
        return {"active": False}


def order_payload() -> dict:
    return {
        "signal_id": "signal-api-0001",
        "expert_id": "orb-v1",
        "symbol": "EURUSD",
        "side": "BUY",
        "volume": 0.01,
        "observed_at_epoch": int(time.time()),
        "sl": 1.09,
        "tp": 1.12,
    }


def test_gateway_exposes_health_and_requires_token_for_execution() -> None:
    app = create_app(execution_service=FakeExecutionService())

    with TestClient(app) as client:
        assert client.get("/health/live").status_code == 200
        assert client.get("/health/ready").status_code == 200
        assert client.post("/v1/orders", json=order_payload()).status_code == 401

        response = client.post(
            "/v1/orders",
            json=order_payload(),
            headers={"X-MT5-Gateway-Token": "test-token"},
        )

    assert response.status_code == 200
    assert response.json()["state"] == "filled"


def test_execution_contract_rejects_unknown_bypass_fields() -> None:
    try:
        ExecutionOrderRequest(**{**order_payload(), "bypass_risk": True})
    except ValidationError:
        pass
    else:
        raise AssertionError("unknown execution controls must be rejected")


def test_gateway_exposes_authenticated_durable_kill_switch() -> None:
    service = FakeExecutionService()
    app = create_app(execution_service=service)

    with TestClient(app) as client:
        activated = client.post(
            "/v1/kill-switch",
            json={"reason": "operator emergency stop"},
            headers={"X-MT5-Gateway-Token": "test-token"},
        )
        reset = client.post(
            "/v1/kill-switch/reset",
            json={"confirm": "RESET"},
            headers={"X-MT5-Gateway-Token": "test-token"},
        )

    assert activated.status_code == 200
    assert activated.json()["active"] is True
    assert reset.status_code == 200
    assert reset.json()["active"] is False
