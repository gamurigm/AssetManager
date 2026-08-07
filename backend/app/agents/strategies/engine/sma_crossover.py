"""Simple, pure SMA crossover strategy compatible with IStrategyEngine."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .indicators import compute_ATR
from .models import CandleRow, StrategyConfig, TradeSignal
from .position_sizer import FixedFractionPositionSizer


@dataclass(frozen=True)
class SMACrossover:
    fast_period: int = 20
    slow_period: int = 50

    def __post_init__(self) -> None:
        if self.fast_period <= 0 or self.slow_period <= self.fast_period:
            raise ValueError("SMA periods must satisfy 0 < fast_period < slow_period")

    def run_session(
        self,
        m5_candles: List[CandleRow],
        m1_candles: List[CandleRow],
        account_size: float,
        config: StrategyConfig,
    ) -> List[TradeSignal]:
        if len(m1_candles) < self.slow_period + 1:
            return []

        closes = [float(candle["close"]) for candle in m1_candles]
        previous_fast = sum(closes[-self.fast_period - 1:-1]) / self.fast_period
        previous_slow = sum(closes[-self.slow_period - 1:-1]) / self.slow_period
        current_fast = sum(closes[-self.fast_period:]) / self.fast_period
        current_slow = sum(closes[-self.slow_period:]) / self.slow_period

        if previous_fast <= previous_slow and current_fast > current_slow:
            side = "LONG"
        elif previous_fast >= previous_slow and current_fast < current_slow:
            side = "SHORT"
        else:
            return []

        candle = m1_candles[-1]
        entry = float(candle["close"])
        atr = compute_ATR(m1_candles, period=14)
        risk_distance = max(atr, abs(entry) * 0.002)
        direction_sign = 1.0 if side == "LONG" else -1.0
        stop = entry - direction_sign * risk_distance
        target = entry + direction_sign * risk_distance * config.rr_target
        size = FixedFractionPositionSizer().calculate(
            account_size,
            config.risk_per_trade,
            risk_distance,
            1.0,
        )
        context = m5_candles[0] if m5_candles else candle

        return [
            TradeSignal(
                signal_id=f"SMA_CROSS:{candle['timestamp']}:{side}:{entry:.8f}",
                timestamp=str(candle["timestamp"]),
                direction=side,
                orh=float(context["high"]),
                orl=float(context["low"]),
                fvg_top=entry,
                fvg_bottom=entry,
                entry=entry,
                stop=stop,
                tp=target,
                risk_pips=risk_distance,
                position_size=size,
                confidence="standard",
                atr_m1=atr,
            )
        ]
