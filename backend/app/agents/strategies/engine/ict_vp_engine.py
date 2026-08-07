"""
ICT + Volume Profile Engine (ict_vp_engine.py)
==============================================
Implements IStrategyEngine.
Logic:
1. Computes rolling Volume Profile (VP) over the current session.
2. Identifies Liquidity Sweeps (price breaking a previous swing high/low).
3. If the sweep taps an HVN edge and rejects it (pin bar / engulfing).
4. Waits for an FVG to form in the reversal direction as confirmation.
5. Executes Limit order at the FVG.
"""

from __future__ import annotations

from typing import List, Optional

from .models import CandleRow, StrategyConfig, FVG, TradeSignal
from .position_sizer import FixedFractionPositionSizer
from .volume_profile import VolumeProfileCalculator, VolumeProfileResult
from .indicators import compute_ATR, is_bullish, is_bearish

class ICTSessionState:
    def __init__(self):
        self.vp_result: Optional[VolumeProfileResult] = None
        self.sweep_detected = False
        self.sweep_direction: Optional[str] = None # 'bullish' (swept lows, looking long) or 'bearish'
        self.rejection_detected = False
        self.fvg: Optional[FVG] = None
        self.fvg_countdown = 0
        self.setup_active = False

class IctVpEngine:
    """Strategy Engine for ICT + Volume Profile."""
    
    def __init__(self):
        self.vp_calc = VolumeProfileCalculator(num_bins=50, value_area_pct=0.70, hvn_threshold_pct=0.5)

    def run_session(
        self,
        m5_candles: List[CandleRow],
        m1_candles: List[CandleRow],
        account_size: float,
        config: StrategyConfig,
    ) -> List[TradeSignal]:
        
        if len(m1_candles) < 30: # Need some data to build a profile and swings
            return []

        state = ICTSessionState()
        prev_candle: Optional[CandleRow] = None

        for idx, candle in enumerate(m1_candles):
            if idx < 15: # Skip first 15 mins to let the day develop a bit of structure
                prev_candle = candle
                continue

            current_buffer = m1_candles[max(0, idx - 19):idx + 1]
            atr_m1 = compute_ATR(current_buffer, period=14)
                
            # 1. Update rolling Volume Profile
            # Note: in real-time, this would be computed up to idx.
            # Doing it every minute is fast enough with Numpy.
            state.vp_result = self.vp_calc.compute(m1_candles[:idx])

            # 2. Detect Liquidity Sweep + Tap at HVN
            if not state.sweep_detected:
                # Find swing extremes of the session so far
                swing_high = max(c["high"] for c in m1_candles[:idx])
                swing_low = min(c["low"] for c in m1_candles[:idx])
                
                # Check for sweep
                swept_high = candle["high"] > swing_high
                swept_low = candle["low"] < swing_low
                
                if swept_high or swept_low:
                    # Verify if it tapped an HVN edge
                    if state.vp_result and self._tapped_hvn(candle, state.vp_result):
                        state.sweep_detected = True
                        state.sweep_direction = "bearish" if swept_high else "bullish"
                        # We need immediate rejection
                        
            # 3. Detect Rejection (Pin bar or Engulfing)
            elif not state.rejection_detected:
                if prev_candle is not None:
                    # A basic rejection is an engulfing candle or a strong close back inside range
                    if self._is_rejection(candle, prev_candle, state.sweep_direction):
                        state.rejection_detected = True
                        state.fvg_countdown = config.wait_fvg_max_m1 # Reuse param
                    else:
                        # If no immediate rejection, invalidate the sweep
                        state.sweep_detected = False
                        state.sweep_direction = None

            # 4. FVG Hunting
            elif not state.fvg:
                if state.fvg_countdown <= 0:
                    # Timeout, reset state
                    state.sweep_detected = False
                    state.rejection_detected = False
                    continue
                
                state.fvg_countdown -= 1
                
                if idx >= 2:
                    fvg = self._compute_fvg(
                        m1_candles[idx - 2],
                        m1_candles[idx - 1],
                        candle,
                        state.sweep_direction,
                        atr_m1,
                        config
                    )
                    if fvg:
                        state.fvg = fvg
                        # Immediately generate signal upon FVG formation (limit order placed)
                        signal = self._build_signal(
                            candle, fvg, m1_candles[:idx+1], atr_m1, account_size, config
                        )
                        if signal:
                            return [signal]

            prev_candle = candle

        return []

    def _tapped_hvn(self, candle: CandleRow, vp: VolumeProfileResult) -> bool:
        """Check if candle wicks into any HVN edge, POC, VAH, or VAL."""
        c_high = candle["high"]
        c_low = candle["low"]
        
        # Tap POC?
        if c_low <= vp.poc <= c_high: return True
        # Tap VAH/VAL?
        if c_low <= vp.vah <= c_high: return True
        if c_low <= vp.val <= c_high: return True
        
        # Tap HVN edges?
        for low_edge, high_edge in vp.hvn_edges:
            if c_low <= low_edge <= c_high: return True
            if c_low <= high_edge <= c_high: return True
            
        return False

    def _is_rejection(self, curr: CandleRow, prev: CandleRow, direction: str) -> bool:
        """Detect a strong rejection candle (engulfing or pin bar)."""
        body = abs(curr["close"] - curr["open"])
        total = curr["high"] - curr["low"]
        if total == 0: return False
        
        if direction == "bearish": # Swept highs, looking to short
            # Bearish engulfing OR strong upper wick (pin bar)
            engulfing = is_bearish(curr) and curr["close"] < prev["low"]
            pin_bar = is_bearish(curr) and (curr["high"] - max(curr["open"], curr["close"])) > body * 1.5
            return engulfing or pin_bar
        else: # Swept lows, looking to long
            # Bullish engulfing OR strong lower wick
            engulfing = is_bullish(curr) and curr["close"] > prev["high"]
            pin_bar = is_bullish(curr) and (min(curr["open"], curr["close"]) - curr["low"]) > body * 1.5
            return engulfing or pin_bar

    def _compute_fvg(self, prev2: CandleRow, prev1: CandleRow, curr: CandleRow, direction: str, atr: float, config: StrategyConfig) -> Optional[FVG]:
        """Detect Fair Value Gap."""
        if direction == "bullish":
            if curr["low"] > prev2["high"]:
                size = curr["low"] - prev2["high"]
                if atr == 0 or size >= config.min_fvg_size_atr * atr:
                    return FVG(curr["low"], prev2["high"], (curr["low"] + prev2["high"])/2, "bullish", size)
        elif direction == "bearish":
            if curr["high"] < prev2["low"]:
                size = prev2["low"] - curr["high"]
                if atr == 0 or size >= config.min_fvg_size_atr * atr:
                    return FVG(prev2["low"], curr["high"], (curr["low"] + prev2["high"])/2, "bearish", size)
        return None

    def _build_signal(self, candle: CandleRow, fvg: FVG, m1_candles: List[CandleRow], atr: float, account_size: float, config: StrategyConfig) -> Optional[TradeSignal]:
        direction = fvg.direction
        buffer = config.buffer_sl_factor * atr
        
        if direction == "bearish":
            entry = fvg.top
            swing_high = max(c["high"] for c in m1_candles[-config.swing_lookback:])
            stop = max(fvg.top, swing_high) + buffer
            tp = entry - config.rr_target * abs(entry - stop)
            side = "SHORT"
        else:
            entry = fvg.bottom
            swing_low = min(c["low"] for c in m1_candles[-config.swing_lookback:])
            stop = min(fvg.bottom, swing_low) - buffer
            tp = entry + config.rr_target * abs(entry - stop)
            side = "LONG"
            
        risk_pips = abs(entry - stop)
        if risk_pips == 0: return None
        
        pos_size = FixedFractionPositionSizer().calculate(
            account_size,
            config.risk_per_trade,
            risk_pips,
            1.0,
        )

        return TradeSignal(
            signal_id=f"ICT_VP:{candle['timestamp']}:{side}:{entry:.8f}",
            timestamp=candle["timestamp"],
            direction=side,
            orh=0.0, orl=0.0, # Not strictly ORB
            fvg_top=fvg.top, fvg_bottom=fvg.bottom,
            entry=entry, stop=stop, tp=tp,
            risk_pips=risk_pips, position_size=pos_size,
            confidence="standard", atr_m1=atr
        )
