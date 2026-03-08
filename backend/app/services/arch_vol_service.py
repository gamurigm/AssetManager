"""
ArchVolService
==============
ARCH / GARCH(p,q) conditional heteroscedasticity — pure NumPy/SciPy,
no external `arch` library required.

Model (GARCH(1,1)):
    r_t   = mu + eps_t,      eps_t ~ N(0, sig2_t)
    sig2_t = omega + alpha*eps2_{t-1} + beta*sig2_{t-1}

Key outputs:
  - conditional_vol  : [{date, sigma_pct, sigma_ann_pct}] per trading day
  - params           : {mu, omega, alpha, beta, persistence}
  - fit              : {log_likelihood, aic, bic}
  - forecast         : {h1, h5, h21}  (annualised vol forecast, %)
  - var              : {var_95_pct, var_99_pct}  (daily Value-at-Risk, %)
  - arch_lm_test     : {stat, p_value}  — Engle LM test on residuals
  - long_run_vol_ann : long-run (unconditional) annualised vol (%)

The MLE uses scipy.optimize.minimize with method='L-BFGS-B' plus a
numerical gradient approximation for speed.  ω,α,β are parameterised in
log-space to enforce positivity automatically.

Usage
-----
    from app.services.arch_vol_service import arch_vol_service
    result = await arch_vol_service.get_garch(symbol="AAPL", days=500)
"""

from __future__ import annotations

import math
from datetime import datetime
from typing import Any, Dict, List, Optional

import numpy as np

_ANNUALIZE = math.sqrt(252)


# ── GARCH(1,1) core ───────────────────────────────────────────────────────────

def _filter_garch(params: np.ndarray, rets: np.ndarray
                   ) -> tuple[np.ndarray, np.ndarray]:
    """
    Kalman-like GARCH variance filter.
    Returns (sigma2_series, eps_series).
    params = [mu, log_omega, log_alpha, log_beta]
    """
    mu       = params[0]
    omega    = math.exp(params[1])
    alpha    = math.exp(params[2])
    beta     = math.exp(params[3])

    n    = len(rets)
    eps  = rets - mu
    sig2 = np.empty(n)

    # Initialise with unconditional variance (or sample var as fallback)
    denom = max(1.0 - alpha - beta, 1e-8)
    sig2[0] = omega / denom
    if sig2[0] < 1e-12:
        sig2[0] = float(np.var(rets))

    for t in range(1, n):
        sig2[t] = omega + alpha * eps[t - 1] ** 2 + beta * sig2[t - 1]
        sig2[t] = max(sig2[t], 1e-12)

    return sig2, eps


def _neg_log_likelihood(params: np.ndarray, rets: np.ndarray) -> float:
    """Gaussian GARCH(1,1) negative log-likelihood."""
    try:
        sig2, eps = _filter_garch(params, rets)
        alpha = math.exp(params[2])
        beta  = math.exp(params[3])
        if alpha + beta >= 0.9999:          # covariance-stationarity constraint
            return 1e10
        ll = -0.5 * np.sum(np.log(sig2) + eps ** 2 / sig2)
        return -ll
    except Exception:
        return 1e10


def _fit_garch(rets: np.ndarray) -> Optional[Dict[str, Any]]:
    """
    Fit GARCH(1,1) via L-BFGS-B.
    Returns dict with params + fit quality, or None on failure.
    """
    from scipy.optimize import minimize

    # Initial guess in log-space: ω~sample_var*0.05, α~0.10, β~0.85
    sv = float(np.var(rets))
    mu0   = float(np.mean(rets))
    x0    = np.array([mu0, math.log(max(sv * 0.05, 1e-10)),
                      math.log(0.10), math.log(0.85)])

    bounds = [
        (-0.1, 0.1),               # mu
        (-20.0, -2.0),             # log_omega  (very small positive)
        (-6.0, -0.1),              # log_alpha  (0.002 – 0.90)
        (-6.0, -0.01),             # log_beta   (0.002 – 0.99)
    ]

    result = minimize(
        _neg_log_likelihood, x0, args=(rets,),
        method='L-BFGS-B', bounds=bounds,
        options={'maxiter': 3000, 'ftol': 1e-12, 'gtol': 1e-8},
    )

    if not result.success and result.fun > 1e9:
        return None

    p       = result.x
    mu      = float(p[0])
    omega   = float(math.exp(p[1]))
    alpha   = float(math.exp(p[2]))
    beta    = float(math.exp(p[3]))
    ll      = float(-result.fun)
    k       = 4   # number of parameters
    n       = len(rets)
    aic     = 2 * k - 2 * ll
    bic     = k * math.log(n) - 2 * ll

    return {
        "x":     p,
        "mu":    mu,
        "omega": omega,
        "alpha": alpha,
        "beta":  beta,
        "ll":    ll,
        "aic":   aic,
        "bic":   bic,
    }


def _garch_forecast(omega: float, alpha: float, beta: float,
                    last_eps2: float, last_sig2: float,
                    horizons: List[int]) -> Dict[int, float]:
    """
    Multi-step-ahead GARCH(1,1) forecast.
    E[sig2_{t+h}] = (omega/(1-alpha-beta)) + (alpha+beta)^h * (sig2_t - omega/(1-alpha-beta))
    Returns annualised vol forecast per horizon.
    """
    persist = alpha + beta
    lr_var  = omega / max(1.0 - persist, 1e-8)
    out: Dict[int, float] = {}
    for h in horizons:
        var_h = lr_var + persist ** h * (last_sig2 - lr_var)
        var_h = max(var_h, 1e-12)
        out[h] = math.sqrt(var_h * 252) * 100   # annualised %
    return out


def _engle_lm_test(std_resid: np.ndarray, lags: int = 5) -> Dict[str, float]:
    """
    Engle (1982) LM test for remaining ARCH effects in standardised residuals.
    H0: no ARCH effects remaining (model is adequate).
    Returns test statistic and chi-squared p-value.
    """
    from scipy.stats import chi2 as chi2_dist

    e2 = std_resid ** 2
    n  = len(e2)
    if n <= lags + 1:
        return {"stat": float("nan"), "p_value": float("nan")}

    y = e2[lags:]
    X = np.column_stack([e2[lags - i - 1: n - i - 1] for i in range(lags)])
    X = np.column_stack([np.ones(len(y)), X])

    try:
        β    = np.linalg.lstsq(X, y, rcond=None)[0]
        yhat = X @ β
        ssr  = float(np.sum((yhat - y.mean()) ** 2))
        sst  = float(np.sum((y - y.mean()) ** 2))
        r2   = ssr / sst if sst > 0 else 0.0
        stat = n * r2
        pval = float(1 - chi2_dist.cdf(stat, df=lags))
    except Exception:
        stat, pval = float("nan"), float("nan")

    return {"stat": round(stat, 4), "p_value": round(pval, 4)}


# ── Service class ──────────────────────────────────────────────────────────────

class ArchVolService:
    """Fits GARCH(1,1) to historical returns and exposes volatility analytics."""

    def __init__(self) -> None:
        self._mds  = None
        self._repo = None

    def _get_deps(self):
        if self._mds is None:
            from .market_data import market_data_service
            from ..core.container import duckdb_repo
            self._mds  = market_data_service
            self._repo = duckdb_repo

    async def get_garch(
        self,
        symbol: str,
        days:   int = 500,
    ) -> Dict[str, Any]:
        """
        Fit GARCH(1,1) on the last *days* trading sessions and return:
          symbol, n_obs, params, fit, forecast, var, arch_lm_test,
          long_run_vol_ann, conditional_vol (sequence)
        """
        self._get_deps()

        df = await self._fetch_ohlcv(symbol, days)
        if df is None or len(df) < 50:
            return {"error": f"Insufficient data for {symbol} (need ≥50 rows)"}

        import pandas as pd

        df = df.sort_values("date").reset_index(drop=True)
        df["log_ret"] = np.log(df["close"] / df["close"].shift(1))
        df = df.dropna(subset=["log_ret"]).reset_index(drop=True)

        rets = df["log_ret"].values.astype(float)
        n    = len(rets)

        fit = _fit_garch(rets)
        if fit is None:
            return {"error": "GARCH optimisation failed to converge"}

        # Build conditional variance series
        sig2, eps = _filter_garch(fit["x"], rets)
        sigma     = np.sqrt(sig2)           # daily conditional vol
        sigma_ann = sigma * _ANNUALIZE      # annualised conditional vol

        # Standardised residuals for diagnostics
        std_resid = eps / np.maximum(sigma, 1e-12)

        # Build date-aligned output sequence
        cond_vol: List[Dict[str, Any]] = []
        for i in range(n):
            cond_vol.append({
                "date":          str(df["date"].iloc[i])[:10],
                "sigma_pct":     round(float(sigma[i]) * 100, 4),
                "sigma_ann_pct": round(float(sigma_ann[i]) * 100, 2),
                "ret_pct":       round(float(rets[i]) * 100, 4),
            })

        # Forecast
        last_eps2 = float(eps[-1] ** 2)
        last_sig2 = float(sig2[-1])
        forecast  = _garch_forecast(
            fit["omega"], fit["alpha"], fit["beta"],
            last_eps2, last_sig2, [1, 5, 21],
        )

        # Long-run (unconditional) vol
        persist   = fit["alpha"] + fit["beta"]
        lr_var    = fit["omega"] / max(1.0 - persist, 1e-8)
        lr_vol    = round(math.sqrt(lr_var * 252) * 100, 2)

        # VaR (parametric, daily %)
        from scipy.stats import norm as sp_norm
        var_95 = round(float(-sp_norm.ppf(0.05) * sigma[-1]) * 100, 4)
        var_99 = round(float(-sp_norm.ppf(0.01) * sigma[-1]) * 100, 4)

        # LM test
        lm = _engle_lm_test(std_resid, lags=5)

        return {
            "symbol":         symbol.upper(),
            "n_obs":          n,
            "model":          "GARCH(1,1)",
            "params": {
                "mu":          round(fit["mu"] * 100, 6),     # daily %
                "omega":       f"{fit['omega']:.2e}",
                "alpha":       round(fit["alpha"], 6),
                "beta":        round(fit["beta"],  6),
                "persistence": round(persist, 6),             # α + β
            },
            "fit": {
                "log_likelihood": round(fit["ll"], 2),
                "aic":            round(fit["aic"], 2),
                "bic":            round(fit["bic"], 2),
            },
            "long_run_vol_ann_pct": lr_vol,
            "current_sigma_ann_pct": round(float(sigma_ann[-1]) * 100, 2),
            "forecast": {
                "h1_ann_pct":  round(forecast[1],  2),
                "h5_ann_pct":  round(forecast[5],  2),
                "h21_ann_pct": round(forecast[21], 2),
            },
            "var_daily": {
                "var_95_pct": var_95,
                "var_99_pct": var_99,
            },
            "arch_lm_test": {
                "stat":    lm["stat"],
                "p_value": lm["p_value"],
                "adequate": lm["p_value"] > 0.05 if not math.isnan(lm["p_value"]) else None,
            },
            "conditional_vol": cond_vol,
        }

    async def _fetch_ohlcv(self, symbol: str, days: int):
        """DuckDB first, fallback to market_data_service."""
        import pandas as pd

        try:
            conn = self._repo._connect(read_only=True)
            try:
                df = conn.execute(
                    "SELECT date, close FROM ohlcv WHERE symbol = ? ORDER BY date ASC",
                    [symbol.upper()],
                ).df()
            finally:
                conn.close()
            if len(df) >= days // 2:
                df["date"] = pd.to_datetime(df["date"])
                df["close"] = pd.to_numeric(df["close"], errors="coerce")
                return df.dropna(subset=["close"]).tail(days).reset_index(drop=True)
        except Exception:
            pass

        try:
            data = await self._mds.get_historical(symbol, limit=days)
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


# ── Singleton ──────────────────────────────────────────────────────────────────
arch_vol_service = ArchVolService()
