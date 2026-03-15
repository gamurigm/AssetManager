╔════════════════════════════════════════════════════════════════════════════════════╗
║                      🌌 GRAVITY ASSET MANAGER U · OPENBB PLATFORM                  ║
║                            ADVANCED CLI TERMINAL v3.0.0                            ║
╚════════════════════════════════════════════════════════════════════════════════════╝

  SYNTAX:  command --flag value --flag2 value2
           Add  --chart true  to any ★ command to open an interactive Plotly chart.

━━━━━━━━━━━━━━━━━━━━━━━━━━ 💼 PORTFOLIO EXECUTION (DANGER)  ━━━━━━━━━━━━━━━━━━━━━━
  portfolio liquidate --all              | Sells entirety of the portfolio at market price.
  portfolio liquidate --symbol AAPL      | Liquidates a specific holding.
  portfolio liquidate --losers           | Sells only positions with negative PnL.
  portfolio pie                          | View current allocation pie chart (interactive).
  portfolio risk                         | View sector exposure risk (interactive).
  portfolio performance                  | View PnL performance per ticker (interactive).
  portfolio equity                       | View historical equity curve vs realized balance.
  portfolio 3d                           | View quantitative 3D risk vs return landscape.
  portfolio distribution                   | View statistical histogram of PnL returns.

━━━━━━━━━━━━━━━━━━━━━━━━━━ 🧮 QUANTITATIVE 3D MODELS (Math)       ━━━━━━━━━━━━━━━━━━━━━━
  models options surface                  | 3D Implied Volatility Surface (Strike/DTE/IV).
  models yield surface                    | 3D US Treasury Yield Curve Evolution.
  models pca clusters --symbols A,B,C...  | 3D PCA Factor Loadings Eigenspace.
  models blackscholes --symbol AAPL       | Black-Scholes Options Pricing & 3D Greeks.
  models ratio --symbol1 QQQ --symbol2 SPY| Relative Strength & Z-Score Pair Trading.

━━━━━━━━━━━━━━━━━━━━━━━━━━ 🧠 MACHINE LEARNING (AI-Powered)         ━━━━━━━━━━━━━━━━━━━━━━
  ml hmm --symbol SPY                    | HMM 3D Regime Detection (Bull/Bear/Neutral).
  ml montecarlo --symbol AAPL             | Monte Carlo GBM Price Simulation (Fan Chart).
  ml montecarlo --symbol TSLA --days 90   | Custom horizon simulation.
  ml clusters --symbols A,B,C...          | K-Means Unsupervised Asset Clustering (3D).
  ml bootstrap --symbol AAPL              | Block Bootstrap Resampling (multi-panel).
  ml intraday --symbol NVDA               | Real-Time 1m VWAP & Isolation Forest Anomalies.

━━━━━━━━━━━━━━━━━━━━━━━━━━ 💹 TRADING & EXECUTION (Live)           ━━━━━━━━━━━━━━━━━━━━━━
  buy --symbol AAPL --shares 10          | Market Buy.
  buy --symbol NVDA --usd 5000           | Buy $5,000 worth of NVIDIA.
  sell --symbol AAPL --shares 5          | Market Sell.
  buy --symbol BTC --shares 0.5 --price 60k | Limit Buy (simulated).
  modify --symbol AAPL --sl 150 --tp 200 | Set Stop-Loss and Take-Profit.
  positions                              | List current open positions with SL/TP status.

━━━━━━━━━━━━━━━━━━━━━━━━━━ 🔍 MARKET DISCOVERY                   ━━━━━━━━━━━━━━━━━━━━━━
  active         Most active stocks           | active
  gainers        Top market gainers           | gainers
  losers         Top market losers            | losers
  etf_holdings   List ETF components          | etf_holdings SPY
  index_members  List Index constituents      | index_members ^NDX

━━━━━━━━━━━━━━━━━━━━━━━━━━ 📊 CORE MARKET DATA (Lightning Fast) ━━━━━━━━━━━━━━━━━━━━━━
  quote          Real-time price quote        | quote --symbol AAPL
  historical     Price history candles        | historical --symbol TSLA --limit 50
  profile        Company overview             | profile --symbol MSFT
  search         Find ticker by name          | search --query "nvidia"
  assets         Browse/search global tickers | assets --query tech --limit 50
  news           Latest market news           | news --limit 10

━━━━━━━━━━━━━━━━━━━━━━━━━━ 🏦 FUNDAMENTALS & ECONOMY            ━━━━━━━━━━━━━━━━━━━━━━
  income         Income statement             | income AAPL
  balance        Balance sheet                | balance AMZN
  cash           Cash flow statement          | cash MSFT
  earnings       Earnings calendar            | earnings TSLA
  dividends      Dividend history             | dividends KO
  estimates      Analyst price targets        | estimates NVDA
  insiders       Insider trading activity     | insiders AAPL
  institutional  Institutional ownership      | institutional MSFT
  short          Short interest data          | short TSLA
  calendar       Economic calendar            | calendar
  cpi            Consumer Price Index         | cpi
  gdp            Nominal GDP                  | gdp
  unemployment   Unemployment Rate            | unemployment
  fedfunds       Fed Funds Rate               | fedfunds
  treasury       Government Treasury Rates    | treasury
  yieldcurve     Yield Curve Data             | yieldcurve
  options        Options chains               | options SPY

━━━━━━━━━━━━━━━━━━━━━━━━━━ 📈 CHARTS  (abren en ventana nativa) ━━━━━━━━━━━━━━━━━━━━━━
  Añade --chart true a cualquier comando ★ para abrir gráfico interactivo Plotly.

  ★ EQUITY
    equity price historical --symbol AAPL --chart true
    equity price historical --symbol MSFT --start_date 2024-01-01 --chart true
    equity price performance --symbol NVDA --chart true
    equity historical_market_cap --symbol TSLA --chart true

  ★ CRYPTO
    crypto price historical --symbol BTC-USD --chart true
    crypto price historical --symbol ETH-USD --start_date 2024-01-01 --chart true

  ★ CURRENCY / FOREX
    currency price historical --symbol EURUSD=X --chart true
    currency price historical --symbol GBPUSD=X --chart true

  ★ ETF
    etf historical --symbol SPY --chart true
    etf holdings --symbol QQQ --chart true
    etf price_performance --symbol IWM --chart true

  ★ DERIVATIVES
    derivatives futures curve --symbol CL --chart true
    derivatives futures historical --symbol CL --chart true
    derivatives options surface --symbol SPY --chart true

  ★ FIXED INCOME
    fixedincome government yield_curve --chart true
    fixedincome government yield_curve --date 2024-01-01 --chart true

  ★ INDEX
    index price historical --symbol ^GSPC --chart true
    index price historical --symbol ^NDX --chart true

  ★ ECONOMY / MACRO
    economy fred_series --symbol GDP --chart true
    economy fred_series --symbol CPIAUCSL --chart true
    economy fred_series --symbol FEDFUNDS --chart true
    economy shipping chokepoint_info --chart true
    economy shipping port_info --chart true
    economy survey bls_series --symbol CES0000000001 --chart true

  ★ TECHNICAL INDICATORS  (requieren datos previos cargados)
    technical macd --symbol AAPL --chart true
    technical rsi --symbol AAPL --chart true
    technical ema --symbol AAPL --length 50 --chart true
    technical sma --symbol AAPL --length 200 --chart true
    technical wma --symbol AAPL --chart true
    technical hma --symbol AAPL --chart true
    technical zlma --symbol AAPL --chart true
    technical adx --symbol AAPL --chart true
    technical aroon --symbol AAPL --chart true
    technical cones --symbol AAPL --chart true
    technical relative_rotation --symbol AAPL --benchmark ^GSPC --chart true

  ★ ECONOMETRICS
    econometrics correlation_matrix --symbol AAPL,MSFT,NVDA --chart true

━━━━━━━━━━━━━━━━━━━━━━━━━━ 🤖 AI AUTOPILOT                      ━━━━━━━━━━━━━━━━━━━━━━
  /qwen, q       Delega ejecución natural a la IA Qwen 3.5.
                 q liquida tesla
                 q vende todas mis posiciones en rojo
                 /qwen What command shows bond yields?

  ★ QUICK ANALYTICS (Shortcuts)
    ratio AAPL MSFT --chart true          | Compare relative strength.
    bs AAPL                               | Black-Scholes Dashboard.
    hmm SPY                               | Market Regime Detection.
    mc TSLA --days 90                     | Monte Carlo Simulation.
    buy AAPL 10                           | Quick Buy (Positional Args).
    sell TSLA 5                           | Quick Sell (Positional Args).

  ★ QUICK KEYS
  ↑ / ↓          Navigate history
  Tab            Autocomplete
  Enter          Execute
  ctrl+l         Clear terminal
  esc            Close terminal
