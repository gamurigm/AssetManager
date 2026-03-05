import plotly.graph_objects as go
import plotly.express as px
from typing import List, Dict, Any, Optional
import pandas as pd
import json

class PortfolioChartService:
    def __init__(self, repo, get_quote_use_case):
        self.repo = repo
        self.get_quote = get_quote_use_case

    async def _get_enriched_portfolio(self) -> List[Dict[str, Any]]:
        holdings = self.repo.get_portfolio()
        enriched = []
        for h in holdings:
            symbol = h.get('symbol', 'Unknown')
            shares = float(h.get('shares') or 0.0)
            entry_price = float(h.get('entryPrice') or 0.0)
            factor = float(h.get('factor') or 1.0)
            
            try:
                quote = await self.get_quote.execute(symbol)
                # If quote fails, we fall back to entry_price to avoid 0 values
                current_price = float(quote.get('price', quote.get('last_price', entry_price)) or entry_price)
            except Exception as e:
                print(f"[ChartService] Quote fetch error for {symbol}: {e}")
                current_price = entry_price
            
            # Use absolute value for VALUE (Exposure) - pie charts need positive numbers
            # We store the signed value for PnL but provide absValue for the chart
            signed_value = shares * current_price * factor
            abs_value = abs(signed_value)
            
            cost = shares * entry_price * factor
            pnl = signed_value - cost
            pnl_pct = (pnl / abs(cost) * 100) if cost != 0 else 0
            
            h['currentPrice'] = current_price
            h['currentValue'] = signed_value
            h['absAllocation'] = abs_value  # Use this for Pie
            h['costBasis'] = cost
            h['pnl'] = pnl
            h['pnlPct'] = pnl_pct
            enriched.append(h)
        return enriched

    async def get_allocation_pie(self) -> str:
        data = await self._get_enriched_portfolio()
        if not data: return "<div style='color:white; text-align:center; padding:20px;'>No hay datos en el portafolio</div>"
        
        df = pd.DataFrame(data)
        total_abs = df['absAllocation'].sum()
        
        # Group assets < 1% into 'Others' to avoid visual clutter
        threshold = total_abs * 0.01
        df['display_symbol'] = df.apply(lambda row: row['symbol'] if row['absAllocation'] >= threshold else 'Others', axis=1)
        plot_df = df.groupby('display_symbol')['absAllocation'].sum().reset_index().sort_values('absAllocation', ascending=False)
        
        fig = px.pie(plot_df, values='absAllocation', names='display_symbol', 
                     title='📊 Portfolio Allocation (By Market Exposure)',
                     hole=0.45,
                     color_discrete_sequence=px.colors.qualitative.Pastel)
        
        fig.update_traces(
            textinfo='percent+label',
            textposition='outside',
            insidetextorientation='radial',
            marker=dict(line=dict(color='#0a0a0a', width=2))
        )
        
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='#0a0a0a',
            plot_bgcolor='#0a0a0a',
            font=dict(family="Inter, system-ui, sans-serif", size=11, color="#e2e8f0"),
            title=dict(x=0.5, font=dict(size=18, color="#f8fafc")),
            legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.1),
            margin=dict(t=80, b=40, l=40, r=150),
            showlegend=True
        )
        
        return fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True})

    async def get_risk_analysis(self) -> str:
        data = await self._get_enriched_portfolio()
        if not data: return "<div>No hay datos en el portafolio</div>"
        
        df = pd.DataFrame(data)
        # Sector Exposure (Absolute)
        sector_df = df.groupby('sector')['absAllocation'].sum().reset_index()
        
        fig = px.bar(sector_df, x='sector', y='absAllocation', 
                     title='🛡️ Risk Analysis: Sector Exposure',
                     color='absAllocation',
                     color_continuous_scale='Viridis')
        
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='#0a0a0a',
            plot_bgcolor='#0a0a0a',
            xaxis_title="Sector",
            yaxis_title="Total Exposure ($)",
            font=dict(family="Inter, system-ui, sans-serif", size=11),
            title=dict(x=0.5, font=dict(size=18)),
            margin=dict(t=80, b=40, l=60, r=40)
        )
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    async def get_pnl_performance(self) -> str:
        data = await self._get_enriched_portfolio()
        if not data: return "<div>No hay datos en el portafolio</div>"
        
        df = pd.DataFrame(data)
        df['color'] = df['pnl'].apply(lambda x: 'Profit' if x >= 0 else 'Loss')
        
        fig = px.bar(df, x='symbol', y='pnl', 
                     title='📈 Unrealized PnL Performance',
                     color='color',
                     color_discrete_map={'Profit': '#26a69d', 'Loss': '#ef5350'},
                     hover_data=['pnlPct', 'currentValue'])
        
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='#0a0a0a',
            plot_bgcolor='#0a0a0a',
            xaxis_title="Ticker",
            yaxis_title="Unrealized PnL ($)",
            font=dict(family="Inter, system-ui, sans-serif", size=11),
            title=dict(x=0.5, font=dict(size=18)),
            margin=dict(t=80, b=40, l=60, r=40)
        )
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    async def get_3d_risk_return(self) -> str:
        data = await self._get_enriched_portfolio()
        if not data: return "<div style='color:#94a3b8; text-align:center; padding:40px; font-family:sans-serif;'>📊 No hay datos en el portafolio para gráficos 3D</div>"
        
        df = pd.DataFrame(data)
        if len(df) == 0:
            return "<div>Portafolio vacío</div>"
            
        df['color'] = df['pnl'].apply(lambda x: 'Profit' if x >= 0 else 'Loss')
        
        # Usamos absAllocation para el tamaño de las esferas
        max_alloc = df['absAllocation'].max() if not df['absAllocation'].empty else 1
        # Normalizamos tamaño de esferas
        df['bubble_size'] = df['absAllocation'].apply(lambda x: max(2, (x / max_alloc) * 40) if max_alloc > 0 else 10)
        
        fig = px.scatter_3d(
            df, 
            x='costBasis', 
            y='pnlPct', 
            z='currentValue',
            color='color',
            color_discrete_map={'Profit': '#10b981', 'Loss': '#ef4444'},
            size='bubble_size',
            size_max=45,
            hover_name='symbol',
            hover_data={'costBasis': ':.2f', 'pnlPct': ':.2f', 'shares': True, 'pnl': ':.2f', 'absAllocation': ':.2f', 'bubble_size': False, 'color': False},
            title=''
        )
        
        fig.update_layout(
            title=dict(
                text='🌌 3D QUANT FIN LANDSCAPE: Cost vs Return vs Exposure',
                x=0.5, font=dict(size=18, color="#f8fafc", family="Inter")
            ),
            template='plotly_dark',
            paper_bgcolor='#0a0a0a',
            plot_bgcolor='#0a0a0a',
            font=dict(family="Inter, system-ui, sans-serif", size=11, color="#94a3b8"),
            margin=dict(t=80, b=10, l=10, r=10),
            scene=dict(
                xaxis_title='Cost Basis ($)',
                yaxis_title='Return (PnL %)',
                zaxis_title='Exposure ($)',
                xaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(255,255,255,0.01)', showbackground=True),
                yaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(255,255,255,0.01)', showbackground=True),
                zaxis=dict(gridcolor='rgba(255,255,255,0.05)', backgroundcolor='rgba(255,255,255,0.01)', showbackground=True),
            ),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        )

        # Summary
        n_profit = len(df[df['pnl'] >= 0])
        n_loss = len(df[df['pnl'] < 0])
        total_pnl = df['pnl'].sum()
        best = df.loc[df['pnlPct'].idxmax()]
        worst = df.loc[df['pnlPct'].idxmin()]
        win_rate = (n_profit / len(df)) * 100
        
        summary = (
            f"<b>🌍 PAISAJE CONVEXO DEL PORTAFOLIO (3D Risk-Return)</b><br><br>"
            f"<b>Resumen de Exposiciones:</b> {len(df)} Posiciones Activas  |  PnL Neto: <b>${total_pnl:+,.2f}</b><br>"
            f"<b>Win Rate (Hit Ratio):</b> {win_rate:.1f}% ({n_profit} Ganadoras / {n_loss} Perdedoras)<br>"
            f"<b>Mejor Contribución:</b> {best['symbol']} ({best['pnlPct']:+.1f}% | ${best['pnl']:+,.2f})<br>"
            f"<b>Peor Detractor:</b> {worst['symbol']} ({worst['pnlPct']:+.1f}% | ${worst['pnl']:+,.2f})<br><br>"
            f"<b>💡 Interpretación Visual (Risk Management):</b><br>"
            f"• <b>Concentración de Riesgo (Eje Z):</b> Burbujas grandes indican donde está concentrado tu capital bruto.<br>"
            f"• <b>Retorno (Eje Y):</b> Burbujas altas contribuyen Alpha. Burbujas bajas detraen valor.<br>"
            f"• <i>Red Flag:</i> Si ves una burbuja GRANDE (mucha exposición) en la parte BAJA (grandes pérdidas),<br>"
            f"  ese activo representa un riesgo sistémico para el portafolio. Considera aplicar stop-losses."
        )
        fig.add_annotation(
            text=summary, x=0.01, y=0.99, xref='paper', yref='paper',
            showarrow=False, align='left', font=dict(size=11, color='#cbd5e1', family='Inter'),
            bgcolor='rgba(15,23,42,0.85)', bordercolor='rgba(99,102,241,0.5)',
            borderwidth=1, borderpad=10,
        )

        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    async def get_returns_distribution(self) -> str:
        data = await self._get_enriched_portfolio()
        if not data: return "<div style='color:#94a3b8; text-align:center; padding:40px;'>📊 No hay datos para distribución de retornos</div>"
        
        df = pd.DataFrame(data)
        if len(df) == 0:
            return "<div>Portafolio vacío</div>"

        # Histogram of PnL Percentages
        fig = px.histogram(
            df,
            x='pnlPct',
            nbins=15,
            title='📊 QUANTITATIVE: PnL Returns Distribution',
            color_discrete_sequence=['#3b82f6'],
            opacity=0.8,
            marginal="box" # adds a boxplot at the top showing outliers and quartiles
        )
        
        # Add a vertical line at 0 for profitability threshold
        fig.add_vline(x=0, line_width=2, line_dash="dash", line_color="#ef4444")

        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='#0a0a0a',
            plot_bgcolor='#0a0a0a',
            xaxis_title="Return (PnL %)",
            yaxis_title="Asset Count (Frequency)",
            font=dict(family="Inter, system-ui, sans-serif", size=11, color="#94a3b8"),
            title=dict(x=0.5, font=dict(size=18, color="#f8fafc")),
            margin=dict(t=80, b=40, l=60, r=40),
            showlegend=False
        )

        # Distribution stats
        mean_pnl = df['pnlPct'].mean()
        median_pnl = df['pnlPct'].median()
        std_pnl = df['pnlPct'].std()
        pct_positive = (df['pnlPct'] > 0).sum() / len(df) * 100
        skewness = df['pnlPct'].skew()
        
        skew_text = "Asimetría Positiva" if skewness > 0 else "Asimetría Negativa"
        
        summary = (
            f"<b>📊 DISTRIBUCIÓN ESTADÍSTICA DE RETORNOS LATENTES</b><br><br>"
            f"<b>Tendencia Central:</b> Media = {mean_pnl:+.2f}%  |  Mediana = {median_pnl:+.2f}%<br>"
            f"<b>Dispersión (Cross-sectional Vol):</b> Desviación Estándar = {std_pnl:.2f}%<br>"
            f"<b>Perfil (Skewness):</b> {skewness:.2f} ({skew_text})<br><br>"
            f"<b>💡 Insights de Optimización:</b><br>"
            f"• El <b>{pct_positive:.0f}%</b> de tus posiciones están en profit. Históricamente, en estrategias Momentum, una asimetría positiva<br>"
            f"  (Skew > 0) significa que dejas correr las ganancias ('let winners ride') y las pérdidas están acotadas.<br>"
            f"• Si ves una cola gorda a la izquierda (Skew < 0), estás cortando las ganancias demasiado pronto<br>"
            f"  y sosteniendo perdedores masivos ('bagholding'). Revisa tu disciplina de Stop Loss."
        )
        fig.add_annotation(
            text=summary, x=0.5, y=-0.18, xref='paper', yref='paper',
            showarrow=False, align='center', font=dict(size=11, color='#cbd5e1', family='Inter'),
            bgcolor='rgba(15,23,42,0.9)', bordercolor='rgba(99,102,241,0.5)',
            borderwidth=1, borderpad=10,
        )
        
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    async def get_equity_curve(self) -> str:
        history = self.repo.get_equity_history()
        if not history: 
            return "<div style='color:#94a3b8; text-align:center; padding:40px; font-family:sans-serif;'>📊 No hay suficiente historial de snapshots para generar la curva de equidad aún.</div>"
        
        df = pd.DataFrame(history)
        # Ensure 'time' is treated as seconds
        df['date'] = pd.to_datetime(df['time'], unit='s')
        df = df.sort_values('date')
        
        fig = go.Figure()
        
        # Realized Balance (The "Floor")
        fig.add_trace(go.Scatter(
            x=df['date'], y=df['realized'],
            name='Realized Balance',
            line=dict(color='#94a3b8', width=1, dash='dot'),
            hoverinfo='x+y',
            mode='lines'
        ))
        
        # Total Equity (The "Curve")
        fig.add_trace(go.Scatter(
            x=df['date'], y=df['total'],
            name='Total Equity',
            line=dict(color='#10b981', width=3),
            fill='tonexty', 
            fillcolor='rgba(16, 185, 129, 0.1)',
            hoverinfo='x+y',
            mode='lines+markers',
            marker=dict(size=4, color='#10b981')
        ))
        
        fig.update_layout(
            title=dict(
                text='📈 EVOLUCIÓN DEL EQUITY (HISTÓRICO)',
                x=0.5, font=dict(size=20, color="#f8fafc", family="Inter")
            ),
            template='plotly_dark',
            paper_bgcolor='#0a0a0a',
            plot_bgcolor='#0a0a0a',
            xaxis=dict(
                title="Fecha",
                gridcolor='rgba(255,255,255,0.05)',
                rangeslider=dict(visible=True, bgcolor='rgba(255,255,255,0.02)'),
                type='date',
                tickformat='%d %b\n%Y'
            ),
            yaxis=dict(
                title="Balance ($)",
                gridcolor='rgba(255,255,255,0.05)',
                side='right'
            ),
            font=dict(family="Inter, sans-serif", size=12),
            hovermode='x unified',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            margin=dict(t=100, b=40, l=40, r=60)
        )
        
        return fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True})
