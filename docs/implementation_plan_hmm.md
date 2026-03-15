# HMM Implementation Plan: Market Regime Detection

## Objective
Implement a Hidden Markov Model (HMM) to detect market regimes (Bull, Bear, Choppy) using historical OHLCV data stored in DuckDB. This will enhance the AI Agent's decision-making capabilities.

## Architecture
- **Location**: `backend/app/analytics/models/hmm.py` (New quantitative module)
- **Library**: `hmmlearn` (Install via pip)
- **Data Source**: `DuckDBRepository`

## Implementation Steps

### 1. Setup & Environment
- [ ] Install dependencies (`hmmlearn`, `scikit-learn`, `pandas`, `numpy`)
- [ ] Create `backend/app/analytics` directory structure

### 2. Core HMM Logic
- [ ] Implement `MarketRegimeModel` class
    - **Input**: Historical OHLCV (pandas DataFrame)
    - **Features**: Log Returns, Volatility (Rolling Std Dev), Volume Change
    - **Model**: GaussianHMM with 3 components (Bull, Bear, Neutral)
    - **Training**: Fit model on historical data
    - **Prediction**: Predict hidden states for the sequence
- [ ] Develop helper to interpret states (e.g., map state 0 -> "Low Volatility Bullish")

### 3. API Integration
- [ ] Create endpoint `GET /api/v1/analytics/regime/{symbol}`
- [ ] Integrate with `GetHistoricalUseCase` to fetch data for analysis

### 4. Agent Context Enhancement
- [ ] Modify `ChatRequest` to include `market_regime` context
- [ ] Update `orchestrator.py` to inject regime info into the AI prompt

## Technical Details

### Features for HMM
We will use Gaussian distributions for emissions.
Observation vector $O_t$:
1. **Daily Log Return**: $r_t = \ln(P_t / P_{t-1})$
2. **Range Volatility**: $(High_t - Low_t) / Close_t$
3. **Volume Change**: $\ln(V_t / V_{t-1})$

### State Interpretation
After training, we analyze the means/variances of each hidden state to label them:
- **Bullish**: Positive mean return, low variance.
- **Bearish**: Negative mean return, high variance.
- **Choppy/Neutral**: Near-zero mean return, medium variance.
