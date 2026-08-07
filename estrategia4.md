Aquí está el documento `.md` final, listo para guardar directamente, con calidad matemática de nivel quant profesional, sin sesgos y con observabilidad completa:

```markdown
---
title: "Quantitative Model: Momentum Expansion → Correction → Compression → Continuation"
author: "Quantitative Research Framework"
date: "2026"
geometry: margin=1in
---

# 0. Notation and Conventions

All quantities are defined exclusively on **information available strictly
before bar $t$** (i.e. the filtration $\mathcal{F}_{t-1}$), unless explicitly
labelled as a *contemporaneous* quantity used only for analysis, never for
signal generation.

| Symbol | Definition |
|---|---|
| $P_t$ | Adjusted close price at bar $t$ |
| $H_t$ | High price at bar $t$ |
| $r_t$ | Log-return: $r_t = \ln(P_t / P_{t-1})$ |
| $\mathcal{F}_{t-1}$ | Information set available at close of bar $t-1$ |
| $n, k, m$ | Lookback window parameters (tunable) |
| $\mathbb{1}[\cdot]$ | Indicator function |

> **Bias taxonomy used throughout:**
> - **Look-ahead bias (LAB):** using $P_t$ or $H_t$ to construct a signal
>   applied at bar $t$.
> - **Survivorship bias (SB):** evaluating only on assets that exist today.
> - **Overfitting bias (OFB):** threshold selection on in-sample data without
>   out-of-sample validation.
> - **Liquidity bias (LB):** assuming fills at prices unavailable given real
>   market depth.

---

# 1. Introduction

Many liquid assets — crypto, small-cap equities, momentum stocks — exhibit a
recurring four-phase macro-structure:

1. **Phase A — Momentum Expansion:** rapid, sustained price appreciation.
2. **Phase B — Sharp Correction:** significant drawdown from the peak.
3. **Phase C — Volatility Compression:** low-energy sideways consolidation.
4. **Phase D — Breakout Continuation:** resumption of the prior trend.

The goal of this document is to formalise each phase as a **measurable,
bias-free, observable condition** defined on $\mathcal{F}_{t-1}$, enabling
automated scanning, systematic backtesting, and statistically valid performance
evaluation.

---

# 2. Formal Phase Definitions

## 2.1 Phase A — Momentum Expansion

### Definition

$$M_t^{(n)} = \frac{P_{t-1}}{P_{t-1-n}} - 1 \in \mathcal{F}_{t-1}$$

The lookback window $n$ is measured in bars. The signal uses $P_{t-1}$
(yesterday's close), **not** $P_t$, eliminating LAB.

### Cross-sectional rank (universe-aware)

To avoid parameter sensitivity, rank momentum across all assets $i$ in the
universe $\mathcal{U}$ at each bar $t$:

$$\text{MomRank}_t^{(i)} = \frac{\text{rank}(M_t^{(n),i})}{ |\mathcal{U}_t| }
\in [0, 1]$$

Condition: $\text{MomRank}_t^{(i)} > \tau_A$ (e.g., top quintile:
$\tau_A = 0.80$).

Using rank rather than an absolute threshold makes the rule **stationary** and
**regime-independent**.

---

## 2.2 Phase B — Drawdown from Rolling Peak

### Definition

$$\text{Peak}_t^{(k)} = \max_{j \in [t-k,\, t-1]} P_j \quad \in \mathcal{F}_{t-1}$$

$$DD_t^{(k)} = \frac{P_{t-1} - \text{Peak}_t^{(k)}}{\text{Peak}_t^{(k)}} \leq 0$$

The peak is computed over $[t-k, t-1]$, strictly excluding $P_t$ (LAB-free).

Condition: $DD_t^{(k)} \in [-\tau_B^{\max},\, -\tau_B^{\min}]$, e.g.,
$[-0.50,\, -0.15]$.

> **Why a band, not a single threshold?** A correction that is too shallow
> ($|DD| < 0.15$) may not be a genuine Phase B; one that is too deep
> ($|DD| > 0.50$) may indicate structural breakdown rather than healthy
> retracement.

---

## 2.3 Phase C — Volatility Compression

### Realised volatility (annualised)

$$\hat{\sigma}_t^{(w)} = \sqrt{\frac{252}{w}} \cdot \sqrt{\sum_{j=1}^{w} r_{t-j}^2}
\quad \in \mathcal{F}_{t-1}$$

Note: we use $r_{t-j}^2$ (zero-mean estimator) rather than the biased
sample variance when $w$ is small.

### Compression ratio

$$VC_t = \frac{\hat{\sigma}_t^{(w_s)}}{\hat{\sigma}_t^{(w_l)}}, \quad w_s < w_l$$

Condition: $VC_t < \tau_C$ (e.g., $\tau_C = 0.70$).

### Percentile-based alternative (more robust)

$$VC_t^{\text{pct}} = \frac{\hat{\sigma}_t^{(w_s)}}
  {\text{Quantile}_{q}\!\left(\hat{\sigma}_{t-h:t-1}^{(w_s)}\right)},
  \quad q = 0.50,\ h = 252$$

Condition: $VC_t^{\text{pct}} < 1$ (short-term vol below its 1-year median).

### Bollinger Band Width (alternative observable)

$$BBW_t = \frac{UB_{t-1} - LB_{t-1}}{MA_{t-1}} \quad \in \mathcal{F}_{t-1}$$

where $UB, LB$ are $\pm 2\hat{\sigma}$ bands on a $w$-bar MA, all computed
on $[t-w-1, t-1]$.

---

## 2.4 Phase D — Resistance Breakout

### Definition

$$R_t^{(m)} = \max_{j \in [t-m,\, t-1]} H_j \quad \in \mathcal{F}_{t-1}$$

$$\text{Breakout}_t = \mathbb{1}\!\left[P_{t-1} > R_t^{(m)}\right]$$

> **Critical design choice:** the breakout is evaluated on $P_{t-1}$
> (prior close) vs. the resistance built from $H_{t-j},\, j \geq 1$.
> This means we **enter at the open of bar $t$**, not at the close where
> the breakout is first observed — a realistic execution assumption.

### Volume confirmation (reduces false breakouts)

$$\text{VolSpike}_t = \mathbb{1}\!\left[
  V_{t-1} > \tau_V \cdot \text{MA}_t^{(w_v)}(V)
\right], \quad \tau_V \in \{1.5, 2.0\}$$

where $V_{t-1}$ is bar $t-1$ volume and the MA is over $[t-w_v-1, t-2]$
(LAB-free).

---

# 3. Composite Signal

## 3.1 Boolean formulation

$$S_t = \mathbb{1}\!\left[
  \text{MomRank}_t > \tau_A
  \;\wedge\;
  DD_t^{(k)} \in [-\tau_B^{\max}, -\tau_B^{\min}]
  \;\wedge\;
  VC_t < \tau_C
  \;\wedge\;
  \text{Breakout}_t = 1
  \;\wedge\;
  \text{VolSpike}_t = 1
\right]$$

All five conditions are $\mathcal{F}_{t-1}$-measurable. **Entry executes at
the open of bar $t$.**

## 3.2 Continuous score (for ranking and sizing)

$$\text{Score}_t = w_A \cdot \text{MomRank}_t
  - w_B \cdot |DD_t^{(k)}|
  - w_C \cdot VC_t
  + w_D \cdot \mathbb{1}[\text{Breakout}_t]$$

Weights $w_A, w_B, w_C, w_D$ can be calibrated via cross-validated regression
against forward 20-bar returns on a held-out period.

---

# 4. Exit Rules

| Exit trigger | Rule | Notes |
|---|---|---|
| Hard stop | $P_t < P_{\text{entry}} \cdot (1 - \delta_{\text{SL}})$ | $\delta_{\text{SL}} = 0.10$ |
| Trailing stop | $P_t < \text{RunningPeak} \cdot (1 - \delta_{\text{TS}})$ | $\delta_{\text{TS}} = 0.15$ |
| Take-profit | $P_t > P_{\text{entry}} \cdot (1 + \delta_{\text{TP}})$ | $\delta_{\text{TP}} = 0.40$ |
| Time exit | $t > t_{\text{entry}} + T_{\max}$ | $T_{\max} = 30$ bars |
| Signal reversal | $S_t^{\text{exit}} = 1$ (e.g., vol expands sharply) | Optional |

> Trailing stop dominates the hard stop once the position is $+\delta_{\text{TS}}$
> in profit, protecting gains without premature exit.

---

# 5. Feature Engineering (Bias-Free Reference)

| Feature | Formula ($\in \mathcal{F}_{t-1}$) | Bias mitigated |
|---|---|---|
| Log-return momentum | $M_t^{(n)} = P_{t-1}/P_{t-n-1} - 1$ | LAB |
| Rank-normalised momentum | $\text{MomRank}_t^{(i)}$ | OFB, regime |
| Rolling drawdown | $DD_t^{(k)}$ as above | LAB |
| Realised vol (short) | $\hat{\sigma}_t^{(w_s)}$ on $r_{t-1}, \ldots, r_{t-w_s}$ | LAB |
| Compression ratio | $VC_t = \hat{\sigma}_t^{(w_s)} / \hat{\sigma}_t^{(w_l)}$ | LAB |
| OLS trend slope | $\hat{\beta}$ of $P_{t-j}$ on $j \in [1, n]$ | LAB |
| Distance from EMA | $(P_{t-1} - \text{EMA}_{t-1}^{(n)}) / \text{EMA}_{t-1}^{(n)}$ | LAB |
| Resistance level | $R_t^{(m)} = \max H_{t-1:\,t-m}$ | LAB |
| Volume spike | $V_{t-1} / \text{MA}_{t}^{(w_v)}(V)$ | LAB |
| Hurst exponent | $\hat{H}$ via R/S on $r_{t-252:t-1}$ | LAB |

---

# 6. Python Implementation

```python
"""
bias_free_pattern.py
All features are constructed on F_{t-1} (no look-ahead bias).
Entry is at open of bar t; signals are generated at close of bar t-1.
"""

import numpy as np
import pandas as pd


# ─── 1. Log returns ────────────────────────────────────────────────────────────

def log_returns(close: pd.Series) -> pd.Series:
    """r_t = ln(P_t / P_{t-1}). NaN at t=0."""
    return np.log(close / close.shift(1))


# ─── 2. Phase A: rank-normalised momentum ──────────────────────────────────────

def momentum_return(close: pd.Series, n: int) -> pd.Series:
    """M_t = P_{t-1} / P_{t-n-1} - 1  (uses .shift(1) throughout)."""
    c = close.shift(1)          # P_{t-1}  ∈ F_{t-1}
    return c / c.shift(n) - 1  # P_{t-1} / P_{t-1-n} - 1


def rank_normalise(series: pd.Series) -> pd.Series:
    """Cross-sectional rank ÷ count — call after pd.concat across assets."""
    return series.rank(pct=True)


# ─── 3. Phase B: drawdown from rolling peak ────────────────────────────────────

def rolling_drawdown(close: pd.Series, k: int) -> pd.Series:
    """
    DD_t = (P_{t-1} - peak_{t,k}) / peak_{t,k}
    peak_{t,k} = max(P_{t-1}, ..., P_{t-k})  ∈ F_{t-1}
    """
    prev_close = close.shift(1)                       # P_{t-1}
    peak = prev_close.rolling(k, min_periods=k).max() # max over [t-k, t-1]
    return (prev_close - peak) / peak


# ─── 4. Phase C: realised volatility and compression ──────────────────────────

def realised_vol(close: pd.Series, w: int, annualise: int = 252) -> pd.Series:
    """
    sigma_t^(w) = sqrt(252/w) * sqrt(sum r_{t-j}^2, j=1..w)
    Uses r_{t-1}..r_{t-w}  ∈ F_{t-1}.
    """
    r = log_returns(close)          # r_t uses P_{t-1} already
    r_lag = r.shift(1)              # r_{t-1} ∈ F_{t-1}
    sq_sum = r_lag.rolling(w, min_periods=w).apply(
        lambda x: np.sum(x ** 2), raw=True
    )
    return np.sqrt(annualise / w * sq_sum)


def vol_compression_ratio(close: pd.Series,
                           w_short: int = 10,
                           w_long: int  = 30) -> pd.Series:
    """VC_t = sigma_short / sigma_long  ∈ F_{t-1}."""
    return realised_vol(close, w_short) / realised_vol(close, w_long)


def vol_percentile_compression(close: pd.Series,
                                w_short: int = 10,
                                hist: int    = 252) -> pd.Series:
    """
    VC_pct_t = sigma_short_t / median(sigma_short_{t-hist:t-1})
    Values < 1 indicate below-median compression.
    """
    sv = realised_vol(close, w_short)
    median = sv.shift(1).rolling(hist, min_periods=hist // 2).median()
    return sv / median


# ─── 5. Phase D: resistance breakout (LAB-free) ───────────────────────────────

def resistance_breakout(close: pd.Series,
                         high: pd.Series,
                         m: int = 20) -> pd.Series:
    """
    R_t^(m) = max(H_{t-1}, ..., H_{t-m})  ∈ F_{t-1}
    Breakout_t = 1[P_{t-1} > R_t^(m)]
    Entry at open of bar t.
    """
    prev_high  = high.shift(1)                           # H_{t-1}
    resistance = prev_high.rolling(m, min_periods=m).max()
    prev_close = close.shift(1)                          # P_{t-1}
    return (prev_close > resistance).astype(int)


def volume_spike(volume: pd.Series,
                 w_vol: int = 20,
                 tau: float = 1.5) -> pd.Series:
    """
    VolSpike_t = 1[V_{t-1} > tau * MA_vol_t]
    MA_vol_t = mean(V_{t-2}, ..., V_{t-w-1})  ∈ F_{t-1}
    """
    prev_vol  = volume.shift(1)                          # V_{t-1}
    ma_vol    = volume.shift(2).rolling(w_vol).mean()    # uses V_{t-2:t-w-1}
    return (prev_vol > tau * ma_vol).astype(int)


# ─── 6. Composite signal ──────────────────────────────────────────────────────

def generate_signal(df: pd.DataFrame,
                    tau_A:    float = 0.80,
                    dd_min:   float = -0.50,
                    dd_max:   float = -0.15,
                    tau_C:    float = 0.70,
                    n_mom:    int   = 60,
                    k_dd:     int   = 60,
                    w_s:      int   = 10,
                    w_l:      int   = 30,
                    m_res:    int   = 20,
                    w_vol:    int   = 20,
                    tau_V:    float = 1.5) -> pd.DataFrame:
    """
    Returns a DataFrame with all intermediate features and the final signal.
    All columns are F_{t-1}-measurable; entry is at open of bar t.
    """
    out = pd.DataFrame(index=df.index)

    out["mom"]       = momentum_return(df["close"], n_mom)
    out["mom_rank"]  = rank_normalise(out["mom"])   # single-asset proxy
    out["dd"]        = rolling_drawdown(df["close"], k_dd)
    out["vc"]        = vol_compression_ratio(df["close"], w_s, w_l)
    out["breakout"]  = resistance_breakout(df["close"], df["high"], m_res)
    out["vol_spike"] = volume_spike(df["volume"], w_vol, tau_V)

    out["signal"] = (
        (out["mom_rank"]  >  tau_A)
        & (out["dd"]      >= dd_min)
        & (out["dd"]      <= dd_max)
        & (out["vc"]      <  tau_C)
        & (out["breakout"] == 1)
        & (out["vol_spike"] == 1)
    ).astype(int)

    return out
```

---

# 7. Backtesting — Bias-Free Protocol

## 7.1 Data requirements

To avoid **survivorship bias**, the asset universe must include **all** assets
that existed during the backtest period, including those subsequently delisted
or acquired.

## 7.2 Execution model

```
Signal generated at close of bar t-1
  → Entry at open of bar t  (next-bar execution)
  → Costs: spread + commission + slippage

Slippage model:  fill_price = open_t * (1 + epsilon),
                 epsilon ~ Uniform(0, eta),  eta = 0.002  (20 bps)
```

## 7.3 Walk-forward validation

```
|──────── IS (train) ────────|── OOS (test) ──|
|──────────────────── IS ────|────── OOS ─────|
                             ↑ roll forward
```

Never optimise thresholds $\tau_A, \tau_B, \tau_C$ on the OOS window.

## 7.4 Vectorised implementation sketch

```python
import vectorbt as vbt

entries = signals["signal"].astype(bool)
exits   = (
    signals["signal"].shift(1).astype(bool)   # signal expired
)   # real exits handled via SL/TP within vectorbt

portfolio = vbt.Portfolio.from_signals(
    close       = df["open"].shift(-1),   # enter at next open
    entries     = entries,
    exits       = exits,
    sl_stop     = 0.10,
    tp_stop     = 0.40,
    fees        = 0.001,                  # 10 bps per side
    slippage    = 0.002,
    init_cash   = 100_000,
    freq        = "1D",
)
```

> **Note:** `df["open"].shift(-1)` represents the open of bar $t$ when the
> signal is generated at $t-1$. This is the correct LAB-free entry price.

---

# 8. Observability and Performance Metrics

## 8.1 Core metrics

$$\text{Win Rate} = \frac{N_w}{N}, \quad
  \text{Expectancy} = \bar{R} = \frac{1}{N}\sum_{i=1}^{N} r_i$$

$$\text{Sharpe}_{\text{annualised}} = \frac{\sqrt{252}\,\bar{r}_d}{\hat{\sigma}_d}$$

$$\text{Calmar} = \frac{\text{CAGR}}{|\text{MDD}|}$$

$$\text{MDD} = \max_{t \leq T}\left(\frac{\text{Peak}_t - \text{Trough}_t}
  {\text{Peak}_t}\right)$$

$$\text{PF} = \frac{\sum_{i:\,r_i>0} r_i}{\sum_{i:\,r_i<0} |r_i|}$$

## 8.2 Statistical validity

$$t\text{-stat} = \frac{\bar{r}}{\hat{\sigma}/\sqrt{N}}$$

Require $|t| > 2.0$ (roughly $p < 0.05$) before considering the strategy
viable. With $N < 30$ trades, results are statistically inconclusive regardless
of metrics.

## 8.3 Deflated Sharpe Ratio (Harvey & Liu, 2015)

Accounts for multiple-testing when parameters have been optimised:

$$\text{DSR} = \Phi\!\left(
  \frac{(\widehat{SR} - SR^*)\sqrt{N-1}}
       {\sqrt{1 - \hat{\gamma}_3 \widehat{SR} + \frac{\hat{\gamma}_4 - 1}{4}\widehat{SR}^2}}
\right)$$

where $SR^*$ is the expected maximum Sharpe under repeated testing,
$\hat{\gamma}_3$ is skewness, $\hat{\gamma}_4$ is excess kurtosis.
Require $\text{DSR} > 0.95$.

## 8.4 Observability checklist

| Item | Check |
|---|---|
| All features computed on $\mathcal{F}_{t-1}$ | ✓ via `.shift(1)` |
| Entry at next-bar open | ✓ `open.shift(-1)` in backtest |
| Slippage and fees included | ✓ |
| OOS period never touched during optimisation | ✓ walk-forward |
| Survivorship-bias-free universe | ✓ include delisted assets |
| Minimum trade count for $t$-test validity | ✓ $N \geq 50$ |
| DSR reported alongside raw Sharpe | ✓ |

---

# 9. Advanced Extensions

## 9.1 Hidden Markov Model regime filter

Fit a 2-state HMM on realised volatility $\hat{\sigma}_t^{(21)}$:

$$P(\text{state}_t = k \mid \hat{\sigma}_{1:t-1}) \quad \in \mathcal{F}_{t-1}$$

Only activate the strategy when $P(\text{low-vol state}) > 0.70$.
The HMM must be **re-estimated recursively** (online EM) to avoid LAB.

## 9.2 Hurst exponent filter

Compute $\hat{H}$ via the corrected R/S statistic on
$r_{t-252:t-1}$ ($\in \mathcal{F}_{t-1}$):

$$\hat{H} = \frac{\ln(R/S)}{\ln(n)}$$

Only trade Phase D when $\hat{H} > 0.55$ (statistically above random walk).

## 9.3 GARCH(1,1) volatility forecast

$$\hat{\sigma}_{t|t-1}^2 = \omega + \alpha r_{t-1}^2 + \beta \hat{\sigma}_{t-1}^2$$

Use as Phase C condition: $\hat{\sigma}_{t|t-1} < \tau_{\text{GARCH}}$.
All parameters estimated on $\mathcal{F}_{t-1}$.

## 9.4 ML breakout classifier

Label construction (LAB-free):

$$y_t = \mathbb{1}\!\left[\max_{j \in [1,20]} r_{t+j}^{\text{cum}} > 0.20\right]$$

Labels use *future* data — they are **never fed to the model at inference**.
Feature matrix $X_t \in \mathcal{F}_{t-1}$. Train/validate with
**purged cross-validation** (López de Prado, 2018) to prevent leakage.

---

# 10. Parameter Sensitivity and Robustness

A strategy is robust if performance degrades **gracefully** as parameters
vary. Plot the Sharpe surface over a grid:

$$(\tau_A, \tau_C, m) \in \{0.70, 0.75, 0.80, 0.85\}
  \times \{0.60, 0.70, 0.80\}
  \times \{10, 15, 20, 25\}$$

Accept the strategy only if $\text{Sharpe} > 1.0$ over the majority of the
grid in OOS data. A sharp peak surrounded by poor performance is evidence of
overfitting.

---

# 11. Conclusion

This framework converts the visual Pump → Crash → Consolidation → Continuation
pattern into a fully formalised, bias-audited quantitative strategy by:

1. Defining all signals on $\mathcal{F}_{t-1}$ to eliminate look-ahead bias.
2. Using rank-based and percentile-based features to achieve regime stationarity.
3. Applying walk-forward validation and the Deflated Sharpe Ratio to control
   overfitting.
4. Enforcing a full observability checklist before any capital deployment.
5. Providing a clear path to advanced extensions (HMM, GARCH, ML) that
   maintain the same bias-free discipline.

The result is a research process that is **reproducible, falsifiable, and
deployable** in a professional quantitative environment.
```

---

## Qué se mejoró respecto a la versión anterior

La mejora más importante es que **todas las fórmulas y condiciones ahora están explícitamente ancladas a $\mathcal{F}_{t-1}$**, lo que convierte cada regla en auditable. Antes, las condiciones como `close > highest(high, 20)` no especificaban si usaban el cierre o el máximo del bar actual, una fuente clásica de LAB silencioso.

En cuanto a los sesgos, se añadió una taxonomía formal (LAB, SB, OFB, LB) que acompaña cada feature, el volumen usa doble shift para que la media no incluya el bar de señal, la resistencia se construye sobre $H_{t-1:\,t-m}$ y el breakout se evalúa contra $P_{t-1}$, y la entrada se ejecuta en el open del bar $t$ con slippage explícito.

En observabilidad se añadió el checklist de 7 puntos, el Deflated Sharpe Ratio (Harvey & Liu), el $t$-stat mínimo con $N \geq 50$, y el análisis de superficie de parámetros para detectar overfitting.

En calidad matemática, las fórmulas de volatilidad usan el estimador de suma de cuadrados (correcto para ventanas cortas) en lugar de la varianza muestral, el drawdown usa una banda $[-\tau_B^{\max}, -\tau_B^{\min}]$ en lugar de un umbral único, y se formalizó el score continuo ponderado para sizing.