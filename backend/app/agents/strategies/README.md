# Strategy Creation Guide for AssetManager 🧠📉

When creating a new trading strategy engine for AssetManager (e.g., `ICTEngine`, `MACDCrossoverEngine`), you MUST implement the `IStrategyEngine` interface.

To maintain algorithmic integrity and prevent dangerously optimistic backtests, every strategy must strictly adhere to the following **three pillars**:

## 1. 🔍 Avoiding Look-Ahead Bias (Sesgo de Precognición)

**Definition:** Look-ahead bias occurs when a strategy uses data or information that was not yet known or available during the period being simulated. 

**Rules for Strategy Implementation (`run_session`):**
- **Strictly Point-in-Time:** At each chronological time step `t` (e.g., inside the `for idx, candle in enumerate(m1_candles):` loop), you must build all features and technical indicators using **ONLY** the information available up to and including `idx`.
- **No Future Data:** Never compute an indicator like ATR, RSI, or Average Volume using the entire day's data `m1_candles[-20:]` or `m1_candles` beforehand.
- **Rolling Buffers:** Calculate indicators on a sliding window explicitly ending at `idx`. 
  *Correct Pattern:*
  ```python
  # CORRECT: We only see up to time `idx`
  current_buffer = m1_candles[max(0, idx - 19) : idx + 1]
  atr = compute_ATR(current_buffer, period=14)
  ```
  *Incorrect Pattern:*
  ```python
  # WRONG: Calculation peeks into the future of the session
  atr = compute_ATR(m1_candles, period=14) 
  ```

## 2. 🚶 Walk-Forward Validation (Validación Hacia Adelante)

**Definition:** Evaluating a strategy using strictly sequential `Out-Of-Sample` periods without mixing past and future. We do not use random K-Folds for time series.

**Rules for Backtesting:**
- The engine supports this inherently via the `BacktestRunner.run_wfa(config)` command.
- The `WalkForwardSplitter` divides time chronologically. 
- You do not need to build WFA into your individual strategy logic; just ensure your strategy allows configuration parsing and that you invoke `run_wfa` rather than single-pass `run` when rigorously evaluating new alphas.

## 3. 🪦 Avoiding Survivorship Bias (Sesgo de Supervivencia)

**Definition:** Survivorship bias happens when backtesting is performed solely on current active assets (like the current S&P 500 roster), ignoring companies that went bankrupt, merged, or delisted.

**Rules for Testing & Data Services:**
- Always define universes based on **Point-in-Time** membership.
- For backtest configuration, define your asset lists taking into account historical deletions. 
- The DuckDB repository and BacktestRunner correctly handle missing days, meaning if an asset stops trading halfway through your backtest period, the system logs it as `missing_data_days`. Do not attempt to zero-fill data where the asset didn't exist. Let the engine naturally skip trading it.
