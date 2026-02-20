"""
Strategy Engine — Value Objects (models.py)
============================================
All dataclasses are FROZEN (immutable) — they are pure Value Objects with no identity.
This ensures:
  - Thread safety in the async backtest runner.
  - Transparent testability: two signals with same fields == equal.
  - No accidental mutation across pipeline stages.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, List


# --------------------------------------------------------------------------- #
#  Strategy Configuration                                                      #
# --------------------------------------------------------------------------- #

@dataclass(frozen=True)
class StrategyConfig:
    """
    All tunable parameters from the ORB FVG Engulfing spec (Section 5 & 10).
    Frozen so a single config object can be safely shared across sessions.
    """
    # ORB
    min_range_pips: float = 0.1            # Minimum ORB range to trade that day

    # Breakout validation
    vol_ruptura_ratio: float = 0.50         # Volume multiplier on breakout candle
    body_ratio_breakout: float = 0.10       # Min body/range ratio on breakout candle

    # FVG
    min_fvg_size_atr: float = 0.10         # FVG size ≥ factor × ATR_M1

    # FCR candle (M5 impulse filter — optional)
    k1_atr_fcr: float = 1.5               # Range ≥ k1 × ATR_M5
    k2_body_ratio: float = 0.60           # Body ratio ≥ k2
    k3_vol_ratio_fcr: float = 1.50        # Volume ≥ k3 × avg_vol_M5

    # Engulfing (confirmation in M1)
    p_cuerpo_min: float = 0.10            # Body ≥ p_cuerpo_min × ATR_M1
    p_vol_min: float = 0.50               # Volume ≥ p_vol_min × avg_vol_M1

    # Retest patience
    wait_retest_max_m1: int = 30          # Max M1 candles to wait for price to return to FVG

    # Execution
    rr_target: float = 3.0               # Risk/Reward ratio (fixed)
    buffer_sl_factor: float = 0.10       # SL buffer = factor × ATR_M1
    max_spread: float = 0.0005           # Max allowed spread at entry
    swing_lookback: int = 5              # M1 candles to look back for swing extreme

    # Risk
    risk_per_trade: float = 0.005        # Fraction of account to risk (0.5%)
    max_trades_per_day: int = 2
    max_concurrent_trades: int = 1

    # Circuit breakers
    max_daily_losses: int = 2
    max_daily_drawdown_pct: float = 0.02
    max_monthly_drawdown_pct: float = 0.10

    # TP scaling (optional)
    tp_scaling_enabled: bool = False
    tp1_rr: float = 2.0
    tp1_size_pct: float = 50.0
    tp2_rr: float = 3.0
    tp2_size_pct: float = 50.0

    @classmethod
    def default(cls) -> "StrategyConfig":
        return cls()

    @classmethod
    def from_dict(cls, d: dict) -> "StrategyConfig":
        """Factory from dict — allows API to override individual params."""
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


# --------------------------------------------------------------------------- #
#  Domain Entities (pure data, no behaviour)                                  #
# --------------------------------------------------------------------------- #

@dataclass(frozen=True)
class ORBLevel:
    """Opening Range Breakout levels — calculated from the 9:30 M5 candle."""
    high: float
    low: float
    range_: float
    valid: bool          # False when range < min_range_pips


@dataclass(frozen=True)
class FVG:
    """
    Fair Value Gap — price imbalance (inefficiency) detected after a breakout.
    Direction refers to the TRADE direction, not the gap body direction.
    """
    top: float
    bottom: float
    midpoint: float
    direction: str       # 'bullish' (long setup) | 'bearish' (short setup)
    size: float          # top - bottom


@dataclass(frozen=True)
class TradeSignal:
    """
    Trade signal produced by the strategy engine.
    Fully self-contained — carries everything needed to execute or log.
    """
    signal_id: str
    timestamp: str           # ISO-8601 of the confirmation candle close
    direction: str           # 'LONG' | 'SHORT'
    orh: float
    orl: float
    fvg_top: float
    fvg_bottom: float
    entry: float
    stop: float
    tp: float
    risk_pips: float
    position_size: float     # Calculated lots/units
    confidence: str          # 'standard' | 'premium' (premium = pinbar + engulfing)
    atr_m1: float            # ATR at time of signal (for context)


@dataclass(frozen=True)
class TradeRecord:
    """
    Result of simulating a TradeSignal against subsequent M1 candles.
    Produced by BacktestRunner._simulate_trade().
    """
    signal: TradeSignal
    outcome: str             # 'win_tp' | 'loss_sl' | 'expired' | 'circuit_break'
    exit_price: float
    exit_timestamp: str
    pnl_r: float             # +3.0 for TP hit, -1.0 for SL hit, 0 for expired
    pnl_usd: float
    slippage_pips: float

    @property
    def is_win(self) -> bool:
        return self.outcome == "win_tp"

    @property
    def is_loss(self) -> bool:
        return self.outcome == "loss_sl"


@dataclass
class SessionState:
    """
    Mutable intra-session state for the strategy engine loop.
    NOT frozen — this is the agent's working memory for one trading session.
    """
    orb: Optional[ORBLevel] = None
    fvg: Optional[FVG] = None
    setup_active: bool = False
    retest_countdown: int = 0
    breakout_detected: bool = False
    breakout_direction: Optional[str] = None
    trades_today: int = 0

    def reset(self) -> None:
        self.orb = None
        self.fvg = None
        self.setup_active = False
        self.retest_countdown = 0
        self.breakout_detected = False
        self.breakout_direction = None
        self.trades_today = 0


@dataclass(frozen=True)
class KPIResult:
    """
    Backtest Key Performance Indicators — all defined in Section 8 of the strategy doc.
    Frozen: produced once at end of backtest, never mutated.
    """
    total_trades: int
    wins: int
    losses: int
    win_rate: float
    expectancy_r: float       # E = (WR × avg_win_R) − (LR × avg_loss_R)
    profit_factor: float      # Σ wins_usd / Σ losses_usd
    max_drawdown_pct: float   # Peak-to-trough on running equity
    sharpe_ratio: float
    avg_rr_realized: float    # Actual RR achieved (not target)
    total_r: float            # Sum of pnl_r across all trades
    final_equity: float
    cagr: float               # Annualised growth rate

    def as_dict(self) -> dict:
        return {
            "total_trades": self.total_trades,
            "wins": self.wins,
            "losses": self.losses,
            "win_rate": round(self.win_rate, 4),
            "expectancy_r": round(self.expectancy_r, 4),
            "profit_factor": round(self.profit_factor, 4),
            "max_drawdown_pct": round(self.max_drawdown_pct, 4),
            "sharpe_ratio": round(self.sharpe_ratio, 4),
            "avg_rr_realized": round(self.avg_rr_realized, 4),
            "total_r": round(self.total_r, 4),
            "final_equity": round(self.final_equity, 2),
            "cagr": round(self.cagr, 4),
        }
