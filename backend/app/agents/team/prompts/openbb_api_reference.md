## 🌌 GRAVITY ASSET MANAGER U · OPENBB VERIFIED COMMANDS
You have access to the following HIGH-LEVEL commands. These are verified aliases and specialized models for the Gravity Platform. 
**NEVER use raw OpenBB Platform SDK paths unless explicitly listed below.**

### 1. PORTFOLIO & TRADING (Active Management)
- `portfolio liquidate [--all | --symbol TICKER | --losers]` (Exit positions)
- `portfolio pie` (Allocation Chart)
- `portfolio risk` (Sector Exposure)
- `portfolio performance` (PnL by Ticker)
- `portfolio equity` (Equity Curve)
- `portfolio 3d` (Quant Risk/Return Landscape)
- `positions` (List current holdings)
- `buy --symbol TICKER --shares N [--sl PRICE --tp PRICE]`
- `sell --symbol TICKER --shares N`
- `modify --symbol TICKER --sl PRICE --tp PRICE`

### 2. QUANTITATIVE 3D MODELS (Advanced Math)
- `models options surface --symbol TICKER` (3D IV Surface)
- `models yield surface` (3D US Treasury Evolution)
- `models pca clusters --symbols A,B,C` (3D Factor Loadings)
- `models blackscholes --symbol TICKER [--rf RATE]` (Pricing & Greeks)
- `models ratio --symbol1 T1 --symbol2 T2` (Relative Strength)
- `ratio T1 T2 --chart true` (Shortcut for comparison)

### 3. MACHINE LEARNING & AI
- `ml hmm --symbol TICKER` (3D Market Regime Detection)
- `ml montecarlo --symbol TICKER [--days N]` (Price Simulation)
- `ml clusters --symbols A,B,C` (Unsupervised 3D Clustering)
- `ml bootstrap --symbol TICKER` (Resampling analysis)
- `ml intraday --symbol TICKER` (1m Anomaly Detection)
- `hmm TICKER` / `mc TICKER` (Shortcuts)

### 4. CORE MARKET DATA (Fast Access)
- `quote --symbol TICKER` (Live price)
- `historical --symbol TICKER [--limit N]` (History)
- `profile --symbol TICKER` (Company info)
- `search --query "NAME"` (Find ticker)
- `assets --query "SECTOR"` (Global search)
- `news --limit N` (Market news)
- `active` / `gainers` / `losers` (Market snapshots)

### 5. FUNDAMENTALS & MACRO
- `income TICKER` / `balance TICKER` / `cash TICKER` (Financials)
- `earnings TICKER` / `dividends TICKER` / `estimates TICKER`
- `insiders TICKER` / `institutional TICKER` / `short TICKER`
- `calendar` / `cpi` / `gdp` / `unemployment` / `fedfunds`
- `treasury` / `yieldcurve` / `options TICKER`

### 6. TECHNICAL INDICATORS (Requires --chart true)
- `technical rsi --symbol TICKER --chart true`
- `technical macd --symbol TICKER --chart true`
- `technical bbands --symbol TICKER --chart true`
- `technical ema --symbol TICKER --chart true`
- `technical sma --symbol TICKER --chart true`
- `technical relative_rotation --symbol A,B,C --benchmark ^GSPC --chart true`

### ⚠️ IMPORTANT RULES:
1. **Always use --chart true** for visualization.
2. **Positional Args**: Commands like `income AAPL` or `buy AAPL 10` are supported for speed.
3. **If a command fails**, check `terminal_help.md` for exact syntax.
