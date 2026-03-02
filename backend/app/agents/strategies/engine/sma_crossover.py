from dataclasses import dataclass
from typing import Optional
from .interfaces import IStrategyEngine
from app.agents.strategies.engine import TradeSignal
import pandas as pd

@dataclass
class SMACrossover(IStrategyEngine):
    def run_session(self, symbol: str, data: pd.DataFrame) -> Optional[TradeSignal]:
        # Calculate SMAs
        sma20 = data['close'].rolling(window=20).mean()
        sma50 = data['close'].rolling(window=50).mean()

        # Generate signals
        if sma20.iloc[-1] > sma50.iloc[-1] and sma20.iloc[-2] <= sma50.iloc[-2]:
            return TradeSignal(symbol=symbol, direction='Long', entry_price=data['close'].iloc[-1])
        elif sma20.iloc[-1] < sma50.iloc[-1] and sma20.iloc[-2] >= sma50.iloc[-2]:
            return TradeSignal(symbol=symbol, direction='Short', entry_price=data['close'].iloc[-1])
        return None