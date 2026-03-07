import argparse
import sys
import os
from pathlib import Path
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

# Setup paths so we can import from backend
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.core.container import duckdb_repo
from app.services.math_core import math_core
from datetime import datetime, timedelta

def fetch_data(tickers: list, benchmark: str, lookback_days: int) -> pd.DataFrame:
    """Fetch history from DuckDB for tickers and benchmark."""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=lookback_days)
    
    conn = duckdb_repo._connect(read_only=True)
    all_data = {}
    
    symbols_to_fetch = list(set(tickers + [benchmark]))
    
    try:
        for sym in symbols_to_fetch:
            df = conn.execute(
                "SELECT date, close FROM ohlcv WHERE symbol = ? AND date >= ? ORDER BY date ASC", 
                [sym, start_date.date()]
            ).df()
            
            if not df.empty and len(df) > 10:
                df['returns'] = df['close'].pct_change().fillna(0)
                # Ensure date is sorted and set as index
                all_data[sym] = df.set_index('date')['returns']
            else:
                print(f"Warning: Not enough data for {sym}")
                
        if not all_data:
            return pd.DataFrame()
            
        returns_df = pd.DataFrame(all_data).fillna(0)
        return returns_df
        
    finally:
        conn.close()

def main():
    parser = argparse.ArgumentParser(description="Portfolio Factor Analysis (CAPM, PCA, Risk)")
    parser.add_argument('--tickers', type=str, required=True, help="Comma separated list of tickers (e.g. AAPL,MSFT,NVDA)")
    parser.add_argument('--benchmark', type=str, default='SPY', help="Benchmark for market proxy (default: SPY)")
    parser.add_argument('--days', type=int, default=252, help="Lookback period in days (default: 252)")
    parser.add_argument('--output', type=str, default='reports/factor_analysis.html', help="Output html file for charts")
    
    args = parser.parse_args()
    
    tickers = [t.strip().upper() for t in args.tickers.split(',')]
    benchmark = args.benchmark.upper()
    
    print(f"\n--- Starting Factor Analysis ---")
    print(f"Assets: {tickers}")
    print(f"Benchmark: {benchmark}\n")
    
    returns_df = fetch_data(tickers, benchmark, args.days)
    if returns_df.empty:
        print("Error: No data retrieved.")
        sys.exit(1)
        
    if benchmark not in returns_df.columns:
        print(f"Error: Market proxy {benchmark} missing from data.")
        sys.exit(1)
        
    valid_tickers = [t for t in tickers if t in returns_df.columns]
    market_returns = returns_df[benchmark].values
    
    # Calculate Metrics
    results = {}
    returns_dict = {t: returns_df[t].values for t in valid_tickers}
    
    for t in valid_tickers:
        asset_ret = returns_df[t].values
        beta, alpha, exp_ret = math_core.calculate_capm(asset_ret, market_returns)
        idio_risk = math_core.calculate_idiosyncratic_risk(asset_ret, market_returns)
        
        results[t] = {
            "Beta": beta,
            "Alpha (Daily)": alpha,
            "CAPM Exp. Return (Ann.)": exp_ret,
            "Idiosyncratic Risk (Ann.)": idio_risk
        }
        
    # PCA & Covariance
    pca_results = math_core.calculate_pca(returns_dict)
    _, cov_matrix = math_core.calculate_covariance_matrix(returns_dict)
    
    # Terminal Output
    print(f"{'Asset':<10} | {'Beta':<10} | {'Alpha(d)':<12} | {'Exp.Ret(a)':<12} | {'Idio.Risk(a)'}")
    print("-" * 65)
    for t, m in results.items():
        print(f"{t:<10} | {m['Beta']:<10.4f} | {m['Alpha (Daily)']:<12.6f} | {m['CAPM Exp. Return (Ann.)']:<12.4f} | {m['Idiosyncratic Risk (Ann.)']:.4f}")
        
    print("\n--- Principal Components ---")
    print(f"Components Explaining Variance:")
    for i, var in enumerate(pca_results['explained_variance']):
        print(f"PC{i+1}: {var*100:.2f}% (Cumulative: {pca_results['cumulative_variance'][i]*100:.2f}%)")
        
    # Plotting Output
    print(f"\nGenerating visual charts...")
    
    # 1. Covariance Heatmap
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=("Covariance Matrix (Annualized)", "PCA Scree Plot", "CAPM Regression (Sample)", "Risk/Return Profile"),
        specs=[[{"type": "heatmap"}, {"type": "xy"}], 
               [{"type": "xy"}, {"type": "xy"}]]
    )
    
    fig.add_trace(
        go.Heatmap(
            z=cov_matrix, x=pca_results['tickers'], y=pca_results['tickers'],
            colorscale='Viridis', showscale=True
        ), row=1, col=1
    )
    
    # 2. PCA Scree Plot
    x_pca = [f"PC{i+1}" for i in range(len(pca_results['eigenvalues']))]
    fig.add_trace(
        go.Bar(name='Explained Variance', x=x_pca, y=pca_results['explained_variance']),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(name='Cumulative Variance', x=x_pca, y=pca_results['cumulative_variance'], mode='lines+markers'),
        row=1, col=2
    )
    
    # 3. CAPM Regression (first asset vs market)
    sample_ticker = valid_tickers[0]
    fig.add_trace(
        go.Scatter(name=f'{sample_ticker} Returns', x=market_returns, y=returns_df[sample_ticker].values, mode='markers', marker=dict(opacity=0.5)),
        row=2, col=1
    )
    
    beta_s, alpha_s, _ = math_core.calculate_capm(returns_df[sample_ticker].values, market_returns)
    x_line = np.linspace(min(market_returns), max(market_returns), 10)
    y_line = beta_s * x_line + alpha_s
    fig.add_trace(
        go.Scatter(name='CAPM Best Fit', x=x_line, y=y_line, mode='lines', line=dict(color='red')),
        row=2, col=1
    )
    
    # 4. Risk / Return Scatter
    exp_returns = [results[t]['CAPM Exp. Return (Ann.)'] for t in valid_tickers]
    betas = [results[t]['Beta'] for t in valid_tickers]
    idio_risks = [results[t]['Idiosyncratic Risk (Ann.)'] for t in valid_tickers]
    
    fig.add_trace(
        go.Scatter(
            name='Assets',
            x=betas, 
            y=exp_returns, 
            mode='markers+text',
            text=valid_tickers,
            textposition="top center",
            marker=dict(size=12, color=idio_risks, colorscale='Plasma', showscale=True, colorbar=dict(title="Idiosyncratic Risk"))
        ), row=2, col=2
    )
    
    fig.update_layout(height=800, title_text=f"Factor & Portfolio Analytics (Benchmark: {benchmark})", showlegend=False)
    fig.update_xaxes(title_text="Beta", row=2, col=2)
    fig.update_yaxes(title_text="Expected Return", row=2, col=2)
    fig.update_xaxes(title_text=f"{benchmark} Returns", row=2, col=1)
    fig.update_yaxes(title_text=f"{sample_ticker} Returns", row=2, col=1)
    
    out_dir = Path(args.output).parent
    # Ensure relative paths work and directory exists
    if not out_dir.is_absolute():
        out_dir = Path(__file__).resolve().parent.parent / out_dir
        
    os.makedirs(out_dir, exist_ok=True)
    out_file = out_dir / Path(args.output).name
    
    fig.write_html(str(out_file))
    print(f"\nAnalysis complete! Visual report generated at: {out_file.absolute()}")

if __name__ == "__main__":
    main()
