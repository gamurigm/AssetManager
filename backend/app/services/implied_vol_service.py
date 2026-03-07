"""
ImpliedVolService
=================
Black-Scholes IV inversion via Newton-Raphson (primary) + Brentq fallback.

Core idea: given a *market price* for a call or put option, find the σ
(implied volatility) such that:

    C_BS(S, K, T, r, σ)  =  C_market

The first-order approach uses Newton-Raphson:

    σ_{n+1} = σ_n - [C_BS(σ_n) - C_market] / ν(σ_n)

where ν = ∂C/∂σ = S · N'(d₁) · √T  (Vega).

If NR diverges (e.g. deep OTM with near-zero vega), we fall back to
scipy.optimize.brentq over σ ∈ [0.001, 20.0].

Usage
-----
    from app.services.implied_vol_service import implied_vol_service
    result = await implied_vol_service.get_iv_smile("SPY", rf=0.045)
"""

from __future__ import annotations

import math
from datetime import datetime
from typing import Any, Dict, List, Optional

import numpy as np

_SQRT2PI = math.sqrt(2 * math.pi)


# ── Pure Black-Scholes mathematics (no external deps) ─────────────────────────

def _norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2)))


def _norm_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / _SQRT2PI


def _d1d2(S: float, K: float, T: float, r: float, sigma: float):
    d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return d1, d2


def bs_price(opt_type: str, S: float, K: float, T: float, r: float, sigma: float) -> float:
    """European Black-Scholes call/put price."""
    d1, d2 = _d1d2(S, K, T, r, sigma)
    if opt_type.upper() == "PUT":
        return K * math.exp(-r * T) * _norm_cdf(-d2) - S * _norm_cdf(-d1)
    # CALL (default)
    return S * _norm_cdf(d1) - K * math.exp(-r * T) * _norm_cdf(d2)


def bs_vega(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """∂C/∂σ = S · N'(d₁) · √T  (same for calls and puts)."""
    d1, _ = _d1d2(S, K, T, r, sigma)
    return S * _norm_pdf(d1) * math.sqrt(T)


def newton_iv(
    market_price: float,
    S: float, K: float, T: float, r: float,
    opt_type: str = "CALL",
    tol: float = 1e-7,
    max_iter: int = 100,
) -> Optional[float]:
    """
    Newton-Raphson solver for implied volatility.
    Returns σ ∈ (0, ∞) or None if it fails to converge.
    """
    sigma = 0.20  # initial guess: 20%
    for _ in range(max_iter):
        price  = bs_price(opt_type, S, K, T, r, sigma)
        vega   = bs_vega(S, K, T, r, sigma)
        diff   = price - market_price
        if abs(diff) < tol:
            return sigma
        if abs(vega) < 1e-12:
            return None
        sigma -= diff / vega
        if sigma <= 0 or sigma > 30.0:
            return None
    return None


def brentq_iv(
    market_price: float,
    S: float, K: float, T: float, r: float,
    opt_type: str = "CALL",
) -> Optional[float]:
    """
    Brentq bracketed root-finder fallback (scipy).
    Guaranteed convergence if a root exists in [σ_lo, σ_hi].
    """
    try:
        from scipy.optimize import brentq

        def objective(sigma: float) -> float:
            return bs_price(opt_type, S, K, T, r, sigma) - market_price

        lo, hi = 1e-4, 20.0
        # Verify bracket straddles zero
        f_lo, f_hi = objective(lo), objective(hi)
        if f_lo * f_hi > 0:
            return None
        return brentq(objective, lo, hi, xtol=1e-7, maxiter=500)
    except Exception:
        return None


def compute_iv(
    market_price: float,
    S: float, K: float, T: float, r: float,
    opt_type: str = "CALL",
) -> Optional[float]:
    """
    Try Newton-Raphson → fallback Brentq → return None on failure.
    Returns implied volatility as a decimal (0.20 = 20%).
    """
    if T <= 0 or market_price <= 0 or S <= 0 or K <= 0:
        return None
    iv = newton_iv(market_price, S, K, T, r, opt_type)
    if iv is None or iv <= 0:
        iv = brentq_iv(market_price, S, K, T, r, opt_type)
    if iv is None or iv <= 1e-4 or iv > 15.0:  # sanity range: 0.01% – 1500%
        return None
    return iv


# ── Service class ──────────────────────────────────────────────────────────────

class ImpliedVolService:
    """
    Fetches live options chain from yfinance and computes per-contract IV
    via Black-Scholes inversion.  Returns a structured JSON response with
    the IV smile per expiration.
    """

    async def get_iv_smile(
        self,
        symbol: str,
        rf: float = 0.045,
    ) -> Dict[str, Any]:
        """
        Compute the full IV smile across strikes for all near-term expirations.

        Returns
        -------
        {
          symbol, spot, rf, as_of,
          expirations: [
            { exp_date, dte, atm_iv,
              smile: [{
                strike, moneyness_pct, iv, iv_pct, type,
                market_price, bid, ask, volume, open_interest
              }]
            }
          ]
        }
        """
        try:
            import yfinance as yf
        except ImportError:
            return {"error": "yfinance not installed"}

        ticker = yf.Ticker(symbol.upper())

        # --- spot price ---
        try:
            hist = ticker.history(period="2d")
            if hist.empty:
                return {"error": f"No price data for {symbol}"}
            S = float(hist["Close"].iloc[-1])
        except Exception as e:
            return {"error": f"Failed to fetch spot price: {e}"}

        today = datetime.now()
        expirations_out: List[Dict[str, Any]] = []

        # Limit to 8 nearest expirations to keep latency reasonable
        exp_dates = getattr(ticker, "options", [])[:8]
        if not exp_dates:
            return {"error": f"No options chain found for {symbol} — may not have listed options"}

        for exp_str in exp_dates:
            try:
                exp_date = datetime.strptime(exp_str, "%Y-%m-%d")
                dte = (exp_date - today).days
                if dte <= 0:
                    continue

                T = dte / 365.0
                chain = ticker.option_chain(exp_str)

                calls = self._extract_contracts(chain.calls, "CALL", S, K_col="strike", T=T, r=rf)
                puts  = self._extract_contracts(chain.puts,  "PUT",  S, K_col="strike", T=T, r=rf)

                all_contracts = sorted(calls + puts, key=lambda x: (x["strike"], x["type"]))
                if not all_contracts:
                    continue

                # ATM IV: closest call to spot
                call_contracts = [c for c in all_contracts if c["type"] == "CALL" and c["iv"] is not None]
                atm_iv: Optional[float] = None
                if call_contracts:
                    atm_call = min(call_contracts, key=lambda c: abs(c["strike"] - S))
                    atm_iv = atm_call["iv"]

                expirations_out.append({
                    "exp_date": exp_str,
                    "dte": dte,
                    "atm_iv": round(atm_iv * 100, 2) if atm_iv is not None else None,
                    "smile": all_contracts,
                })

            except Exception:
                continue

        if not expirations_out:
            return {"error": f"Could not compute IV smile for {symbol} — insufficient options data"}

        return {
            "symbol":      symbol.upper(),
            "spot":        round(S, 4),
            "rf":          rf,
            "as_of":       today.strftime("%Y-%m-%d %H:%M"),
            "expirations": expirations_out,
        }

    async def get_atm_iv_snapshot(
        self,
        symbol: str,
        rf: float = 0.045,
    ) -> Dict[str, Any]:
        """
        Return a compact ATM snapshot from the live options chain.

        The snapshot is built from the nearest listed expiration with usable
        ATM call/put IVs derived from real option prices via Black-Scholes.
        """
        smile = await self.get_iv_smile(symbol, rf=rf)
        if "error" in smile:
            return smile

        spot = float(smile.get("spot", 0.0) or 0.0)
        best: Optional[Dict[str, Any]] = None
        best_key: Optional[tuple[int, float]] = None

        for exp in smile.get("expirations", []):
            contracts = exp.get("smile", [])
            calls = [c for c in contracts if c.get("type") == "CALL" and c.get("iv_pct") is not None]
            puts = [c for c in contracts if c.get("type") == "PUT" and c.get("iv_pct") is not None]
            if not calls and not puts:
                continue

            atm_call = min(calls, key=lambda c: abs(float(c["strike"]) - spot)) if calls else None
            atm_put = min(puts, key=lambda c: abs(float(c["strike"]) - spot)) if puts else None

            strike_candidates = [float(c["strike"]) for c in (atm_call, atm_put) if c is not None]
            if not strike_candidates:
                continue

            strike = float(sum(strike_candidates) / len(strike_candidates))
            distance = min(abs(s - spot) for s in strike_candidates)
            dte = int(exp.get("dte", 999999) or 999999)
            key = (dte, distance)
            if best_key is not None and key >= best_key:
                continue

            iv_terms = [float(c["iv_pct"]) for c in (atm_call, atm_put) if c is not None and c.get("iv_pct") is not None]
            avg_iv = float(sum(iv_terms) / len(iv_terms)) if iv_terms else None
            skew = None
            if atm_call is not None and atm_put is not None:
                skew = float(atm_put["iv_pct"]) - float(atm_call["iv_pct"])

            best = {
                "symbol": symbol.upper(),
                "spot": round(spot, 4),
                "rf": rf,
                "as_of": smile.get("as_of"),
                "source": "live_options_chain_bs",
                "exp_date": exp.get("exp_date"),
                "dte": dte,
                "strike": round(strike, 4),
                "moneyness_pct": round((strike - spot) / spot * 100, 4) if spot > 0 else None,
                "atm_call_iv": round(float(atm_call["iv_pct"]), 4) if atm_call is not None else None,
                "atm_put_iv": round(float(atm_put["iv_pct"]), 4) if atm_put is not None else None,
                "atm_iv": round(avg_iv, 4) if avg_iv is not None else None,
                "skew_pct": round(skew, 4) if skew is not None else None,
                "call_price": round(float(atm_call["market_price"]), 4) if atm_call is not None else None,
                "put_price": round(float(atm_put["market_price"]), 4) if atm_put is not None else None,
            }
            best_key = key

        if best is None:
            return {"error": f"Could not derive ATM IV snapshot for {symbol}"}

        return best

    # ── helpers ───────────────────────────────────────────────────────────────

    @staticmethod
    def _extract_contracts(
        df,
        opt_type: str,
        S: float,
        K_col: str,
        T: float,
        r: float,
    ) -> List[Dict[str, Any]]:
        """
        Convert a yfinance calls/puts DataFrame to a list of contract dicts
        with computed IV.  Only include contracts with a usable market price.
        """
        results: List[Dict[str, Any]] = []
        if df is None or df.empty:
            return results

        for _, row in df.iterrows():
            try:
                K = float(row.get(K_col, 0) or 0)
                bid = float(row.get("bid", 0) or 0)
                ask = float(row.get("ask", 0) or 0)
                last = float(row.get("lastPrice", 0) or 0)
                volume = int(row.get("volume", 0) or 0)
                oi = int(row.get("openInterest", 0) or 0)

                if K <= 0:
                    continue

                # Use mid-price if available, fallback to last traded price
                if bid > 0 and ask > 0:
                    market_price = (bid + ask) / 2.0
                elif last > 0:
                    market_price = last
                else:
                    continue  # no usable price

                iv = compute_iv(market_price, S, K, T, r, opt_type)
                if iv is None:
                    continue

                moneyness = round((K - S) / S * 100, 2)  # negative = ITM for calls

                results.append({
                    "strike":        round(K, 2),
                    "moneyness_pct": moneyness,
                    "type":          opt_type,
                    "iv":            round(iv, 6),
                    "iv_pct":        round(iv * 100, 2),
                    "market_price":  round(market_price, 4),
                    "bid":           round(bid, 4),
                    "ask":           round(ask, 4),
                    "volume":        volume,
                    "open_interest": oi,
                })
            except Exception:
                continue

        return results


# ── Module-level singleton ─────────────────────────────────────────────────────
implied_vol_service = ImpliedVolService()
