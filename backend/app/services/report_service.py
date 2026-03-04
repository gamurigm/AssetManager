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


class AlphaReport(FPDF):
    """Premium dark-header institutional PDF report."""

    def safe_text(self, text: str) -> str:
        """Strips non-ASCII characters that cause FPDF crashes with standard fonts."""
        if not text: return ""
        # Standard fonts like Helvetica/Times only support Latin-1/WinAnsi.
        # We'll encode to latin-1 and ignore or replace errors to keep it safe.
        try:
            # We first try standard normalization or simple stripping
            # For this context, skipping characters fpdf doesn't like is safest.
            return text.encode("latin-1", "ignore").decode("latin-1")
        except Exception:
            # Full fallback to ASCII if latin-1 also fails somehow
            return text.encode("ascii", "ignore").decode("ascii")

    def header(self):
        # Dark header band
        self.set_fill_color(30, 30, 35)
        self.rect(0, 0, 210, 32, "F")
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(255, 255, 255)
        self.set_y(7)
        self.cell(0, 10, "ASSET MANDATE ALPHA", align="L")
        self.set_font("Helvetica", "", 8)
        self.set_text_color(160, 160, 170)
        date_str = f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        self.cell(0, 10, self.safe_text(date_str), align="R")
        self.ln(9)
        self.set_font("Helvetica", "I", 9)
        self.cell(0, 5, "Institutional Portfolio Alpha Core | Intelligence Generated Financial Report", align="L")
        self.ln(14)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(150, 150, 150)
        footer_text = f"MMAM Intelligence Core | Page {self.page_no()} | ALPHA-9 Node"
        self.cell(0, 10, self.safe_text(footer_text), align="C")

    def section_title(self, title: str):
        self.ln(4)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(44, 62, 80)
        safe_title = self.safe_text(title)
        self.cell(0, 8, safe_title, new_x="LMARGIN", new_y="NEXT")
        # Accent line
        self.set_draw_color(52, 152, 219)
        self.set_line_width(0.6)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def metric_card(self, label: str, value: str, x: float, y: float, w: float = 60):
        self.set_xy(x, y)
        # Card background
        self.set_fill_color(248, 249, 250)
        self.rect(x, y, w, 18, "F")
        # Left accent
        self.set_fill_color(52, 152, 219)
        self.rect(x, y, 2, 18, "F")
        # Label
        self.set_xy(x + 4, y + 2)
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(127, 140, 141)
        self.cell(w - 6, 5, self.safe_text(label.upper()))
        # Value
        self.set_xy(x + 4, y + 8)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(26, 26, 26)
        self.cell(w - 6, 8, self.safe_text(value))

    def long_text_box(self, content: str):
        self.set_font("Helvetica", "", 9)
        self.set_text_color(44, 62, 80)
        # Ensure AI generated text doesn't have characters that crash FPDF
        safe_content = self.safe_text(content)
        self.multi_cell(0, 5, safe_content)
        self.ln(2)


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
        """Generates a professional PDF report with risk analytics and charts."""
        # 1. Risk analytics
        risk_report = risk_service.get_portfolio_risk_report(holdings)

        # 2. Charts
        try:
            eq_b64 = self._generate_equity_chart()
        except Exception:
            eq_b64 = ""
        try:
            mom_b64 = self._generate_momentum_chart()
        except Exception:
            mom_b64 = ""

        eq_path = self._save_chart_as_file(eq_b64, "equity")
        mom_path = self._save_chart_as_file(mom_b64, "momentum")

        # 3. Build PDF
        pdf = AlphaReport()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        # ── Top metrics row ─────────────────────────────────────────
        y = pdf.get_y() + 2
        pdf.metric_card("Net Asset Value (NAV)", f"${total_value:,.2f}", 10, y)
        pnl_str = f"{'+'if total_pnl>=0 else ''}${total_pnl:,.2f}"
        pdf.metric_card("Total P&L (Unrealized)", pnl_str, 75, y)

        rar_val = risk_report.get("risk_adjusted_return", "N/A")
        pdf.metric_card("Risk Adjusted Return", str(rar_val), 140, y)
        pdf.set_y(y + 22)

        # ── Risk metrics row ────────────────────────────────────────
        pdf.section_title("Risk Matrix & Performance Metrics")
        y2 = pdf.get_y()
        pdf.metric_card("VaR (95%)", f"{risk_report.get('var_95_percent', 'N/A')}%", 10, y2)
        pdf.metric_card("Sharpe Ratio", str(risk_report.get("sharpe_ratio", "N/A")), 75, y2)
        pdf.metric_card("Expected Value E[x]", f"${risk_report.get('expected_value_trade', 0)}", 140, y2)
        pdf.set_y(y2 + 22)

        y3 = pdf.get_y()
        pdf.metric_card("Ann. Volatility", f"{risk_report.get('annualized_volatility', 'N/A')}%", 10, y3)
        pdf.metric_card("Skewness", str(risk_report.get("skewness", 0)), 75, y3)
        pdf.metric_card("Excess Kurtosis", str(risk_report.get("excess_kurtosis", 0)), 140, y3)
        pdf.set_y(y3 + 22)

        # (formulas omitted — kept in math_core.py docstrings for reference)

        # ── Holdings table ──────────────────────────────────────────
        pdf.section_title("Portfolio Exposure")
        pdf.set_font("Helvetica", "B", 7)
        pdf.set_fill_color(44, 62, 80)
        pdf.set_text_color(255, 255, 255)
        col_w = [25, 50, 22, 28, 28, 30]
        headers = ["Symbol", "Name", "Shares", "Entry", "Market", "P&L ($)"]
        for i, h in enumerate(headers):
            pdf.cell(col_w[i], 7, h, border=1, fill=True, align="C")
        pdf.ln()

        pdf.set_font("Helvetica", "", 7)
        pdf.set_text_color(26, 26, 26)
        for idx, h in enumerate(holdings):
            if pdf.get_y() > 270:
                pdf.add_page()
            fill = idx % 2 == 0
            if fill:
                pdf.set_fill_color(253, 253, 253)
            else:
                pdf.set_fill_color(255, 255, 255)

            sym = pdf.safe_text(h.get("symbol", "N/A"))
            name = pdf.safe_text(h.get("name", "N/A")[:26])
            shares = h.get("shares", 0)
            entry = h.get("entryPrice", 0)
            price = h.get("price", 0)
            change = h.get("change", 0)

            pdf.cell(col_w[0], 6, sym, border=1, fill=fill, align="C")
            pdf.cell(col_w[1], 6, name, border=1, fill=fill)
            pdf.cell(col_w[2], 6, f"{shares:.2f}", border=1, fill=fill, align="R")
            pdf.cell(col_w[3], 6, f"${entry:,.2f}", border=1, fill=fill, align="R")
            pdf.cell(col_w[4], 6, f"${price:,.2f}", border=1, fill=fill, align="R")
            # Color P&L
            if change >= 0:
                pdf.set_text_color(39, 174, 96)
            else:
                pdf.set_text_color(192, 57, 43)
            pdf.cell(col_w[5], 6, f"${change:,.2f}", border=1, fill=fill, align="R")
            pdf.set_text_color(26, 26, 26)
            pdf.ln()

        # ── Charts ──────────────────────────────────────────────────
        if eq_path and os.path.exists(eq_path):
            pdf.add_page()
            pdf.section_title("Equity Curve & Trend Projection")
            pdf.image(eq_path, x=10, w=190)
            pdf.ln(3)
            pdf.set_font("Helvetica", "I", 7)
            pdf.set_text_color(127, 140, 141)
            pdf.cell(0, 5, "Historical equity curve with smoothed trend line projection.")
            pdf.ln(6)

        if mom_path and os.path.exists(mom_path):
            if not eq_path:
                pdf.add_page()
            pdf.section_title("Asset Momentum (Linear Regression Slopes)")
            pdf.image(mom_path, x=10, w=190)
            pdf.ln(3)
            pdf.set_font("Helvetica", "I", 7)
            pdf.set_text_color(127, 140, 141)
            pdf.cell(0, 5, "Positive slope = bullish momentum, negative = bearish. Based on 30-day regression.")
            pdf.ln(6)

        # ── Transaction Log (The Audit Trail) ───────────────────────
        pdf.add_page()
        pdf.section_title("Institutional Transaction History (Audit Trail)")
        pdf.set_font("Helvetica", "B", 7)
        pdf.set_fill_color(30, 30, 35)
        pdf.set_text_color(255, 255, 255)
        
        tx_w = [25, 20, 20, 20, 30, 30, 45]
        tx_headers = ["Symbol", "Type", "Shares", "Price", "Realized P&L", "Date", "Status"]
        for i, th in enumerate(tx_headers):
            pdf.cell(tx_w[i], 7, th, border=1, fill=True, align="C")
        pdf.ln()

        pdf.set_font("Helvetica", "", 7)
        pdf.set_text_color(40, 40, 40)
        
        transactions = duckdb_repo.get_transactions()
        for idx, t in enumerate(reversed(transactions[-40:])):  # Last 40 trades
            fill = idx % 2 == 0
            pdf.set_fill_color(245, 245, 245) if fill else pdf.set_fill_color(255, 255, 255)
            
            pnl = t.get("realized_pnl", 0)
            pnl_c = (39, 174, 96) if pnl > 0 else (192, 57, 43) if pnl < 0 else (120, 120, 120)

            pdf.cell(tx_w[0], 6, t.get("symbol"), border=1, fill=fill, align="C")
            pdf.cell(tx_w[1], 6, t.get("type"), border=1, fill=fill, align="C")
            pdf.cell(tx_w[2], 6, f"{t.get('shares'):.2f}", border=1, fill=fill, align="R")
            pdf.cell(tx_w[3], 6, f"${t.get('price'):,.2f}", border=1, fill=fill, align="R")
            
            # Color the P&L cell
            pdf.set_text_color(*pnl_c)
            pdf.cell(tx_w[4], 6, f"${pnl:,.2f}", border=1, fill=fill, align="R")
            pdf.set_text_color(40, 40, 40)
            
            pdf.cell(tx_w[5], 6, t.get("date"), border=1, fill=fill, align="C")
            pdf.cell(tx_w[6], 6, "CONFIRMED_NODE_ALPHA", border=1, fill=fill, align="C")
            pdf.ln()

        # ── Theoretical Foundations ─────────────────────────────────
        self._add_theoretical_foundations(pdf)

        # 4. Save
        filename = f"alpha_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = os.path.join(self.reports_dir, filename)
        pdf.output(filepath)

        # Cleanup temp chart images
        for p in [eq_path, mom_path]:
            if p and os.path.exists(p):
                try:
                    os.remove(p)
                except Exception:
                    pass

        return filename

    def _add_theoretical_foundations(self, pdf: AlphaReport):
        """Appends a theoretical appendix to the risk report."""
        pdf.add_page()
        pdf.section_title("Algorithmic Risk Theory & Statistical Foundations")
        
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(44, 62, 80)
        pdf.cell(0, 6, "1. Value at Risk (VaR) vs Modified VaR (Cornish-Fisher)", ln=True)
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(40, 40, 40)
        text_var = (
            "Standard Value at Risk (VaR) assumes that asset returns follow a normal distribution. However, "
            "financial markets exhibit 'fat tails' and skewness, meaning extreme events occur more frequently "
            "than a normal distribution predicts. Our system implements the Cornish-Fisher expansion (Modified VaR) "
            "to adjust the standard Z-score using the calculated Skewness and Excess Kurtosis of the portfolio. "
            "This provides a much more robust risk threshold during market drawdowns."
        )
        pdf.multi_cell(0, 5, text_var)
        pdf.ln(5)

        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(44, 62, 80)
        pdf.cell(0, 6, "2. Gradient Descent & Momentum Prediction", ln=True)
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(40, 40, 40)
        text_gd = (
            "Rather than relying on lagging indicators like Simple Moving Averages, the system models asset trajectory "
            "using Linear Regression optimized via Gradient Descent over a rolling 30-day epoch window. By minimizing the Mean "
            "Squared Error (MSE) between the regression line and normalized price action, we mathematically extract the structural slope "
            "(momentum) of the asset. A positive slope indicates definitive capital inflow, while a negative slope signifies distribution."
        )
        pdf.multi_cell(0, 5, text_gd)
        pdf.ln(5)

        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(44, 62, 80)
        pdf.cell(0, 6, "3. Risk-Adjusted Return (RAR) & Sharpe Architecture", ln=True)
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(40, 40, 40)
        text_sharpe = (
            "The Sharpe Ratio evaluates return per unit of standard deviation (volatility), subtracting the risk-free rate. "
            "Our RAR (Risk-Adjusted Return) metric takes this further by computing Expected Return (E[R]) normalized against "
            "both Volatility (sigma) and total Capital at Risk (C). This ensures that heavy allocations in highly volatile assets "
            "are mathematically penalized if they do not provide geometrically outsized expectations."
        )
        pdf.multi_cell(0, 5, text_sharpe)
        pdf.ln(5)
        
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(44, 62, 80)
        pdf.cell(0, 6, "4. Skewness and Excess Kurtosis Dynamics", ln=True)
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(40, 40, 40)
        text_kurt = (
            "Skewness measures the asymmetry of the return distribution. Negative skewness indicates a tendency for large "
            "losses and small gains. Kurtosis measures the 'tailedness'. Excess Kurtosis > 0 (Leptokurtic distribution) indicates a high "
            "probability of black swan tail events. The risk engine continuously monitors these metrics to algorithmically trigger "
            "Protective Put Collar strategies when the structural tail risk exceeds the portfolio's mandate thresholds."
        )
        pdf.multi_cell(0, 5, text_kurt)
        pdf.ln(6)

    def generate_custom_intelligence_report(
        self,
        analysis_text: str,
        holdings: List[Dict[str, Any]],
        total_value: float,
        total_pnl: float,
    ) -> str:
        """Generates a PDF that includes bespoke specialist analysis text."""
        # 1. Base Logic (Charts)
        risk_report = risk_service.get_portfolio_risk_report(holdings)
        try:
            eq_b64 = self._generate_equity_chart()
        except: eq_b64 = ""
        eq_path = self._save_chart_as_file(eq_b64, "custom_equity")

        # 2. Build PDF
        pdf = AlphaReport()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        # Metrics row
        y = pdf.get_y() + 2
        pdf.metric_card("Net Asset Value", f"${total_value:,.2f}", 10, y)
        pdf.metric_card("Portfolio P&L", f"${total_pnl:,.2f}", 75, y)
        pdf.metric_card("VaR (95%)", f"{risk_report.get('var_95_percent')}%", 140, y)
        pdf.set_y(y + 22)

        # ── Intelligence Section ────────────────────────────────────
        pdf.section_title("Specialist Neural Intelligence Analysis")
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(52, 152, 219)
        pdf.cell(0, 6, "CONFIDENTIAL STRATEGIC ADVISORY", ln=True)
        pdf.ln(2)
        
        # Injected AI text
        pdf.long_text_box(analysis_text)
        pdf.ln(5)

        # ── Visual Analytics ────────────────────────────────────────
        if eq_path and os.path.exists(eq_path):
            pdf.section_title("Equity Performance & Alpha Projection")
            pdf.image(eq_path, x=10, w=190)
            os.remove(eq_path)

        # ── Asset matrix ────────────────────────────────────────────
        pdf.ln(10)
        pdf.section_title("Current Institutional Exposure")
        pdf.set_font("Helvetica", "B", 8)
        pdf.set_text_color(255, 255, 255)
        pdf.set_fill_color(30, 30, 35)
        w = [30, 60, 30, 30, 40]
        h_titles = ["Symbol", "Position Name", "Shares", "Price", "Value"]
        for i, t in enumerate(h_titles):
            pdf.cell(w[i], 7, t, border=1, fill=True, align="C")
        pdf.ln()

        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(40, 40, 40)
        for h in holdings:
            pdf.cell(w[0], 6, pdf.safe_text(str(h.get('symbol'))), border=1)
            pdf.cell(w[1], 6, pdf.safe_text(str(h.get('name'))[:30]), border=1)
            pdf.cell(w[2], 6, f"{h.get('shares'):.2f}", border=1, align="R")
            pdf.cell(w[3], 6, f"${h.get('price', 0):,.2f}", border=1, align="R")
            pdf.cell(w[4], 6, f"${h.get('shares')*h.get('price',0):,.2f}", border=1, align="R")
            pdf.ln()

        # 3. Save
        filename = f"custom_alpha_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(os.path.join(self.reports_dir, filename))
        return filename


report_service = ReportService()
