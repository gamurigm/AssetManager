import os
import sys
import time
import asyncio
import inspect
import logging
import socket
from datetime import datetime
from typing import Dict, Any, List, Optional, Callable, Tuple
import nest_asyncio
from ib_insync import IB, Contract, Forex, MarketOrder, Stock, util
# Patch asyncio for nestable loops (important for FastAPI + ib_insync)
nest_asyncio.apply()
util.patchAsyncio()

logger = logging.getLogger("MMAM")

class IBKRService:
    _DEFAULT_PORTS: Tuple[int, ...] = (7497, 4002, 7496, 4001, 4000)
    _FOREX_CODES = {
        "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "NZD", "HKD", "SGD",
        "SEK", "NOK", "DKK", "MXN", "CNY", "INR", "BRL", "ZAR", "TRY", "KRW",
        "THB", "PLN", "HUF", "CZK", "ILS", "CLP", "PHP", "IDR", "MYR", "RON",
    }

    _CONNECT_COOLDOWN_SECONDS: float = 1.0 # Reduced for debugging

    def __init__(self):
        self.ib: Optional[IB] = None
        self.host = os.getenv("IBKR_HOST", "127.0.0.1")
        self.configured_port = int(os.getenv("IBKR_PORT", 7497))
        self.port = self.configured_port
        # Use a high Client ID by default or from env to avoid collisions
        self.client_id = int(os.getenv("IBKR_CLIENT_ID", 101)) 
        self.is_connected = False
        self.last_connection_error: Optional[str] = None
        self._last_connect_attempt: float = 0.0
        self.market_data_cache: Dict[str, Any] = {}
        self.subscribed_symbols: set[str] = set()
        self._contract_symbols: Dict[str, str] = {}
        self._tick_listeners: List[Callable[[Dict[str, Any]], Any]] = []
        self._active_loop: Optional[asyncio.AbstractEventLoop] = None
        self._lock: Optional[asyncio.Lock] = None
        self._lock_loop: Optional[asyncio.AbstractEventLoop] = None
        self._pending_ticker_listener_registered = False
        self._is_connecting = False

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

    @classmethod
    def _normalize_order_symbol(cls, symbol: str) -> str:
        normalized = cls._normalize_symbol(symbol)
        compact = normalized.replace("=X", "").replace("/", "").replace(" ", "")
        return compact.upper()

    def _build_order_contract(
        self,
        symbol: str,
        asset_type: str = "stock",
        currency: str = "USD",
        exchange: Optional[str] = None,
        primary_exchange: Optional[str] = None,
        last_trade_date: Optional[str] = None,
    ):
        normalized_asset_type = str(asset_type or "stock").lower().strip()
        normalized_symbol = self._normalize_order_symbol(symbol)
        normalized_currency = str(currency or "USD").upper().strip()
        normalized_exchange = str(exchange).upper().strip() if exchange else None
        normalized_primary_exchange = (
            str(primary_exchange).upper().strip() if primary_exchange else None
        )

        if normalized_asset_type in {"stock", "equity", "stk"}:
            contract = Stock(normalized_symbol, normalized_exchange or "SMART", normalized_currency)
            if normalized_primary_exchange:
                contract.primaryExchange = normalized_primary_exchange
            return contract, normalized_symbol, "stock"

        if normalized_asset_type in {"forex", "fx", "cash"}:
            if not self._is_forex_symbol(normalized_symbol):
                raise ValueError("Forex symbols must be six-character pairs like EURUSD or EUR/USD")
            contract = Forex(normalized_symbol, exchange=normalized_exchange or "IDEALPRO")
            return contract, f"{normalized_symbol}=X", "forex"

        if normalized_asset_type in {"future", "futures", "fut"}:
            if not last_trade_date:
                raise ValueError("last_trade_date is required for futures orders")
            contract = Contract(
                symbol=normalized_symbol,
                secType="FUT",
                exchange=normalized_exchange or "CME",
                currency=normalized_currency,
                lastTradeDateOrContractMonth=str(last_trade_date),
            )
            return contract, normalized_symbol, "future"

        if normalized_asset_type == "crypto":
            contract = Contract(
                symbol=normalized_symbol,
                secType="CRYPTO",
                exchange=normalized_exchange or "PAXOS",
                currency=normalized_currency,
            )
            return contract, normalized_symbol, "crypto"

        raise ValueError(
            "Unsupported asset_type. Use stock, forex, future, or crypto"
        )

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

    async def _is_port_open_async(self, host: str, port: int, timeout: float = 0.5) -> bool:
        try:
            # Using asyncio.open_connection is non-blocking
            _, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout=timeout)
            writer.close()
            try:
                await writer.wait_closed()
            except:
                pass
            return True
        except:
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

        try:
            current_loop = asyncio.get_running_loop()
        except RuntimeError:
            return

        for listener in list(self._tick_listeners):
            try:
                result = listener(payload)
                if inspect.isawaitable(result):
                    if current_loop == self._active_loop:
                        current_loop.create_task(result)
                    else:
                        asyncio.run_coroutine_threadsafe(result, self._active_loop or current_loop)
            except Exception as exc:
                logger.error(f"[IBKR] Tick listener error: {exc}")
                
    def _get_loop(self):
        try:
            return asyncio.get_running_loop()
        except RuntimeError:
            return None

    async def _get_lock(self) -> asyncio.Lock:
        current_loop = asyncio.get_running_loop()
        if self._lock is None or self._lock_loop != current_loop:
            self._lock = asyncio.Lock()
            self._lock_loop = current_loop
        return self._lock

    def _ensure_ib_instance(self):
        """Create a fresh IB() instance if needed, ensuring loop affinity."""
        try:
            current_loop = asyncio.get_running_loop()
        except RuntimeError:
            return

        # On Windows, we MUST use SelectorEventLoop for ib_insync
        if sys.platform == 'win32':
            try:
                from asyncio import WindowsSelectorEventLoopPolicy
                if not isinstance(asyncio.get_event_loop_policy(), WindowsSelectorEventLoopPolicy):
                    asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
            except:
                pass

        needs_reset = False
        if self.ib is not None:
            internal_loop = getattr(self.ib, 'loop', None)
            if internal_loop and internal_loop != current_loop:
                logger.warning(f"[IBKR] Loop mismatch: resetting instance.")
                needs_reset = True
            elif self._active_loop and self._active_loop != current_loop:
                needs_reset = True
            
            if needs_reset:
                try: self.ib.disconnect()
                except: pass
                self.ib = None

        if self.ib is None:
            self.ib = IB()
            self._active_loop = current_loop
            self._pending_ticker_listener_registered = False
            self.is_connected = False
            logger.info(f"[IBKR] New IB instance created on {id(current_loop)}")

    def _validate_loop(self):
        """Ensure the IB instance is bound to the current event loop."""
        self._ensure_ib_instance()

    async def connect(self, force: bool = False):
        """Connect to TWS or IB Gateway."""
        self._validate_loop()
        if self._ib_connected():
            return

        lock = await self._get_lock()
        async with lock:
            if self._ib_connected():
                return
            
            # Cooldown check INSIDE the lock. Skips if 'force' is True (for orders)
            now = time.time()
            if not force and (now - self._last_connect_attempt < self._CONNECT_COOLDOWN_SECONDS):
                return
            
            self._is_connecting = True
            try:
                # Update attempt time
                self._last_connect_attempt = time.time()

                reachable_ports = []
                for port in self._get_port_candidates():
                    if await self._is_port_open_async(self.host, port):
                        reachable_ports.append(port)

                logger.info(f"[IBKR] Port scan results: {reachable_ports}")
                if not reachable_ports:
                    self.is_connected = False
                    tried_ports = ", ".join(str(port) for port in self._get_port_candidates())
                    self.last_connection_error = f"No reachable IBKR endpoint on {self.host}. Tried ports: {tried_ports}"
                    logger.warning(f"[IBKR] {self.last_connection_error}")
                    return

                self._ensure_ib_instance()
                logger.info(f"[IBKR] Using ClientID: {self.client_id}")

                for port in reachable_ports:
                    try:
                        logger.info(f"[IBKR] Attempting connection to {self.host}:{port} with ClientID {self.client_id} (timeout=10s)...")
                        await self.ib.connectAsync(self.host, port, clientId=self.client_id, timeout=10)
                        await asyncio.sleep(0.1)

                        if self.ib.isConnected():
                            self.is_connected = True
                            self.port = port
                            self.last_connection_error = None
                            if not self._pending_ticker_listener_registered:
                                self.ib.pendingTickersEvent += self._on_pending_tickers
                                self.ib.disconnectedEvent += self._on_disconnected
                                self._pending_ticker_listener_registered = True
                            logger.info(f"OK [IBKR] Connected to {self.host}:{self.port}")
                            return
                        else:
                            raise Exception("connectAsync completed but isConnected() is False")

                    except RuntimeError as e:
                        err_str = repr(e)
                        if "attached to a different loop" in err_str.lower():
                            logger.warning(f"[IBKR] Loop Error during connectAsync: {err_str}. Resetting and skipping port for now.")
                            self.ib = None
                            self._ensure_ib_instance()
                        continue
                    except Exception as e:
                        import traceback
                        err_type = type(e).__name__
                        err_str = repr(e)
                        full_trace = traceback.format_exc()
                        logger.warning(f"[IBKR] Port {port} failed ({err_type}): {err_str}")
                        
                        if any(x in err_str.lower() for x in ["different loop", "different thread", "different event loop"]):
                            self.ib = None
                            self._active_loop = None
                            self._ensure_ib_instance()
                            try:
                                await self.ib.connectAsync(self.host, port, clientId=self.client_id, timeout=10)
                                if self.ib.isConnected():
                                    self.is_connected = True
                                    self.port = port
                                    self.last_connection_error = None
                                    return
                            except:
                                pass

                        self.is_connected = False
                        self.last_connection_error = f"{self.host}:{port} -> [{err_type}] {err_str}"
            
            finally:
                self._is_connecting = False

    def disconnect(self):
        self._validate_loop()
        if self.ib is not None:
            if self._pending_ticker_listener_registered:
                try:
                    self.ib.pendingTickersEvent -= self._on_pending_tickers
                    self.ib.disconnectedEvent -= self._on_disconnected
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
        """Simple check if connected. Loop affinity is handled in connect()."""
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

    async def place_market_order(
        self,
        symbol: str,
        quantity: float,
        side: str,
        asset_type: str = "stock",
        currency: str = "USD",
        exchange: Optional[str] = None,
        primary_exchange: Optional[str] = None,
        last_trade_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Place a market order for a supported TWS/Gateway contract."""
        self._validate_loop()
        normalized_side = str(side or "").upper().strip()
        if normalized_side not in {"BUY", "SELL"}:
            return {"error": "side must be BUY or SELL"}

        self._validate_loop()
        if quantity <= 0:
            return {"error": "quantity must be > 0"}

        if not self._ib_connected():
            # Force connection attempt for real trading operations
            await self.connect(force=True)
        
        if not self._ib_connected():
            err_msg = self.last_connection_error or "Unknown connection failure."
            return {"error": f"Not connected to IBKR. {err_msg}"}

        try:
            contract, app_symbol, normalized_asset_type = self._build_order_contract(
                symbol=symbol,
                asset_type=asset_type,
                currency=currency,
                exchange=exchange,
                primary_exchange=primary_exchange,
                last_trade_date=last_trade_date,
            )
        except ValueError as exc:
            return {"error": str(exc)}

        try:
            qualified_contracts = await self.ib.qualifyContractsAsync(contract)
        except RuntimeError as e:
            logger.warning(f"[IBKR] Loop error during qualifyContractsAsync: {repr(e)}. Retrying once.")
            self._ensure_ib_instance()
            await self.connect(force=True)
            qualified_contracts = await self.ib.qualifyContractsAsync(contract)
        if not qualified_contracts:
            return {"error": f"Unable to qualify IBKR contract for {symbol}"}

        contract = qualified_contracts[0]
        self._remember_contract_symbol(contract, app_symbol)
        
        order = MarketOrder(normalized_side, quantity)
        trade = self.ib.placeOrder(contract, order)
        
        # Wait for the order to be filled or cancelled
        try:
            while not trade.isDone():
                await asyncio.sleep(0.1)
        except RuntimeError as e:
            if "different loop" in str(e):
                logger.error("[IBKR] Fatal loop error while waiting for order execution.")
            
        return {
            "symbol": app_symbol,
            "asset_type": normalized_asset_type,
            "exchange": getattr(contract, "exchange", None),
            "currency": getattr(contract, "currency", None),
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

    def _on_disconnected(self):
        """Callback for connection loss."""
        self.is_connected = False
        logger.warning("🔌 [IBKR] Connection lost. Will attempt to reconnect on next operation.")
        # Optional: could trigger a background reconnect task here but place_market_order does it 

    async def subscribe_market_data(self, symbol: str):
        """Subscribe to live market data for a symbol."""
        try:
            normalized_symbol = self._to_app_symbol(symbol)
            if normalized_symbol in self.subscribed_symbols and self._ib_connected():
                return

            if not self._ib_connected():
                await self.connect()

            if not self._ib_connected():
                return

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
        except Exception as exc:
            logger.error(f"[IBKR] Error subscribing to {symbol}: {repr(exc)}")

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
        """Get the current status of the IBKR connection."""
        try:
            self._validate_loop()
        except:
            pass
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
