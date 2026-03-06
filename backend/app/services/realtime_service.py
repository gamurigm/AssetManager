from typing import Set, Dict
from app.core.logging import logger
from app.core.container import get_quote

class RealtimeService:
    def __init__(self):
        self.active_symbols: Set[str] = set()
        self.client_subscriptions: Dict[str, Set[str]] = {} # sid -> {symbols}

    def subscribe(self, sid: str, symbol: str):
        if sid not in self.client_subscriptions:
            self.client_subscriptions[sid] = set()
        
        self.client_subscriptions[sid].add(symbol)
        self.active_symbols.add(symbol)
        logger.info(f"[Socket] Client {sid} subscribed to {symbol}. Active: {len(self.active_symbols)}")

    def unsubscribe(self, sid: str, symbol: str):
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
        for symbol in self.active_symbols:
            try:
                # Fetch quote via existing Clean Architecture Use Case
                quote_data = await get_quote.execute(symbol)
                if quote_data and "price" in quote_data:
                    # Emit to a "room" named after the symbol
                    await sio.emit("price_update", {
                        "symbol": symbol,
                        "price": quote_data["price"],
                        "change": quote_data.get("change", 0),
                        "changePercent": quote_data.get("changePercentage", 0)
                    }, room=symbol)
            except Exception as e:
                logger.error(f"[Realtime] Error fetching {symbol} for broadcast: {e}")

realtime_service = RealtimeService()
