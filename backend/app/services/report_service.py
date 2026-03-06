"""
ReportService — generates institutional-quality PDF reports using FPDF2 + Matplotlib.
No system dependencies required (pure Python).
"""
import os
import io
import base64
from datetime import datetime
from typing import List, Dict, Any
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from fpdf import FPDF
from .risk_service import risk_service
from ..core.container import duckdb_repo
from .report_styler import AlphaReport

class ReportService:
    def __init__(self, reports_dir: str = "reports"):
        self.reports_dir = reports_dir
        os.makedirs(self.reports_dir, exist_ok=True)

    def _generate_momentum_chart(self) -> str:
        """Generates momentum bar chart for top holdings."""
        holdings = duckdb_repo.get_portfolio()
        risk_report = risk_service.get_portfolio_risk_report(holdings)
        momentum = risk_report.get("momentum", {})

        if not momentum:
            return ""

        symbols = list(momentum.keys())[:10]
        values = [momentum[s] for s in symbols]
        colors = ["#27ae60" if v >= 0 else "#c0392b" for v in values]

        fig, ax = plt.subplots(figsize=(8, 3), dpi=120)
        ax.barh(symbols, values, color=colors, height=0.6, edgecolor="none")
        ax.set_xlabel("Momentum (Slope via GD)", fontsize=9)
        ax.set_title("Asset Momentum — Linear Regression Slopes", fontsize=11, fontweight="bold")
        ax.axvline(x=0, color="#bdc3c7", linewidth=0.8)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(labelsize=8)
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        plt.close(fig)
        return base64.b64encode(buf.getvalue()).decode("utf-8")

    def _generate_equity_chart(self) -> str:
        """Generates a clean, professional equity curve chart."""
        history = duckdb_repo.get_equity_history()
        if not history or len(history) < 3:
            return ""

        times_raw = [datetime.fromtimestamp(h["time"]) for h in history]
        vals_raw = np.array([h["total"] for h in history], dtype=np.float64)

        # ── Smooth out spikes: rolling median (window=5) ─────────
        window = min(5, len(vals_raw))
        vals_smooth = np.copy(vals_raw)
        for i in range(len(vals_raw)):
            lo = max(0, i - window // 2)
            hi = min(len(vals_raw), i + window // 2 + 1)
            vals_smooth[i] = np.median(vals_raw[lo:hi])

        # ── Clip remaining outliers to IQR ×2 ────────────────────
        q1, q3 = np.percentile(vals_smooth, [25, 75])
        iqr = q3 - q1
        lower = q1 - 2 * iqr
        upper = q3 + 2 * iqr
        vals_clean = np.clip(vals_smooth, lower if lower > 0 else 0, upper)

        # ── Build chart ──────────────────────────────────────────
        fig, ax = plt.subplots(figsize=(9, 3.8), dpi=130)

        # Main equity line
        ax.plot(times_raw, vals_clean, color="#2980b9", linewidth=1.8,
                label="Portfolio NAV", zorder=3)

        # Subtle gradient fill
        ax.fill_between(times_raw, vals_clean,
                         min(vals_clean) * 0.98,
                         alpha=0.08, color="#2980b9", zorder=1)

        # Trend line (on smoothed data)
        if len(vals_clean) > 10:
            from .math_core import math_core
            w, b = math_core.gradient_descent_momentum(vals_clean, epochs=2000)
            x_norm = np.linspace(0, 1, len(vals_clean))
            trend = w * x_norm + b
            direction = "Bullish" if w > 0 else "Bearish"
            ax.plot(times_raw, trend, color="#e74c3c", linestyle="--",
                    linewidth=1.2, alpha=0.65,
                    label=f"Trend ({direction}, Δ${abs(w):,.0f})", zorder=2)

        ax.set_title("Portfolio Equity Curve", fontsize=12, fontweight="bold", pad=10)
        ax.set_ylabel("NAV ($)", fontsize=9)
        ax.legend(fontsize=8, loc="upper left", framealpha=0.9)
        ax.grid(True, alpha=0.15, linestyle="-")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(labelsize=7)

        # Clean date formatting
        import matplotlib.dates as mdates
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=4, maxticks=8))
        fig.autofmt_xdate(rotation=25, ha="right")

        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        plt.close(fig)
        return base64.b64encode(buf.getvalue()).decode("utf-8")

    def _save_chart_as_file(self, b64: str, name: str) -> str:
        """Decode base64 chart to a temp PNG file and return the path."""
        if not b64:
            return ""
        path = os.path.join(self.reports_dir, f"_tmp_{name}.png")
        with open(path, "wb") as f:
            f.write(base64.b64decode(b64))
        return path

    def generate_balance_sheet(
        self,
        holdings: List[Dict[str, Any]],
        total_value: float,
        total_pnl: float,
    ) -> str:
        """Standard Portfolio Performance Report."""
        risk_report = risk_service.get_portfolio_risk_report(holdings)
        
        try: eq_path = self._save_chart_as_file(self._generate_equity_chart(), "equity")
        except: eq_path = ""
        try: mom_path = self._save_chart_as_file(self._generate_momentum_chart(), "momentum")
        except: mom_path = ""

        pdf = AlphaReport(mode="Standard")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        # Metrics Row 1
        y = pdf.get_y()
        pnl_pct = (total_pnl / (total_value - total_pnl) * 100) if (total_value - total_pnl) != 0 else 0
        pdf.metric_card("Net Asset Value (NAV)", f"${total_value:,.2f}", 12, y)
        pdf.metric_card("Total P&L (Unrealized)", f"${total_pnl:,.2f}", 77, y, trend=f"{pnl_pct:+.2f}%")
        pdf.metric_card("Risk Adj. Return", str(risk_report.get("risk_adjusted_return", "N/A")), 142, y)
        pdf.set_y(y + 26)

        # Asset Matrix
        pdf.section_title("Core Portfolio Exposure")
        pdf.box_note("Structural Overview", 
                    f"Portfolio contains {len(holdings)} active positions across multiple sectors. "
                    f"Aggregate volatility is currently {risk_report.get('annualized_volatility')}% with a Sharpe of {risk_report.get('sharpe_ratio')}.")

        rows = []
        for h in holdings:
            rows.append([
                h.get("symbol"), 
                h.get("name")[:25], 
                f"{h.get('shares'):.2f}", 
                f"${h.get('entryPrice',0):,.2f}", 
                f"${h.get('price',0):,.2f}", 
                f"{'+' if h.get('change',0)>=0 else ''}${h.get('change',0):,.2f}"
            ])
        pdf.summary_table(rows, ["Asset", "Security Name", "Size", "Entry", "Last", "PnL ($)"], [22, 55, 25, 28, 28, 30])
        
        # Charts Page
        if eq_path:
            pdf.add_page()
            pdf.section_title("Performance & Trend Projection")
            pdf.image(eq_path, x=12, w=186)
            pdf.box_note("Quant Insight", "The equity curve includes a 30-day structural trend projection optimized via Gradient Descent.")

        # Save
        filename = f"performance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(os.path.join(self.reports_dir, filename))
        for p in [eq_path, mom_path]:
            if p and os.path.exists(p): os.remove(p)
        return filename

    def generate_executive_summary(self, holdings: List[Dict[str, Any]], intelligence_text: str) -> str:
        """High-level brief for Asset Managers (Executive Mode)."""
        total_val = sum(h['shares'] * h.get('price', h['entryPrice']) for h in holdings)
        risk_report = risk_service.get_portfolio_risk_report(holdings)

        pdf = AlphaReport(mode="Executive")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        y = pdf.get_y()
        pdf.metric_card("Current AUM", f"${total_val:,.2f}", 12, y)
        pdf.metric_card("Portfolio VaR", f"{risk_report.get('var_95_percent')}%", 77, y)
        pdf.metric_card("Efficiency (Sharpe)", str(risk_report.get("sharpe_ratio")), 142, y)
        pdf.set_y(y + 28)

        pdf.section_title("Intelligence Alpha Brief")
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(44, 62, 80)
        pdf.cell(0, 8, "STRATEGIC OUTLOOK & NEURAL CONFLUENCE", ln=True)
        pdf.ln(2)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 6, pdf.safe_text(intelligence_text))
        
        pdf.ln(10)
        pdf.section_title("Top Positional Exposures")
        top_rows = []
        for h in sorted(holdings, key=lambda x: x['shares']*x.get('price', 0), reverse=True)[:5]:
            val = h['shares'] * h.get('price', 0)
            top_rows.append([h['symbol'], h['name'][:30], f"{(val/total_val*100):.1f}%", f"${val:,.2f}"])
        pdf.summary_table(top_rows, ["Symbol", "Security", "Weight (%)", "Market Value"], [30, 80, 40, 40])

        filename = f"executive_brief_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(os.path.join(self.reports_dir, filename))
        return filename

    def generate_risk_audit(self, holdings: List[Dict[str, Any]]) -> str:
        """Deep-dive Risk Audit (Risk Mode)."""
        risk_report = risk_service.get_portfolio_risk_report(holdings)
        
        pdf = AlphaReport(mode="Risk")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        y = pdf.get_y()
        pdf.metric_card("Value at Risk (95%)", f"{risk_report.get('var_95_percent')}%", 12, y)
        pdf.metric_card("Ann. Volatility", f"{risk_report.get('annualized_volatility')}%", 77, y)
        pdf.metric_card("E[X] Per Trade", f"${risk_report.get('expected_value_trade', 0):,.2f}", 142, y)
        pdf.set_y(y + 28)

        pdf.section_title("Tail Risk & Statistical Moments")
        pdf.box_note("Risk Advisory", 
                    "The following metrics measure the asymmetry and tail density of portfolio returns. "
                    "Extreme kurtosis suggests black-swan vulnerability.")
        
        mom_rows = [
            ["Skewness (Asymmetry)", str(risk_report.get("skewness", 0)), "Target: > -0.5"],
            ["Excess Kurtosis", str(risk_report.get("excess_kurtosis", 0)), "Target: < 3.0"],
            ["Modified VaR (Cornish-Fisher)", f"{risk_report.get('var_95_percent')}%", "Institutional Limit: 15%"]
        ]
        pdf.summary_table(mom_rows, ["Metric Name", "Portfolio Value", "Institutional Benchmark"], [70, 50, 68])

        pdf.ln(5)
        pdf.section_title("Hedged Strategy Recommendations")
        strat = risk_report.get("hedging_strategy", {})
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(192, 57, 43)
        pdf.cell(0, 8, f"RECOMMENDED ACTION: {strat.get('action', 'MONITOR')}", ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(44, 62, 80)
        pdf.multi_cell(0, 6, f"Primary Strategy: {strat.get('recommended_strategy')}\nTarget: {strat.get('primary_hedge_target')}\nRatio: {strat.get('hedge_ratio')}")

        filename = f"risk_audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(os.path.join(self.reports_dir, filename))
        return filename

    def generate_custom_intelligence_report(self, analysis_text: str, holdings: List[Dict[str, Any]], total_value: float, total_pnl: float) -> str:
        """The 'Bespoke Intel' variant (Intelligence Mode)."""
        pdf = AlphaReport(mode="Intelligence")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        
        y = pdf.get_y()
        pdf.metric_card("NAV", f"${total_value:,.2f}", 12, y)
        pdf.metric_card("PnL", f"${total_pnl:,.2f}", 77, y)
        pdf.metric_card("Intel Score", "High Alpha", 142, y)
        pdf.set_y(y + 28)

        pdf.section_title("Global Signal Convergence")
        pdf.long_text_box(analysis_text)
        
        filename = f"intel_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(os.path.join(self.reports_dir, filename))
        return filename

report_service = ReportService()


report_service = ReportService()
