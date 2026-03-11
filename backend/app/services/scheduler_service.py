"""
Automated Background Intelligence — APScheduler-based tasks.
Runs periodic portfolio scans, risk checks, and generates alerts.
"""

import asyncio
import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.core.logging import logger
from app.core.container import duckdb_repo
from app.services.risk_service import risk_service
from app.services.crawler import crawler_service
from app.services.realtime_service import realtime_service
from app.services.ibkr_service import ibkr_service


# ──────────────────────────────────────────────
# 1. PORTFOLIO RISK SCANNER (every 60 min)
# ──────────────────────────────────────────────
async def run_portfolio_scan():
    """Scan all stored portfolios for concentration risk, bad Sharpe, or extreme kurtosis."""
    logger.info("[AutoScan] Starting automated portfolio risk scan...")
    try:
        holdings = duckdb_repo.get_portfolio()
        if not holdings:
            logger.info("[AutoScan] No holdings found — skipping scan.")
            return

        total_value = sum(h.get("shares", 0) * h.get("entryPrice", 0) for h in holdings)
        if total_value <= 0:
            logger.info("[AutoScan] Portfolio value is zero — skipping scan.")
            return

        alerts = []

        # ── Concentration Risk ──
        for h in holdings:
            weight = (h["shares"] * h["entryPrice"]) / total_value * 100
            if weight > 20:
                alerts.append(
                    f"CONCENTRATION: {h['symbol']} is {weight:.1f}% of portfolio (limit: 20%)"
                )

        # ── Pfaff Risk Metrics ──
        risk_report = risk_service.get_portfolio_risk_report(holdings)
        if "error" not in risk_report:
            sharpe = risk_report.get("sharpe_ratio", 0)
            kurtosis = risk_report.get("excess_kurtosis", 0)
            mvar = risk_report.get("mvar_95_percent", 0)

            if sharpe < 0:
                alerts.append(
                    f"NEGATIVE SHARPE: Annualized Sharpe is {sharpe:.2f} — portfolio is underperforming risk-free rate."
                )
            if kurtosis > 3:
                alerts.append(
                    f"HIGH KURTOSIS: Excess kurtosis is {kurtosis:.2f} — heavy-tail risk detected (fat tails)."
                )
            if mvar and float(str(mvar).replace("%", "")) > 3:
                alerts.append(
                    f"HIGH VaR: Modified VaR (95%) is {mvar}% — daily loss could exceed 3% of AUM."
                )
        else:
            alerts.append(f"Risk analysis unavailable: {risk_report.get('error')}")

        # ── Log Results ──
        if alerts:
            alert_text = "\n".join(alerts)
            logger.warning(f"[AutoScan] {len(alerts)} alert(s) detected:\n{alert_text}")
        else:
            logger.info("[AutoScan] Portfolio is healthy — no alerts.")

    except Exception as e:
        logger.error(f"[AutoScan] Error during scan: {e}")


# ──────────────────────────────────────────────
# 2. DAILY BRIEFING GENERATOR (every day 8:00 AM)
# ──────────────────────────────────────────────
async def generate_daily_briefing():
    """Generate a pre-market briefing using the Orchestrator."""
    logger.info("[DailyBrief] Generating morning briefing...")
    try:
        from app.agents.team.orchestrator import orchestrator

        holdings = duckdb_repo.get_portfolio()
        if not holdings:
            logger.info("[DailyBrief] No holdings — skipping briefing.")
            return

        symbols = [h["symbol"] for h in holdings[:10]]  # Top 10 holdings
        instruction = (
            f"AUTOMATED DAILY BRIEFING: Generate a concise pre-market analysis for these assets: "
            f"{', '.join(symbols)}. Include: 1) Key overnight news, 2) Technical levels to watch, "
            f"3) Any macro events today that could impact the portfolio. Keep it under 300 words."
        )

        result = await orchestrator.run(instruction)
        logger.info(f"[DailyBrief] Morning Briefing:\n{result}\n{'='*60}")

    except Exception as e:
        logger.error(f"[DailyBrief] Error: {e}")


# ──────────────────────────────────────────────
# 3. EQUITY CURVE SNAPSHOT (every 30 min during market hours)
# ──────────────────────────────────────────────
async def record_equity_snapshot():
    """Record a point on the equity curve for historical tracking."""
    try:
        holdings = duckdb_repo.get_portfolio()
        if not holdings:
            return

        # Use entry prices as a baseline (in production, we'd fetch live prices)
        total_equity = sum(h.get("shares", 0) * h.get("entryPrice", 0) for h in holdings)
        if total_equity > 0:
            duckdb_repo.record_equity_snapshot(total_equity)
            logger.info(f"[EquitySnap] Recorded equity snapshot: ${total_equity:,.2f}")

    except Exception as e:
        logger.error(f"[EquitySnap] Error: {e}")


# ──────────────────────────────────────────────
# SCHEDULER INITIALIZATION
# ──────────────────────────────────────────────
# ──────────────────────────────────────────────
# 4. REAL-TIME PRICE BROADCASTER (every 5-10 s)
# ──────────────────────────────────────────────
async def broadcast_prices_job(sio):
    """Broadcast prices for all active symbols to their respective Socket.IO rooms."""
    await realtime_service.broadcast_prices(sio)

scheduler = AsyncIOScheduler()

def start_scheduler(sio=None):
    """Start all background jobs."""

    # 1. Portfolio Risk Scan — every 60 minutes
    scheduler.add_job(
        run_portfolio_scan,
        "interval",
        minutes=60,
        id="portfolio_scan_hourly",
        replace_existing=True,
    )

    # 2. Daily Briefing — every weekday at 8:00 AM (local time)
    scheduler.add_job(
        generate_daily_briefing,
        "cron",
        day_of_week="mon-fri",
        hour=8,
        minute=0,
        id="daily_briefing",
        replace_existing=True,
    )

    # 3. Equity Snapshot — every 30 minutes during market hours (9:30–16:00 ET, weekdays)
    scheduler.add_job(
        record_equity_snapshot,
        "cron",
        day_of_week="mon-fri",
        hour="9-15",
        minute="*/30",
        id="equity_snapshot",
        replace_existing=True,
    )

    # 4. Background Crawler — Drip-fetch every 2 minutes
    scheduler.add_job(
        crawler_service.crawl_single_step,
        "interval",
        minutes=2,
        id="background_crawler_drip",
        replace_existing=True,
    )

    # 5. IBKR Keep-Alive (ensures connection stays active)
    scheduler.add_job(
        ibkr_service.connect,
        "interval",
        minutes=5,
        id="ibkr_keep_alive",
        replace_existing=True,
    )

    # 6. Run an initial scan 15 seconds after startup (for demo/testing)
    run_date = datetime.datetime.now() + datetime.timedelta(seconds=15)
    scheduler.add_job(
        run_portfolio_scan,
        "date",
        run_date=run_date,
        id="portfolio_scan_startup",
    )

    # 5. Fast Market Data Stream — Polls quotes for active socket rooms
    # Only fires for symbols that don't already have a fresh IBKR/Kafka tick.
    if sio:
        scheduler.add_job(
            broadcast_prices_job,
            "interval",
            seconds=5,
            args=[sio],
            id="broadcast_prices",
            replace_existing=True,
        )

    scheduler.start()
    logger.info(
        "Background Scheduler Started:\n"
        "   * Portfolio Risk Scan  - every 60 min + 15s after boot\n"
        "   * Daily Briefing       - Mon-Fri at 8:00 AM\n"
        "   * Equity Snapshots     - every 30 min during market hours\n"
        "   * Background Crawler   - every 2 min (drip-feed)\n"
        "   * Price Broadcast      - every 5s (active socket rooms)"
    )


def stop_scheduler():
    """Gracefully shut down the scheduler."""
    if scheduler.running:
        scheduler.shutdown(wait=False)
        logger.info("Background Scheduler Stopped.")
