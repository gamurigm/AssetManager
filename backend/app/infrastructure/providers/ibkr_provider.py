from typing import Optional, List
from ...domain.interfaces.market_provider import IMarketDataProvider
from ...domain.entities.market import Quote, Candle
from ...services.ibkr_service import ibkr_service

class IBKRProvider(IMarketDataProvider):
    """
    Interactive Brokers Market Data Provider.
    Prioritizes live data from TWS/Gateway.
    """

    @property
    def name(self) -> str:
        return "ibkr"

    async def get_quote(self, symbol: str) -> Optional[Quote]:
        """Fetch a real-time quote from the IBKR service cache."""
        try:
            # First, ensure we are subscribed to market data for this symbol
            # (In a real high-throughput system, subscription would be managed elsewhere,
            # but for this app's "RealtimeService" polling, we check/subscribe here.)
            latest = ibkr_service.get_latest_quote(symbol, max_age_seconds=3.0)
            
            if not latest:
                # If not cached, trigger a subscription (lazy init)
                await ibkr_service.subscribe_market_data(symbol)
                return None # Return None for the first call until data arrives
            
            return Quote(
                symbol=symbol,
                price=float(latest["price"]),
                change=float(latest.get("change", 0.0)),
                change_percent=float(latest.get("changePercent", 0.0)),
                volume=int(latest.get("volume", 0)),
                source=latest.get("source", "IBKR Live")
            )
        except Exception as e:
            print(f"[IBKRProvider] Error for {symbol}: {e}")
            return None

    async def get_historical(
        self, symbol: str, limit: int = 300, start_date: Optional[str] = None
    ) -> Optional[List[Candle]]:
        """
        Historical data for IBKR is handled via the TWS API.
        For now, we can fallback to other providers for history strings
        or implement the full reqHistoricalData if needed.
        """
        # Fallback to next provider in chain for history
        return None
