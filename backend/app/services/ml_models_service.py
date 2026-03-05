"""
Machine Learning Financial Models Service
==========================================
Provides ML-powered visualizations for market analysis:

  1. HMM Regime Detection — 3D visualization of Hidden Markov Model states
  2. Monte Carlo Price Simulation — Fan chart of probabilistic future paths
  3. K-Means Asset Clustering — Unsupervised grouping by risk/return profile
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from typing import List, Dict, Any
from datetime import datetime, timedelta


_DARK_LAYOUT = dict(
    template='plotly_dark',
    paper_bgcolor='#0a0a0a',
    plot_bgcolor='#0a0a0a',
    font=dict(family="Inter, system-ui, sans-serif", size=11, color="#94a3b8"),
)

_EMPTY = "<div style='color:#94a3b8; text-align:center; padding:40px; font-family:Inter,sans-serif;'>📊 Datos insuficientes para este modelo ML.</div>"


class MLModelsService:
    """Machine Learning models integrated with Plotly for interactive 3D market analysis."""

    def __init__(self):
        pass

    # ══════════════════════════════════════════════════════════════════════════
    # 1 ─ HMM REGIME DETECTION (3D Visualization)
    # ══════════════════════════════════════════════════════════════════════════
    async def get_hmm_regimes(self, symbol: str = "SPY") -> str:
        """
        Fits a 3-state Gaussian Hidden Markov Model on OHLCV data to detect
        Bull, Bear, and Neutral regimes. Visualizes in 3D:
        X = Log Returns, Y = Range Volatility, Z = Volume Change
        Color = Detected Regime
        """
        try:
            import yfinance as yf
            from hmmlearn.hmm import GaussianHMM

            tk = yf.Ticker(symbol)
            hist = tk.history(period="2y")
            if hist.empty or len(hist) < 60:
                return _EMPTY

            df = hist.copy()
            df.columns = [c.lower() for c in df.columns]

            # Feature engineering
            df['log_ret'] = np.log(df['close'] / df['close'].shift(1))
            df['range_vol'] = (df['high'] - df['low']) / df['close']
            df['log_vol_change'] = np.log((df['volume'] + 1) / (df['volume'].shift(1) + 1))
            df = df.dropna()

            X = df[['log_ret', 'range_vol', 'log_vol_change']].values

            # Fit HMM
            model = GaussianHMM(n_components=3, covariance_type="full", n_iter=200, random_state=42)
            model.fit(X)
            states = model.predict(X)

            # Interpret states by mean return
            state_means = {}
            for s in range(3):
                mask = states == s
                if mask.any():
                    state_means[s] = X[mask, 0].mean()

            sorted_states = sorted(state_means.items(), key=lambda x: x[1])
            labels = {}
            labels[sorted_states[0][0]] = "🐻 Bearish"
            labels[sorted_states[-1][0]] = "🐂 Bullish"
            remaining = set(range(3)) - {sorted_states[0][0], sorted_states[-1][0]}
            labels[list(remaining)[0]] = "⚡ Neutral"

            df = df.iloc[:len(states)].copy()
            df['regime'] = [labels[s] for s in states]
            df['state'] = states

            # Get probabilities
            probs = model.predict_proba(X)
            df['confidence'] = [probs[i, states[i]] for i in range(len(states))]

            # Current regime info
            current = labels[states[-1]]
            current_conf = probs[-1, states[-1]] * 100

            fig = px.scatter_3d(
                df.reset_index(),
                x='log_ret',
                y='range_vol',
                z='log_vol_change',
                color='regime',
                color_discrete_map={
                    "🐂 Bullish": "#10b981",
                    "🐻 Bearish": "#ef4444",
                    "⚡ Neutral": "#f59e0b"
                },
                size='confidence',
                size_max=12,
                opacity=0.7,
                hover_data={'log_ret': ':.4f', 'range_vol': ':.4f', 'log_vol_change': ':.4f', 'confidence': ':.2f'},
                title='',
            )

            fig.update_layout(
                **_DARK_LAYOUT,
                title=dict(
                    text=f'🧠 HMM REGIME DETECTION — {symbol.upper()} | Current: {current} ({current_conf:.0f}% conf.)',
                    x=0.5, font=dict(size=17, color="#f8fafc", family="Inter")
                ),
                scene=dict(
                    xaxis_title='Log Returns',
                    yaxis_title='Range Volatility',
                    zaxis_title='Volume Change',
                    xaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    yaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    zaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    camera=dict(eye=dict(x=1.5, y=-1.5, z=1.0)),
                ),
                margin=dict(t=80, b=10, l=10, r=10),
            )

            # Regime counts
            bull_pct = (df['regime'] == '🐂 Bullish').sum() / len(df) * 100
            bear_pct = (df['regime'] == '🐻 Bearish').sum() / len(df) * 100
            neutral_pct = 100 - bull_pct - bear_pct

            # Regime insights
            recent_vol = df['range_vol']. tail(10).mean() * 100
            
            summary = (
                f"<b>🧠 ANÁLISIS HMM (Markov Regime Detection)</b><br><br>"
                f"<b>Régimen Detectado:</b> {current} ({current_conf:.1f}% probabilidad posterior)<br>"
                f"<b>Distribución Histórica (2Y):</b> 🐂 Bullish: {bull_pct:.0f}%  |  ⚡ Neutral: {neutral_pct:.0f}%  |  🐻 Bearish: {bear_pct:.0f}%<br><br>"
                f"<b>💡 Interpretación Cuantitativa:</b><br>"
                f"• El modelo oculto de Markov ha segmentado el historial en 3 estados latentes<br>"
                f"  basados en la covarianza de retornos logarítmicos, volatilidad y volumen.<br>"
                f"• En regímenes <b>🐂 Bullish</b>, las estrategias de seguimiento de tendencia (Trend Following) y Buy & Hold tienen Alpha positivo.<br>"
                f"• En regímenes <b>🐻 Bearish</b>, se observa fat-tail risk (riesgo de cola). Prioriza preservación de capital y cobertura (Hedging).<br>"
                f"• En regímenes <b>⚡ Neutrales/Choppy</b>, los retornos divergen hacia reversión a la media (Mean Reversion).<br>"
                f"• Volatilidad de rango reciente: {recent_vol:.2f}% por día."
            )
            fig.add_annotation(
                text=summary, x=0.01, y=0.99, xref='paper', yref='paper',
                showarrow=False, align='left', font=dict(size=11, color='#cbd5e1', family='Inter'),
                bgcolor='rgba(15,23,42,0.85)', bordercolor='rgba(99,102,241,0.5)',
                borderwidth=1, borderpad=10,
            )

            return fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True, 'scrollZoom': True})

        except Exception as e:
            return f"<div style='color:#ef4444; text-align:center; padding:40px;'>HMM Error: {e}</div>"

    # ══════════════════════════════════════════════════════════════════════════
    # 2 ─ MONTE CARLO PRICE SIMULATION
    # ══════════════════════════════════════════════════════════════════════════
    async def get_monte_carlo(self, symbol: str = "SPY", days: int = 60, sims: int = 500) -> str:
        """
        Geometric Brownian Motion Monte Carlo simulation.
        Uses historical μ (drift) and σ (volatility) to project future price paths.
        Displays fan chart with percentile bands (5th, 25th, 50th, 75th, 95th).
        """
        try:
            import yfinance as yf

            tk = yf.Ticker(symbol)
            hist = tk.history(period="1y")
            if hist.empty or len(hist) < 30:
                return _EMPTY

            closes = hist['Close'].values
            log_returns = np.log(closes[1:] / closes[:-1])

            mu = log_returns.mean()  # daily drift
            sigma = log_returns.std()  # daily volatility
            last_price = closes[-1]
            last_date = hist.index[-1]

            # Generate simulations using Geometric Brownian Motion (GBM)
            dt = 1  # 1 trading day
            np.random.seed(42)
            simulations = np.zeros((sims, days))

            for i in range(sims):
                prices = [last_price]
                for d in range(days):
                    shock = np.random.normal(mu * dt, sigma * np.sqrt(dt))
                    prices.append(prices[-1] * np.exp(shock))
                simulations[i] = prices[1:]

            # Calculate percentile bands
            p5 = np.percentile(simulations, 5, axis=0)
            p25 = np.percentile(simulations, 25, axis=0)
            p50 = np.percentile(simulations, 50, axis=0)
            p75 = np.percentile(simulations, 75, axis=0)
            p95 = np.percentile(simulations, 95, axis=0)

            # Future dates
            future_dates = pd.bdate_range(start=last_date + timedelta(days=1), periods=days)

            # Historical prices (last 90 days for context)
            hist_tail = hist.tail(90)

            fig = go.Figure()

            # Historical
            fig.add_trace(go.Scatter(
                x=hist_tail.index, y=hist_tail['Close'],
                mode='lines', name='Historical',
                line=dict(color='#e2e8f0', width=2)
            ))

            # Fan chart bands
            fig.add_trace(go.Scatter(
                x=list(future_dates) + list(future_dates[::-1]),
                y=list(p95) + list(p5[::-1]),
                fill='toself', fillcolor='rgba(99, 102, 241, 0.08)',
                line=dict(color='rgba(0,0,0,0)'),
                name='5th-95th Percentile', hoverinfo='skip'
            ))
            fig.add_trace(go.Scatter(
                x=list(future_dates) + list(future_dates[::-1]),
                y=list(p75) + list(p25[::-1]),
                fill='toself', fillcolor='rgba(99, 102, 241, 0.18)',
                line=dict(color='rgba(0,0,0,0)'),
                name='25th-75th Percentile', hoverinfo='skip'
            ))

            # Median path
            fig.add_trace(go.Scatter(
                x=future_dates, y=p50,
                mode='lines', name='Median (50th)',
                line=dict(color='#6366f1', width=3, dash='dot')
            ))

            # Sample paths (first 30 for texture)
            for i in range(min(30, sims)):
                fig.add_trace(go.Scatter(
                    x=future_dates, y=simulations[i],
                    mode='lines', line=dict(color='rgba(99,102,241,0.1)', width=0.5),
                    showlegend=False, hoverinfo='skip'
                ))

            # Percentile lines
            fig.add_trace(go.Scatter(x=future_dates, y=p95, mode='lines', name='95th %', line=dict(color='#ef4444', width=1, dash='dash')))
            fig.add_trace(go.Scatter(x=future_dates, y=p5, mode='lines', name='5th %', line=dict(color='#10b981', width=1, dash='dash')))

            # Expected return annotation
            expected_return = ((p50[-1] / last_price) - 1) * 100
            p95_ret = ((p95[-1] / last_price) - 1) * 100
            p5_ret = ((p5[-1] / last_price) - 1) * 100
            ann_vol = sigma * np.sqrt(252) * 100

            fig.update_layout(
                **_DARK_LAYOUT,
                title=dict(
                    text=f'🎲 MONTE CARLO GBM — {symbol.upper()} | {sims} Simulations × {days} Days | E[R] = {expected_return:+.1f}%',
                    x=0.5, font=dict(size=16, color="#f8fafc", family="Inter")
                ),
                xaxis_title='Date',
                yaxis_title='Price ($)',
                hovermode='x unified',
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                margin=dict(t=80, b=80, l=60, r=40),
                xaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
                yaxis=dict(gridcolor='rgba(255,255,255,0.05)', side='right'),
            )

            prob_profit_mc = (p50[-1] > last_price) * 100 if p50[-1] else 50.0  # approximate
            
            summary = (
                f"<b>🎲 PROYECCIÓN MONTE CARLO (Movimiento Browniano Geométrico)</b><br><br>"
                f"<b>Parámetros:</b> Drift (μ) diario histórico = {mu*100:.3f}%  |  Volatilidad diaria (σ) = {sigma*100:.3f}% (Anualizada: {ann_vol:.1f}%)<br>"
                f"<b>Fronteras {days} días:</b> Precio Mín 5% = ${p5[-1]:,.2f} ({p5_ret:+.1f}%)  |  Precio Máx 95% = ${p95[-1]:,.2f} ({p95_ret:+.1f}%)<br>"
                f"<b>Escenario Central (Mediana):</b> ${p50[-1]:,.2f} (Retorno Esperado E[R]: {expected_return:+.2f}%)<br><br>"
                f"<b>💡 Interpretación Cuantitativa:</b><br>"
                f"• Este abanico probabilístico simula {sims} universos usando el modelo subyacente de Black-Scholes.<br>"
                f"• La amplitud entre el percentil 5° y 95° representa el Rango Gáussico de Riesgo. A mayor amplitud, mayor prima de riesgo asumes.<br>"
                f"• ⚠️ <i>Nota:</i> GBM asume distribución normal de retornos y volatilidad constante. No captura 'Cisnes Negros' (fat tails).<br>"
                f"• Estrategia: Útil para trazar strikes de opciones (Iron Condors, Covered Calls) fuera de las bandas del 10% y 90%."
            )
            fig.add_annotation(
                text=summary, x=0.5, y=-0.20, xref='paper', yref='paper',
                showarrow=False, align='left', font=dict(size=11, color='#cbd5e1', family='Inter'),
                bgcolor='rgba(15,23,42,0.9)', bordercolor='rgba(99,102,241,0.5)',
                borderwidth=1, borderpad=10,
            )

            return fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True})

        except Exception as e:
            return f"<div style='color:#ef4444; text-align:center; padding:40px;'>Monte Carlo Error: {e}</div>"

    # ══════════════════════════════════════════════════════════════════════════
    # 3 ─ K-MEANS ASSET CLUSTERING
    # ══════════════════════════════════════════════════════════════════════════
    async def get_kmeans_clusters(self, symbols_str: str = "AAPL,MSFT,NVDA,TSLA,META,AMZN,GOOGL,JPM,V,JNJ,XOM,PFE,KO,DIS,NFLX", n_clusters: int = 4) -> str:
        """
        K-Means clustering of assets by their quantitative risk/return profile:
        - Annualized Return
        - Annualized Volatility
        - Sharpe Ratio
        Projects in 3D space with cluster coloring.
        """
        try:
            import yfinance as yf
            from sklearn.cluster import KMeans
            from sklearn.preprocessing import StandardScaler

            symbols = [s.strip().upper() for s in symbols_str.split(',') if s.strip()]
            if len(symbols) < 4:
                return "<div style='color:#ef4444; text-align:center; padding:40px;'>Se necesitan al menos 4 símbolos para clustering.</div>"

            end_date = datetime.now()
            start_date = end_date - timedelta(days=365)

            price_data = yf.download(
                symbols,
                start=start_date.strftime('%Y-%m-%d'),
                end=end_date.strftime('%Y-%m-%d'),
                progress=False
            )

            if price_data.empty:
                return _EMPTY

            if 'Close' in price_data.columns.get_level_values(0):
                closes = price_data['Close']
            else:
                closes = price_data

            if isinstance(closes, pd.Series):
                return _EMPTY

            closes = closes.dropna(axis=1, thresh=int(len(closes) * 0.7))
            if closes.shape[1] < 4:
                return "<div style='color:#ef4444;'>No hay suficientes datos para clustering.</div>"

            returns = closes.pct_change().dropna()

            # Compute metrics per asset
            metrics = []
            for col in returns.columns:
                ann_ret = returns[col].mean() * 252 * 100
                ann_vol = returns[col].std() * np.sqrt(252) * 100
                sharpe = (ann_ret / ann_vol) if ann_vol > 0 else 0
                max_dd = ((closes[col] / closes[col].cummax()) - 1).min() * 100
                skew = returns[col].skew()
                metrics.append({
                    'symbol': col,
                    'ann_return': ann_ret,
                    'ann_volatility': ann_vol,
                    'sharpe': sharpe,
                    'max_drawdown': max_dd,
                    'skewness': skew,
                })

            df = pd.DataFrame(metrics)

            # K-Means clustering on standardized features
            features = df[['ann_return', 'ann_volatility', 'sharpe']].values
            scaler = StandardScaler()
            features_scaled = scaler.fit_transform(features)

            actual_k = min(n_clusters, len(df))
            kmeans = KMeans(n_clusters=actual_k, random_state=42, n_init=10)
            df['cluster'] = kmeans.fit_predict(features_scaled)

            # Label clusters by mean return
            cluster_labels = {}
            cluster_colors = ['#6366f1', '#10b981', '#f59e0b', '#ef4444', '#ec4899', '#06b6d4']
            for c in range(actual_k):
                mask = df['cluster'] == c
                mean_ret = df.loc[mask, 'ann_return'].mean()
                mean_vol = df.loc[mask, 'ann_volatility'].mean()
                if mean_ret > 15:
                    label = "🚀 High Growth"
                elif mean_ret > 0:
                    label = "📈 Steady"
                elif mean_vol > 30:
                    label = "⚡ High Risk"
                else:
                    label = "🛡️ Defensive"
                cluster_labels[c] = label

            df['cluster_label'] = df['cluster'].map(cluster_labels)

            fig = px.scatter_3d(
                df,
                x='ann_return',
                y='ann_volatility',
                z='sharpe',
                color='cluster_label',
                color_discrete_sequence=cluster_colors[:actual_k],
                size=df['ann_volatility'].abs(),
                size_max=35,
                hover_name='symbol',
                hover_data={
                    'ann_return': ':.1f',
                    'ann_volatility': ':.1f',
                    'sharpe': ':.2f',
                    'max_drawdown': ':.1f',
                    'skewness': ':.2f',
                    'cluster_label': False,
                },
                text='symbol',
                title='',
            )

            fig.update_traces(
                textposition='top center',
                textfont=dict(size=10, color='#f8fafc', family='Inter'),
                marker=dict(line=dict(width=1, color='rgba(255,255,255,0.2)'))
            )

            fig.update_layout(
                **_DARK_LAYOUT,
                title=dict(
                    text=f'🤖 K-MEANS CLUSTERING — {len(df)} Assets × {actual_k} Clusters (Unsupervised ML)',
                    x=0.5, font=dict(size=17, color="#f8fafc", family="Inter")
                ),
                scene=dict(
                    xaxis_title='Annualized Return (%)',
                    yaxis_title='Annualized Volatility (%)',
                    zaxis_title='Sharpe Ratio',
                    xaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    yaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    zaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    camera=dict(eye=dict(x=1.5, y=-1.5, z=1.0)),
                ),
                margin=dict(t=80, b=10, l=10, r=10),
            )

            # Build summary of clusters
            cluster_summary_parts = []
            for c in range(actual_k):
                mask = df['cluster'] == c
                syms = ', '.join(df.loc[mask, 'symbol'].tolist())
                label = cluster_labels[c]
                avg_ret = df.loc[mask, 'ann_return'].mean()
                cluster_summary_parts.append(f"{label}: [{syms}] (Ret:{avg_ret:+.0f}%)")

            best_sym = df.loc[df['sharpe'].idxmax()]
            worst_dd = df.loc[df['max_drawdown'].idxmin()]
            
            summary = (
                f"<b>🤖 CLUSTERING K-MEANS NO SUPERVISADO</b><br><br>"
                f"<b>Métricas Destacadas:</b><br>"
                f"• Asset más eficiente (Mejor Sharpe): <b>{best_sym['symbol']}</b> ({best_sym['sharpe']:.2f})<br>"
                f"• Mayor riesgo de ruina (Max Drawdown histórico): <b>{worst_dd['symbol']}</b> ({worst_dd['max_drawdown']:.1f}%)<br><br>"
                f"<b>Agrupaciones Descubiertas:</b><br>"
                + "<br>".join(f"• {p}" for p in cluster_summary_parts) + 
                f"<br><br><b>💡 Interpretación Cuantitativa:</b><br>"
                f"• El algoritmo agrupó geométricamente los activos en la intersección de Retorno, Volatilidad y Ratio Sharpe.<br>"
                f"• Activos en el mismo cluster comparten vectores de exposición sistemática y <b>NO proporcionan diversificación ortogonal</b>.<br>"
                f"• Para construir un portafolio robusto protegido contra choques macro, selecciona activos semilla de <b>diferentes clusters</b> separados espacialmente."
            )
            fig.add_annotation(
                text=summary, x=0.01, y=0.99, xref='paper', yref='paper',
                showarrow=False, align='left', font=dict(size=10, color='#cbd5e1', family='Inter'),
                bgcolor='rgba(15,23,42,0.85)', bordercolor='rgba(99,102,241,0.5)',
                borderwidth=1, borderpad=10,
            )

            return fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True, 'scrollZoom': True})

        except Exception as e:
            return f"<div style='color:#ef4444; text-align:center; padding:40px;'>K-Means Error: {e}</div>"

    # ══════════════════════════════════════════════════════════════════════════
    # 4 ─ BOOTSTRAP RESAMPLING (Configurable)
    # ══════════════════════════════════════════════════════════════════════════
    async def get_bootstrap(
        self,
        symbol: str = "SPY",
        n_resamples: int = 1000,
        block_size: int = 5,
        horizon: int = 60,
        confidence: float = 95.0
    ) -> str:
        """
        Stationary Block Bootstrap Resampling for return distribution analysis.

        Instead of assuming a parametric distribution (like Monte Carlo GBM),
        Bootstrap directly resamples from the REAL historical return data to
        build empirical confidence intervals. Block bootstrap preserves
        autocorrelation structure in returns.

        Parameters:
          - n_resamples: Number of bootstrap samples (default 1000)
          - block_size:  Size of contiguous blocks to resample (default 5 days)
          - horizon:     Forward projection in trading days (default 60)
          - confidence:  Confidence level for intervals (default 95%)

        Output: Multi-panel chart with:
          1. Bootstrapped cumulative return fan chart
          2. Return distribution histogram with VaR/CVaR markers
          3. Statistical summary table
        """
        try:
            import yfinance as yf
            from plotly.subplots import make_subplots

            tk = yf.Ticker(symbol)
            hist = tk.history(period="2y")
            if hist.empty or len(hist) < 60:
                return _EMPTY

            closes = hist['Close'].values
            daily_returns = np.diff(np.log(closes))  # log returns

            if len(daily_returns) < block_size * 2:
                return _EMPTY

            # ── Block Bootstrap Resampling ──────────────────────────────
            n_returns = len(daily_returns)
            n_blocks = int(np.ceil(horizon / block_size))
            bootstrap_paths = np.zeros((n_resamples, horizon))

            np.random.seed(None)  # True randomness each run
            for i in range(n_resamples):
                sampled_returns = []
                for _ in range(n_blocks):
                    # Pick a random starting point for a block
                    start = np.random.randint(0, n_returns - block_size)
                    sampled_returns.extend(daily_returns[start:start + block_size])
                # Trim to exact horizon length
                sampled_returns = sampled_returns[:horizon]
                # Cumulative return path
                bootstrap_paths[i] = np.cumsum(sampled_returns)

            # Convert log cumulative returns to price levels
            last_price = closes[-1]
            price_paths = last_price * np.exp(bootstrap_paths)

            # ── Terminal return distribution ────────────────────────────
            terminal_returns = bootstrap_paths[:, -1] * 100  # percentage

            # Percentile calculations
            alpha = (100 - confidence) / 2
            p_low = np.percentile(price_paths, alpha, axis=0)
            p_mid = np.percentile(price_paths, 50, axis=0)
            p_high = np.percentile(price_paths, 100 - alpha, axis=0)
            p25 = np.percentile(price_paths, 25, axis=0)
            p75 = np.percentile(price_paths, 75, axis=0)

            # VaR & CVaR
            var_pct = np.percentile(terminal_returns, alpha)
            cvar_pct = terminal_returns[terminal_returns <= var_pct].mean() if (terminal_returns <= var_pct).any() else var_pct
            var_dollar = last_price * (np.exp(var_pct / 100) - 1)

            # Stats
            mean_ret = terminal_returns.mean()
            median_ret = np.median(terminal_returns)
            std_ret = terminal_returns.std()
            prob_profit = (terminal_returns > 0).sum() / n_resamples * 100
            best_case = terminal_returns.max()
            worst_case = terminal_returns.min()

            # ── Build multi-panel figure ───────────────────────────────
            last_date = hist.index[-1]
            future_dates = pd.bdate_range(start=last_date + timedelta(days=1), periods=horizon)
            hist_tail = hist.tail(60)

            fig = make_subplots(
                rows=2, cols=2,
                subplot_titles=[
                    f'Bootstrap Price Paths ({confidence:.0f}% CI)',
                    'Terminal Return Distribution',
                    'Cumulative Return Over Time',
                    'Block Bootstrap Statistics'
                ],
                specs=[
                    [{"type": "scatter"}, {"type": "histogram"}],
                    [{"type": "scatter"}, {"type": "table"}]
                ],
                vertical_spacing=0.12,
                horizontal_spacing=0.08,
            )

            # ── Panel 1: Fan Chart ─────────────────────────────────────
            # Historical
            fig.add_trace(go.Scatter(
                x=hist_tail.index, y=hist_tail['Close'],
                mode='lines', name='Historical',
                line=dict(color='#e2e8f0', width=2)
            ), row=1, col=1)

            # CI band
            fig.add_trace(go.Scatter(
                x=list(future_dates) + list(future_dates[::-1]),
                y=list(p_high) + list(p_low[::-1]),
                fill='toself', fillcolor='rgba(99, 102, 241, 0.1)',
                line=dict(color='rgba(0,0,0,0)'),
                name=f'{confidence:.0f}% CI', hoverinfo='skip'
            ), row=1, col=1)

            # IQR band
            fig.add_trace(go.Scatter(
                x=list(future_dates) + list(future_dates[::-1]),
                y=list(p75) + list(p25[::-1]),
                fill='toself', fillcolor='rgba(99, 102, 241, 0.2)',
                line=dict(color='rgba(0,0,0,0)'),
                name='IQR (25-75%)', hoverinfo='skip'
            ), row=1, col=1)

            # Median
            fig.add_trace(go.Scatter(
                x=future_dates, y=p_mid,
                mode='lines', name='Median',
                line=dict(color='#6366f1', width=2.5, dash='dot')
            ), row=1, col=1)

            # Sample paths
            for i in range(min(40, n_resamples)):
                fig.add_trace(go.Scatter(
                    x=future_dates, y=price_paths[i],
                    mode='lines', line=dict(color='rgba(99,102,241,0.06)', width=0.5),
                    showlegend=False, hoverinfo='skip'
                ), row=1, col=1)

            # ── Panel 2: Return Distribution ───────────────────────────
            fig.add_trace(go.Histogram(
                x=terminal_returns,
                nbinsx=50,
                marker_color='#6366f1',
                opacity=0.75,
                name='Returns Dist.',
            ), row=1, col=2)

            # VaR line
            fig.add_vline(x=var_pct, line_width=2, line_dash="dash", line_color="#ef4444", row=1, col=2)
            # Zero line
            fig.add_vline(x=0, line_width=1, line_dash="dot", line_color="#94a3b8", row=1, col=2)
            # Mean line
            fig.add_vline(x=mean_ret, line_width=2, line_dash="solid", line_color="#10b981", row=1, col=2)

            # ── Panel 3: Cumulative Return Percentiles ─────────────────
            cum_returns_median = bootstrap_paths[:, :].mean(axis=0) * 100
            cum_returns_low = np.percentile(bootstrap_paths * 100, alpha, axis=0)
            cum_returns_high = np.percentile(bootstrap_paths * 100, 100 - alpha, axis=0)

            fig.add_trace(go.Scatter(
                x=list(range(1, horizon + 1)),
                y=cum_returns_high,
                mode='lines', name=f'Upper {100-alpha:.0f}%',
                line=dict(color='#10b981', width=1, dash='dash')
            ), row=2, col=1)

            fig.add_trace(go.Scatter(
                x=list(range(1, horizon + 1)),
                y=cum_returns_low,
                mode='lines', name=f'Lower {alpha:.0f}%',
                line=dict(color='#ef4444', width=1, dash='dash'),
                fill='tonexty', fillcolor='rgba(99,102,241,0.08)'
            ), row=2, col=1)

            fig.add_trace(go.Scatter(
                x=list(range(1, horizon + 1)),
                y=cum_returns_median,
                mode='lines', name='Mean Path',
                line=dict(color='#f8fafc', width=2)
            ), row=2, col=1)

            # Zero line for cumulative
            fig.add_hline(y=0, line_width=1, line_dash="dot", line_color="#94a3b8", row=2, col=1)

            # ── Panel 4: Statistics Table ──────────────────────────────
            fig.add_trace(go.Table(
                header=dict(
                    values=['<b>Metric</b>', '<b>Value</b>'],
                    fill_color='#1e293b',
                    font=dict(color='#f8fafc', size=12, family='Inter'),
                    align='left', height=30,
                ),
                cells=dict(
                    values=[
                        [
                            'Resamples', 'Block Size', 'Horizon',
                            'Confidence', 'Mean Return', 'Median Return',
                            'Std Dev', f'VaR ({alpha:.1f}%)',
                            f'CVaR ({alpha:.1f}%)', 'VaR ($)',
                            'P(Profit)', 'Best Case', 'Worst Case'
                        ],
                        [
                            f'{n_resamples:,}', f'{block_size} days', f'{horizon} days',
                            f'{confidence:.0f}%', f'{mean_ret:+.2f}%', f'{median_ret:+.2f}%',
                            f'{std_ret:.2f}%', f'{var_pct:+.2f}%',
                            f'{cvar_pct:+.2f}%', f'${var_dollar:+,.2f}',
                            f'{prob_profit:.1f}%', f'{best_case:+.2f}%', f'{worst_case:+.2f}%'
                        ],
                    ],
                    fill_color='#0f172a',
                    font=dict(color='#94a3b8', size=11, family='Inter'),
                    align='left', height=25,
                )
            ), row=2, col=2)

            fig.update_layout(
                **_DARK_LAYOUT,
                title=dict(
                    text=f'🔄 BOOTSTRAP RESAMPLING — {symbol.upper()} | {n_resamples:,} Samples × Block={block_size} × {horizon}d | P(Profit)={prob_profit:.0f}%',
                    x=0.5, font=dict(size=15, color="#f8fafc", family="Inter")
                ),
                height=850,
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.05, xanchor="center", x=0.5, font=dict(size=9)),
                margin=dict(t=80, b=60, l=50, r=40),
            )

            # Axis labels
            fig.update_xaxes(title_text='Date', row=1, col=1, gridcolor='rgba(255,255,255,0.05)')
            fig.update_yaxes(title_text='Price ($)', row=1, col=1, gridcolor='rgba(255,255,255,0.05)')
            fig.update_xaxes(title_text='Terminal Return (%)', row=1, col=2, gridcolor='rgba(255,255,255,0.05)')
            fig.update_yaxes(title_text='Frequency', row=1, col=2, gridcolor='rgba(255,255,255,0.05)')
            fig.update_xaxes(title_text='Day', row=2, col=1, gridcolor='rgba(255,255,255,0.05)')
            fig.update_yaxes(title_text='Cumul. Return (%)', row=2, col=1, gridcolor='rgba(255,255,255,0.05)')

            return fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True})

        except Exception as e:
            return f"<div style='color:#ef4444; text-align:center; padding:40px;'>Bootstrap Error: {e}</div>"

    # ══════════════════════════════════════════════════════════════════════════
    # 5 ─ REAL-TIME INTRADAY ANOMALY DETECTION (ISOLATION FOREST)
    # ══════════════════════════════════════════════════════════════════════════
    async def get_intraday_anomaly(self, symbol: str = "AAPL", contamination: float = 0.02) -> str:
        """
        Fetches 1-minute intraday data, calculates VWAP, Cumulative Volume Delta proxy,
        and uses an Isolation Forest to detect algorithmic sweeping / sudden shocks in real-time.
        """
        try:
            import yfinance as yf
            from sklearn.ensemble import IsolationForest
            from plotly.subplots import make_subplots
            
            # Fetch 1-minute data for the current/last available trading day
            ticker = yf.Ticker(symbol)
            df = ticker.history(period="1d", interval="1m")
            
            if df.empty or len(df) < 30:
                return f"<div style='color:#94a3b8; text-align:center; padding:40px;'>No hay datos intradía suficientes para {symbol.upper()}. Probablemente el mercado está cerrado o no soporta ticks de 1m.</div>"
                
            # Time zone strip for Plotly compatibility
            df.index = df.index.tz_localize(None)

            # 1. Feature Engineering
            df['typical_price'] = (df['High'] + df['Low'] + df['Close']) / 3
            df['pv'] = df['typical_price'] * df['Volume']
            df['vwap'] = df['pv'].cumsum() / df['Volume'].cumsum()
            
            df['ret_1m'] = df['Close'].pct_change()
            df['vol_change'] = df['Volume'].pct_change()
            df['spread'] = df['High'] - df['Low']
            
            # Proxy for Cumulative Volume Delta (CVD)
            # If close > open -> buying pressure, else selling pressure
            df['buy_vol'] = np.where(df['Close'] >= df['Open'], df['Volume'], 0)
            df['sell_vol'] = np.where(df['Close'] < df['Open'], df['Volume'], 0)
            df['delta'] = df['buy_vol'] - df['sell_vol']
            df['cvd'] = df['delta'].cumsum()
            
            df.dropna(inplace=True)
            
            # 2. Unsupervised Anomaly Detection (Isolation Forest)
            # We look for statistical outliers in short-term momentum and volume bursts
            features = df[['ret_1m', 'vol_change', 'spread']].copy()
            # Handle infinite values that can occur when volume goes from 0 to N
            features.replace([np.inf, -np.inf], np.nan, inplace=True)
            features.fillna(0, inplace=True)
            
            iso = IsolationForest(contamination=contamination, random_state=42)
            df['anomaly'] = iso.fit_predict(features)
            # IsolationForest returns -1 for anomalies, 1 for normal
            anomalies = df[df['anomaly'] == -1]

            # 3. Visualization
            fig = make_subplots(
                rows=3, cols=1, 
                shared_xaxes=True, 
                vertical_spacing=0.03,
                row_heights=[0.6, 0.2, 0.2],
                subplot_titles=[f'Real-Time 1m Price (VWAP) & Anomalies ({contamination*100:.1f}%)', 'Cumulative Volume Delta (CVD)', 'Tick Volume']
            )

            # Price & VWAP
            fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Price', line=dict(color='#3b82f6', width=2)), row=1, col=1)
            fig.add_trace(go.Scatter(x=df.index, y=df['vwap'], mode='lines', name='VWAP', line=dict(color='#f59e0b', width=2, dash='dot')), row=1, col=1)
            
            # Highlight Anomalies
            if not anomalies.empty:
                fig.add_trace(go.Scatter(
                    x=anomalies.index, y=anomalies['Close'], mode='markers', name='Anomaly Detected',
                    marker=dict(color='#ef4444', size=10, symbol='x', line=dict(width=2, color='white')),
                    hovertemplate='Time: %{x}<br>Price: %{y}<br>Vol Shock: %{customdata[0]:.0%}<br>Ret 1m: %{customdata[1]:.2%}<extra></extra>',
                    customdata=anomalies[['vol_change', 'ret_1m']]
                ), row=1, col=1)

            # Cumulative Volume Delta
            fig.add_trace(go.Scatter(x=df.index, y=df['cvd'], mode='lines', name='CVD', fill='tozeroy', line=dict(color='#8b5cf6', width=1)), row=2, col=1)

            # Volume Bar
            colors = np.where(df['Close'] >= df['Open'], '#10b981', '#ef4444')
            fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume', marker_color=colors), row=3, col=1)

            fig.update_layout(
                **_DARK_LAYOUT,
                title=dict(
                    text=f'⚡ INTRADAY REAL-TIME & ANOMALY DETECTION — {symbol.upper()} | {df.index[0].strftime("%B %d, %Y")}',
                    x=0.5, font=dict(size=18, color="#f8fafc", family="Inter")
                ),
                height=900, hovermode='x unified', margin=dict(t=80, b=150, l=40, r=40),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )

            # Layout grid updates
            for i in range(1, 4):
                fig.update_yaxes(gridcolor='rgba(255,255,255,0.05)', row=i, col=1)
                fig.update_xaxes(gridcolor='rgba(255,255,255,0.05)', row=i, col=1)
            
            # Anomaly summary stats
            last_price = df['Close'].iloc[-1]
            vwap_val = df['vwap'].iloc[-1]
            cvd_val = df['cvd'].iloc[-1]
            total_vol = df['Volume'].sum()
            cvd_state = "Dominancia COMPRADORA" if cvd_val > 0 else "Dominancia VENDEDORA"

            summary = (
                f"<b>⚡ ANÁLISIS INSTITUCIONAL EN TIEMPO REAL (Ticks de 1 min)</b><br><br>"
                f"<b>Métricas del Día:</b> Precio=$<b>{last_price:,.2f}</b>  |  VWAP Institucional=$<b>{vwap_val:,.2f}</b><br>"
                f"Volumen Acumulado={total_vol:,.0f} nominales  |  CVD Neto={cvd_val:+,.0f} ({cvd_state})<br><br>"
                f"<b>💡 Interpretación Cuantitativa:</b><br>"
                f"• <b>Isolation Forest (Machine Learning):</b> El algoritmo está analizando la covarianza de la velocidad del precio, aceleración del volumen y bid/ask spread proxy.<br>"
                f"• Las cruces rojas marcadas en el gráfico indican <span style='color:#ef4444'><b>Micro-Crash Alerts</b></span>: Desviaciones algorítmicas extremas en periodos de 60 segundos (ej. Whale sweep, Stop Hunt).<br>"
                f"• <b>VWAP:</b> Línea dorada. Benchmark institucional. Precio > VWAP indica presión Bullish intradía general.<br>"
                f"• <b>CVD (Cumulative Volume Delta):</b> La presión agregada del Order Flow. Si el precio sube pero el CVD cae (Divergencia Oculta), se avecina un colapso."
            )
            fig.add_annotation(
                text=summary, x=0.5, y=-0.25, xref='paper', yref='paper',
                showarrow=False, align='center', font=dict(size=12, color='#cbd5e1', family='Inter'),
                bgcolor='rgba(15,23,42,0.95)', bordercolor='rgba(99,102,241,0.6)',
                borderwidth=1, borderpad=12,
            )

            return fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True})

        except Exception as e:
            import traceback
            tb = traceback.format_exc()
            return f"<div style='color:#ef4444; text-align:center; padding:40px;'>Intraday ML Error: {e}<br><pre>{tb}</pre></div>"
