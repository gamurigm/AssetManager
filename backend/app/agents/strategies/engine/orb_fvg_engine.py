"""
ORB FVG Engulfing Engine (orb_fvg_engine.py)
=============================================
Implements IStrategyEngine.  All signal-detection logic lives here as
pure functions grouped inside the class — no I/O, no HTTP, no persistence.

Implements the full algorithm from Sections 2–7 of the strategy document:
  PASO 1: ORB  →  PASO 2: Breakout  →  PASO 3: FVG  →
  PASO 4: Retest  →  PASO 5: Engulfing  →  PASO 6: Entry params

SOLID:
  - S: Only produces TradeSignal from raw candles. Nothing else.
  - O: Extend by subclassing (override _is_premium_signal for add-ons).
  - D: Referenced as IStrategyEngine everywhere else; concrete type stays here.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import List, Optional, Tuple

from .models import StrategyConfig, ORBLevel, FVG, TradeSignal, SessionState
from .indicators import compute_ATR, compute_avg_volume, body_ratio, is_bullish, is_bearish

# Local alias — engine layer stays independent of infrastructure
from typing import Dict, Any
CandleRow = Dict[str, Any]


class ORBFVGEngine:
    """
    Strategy Pattern — concrete implementation of IStrategyEngine.

    Usage:
        engine = ORBFVGEngine()
        signal = engine.run_session(m5_candles, m1_candles, account_size, config)
    """

    # ================================================================== #
    #  IStrategyEngine interface                                          #
    # ================================================================== #

    def run_session(
        self,
        m5_candles: List[CandleRow],
        m1_candles: List[CandleRow],
        account_size: float,
        config: StrategyConfig,
    ) -> Optional[TradeSignal]:
        """
        Evaluate one trading session (9:30–11:00 NY).

        Args:
            m5_candles: M5 candles.  Index 0 = the 9:30 opening candle (ORB).
            m1_candles: M1 candles starting at 9:35, in chronological order.
            account_size: Current equity for position sizing.
            config: Strategy parameters.

        Returns:
            TradeSignal if a valid setup completes, None otherwise.
        """
        if not m5_candles or not m1_candles:
            return None

        # PASO 1: Register ORB
        orb = self._detect_orb(m5_candles[0], config.min_range_pips)
        if not orb.valid:
            return None

        state = SessionState()
        state.orb = orb

        atr_m1 = compute_ATR(m1_candles[-20:], period=14)
        avg_vol_m1 = compute_avg_volume(m1_candles[-20:], period=20)

        prev_candle: Optional[CandleRow] = None

        for idx, candle in enumerate(m1_candles):
            # ---------------------------------------------------------- #
            # PASO 2: Detect breakout (only when no FVG yet)              #
            # ---------------------------------------------------------- #
            if not state.fvg:
                if prev_candle is not None:
                    bk = self._detect_breakout(
                        candle, prev_candle, orb.high, orb.low, avg_vol_m1, config
                    )
                    if bk["valid"] and not state.breakout_detected:
                        state.breakout_detected = True
                        state.breakout_direction = bk["direction"]

                        # PASO 3: Compute FVG from the 3 most recent M1 candles
                        if idx >= 2:
                            fvg = self._compute_fvg(
                                m1_candles[idx - 2],
                                m1_candles[idx - 1],
                                candle,
                                bk["direction"],
                                atr_m1,
                                config,
                            )
                            if fvg:
                                state.fvg = fvg
                                state.retest_countdown = config.wait_retest_max_m1

            # ---------------------------------------------------------- #
            # PASO 4: Wait for retest of FVG                             #
            # ---------------------------------------------------------- #
            elif not state.setup_active:
                if state.retest_countdown <= 0:
                    return None  # Setup expired — best attempt for this session

                state.retest_countdown -= 1

                # Invalidation checks
                if self._setup_invalidated(candle, state.fvg, orb, config):
                    return None

                # Check if price has returned to FVG
                if self._price_in_fvg(candle, state.fvg):
                    # PASO 5: Engulfing confirmation
                    if prev_candle is not None and self._is_engulfing(
                        candle, prev_candle, state.fvg.direction, atr_m1, avg_vol_m1, config
                    ):
                        # PASO 6: Calculate trade parameters
                        signal = self._build_signal(
                            confirm_candle=candle,
                            fvg=state.fvg,
                            orb=orb,
                            m1_candles=m1_candles[: idx + 1],
                            atr_m1=atr_m1,
                            account_size=account_size,
                            config=config,
                            premium=self._is_premium_signal(candle, prev_candle),
                        )
                        if signal:
                            state.setup_active = True
                            return signal

            prev_candle = candle

        return None  # No valid signal found this session

    # ================================================================== #
    #  PASO 1 — ORB Detection                                             #
    # ================================================================== #

    @staticmethod
    def _detect_orb(m5_candle: CandleRow, min_range: float) -> ORBLevel:
        """Extract ORH/ORL from the 9:30 M5 candle."""
        high = m5_candle["high"]
        low  = m5_candle["low"]
        rng  = high - low
        return ORBLevel(high=high, low=low, range_=rng, valid=(rng >= min_range))

    # ================================================================== #
    #  PASO 2 — Breakout Detection                                        #
    # ================================================================== #

    @staticmethod
    def _detect_breakout(
        candle: CandleRow,
        prev_candle: CandleRow,
        orh: float,
        orl: float,
        avg_vol: float,
        config: StrategyConfig,
    ) -> dict:
        """
        Validate a M1 candle as a valid ORB breakout.
        Returns dict with 'valid' (bool) and 'direction' ('bullish'|'bearish'|None).
        """
        br   = body_ratio(candle)
        vol  = candle["volume"]
        close = candle["close"]

        # Noise zone: clamp to ±1 pip equivalent (we use 0 tolerance, strategy doc says 1 pip)
        bullish_break = close > orh and br >= config.body_ratio_breakout and vol >= avg_vol * config.vol_ruptura_ratio
        bearish_break = close < orl and br >= config.body_ratio_breakout and vol >= avg_vol * config.vol_ruptura_ratio

        if bullish_break:
            return {"valid": True, "direction": "bullish"}
        if bearish_break:
            return {"valid": True, "direction": "bearish"}
        return {"valid": False, "direction": None}

    # ================================================================== #
    #  PASO 3 — FVG Detection                                             #
    # ================================================================== #

    @staticmethod
    def _compute_fvg(
        c_prev2: CandleRow,
        c_prev1: CandleRow,
        c_curr: CandleRow,
        direction: str,
        atr_m1: float,
        config: StrategyConfig,
    ) -> Optional[FVG]:
        """
        Detect an FVG (Fair Value Gap) in the three most recent M1 candles.
        Formula from Section 2.3 of strategy doc.

        For BULLISH setup (price broke above ORH and will retrace down to FVG):
            FVG exists when Low(curr) > High(prev2)
            FVG_bottom = High(prev2),  FVG_top = Low(curr)

        For BEARISH setup (price broke below ORL and will retrace up to FVG):
            FVG exists when High(curr) < Low(prev2)
            FVG_bottom = High(curr),   FVG_top = Low(prev2)
        """
        if direction == "bullish":
            if c_curr["low"] > c_prev2["high"]:
                bottom = c_prev2["high"]
                top    = c_curr["low"]
                size   = top - bottom
                if atr_m1 == 0 or size >= config.min_fvg_size_atr * atr_m1:
                    mid = (top + bottom) / 2
                    return FVG(top=top, bottom=bottom, midpoint=mid,
                               direction="bullish", size=size)

        elif direction == "bearish":
            if c_curr["high"] < c_prev2["low"]:
                top    = c_prev2["low"]
                bottom = c_curr["high"]
                size   = top - bottom
                if atr_m1 == 0 or size >= config.min_fvg_size_atr * atr_m1:
                    mid = (top + bottom) / 2
                    return FVG(top=top, bottom=bottom, midpoint=mid,
                               direction="bearish", size=size)

        return None

    # ================================================================== #
    #  PASO 4 — Retest / Invalidation                                     #
    # ================================================================== #

    @staticmethod
    def _price_in_fvg(candle: CandleRow, fvg: FVG) -> bool:
        """True when any part of the candle overlaps the FVG zone."""
        return candle["low"] <= fvg.top and candle["high"] >= fvg.bottom

    @staticmethod
    def _setup_invalidated(candle: CandleRow, fvg: FVG, orb: ORBLevel, config: StrategyConfig) -> bool:
        """
        Invalidation conditions from Section 3 / PASO 4 of strategy doc.
        Returns True when the setup should be cancelled.
        """
        if fvg.direction == "bearish":
            # Price closes below FVG_bottom in a short setup → weakness signal
            if candle["close"] < fvg.bottom:
                pass # let's turn off for testing
            # New swing high above ORH before retest
            if candle["high"] > orb.high:
                return True
        else:  # bullish
            if candle["close"] > fvg.top:
                 pass
            if candle["low"] < orb.low:
                return True
        return False

    # ================================================================== #
    #  PASO 5 — Engulfing Confirmation                                    #
    # ================================================================== #

    @staticmethod
    def _is_engulfing(
        curr: CandleRow,
        prev: CandleRow,
        direction: str,
        atr_m1: float,
        avg_vol: float,
        config: StrategyConfig,
    ) -> bool:
        """
        Bearish engulfing (for SHORT setup) / Bullish engulfing (for LONG setup).
        Conditions from Section 2.6 of strategy doc.
        """
        body_size = abs(curr["close"] - curr["open"])

        # Minimum body size
        if atr_m1 > 0 and body_size < config.p_cuerpo_min * atr_m1:
            return False

        # Volume confirmation
        if curr["volume"] < config.p_vol_min * avg_vol:
            return False

        if direction == "bearish":
            # Bearish candle that opens ≥ prev close, closes ≤ prev open
            return (
                is_bearish(curr)
                and curr["open"] >= prev["close"]
                and curr["close"] <= prev["open"]
            )
        else:  # bullish
            return (
                is_bullish(curr)
                and curr["open"] <= prev["close"]
                and curr["close"] >= prev["open"]
            )

    # ================================================================== #
    #  PASO 6 — Build Trade Signal                                        #
    # ================================================================== #

    def _build_signal(
        self,
        confirm_candle: CandleRow,
        fvg: FVG,
        orb: ORBLevel,
        m1_candles: List[CandleRow],
        atr_m1: float,
        account_size: float,
        config: StrategyConfig,
        premium: bool,
    ) -> Optional[TradeSignal]:
        """
        Compute entry, stop-loss, take-profit, and position size.
        Returns None if position size is zero or spread exceeds limit.
        """
        direction = fvg.direction
        buffer = config.buffer_sl_factor * atr_m1

        # Entry price
        if direction == "bearish":
            entry = fvg.top             # Limit at top of FVG for short
            swing_high = self._swing_high(m1_candles, config.swing_lookback)
            stop  = max(fvg.top, swing_high) + buffer
            tp    = entry - config.rr_target * abs(entry - stop)
            side  = "SHORT"
        else:
            entry = fvg.bottom          # Limit at bottom of FVG for long
            swing_low = self._swing_low(m1_candles, config.swing_lookback)
            stop  = min(fvg.bottom, swing_low) - buffer
            tp    = entry + config.rr_target * abs(entry - stop)
            side  = "LONG"

        risk_pips = abs(entry - stop)
        if risk_pips == 0:
            return None

        position_size = self._calc_position_size(
            account_size, config.risk_per_trade, risk_pips
        )

        return TradeSignal(
            signal_id=f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}_ORB_{side}_{uuid.uuid4().hex[:4].upper()}",
            timestamp=confirm_candle["timestamp"],
            direction=side,
            orh=orb.high,
            orl=orb.low,
            fvg_top=fvg.top,
            fvg_bottom=fvg.bottom,
            entry=entry,
            stop=stop,
            tp=tp,
            risk_pips=risk_pips,
            position_size=position_size,
            confidence="premium" if premium else "standard",
            atr_m1=atr_m1,
        )

    # ================================================================== #
    #  Helpers (pure, static)                                             #
    # ================================================================== #

    @staticmethod
    def _calc_position_size(account: float, risk_pct: float, risk_pips: float, pip_value: float = 1.0) -> float:
        """
        position_size = (account × risk_pct) / (risk_pips × pip_value)
        Section 4.1 of strategy doc.
        """
        if risk_pips <= 0 or pip_value <= 0:
            return 0.0
        risk_amount = account * risk_pct
        return risk_amount / (risk_pips * pip_value)

    @staticmethod
    def _swing_high(candles: List[CandleRow], lookback: int) -> float:
        """Highest high of the last `lookback` M1 candles."""
        recent = candles[-lookback:] if len(candles) >= lookback else candles
        return max(c["high"] for c in recent) if recent else 0.0

    @staticmethod
    def _swing_low(candles: List[CandleRow], lookback: int) -> float:
        """Lowest low of the last `lookback` M1 candles."""
        recent = candles[-lookback:] if len(candles) >= lookback else candles
        return min(c["low"] for c in recent) if recent else 0.0

    @staticmethod
    def _is_premium_signal(curr: CandleRow, prev: CandleRow) -> bool:
        """
        Premium signal: pin bar rejection + engulfing in same zone.
        Section 3 / PASO 5 — 'variante premium'.
        Heuristic: upper wick > 2× body for bearish, lower wick > 2× body for bullish.
        """
        body = abs(curr["close"] - curr["open"])
        total = curr["high"] - curr["low"]
        if total == 0:
            return False
        wick_ratio = (total - body) / total
        return wick_ratio >= 0.60  # 60% wick = strong rejection
