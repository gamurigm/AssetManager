import os
import sys
import time
import asyncio
import threading
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional, Callable, Tuple
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order

logger = logging.getLogger("MMAM")

class TWSClient(EWrapper, EClient):
    """OFFICIAL IBAPI (pure) implementation client."""
    def __init__(self, service):
        EClient.__init__(self, self)
        self.service = service
        self._next_valid_id = None
        self._id_event = threading.Event()
        self._connection_event = threading.Event()
        self._is_connected = False
        self.futures: Dict[int, asyncio.Future] = {}
        self.order_status: Dict[int, Dict[str, Any]] = {}
        self._order_events: Dict[int, threading.Event] = {}
        self.account_summary: List[Dict[str, Any]] = []
        self._account_summary_event = threading.Event()
        self.positions: List[Dict[str, Any]] = []
        self._positions_event = threading.Event()
        
    def error(self, reqId: int, errorCode: int, errorString: str, advancedOrderRejectJson: str = ""):
        if errorCode in [2104, 2106, 2158]: # Connection status info
            logger.info(f"[IBAPI] {errorCode}: {errorString}")
        else:
            logger.warning(f"[IBAPI] Error {errorCode}: {errorString}")
            # Signal any waiting orders that an error occurred
            if reqId in self._order_events:
                self.order_status[reqId] = {"status": f"Error:{errorCode}", "filled": 0.0}
                self._order_events[reqId].set()

            if reqId in self.futures:
                loop = self.service._get_loop()
                if loop and loop.is_running():
                    loop.call_soon_threadsafe(
                        self.futures[reqId].set_exception, 
                        Exception(f"IBKR Error {errorCode}: {errorString}")
                    )
                del self.futures[reqId]

    def nextValidId(self, orderId: int):
        self._next_valid_id = orderId
        self._id_event.set()
        logger.info(f"[IBAPI] Next valid order ID: {orderId}")

    def connectAck(self):
        self._is_connected = True
        self._connection_event.set()
        logger.info("[IBAPI] Connection acknowledged.")

    def connectionClosed(self):
        self._is_connected = False
        self._connection_event.clear()
        self.service.is_connected = False
        logger.warning("[IBAPI] Connection closed.")

    # --- Market Data ---
    def tickPrice(self, reqId: int, tickType: int, price: float, attrib: Any):
        # TickTypes: 1=bid, 2=ask, 4=last, 9=close
        symbol = self.service._req_id_to_symbol.get(reqId)
        if not symbol or price <= 0:
            return
            
        payload = self.service.market_data_cache.get(symbol, {
            "symbol": symbol,
            "source": "IBKR Live",
            "live": True,
            "timestamp": time.time(),
        })
        
        updated = False
        if tickType == 1: # BID
            payload["bid"] = price
            updated = True
        elif tickType == 2: # ASK
            payload["ask"] = price
            updated = True
        elif tickType in [4, 9]: # LAST or CLOSE fallback
            payload["price"] = price
            updated = True
            
        if updated:
            payload["last_updated"] = time.time()
            self.service.market_data_cache[symbol] = payload
            self.service._dispatch_tick(payload)

    def tickSize(self, reqId: int, tickType: int, size: int):
        # TickType 8 = Volume
        if tickType == 8:
            symbol = self.service._req_id_to_symbol.get(reqId)
            if symbol:
                payload = self.service.market_data_cache.get(symbol, {"symbol": symbol})
                payload["volume"] = size
                self.service.market_data_cache[symbol] = payload

    # --- Account & Positions ---
    def accountSummary(self, reqId: int, account: str, tag: str, value: str, currency: str):
        self.account_summary.append({"tag": tag, "value": value, "currency": currency})

    def accountSummaryEnd(self, reqId: int):
        self._account_summary_event.set()

    def position(self, account: str, contract: Contract, position: float, avgCost: float):
        self.positions.append({
            "account": account,
            "symbol": contract.symbol,
            "position": position,
            "avgCost": avgCost
        })

    def positionEnd(self):
        self._positions_event.set()

    # --- Orders ---
    def orderStatus(self, orderId: int, status: str, filled: float, remaining: float, 
                    avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, 
                    clientId: int, whyHeld: str, mktCapPrice: float):
        logger.info(f"[IBAPI] Order {orderId} state: {status}, filled: {filled}")
        
        self.order_status[orderId] = {
            "status": status,
            "filled": filled,
            "remaining": remaining,
            "avgFillPrice": avgFillPrice
        }
        
        # If the order is in a final state, signal the waiter
        if status in ["Filled", "Cancelled", "Inactive", "ApiCancelled"]:
            if orderId in self._order_events:
                self._order_events[orderId].set()

class IBKRService:
    _DEFAULT_PORTS: Tuple[int, ...] = (7497, 4002, 7496, 4001, 4000)
    _FOREX_CODES = {
        "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "NZD", "HKD", "SGD",
        "SEK", "NOK", "DKK", "MXN", "CNY", "INR", "BRL", "ZAR", "TRY", "KRW",
        "THB", "PLN", "HUF", "CZK", "ILS", "CLP", "PHP", "IDR", "MYR", "RON",
    }

    def __init__(self):
        self.client: Optional[TWSClient] = None
        self.host = os.getenv("IBKR_HOST", "127.0.0.1")
        self.configured_port = int(os.getenv("IBKR_PORT", 7497))
        self.client_id = int(os.getenv("IBKR_CLIENT_ID", 101))
        self.is_connected = False
        self.last_connection_error = None
        self.market_data_cache: Dict[str, Any] = {}
        self.subscribed_symbols: set[str] = set()
        self._tick_listeners: List[Callable[[Dict[str, Any]], Any]] = []
        self._req_id_to_symbol: Dict[int, str] = {}
        self._symbol_to_req_id: Dict[str, int] = {}
        self._contract_symbols: Dict[tuple, str] = {}
        self._next_req_id = 1000
        self._client_thread: Optional[threading.Thread] = None
        self._loop: Optional[asyncio.AbstractEventLoop] = None

    def _get_loop(self):
        if self._loop and not self._loop.is_closed():
            return self._loop
        try:
            return asyncio.get_running_loop()
        except RuntimeError:
            return None

    def set_event_loop(self, loop):
        """Register the application loop used for thread-safe tick dispatch."""
        self._loop = loop

    def _ib_connected(self) -> bool:
        return bool(
            self.is_connected
            and self.client is not None
            and self.client.isConnected()
        )

    def _get_port_candidates(self) -> List[int]:
        configured = [self.configured_port]
        raw_candidates = os.getenv("IBKR_PORT_CANDIDATES", "")
        configured.extend(
            int(value.strip())
            for value in raw_candidates.split(",")
            if value.strip().isdigit()
        )
        configured.extend(self._DEFAULT_PORTS)
        return list(dict.fromkeys(configured))

    @classmethod
    def _to_app_symbol(cls, symbol: str) -> str:
        normalized = symbol.strip().upper().replace("/", "").replace("=X", "")
        if (
            len(normalized) == 6
            and normalized[:3] in cls._FOREX_CODES
            and normalized[3:] in cls._FOREX_CODES
        ):
            return f"{normalized}=X"
        return symbol.strip().upper()

    @staticmethod
    def _contract_key(contract: Contract) -> tuple:
        con_id = int(getattr(contract, "conId", 0) or 0)
        if con_id:
            return ("conId", con_id)
        return (
            str(getattr(contract, "secType", "")),
            str(getattr(contract, "symbol", "")),
            str(getattr(contract, "currency", "")),
            str(getattr(contract, "exchange", "")),
        )

    def _remember_contract_symbol(self, contract: Contract, app_symbol: str) -> None:
        self._contract_symbols[self._contract_key(contract)] = app_symbol

    def _resolve_app_symbol(self, contract: Contract) -> str:
        remembered = self._contract_symbols.get(self._contract_key(contract))
        if remembered:
            return remembered
        if str(getattr(contract, "secType", "")).upper() == "CASH":
            return self._to_app_symbol(
                f"{getattr(contract, 'symbol', '')}{getattr(contract, 'currency', '')}"
            )
        return str(getattr(contract, "symbol", "")).upper()

    def _build_market_data_contract(self, symbol: str) -> Tuple[Contract, str]:
        app_symbol = self._to_app_symbol(symbol)
        contract = Contract()
        if app_symbol.endswith("=X"):
            pair = app_symbol[:-2]
            contract.symbol = pair[:3]
            contract.currency = pair[3:6]
            contract.secType = "CASH"
            contract.exchange = "IDEALPRO"
        else:
            contract.symbol = app_symbol
            contract.currency = "USD"
            contract.secType = "STK"
            contract.exchange = "SMART"
        self._remember_contract_symbol(contract, app_symbol)
        return contract, app_symbol

    def _build_order_contract(
        self,
        symbol: str,
        *,
        asset_type: str = "stock",
        currency: str = "USD",
        exchange: Optional[str] = None,
        primary_exchange: Optional[str] = None,
        last_trade_date: Optional[str] = None,
    ) -> Tuple[Contract, str, str]:
        normalized_type = asset_type.strip().lower()
        contract = Contract()
        if normalized_type in {"forex", "fx", "cash"}:
            contract, app_symbol = self._build_market_data_contract(
                self._to_app_symbol(symbol)
            )
            return contract, app_symbol, "forex"

        app_symbol = symbol.strip().upper()
        contract.symbol = app_symbol
        contract.currency = currency.strip().upper()
        if normalized_type in {"stock", "equity"}:
            canonical_type = "stock"
            contract.secType = "STK"
            contract.exchange = exchange or "SMART"
        elif normalized_type in {"future", "futures"}:
            canonical_type = "future"
            contract.secType = "FUT"
            contract.exchange = exchange or "CME"
            contract.lastTradeDateOrContractMonth = last_trade_date or ""
        elif normalized_type == "crypto":
            canonical_type = "crypto"
            contract.secType = "CRYPTO"
            contract.exchange = exchange or "PAXOS"
        else:
            raise ValueError(f"Unsupported IBKR asset_type '{asset_type}'")
        if primary_exchange:
            contract.primaryExchange = primary_exchange
        self._remember_contract_symbol(contract, app_symbol)
        return contract, app_symbol, canonical_type

    def has_fresh_tick(self, symbol: str, max_age: float = 5.0) -> bool:
        """Check if we have a recent tick (within max_age seconds)."""
        symbol = symbol.upper()
        payload = self.market_data_cache.get(symbol)
        if not payload: return False
        return (time.time() - payload.get("last_updated", 0)) <= max_age

    def get_latest_quote(
        self,
        symbol: str,
        max_age_seconds: float = 5.0,
    ) -> Optional[Dict[str, Any]]:
        app_symbol = self._to_app_symbol(symbol)
        if not self.has_fresh_tick(app_symbol, max_age_seconds):
            return None
        return dict(self.market_data_cache[app_symbol])

    def _dispatch_tick(self, payload: Dict[str, Any]):
        """Dispatches ticks to listeners in a thread-safe manner."""
        loop = self._get_loop()
        if not loop or not loop.is_running(): 
            return

        def _notify():
            if loop.is_closed(): return
            for listener in list(self._tick_listeners):
                try:
                    res = listener(payload)
                    if asyncio.iscoroutine(res):
                        loop.create_task(res)
                except Exception as e:
                    logger.error(f"[IBKR] Listener error: {e}")
        
        try:
            loop.call_soon_threadsafe(_notify)
        except RuntimeError:
            pass # Loop is likely closing

    def add_tick_listener(self, listener: Callable):
        if listener not in self._tick_listeners:
            self._tick_listeners.append(listener)

    def remove_tick_listener(self, listener: Callable):
        if listener in self._tick_listeners:
            self._tick_listeners.remove(listener)

    async def connect(self):
        """Connect to TWS via separate thread."""
        self._loop = asyncio.get_running_loop()
        if self.is_connected and self.client and self.client.isConnected():
            return
            
        logger.info(f"[IBKR] Starting IBAPI connection thread to {self.host}:{self.configured_port}...")
        self.client = TWSClient(self)
        self.client.connect(self.host, self.configured_port, self.client_id)
        
        self._client_thread = threading.Thread(target=self.client.run, daemon=True)
        self._client_thread.start()
        
        # Wait for connection acknowledge
        connected = await asyncio.to_thread(self.client._connection_event.wait, timeout=5.0)
        if connected and self.client.isConnected():
            self.is_connected = True
            self.last_connection_error = None
            # Fetch valid IDs
            await asyncio.to_thread(self.client._id_event.wait, timeout=2.0)
            
            # Set market data type to 3 (Delayed) to ensure we get data in Paper accounts
            # without active real-time subscriptions for US Stocks/Futures.
            self.client.reqMarketDataType(3) 
            
            logger.info("✅ [IBKR] Pure IBAPI successfully connected (Delayed Data Enabled).")
        else:
            self.is_connected = False
            self.last_connection_error = "Connection timeout"
            logger.error("❌ [IBKR] Connection timeout.")

    def disconnect(self):
        """Shutdown IBKR connection."""
        if self.client:
            self.client.disconnect()
            self.is_connected = False
            self.subscribed_symbols.clear()
            self._req_id_to_symbol.clear()
            self._symbol_to_req_id.clear()
            logger.info("🔌 [IBKR] Disconnected (Pure IBAPI).")

    async def get_account_summary(self) -> List[Dict[str, Any]]:
        if not self.is_connected: await self.connect()
        if not self.is_connected: return [{"error": "Not connected"}]
        
        self.client.account_summary = []
        self.client._account_summary_event.clear()
        self.client.reqAccountSummary(9001, "All", "NetLiquidation,TotalCashValue,SettledCash,BuyingPower")
        
        await asyncio.to_thread(self.client._account_summary_event.wait, timeout=5.0)
        self.client.cancelAccountSummary(9001)
        return self.client.account_summary

    async def get_positions(self) -> List[Dict[str, Any]]:
        if not self.is_connected: await self.connect()
        if not self.is_connected: return []
        
        self.client.positions = []
        self.client._positions_event.clear()
        self.client.reqPositions()
        
        await asyncio.to_thread(self.client._positions_event.wait, timeout=5.0)
        return self.client.positions

    async def subscribe_market_data(self, symbol: str):
        if not self.is_connected: await self.connect()
        if not self.is_connected: return
        
        symbol = self._to_app_symbol(symbol)
        if symbol in self.subscribed_symbols: return
        contract, symbol = self._build_market_data_contract(symbol)

        req_id = self._next_req_id
        self._next_req_id += 1
        self._req_id_to_symbol[req_id] = symbol
        self._symbol_to_req_id[symbol] = req_id
        
        self.client.reqMktData(req_id, contract, "", False, False, [])
        self.subscribed_symbols.add(symbol)
        logger.info(f"📈 [IBAPI] Subscribed to {symbol} (ReqId: {req_id})")

    async def place_market_order(self, symbol: str, quantity: float, side: str, **kwargs) -> Dict[str, Any]:
        normalized_side = side.strip().upper()
        if normalized_side not in {"BUY", "SELL"}:
            return {"error": "side must be BUY or SELL"}
        if quantity <= 0:
            return {"error": "quantity must be greater than zero"}
        if not self.is_connected: await self.connect()
        if not self.is_connected: return {"error": "Not connected"}
        
        # Fresh ID check
        self.client._id_event.clear()
        self.client.reqIds(-1)
        await asyncio.to_thread(self.client._id_event.wait, timeout=2.0)
        
        order_id = self.client._next_valid_id
        if order_id is None:
            return {"error": "IBKR did not provide a valid order ID"}
        try:
            contract, app_symbol, asset_type = self._build_order_contract(
                symbol,
                asset_type=str(kwargs.get("asset_type", "stock")),
                currency=str(kwargs.get("currency", "USD")),
                exchange=kwargs.get("exchange"),
                primary_exchange=kwargs.get("primary_exchange"),
                last_trade_date=kwargs.get("last_trade_date"),
            )
        except ValueError as exc:
            return {"error": str(exc)}
        
        order = Order()
        order.action = normalized_side
        order.orderType = "MKT"
        order.totalQuantity = quantity
        # Set explicitly to False to avoid error 10268 on some exchange/account types
        order.eTradeOnly = False
        order.firmQuoteOnly = False
        
        # Setup tracking BEFORE placing
        done_event = threading.Event()
        self.client._order_events[order_id] = done_event
        
        self.client.placeOrder(order_id, contract, order)
        
        # Wait for the order to reach a final state (Filled/Cancelled)
        # We use a timeout to avoid hanging forever if TWS doesn't respond
        await asyncio.to_thread(done_event.wait, timeout=30.0)
        
        # Get final result
        res = self.client.order_status.get(order_id, {"status": "Unknown", "filled": 0.0})
        
        # Cleanup
        self.client._order_events.pop(order_id, None)
        
        return {
            "status": res["status"],
            "orderId": order_id,
            "symbol": app_symbol,
            "filled": res.get("filled", 0.0),
            "avgFillPrice": res.get("avgFillPrice", 0.0),
            "asset_type": asset_type
        }

    def get_status(self) -> Dict[str, Any]:
        return {
            "connected": self._ib_connected(),
            "host": self.host,
            "port": self.configured_port,
            "subscribed_count": len(self.subscribed_symbols)
        }

ibkr_service = IBKRService()
