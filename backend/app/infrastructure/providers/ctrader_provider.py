from typing import Optional, List
from ...domain.interfaces.market_provider import IMarketDataProvider
from ...domain.entities.market import Quote, Candle
from ...services.ctrader_service import ctrader_service

class CTraderProvider(IMarketDataProvider):
    """
    cTrader Market Data Provider.
    Handles Forex and Spot prices.
    """

    @property
    def name(self) -> str:
        return "ctrader"

    async def get_quote(self, symbol: str) -> Optional[Quote]:
        """Fetch real-time spot quote from cTrader service."""
        try:
            latest = ctrader_service.get_latest_quote(symbol)
            if not latest:
                # Lazy subscription
                ctrader_service.subscribe_spots(symbol)
                return None
            
            return Quote(
                symbol=symbol,
                price=float(latest["price"]) if latest["price"] else 0.0,
                change=0.0,
                change_percent=0.0,
                volume=0, # Volume info not always in basic spot events
                source="cTrader Live"
            )
        except Exception as e:
            print(f"[CTraderProvider] Error for {symbol}: {e}")
            return None

    async def get_historical(
        self, symbol: str, limit: int = 300, start_date: Optional[str] = None
    ) -> Optional[List[Candle]]:
        """Historical data from cTrader is handled via Protobuf messages if needed."""
        return None
