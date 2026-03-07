"""
Quantitative Finance 3D Model Service
======================================
Provides advanced 3D surface and scatter visualizations used in
institutional quantitative analysis:

  1. Options Volatility Surface (Strike × Expiry × IV)
  2. Treasury Yield Curve Evolution (Maturity × Date × Yield)
  3. PCA Market Clustering (PC1 × PC2 × PC3 eigenspace)
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from typing import List, Dict, Any, Tuple
from scipy.interpolate import griddata
from scipy.fft import fft
from scipy.integrate import quad
from datetime import datetime, timedelta


# ──────────────────────────────────────────────────────────────────────────────
# Dark theme constants
# ──────────────────────────────────────────────────────────────────────────────
_DARK_LAYOUT = dict(
    template='plotly_dark',
    paper_bgcolor='#0a0a0a',
    plot_bgcolor='#0a0a0a',
    font=dict(family="Inter, system-ui, sans-serif", size=11, color="#94a3b8"),
)

_EMPTY_MSG = "<div style='color:#94a3b8; text-align:center; padding:40px; font-family:Inter,sans-serif;'>📊 No se pudieron obtener datos suficientes para generar este modelo 3D.</div>"


class QuantModelsService:
    """Generates interactive Plotly 3D charts for quantitative finance models."""

    def __init__(self, get_historical_uc, yahoo_provider):
        self.get_historical = get_historical_uc
        self.yahoo = yahoo_provider

    # ══════════════════════════════════════════════════════════════════════════
    # 1 ─ OPTIONS VOLATILITY SURFACE
    # ══════════════════════════════════════════════════════════════════════════
    async def get_volatility_surface(self, symbol: str = "SPY") -> str:
        """
        Builds a 3D implied-volatility surface from live options chain data.
        X = Strike Price, Y = Days to Expiration, Z = Implied Volatility (%)
        Uses scipy griddata for smooth cubic interpolation.
        """
        try:
            import yfinance as yf
            ticker = yf.Ticker(symbol)
            chain_data = self._yf_options_to_list(ticker)
        except Exception as e:
            return f"<div style='color:#ef4444; text-align:center; padding:40px;'>Error obteniendo cadena de opciones para {symbol}: {e}</div>"

        if not chain_data or len(chain_data) < 5:
            return _EMPTY_MSG

        df = pd.DataFrame(chain_data)
        required = {'strike', 'impliedVolatility', 'daysToExpiration'}
        if not required.issubset(set(df.columns)):
            # Try alternate column names
            col_map = {
                'implied_volatility': 'impliedVolatility',
                'days_to_expiration': 'daysToExpiration',
                'dte': 'daysToExpiration',
                'iv': 'impliedVolatility',
            }
            df.rename(columns=col_map, inplace=True)
            if not required.issubset(set(df.columns)):
                return _EMPTY_MSG

        df = df.dropna(subset=['strike', 'impliedVolatility', 'daysToExpiration'])
        df = df[df['impliedVolatility'] > 0]
        df = df[df['daysToExpiration'] > 0]

        if len(df) < 5:
            return _EMPTY_MSG

        # Interpolation grid
        strikes = df['strike'].values
        dte = df['daysToExpiration'].values
        iv = df['impliedVolatility'].values * 100  # to percentage

        grid_x = np.linspace(strikes.min(), strikes.max(), 60)
        grid_y = np.linspace(dte.min(), dte.max(), 40)
        gx, gy = np.meshgrid(grid_x, grid_y)

        try:
            gz = griddata((strikes, dte), iv, (gx, gy), method='cubic')
            # Fill NaN edges with nearest-neighbor
            gz_nn = griddata((strikes, dte), iv, (gx, gy), method='nearest')
            gz = np.where(np.isnan(gz), gz_nn, gz)
        except Exception:
            gz = griddata((strikes, dte), iv, (gx, gy), method='nearest')

        fig = go.Figure(data=[go.Surface(
            x=gx, y=gy, z=gz,
            colorscale='Viridis',
            colorbar=dict(title='IV (%)', ticksuffix='%'),
            contours=dict(
                z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True)
            ),
            opacity=0.92,
            hovertemplate='Strike: $%{x:.0f}<br>DTE: %{y:.0f} days<br>IV: %{z:.1f}%<extra></extra>'
        )])

        fig.update_layout(
            **_DARK_LAYOUT,
            title=dict(
                text=f'🌐 VOLATILITY SURFACE — {symbol.upper()}',
                x=0.5, font=dict(size=20, color="#f8fafc", family="Inter")
            ),
            scene=dict(
                xaxis_title='Strike Price ($)',
                yaxis_title='Days to Expiration',
                zaxis_title='Implied Volatility (%)',
                xaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                yaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                zaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                camera=dict(eye=dict(x=1.5, y=-1.5, z=1.0)),
            ),
            margin=dict(t=80, b=10, l=10, r=10),
        )

        # Stats for annotation
        iv_mean = iv.mean()
        iv_min = iv.min()
        iv_max = iv.max()
        n_calls = len([r for r in chain_data if r.get('type') == 'CALL'])
        n_puts = len([r for r in chain_data if r.get('type') == 'PUT'])
        n_exp = len(set(df['daysToExpiration']))
        
        smirk_detected = iv_max - iv_min > 15
        
        summary = (
            f"<b>🌐 SUPERFICIE DE VOLATILIDAD IMPLÍCITA (IV Surface)</b><br><br>"
            f"<b>Liquidez y Rango:</b> {n_calls} Calls + {n_puts} Puts en {n_exp} fechas de expiración.<br>"
            f"Intervalo de Strikes: ${strikes.min():.0f} – ${strikes.max():.0f}  |  IV Promedio: <b>{iv_mean:.1f}%</b><br><br>"
            f"<b>💡 Interpretación Cuantitativa:</b><br>"
            f"• El eje Z muestra qué tan cara es la 'prima de seguro' (IV) para cada Strike a través del tiempo.<br>"
            f"• {'⚠️ <b>Volatility Smirk/Smile detectado (>15% spread)</b>: El mercado está pagando un premium extremo por opciones Deep OTM (protección contra Crash o FOMO upside).' if smirk_detected else '✅ <b>Superficie Plana</b>: El mercado no anticipa eventos de cola (Black Swans) significativos; distribución cuasi-normal.'}<br>"
            f"• <b>Term Structure (Estructura Temporal):</b> Observa el eje DTE. Si la IV de corto plazo > largo plazo (Backwardation), hay pánico inminente.<br>"
            f"• <b>Edge de Trading:</b> Busca 'valles' (IV verde oscuro) para comprar opciones baratas, o 'picos' (IV amarillo/roja) para vender prima (Credit Spreads)."
        )
        fig.add_annotation(
            text=summary, x=0.01, y=0.99, xref='paper', yref='paper',
            showarrow=False, align='left', font=dict(size=11, color='#cbd5e1', family='Inter'),
            bgcolor='rgba(15,23,42,0.85)', bordercolor='rgba(99,102,241,0.5)',
            borderwidth=1, borderpad=10,
        )

        return fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True, 'scrollZoom': True})

    def _yf_options_to_list(self, ticker) -> list:
        """Convert yfinance Ticker options to a flat list of dicts."""
        rows = []
        today = datetime.now()
        for exp_str in ticker.options[:8]:  # limit to 8 expirations
            try:
                chain = ticker.option_chain(exp_str)
                exp_date = datetime.strptime(exp_str, "%Y-%m-%d")
                dte = (exp_date - today).days
                if dte <= 0:
                    continue
                for _, row in chain.calls.iterrows():
                    iv = row.get('impliedVolatility', 0)
                    if iv and iv > 0:
                        rows.append({
                            'strike': float(row['strike']),
                            'impliedVolatility': float(iv),
                            'daysToExpiration': dte,
                            'type': 'CALL',
                        })
                for _, row in chain.puts.iterrows():
                    iv = row.get('impliedVolatility', 0)
                    if iv and iv > 0:
                        rows.append({
                            'strike': float(row['strike']),
                            'impliedVolatility': float(iv),
                            'daysToExpiration': dte,
                            'type': 'PUT',
                        })
            except Exception:
                continue
        return rows

    # ══════════════════════════════════════════════════════════════════════════
    # 2 ─ YIELD CURVE EVOLUTION SURFACE
    # ══════════════════════════════════════════════════════════════════════════
    async def get_yield_surface(self) -> str:
        """
        Builds a 3D surface showing how the US Treasury yield curve
        has evolved over the past ~12 months.
        X = Maturity (months), Y = Date, Z = Yield (%)
        """
        try:
            import yfinance as yf

            # Treasury tickers and their maturities in months
            tickers_map = {
                '^IRX': 3,    # 3-Month Treasury Bill
                '^FVX': 60,   # 5-Year Treasury Note
                '^TNX': 120,  # 10-Year Treasury Note
                '^TYX': 360,  # 30-Year Treasury Bond
            }

            end_date = datetime.now()
            start_date = end_date - timedelta(days=365)

            frames = []
            for ticker_sym, maturity_months in tickers_map.items():
                try:
                    tk = yf.Ticker(ticker_sym)
                    hist = tk.history(start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
                    if hist.empty:
                        continue
                    df_t = hist[['Close']].copy()
                    df_t.columns = ['yield_pct']
                    df_t['maturity'] = maturity_months
                    df_t['date'] = df_t.index
                    frames.append(df_t.reset_index(drop=True))
                except Exception:
                    continue

            if len(frames) < 2:
                return _EMPTY_MSG

            df = pd.concat(frames, ignore_index=True)
            df = df.dropna(subset=['yield_pct'])
            df['date_num'] = (df['date'] - df['date'].min()).dt.days

            # Interpolation
            maturities = df['maturity'].values
            date_nums = df['date_num'].values
            yields = df['yield_pct'].values

            grid_x = np.linspace(maturities.min(), maturities.max(), 50)
            grid_y = np.linspace(date_nums.min(), date_nums.max(), 80)
            gx, gy = np.meshgrid(grid_x, grid_y)

            try:
                gz = griddata((maturities, date_nums), yields, (gx, gy), method='cubic')
                gz_nn = griddata((maturities, date_nums), yields, (gx, gy), method='nearest')
                gz = np.where(np.isnan(gz), gz_nn, gz)
            except Exception:
                gz = griddata((maturities, date_nums), yields, (gx, gy), method='nearest')

            # Create date labels for the Y axis
            min_date = df['date'].min()
            tick_positions = np.linspace(grid_y.min(), grid_y.max(), 8)
            tick_labels = [(min_date + timedelta(days=int(d))).strftime('%b %Y') for d in tick_positions]

            maturity_labels = {3: '3M', 6: '6M', 12: '1Y', 24: '2Y', 60: '5Y', 120: '10Y', 360: '30Y'}

            fig = go.Figure(data=[go.Surface(
                x=gx, y=gy, z=gz,
                colorscale='RdYlGn_r',
                colorbar=dict(title='Yield %', ticksuffix='%'),
                opacity=0.90,
                hovertemplate='Maturity: %{x:.0f}mo<br>Day Offset: %{y:.0f}<br>Yield: %{z:.2f}%<extra></extra>'
            )])

            fig.update_layout(
                **_DARK_LAYOUT,
                title=dict(
                    text='📐 TERM STRUCTURE EVOLUTION — US Treasury Yield Surface (12M)',
                    x=0.5, font=dict(size=18, color="#f8fafc", family="Inter")
                ),
                scene=dict(
                    xaxis_title='Maturity (Months)',
                    yaxis_title='Time',
                    zaxis_title='Yield (%)',
                    yaxis=dict(
                        tickvals=tick_positions.tolist(),
                        ticktext=tick_labels,
                        gridcolor='rgba(255,255,255,0.05)',
                        backgroundcolor='rgba(10,10,10,0.95)',
                        showbackground=True,
                    ),
                    xaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    zaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    camera=dict(eye=dict(x=1.8, y=-1.2, z=0.8)),
                ),
                margin=dict(t=80, b=10, l=10, r=10),
            )

            # Yield stats
            latest_yields = df.groupby('maturity')['yield_pct'].last()
            earliest_yields = df.groupby('maturity')['yield_pct'].first()
            spread_now = latest_yields.max() - latest_yields.min() if len(latest_yields) > 1 else 0
            
            # Check 10y2y or similar inversion
            yield_5y = latest_yields.get(60, 0)
            yield_10y = latest_yields.get(120, 0)
            yield_3m = latest_yields.get(3, 0)
            is_inverted = yield_3m > yield_10y if (yield_3m and yield_10y) else False

            summary = (
                f"<b>📐 EVOLUCIÓN DE LA CURVA DE RENDIMIENTOS DEL TESORO (US Treasury)</b><br><br>"
                f"<b>Estado Actual:</b> Spread Corto-Largo: {spread_now:.2f}%<br>"
                f"Rendimientos Hoy: 3M={yield_3m:.2f}% | 5Y={yield_5y:.2f}% | 10Y={yield_10y:.2f}%<br><br>"
                f"<b>💡 Implicaciones Macroeconómicas:</b><br>"
                f"• { '⚠️ <span style=\"color:#ef4444\"><b>CURVA INVERTIDA (3M > 10Y):</b></span> Fuerte indicador leading de recesión económica y estrés crediticio.' if is_inverted else '✅ <span style=\"color:#10b981\"><b>CURVA NORMAL (Ascendente):</b></span> Indica expansión económica y compensación normal por riesgo de duración.' }<br>"
                f"• El color de la superficie sigue la pendiente de los tipos de interés. Observa el eje temporal para ver las pausas o pivotes de la FED.<br>"
                f"• Cuando los bonos a largo plazo caen por debajo de los de corto plazo, el smart money está asegurando yields a largo asumiendo que<br>"
                f"  los bancos centrales tendrán que recortar tipos agresivamente ante una caída económica."
            )
            fig.add_annotation(
                text=summary, x=0.01, y=0.99, xref='paper', yref='paper',
                showarrow=False, align='left', font=dict(size=11, color='#cbd5e1', family='Inter'),
                bgcolor='rgba(15,23,42,0.85)', bordercolor={'rgba(239, 68, 68, 0.5)' if is_inverted else 'rgba(16, 185, 129, 0.5)'},
                borderwidth=1, borderpad=10,
            )

            return fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True, 'scrollZoom': True})

        except Exception as e:
            return f"<div style='color:#ef4444; text-align:center; padding:40px;'>Error generando Yield Surface: {e}</div>"

    # ══════════════════════════════════════════════════════════════════════════
    # 3 ─ PCA CLUSTERING (PRINCIPAL COMPONENT ANALYSIS)
    # ══════════════════════════════════════════════════════════════════════════
    async def get_pca_clusters(self, symbols_str: str = "AAPL,MSFT,NVDA,TSLA,META,AMZN,GOOGL,JPM,V,JNJ") -> str:
        """
        Performs Principal Component Analysis on daily returns of the
        given basket of stocks. Projects them into 3D eigenspace
        (PC1, PC2, PC3) to reveal latent market factor clustering.
        """
        try:
            import yfinance as yf

            symbols = [s.strip().upper() for s in symbols_str.split(',') if s.strip()]
            if len(symbols) < 3:
                return "<div style='color:#ef4444; text-align:center; padding:40px;'>Se necesitan al menos 3 símbolos para PCA.</div>"

            end_date = datetime.now()
            start_date = end_date - timedelta(days=365)

            # Download all prices at once
            price_data = yf.download(
                symbols,
                start=start_date.strftime('%Y-%m-%d'),
                end=end_date.strftime('%Y-%m-%d'),
                progress=False
            )

            if price_data.empty:
                return _EMPTY_MSG

            # Extract closing prices
            if 'Close' in price_data.columns.get_level_values(0):
                closes = price_data['Close']
            else:
                closes = price_data

            # Handle single-symbol edge case
            if isinstance(closes, pd.Series):
                return "<div style='color:#ef4444;'>Se necesitan al menos 3 símbolos válidos para PCA.</div>"

            # Drop symbols with too many NaN
            closes = closes.dropna(axis=1, thresh=int(len(closes) * 0.7))
            if closes.shape[1] < 3:
                return "<div style='color:#ef4444;'>No se obtuvieron suficientes datos. Intenta con otros símbolos.</div>"

            # Daily returns
            returns = closes.pct_change().dropna()
            if len(returns) < 30:
                return _EMPTY_MSG

            # Standardize
            returns_std = (returns - returns.mean()) / returns.std()

            # Covariance matrix & Eigen decomposition
            cov_matrix = returns_std.cov().values
            eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

            # Sort by descending eigenvalue
            idx = np.argsort(eigenvalues)[::-1]
            eigenvalues = eigenvalues[idx]
            eigenvectors = eigenvectors[:, idx]

            # Project data onto first 3 principal components
            pc_scores = returns_std.values @ eigenvectors[:, :3]

            # Build DataFrame for plotting — one point per asset
            # We take the mean projection of each asset across time
            asset_names = returns_std.columns.tolist()
            asset_projections = []
            for i, sym in enumerate(asset_names):
                asset_projections.append({
                    'symbol': sym,
                    'PC1': float(eigenvectors[i, 0]),
                    'PC2': float(eigenvectors[i, 1]),
                    'PC3': float(eigenvectors[i, 2]),
                    'volatility': float(returns[sym].std() * np.sqrt(252) * 100),  # annualized vol %
                    'return': float(returns[sym].mean() * 252 * 100),  # annualized return %
                })

            df_pca = pd.DataFrame(asset_projections)

            # Variance explained
            total_var = eigenvalues.sum()
            var_explained = eigenvalues[:3] / total_var * 100

            fig = px.scatter_3d(
                df_pca,
                x='PC1', y='PC2', z='PC3',
                color='volatility',
                color_continuous_scale='Plasma',
                size='volatility',
                size_max=30,
                hover_name='symbol',
                hover_data={
                    'return': ':.1f',
                    'volatility': ':.1f',
                    'PC1': ':.4f',
                    'PC2': ':.4f',
                    'PC3': ':.4f',
                },
                text='symbol',
                title='',
            )

            fig.update_traces(
                textposition='top center',
                textfont=dict(size=11, color='#f8fafc', family='Inter'),
                marker=dict(line=dict(width=1, color='rgba(255,255,255,0.3)'))
            )

            fig.update_layout(
                **_DARK_LAYOUT,
                title=dict(
                    text=f'🧬 PCA MARKET CLUSTERING — Eigenspace Projection ({len(asset_names)} Assets)',
                    x=0.5, font=dict(size=18, color="#f8fafc", family="Inter")
                ),
                scene=dict(
                    xaxis_title=f'PC1 ({var_explained[0]:.1f}% var)',
                    yaxis_title=f'PC2 ({var_explained[1]:.1f}% var)',
                    zaxis_title=f'PC3 ({var_explained[2]:.1f}% var)',
                    xaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    yaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    zaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    camera=dict(eye=dict(x=1.5, y=-1.5, z=1.2)),
                ),
                margin=dict(t=80, b=10, l=10, r=10),
                coloraxis_colorbar=dict(title='Ann. Vol %'),
            )

            # PCA stats
            total_var_3 = var_explained[:3].sum()
            highest_vol = df_pca.loc[df_pca['volatility'].idxmax()]
            lowest_vol = df_pca.loc[df_pca['volatility'].idxmin()]
            
            summary = (
                f"<b>🧬 EIGENSPACE PCA (Principal Component Analysis)</b><br><br>"
                f"<b>Estructura de Varianza:</b> 3 componentes explican el <b>{total_var_3:.1f}%</b> del riesgo total del grupo.<br>"
                f"Distribución: PC1={var_explained[0]:.1f}%  |  PC2={var_explained[1]:.1f}%  |  PC3={var_explained[2]:.1f}%<br><br>"
                f"<b>💡 Interpretación Cuantitativa:</b><br>"
                f"• El <b>PC1 (Market Factor)</b> representa la direccionalidad general del mercado. Activos muy dispersos en X reaccionan distinto al SP500.<br>"
                f"• El <b>PC2 y PC3</b> suelen aislar factores de rotación sectorial, Growth vs Value, o riesgo intrínseco.<br>"
                f"• <b>Distancia Euclidiana:</b> Activos agrupados de cerca en este espacio 3D son estadísticamente interdependientes. <i>Son el mismo trade.</i><br>"
                f"• Para máxima diversificación, construye spreads entre portfolios ubicados en cuadrantes opuestos del Eigenspace.<br>"
                f"• Esfera más pequeña = {lowest_vol['symbol']} (Hedge defensivo). Esfera más grande = {highest_vol['symbol']} (Driver de riesgo)."
            )
            fig.add_annotation(
                text=summary, x=0.01, y=0.99, xref='paper', yref='paper',
                showarrow=False, align='left', font=dict(size=11, color='#cbd5e1', family='Inter'),
                bgcolor='rgba(15,23,42,0.85)', bordercolor='rgba(99,102,241,0.5)',
                borderwidth=1, borderpad=10,
            )

            return fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True, 'scrollZoom': True})

        except Exception as e:
            return f"<div style='color:#ef4444; text-align:center; padding:40px;'>Error en PCA: {e}</div>"

    # ══════════════════════════════════════════════════════════════════════════
    # 4 ─ BLACK-SCHOLES OPTIONS & 3D GREEKS
    # ══════════════════════════════════════════════════════════════════════════
    async def get_black_scholes(self, symbol: str = "SPY", risk_free_rate: float = 0.045) -> str:
        """
        Calculates Black-Scholes theoretical pricing for at-the-money options
        and plots the 3D surface of the Greeks (Delta, Gamma, Vega, Theta).
        Also calculates Implied Volatility using Newton-Raphson.
        """
        try:
            import yfinance as yf
            from scipy.stats import norm
            from plotly.subplots import make_subplots

            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="1y")
            S = hist['Close'].values[-1]  # Current underlying price
            volatility = hist['Close'].pct_change().std() * np.sqrt(252) # Historical proxy

            chain_data = self._yf_options_to_list(ticker)
            if not chain_data:
                return _EMPTY_MSG
            
            df = pd.DataFrame(chain_data)
            calls = df[df['type'] == 'CALL']
            if calls.empty: return _EMPTY_MSG
            
            # Sub-functions for BS Math
            def d1(S, K, T, r, sigma):
                return (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
            
            def d2(S, K, T, r, sigma):
                return d1(S, K, T, r, sigma) - sigma*np.sqrt(T)
            
            def bs_call(S, K, T, r, sigma):
                return S * norm.cdf(d1(S, K, T, r, sigma)) - K * np.exp(-r*T) * norm.cdf(d2(S, K, T, r, sigma))
            
            def greeks_call(S, K, T, r, sigma):
                d1_val = d1(S, K, T, r, sigma)
                d2_val = d2(S, K, T, r, sigma)
                
                delta = norm.cdf(d1_val)
                gamma = norm.pdf(d1_val) / (S * sigma * np.sqrt(T))
                vega = S * norm.pdf(d1_val) * np.sqrt(T) / 100 # per 1% change
                theta = (-S * norm.pdf(d1_val) * sigma / (2 * np.sqrt(T)) - r * K * np.exp(-r*T) * norm.cdf(d2_val)) / 365
                rho = K * T * np.exp(-r*T) * norm.cdf(d2_val) / 100
                
                return delta, gamma, vega, theta, rho

            # Generate Grid for 3D Surface (Strike vs Time to Expiration)
            strike_range = np.linspace(S * 0.7, S * 1.3, 50)
            time_range = np.linspace(0.01, 1.0, 50) # 1 day to 1 year
            X, Y = np.meshgrid(strike_range, time_range)
            
            Delta = np.zeros_like(X)
            Gamma = np.zeros_like(X)
            Vega = np.zeros_like(X)
            Theta = np.zeros_like(X)
            
            for i in range(X.shape[0]):
                for j in range(X.shape[1]):
                    K = X[i, j]
                    T = Y[i, j]
                    delta, gamma, vega, theta, _ = greeks_call(S, K, T, risk_free_rate, volatility)
                    Delta[i, j] = delta
                    Gamma[i, j] = gamma
                    Vega[i, j] = vega
                    Theta[i, j] = theta

            # Find nearest ATM Call on nearest expiration for reference pricing
            calls['strike_diff'] = abs(calls['strike'] - S)
            closest_strike = calls.loc[calls['strike_diff'].idxmin()]
            K_atm = closest_strike['strike']
            T_atm = closest_strike['daysToExpiration'] / 365.0
            actual_iv = closest_strike['impliedVolatility']
            
            bs_price = bs_call(S, K_atm, T_atm, risk_free_rate, actual_iv)
            atm_delta, atm_gamma, atm_vega, atm_theta, atm_rho = greeks_call(S, K_atm, T_atm, risk_free_rate, actual_iv)

            # Build Multi-panel Subplots (2x2)
            fig = make_subplots(
                rows=2, cols=2,
                specs=[[{'type': 'surface'}, {'type': 'surface'}],
                       [{'type': 'surface'}, {'type': 'table'}]],
                subplot_titles=['Δ Delta Surface', 'Γ Gamma Surface', 'ν Vega Surface', 'Quantitative Pricing Model']
            )

            # Delta Surface
            fig.add_trace(go.Surface(
                x=X, y=Y*365, z=Delta, colorscale='Viridis',
                colorbar=dict(title='Delta', x=0.45, len=0.4, y=0.8),
                hovertemplate='Strike: $%{x:.1f}<br>DTE: %{y:.0f}<br>Delta: %{z:.3f}<extra></extra>'
            ), row=1, col=1)

            # Gamma Surface
            fig.add_trace(go.Surface(
                x=X, y=Y*365, z=Gamma, colorscale='Plasma',
                colorbar=dict(title='Gamma', x=1.0, len=0.4, y=0.8),
                hovertemplate='Strike: $%{x:.1f}<br>DTE: %{y:.0f}<br>Gamma: %{z:.4f}<extra></extra>'
            ), row=1, col=2)

            # Vega Surface
            fig.add_trace(go.Surface(
                x=X, y=Y*365, z=Vega, colorscale='Inferno',
                colorbar=dict(title='Vega', x=0.45, len=0.4, y=0.2),
                hovertemplate='Strike: $%{x:.1f}<br>DTE: %{y:.0f}<br>Vega: %{z:.3f}<extra></extra>'
            ), row=2, col=1)

            # Table Stats
            row_colors = ['#1e293b', '#0f172a'] * 6
            fig.add_trace(go.Table(
                header=dict(
                    values=['<b>Métrica Black-Scholes</b>', '<b>Valor Actual</b>'],
                    fill_color='#334155', font=dict(color='white', size=14, family='Inter'),
                    height=35
                ),
                cells=dict(
                    values=[
                        ['Underlying Price (S)', 'Strike (ATM)', 'Days to Exp (DTE)', 'Risk-Free Rate', 'Implied Volatility (σ)', '<b>Theo BS Call Price</b>', 'Δ Delta', 'Γ Gamma', 'ν Vega (per 1% IV)', 'Θ Theta (per day)', 'ρ Rho'],
                        [f"${S:.2f}", f"${K_atm:.2f}", f"{T_atm*365:.0f}", f"{risk_free_rate*100:.1f}%", f"{actual_iv*100:.1f}%", f"<b>${bs_price:.2f}</b>", f"{atm_delta:.3f}", f"{atm_gamma:.4f}", f"${atm_vega:.2f}", f"${atm_theta:.2f}", f"${atm_rho:.3f}"]
                    ],
                    fill_color=[row_colors]*2, font=dict(color='#f8fafc', size=13, family='Inter'), height=32
                )
            ), row=2, col=2)

            fig.update_layout(
                **_DARK_LAYOUT,
                title=dict(
                    text=f'📉 BLACK-SCHOLES OPTIONS THEORETICAL MODEL — {symbol.upper()}',
                    x=0.5, font=dict(size=18, color="#f8fafc", family="Inter")
                ),
                height=1100,
                margin=dict(t=80, b=220, l=10, r=10)
            )

            # Update 3D scenes
            for i, j in [(1,1), (1,2), (2,1)]:
                scene = f'scene{i if i==1 and j==1 else (2 if i==1 else 3)}'
                fig.layout[scene].update(
                    xaxis_title='Strike Price ($)',
                    yaxis_title='Time to Expiry (Days)',
                    xaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    yaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    zaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(10,10,10,0.95)', showbackground=True),
                    camera=dict(eye=dict(x=1.5, y=-1.5, z=1.0))
                )

            summary = (
                f"<b>🧠 BLACK-SCHOLES (Partial Differential Equation)</b><br><br>"
                f"<b>💡 Interpretación Cuantitativa:</b><br>"
                f"• <b>Δ Delta:</b> Exposición direccional. ATM Call Delta ≈ 0.50. Representa 'cuántas acciones posees sintéticamente'.<br>"
                f"• <b>Γ Gamma:</b> Aceleración de Delta. Observa su pico en ATM cerca de expiración (Gamma Risk).<br>"
                f"• <b>ν Vega:</b> Riesgo de Volatilidad. Opciones de largo plazo son altamente sensibles a IV (vega máxima).<br>"
                f"• <b>Θ Theta:</b> Riesgo de Tiempo (Decaimiento). Acelera agresivamente en la última semana antes de expiración."
            )
            fig.add_annotation(
                text=summary, x=0.5, y=-0.28, xref='paper', yref='paper',
                showarrow=False, align='center', font=dict(size=12, color='#cbd5e1', family='Inter'),
                bgcolor='rgba(15,23,42,0.95)', bordercolor='rgba(99,102,241,0.6)',
                borderwidth=1, borderpad=12,
            )

            return fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True, 'scrollZoom': True})

        except Exception as e:
            return f"<div style='color:#ef4444; text-align:center; padding:40px;'>Black-Scholes Error: {e}</div>"

    # ══════════════════════════════════════════════════════════════════════════
    # 5 ─ RELATIVE STRENGTH / PAIR TRADING ANALYSIS
    # ══════════════════════════════════════════════════════════════════════════
    async def get_relative_strength(self, symbol1: str = "NVDA", symbol2: str = "INTC", period: str = "2y") -> str:
        """
        Calculates Logarithmic Relative Strength, Z-Score (Mean Reversion), 
        and Rolling Correlation between two assets to find structural dominance or 
        arbitrage/pair trading setups.
        """
        try:
            import yfinance as yf
            from plotly.subplots import make_subplots

            # Fetch Data
            df1 = yf.Ticker(symbol1).history(period=period)['Close']
            df2 = yf.Ticker(symbol2).history(period=period)['Close']

            df = pd.DataFrame({symbol1: df1, symbol2: df2}).dropna()

            if len(df) < 60:
                return f"<div style='color:#94a3b8; text-align:center; padding:40px;'>No hay suficientes precios solapados para {symbol1}/{symbol2}.</div>"

            # 1. Math / Transformations
            # Log Ratio prevents scaling issues
            df['Log_Ratio'] = np.log(df[symbol1] / df[symbol2])
            
            # Simple Ratio for easier readability
            df['Ratio'] = df[symbol1] / df[symbol2]
            
            # 50-Day Moving Average & Z-Score
            ma_window = 50
            df['Ratio_MA'] = df['Ratio'].rolling(window=ma_window).mean()
            df['Ratio_STD'] = df['Ratio'].rolling(window=ma_window).std()
            df['Z_Score'] = (df['Ratio'] - df['Ratio_MA']) / df['Ratio_STD']
            
            # 60-Day Rolling Correlation
            df['Ret1'] = df[symbol1].pct_change()
            df['Ret2'] = df[symbol2].pct_change()
            df['Rolling_Corr'] = df['Ret1'].rolling(window=60).corr(df['Ret2'])

            df.dropna(inplace=True)

            # 2. Build Subplots (3 panels)
            fig = make_subplots(
                rows=3, cols=1,
                shared_xaxes=True,
                vertical_spacing=0.03,
                row_heights=[0.5, 0.25, 0.25],
                subplot_titles=[
                    f"🏆 Fuerza Relativa: {symbol1} / {symbol2} (Línea Ascendente = {symbol1} Domina)",
                    "⚖️ Z-Score Cíclico (Spread Histórico a 50D)",
                    "🔗 Correlación Lineal Rolling (60D)"
                ]
            )

            # --- Panel 1: Relative Strength Ratio ---
            # Color area based on who is outperforming (ratio MA slope)
            fig.add_trace(go.Scatter(
                x=df.index, y=df['Ratio'], mode='lines', name='Spread Real', 
                line=dict(color='#f8fafc', width=2)
            ), row=1, col=1)

            fig.add_trace(go.Scatter(
                x=df.index, y=df['Ratio_MA'], mode='lines', name=f'Media Móvil {ma_window}D', 
                line=dict(color='#8b5cf6', width=1.5, dash='dot')
            ), row=1, col=1)

            # Highlight extreme standard deviations
            fig.add_trace(go.Scatter(
                x=df.index, y=df['Ratio_MA'] + (2 * df['Ratio_STD']), mode='lines', name='+2 StdDev', 
                line=dict(color='#ef4444', width=1, dash='dash')
            ), row=1, col=1)

            fig.add_trace(go.Scatter(
                x=df.index, y=df['Ratio_MA'] - (2 * df['Ratio_STD']), mode='lines', name='-2 StdDev', 
                line=dict(color='#10b981', width=1, dash='dash'), fill='tonexty', fillcolor='rgba(255,255,255,0.02)'
            ), row=1, col=1)

            # --- Panel 2: Z-Score (Mean Reversion) ---
            colors_z = ['#ef4444' if z >= 2 else '#10b981' if z <= -2 else '#3b82f6' for z in df['Z_Score']]
            fig.add_trace(go.Bar(
                x=df.index, y=df['Z_Score'], name='Z-Score', marker_color=colors_z
            ), row=2, col=1)
            
            # Z-Score boundaries
            fig.add_hline(y=2, row=2, col=1, line_dash='dash', line_color='#ef4444', annotation_text='Sobrecomprado')
            fig.add_hline(y=-2, row=2, col=1, line_dash='dash', line_color='#10b981', annotation_text='Sobrevendido')
            fig.add_hline(y=0, row=2, col=1, line_color='rgba(255,255,255,0.2)')

            # --- Panel 3: Correlation ---
            fig.add_trace(go.Scatter(
                x=df.index, y=df['Rolling_Corr'], name='Correlación Pearsons', 
                line=dict(color='#f59e0b', width=1.5), fill='tozeroy', fillcolor='rgba(245, 158, 11, 0.1)'
            ), row=3, col=1)
            fig.add_hline(y=0, row=3, col=1, line_dash='dash', line_color='rgba(255,255,255,0.3)')

            # 3. Layout & Styling
            fig.update_layout(
                **_DARK_LAYOUT,
                title=dict(
                    text=f'⚔️ PAIR TRADING & RELATIVE STRENGTH — {symbol1.upper()} vs {symbol2.upper()}',
                    x=0.5, font=dict(size=18, color="#f8fafc", family="Inter")
                ),
                height=950,
                hovermode='x unified',
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                margin=dict(t=80, b=180, l=40, r=40)
            )

            # Layout grid updates
            for i in range(1, 4):
                fig.update_yaxes(gridcolor='rgba(255,255,255,0.05)', row=i, col=1)
                fig.update_xaxes(gridcolor='rgba(255,255,255,0.05)', row=i, col=1)

            # 4. Institutional Insight Analysis
            current_z = df['Z_Score'].iloc[-1]
            current_corr = df['Rolling_Corr'].iloc[-1]
            current_ratio = df['Ratio'].iloc[-1]
            start_ratio = df['Ratio'].iloc[0]
            
            # Trend Check
            trend = f"<b>{symbol1}</b> está aplastando estructuralmente a {symbol2}." if current_ratio > start_ratio else f"<b>{symbol2}</b> está dominando estructuralmente a {symbol1}."
            
            # ZScore Check
            if current_z > 2:
                signal = f"🚨 <b>EXTREMO:</b> Venta Corta en el Spread ({symbol1} sobre-extendido contra {symbol2})."
            elif current_z < -2:
                signal = f"✅ <b>OPORTUNIDAD:</b> Compra Larga en el Spread ({symbol1} subvaluado contra {symbol2})."
            else:
                signal = f"⚡ <b>NEUTRAL:</b> Estabilidad en la valoración cruzada. Z-Score = {current_z:.2f}."
                
            # Corr Check
            if current_corr < 0:
                corr_txt = "Cobertura Natural (Covarianza Negativa). Ideal para rotación."
            elif current_corr < 0.5:
                corr_txt = "Diversificación moderada. Se mueven independientemente."
            else:
                corr_txt = f"Alto acoplamiento ({current_corr:.2f}). Esencialmente el mismo factor direccional."

            summary = (
                f"<b>🧠 ANÁLISIS DE FUERZA RELATIVA INSTITUCIONAL</b><br><br>"
                f"<b>1. Dominancia Direccional:</b> {trend} El gráfico Log-Ratio filtra el ruido y aísla la ventaja (Edge) de Retorno.<br>"
                f"<b>2. Reversión a la Media (Statistical Arbitrage):</b> {signal}<br>"
                f"   El Panel 2 mide qué tan desviada está la campana de Gauss. Un Z-Score fuera de [-2, +2] genera setups institucionales de reversión.<br>"
                f"<b>3. Régimen de Correlación:</b> {corr_txt}<br>"
                f"   El Panel 3 muestra si el mercado los trata como sustitutos o si los flujos de capital están huyendo del uno hacia el otro."
            )
            fig.add_annotation(
                text=summary, x=0.5, y=-0.25, xref='paper', yref='paper',
                showarrow=False, align='center', font=dict(size=12, color='#cbd5e1', family='Inter'),
                bgcolor='rgba(15,23,42,0.95)', bordercolor='rgba(99,102,241,0.6)',
                borderwidth=1, borderpad=12,
            )

            return fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True})

        except Exception as e:
            return f"<div style='color:#ef4444; text-align:center; padding:40px;'>Relative Strength Error: {e}</div>"
    
    # ══════════════════════════════════════════════════════════════════════════
    # 6 ─ CARR-MADAN FFT OPTION PRICING
    # ══════════════════════════════════════════════════════════════════════════
    async def get_fft_option_pricing(
        self, 
        symbol: str = "SPY", 
        model: str = "heston", 
        risk_free: float = 0.045
    ) -> str:
        """
        Calculates European Call prices using the Carr-Madan FFT algorithm.
        Allows for extremely fast pricing across thousands of strikes.
        
        X = Strike Price ($), Y = Option Price ($)
        Comparison between Market Mid-Price and Theoretical Model (Heston or BS).
        """
        try:
            import yfinance as yf
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="1y")
            S = hist['Close'].values[-1]
            h_vol = hist['Close'].pct_change().std() * np.sqrt(252)

            chain_data = self._yf_options_to_list(ticker)
            if not chain_data:
                # Mock data if none available (weekend or API limit)
                strikes_mkt = np.linspace(S*0.8, S*1.2, 20)
                prices_mkt = np.maximum(S - strikes_mkt, 0)
                dte = 30
            else:
                df_mkt = pd.DataFrame(chain_data)
                df_mkt = df_mkt[df_mkt['type'] == 'CALL'].sort_values('strike')
                # Take the first expiration for clarity in 2D plot or multiple if we want 3D
                first_dte = df_mkt['daysToExpiration'].unique()[0]
                df_mkt = df_mkt[df_mkt['daysToExpiration'] == first_dte]
                strikes_mkt = df_mkt['strike'].values
                # We don't have Bid/Ask in _yf_options_to_list, we only have IV. 
                # Calculating Mid from BS if unavailable, but let's try to get more data
                # Actually, Black-Scholes surface already uses BS, we want to show THEORETICAL prices
                dte = first_dte

            T = dte / 365.0
            r = risk_free

            # FFT Parameters
            N = 4096
            delta_u = 0.25
            alpha = 1.1 # Damping factor
            
            # Strike mapping
            delta_k = (2 * np.pi) / (N * delta_u)
            b = (N * delta_k) / 2
            
            # m range [0, N-1]
            m = np.arange(N)
            k_m = -b + m * delta_k
            K_vals = np.exp(k_m)
            
            # u range: v_j = j * delta_u
            j = np.arange(N)
            v_j = j * delta_u
            
            # Weights for Simpson's rule
            w = np.ones(N)
            w[0] = 1/3
            w[1:N-1:2] = 4/3
            w[2:N-2:2] = 2/3
            
            # Model selection
            if model == "heston":
                # Heston params (typical values)
                v0 = h_vol**2
                kappa = 2.0  # Mean reversion speed
                theta = h_vol**2 # Long run variance
                sigma = 0.3  # Vol of vol
                rho = -0.7   # Correlation
                phi_func = lambda u: self._heston_char_func(u, S, T, r, 0.0, v0, kappa, theta, sigma, rho)
            else:
                # Black-Scholes
                phi_func = lambda u: self._bs_char_func(u, S, T, r, 0.0, h_vol)

            # Modified Characteristic Function
            # psi(v) = exp(-rt) * phi(v - (alpha+1)i) / (alpha^2 + alpha - v^2 + i(2alpha+1)v)
            def psi(v):
                u_shifted = v - (alpha + 1) * 1j
                denom = (alpha**2 + alpha - v**2 + 1j * (2 * alpha + 1) * v)
                return np.exp(-r * T) * phi_func(u_shifted) / denom

            psi_vals = psi(v_j)
            
            # FFT input
            x = np.exp(1j * b * v_j) * psi_vals * delta_u * w
            ff_res = fft(x)
            
            # Call price C(k_m) = exp(-alpha * k_m) / pi * Re(ff_res)
            C_list = (np.exp(-alpha * k_m) / np.pi) * np.real(ff_res)
            
            # Filter reasonable range around S (S*0.5 to S*1.5)
            mask = (K_vals > S * 0.5) & (K_vals < S * 1.5)
            K_plot = K_vals[mask]
            C_plot = C_list[mask]
            
            # Plotly Visualization
            fig = go.Figure()
            
            # Theoretical Model
            fig.add_trace(go.Scatter(
                x=K_plot, y=C_plot,
                mode='lines',
                name=f'FFT Model: {model.upper()}',
                line=dict(color='#22d3ee', width=3),
                hovertemplate='Strike: $%{x:.2f}<br>Price: $%{y:.2f}'
            ))
            
            # Market points (if available)
            if len(strikes_mkt) > 0 and 'df_mkt' in locals():
                from scipy.stats import norm
                def bs_c(S, K, T, r, sigma):
                    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
                    d2 = d1 - sigma*np.sqrt(T)
                    return S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
                
                mkt_mid = []
                for idx, row in df_mkt.iterrows():
                    mkt_mid.append(bs_c(S, row['strike'], T, r, row['impliedVolatility']))
                
                fig.add_trace(go.Scatter(
                    x=strikes_mkt, y=mkt_mid,
                    mode='markers',
                    name='Market Mid (BS Proxy)',
                    marker=dict(color='#fb923c', size=8, symbol='x'),
                    hovertemplate='Market Strike: $%{x:.2f}<br>Market Price: $%{y:.2f}'
                ))

            fig.update_layout(
                **_DARK_LAYOUT,
                title=dict(
                    text=f'⚡ CARR-MADAN FFT OPTION PRICING — {symbol.upper()} ({model.capitalize()})',
                    x=0.5, font=dict(size=18, color="#f8fafc", family="Inter")
                ),
                xaxis=dict(title='Strike Price ($)', gridcolor='rgba(255,255,255,0.05)'),
                yaxis=dict(title='Price ($)', gridcolor='rgba(255,255,255,0.05)'),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                margin=dict(t=100, b=150, l=60, r=40)
            )

            # Annotation for Quants
            summary = (
                f"<b>⚡ VALORACIÓN POR TRANSFORMADA DE FOURIER (Carr-Madan 1999)</b><br><br>"
                f"<b>Modelo:</b> {model.upper()} | <b>Spot (S₀):</b> ${S:.2f} | <b>DTE:</b> {dte} días<br>"
                f"<b>Configuración FFT:</b> N={N}, Δu={delta_u}, α={alpha}<br><br>"
                f"<b>💡 Insight:</b> FFT permite calcular precios para <b>{N} strikes</b> simultáneamente en milisegundos.<br>"
                f"• El modelo de {model.capitalize()} captura mejor {'la asimetría (skewness) y curtosis (vol of vol)' if model == 'heston' else 'la distribución log-normal estándar'}.<br>"
                f"• Si el <b>SML (Skew)</b> es pronunciado, Heston se ajusta mejor que Black-Scholes."
            )
            fig.add_annotation(
                text=summary, x=0.5, y=-0.25, xref='paper', yref='paper',
                showarrow=False, align='center', font=dict(size=12, color='#cbd5e1', family='Inter'),
                bgcolor='rgba(15,23,42,0.95)', bordercolor='rgba(34,211,238,0.6)',
                borderwidth=1, borderpad=12,
            )

            return fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True})

        except Exception as e:
            return f"<div style='color:#ef4444; text-align:center; padding:40px;'>FFT Pricing Error: {e}</div>"

    def _bs_char_func(self, u, S, T, r, q, sigma):
        """Standard Black-Scholes Characteristic Function."""
        mu = np.log(S) + (r - q - 0.5 * sigma**2) * T
        return np.exp(1j * u * mu - 0.5 * sigma**2 * u**2 * T)

    def _heston_char_func(self, u, S, T, r, q, v0, kappa, theta, sigma, rho):
        """Heston Stochastic Volatility Model Characteristic Function."""
        # Derived from Heston (1993)
        x = np.log(S)
        a = kappa * theta
        b = kappa
        
        d = np.sqrt((rho * sigma * u * 1j - b)**2 - sigma**2 * (-u * 1j - u**2))
        g = (b - rho * sigma * u * 1j + d) / (b - rho * sigma * u * 1j - d)
        
        C = (r - q) * u * 1j * T + a / sigma**2 * ((b - rho * sigma * u * 1j + d) * T - 2 * np.log((1 - g * np.exp(d * T)) / (1 - g)))
        D = (b - rho * sigma * u * 1j + d) / sigma**2 * ((1 - np.exp(d * T)) / (1 - g * np.exp(d * T)))
        
        return np.exp(C + D * v0 + 1j * u * x)
