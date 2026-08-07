"""Safe MetaTrader 5 terminal adapter for Expert Advisor execution.

The official MetaTrader5 Python package is synchronous.  Public methods use
asyncio.to_thread and all native calls are serialized with an RLock because a
single local terminal/account is the source of truth.
"""

from __future__ import annotations

import asyncio
import hmac
import importlib
import math
import os
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Optional

from .mt5_gateway_journal import MT5GatewayJournal, mt5_gateway_journal


class MT5Error(RuntimeError):
    """Base error exposed by the MT5 gateway."""


class MT5ConfigurationError(MT5Error):
    pass


class MT5ValidationError(MT5Error):
    pass


class MT5ExecutionBlocked(MT5Error):
    pass


@dataclass(frozen=True)
class MT5OrderIntent:
    signal_id: str
    expert_id: str
    symbol: str
    side: str
    volume: float
    observed_at_epoch: int
    sl: Optional[float] = None
    tp: Optional[float] = None
    deviation: Optional[int] = None
    magic: Optional[int] = None
    comment: str = "AssetManager EA"
    confirm_live: bool = False


def _as_dict(value: Any) -> Dict[str, Any]:
    if value is None:
        return {}
    if hasattr(value, "_asdict"):
        raw = value._asdict()
    elif isinstance(value, dict):
        raw = value
    else:
        return {"value": str(value)}
    converted: Dict[str, Any] = {}
    for key, item in raw.items():
        if hasattr(item, "_asdict"):
            converted[key] = _as_dict(item)
        elif isinstance(item, (str, int, float, bool)) or item is None:
            converted[key] = item
        else:
            converted[key] = str(item)
    return converted


class MT5Service:
    VALID_MODES = {"disabled", "paper", "live"}

    def __init__(
        self,
        *,
        mt5_module: Any = None,
        journal: Optional[MT5GatewayJournal] = None,
    ) -> None:
        self._mt5 = mt5_module
        self._journal = journal or mt5_gateway_journal
        self._lock = threading.RLock()
        self._connected = False
        self._last_error: Optional[str] = None

    @property
    def execution_mode(self) -> str:
        mode = os.getenv("MT5_EXECUTION_MODE", "disabled").strip().lower()
        return mode if mode in self.VALID_MODES else "disabled"

    @staticmethod
    def _csv_set(name: str) -> set[str]:
        return {
            item.strip().upper()
            for item in os.getenv(name, "").split(",")
            if item.strip()
        }

    def verify_gateway_token(self, candidate: Optional[str]) -> bool:
        configured = os.getenv("MT5_GATEWAY_TOKEN", "")
        return bool(configured and candidate and hmac.compare_digest(configured, candidate))

    def _module(self) -> Any:
        if self._mt5 is None:
            try:
                self._mt5 = importlib.import_module("MetaTrader5")
            except ImportError as exc:
                raise MT5ConfigurationError(
                    "MetaTrader5 is not installed in backend/venv. "
                    "Install the pinned backend requirement first."
                ) from exc
        return self._mt5

    async def connect(self) -> Dict[str, Any]:
        return await asyncio.to_thread(self._connect_sync)

    def _connect_sync(self) -> Dict[str, Any]:
        with self._lock:
            mt5 = self._module()
            terminal_path = os.getenv(
                "MT5_TERMINAL_PATH", r"C:\Program Files\MetaTrader 5\terminal64.exe"
            ).strip()
            if terminal_path and not Path(terminal_path).exists():
                raise MT5ConfigurationError(f"MT5 terminal not found: {terminal_path}")

            kwargs: Dict[str, Any] = {
                "timeout": int(os.getenv("MT5_CONNECT_TIMEOUT_MS", "15000")),
            }
            login = os.getenv("MT5_LOGIN", "").strip()
            password = os.getenv("MT5_PASSWORD", "").strip()
            server = os.getenv("MT5_SERVER", "").strip()
            if login:
                kwargs["login"] = int(login)
            if password:
                kwargs["password"] = password
            if server:
                kwargs["server"] = server

            initialized = mt5.initialize(terminal_path, **kwargs) if terminal_path else mt5.initialize(**kwargs)
            if not initialized:
                self._connected = False
                self._last_error = str(mt5.last_error())
                raise MT5Error(f"MT5 initialize failed: {self._last_error}")

            account = mt5.account_info()
            terminal = mt5.terminal_info()
            if account is None or terminal is None:
                self._connected = False
                self._last_error = str(mt5.last_error())
                mt5.shutdown()
                raise MT5Error(f"MT5 terminal connected without account context: {self._last_error}")

            self._connected = True
            self._last_error = None
            return self._status_sync(include_account=True)

    async def disconnect(self) -> None:
        await asyncio.to_thread(self._disconnect_sync)

    def _disconnect_sync(self) -> None:
        with self._lock:
            if self._mt5 is not None:
                self._mt5.shutdown()
            self._connected = False

    def get_status(self, *, include_account: bool = False) -> Dict[str, Any]:
        with self._lock:
            return self._status_sync(include_account=include_account)

    def _status_sync(self, *, include_account: bool = False) -> Dict[str, Any]:
        package_available = True
        try:
            mt5 = self._module()
        except MT5ConfigurationError:
            package_available = False
            mt5 = None

        account = mt5.account_info() if self._connected and mt5 else None
        terminal = mt5.terminal_info() if self._connected and mt5 else None
        account_mode = self._account_mode(mt5, account) if account is not None else None
        terminal_data = _as_dict(terminal)
        account_data = _as_dict(account)
        live_armed_until = float(os.getenv("MT5_LIVE_ARMED_UNTIL_EPOCH", "0") or 0)
        live_armed = (
            self.execution_mode == "live"
            and os.getenv("MT5_LIVE_TRADING_ENABLED", "false").lower() == "true"
            and live_armed_until > time.time()
        )

        return {
            "connected": bool(self._connected and account is not None and terminal is not None),
            "package_available": package_available,
            "execution_mode": self.execution_mode,
            "live_trading_enabled": os.getenv("MT5_LIVE_TRADING_ENABLED", "false").lower() == "true",
            "live_armed": live_armed,
            "live_armed_until_epoch": live_armed_until or None,
            "gateway_token_configured": bool(os.getenv("MT5_GATEWAY_TOKEN", "")),
            "terminal_path": os.getenv(
                "MT5_TERMINAL_PATH", r"C:\Program Files\MetaTrader 5\terminal64.exe"
            ),
            "terminal": {
                "name": terminal_data.get("name"),
                "build": terminal_data.get("build"),
                "connected": terminal_data.get("connected"),
                "trade_allowed": terminal_data.get("trade_allowed"),
                "tradeapi_disabled": terminal_data.get("tradeapi_disabled"),
            } if terminal_data else None,
            "account": {
                "login_masked": self._mask_login(account_data.get("login")),
                "server": account_data.get("server"),
                "currency": account_data.get("currency"),
                "trade_mode": account_mode,
                "balance": account_data.get("balance"),
                "equity": account_data.get("equity"),
                "margin_free": account_data.get("margin_free"),
                "trade_allowed": account_data.get("trade_allowed"),
                "trade_expert": account_data.get("trade_expert"),
            } if include_account and account_data else None,
            "allowed_symbols": sorted(self._csv_set("MT5_ALLOWED_SYMBOLS")) if include_account else [],
            "allowed_experts": sorted(self._csv_set("MT5_ALLOWED_EXPERTS")) if include_account else [],
            "limits": {
                "max_open_positions": int(os.getenv("MT5_MAX_OPEN_POSITIONS", "3")),
                "max_pending_orders": int(os.getenv("MT5_MAX_PENDING_ORDERS", "3")),
                "max_total_volume": float(os.getenv("MT5_MAX_TOTAL_VOLUME", "0.30")),
                "max_symbol_volume": float(os.getenv("MT5_MAX_SYMBOL_VOLUME", "0.20")),
                "max_aggregate_risk_pct": float(os.getenv("MT5_MAX_AGGREGATE_RISK_PCT", "2.0")),
                "max_orders_per_minute": int(os.getenv("MT5_MAX_ORDERS_PER_MINUTE", "3")),
                "max_orders_per_day": int(os.getenv("MT5_MAX_ORDERS_PER_DAY", "20")),
            } if include_account else None,
            "last_error": self._last_error,
            "kill_switch": self.kill_switch_status(),
        }

    def kill_switch_status(self) -> Dict[str, Any]:
        state = self._journal.get_control("kill_switch")
        if state is None:
            return {"active": False, "reason": None, "updated_at": None}
        return {
            "active": bool(state.get("active")),
            "reason": state.get("reason"),
            "updated_at": state.get("updated_at"),
        }

    def activate_kill_switch(self, reason: str) -> Dict[str, Any]:
        normalized = reason.strip()
        if len(normalized) < 5:
            raise MT5ValidationError("Kill switch reason must contain at least 5 characters")
        return self._journal.set_control(
            "kill_switch",
            {
                "active": True,
                "reason": normalized[:500],
                "activated_at": datetime.now(timezone.utc).isoformat(),
            },
        )

    def reset_kill_switch(self, *, confirm: str) -> Dict[str, Any]:
        if confirm != "RESET":
            raise MT5ValidationError("Kill switch reset requires confirm=RESET")
        previous = self.kill_switch_status()
        return self._journal.set_control(
            "kill_switch",
            {
                "active": False,
                "reason": previous.get("reason"),
                "reset_at": datetime.now(timezone.utc).isoformat(),
            },
        )

    @staticmethod
    def _mask_login(login: Any) -> Optional[str]:
        if login is None:
            return None
        raw = str(login)
        return f"***{raw[-4:]}" if len(raw) > 4 else "****"

    @staticmethod
    def _account_mode(mt5: Any, account: Any) -> str:
        value = getattr(account, "trade_mode", None)
        mapping = {
            getattr(mt5, "ACCOUNT_TRADE_MODE_DEMO", 0): "demo",
            getattr(mt5, "ACCOUNT_TRADE_MODE_CONTEST", 1): "contest",
            getattr(mt5, "ACCOUNT_TRADE_MODE_REAL", 2): "real",
        }
        return mapping.get(value, f"unknown:{value}")

    def ensure_expert_allowed(self, expert_id: str) -> None:
        allowed = self._csv_set("MT5_ALLOWED_EXPERTS")
        if not allowed:
            raise MT5ExecutionBlocked("MT5_ALLOWED_EXPERTS is empty; no Expert Advisor is authorized")
        if expert_id.upper() not in allowed:
            raise MT5ExecutionBlocked(f"Expert Advisor '{expert_id}' is not authorized")

    def _ensure_symbol_allowed(self, symbol: str) -> None:
        allowed = self._csv_set("MT5_ALLOWED_SYMBOLS")
        if not allowed:
            raise MT5ExecutionBlocked("MT5_ALLOWED_SYMBOLS is empty; no symbol is authorized")
        if symbol.upper() not in allowed:
            raise MT5ExecutionBlocked(f"Symbol '{symbol}' is not authorized")

    async def preview_order(self, intent: MT5OrderIntent) -> Dict[str, Any]:
        return await asyncio.to_thread(self._preview_order_sync, intent)

    def _preview_order_sync(self, intent: MT5OrderIntent) -> Dict[str, Any]:
        with self._lock:
            if not self._connected:
                self._connect_sync()
            self.ensure_expert_allowed(intent.expert_id)
            self._ensure_symbol_allowed(intent.symbol)
            return self._prepare_order_sync(intent)

    def _prepare_order_sync(self, intent: MT5OrderIntent) -> Dict[str, Any]:
        mt5 = self._module()
        symbol = intent.symbol.strip().upper()
        side = intent.side.strip().upper()
        if side not in {"BUY", "SELL"}:
            raise MT5ValidationError("side must be BUY or SELL")

        max_signal_age = float(os.getenv("MT5_MAX_SIGNAL_AGE_SECONDS", "10"))
        signal_age = time.time() - intent.observed_at_epoch
        if signal_age < -5 or signal_age > max_signal_age:
            raise MT5ValidationError(
                f"Signal is stale or clock-skewed ({signal_age:.2f}s; max {max_signal_age:.2f}s)"
            )

        info = mt5.symbol_info(symbol)
        if info is None:
            raise MT5ValidationError(f"Unknown MT5 symbol: {symbol}")
        if not getattr(info, "visible", False) and not mt5.symbol_select(symbol, True):
            raise MT5ValidationError(f"Unable to add {symbol} to Market Watch")
        info = mt5.symbol_info(symbol)
        tick = mt5.symbol_info_tick(symbol)
        if info is None or tick is None:
            raise MT5ValidationError(f"No tradable tick available for {symbol}")

        tick_ms = int(getattr(tick, "time_msc", 0) or 0)
        tick_age = time.time() - (tick_ms / 1000 if tick_ms else float(getattr(tick, "time", 0)))
        max_tick_age = float(os.getenv("MT5_MAX_TICK_AGE_SECONDS", "5"))
        if tick_age < -5 or tick_age > max_tick_age:
            raise MT5ValidationError(f"MT5 quote is stale ({tick_age:.2f}s; max {max_tick_age:.2f}s)")

        volume = float(intent.volume)
        volume_min = float(getattr(info, "volume_min", 0.0) or 0.0)
        volume_max = float(getattr(info, "volume_max", 0.0) or 0.0)
        volume_step = float(getattr(info, "volume_step", 0.0) or 0.0)
        configured_max = float(os.getenv("MT5_MAX_VOLUME_PER_ORDER", "0.10"))
        if volume < volume_min or (volume_max and volume > volume_max) or volume > configured_max:
            raise MT5ValidationError(
                f"Volume {volume} outside allowed range {volume_min}..{min(volume_max or configured_max, configured_max)}"
            )
        if volume_step:
            steps = round((volume - volume_min) / volume_step)
            normalized = volume_min + steps * volume_step
            if not math.isclose(volume, normalized, rel_tol=0.0, abs_tol=max(volume_step / 1000, 1e-9)):
                raise MT5ValidationError(f"Volume must follow broker step {volume_step}")

        ask = float(getattr(tick, "ask", 0.0) or 0.0)
        bid = float(getattr(tick, "bid", 0.0) or 0.0)
        price = ask if side == "BUY" else bid
        if price <= 0 or ask <= 0 or bid <= 0:
            raise MT5ValidationError(f"Invalid bid/ask for {symbol}")

        point = float(getattr(info, "point", 0.0) or 0.0)
        spread_points = (ask - bid) / point if point else 0.0
        max_spread = float(os.getenv("MT5_MAX_SPREAD_POINTS", "30"))
        if max_spread > 0 and spread_points > max_spread:
            raise MT5ExecutionBlocked(
                f"Spread {spread_points:.1f} points exceeds configured maximum {max_spread:.1f}"
            )

        self._validate_stops(intent, price, point, int(getattr(info, "trade_stops_level", 0) or 0))

        order_type = mt5.ORDER_TYPE_BUY if side == "BUY" else mt5.ORDER_TYPE_SELL
        request: Dict[str, Any] = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": order_type,
            "price": price,
            "deviation": int(intent.deviation or os.getenv("MT5_DEFAULT_DEVIATION", "10")),
            "magic": int(intent.magic or os.getenv("MT5_MAGIC", "260806")),
            "comment": intent.comment[:31],
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": self._filling_mode(mt5),
        }
        if intent.sl is not None:
            request["sl"] = float(intent.sl)
        if intent.tp is not None:
            request["tp"] = float(intent.tp)

        check = mt5.order_check(request)
        if check is None:
            raise MT5Error(f"MT5 order_check failed: {mt5.last_error()}")
        check_data = _as_dict(check)
        if int(check_data.get("retcode", -1)) != 0:
            raise MT5ExecutionBlocked(
                f"MT5 order_check rejected the order: {check_data.get('comment', check_data.get('retcode'))}"
            )

        margin = mt5.order_calc_margin(order_type, symbol, volume, price)
        if margin is None:
            raise MT5ExecutionBlocked(f"Unable to calculate required margin: {mt5.last_error()}")
        max_margin = float(os.getenv("MT5_MAX_MARGIN_PER_ORDER", "500"))
        if max_margin > 0 and float(margin) > max_margin:
            raise MT5ExecutionBlocked(
                f"Required margin {float(margin):.2f} exceeds configured maximum {max_margin:.2f}"
            )

        risk_amount: Optional[float] = None
        risk_limit: Optional[float] = None
        if intent.sl is not None:
            projected = mt5.order_calc_profit(order_type, symbol, volume, price, float(intent.sl))
            if projected is None:
                raise MT5ExecutionBlocked(f"Unable to calculate stop-loss risk: {mt5.last_error()}")
            risk_amount = max(0.0, -float(projected))
            account = mt5.account_info()
            equity = float(getattr(account, "equity", 0.0) or 0.0)
            max_risk_pct = float(os.getenv("MT5_MAX_RISK_PER_ORDER_PCT", "0.5"))
            risk_limit = equity * max_risk_pct / 100.0
            if risk_limit > 0 and risk_amount > risk_limit:
                raise MT5ExecutionBlocked(
                    f"Stop-loss risk {risk_amount:.2f} exceeds {max_risk_pct:.2f}% of account equity ({risk_limit:.2f})"
                )

        exposure = self._aggregate_exposure_snapshot(
            mt5,
            symbol=symbol,
            new_volume=volume,
            new_stop_risk=risk_amount,
        )

        return {
            "signal_id": intent.signal_id,
            "expert_id": intent.expert_id,
            "symbol": symbol,
            "side": side,
            "volume": volume,
            "price": price,
            "bid": bid,
            "ask": ask,
            "spread_points": round(spread_points, 2),
            "tick_age_seconds": round(tick_age, 3),
            "margin_required": float(margin),
            "stop_risk_amount": risk_amount,
            "stop_risk_limit": risk_limit,
            "aggregate_exposure": exposure,
            "account_mode": self._account_mode(mt5, mt5.account_info()),
            "execution_mode": self.execution_mode,
            "check": check_data,
            "request": request,
        }

    @staticmethod
    def _validate_stops(intent: MT5OrderIntent, price: float, point: float, stops_level: int) -> None:
        minimum_distance = point * stops_level
        if intent.side.upper() == "BUY":
            if intent.sl is not None and intent.sl >= price - minimum_distance:
                raise MT5ValidationError("BUY stop-loss must be below price and respect broker stops level")
            if intent.tp is not None and intent.tp <= price + minimum_distance:
                raise MT5ValidationError("BUY take-profit must be above price and respect broker stops level")
        else:
            if intent.sl is not None and intent.sl <= price + minimum_distance:
                raise MT5ValidationError("SELL stop-loss must be above price and respect broker stops level")
            if intent.tp is not None and intent.tp >= price - minimum_distance:
                raise MT5ValidationError("SELL take-profit must be below price and respect broker stops level")

    @staticmethod
    def _filling_mode(mt5: Any) -> int:
        configured = os.getenv("MT5_FILLING_MODE", "IOC").strip().upper()
        mapping = {
            "FOK": mt5.ORDER_FILLING_FOK,
            "IOC": mt5.ORDER_FILLING_IOC,
            "RETURN": mt5.ORDER_FILLING_RETURN,
        }
        if configured not in mapping:
            raise MT5ConfigurationError("MT5_FILLING_MODE must be FOK, IOC, or RETURN")
        return mapping[configured]

    def _aggregate_exposure_snapshot(
        self,
        mt5: Any,
        *,
        symbol: str,
        new_volume: float,
        new_stop_risk: Optional[float],
    ) -> Dict[str, Any]:
        positions = list(mt5.positions_get() or [])
        orders_get = getattr(mt5, "orders_get", None)
        pending_orders = list(orders_get() or []) if callable(orders_get) else []

        max_positions = int(os.getenv("MT5_MAX_OPEN_POSITIONS", "3"))
        max_pending = int(os.getenv("MT5_MAX_PENDING_ORDERS", "3"))
        if max_positions > 0 and len(positions) + 1 > max_positions:
            raise MT5ExecutionBlocked(
                f"Open position limit reached ({len(positions)}/{max_positions})"
            )
        if max_pending >= 0 and len(pending_orders) > max_pending:
            raise MT5ExecutionBlocked(
                f"Pending order limit exceeded ({len(pending_orders)}/{max_pending})"
            )

        total_volume = sum(
            abs(float(getattr(position, "volume", 0.0) or 0.0))
            for position in positions
        )
        symbol_volume = sum(
            abs(float(getattr(position, "volume", 0.0) or 0.0))
            for position in positions
            if str(getattr(position, "symbol", "")).upper() == symbol
        )
        max_total_volume = float(os.getenv("MT5_MAX_TOTAL_VOLUME", "0.30"))
        max_symbol_volume = float(os.getenv("MT5_MAX_SYMBOL_VOLUME", "0.20"))
        if max_total_volume > 0 and total_volume + new_volume > max_total_volume:
            raise MT5ExecutionBlocked(
                f"Aggregate volume {total_volume + new_volume:.2f} exceeds "
                f"account limit {max_total_volume:.2f}"
            )
        if max_symbol_volume > 0 and symbol_volume + new_volume > max_symbol_volume:
            raise MT5ExecutionBlocked(
                f"{symbol} volume {symbol_volume + new_volume:.2f} exceeds "
                f"symbol limit {max_symbol_volume:.2f}"
            )

        existing_stop_risk = 0.0
        unprotected_positions: list[str] = []
        buy_type = getattr(mt5, "POSITION_TYPE_BUY", 0)
        for position in positions:
            position_symbol = str(getattr(position, "symbol", "")).upper()
            position_volume = abs(float(getattr(position, "volume", 0.0) or 0.0))
            stop_loss = float(getattr(position, "sl", 0.0) or 0.0)
            if position_volume <= 0:
                continue
            if stop_loss <= 0:
                unprotected_positions.append(position_symbol or "UNKNOWN")
                continue
            position_type = getattr(position, "type", buy_type)
            order_type = (
                mt5.ORDER_TYPE_BUY
                if position_type == buy_type
                else mt5.ORDER_TYPE_SELL
            )
            price_open = float(getattr(position, "price_open", 0.0) or 0.0)
            projected = mt5.order_calc_profit(
                order_type,
                position_symbol,
                position_volume,
                price_open,
                stop_loss,
            )
            if projected is None:
                raise MT5ExecutionBlocked(
                    f"Unable to calculate aggregate stop risk for {position_symbol}"
                )
            existing_stop_risk += max(0.0, -float(projected))

        block_unprotected = (
            os.getenv("MT5_BLOCK_ON_UNPROTECTED_POSITION", "true").lower()
            == "true"
        )
        if block_unprotected and unprotected_positions:
            symbols = ", ".join(sorted(set(unprotected_positions)))
            raise MT5ExecutionBlocked(
                f"Unprotected MT5 positions block new execution: {symbols}"
            )

        account = mt5.account_info()
        equity = float(getattr(account, "equity", 0.0) or 0.0)
        aggregate_risk = existing_stop_risk + float(new_stop_risk or 0.0)
        max_risk_pct = float(os.getenv("MT5_MAX_AGGREGATE_RISK_PCT", "2.0"))
        aggregate_limit = equity * max_risk_pct / 100.0
        if aggregate_limit > 0 and aggregate_risk > aggregate_limit:
            raise MT5ExecutionBlocked(
                f"Aggregate stop risk {aggregate_risk:.2f} exceeds "
                f"{max_risk_pct:.2f}% of equity ({aggregate_limit:.2f})"
            )

        return {
            "open_positions": len(positions),
            "pending_orders": len(pending_orders),
            "current_total_volume": round(total_volume, 8),
            "projected_total_volume": round(total_volume + new_volume, 8),
            "current_symbol_volume": round(symbol_volume, 8),
            "projected_symbol_volume": round(symbol_volume + new_volume, 8),
            "existing_stop_risk": round(existing_stop_risk, 2),
            "projected_stop_risk": round(aggregate_risk, 2),
            "aggregate_stop_risk_limit": round(aggregate_limit, 2),
            "unprotected_positions": sorted(set(unprotected_positions)),
        }

    async def execute_order(self, intent: MT5OrderIntent) -> Dict[str, Any]:
        return await asyncio.to_thread(self._execute_order_sync, intent)

    def _execute_order_sync(self, intent: MT5OrderIntent) -> Dict[str, Any]:
        with self._lock:
            kill_switch = self.kill_switch_status()
            if kill_switch["active"]:
                raise MT5ExecutionBlocked(
                    f"MT5 kill switch is active: {kill_switch.get('reason') or 'no reason provided'}"
                )
            if not self._connected:
                self._connect_sync()
            self.ensure_expert_allowed(intent.expert_id)
            self._ensure_symbol_allowed(intent.symbol)
            preview = self._prepare_order_sync(intent)
            self._enforce_execution_mode(intent, preview["account_mode"])
            max_orders_per_minute = int(
                os.getenv("MT5_MAX_ORDERS_PER_MINUTE", "3")
            )
            recent_orders = self._journal.count_recent_executions(60)
            if (
                max_orders_per_minute > 0
                and recent_orders >= max_orders_per_minute
            ):
                raise MT5ExecutionBlocked(
                    f"MT5 order rate limit reached "
                    f"({recent_orders}/{max_orders_per_minute} in 60 seconds)"
                )
            max_orders_per_day = int(
                os.getenv("MT5_MAX_ORDERS_PER_DAY", "20")
            )
            daily_orders = self._journal.count_recent_executions(86_400)
            if max_orders_per_day > 0 and daily_orders >= max_orders_per_day:
                raise MT5ExecutionBlocked(
                    f"MT5 daily order limit reached "
                    f"({daily_orders}/{max_orders_per_day})"
                )

            reserved = self._journal.reserve(
                signal_id=intent.signal_id,
                expert_id=intent.expert_id,
                symbol=preview["symbol"],
                side=preview["side"],
                volume=preview["volume"],
                execution_mode=self.execution_mode,
                request=preview,
            )
            if not reserved:
                existing = self._journal.get(intent.signal_id)
                raise MT5ExecutionBlocked(
                    f"Duplicate signal_id '{intent.signal_id}' blocked; existing state={existing.get('state') if existing else 'unknown'}"
                )

            mt5 = self._module()
            result = mt5.order_send(preview["request"])
            if result is None:
                payload = {"error": str(mt5.last_error())}
                self._journal.complete(intent.signal_id, "unknown", payload)
                raise MT5Error(f"MT5 order_send returned no result: {payload['error']}")

            payload = _as_dict(result)
            retcode = int(payload.get("retcode", -1))
            state = self._state_for_retcode(mt5, retcode)
            self._journal.complete(intent.signal_id, state, payload)
            if state == "rejected":
                raise MT5ExecutionBlocked(
                    f"MT5 rejected order {intent.signal_id}: {payload.get('comment', retcode)}"
                )
            return {"state": state, "preview": preview, "result": payload}

    def _enforce_execution_mode(self, intent: MT5OrderIntent, account_mode: str) -> None:
        mode = self.execution_mode
        if mode == "disabled":
            raise MT5ExecutionBlocked("MT5 execution is disabled; previews remain available")
        if os.getenv("MT5_REQUIRE_STOP_LOSS", "true").lower() == "true" and intent.sl is None:
            raise MT5ExecutionBlocked("A stop-loss is required for MT5 execution")

        mt5 = self._module()
        terminal = mt5.terminal_info()
        account = mt5.account_info()
        if terminal is None or account is None:
            raise MT5ExecutionBlocked("MT5 terminal/account state is unavailable")
        if bool(getattr(terminal, "tradeapi_disabled", False)):
            raise MT5ExecutionBlocked("MT5 Python trading API is disabled in the terminal")
        if not bool(getattr(terminal, "trade_allowed", False)):
            raise MT5ExecutionBlocked("MT5 Algo Trading is disabled in the terminal")
        if not bool(getattr(account, "trade_allowed", False)) or not bool(getattr(account, "trade_expert", False)):
            raise MT5ExecutionBlocked("The MT5 account does not allow Expert Advisor trading")

        balance = float(getattr(account, "balance", 0.0) or 0.0)
        equity = float(getattr(account, "equity", 0.0) or 0.0)
        max_drawdown = float(os.getenv("MT5_MAX_EQUITY_DRAWDOWN_PCT", "5"))
        drawdown_pct = ((balance - equity) / balance * 100.0) if balance > 0 else 0.0
        if max_drawdown > 0 and drawdown_pct >= max_drawdown:
            raise MT5ExecutionBlocked(
                f"Account equity drawdown {drawdown_pct:.2f}% reached the {max_drawdown:.2f}% limit"
            )
        if mode == "paper" and account_mode not in {"demo", "contest"}:
            raise MT5ExecutionBlocked("Paper mode refuses to send orders to a real MT5 account")
        if mode == "live":
            live_enabled = os.getenv("MT5_LIVE_TRADING_ENABLED", "false").lower() == "true"
            if not live_enabled or not intent.confirm_live:
                raise MT5ExecutionBlocked("Live execution requires server opt-in and confirm_live=true")
            armed_until = float(
                os.getenv("MT5_LIVE_ARMED_UNTIL_EPOCH", "0") or 0
            )
            if armed_until <= time.time():
                raise MT5ExecutionBlocked(
                    "Live execution is not armed or the live window has expired"
                )
            if account_mode != "real":
                raise MT5ExecutionBlocked("Live mode requires an MT5 real account")

    @staticmethod
    def _state_for_retcode(mt5: Any, retcode: int) -> str:
        if retcode == getattr(mt5, "TRADE_RETCODE_DONE", 10009):
            return "filled"
        if retcode == getattr(mt5, "TRADE_RETCODE_DONE_PARTIAL", 10010):
            return "partial"
        if retcode == getattr(mt5, "TRADE_RETCODE_PLACED", 10008):
            return "submitted"
        return "rejected"

    async def reconcile_orders(self, limit: int = 200) -> Dict[str, Any]:
        return await asyncio.to_thread(self._reconcile_orders_sync, limit)

    def _reconcile_orders_sync(self, limit: int = 200) -> Dict[str, Any]:
        with self._lock:
            if not self._connected:
                self._connect_sync()
            mt5 = self._module()
            unresolved = self._journal.list_by_states(
                ["submitting", "submitted", "partial", "unknown"],
                limit=limit,
            )
            updates: list[Dict[str, Any]] = []
            for entry in unresolved:
                previous_state = str(entry["state"])
                state, source = self._resolve_journal_state(mt5, entry)
                details = {
                    "checked_at": datetime.now(timezone.utc).isoformat(),
                    "previous_state": previous_state,
                    "state": state,
                    "source": source,
                }
                self._journal.reconcile(entry["signal_id"], state, details)
                updates.append({
                    "signal_id": entry["signal_id"],
                    "previous_state": previous_state,
                    "state": state,
                    "source": source,
                })
            return {
                "checked": len(unresolved),
                "changed": sum(
                    item["state"] != item["previous_state"]
                    for item in updates
                ),
                "updates": updates,
            }

    @staticmethod
    def _mt5_items(mt5: Any, method_name: str, *, ticket: int) -> list[Any]:
        method = getattr(mt5, method_name, None)
        if not callable(method) or ticket <= 0:
            return []
        try:
            return list(method(ticket=ticket) or [])
        except TypeError:
            if not method_name.startswith("history_"):
                return []
            end = datetime.now(timezone.utc)
            start = end - timedelta(days=30)
            return [
                item
                for item in list(method(start, end) or [])
                if int(getattr(item, "ticket", 0) or 0) == ticket
            ]

    def _resolve_journal_state(
        self,
        mt5: Any,
        entry: Dict[str, Any],
    ) -> tuple[str, str]:
        result = entry.get("result") or {}
        order_ticket = int(result.get("order", 0) or 0)
        deal_ticket = int(result.get("deal", 0) or 0)
        deals = self._mt5_items(
            mt5,
            "history_deals_get",
            ticket=deal_ticket,
        )
        active_orders = self._mt5_items(
            mt5,
            "orders_get",
            ticket=order_ticket,
        )
        if deals and active_orders:
            return "partial", "history_deal+active_order"
        if deals:
            return "filled", "history_deal"
        if active_orders:
            return "submitted", "active_order"

        historical_orders = self._mt5_items(
            mt5,
            "history_orders_get",
            ticket=order_ticket,
        )
        if historical_orders:
            order_state = getattr(historical_orders[-1], "state", None)
            if order_state == getattr(mt5, "ORDER_STATE_FILLED", 4):
                return "filled", "history_order"
            cancelled_states = {
                getattr(mt5, "ORDER_STATE_CANCELED", 2),
                getattr(mt5, "ORDER_STATE_REJECTED", 3),
                getattr(mt5, "ORDER_STATE_EXPIRED", 6),
            }
            if order_state in cancelled_states:
                return "cancelled", "history_order"
        return str(entry["state"]), "unresolved"

    async def positions(self) -> list[Dict[str, Any]]:
        return await asyncio.to_thread(self._positions_sync)

    def _positions_sync(self) -> list[Dict[str, Any]]:
        with self._lock:
            if not self._connected:
                self._connect_sync()
            positions: Iterable[Any] = self._module().positions_get() or []
            return [_as_dict(position) for position in positions]

    def recent_orders(self, limit: int = 50) -> list[Dict[str, Any]]:
        return self._journal.list_recent(limit)


mt5_service = MT5Service()
