"""
MarkovVolatilityService
========================
Models 3 volatility regimes (Low / Med / High) via percentile-based state
assignment on rolling historical volatility, then exposes the full Markov
chain machinery:
  - State sequence (one label per trading day)
  - Transition probability matrix (3×3)
  - Per-state return distributions (mean, std, annualized vol, count)

This is the *observable-state* Markov model (Phase 1).
Phase 2 (latent-state HMM with Baum-Welch / Viterbi) is deferred.

Usage
-----
    from app.services.markov_vol_service import markov_vol_service
    result = await markov_vol_service.get_volatility_regimes("AAPL", days=500)
"""

from __future__ import annotations

import math
from typing import Any, Dict, List

import numpy as np
import pandas as pd

# ── State constants ────────────────────────────────────────────────────────────
STATE_LOW  = 0   # rolling-vol in bottom 33rd percentile
STATE_MED  = 1   # rolling-vol in 33rd–66th percentile
STATE_HIGH = 2   # rolling-vol above 66th percentile

STATE_LABELS: Dict[int, str] = {
    STATE_LOW:  "Low Volatility",
    STATE_MED:  "Med Volatility",
    STATE_HIGH: "High Volatility",
}

STATE_COLORS: Dict[int, str] = {
    STATE_LOW:  "#22c55e",   # green
    STATE_MED:  "#eab308",   # yellow
    STATE_HIGH: "#ef4444",   # red
}

_ANNUALIZE = math.sqrt(252)


class MarkovVolatilityService:
    """Percentile-based 3-state volatility Markov chain service."""

    def __init__(self) -> None:
        # Lazy imports to avoid circular-import issues at module load
        self._mds = None
        self._repo = None

    def _get_deps(self):
        if self._mds is None:
            from .market_data import market_data_service
            from .duckdb_store import duckdb_repo
            self._mds  = market_data_service
            self._repo = duckdb_repo

    # ──────────────────────────────────────────────────────────────────────────
    # Public API
    # ──────────────────────────────────────────────────────────────────────────

    async def get_volatility_regimes(
        self,
        symbol: str,
        days:   int = 500,
        window: int = 20,
    ) -> Dict[str, Any]:
        """
        Compute the full Markov volatility model for *symbol*.

        Returns
        -------
        dict with keys:
          symbol, window, state_labels, state_colors,
          regime_sequence   – list of {date, state, vol, ret}
          transition_matrix – row-stochastic 3×3 list-of-lists
          distributions     – per-state {mean_ret, std_ret, annualized_vol,
                               mean_ret_annualized, count, sharpe}
          current_state     – int (0/1/2)
          current_label     – str
          next_probs        – {label: probability}
        """
        self._get_deps()

        df = await self._fetch_ohlcv(symbol, days)
        if df is None or len(df) < window + 10:
            return {"error": f"Insufficient data for {symbol} (need >{window+10} rows)"}

        df = self._add_features(df, window)
        df = self._assign_states(df)

        regime_sequence = self._build_regime_sequence(df)
        tm               = self._transition_matrix(df["state"].tolist())
        distributions    = self._compute_distributions(df)
        current_state    = int(df["state"].iloc[-1])
        next_probs       = self._next_state_probs(tm, current_state)

        return {
            "symbol":           symbol.upper(),
            "window":           window,
            "total_days":       len(df),
            "state_labels":     {str(k): v for k, v in STATE_LABELS.items()},
            "state_colors":     {str(k): v for k, v in STATE_COLORS.items()},
            "regime_sequence":  regime_sequence,
            "transition_matrix": tm,
            "distributions":    distributions,
            "current_state":    current_state,
            "current_label":    STATE_LABELS[current_state],
            "next_probs":       next_probs,
        }

    # ──────────────────────────────────────────────────────────────────────────
    # Private helpers
    # ──────────────────────────────────────────────────────────────────────────

    async def _fetch_ohlcv(self, symbol: str, days: int) -> pd.DataFrame | None:
        """Try DuckDB first, fall back to market_data_service (Yahoo)."""
        try:
            conn = self._repo._connect(read_only=True)
            try:
                df = conn.execute(
                    "SELECT date, open, high, low, close, volume "
                    "FROM ohlcv WHERE symbol = ? ORDER BY date ASC",
                    [symbol.upper()],
                ).df()
            finally:
                conn.close()

            if len(df) >= days // 2:
                df["date"] = pd.to_datetime(df["date"])
                return df.tail(days).reset_index(drop=True)
        except Exception:
            pass

        # Fall back to market_data_service
        try:
            data = await self._mds.get_historical(symbol, limit=days)
            hist = data.get("historical", []) if data else []
            if not hist:
                return None
            records = [
                (h.__dict__ if hasattr(h, "__dict__") else h) for h in hist
            ]
            df = pd.DataFrame(records)
            df["date"] = pd.to_datetime(df["date"])
            df = df.sort_values("date").reset_index(drop=True)
            for col in ("open", "high", "low", "close", "volume"):
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors="coerce")
            return df
        except Exception:
            return None

    @staticmethod
    def _add_features(df: pd.DataFrame, window: int) -> pd.DataFrame:
        """Add log_ret and rolling_vol columns; drop leading NaN rows."""
        df = df.copy()
        df["log_ret"]    = np.log(df["close"] / df["close"].shift(1))
        df["rolling_vol"] = (
            df["log_ret"]
            .rolling(window)
            .std()
            .mul(_ANNUALIZE)          # annualized
        )
        df = df.dropna(subset=["rolling_vol", "log_ret"]).reset_index(drop=True)
        return df

    @staticmethod
    def _assign_states(df: pd.DataFrame) -> pd.DataFrame:
        """Assign state 0/1/2 based on global percentile of rolling_vol."""
        df = df.copy()
        p33 = df["rolling_vol"].quantile(1 / 3)
        p66 = df["rolling_vol"].quantile(2 / 3)
        df["state"] = np.where(
            df["rolling_vol"] <= p33, STATE_LOW,
            np.where(df["rolling_vol"] <= p66, STATE_MED, STATE_HIGH),
        ).astype(int)
        df["p33"] = p33
        df["p66"] = p66
        return df

    @staticmethod
    def _build_regime_sequence(df: pd.DataFrame) -> List[Dict[str, Any]]:
        seq: List[Dict[str, Any]] = []
        for _, row in df.iterrows():
            seq.append({
                "date":  str(row["date"])[:10],
                "state": int(row["state"]),
                "vol":   round(float(row["rolling_vol"]), 4),
                "ret":   round(float(row["log_ret"]), 6),
            })
        return seq

    @staticmethod
    def _transition_matrix(states: List[int]) -> List[List[float]]:
        """Row-stochastic 3×3 transition matrix (Laplace smoothed)."""
        # initialise with pseudocount 1 to avoid zero-probability rows
        counts = np.ones((3, 3))
        for i in range(len(states) - 1):
            s, t = states[i], states[i + 1]
            if 0 <= s <= 2 and 0 <= t <= 2:
                counts[s, t] += 1
        row_sums = counts.sum(axis=1, keepdims=True)
        tm = (counts / row_sums).tolist()
        return [[round(p, 4) for p in row] for row in tm]

    @staticmethod
    def _compute_distributions(df: pd.DataFrame) -> Dict[str, Any]:
        dists: Dict[str, Any] = {}
        for state in (STATE_LOW, STATE_MED, STATE_HIGH):
            subset = df[df["state"] == state]["log_ret"]
            if len(subset) == 0:
                dists[str(state)] = {}
                continue
            mean_d  = float(subset.mean())
            std_d   = float(subset.std(ddof=1)) if len(subset) > 1 else 0.0
            ann_vol = std_d * _ANNUALIZE
            ann_ret = mean_d * 252
            sharpe  = (ann_ret / ann_vol) if ann_vol > 0 else 0.0
            dists[str(state)] = {
                "mean_ret":            round(mean_d, 6),
                "std_ret":             round(std_d, 6),
                "annualized_vol_pct":  round(ann_vol * 100, 2),
                "annualized_ret_pct":  round(ann_ret * 100, 2),
                "sharpe":              round(sharpe, 3),
                "count":               int(len(subset)),
                "label":               STATE_LABELS[state],
                "color":               STATE_COLORS[state],
            }
        return dists

    @staticmethod
    def _next_state_probs(
        tm: List[List[float]], current_state: int
    ) -> Dict[str, float]:
        row = tm[current_state]
        return {STATE_LABELS[i]: round(row[i], 4) for i in range(3)}


# ── Module-level singleton ─────────────────────────────────────────────────────
markov_vol_service = MarkovVolatilityService()
