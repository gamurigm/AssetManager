"""
test_cv_real.py
===============
Runs PurgedKFold cross-validation on real intraday data (SPY)
and compares it against the naive single-pass backtest.

Usage:
    python c:\\AssetManager\\test_cv_real.py
"""

import asyncio
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))
os.chdir(os.path.join(os.path.dirname(__file__), "backend"))

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), "backend", ".env"))

import logfire
logfire.configure(send_to_logfire="never")

from app.agents.strategies.backtest_runner import BacktestRunner, BacktestConfig
from app.agents.strategies.engine import ORBFVGEngine, ORBKPICalculator
from app.services.intraday_repository import intraday_repository

SYMBOL     = "SPY"
START_DATE = "2024-06-01"
END_DATE   = "2025-01-31"
ACCOUNT    = 10_000.0
N_SPLITS   = 4        # 4 folds ≈ 2 meses de test cada uno
EMBARGO    = 3        # 3 días de buffer entre train y test

SEP = "=" * 60


async def run():
    runner = BacktestRunner(ORBFVGEngine(), intraday_repository, ORBKPICalculator())

    # ------------------------------------------------------------------ #
    # 1. Single-pass backtest (el enfoque anterior)
    # ------------------------------------------------------------------ #
    print(f"\n{SEP}")
    print("BACKTEST SIMPLE (single-pass — potencialmente sesgado)")
    print(SEP)

    cfg_simple = BacktestConfig(
        symbol=SYMBOL,
        start_date=START_DATE,
        end_date=END_DATE,
        account_size=ACCOUNT,
    )

    result = await runner.run(cfg_simple)
    k = result.kpis
    print(f"  Período     : {START_DATE} → {END_DATE}")
    print(f"  Sesiones    : {result.trading_days} días")
    print(f"  Trades      : {k.total_trades}")
    print(f"  Win Rate    : {k.win_rate:.1%}")
    print(f"  Profit Fac. : {k.profit_factor:.2f}")
    print(f"  Expectancy  : {k.expectancy_r:.3f}R")
    print(f"  Sharpe      : {k.sharpe_ratio:.2f}")
    print(f"  Max DD      : {k.max_drawdown_pct:.1%}")
    print(f"  Total R     : {k.total_r:.2f}R")

    # ------------------------------------------------------------------ #
    # 2. PurgedKFold cross-validation (out-of-sample honesto)
    # ------------------------------------------------------------------ #
    print(f"\n{SEP}")
    print(f"PURGEDKFOLD CV  (K={N_SPLITS}, embargo={EMBARGO} días)")
    print(SEP)

    cfg_cv = BacktestConfig(
        symbol=SYMBOL,
        start_date=START_DATE,
        end_date=END_DATE,
        account_size=ACCOUNT,
        run_cv=True,
        cv_n_splits=N_SPLITS,
        cv_embargo_days=EMBARGO,
    )

    cv = await runner.run_cv(cfg_cv)

    if not cv.folds:
        print("  ⚠️  Sin folds — posiblemente datos insuficientes para el período.")
        return

    print(f"\n  {'Fold':<6} {'Test window':<28} {'Train':>6} {'Test':>5} {'Trades':>7} {'WR':>7} {'PF':>6} {'Exp R':>7} {'Sharpe':>7}")
    print(f"  {'-'*6} {'-'*28} {'-'*6} {'-'*5} {'-'*7} {'-'*7} {'-'*6} {'-'*7} {'-'*7}")

    for f in cv.folds:
        pf_str = f"{f.kpis.profit_factor:.2f}" if f.kpis.profit_factor != float('inf') else "  ∞"
        print(
            f"  {f.fold_index:<6} "
            f"{f.test_start} → {f.test_end}   "
            f"{f.train_days:>6} {f.test_days:>5} "
            f"{f.kpis.total_trades:>7} "
            f"{f.kpis.win_rate:>6.1%} "
            f"{pf_str:>6} "
            f"{f.kpis.expectancy_r:>7.3f} "
            f"{f.kpis.sharpe_ratio:>7.2f}"
        )

    print(f"\n  {'MEDIA':<6} {'':28} {'':>6} {'':>5} "
          f"{'':>7} "
          f"{cv.mean_win_rate:>6.1%} "
          f"{cv.mean_profit_factor:>6.2f} "
          f"{cv.mean_expectancy_r:>7.3f} "
          f"{cv.mean_sharpe:>7.2f}")
    print(f"  {'±STD':<6} {'':28} {'':>6} {'':>5} "
          f"{'':>7} "
          f"{cv.std_win_rate:>6.1%} "
          f"{cv.std_profit_factor:>6.2f} "
          f"{cv.std_expectancy_r:>7.3f} "
          f"{cv.std_sharpe:>7.2f}")

    # ------------------------------------------------------------------ #
    # 3. Diagnóstico comparativo
    # ------------------------------------------------------------------ #
    print(f"\n{SEP}")
    print("DIAGNÓSTICO COMPARATIVO")
    print(SEP)

    wr_diff  = k.win_rate - cv.mean_win_rate
    pf_diff  = k.profit_factor - cv.mean_profit_factor
    exp_diff = k.expectancy_r - cv.mean_expectancy_r

    def flag(diff, threshold=0.05):
        if abs(diff) < threshold:
            return "✅  Consistente"
        elif diff > 0:
            return "⚠️  Backtest SOBREESTIMADO (overfitting posible)"
        else:
            return "✅  CV mejor que backtest simple (raro pero posible)"

    print(f"\n  Métrica        Backtest    CV (media)   Diff      Veredicto")
    print(f"  {'-'*13} {'-'*10} {'-'*11} {'-'*8} {'-'*30}")
    print(f"  Win Rate       {k.win_rate:>8.1%}   {cv.mean_win_rate:>8.1%}   {wr_diff:>+7.1%}   {flag(wr_diff, 0.05)}")
    print(f"  Profit Factor  {k.profit_factor:>8.2f}   {cv.mean_profit_factor:>8.2f}   {pf_diff:>+7.2f}   {flag(pf_diff, 0.20)}")
    print(f"  Expectancy R   {k.expectancy_r:>8.3f}   {cv.mean_expectancy_r:>8.3f}   {exp_diff:>+7.3f}   {flag(exp_diff, 0.05)}")

    print(f"\n  Estabilidad entre folds (std Win Rate): {cv.std_win_rate:.1%}")
    if cv.std_win_rate < 0.10:
        print("  → Estrategia ESTABLE a lo largo del tiempo ✅")
    elif cv.std_win_rate < 0.20:
        print("  → Estabilidad MODERADA — monitorear en live ⚠️")
    else:
        print("  → Alta variabilidad inter-fold — estrategia INESTABLE 🚨")

    print()


if __name__ == "__main__":
    asyncio.run(run())
