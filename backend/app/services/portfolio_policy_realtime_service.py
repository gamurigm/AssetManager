from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List, Optional

from app.core.logging import logger

from .portfolio_policy_service import portfolio_policy_service


class PortfolioPolicyRealtimeService:
    def __init__(self, policy_service: Any | None = None) -> None:
        self._sio = None
        self._policy_service = policy_service or portfolio_policy_service
        self._subscriptions: Dict[str, Dict[str, Any]] = {}

    def configure(self, sio) -> None:
        self._sio = sio

    def clear_client(self, sid: str) -> None:
        self._subscriptions.pop(sid, None)

    async def subscribe(self, sid: str, payload: Optional[Dict[str, Any]] = None) -> None:
        request = payload or {}
        portfolio_id = str(request.get("portfolio_id") or "main")
        holdings = self._normalize_holdings(request.get("holdings") or [])
        params = {
            "benchmark": str(request.get("benchmark") or "SPY").upper(),
            "lookback_days": int(request.get("lookback_days") or 252),
            "risk_aversion": float(request.get("risk_aversion") or 0.35),
            "turnover_penalty": float(request.get("turnover_penalty") or 0.08),
            "max_weight": float(request.get("max_weight") or 0.35),
            "gross_limit": float(request.get("gross_limit") or 1.0),
        }

        self._subscriptions[sid] = {
            "portfolio_id": portfolio_id,
            "holdings": holdings,
            "params": params,
            "tracked_symbols": {holding["symbol"] for holding in holdings if holding.get("symbol")},
            "last_snapshot": None,
        }
        logger.info(f"[PolicySocket] Client {sid} subscribed for portfolio {portfolio_id} with {len(holdings)} holdings")
        await self._emit_snapshot(sid, reason="subscribe")

    async def unsubscribe(self, sid: str) -> None:
        if sid in self._subscriptions:
            logger.info(f"[PolicySocket] Client {sid} unsubscribed from portfolio policy stream")
        self.clear_client(sid)

    async def handle_price_update(self, payload: Dict[str, Any]) -> None:
        symbol = str(payload.get("symbol") or "").upper()
        price = payload.get("price")
        if not symbol or price is None:
            return

        impacted_sids = [
            sid
            for sid, subscription in self._subscriptions.items()
            if symbol in subscription.get("tracked_symbols", set())
        ]
        if not impacted_sids:
            return

        for sid in impacted_sids:
            subscription = self._subscriptions.get(sid)
            if not subscription:
                continue

            changed = False
            for holding in subscription["holdings"]:
                if holding.get("symbol") != symbol:
                    continue
                holding["price"] = float(price)
                if "change" in payload:
                    holding["change"] = payload.get("change", holding.get("change", 0))
                if "changePercent" in payload:
                    holding["changePercent"] = payload.get("changePercent", holding.get("changePercent", 0))
                if payload.get("source"):
                    holding["source"] = payload["source"]
                changed = True

            if changed:
                await self._emit_snapshot(sid, reason="price_update", changed_symbol=symbol)

    def _normalize_holdings(self, holdings: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        normalized: List[Dict[str, Any]] = []
        for raw_holding in holdings:
            symbol = str(raw_holding.get("symbol") or "").strip().upper()
            shares = float(raw_holding.get("shares", 0) or 0)
            if not symbol or shares == 0:
                continue

            normalized.append(
                {
                    "symbol": symbol,
                    "name": str(raw_holding.get("name") or symbol),
                    "shares": shares,
                    "price": float(raw_holding.get("price") or raw_holding.get("entryPrice") or 0),
                    "entryPrice": float(raw_holding.get("entryPrice") or raw_holding.get("price") or 0),
                    "factor": float(raw_holding.get("factor") or 1.0),
                    "sector": str(raw_holding.get("sector") or "Unknown"),
                    "type": str(raw_holding.get("type") or "asset"),
                    "purchaseDate": raw_holding.get("purchaseDate"),
                    "source": raw_holding.get("source", "Live"),
                    "change": float(raw_holding.get("change") or 0),
                    "changePercent": float(raw_holding.get("changePercent") or 0),
                }
            )
        return normalized

    async def _emit_snapshot(self, sid: str, reason: str, changed_symbol: str | None = None) -> None:
        if not self._sio:
            return

        subscription = self._subscriptions.get(sid)
        if not subscription:
            return

        snapshot = self._policy_service.build_policy_snapshot(
            portfolio_id=subscription["portfolio_id"],
            holdings=deepcopy(subscription["holdings"]),
            benchmark=subscription["params"]["benchmark"],
            lookback_days=subscription["params"]["lookback_days"],
            risk_aversion=subscription["params"]["risk_aversion"],
            turnover_penalty=subscription["params"]["turnover_penalty"],
            max_weight=subscription["params"]["max_weight"],
            gross_limit=subscription["params"]["gross_limit"],
        )

        if "error" in snapshot:
            await self._sio.emit(
                "portfolio_policy_error",
                {
                    "portfolio_id": subscription["portfolio_id"],
                    "error": str(snapshot["error"]),
                    "reason": reason,
                    "changed_symbol": changed_symbol,
                },
                to=sid,
            )
            return

        snapshot["stream"] = {
            "reason": reason,
            "changed_symbol": changed_symbol,
            "tracked_symbols": sorted(subscription.get("tracked_symbols", set())),
            "transport": "socketio",
        }

        previous_snapshot = subscription.get("last_snapshot")
        subscription["last_snapshot"] = snapshot

        if reason == "price_update" and previous_snapshot is not None:
            delta_payload = self._build_delta(previous_snapshot, snapshot)
            await self._sio.emit("portfolio_policy_delta", delta_payload, to=sid)
            return

        await self._sio.emit("portfolio_policy_update", snapshot, to=sid)

    def _build_delta(self, previous_snapshot: Dict[str, Any], snapshot: Dict[str, Any]) -> Dict[str, Any]:
        previous_allocations = {
            allocation["symbol"]: allocation
            for allocation in previous_snapshot.get("allocations", [])
            if allocation.get("symbol")
        }
        changed_allocations = []
        changed_symbols = []

        for allocation in snapshot.get("allocations", []):
            symbol = allocation.get("symbol")
            if not symbol:
                continue
            if previous_allocations.get(symbol) != allocation:
                changed_allocations.append(allocation)
                changed_symbols.append(symbol)

        return {
            "portfolio_id": snapshot.get("portfolio_id"),
            "generated_at": snapshot.get("generated_at"),
            "summary": snapshot.get("summary"),
            "objective": snapshot.get("objective"),
            "allocations": changed_allocations,
            "stream": {
                **(snapshot.get("stream") or {}),
                "transport": "socketio-delta",
                "changed_symbols": changed_symbols,
            },
        }


portfolio_policy_realtime_service = PortfolioPolicyRealtimeService()