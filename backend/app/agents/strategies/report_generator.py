import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
from typing import Dict, Any
from datetime import datetime

def generate_html_report(backtest_result: Any, output_path: str = "backtest_report.html"):
    """
    Generates a highly visual, comprehensive HTML report from a BacktestResult.
    Includes:
    - Equity Curve
    - Trade Outcome distribution
    - Bootstrap Net Profit Histogram (if available)
    - Bootstrap Drawdown Histogram (if available)
    - Key metrics summary panels
    """
    
    # 1. Extract data
    trades = backtest_result.trades
    kpis = backtest_result.kpis
    config = backtest_result.config
    bootstrap = backtest_result.bootstrap_stats
    
    initial_equity = config.account_size
    current_equity = initial_equity
    
    equity_curve = [initial_equity]
    trade_dates = ["Start"]
    
    wins = 0
    losses = 0
    for t in trades:
        current_equity += t.pnl_usd
        equity_curve.append(current_equity)
        trade_dates.append(t.exit_timestamp or "Unknown")
        if t.pnl_usd > 0:
            wins += 1
        elif t.pnl_usd < 0:
            losses += 1
            
    # 2. Setup Subplots
    has_bootstrap = bootstrap is not None and "net_profit_samples" in bootstrap
    
    if has_bootstrap:
        fig = make_subplots(
            rows=2, cols=2,
            specs=[[{"colspan": 2}, None],
                   [{}, {}]],
            subplot_titles=("Curva de Capital (Equity Curve)", 
                            "Distribucion Bootstrap: Retorno Neto", 
                            "Distribucion Bootstrap: Max Drawdown %"),
            vertical_spacing=0.15
        )
    else:
        fig = make_subplots(
            rows=1, cols=1,
            specs=[[{}]],
            subplot_titles=("Curva de Capital (Equity Curve)",)
        )

    # 3. Add Equity Curve
    fig.add_trace(
        go.Scatter(x=list(range(len(equity_curve))), y=equity_curve,
                   mode='lines+markers',
                   name='Equity',
                   line=dict(color='#00F0FF', width=3),
                   marker=dict(size=6, color='#00F0FF'),
                   fill='tozeroy',
                   fillcolor='rgba(0, 240, 255, 0.1)',
                   text=trade_dates,
                   hovertemplate="Trade: %{x}<br>Equity: $%{y:.2f}<br>Date: %{text}<extra></extra>"),
        row=1, col=1
    )

    # 4. Add Bootstrap Histograms if available
    if has_bootstrap:
        np_samples = bootstrap["net_profit_samples"]
        dd_samples = bootstrap["max_drawdown_samples"]
        np_ci = bootstrap.get("net_profit_95_ci", [0, 0])
        dd_ci = bootstrap.get("max_drawdown_95_ci_pct", [0, 0])

        # Net Profit Histogram
        fig.add_trace(
            go.Histogram(x=np_samples, marker_color='#00E676', opacity=0.7, name="Retorno Simulado",
                         nbinsx=50),
            row=2, col=1
        )
        # CI lines Net Profit
        fig.add_vline(x=np_ci[0], line_dash="dash", line_color="red", row=2, col=1, annotation_text="P2.5")
        fig.add_vline(x=np_ci[1], line_dash="dash", line_color="red", row=2, col=1, annotation_text="P97.5")
        
        # Max Drawdown Histogram
        fig.add_trace(
            go.Histogram(x=dd_samples, marker_color='#FF1744', opacity=0.7, name="Drawdown Simulado",
                         nbinsx=50),
            row=2, col=2
        )
        # CI lines Drawdown
        fig.add_vline(x=dd_ci[0], line_dash="dash", line_color="yellow", row=2, col=2, annotation_text="P2.5")
        fig.add_vline(x=dd_ci[1], line_dash="dash", line_color="yellow", row=2, col=2, annotation_text="P97.5")

    # 5. Styling and Layout
    fig.update_layout(
        title=dict(
            text=f"Reporte de Backtest: {config.strategy_name} ({config.symbol})",
            font=dict(size=24, color='white'),
            x=0.5
        ),
        template="plotly_dark",
        plot_bgcolor='#1E1E2E',
        paper_bgcolor='#1E1E2E',
        showlegend=False,
        height=800 if has_bootstrap else 500,
        margin=dict(t=120, b=50, l=50, r=50)
    )

    # 6. HTML generation with KPI boxes
    plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    win_rate = f"{kpis.win_rate*100:.1f}%" if kpis.total_trades > 0 else "0%"
    
    bootstrap_html = ""
    if has_bootstrap:
        bootstrap_html = f"""
        <div class="kpi-panel">
            <h2>Estadisticas de Bootstrap ({bootstrap['iterations']} iteraciones)</h2>
            <div class="kpi-grid">
                <div class="kpi-card">
                    <span class="label">Net Profit (95% CI)</span>
                    <span class="value">${np_ci[0]:.2f}  a  ${np_ci[1]:.2f}</span>
                </div>
                <div class="kpi-card">
                    <span class="label">Max Drawdown (95% CI)</span>
                    <span class="value">{dd_ci[0]:.2f}%  a  {dd_ci[1]:.2f}%</span>
                </div>
            </div>
        </div>
        """

    net_profit_usd = kpis.final_equity - initial_equity
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Backtest Analysis | {config.symbol}</title>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
        <style>
            :root {{
                --bg-color: #0c0c14;
                --card-bg: rgba(30, 30, 46, 0.7);
                --accent-primary: #00f0ff;
                --accent-secondary: #7000ff;
                --text-main: #e0e0e0;
                --text-dim: #a0a0b0;
                --success: #00e676;
                --danger: #ff1744;
                --warning: #ffd600;
            }}

            body {{
                background-color: var(--bg-color);
                background-image: 
                    radial-gradient(circle at 20% 20%, rgba(112, 0, 255, 0.05) 0%, transparent 40%),
                    radial-gradient(circle at 80% 80%, rgba(0, 240, 255, 0.05) 0%, transparent 40%);
                color: var(--text-main);
                font-family: 'Outfit', sans-serif;
                margin: 0;
                padding: 40px 20px;
                line-height: 1.6;
            }}

            .container {{
                max-width: 1400px;
                margin: 0 auto;
            }}

            header {{
                margin-bottom: 40px;
                text-align: left;
                border-left: 5px solid var(--accent-primary);
                padding-left: 20px;
            }}

            header h1 {{
                margin: 0;
                font-size: 2.5rem;
                font-weight: 700;
                letter-spacing: -1px;
                background: linear-gradient(90deg, #fff, var(--accent-primary));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}

            header p {{
                margin: 5px 0 0;
                color: var(--text-dim);
                font-size: 1.1rem;
            }}

            .section-title {{
                font-size: 1.2rem;
                font-weight: 600;
                color: var(--text-dim);
                text-transform: uppercase;
                letter-spacing: 2px;
                margin: 40px 0 20px;
                display: flex;
                align-items: center;
            }}

            .section-title::after {{
                content: "";
                flex: 1;
                height: 1px;
                background: rgba(255,255,255,0.1);
                margin-left: 20px;
            }}

            .kpi-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }}

            .kpi-card {{
                background: var(--card-bg);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-radius: 16px;
                padding: 24px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                position: relative;
                overflow: hidden;
            }}

            .kpi-card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
                border-color: rgba(0, 240, 255, 0.2);
            }}

            .kpi-card::before {{
                content: "";
                position: absolute;
                top: 0;
                left: 0;
                width: 4px;
                height: 100%;
                background: var(--accent-primary);
            }}

            .kpi-card.success::before {{ background: var(--success); }}
            .kpi-card.danger::before {{ background: var(--danger); }}
            .kpi-card.warning::before {{ background: var(--warning); }}
            .kpi-card.purple::before {{ background: var(--accent-secondary); }}

            .label {{
                font-size: 0.85rem;
                color: var(--text-dim);
                text-transform: uppercase;
                font-weight: 600;
                margin-bottom: 8px;
                display: block;
            }}

            .value {{
                font-size: 2.2rem;
                font-weight: 700;
                color: #fff;
            }}

            .sub-value {{
                font-size: 0.9rem;
                color: var(--text-dim);
                margin-top: 4px;
            }}

            .chart-container {{
                background: var(--card-bg);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 20px;
                border: 1px solid rgba(255, 255, 255, 0.05);
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
                margin-bottom: 40px;
            }}

            .summary-footer {{
                text-align: center;
                margin-top: 60px;
                color: var(--text-dim);
                font-size: 0.9rem;
                padding-bottom: 40px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>Backtest Analysis: {config.symbol}</h1>
                <p>Strategy: {config.strategy_name} | Period: {config.start_date} to {config.end_date}</p>
            </header>

            <div class="section-title">Performance Metrics</div>
            <div class="kpi-grid">
                <div class="kpi-card success">
                    <span class="label">Net Profit</span>
                    <span class="value">${net_profit_usd:,.2f}</span>
                    <span class="sub-value">Total Return on Capital</span>
                </div>
                <div class="kpi-card">
                    <span class="label">Win Rate</span>
                    <span class="value">{kpis.win_rate*100:.1f}%</span>
                    <span class="sub-value">{kpis.wins} Wins / {kpis.losses} Losses</span>
                </div>
                <div class="kpi-card danger">
                    <span class="label">Max Drawdown</span>
                    <span class="value">{kpis.max_drawdown_pct:.2f}%</span>
                    <span class="sub-value">Peak to Trough</span>
                </div>
                <div class="kpi-card purple">
                    <span class="label">Profit Factor</span>
                    <span class="value">{kpis.profit_factor:.2f}</span>
                    <span class="sub-value">Σ Gross Profit / Σ Gross Loss</span>
                </div>
                <div class="kpi-card warning">
                    <span class="label">Expectancy</span>
                    <span class="value">{kpis.expectancy_r:.2f}R</span>
                    <span class="sub-value">Average result per trade</span>
                </div>
                <div class="kpi-card">
                    <span class="label">Sharpe Ratio</span>
                    <span class="value">{kpis.sharpe_ratio:.2f}</span>
                    <span class="sub-value">Risk-Adjusted Return</span>
                </div>
            </div>

            {f'''
            <div class="section-title">Bootstrap Statistical Analysis (Monte Carlo)</div>
            <div class="kpi-grid">
                <div class="kpi-card success">
                    <span class="label">Net Profit (95% CI)</span>
                    <span class="value">${bootstrap['net_profit_95_ci'][0]:,.0f} - ${bootstrap['net_profit_95_ci'][1]:,.0f}</span>
                    <span class="sub-value">Probable range after {bootstrap['iterations']} iterations</span>
                </div>
                <div class="kpi-card danger">
                    <span class="label">Drawdown (95% CI)</span>
                    <span class="value">{bootstrap['max_drawdown_95_ci_pct'][0]:,.2f}% - {bootstrap['max_drawdown_95_ci_pct'][1]:,.2f}%</span>
                    <span class="sub-value">Statistical Drawdown Risk</span>
                </div>
            </div>
            ''' if has_bootstrap else ''}

            <div class="section-title">Visual Analysis</div>
            <div class="chart-container">
                {plot_html}
            </div>

            <div class="summary-footer">
                AssetManager v2.0 - Strategy Engine Output | Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            </div>
        </div>
    </body>
    </html>
    """

    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_template)
        
    return output_path
