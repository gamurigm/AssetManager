"""
IVRegimeStrategyService
=======================
Daily-timeframe directional strategy that uses:
    1. Rolling historical-vol percentile (IV Rank proxy)
         — since free yfinance does not provide historical IV,
             we use realised-vol percentile as a historical proxy for backtests.
    2. Markov volatility state (Low / Mid / High)
    3. N-day price momentum
    4. Live ATM implied volatility derived from real option prices
         — used to enrich the latest signal with Black-Scholes ATM IV,
             skew, and IV-vs-realised-vol context.

Historical signal rules:
    LONG  : iv_rank <  iv_rank_low  AND momentum > 0 AND regime in {0,1}
    SHORT : iv_rank >  iv_rank_high AND momentum < 0 AND regime == 2
    EXIT  : hold_days elapsed OR stop-loss hit

Position sizing:
    shares = (equity * risk_pct) / (sl_vol_mult * daily_vol * entry_price)
    SL     = entry ± sl_dist
    TP     = entry ± rr_target * sl_dist
"""

from __future__ import annotations

import math
import uuid
from dataclasses import dataclass, fields as _dc_fields
from typing import Any, Dict, List, Optional

import numpy as np

_ANNUALIZE = math.sqrt(252)


# ── Parameters ────────────────────────────────────────────────────────────────

@dataclass
class IVRegimeParams:
    iv_rank_low:       float = 30.0   # IV rank below this  → trend-follow mode (LONG)
    iv_rank_high:      float = 70.0   # IV rank above this  → mean-revert mode  (SHORT)
    momentum_window:   int   = 5      # days for N-day price  momentum
    iv_rank_window:    int   = 252    # lookback for IV rank percentile
    vol_window:        int   = 20     # rolling vol estimation window
    hold_days:         int   = 5      # max days to hold a position
    sl_vol_mult:       float = 2.0    # SL = sl_vol_mult × daily_vol × entry_price
    rr_target:         float = 2.0    # TP = rr_target × sl_dist
    risk_pct:          float = 0.01   # fraction of equity to risk per trade (1%)
    use_markov_filter: bool  = True   # require matching Markov state
    allow_short:       bool  = True   # allow short positions

    @classmethod
    def from_dict(cls, d: dict) -> "IVRegimeParams":
        known = {f.name for f in _dc_fields(cls)}
        return cls(**{k: v for k, v in d.items() if k in known and v is not None})

    def as_dict(self) -> dict:
        return {f.name: getattr(self, f.name) for f in _dc_fields(self)}


# ── Feature engineering ───────────────────────────────────────────────────────

def _rolling_vol(log_rets: np.ndarray, window: int) -> np.ndarray:
    """Annualised rolling std of log-returns; first (window-1) entries are NaN."""
    n = len(log_rets)
    out = np.full(n, np.nan)
    for i in range(window - 1, n):
        out[i] = float(np.std(log_rets[i - window + 1: i + 1], ddof=1)) * _ANNUALIZE
    return out


def _iv_rank_series(vol_series: np.ndarray, window: int) -> np.ndarray:
    """
    Percentile rank (0-100) of the current rolling vol within the last
    `window` observations. Higher = historically high vol = high IV rank.
    """
    n = len(vol_series)
    out = np.full(n, np.nan)
    for i in range(window - 1, n):
        hist = vol_series[i - window + 1: i + 1]
        valid = hist[~np.isnan(hist)]
        if len(valid) < 10:
            continue
        out[i] = float(np.sum(valid <= valid[-1]) / len(valid) * 100)
    return out


def _markov_state_series(vol_series: np.ndarray, window: int) -> np.ndarray:
    """
    Assign Markov state per day relative to rolling history.
    State 0 = Low (<=33rd pct), 1 = Mid (33-66th), 2 = High (>66th).
    Returns -1 for insufficient data.
    """
    n = len(vol_series)
    out = np.full(n, -1, dtype=int)
    for i in range(window - 1, n):
        hist = vol_series[i - window + 1: i + 1]
        valid = hist[~np.isnan(hist)]
        if len(valid) < 10:
            continue
        p33 = float(np.percentile(valid, 33))
        p66 = float(np.percentile(valid, 66))
        cur = vol_series[i]
        if np.isnan(cur):
            continue
        if cur <= p33:
            out[i] = 0
        elif cur <= p66:
            out[i] = 1
        else:
            out[i] = 2
    return out


# ── Service class ─────────────────────────────────────────────────────────────

class IVRegimeStrategyService:
    """Standalone daily backtest runner for the IV Regime strategy."""

    def __init__(self) -> None:
        self._mds  = None
        self._repo = None
        self._ivs  = None

    def _get_deps(self) -> None:
        if self._mds is None:
            from .market_data import market_data_service
            from .duckdb_store import duckdb_store as duckdb_repo
            from .implied_vol_service import implied_vol_service
            self._mds  = market_data_service
            self._repo = duckdb_repo
            self._ivs  = implied_vol_service

    async def run_backtest(
        self,
        symbol:       str,
        start_date:   str,
        end_date:     str,
        account_size: float = 10_000.0,
        params:       Optional[IVRegimeParams] = None,
    ) -> Dict[str, Any]:
        """
        Run a full daily backtest for the IV Regime strategy.

        Returns a dict with:
          symbol, strategy, start_date, end_date, account_size,
          n_trading_days, params, kpis, trades, signals, current_signal
        """
        self._get_deps()
        if params is None:
            params = IVRegimeParams()

        warmup = params.iv_rank_window + params.vol_window + params.momentum_window + 20
        df = await self._fetch_daily(symbol, limit=warmup + 600)
        if df is None or len(df) < params.vol_window + params.momentum_window + 30:
            return {"error": f"Insufficient daily data for {symbol}"}

        import pandas as pd

        df = df.sort_values("date").reset_index(drop=True)
        df["date_str"] = df["date"].dt.strftime("%Y-%m-%d")

        closes   = df["close"].values.astype(float)
        log_rets = np.concatenate([[np.nan], np.diff(np.log(np.maximum(closes, 1e-10)))])

        # ── Features ─────────────────────────────────────────────────────
        vol_s    = _rolling_vol(log_rets, params.vol_window)
        ivr_s    = _iv_rank_series(vol_s, params.iv_rank_window)
        state_s  = _markov_state_series(vol_s, params.iv_rank_window)

        mw = params.momentum_window
        mom_s = np.full(len(closes), np.nan)
        for i in range(mw, len(closes)):
            base = closes[i - mw]
            if base > 0:
                mom_s[i] = (closes[i] / base - 1) * 100

        # ── Locate backtest window ────────────────────────────────────────
        date_arr   = df["date_str"].values
        start_mask = date_arr >= start_date
        end_mask   = date_arr <= end_date

        if not start_mask.any() or not end_mask.any():
            return {"error": "No data in specified date range"}

        bt_start   = int(np.where(start_mask)[0][0])
        bt_end     = int(np.where(end_mask)[0][-1])

        # ── Simulation loop ───────────────────────────────────────────────
        equity     = account_size
        trades: List[Dict[str, Any]]  = []
        equity_seq: List[float]       = [equity]   # one per backtested day
        in_position = False
        position: Optional[Dict[str, Any]] = None

        for idx in range(bt_start, bt_end + 1):
            cur_date  = date_arr[idx]
            cur_close = float(closes[idx])
            cur_ivr   = float(ivr_s[idx])   if not np.isnan(ivr_s[idx])   else None
            cur_mom   = float(mom_s[idx])   if not np.isnan(mom_s[idx])   else None
            cur_state = int(state_s[idx])   if state_s[idx] >= 0          else None

            # ── Exit check ──────────────────────────────────────────────
            if in_position and position is not None:
                d = position["direction"]
                hit_stop = (d == "LONG"  and cur_close <= position["stop"]) or \
                           (d == "SHORT" and cur_close >= position["stop"])
                hit_tp   = (d == "LONG"  and cur_close >= position["tp"]) or \
                           (d == "SHORT" and cur_close <= position["tp"])
                days_held = idx - position["entry_idx"]
                force_exit = days_held >= params.hold_days

                if hit_tp or hit_stop or force_exit:
                    ep = position["entry_px"]
                    xp = cur_close
                    sl_dist  = abs(ep - position["stop"])
                    sign     = 1.0 if d == "LONG" else -1.0
                    pnl_usd  = (xp - ep) * sign * position["shares"]
                    pnl_r    = pnl_usd / (sl_dist * position["shares"]) if sl_dist > 0 and position["shares"] > 0 else 0.0

                    if hit_tp:
                        outcome = "win"
                    elif hit_stop:
                        outcome = "loss"
                    else:
                        outcome = "win" if pnl_usd > 0 else "loss"

                    equity = max(equity + pnl_usd, 0.01)
                    trades.append({
                        "signal_id":       position["signal_id"],
                        "timestamp":       position["entry_date"],
                        "direction":       d,
                        "entry":           round(ep, 4),
                        "stop":            round(position["stop"], 4),
                        "tp":              round(position["tp"], 4),
                        "exit_price":      round(xp, 4),
                        "exit_timestamp":  cur_date,
                        "outcome":         outcome,
                        "pnl_r":           round(pnl_r, 4),
                        "pnl_usd":         round(pnl_usd, 4),
                        "iv_rank_entry":   round(position["iv_rank"], 2),
                        "momentum_entry": round(position["momentum"], 4),
                        "regime_entry":    position["regime"],
                        "days_held":       days_held,
                    })
                    in_position = False
                    position    = None

            # ── Entry check ─────────────────────────────────────────────
            if not in_position and cur_ivr is not None and cur_mom is not None and cur_state is not None:
                daily_vol = float(vol_s[idx]) / _ANNUALIZE if not np.isnan(vol_s[idx]) else 0.015
                sl_dist   = max(params.sl_vol_mult * daily_vol * cur_close, 0.001 * cur_close)
                risk_usd  = equity * params.risk_pct
                shares    = risk_usd / sl_dist if sl_dist > 0 else 0.0

                long_ok  = (cur_ivr < params.iv_rank_low
                            and cur_mom > 0
                            and (not params.use_markov_filter or cur_state in (0, 1)))
                short_ok = (cur_ivr > params.iv_rank_high
                            and cur_mom < 0
                            and params.allow_short
                            and (not params.use_markov_filter or cur_state == 2))

                direction: Optional[str] = None
                if long_ok:
                    direction = "LONG"
                    stop = cur_close - sl_dist
                    tp   = cur_close + sl_dist * params.rr_target
                elif short_ok:
                    direction = "SHORT"
                    stop = cur_close + sl_dist
                    tp   = cur_close - sl_dist * params.rr_target

                if direction and shares > 0:
                    in_position = True
                    position    = {
                        "signal_id":  str(uuid.uuid4())[:8],
                        "entry_date": cur_date,
                        "entry_idx":  idx,
                        "direction":  direction,
                        "entry_px":   cur_close,
                        "stop":       stop,
                        "tp":         tp,
                        "shares":     shares,
                        "iv_rank":    cur_ivr,
                        "momentum":   cur_mom,
                        "regime":     cur_state,
                    }

            equity_seq.append(equity)

        # Force-close open position at period end
        if in_position and position is not None:
            ep       = position["entry_px"]
            xp       = float(closes[bt_end])
            sl_dist  = abs(ep - position["stop"])
            sign     = 1.0 if position["direction"] == "LONG" else -1.0
            pnl_usd  = (xp - ep) * sign * position["shares"]
            pnl_r    = pnl_usd / (sl_dist * position["shares"]) if sl_dist > 0 and position["shares"] > 0 else 0.0
            equity   = max(equity + pnl_usd, 0.01)
            trades.append({
                "signal_id":      position["signal_id"],
                "timestamp":      position["entry_date"],
                "direction":      position["direction"],
                "entry":          round(ep, 4),
                "stop":           round(position["stop"], 4),
                "tp":             round(position["tp"], 4),
                "exit_price":     round(xp, 4),
                "exit_timestamp": date_arr[bt_end],
                "outcome":        "win" if pnl_usd > 0 else "loss",
                "pnl_r":          round(pnl_r, 4),
                "pnl_usd":        round(pnl_usd, 4),
                "iv_rank_entry":  round(position["iv_rank"], 2),
                "momentum_entry": round(position["momentum"], 4),
                "regime_entry":   position["regime"],
                "days_held":      bt_end - position["entry_idx"],
            })
            equity_seq.append(equity)

        n_days  = bt_end - bt_start + 1
        kpis    = _compute_kpis(trades, account_size, equity, n_days, equity_seq)
        current = _current_signal(ivr_s, state_s, mom_s, closes, vol_s, date_arr, params, bt_end)
        current = await self._attach_live_option_context(symbol, current, params)

        return {
            "symbol":          symbol.upper(),
            "strategy":        "IV_REGIME",
            "start_date":      start_date,
            "end_date":        end_date,
            "account_size":    account_size,
            "n_trading_days":  n_days,
            "params":          params.as_dict(),
            "kpis":            kpis,
            "trades":          trades,
            "current_signal":  current,
        }

    async def _attach_live_option_context(
        self,
        symbol: str,
        current_signal: Optional[Dict[str, Any]],
        params: IVRegimeParams,
    ) -> Optional[Dict[str, Any]]:
        if current_signal is None or self._ivs is None:
            return current_signal

        try:
            snapshot = await self._ivs.get_atm_iv_snapshot(symbol)
        except Exception as exc:
            current_signal["signal_source"] = "PROXY_IVR"
            current_signal["option_context"] = {
                "available": False,
                "error": str(exc),
            }
            return current_signal

        if not snapshot or "error" in snapshot:
            current_signal["signal_source"] = "PROXY_IVR"
            current_signal["option_context"] = {
                "available": False,
                "error": (snapshot or {}).get("error", "Live option IV unavailable"),
            }
            return current_signal

        current_signal["signal_source"] = "HYBRID_PROXY_PLUS_LIVE_IV"
        current_signal["option_context"] = _build_live_option_context(current_signal, snapshot, params)
        return current_signal

    async def _fetch_daily(self, symbol: str, limit: int = 800):
        import pandas as pd

        try:
            conn = self._repo._get_conn()
            try:
                df = conn.execute(
                    "SELECT date, close FROM ohlcv WHERE symbol = ? ORDER BY date ASC",
                    [symbol.upper()],
                ).df()
            finally:
                conn.close()
            if len(df) >= limit // 2:
                df["date"]  = pd.to_datetime(df["date"])
                df["close"] = pd.to_numeric(df["close"], errors="coerce")
                return df.dropna(subset=["close"]).tail(limit).reset_index(drop=True)
        except Exception:
            pass

        try:
            data = await self._mds.get_historical(symbol, limit=limit)
            hist = data.get("historical", []) if data else []
            if not hist:
                return None
            records = [(h.__dict__ if hasattr(h, "__dict__") else h) for h in hist]
            df = pd.DataFrame(records)
            df["date"]  = pd.to_datetime(df["date"])
            df["close"] = pd.to_numeric(df["close"], errors="coerce")
            return df.dropna(subset=["close"]).sort_values("date").reset_index(drop=True)
        except Exception:
            return None


# ── KPI computation ───────────────────────────────────────────────────────────

def _compute_kpis(trades: list, initial_equity: float, final_equity: float,
                  n_days: int, equity_seq: list) -> dict:
    empty = {
        "total_trades": 0, "wins": 0, "losses": 0, "win_rate": 0.0,
        "expectancy_r": 0.0, "profit_factor": 0.0, "max_drawdown_pct": 0.0,
        "sharpe_ratio": 0.0, "avg_rr_realized": 0.0, "total_r": 0.0,
        "final_equity": round(final_equity, 2), "cagr": 0.0,
    }
    if not trades:
        return empty

    wins   = [t for t in trades if t["pnl_usd"] > 0]
    losses = [t for t in trades if t["pnl_usd"] <= 0]
    gross_p = sum(t["pnl_usd"] for t in wins)
    gross_l = abs(sum(t["pnl_usd"] for t in losses))
    pf      = gross_p / gross_l if gross_l > 0 else (float("inf") if gross_p > 0 else 0.0)
    total_r = sum(t["pnl_r"] for t in trades)
    avg_rr  = sum(t["pnl_r"] for t in wins) / len(wins) if wins else 0.0

    # Max drawdown from equity_seq
    peak   = float(equity_seq[0]) if equity_seq else initial_equity
    max_dd = 0.0
    for v in equity_seq:
        vf = float(v)
        if vf > peak:
            peak = vf
        dd = (peak - vf) / peak if peak > 0 else 0.0
        if dd > max_dd:
            max_dd = dd

    # Daily returns for Sharpe (from equity sequence)
    arr = np.array(equity_seq, dtype=float)
    if len(arr) > 2:
        daily_rets = np.diff(arr) / np.maximum(arr[:-1], 1e-8)
        mu  = float(np.mean(daily_rets))
        std = float(np.std(daily_rets, ddof=1))
        sharpe = (mu / std) * _ANNUALIZE if std > 0 else 0.0
    else:
        sharpe = 0.0

    n_years = max(n_days / 252, 1 / 252)
    cagr    = (final_equity / initial_equity) ** (1 / n_years) - 1 if initial_equity > 0 else 0.0

    return {
        "total_trades":    len(trades),
        "wins":            len(wins),
        "losses":          len(losses),
        "win_rate":        round(len(wins) / len(trades), 4),
        "expectancy_r":    round(total_r / len(trades), 4),
        "profit_factor":   round(pf, 4) if math.isfinite(pf) else 9999.0,
        "max_drawdown_pct":round(max_dd, 6),
        "sharpe_ratio":    round(sharpe, 4),
        "avg_rr_realized": round(avg_rr, 4),
        "total_r":         round(total_r, 4),
        "final_equity":    round(final_equity, 2),
        "cagr":            round(cagr, 6),
    }


def _current_signal(ivr_s, state_s, mom_s, closes, vol_s, date_arr, params: IVRegimeParams, bt_end: int) -> Optional[dict]:
    """Extract the current (latest) signal from computed feature arrays."""
    _LABELS = {0: "Low", 1: "Mid", 2: "High"}
    n = len(ivr_s)
    # Use last available bar (could be bt_end or beyond)
    for idx in range(n - 1, -1, -1):
        if np.isnan(ivr_s[idx]) or np.isnan(mom_s[idx]) or state_s[idx] < 0:
            continue
        ivr   = float(ivr_s[idx])
        mom   = float(mom_s[idx])
        state = int(state_s[idx])
        daily_vol = float(vol_s[idx]) / _ANNUALIZE if not np.isnan(vol_s[idx]) else None
        ann_vol = float(vol_s[idx]) if not np.isnan(vol_s[idx]) else None

        long_ok  = ivr < params.iv_rank_low  and mom > 0 and (not params.use_markov_filter or state in (0, 1))
        short_ok = ivr > params.iv_rank_high and mom < 0 and params.allow_short and (not params.use_markov_filter or state == 2)
        direction = "LONG" if long_ok else ("SHORT" if short_ok else "FLAT")

        return {
            "date":           str(date_arr[idx])[:10],
            "close":          round(float(closes[idx]), 4),
            "iv_rank":        round(ivr, 2),
            "regime":         _LABELS.get(state, "Unknown"),
            "momentum_pct":   round(mom, 4),
            "direction":      direction,
            "proxy_direction": direction,
            "signal_source":  "PROXY_IVR",
            "daily_vol_pct":  round(daily_vol * 100, 4) if daily_vol else None,
            "realized_vol_ann_pct": round(ann_vol * 100, 4) if ann_vol is not None else None,
        }
    return None


def _build_live_option_context(
    current_signal: Dict[str, Any],
    snapshot: Dict[str, Any],
    params: IVRegimeParams,
) -> Dict[str, Any]:
    atm_iv = snapshot.get("atm_iv")
    realized_ann = current_signal.get("realized_vol_ann_pct")
    momentum = float(current_signal.get("momentum_pct") or 0.0)
    regime = str(current_signal.get("regime") or "Unknown")

    spread = None
    ratio = None
    if atm_iv is not None and realized_ann is not None and realized_ann > 0:
        spread = float(atm_iv) - float(realized_ann)
        ratio = float(atm_iv) / float(realized_ann)

    long_ok = (
        ratio is not None
        and ratio <= 0.95
        and momentum > 0
        and (not params.use_markov_filter or regime in ("Low", "Mid"))
    )
    short_ok = (
        ratio is not None
        and ratio >= 1.15
        and momentum < 0
        and params.allow_short
        and (not params.use_markov_filter or regime == "High")
    )
    direction_bias = "LONG" if long_ok else ("SHORT" if short_ok else "FLAT")

    return {
        "available": True,
        "signal_mode": "LIVE_OPTION_IV",
        "direction_bias": direction_bias,
        "exp_date": snapshot.get("exp_date"),
        "dte": snapshot.get("dte"),
        "strike": snapshot.get("strike"),
        "moneyness_pct": snapshot.get("moneyness_pct"),
        "atm_iv_pct": snapshot.get("atm_iv"),
        "atm_call_iv_pct": snapshot.get("atm_call_iv"),
        "atm_put_iv_pct": snapshot.get("atm_put_iv"),
        "skew_pct": snapshot.get("skew_pct"),
        "call_price": snapshot.get("call_price"),
        "put_price": snapshot.get("put_price"),
        "iv_realized_spread_pct": round(spread, 4) if spread is not None else None,
        "iv_realized_ratio": round(ratio, 4) if ratio is not None else None,
        "source": snapshot.get("source"),
        "as_of": snapshot.get("as_of"),
    }


# ── Singleton ─────────────────────────────────────────────────────────────────
iv_regime_service = IVRegimeStrategyService()
