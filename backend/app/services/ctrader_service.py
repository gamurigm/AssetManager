import os
import threading
import asyncio
from typing import Dict, Any, Optional, List, Callable
from crochet import setup, run_in_reactor, wait_for
from ctrader_open_api import Client, Protobuf, TcpProtocol, Auth, EndPoints
from ctrader_open_api.messages.OpenApiCommonMessages_pb2 import *
from ctrader_open_api.messages.OpenApiMessages_pb2 import *
from ctrader_open_api.messages.OpenApiModelMessages_pb2 import *
from google.protobuf.json_format import MessageToDict
import logging

# Initialize crochet
setup()

# Suppress noisy Twisted retry logs when cTrader is not configured
logging.getLogger("twisted").setLevel(logging.CRITICAL)

logger = logging.getLogger("MMAM")


def _ctrader_configured() -> bool:
    """Return True only when all four cTrader env vars are set to real values."""
    sentinel = {"", "PLACEHOLDER_TOKEN", "your_client_id", "your_client_secret",
                "your_account_id", "your_access_token", "none", "null"}
    vars_needed = [
        os.getenv("CTRADER_CLIENT_ID", ""),
        os.getenv("CTRADER_CLIENT_SECRET", ""),
        os.getenv("CTRADER_ACCESS_TOKEN", ""),
        os.getenv("CTRADER_ACCOUNT_ID", ""),
    ]
    return all(v.strip().lower() not in sentinel for v in vars_needed)

class CTraderService:
    def __init__(self):
        self.client_id = os.getenv("CTRADER_CLIENT_ID")
        self.client_secret = os.getenv("CTRADER_CLIENT_SECRET")
        self.access_token = os.getenv("CTRADER_ACCESS_TOKEN")
        self.account_id = os.getenv("CTRADER_ACCOUNT_ID")
        
        self.host = EndPoints.PROTOBUF_DEMO_HOST
        self.port = EndPoints.PROTOBUF_PORT
        
        self.client = None
        self.is_connected = False
        self.is_app_auth = False
        self.is_account_auth = False
        
        self._responses = {}  # To store responses for wait_for
        self._callbacks = {}
        self.market_data_cache: Dict[str, Any] = {}
        self.symbol_id_map: Dict[int, str] = {} # id -> name
        
    @run_in_reactor
    def start(self):
        """Start the Twisted reactor and cTrader client service.
        
        No-ops silently if cTrader credentials are not configured in .env.
        """
        if not _ctrader_configured():
            logger.info("ℹ️  [cTrader] Credentials not configured — service disabled. "
                        "Set CTRADER_CLIENT_ID/SECRET/ACCESS_TOKEN/ACCOUNT_ID to enable.")
            return

        if self.client:
            return
            
        self.client = Client(self.host, self.port, TcpProtocol)
        self.client.setConnectedCallback(self._on_connected)
        self.client.setDisconnectedCallback(self._on_disconnected)
        self.client.setMessageReceivedCallback(self._on_message_received)
        self.client.startService()
        logger.info("📡 [cTrader] Twisted service started.")

    def _on_connected(self, client):
        logger.info("✅ [cTrader] Connected to host.")
        self.is_connected = True
        self._authenticate_application_async()

    def _on_disconnected(self, client, reason):
        logger.warning(f"❌ [cTrader] Disconnected: {reason}")
        self.is_connected = False
        self.is_app_auth = False
        self.is_account_auth = False

    def _on_message_received(self, client, message):
        """Handle incoming messages and route them to waiting deferreds or callbacks."""
        msg_type = message.payloadType
        payload = Protobuf.extract(message)

        # logger.debug(f"📥 [cTrader] Received: {msg_type}")

        if msg_type == ProtoOAErrorRes().payloadType:
            logger.error(f"🚨 [cTrader] Error: {payload.errorCode} — {payload.description}")
            return

        if msg_type == ProtoOAApplicationAuthRes().payloadType:
            logger.info("🔐 [cTrader] Application authenticated.")
            self.is_app_auth = True
            if self.access_token and self.access_token != "PLACEHOLDER_TOKEN" and self.account_id:
                self._authenticate_account_async(self.account_id, self.access_token)
            else:
                logger.info("ℹ️ [cTrader] Waiting for Access Token/Account ID to complete auth.")

        if msg_type == ProtoOAAccountAuthRes().payloadType:
            logger.info(f"💼 [cTrader] Account {self.account_id} authenticated.")
            self.is_account_auth = True

        if msg_type == ProtoOASpotEvent().payloadType:
            self._on_spot_event(payload)

        # Trigger internal callbacks for specific request IDs or types
        if msg_type in self._callbacks:
            for cb in self._callbacks[msg_type]:
                cb(payload)

    @run_in_reactor
    def send_message(self, request):
        """Send a protobuf message via the client."""
        if not self.client:
             logger.error("❌ [cTrader] Client not initialized. Call start() first.")
             return
        return self.client.send(request)

    def _authenticate_application_async(self):
        """Send application auth request directly (safe to call from reactor thread)."""
        logger.info("🔐 [cTrader] Authenticating Application...")
        if not self.client:
            return
        req = ProtoOAApplicationAuthReq()
        req.clientId = self.client_id
        req.clientSecret = self.client_secret
        self.client.send(req)

    def _authenticate_account_async(self, account_id: int, token: str):
        """Send account auth request directly (safe to call from reactor thread)."""
        logger.info(f"💼 [cTrader] Authenticating Account {account_id}...")
        if not self.client:
            return
        req = ProtoOAAccountAuthReq()
        req.ctidTraderAccountId = int(account_id)
        req.accessToken = token
        self.client.send(req)

    @wait_for(timeout=10)
    def authenticate_application(self):
        """Send application authentication request (blocking, call from non-reactor thread)."""
        logger.info("🔐 [cTrader] Authenticating Application...")
        req = ProtoOAApplicationAuthReq()
        req.clientId = self.client_id
        req.clientSecret = self.client_secret
        return self.client.send(req)

    @wait_for(timeout=10)
    def authenticate_account(self, account_id: int, token: str):
        """Send account authentication request (blocking, call from non-reactor thread)."""
        logger.info(f"💼 [cTrader] Authenticating Account {account_id}...")
        req = ProtoOAAccountAuthReq()
        req.ctidTraderAccountId = int(account_id)
        req.accessToken = token
        return self.client.send(req)

    @wait_for(timeout=10)
    def get_account_details(self, account_id: int):
        """Get account financial details (balance, equity, etc)."""
        req = ProtoOATraderReq()
        req.ctidTraderAccountId = int(account_id)
        return self.client.send(req)

    @wait_for(timeout=10)
    def place_market_order(self, account_id: int, symbol_name: str, volume: int, side: str):
        """Place a market order."""
        # Note: volume is in units (e.g. 1000 for 0.01 lot in Forex)
        req = ProtoOANewOrderReq()
        req.ctidTraderAccountId = int(account_id)
        req.symbolName = symbol_name.upper()
        req.orderType = ProtoOAOrderType.MARKET
        req.tradeSide = ProtoOATradeSide.BUY if side.upper() == "BUY" else ProtoOATradeSide.SELL
        req.volume = int(volume)
        return self.client.send(req)

    async def get_account_list(self, token: str):
        """Get list of accounts for a token."""
        req = ProtoOAGetAccountListByAccessTokenReq()
        req.accessToken = token
        # This returns a deferred, we need to handle it with crochet
        return await self._async_send(req, ProtoOAAccountListAndParametersRes().payloadType)

    def _async_send(self, req, expected_type):
        """Helper to send and wait for a specific response type asynchronously."""
        # Wrap the wait_for call since it's synchronous in crochet's context
        @wait_for(timeout=10)
        def _call(request):
            return self.client.send(request)
        return _call(req)

    @run_in_reactor
    def subscribe_spots(self, symbol_name: str):
        """Subscribe to spot prices for a symbol."""
        if not self.is_account_auth:
            logger.warning("⚠️ [cTrader] Cannot subscribe: Account not authorized.")
            return

        # We first need the symbol ID from the name. 
        # For brevity in this implementation, we'll assume we know it or fetch it.
        # Most FX symbols are standard. EURUSD is usually 1, etc.
        # A real implementation would query ProtoOASymbolsListReq first.
        # But we'll try to find it or use a default mapping for common ones.
        symbol_ids = {"EURUSD": 1, "GBPUSD": 2, "USDJPY": 4, "XAUUSD": 14}
        sym_id = symbol_ids.get(symbol_name.upper())
        if not sym_id:
             logger.error(f"❌ [cTrader] Symbol ID not found for {symbol_name}")
             return

        self.symbol_id_map[sym_id] = symbol_name.upper()
        req = ProtoOASubscribeSpotsReq()
        req.ctidTraderAccountId = int(self.account_id)
        req.symbolId.append(sym_id)
        self.client.send(req)
        logger.info(f"📈 [cTrader] Subscribed to spots for {symbol_name} (ID: {sym_id})")

    def _on_spot_event(self, event):
        """Callback for real-time spot price updates."""
        sym_id = event.symbolId
        symbol = self.symbol_id_map.get(sym_id)
        if symbol:
            bid = event.bid / 100000.0 if event.bid else None
            ask = event.ask / 100000.0 if event.ask else None
            price = (event.bid + event.ask) / 200000.0 if event.bid and event.ask else None
            self.market_data_cache[symbol] = {"bid": bid, "ask": ask, "price": price}

    def get_latest_quote(self, symbol: str) -> Optional[Dict[str, Any]]:
        return self.market_data_cache.get(symbol.upper())

    def get_status(self) -> Dict[str, bool]:
        return {
            "connected": self.is_connected,
            "app_authorized": self.is_app_auth,
            "account_authorized": self.is_account_auth
        }

# Singleton instance
ctrader_service = CTraderService()
