import os
import time
import asyncio
import inspect
import logging
import socket
from datetime import datetime
from typing import Dict, Any, List, Optional, Callable, Tuple
from ib_insync import IB, Forex, MarketOrder, Stock

logger = logging.getLogger("MMAM")

class IBKRService:
    _DEFAULT_PORTS: Tuple[int, ...] = (7497, 4002, 7496, 4001, 4000)
    _FOREX_CODES = {
        "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "NZD", "HKD", "SGD",
        "SEK", "NOK", "DKK", "MXN", "CNY", "INR", "BRL", "ZAR", "TRY", "KRW",
        "THB", "PLN", "HUF", "CZK", "ILS", "CLP", "PHP", "IDR", "MYR", "RON",
    }

    _CONNECT_COOLDOWN_SECONDS: float = 30.0

    def __init__(self):
        self.ib: Optional[IB] = None
        self.host = os.getenv("IBKR_HOST", "127.0.0.1")
        self.configured_port = int(os.getenv("IBKR_PORT", 7497))
        self.port = self.configured_port
        self.client_id = int(os.getenv("IBKR_CLIENT_ID", 1))
        self.is_connected = False
        self.last_connection_error: Optional[str] = None
        self._last_connect_attempt: float = 0.0
        self.market_data_cache: Dict[str, Any] = {}
        self.subscribed_symbols: set[str] = set()
        self._contract_symbols: Dict[str, str] = {}
        self._tick_listeners: List[Callable[[Dict[str, Any]], Any]] = []
        self._event_loop: Optional[asyncio.AbstractEventLoop] = None
        self._pending_ticker_listener_registered = False

    @classmethod
    def _is_forex_symbol(cls, symbol: str) -> bool:
        normalized = symbol.upper().replace("=X", "").replace("/", "").replace(" ", "")
        if len(normalized) != 6:
            return False

        base, quote = normalized[:3], normalized[3:]
        return base in cls._FOREX_CODES and quote in cls._FOREX_CODES

    @staticmethod
    def _normalize_symbol(symbol: str) -> str:
        normalized = symbol.upper().strip()
        if normalized == "EURSUD":
            return "EURUSD"
        return normalized

    def _to_app_symbol(self, symbol: str) -> str:
        normalized = self._normalize_symbol(symbol)
        compact = normalized.replace("/", "").replace(" ", "")
        if compact.endswith("=X"):
            compact = compact[:-2]

        if self._is_forex_symbol(compact):
            return f"{compact}=X"

        return normalized

    def _build_market_data_contract(self, symbol: str):
        app_symbol = self._to_app_symbol(symbol)
        if self._is_forex_symbol(app_symbol):
            return Forex(app_symbol[:-2]), app_symbol

        return Stock(app_symbol, "SMART", "USD"), app_symbol

    def _get_port_candidates(self) -> List[int]:
        candidates: List[int] = []
        raw_candidates = os.getenv("IBKR_PORT_CANDIDATES", "")

        for raw_port in [str(self.configured_port), *raw_candidates.split(","), *[str(port) for port in self._DEFAULT_PORTS]]:
            raw_port = raw_port.strip()
            if not raw_port:
                continue

            try:
                port = int(raw_port)
            except ValueError:
                continue

            if port not in candidates:
                candidates.append(port)

        return candidates

    @staticmethod
    def _is_port_open(host: str, port: int, timeout: float = 0.5) -> bool:
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return True
        except OSError:
            return False

    def _remember_contract_symbol(self, contract, app_symbol: str):
        con_id = getattr(contract, "conId", 0)
        if con_id:
            self._contract_symbols[f"conid:{con_id}"] = app_symbol

        local_symbol = getattr(contract, "localSymbol", None)
        if local_symbol:
            sec_type = getattr(contract, "secType", "")
            self._contract_symbols[f"local:{sec_type}:{str(local_symbol).upper()}"] = app_symbol

    def _resolve_app_symbol(self, contract) -> Optional[str]:
        con_id = getattr(contract, "conId", 0)
        if con_id:
            cached_symbol = self._contract_symbols.get(f"conid:{con_id}")
            if cached_symbol:
                return cached_symbol

        local_symbol = getattr(contract, "localSymbol", None)
        if local_symbol:
            sec_type = getattr(contract, "secType", "")
            cached_symbol = self._contract_symbols.get(f"local:{sec_type}:{str(local_symbol).upper()}")
            if cached_symbol:
                return cached_symbol

        sec_type = getattr(contract, "secType", "")
        if sec_type == "CASH":
            base = str(getattr(contract, "symbol", "") or "").upper()
            quote = str(getattr(contract, "currency", "") or "").upper()
            if base and quote:
                return f"{base}{quote}=X"

        symbol = str(getattr(contract, "symbol", "") or "").upper()
        return symbol or None

    def set_event_loop(self, loop: Optional[asyncio.AbstractEventLoop] = None):
        """No-op in modern async FastAPI, we use get_running_loop() inside async methods."""
        pass

    def add_tick_listener(self, listener: Callable[[Dict[str, Any]], Any]):
        if listener not in self._tick_listeners:
            self._tick_listeners.append(listener)

    def remove_tick_listener(self, listener: Callable[[Dict[str, Any]], Any]):
        if listener in self._tick_listeners:
            self._tick_listeners.remove(listener)

    def _dispatch_tick(self, payload: Dict[str, Any]):
        if not self._tick_listeners:
            return

        loop = None
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            return

        for listener in list(self._tick_listeners):
            try:
                result = listener(payload)
                if inspect.isawaitable(result):
                    asyncio.run_coroutine_threadsafe(result, loop)
            except Exception as exc:
                logger.error(f"[IBKR] Tick listener error: {exc}")
                
    def _get_loop(self):
        try:
            return asyncio.get_running_loop()
        except RuntimeError:
            return None

    def _ensure_ib_instance(self):
        """Create a fresh IB() instance. Note: Must be called within an running loop."""
        if self.ib is not None:
            try:
                if self.ib.isConnected():
                    self.ib.disconnect()
            except Exception:
                pass
        self._pending_ticker_listener_registered = False
        # ib_insync.IB() by default picks up the current loop if available
        self.ib = IB()

    async def connect(self):
        """Connect to TWS or IB Gateway."""
        if self.ib is not None and self.ib.isConnected():
            return

        now = time.time()
        if now - self._last_connect_attempt < self._CONNECT_COOLDOWN_SECONDS:
            return
        self._last_connect_attempt = now

        reachable_ports = [port for port in self._get_port_candidates() if self._is_port_open(self.host, port)]
        if not reachable_ports:
            self.is_connected = False
            tried_ports = ", ".join(str(port) for port in self._get_port_candidates())
            self.last_connection_error = f"No reachable IBKR endpoint on {self.host}. Tried ports: {tried_ports}"
            logger.warning(f"[IBKR] {self.last_connection_error}")
            return

        self._ensure_ib_instance()

        for port in reachable_ports:
            try:
                await self.ib.connectAsync(self.host, port, clientId=self.client_id, timeout=4)
                self.is_connected = True
                self.port = port
                self.last_connection_error = None
                self.set_event_loop()
                if not self._pending_ticker_listener_registered:
                    self.ib.pendingTickersEvent += self._on_pending_tickers
                    self._pending_ticker_listener_registered = True
                logger.info(f"✅ [IBKR] Connected to {self.host}:{self.port}")
                return
            except Exception as e:
                self.is_connected = False
                self.last_connection_error = f"{self.host}:{port} -> {str(e)}"
                logger.error(f"❌ [IBKR] Connection failed on {self.host}:{port}: {str(e)}")

    def disconnect(self):
        if self.ib is not None:
            if self._pending_ticker_listener_registered:
                try:
                    self.ib.pendingTickersEvent -= self._on_pending_tickers
                except Exception:
                    pass
                self._pending_ticker_listener_registered = False
            try:
                self.ib.disconnect()
            except Exception:
                pass

        self.is_connected = False
        self.subscribed_symbols.clear()
        self.market_data_cache.clear()
        self._contract_symbols.clear()
        logger.info("🔌 [IBKR] Disconnected.")

    def _ib_connected(self) -> bool:
        return self.ib is not None and self.ib.isConnected()

    async def get_account_summary(self) -> List[Dict[str, Any]]:
        """Fetch account summary (Balance, Equity, etc)."""
        if not self._ib_connected():
            await self.connect()
        
        if not self._ib_connected():
            return [{"error": "Not connected to IBKR"}]

        tags = ['NetLiquidation', 'TotalCashValue', 'SettledCash', 'BuyingPower', 'GrossPositionValue']
        summary = await self.ib.accountSummaryAsync()
        
        # Filter and format
        res = []
        for item in summary:
            if item.tag in tags:
                res.append({"tag": item.tag, "value": item.value, "currency": item.currency})
        return res

    async def get_positions(self) -> List[Dict[str, Any]]:
        """Fetch open positions."""
        if not self._ib_connected():
            await self.connect()
        
        if not self._ib_connected():
            return []

        # In ib_insync, positions() is updated automatically
        positions = self.ib.positions()
        res = []
        for p in positions:
            res.append({
                "account": p.account,
                "symbol": p.contract.symbol,
                "position": p.position,
                "avgCost": p.avgCost
            })
        return res

    async def place_market_order(self, symbol: str, quantity: float, side: str) -> Dict[str, Any]:
        """Place a market order for a stock."""
        if not self._ib_connected():
            await self.connect()
        
        if not self._ib_connected():
            return {"error": "Not connected to IBKR"}

        contract = Stock(symbol.upper(), 'SMART', 'USD')
        await self.ib.qualifyContractsAsync(contract)
        
        order = MarketOrder(side.upper(), quantity)
        trade = self.ib.placeOrder(contract, order)
        
        # Wait for the order to be processed
        while not trade.isDone():
            await asyncio.sleep(0.1)
            
        return {
            "orderId": trade.order.orderId,
            "status": trade.orderStatus.status,
            "filled": trade.orderStatus.filled,
            "remaining": trade.orderStatus.remaining,
            "avgFillPrice": trade.orderStatus.avgFillPrice
        }

    def _on_pending_tickers(self, tickers):
        """Callback for real-time market data updates."""
        for t in tickers:
            symbol = self._resolve_app_symbol(t.contract)
            if not symbol:
                continue

            price = t.last if t.last and t.last > 0 else t.close
            if (not price or price <= 0) and hasattr(t, "marketPrice"):
                try:
                    price = t.marketPrice()
                except Exception:
                    price = None

            if not price or price <= 0:
                continue

            tick_time = t.time if isinstance(t.time, datetime) else None
            tick_timestamp = tick_time.timestamp() if tick_time else time.time()
            payload = {
                "symbol": symbol,
                "price": float(price),
                "bid": float(t.bid) if t.bid is not None and t.bid > 0 else None,
                "ask": float(t.ask) if t.ask is not None and t.ask > 0 else None,
                "volume": int(t.volume) if t.volume is not None else 0,
                "time": tick_time.isoformat() if tick_time else None,
                "timestamp": tick_timestamp,
                "change": 0.0,
                "changePercent": 0.0,
                "source": "IBKR Live",
                "live": True,
                "last_updated": time.time(),
            }
            self.market_data_cache[symbol] = payload
            self._dispatch_tick(payload)

    async def subscribe_market_data(self, symbol: str):
        """Subscribe to live market data for a symbol."""
        normalized_symbol = self._to_app_symbol(symbol)
        if normalized_symbol in self.subscribed_symbols and self._ib_connected():
            return

        if not self._ib_connected():
            await self.connect()

        if not self._ib_connected():
            return

        self.set_event_loop()

        contract, normalized_symbol = self._build_market_data_contract(symbol)
        qualified_contracts = await self.ib.qualifyContractsAsync(contract)
        if not qualified_contracts:
            logger.warning(f"[IBKR] Could not qualify contract for {normalized_symbol}")
            return

        contract = qualified_contracts[0]
        self._remember_contract_symbol(contract, normalized_symbol)
        self.ib.reqMktData(contract, '', False, False)
        self.subscribed_symbols.add(normalized_symbol)
        logger.info(f"📈 [IBKR] Subscribed to market data for {normalized_symbol}")

    def get_latest_quote(self, symbol: str, max_age_seconds: Optional[float] = None) -> Optional[Dict[str, Any]]:
        """Get the latest cached quote for a symbol."""
        latest = self.market_data_cache.get(symbol.upper())
        if not latest:
            return None

        if max_age_seconds is not None:
            last_updated = latest.get("last_updated")
            if not last_updated or (time.time() - last_updated) > max_age_seconds:
                return None

        return latest

    def get_last_tick_age(self, symbol: str) -> Optional[float]:
        latest = self.market_data_cache.get(symbol.upper())
        if not latest:
            return None

        last_updated = latest.get("last_updated")
        if not last_updated:
            return None

        return max(0.0, time.time() - last_updated)

    def has_fresh_tick(self, symbol: str, max_age_seconds: float = 3.0) -> bool:
        latest = self.market_data_cache.get(symbol.upper())
        if not latest:
            return False

        last_updated = latest.get("last_updated")
        if not last_updated:
            return False

        return (time.time() - last_updated) <= max_age_seconds

    def get_status(self) -> Dict[str, Any]:
        return {
            "connected": self._ib_connected(),
            "host": self.host,
            "configured_port": self.configured_port,
            "active_port": self.port if self._ib_connected() else None,
            "candidate_ports": self._get_port_candidates(),
            "last_connection_error": self.last_connection_error,
            "subscribed_symbols": sorted(self.subscribed_symbols),
            "cached_symbols": sorted(self.market_data_cache.keys()),
        }

# Singleton instance
ibkr_service = IBKRService()
