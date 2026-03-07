from __future__ import annotations

import math
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from fpdf import FPDF


def _build_equity_curve(backtest_result: Any) -> tuple[list[str], list[float]]:
    trades = backtest_result.trades
    running_equity = float(backtest_result.config.account_size)
    labels = ["Start"]
    equity = [running_equity]

    for trade in trades:
        running_equity += float(trade.pnl_usd)
        labels.append(str(trade.exit_timestamp or trade.signal.timestamp))
        equity.append(running_equity)

    return labels, equity


def _save_equity_chart(backtest_result: Any, output_path: Path) -> None:
    _, equity = _build_equity_curve(backtest_result)
    x = list(range(len(equity)))

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(10, 4), dpi=180)
    ax.plot(x, equity, color="#22c55e", linewidth=2)
    ax.fill_between(x, equity, min(equity), color="#22c55e", alpha=0.14)
    ax.set_title(f"Equity Curve: {backtest_result.config.symbol}")
    ax.set_xlabel("Trade #")
    ax.set_ylabel("Equity")
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def _save_histogram(samples: Iterable[float], title: str, color: str, output_path: Path) -> None:
    values = list(samples)
    if not values:
        return

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(6, 4), dpi=180)
    bins = min(30, max(10, int(math.sqrt(len(values)))))
    ax.hist(values, bins=bins, color=color, alpha=0.82)
    ax.set_title(title)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


class BacktestPDF(FPDF):
    def header(self) -> None:
        self.set_fill_color(15, 23, 32)
        self.rect(0, 0, self.w, 18, style="F")
        self.set_xy(12, 6)
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(255, 255, 255)
        self.cell(0, 0, "AssetManager Backtest Report")

    def footer(self) -> None:
        self.set_y(-12)
        self.set_font("Helvetica", size=8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Page {self.page_no()}", align="R")


def _metric_card(pdf: BacktestPDF, x: float, y: float, width: float, height: float, label: str, value: str) -> None:
    pdf.set_fill_color(22, 28, 36)
    pdf.set_draw_color(52, 64, 78)
    pdf.rect(x, y, width, height, style="FD")
    pdf.set_xy(x + 4, y + 4)
    pdf.set_font("Helvetica", size=8)
    pdf.set_text_color(164, 178, 194)
    pdf.cell(width - 8, 4, label)
    pdf.set_xy(x + 4, y + 10)
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(width - 8, 6, value)


def _fmt_money(value: float) -> str:
    return f"${value:,.2f}"


def _fmt_ratio(value: float) -> str:
    if value == float("inf"):
        return "Inf"
    return f"{value:,.2f}"


def _fmt_pct_fraction(value: float) -> str:
    return f"{value * 100:,.2f}%"


def _add_trade_table(pdf: BacktestPDF, backtest_result: Any) -> None:
    pdf.add_page()
    pdf.set_xy(12, 24)
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 8, "Trades")

    columns = [
        ("Date", 35),
        ("Dir", 16),
        ("Entry", 24),
        ("Exit", 24),
        ("Outcome", 30),
        ("R", 16),
        ("PnL$", 24),
    ]
    row_height = 6

    def draw_header(y: float) -> float:
        pdf.set_xy(12, y)
        pdf.set_font("Helvetica", "B", 8)
        pdf.set_fill_color(24, 32, 44)
        pdf.set_text_color(255, 255, 255)
        for label, width in columns:
            pdf.cell(width, row_height + 1, label, border=1, align="C", fill=True)
        pdf.ln(row_height + 1)
        return y + row_height + 1

    current_y = draw_header(36)
    pdf.set_font("Helvetica", size=7)

    for trade in backtest_result.trades:
        if current_y > 275:
            pdf.add_page()
            pdf.set_xy(12, 24)
            pdf.set_font("Helvetica", "B", 14)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(0, 8, "Trades")
            current_y = draw_header(36)
            pdf.set_font("Helvetica", size=7)

        pdf.set_xy(12, current_y)
        pdf.set_text_color(228, 228, 228)
        values = [
            str(trade.exit_timestamp or trade.signal.timestamp).replace("T", " ")[:16],
            trade.signal.direction,
            f"{trade.signal.entry:,.2f}",
            f"{trade.exit_price:,.2f}",
            trade.outcome,
            f"{trade.pnl_r:,.2f}",
            f"{trade.pnl_usd:,.2f}",
        ]
        for (_, width), value in zip(columns, values):
            pdf.cell(width, row_height, value, border=1, align="C")
        pdf.ln(row_height)
        current_y += row_height


def generate_pdf_report(backtest_result: Any, output_path: str = "backtest_report.pdf") -> str:
    """Generate a PDF backtest report with KPIs, charts and trades."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    config = backtest_result.config
    kpis = backtest_result.kpis
    bootstrap = backtest_result.bootstrap_stats or {}
    net_profit = float(kpis.final_equity) - float(config.account_size)

    pdf = BacktestPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=14)
    pdf.add_page()

    pdf.set_xy(12, 24)
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 9, f"{config.symbol} | {config.strategy_name}")

    pdf.set_xy(12, 34)
    pdf.set_font("Helvetica", size=10)
    pdf.set_text_color(166, 181, 201)
    pdf.cell(0, 6, f"Period: {config.start_date} to {config.end_date}")
    pdf.ln(5)
    pdf.cell(0, 6, f"Initial capital: {_fmt_money(config.account_size)}   Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    cards = [
        ("Net Profit", _fmt_money(net_profit)),
        ("Final Equity", _fmt_money(kpis.final_equity)),
        ("Win Rate", _fmt_pct_fraction(kpis.win_rate)),
        ("Profit Factor", _fmt_ratio(kpis.profit_factor)),
        ("Max Drawdown", _fmt_pct_fraction(kpis.max_drawdown_pct)),
        ("Sharpe Ratio", _fmt_ratio(kpis.sharpe_ratio)),
    ]
    card_w = 58
    card_h = 20
    gap = 6
    top_y = 46

    for idx, (label, value) in enumerate(cards):
        row = idx // 3
        col = idx % 3
        _metric_card(pdf, 12 + col * (card_w + gap), top_y + row * (card_h + gap), card_w, card_h, label, value)

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)

        equity_chart = tmp_path / "equity.png"
        _save_equity_chart(backtest_result, equity_chart)

        pdf.set_xy(12, 96)
        pdf.set_font("Helvetica", "B", 13)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 8, "Equity Curve")
        pdf.image(str(equity_chart), x=12, y=104, w=186)

        if bootstrap:
            profit_ci = bootstrap.get("net_profit_95_ci", [0, 0])
            dd_ci = bootstrap.get("max_drawdown_95_ci_pct", [0, 0])

            profit_hist = tmp_path / "profit_hist.png"
            drawdown_hist = tmp_path / "drawdown_hist.png"
            _save_histogram(bootstrap.get("net_profit_samples", []), "Bootstrap Net Profit", "#22c55e", profit_hist)
            _save_histogram(bootstrap.get("max_drawdown_samples", []), "Bootstrap Max Drawdown", "#ef4444", drawdown_hist)

            pdf.add_page()
            pdf.set_xy(12, 24)
            pdf.set_font("Helvetica", "B", 14)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(0, 8, f"Bootstrap Analysis ({bootstrap.get('iterations', 0)} iterations)")
            pdf.set_xy(12, 34)
            pdf.set_font("Helvetica", size=10)
            pdf.set_text_color(166, 181, 201)
            pdf.cell(0, 6, f"Net profit 95% CI: {_fmt_money(profit_ci[0])} to {_fmt_money(profit_ci[1])}")
            pdf.ln(6)
            pdf.cell(0, 6, f"Max drawdown 95% CI: {dd_ci[0]:.2f}% to {dd_ci[1]:.2f}%")

            if profit_hist.exists():
                pdf.image(str(profit_hist), x=12, y=48, w=90)
            if drawdown_hist.exists():
                pdf.image(str(drawdown_hist), x=108, y=48, w=90)

    _add_trade_table(pdf, backtest_result)
    pdf.output(str(output))
    return str(output)