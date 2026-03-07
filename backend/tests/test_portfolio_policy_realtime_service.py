import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.services.portfolio_policy_realtime_service import PortfolioPolicyRealtimeService


class _FakePolicyService:
    def build_policy_snapshot(self, portfolio_id: str, holdings, **kwargs):
        return {
            "portfolio_id": portfolio_id,
            "generated_at": "2026-03-07T00:00:00Z",
            "summary": {
                "rebalance_required": False,
                "confidence_pct": 80.0,
                "coverage_percent": 100.0,
                "high_conviction_symbols": [holding["symbol"] for holding in holdings[:1]],
                "target_cash_buffer_pct": 0.0,
            },
            "objective": {
                "current_expected_return_pct": 10.0,
                "target_expected_return_pct": 12.0,
                "ev_delta_pct": 2.0,
                "current_risk_pct": 5.0,
                "target_risk_pct": 4.0,
                "risk_delta_pct": -1.0,
                "realized_trade_ev": 0.0,
            },
            "allocations": [
                {
                    "symbol": holding["symbol"],
                    "price": holding["price"],
                    "factor": holding.get("factor", 1.0),
                    "target_notional": holding["price"] * holding["shares"],
                    "delta_shares": 0.0,
                    "current_weight_pct": 50.0,
                    "target_weight_pct": 50.0,
                    "weight_delta_pct": 0.0,
                    "action": "HOLD",
                }
                for holding in holdings
            ],
        }


class _FakeSio:
    def __init__(self):
        self.events = []

    async def emit(self, event, payload, to=None):
        self.events.append({"event": event, "payload": payload, "to": to})


def test_realtime_policy_subscription_emits_initial_and_price_updates() -> None:
    async def _run() -> None:
        fake_sio = _FakeSio()
        service = PortfolioPolicyRealtimeService(policy_service=_FakePolicyService())
        service.configure(fake_sio)

        await service.subscribe(
            "sid-1",
            {
                "portfolio_id": "main",
                "holdings": [
                    {"symbol": "AAPL", "name": "Apple", "shares": 2, "price": 100, "entryPrice": 90, "factor": 1.0, "sector": "Tech", "type": "stock"},
                    {"symbol": "MSFT", "name": "Microsoft", "shares": 1, "price": 200, "entryPrice": 180, "factor": 1.0, "sector": "Tech", "type": "stock"},
                ],
            },
        )
        await service.handle_price_update({"symbol": "AAPL", "price": 123.45, "change": 1.2, "changePercent": 0.98, "source": "ibkr"})

        assert len(fake_sio.events) == 2
        assert fake_sio.events[0]["event"] == "portfolio_policy_update"
        assert fake_sio.events[0]["payload"]["stream"]["reason"] == "subscribe"
        assert fake_sio.events[1]["event"] == "portfolio_policy_delta"
        assert fake_sio.events[1]["payload"]["stream"]["reason"] == "price_update"
        assert fake_sio.events[1]["payload"]["stream"]["changed_symbol"] == "AAPL"
        updated_aapl = next(item for item in fake_sio.events[1]["payload"]["allocations"] if item["symbol"] == "AAPL")
        assert updated_aapl["price"] == 123.45

    asyncio.run(_run())


def test_realtime_policy_clear_client_stops_future_emits() -> None:
    async def _run() -> None:
        fake_sio = _FakeSio()
        service = PortfolioPolicyRealtimeService(policy_service=_FakePolicyService())
        service.configure(fake_sio)

        await service.subscribe(
            "sid-2",
            {"portfolio_id": "main", "holdings": [{"symbol": "NVDA", "name": "NVIDIA", "shares": 1, "price": 500, "entryPrice": 450, "factor": 1.0, "sector": "Tech", "type": "stock"}]},
        )
        service.clear_client("sid-2")
        await service.handle_price_update({"symbol": "NVDA", "price": 510.0})

        assert len(fake_sio.events) == 1
        assert fake_sio.events[0]["payload"]["stream"]["reason"] == "subscribe"

    asyncio.run(_run())