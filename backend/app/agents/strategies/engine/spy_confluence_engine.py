from app.agents.strategies.engine.interfaces import IStrategyEngine
from app.agents.strategies.engine.models import StrategyConfig, TradeSignal
from typing import List

class SPYConfluenceEngine(IStrategyEngine):
    def run_session(self, m5_candles: List[dict], m1_candles: List[dict], account_size: float, config: StrategyConfig) -> List[TradeSignal]:
        # Implementation here
        return []
