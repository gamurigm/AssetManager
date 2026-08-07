import time
import asyncio
from typing import Awaitable, Callable, Set, Dict, Any
from app.core.logging import logger
from app.core.container import get_quote
from app.services.ibkr_service import ibkr_service


TickListener = Callable[[Dict[str, Any]], Awaitable[None]]


class RealtimeService:
    def __init__(self):
        self.active_symbols: Set[str] = set()
        self.client_subscriptions: Dict[str, Set[str]] = {} # sid -> {symbols}
        self.sio = None
        self._ibkr_listener_registered = False
        self._tick_listeners: Set[TickListener] = set()

    def configure_streaming(self, sio):
        self.sio = sio
        try:
            ibkr_service.set_event_loop(asyncio.get_running_loop())
        except RuntimeError:
            pass

        if not self._ibkr_listener_registered:
            ibkr_service.add_tick_listener(self._forward_ibkr_tick)
            self._ibkr_listener_registered = True

    def shutdown_streaming(self):
        if self._ibkr_listener_registered:
            ibkr_service.remove_tick_listener(self._forward_ibkr_tick)
            self._ibkr_listener_registered = False
        self.sio = None

    def add_tick_listener(self, listener: TickListener) -> None:
        self._tick_listeners.add(listener)

    def remove_tick_listener(self, listener: TickListener) -> None:
        self._tick_listeners.discard(listener)

    async def _notify_tick_listeners(self, payload: Dict[str, Any]) -> None:
        if not self._tick_listeners:
            return

        for listener in list(self._tick_listeners):
            try:
                await listener(payload)
            except Exception as exc:
                logger.error(f"[Realtime] Tick listener failed: {exc}")

    async def _forward_ibkr_tick(self, payload: Dict[str, Any]):
        if not self.sio:
            return

        symbol = payload.get("symbol")
        if not symbol or symbol not in self.active_symbols:
            return

        await self.sio.emit("price_update", payload, room=symbol)
        await self._notify_tick_listeners(payload)

    def subscribe(self, sid: str, symbol: str):
        symbol = symbol.upper()
        if sid not in self.client_subscriptions:
            self.client_subscriptions[sid] = set()

        self.client_subscriptions[sid].add(symbol)
        is_new_symbol = symbol not in self.active_symbols
        self.active_symbols.add(symbol)

        if is_new_symbol:
            try:
                asyncio.create_task(ibkr_service.subscribe_market_data(symbol))
            except RuntimeError:
                pass

        logger.info(f"[Socket] Client {sid} subscribed to {symbol}. Active: {len(self.active_symbols)}")

    def unsubscribe(self, sid: str, symbol: str):
        symbol = symbol.upper()
        if sid in self.client_subscriptions:
            self.client_subscriptions[sid].discard(symbol)
            if not self.client_subscriptions[sid]:
                del self.client_subscriptions[sid]

        # Recompute active symbols across all clients
        new_active = set()
        for subs in self.client_subscriptions.values():
            new_active.update(subs)
        self.active_symbols = new_active

    def clear_client(self, sid: str):
        if sid in self.client_subscriptions:
            del self.client_subscriptions[sid]
        
        new_active = set()
        for subs in self.client_subscriptions.values():
            new_active.update(subs)
        self.active_symbols = new_active
        logger.info(f"[Socket] Client {sid} disconnected. Remaining active symbols: {len(self.active_symbols)}")

    async def broadcast_prices(self, sio):
        if not self.active_symbols:
            return

        logger.debug(f"[Realtime] Broadcasting prices for {len(self.active_symbols)} symbols")

        # Filter out symbols that already have fresh IBKR ticks
        symbols_to_fetch = [
            s for s in list(self.active_symbols)
            if not ibkr_service.has_fresh_tick(s)
        ]

        if not symbols_to_fetch:
            return

        async def _fetch_and_emit(symbol: str):
            try:
                quote_data = await get_quote.execute(symbol)
                if quote_data and "price" in quote_data:
                    payload = {
                        "symbol": symbol,
                        "price": quote_data["price"],
                        "change": quote_data.get("change", 0),
                        "changePercent": quote_data.get("changePercentage", 0),
                        "timestamp": time.time(),
                        "source": quote_data.get("source", "fallback"),
                        "live": False,
                    }
                    await sio.emit("price_update", payload, room=symbol)
                    await self._notify_tick_listeners(payload)
            except Exception as e:
                logger.error(f"[Realtime] Error fetching {symbol} for broadcast: {e}")

        # Fire ALL fetches concurrently instead of one-by-one
        await asyncio.gather(*[_fetch_and_emit(s) for s in symbols_to_fetch])

    def get_status(self) -> Dict[str, Any]:
        return {
            "active_symbols": sorted(self.active_symbols),
            "client_count": len(self.client_subscriptions),
            "subscription_count": sum(len(symbols) for symbols in self.client_subscriptions.values()),
        }

realtime_service = RealtimeService()
