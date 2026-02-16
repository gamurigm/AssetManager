from openbb import obb
from typing import List, Dict, Any

class OpenBBService:
    @staticmethod
    async def get_stock_price(symbol: str) -> Dict[str, Any]:
        """Get current market price for a symbol using OpenBB."""
        try:
            # Note: obb functions are usually synchronous in the SDK
            # but we can wrap them if needed. 
            # In v4, many data providers are available.
            data = obb.equity.price.quote(symbol, provider="yfinance")
            return data.to_dict()
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def get_market_news(limit: int = 10) -> List[Dict[str, Any]]:
        """Get latest market news."""
        try:
            data = obb.news.world(limit=limit)
            return data.to_dict()
        except Exception as e:
            return []

openbb_service = OpenBBService()
