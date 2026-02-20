import asyncio
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
from app.agents.strategies.backtest_runner import BacktestRunner, BacktestConfig
from app.agents.strategies.engine.orb_fvg_engine import ORBFVGEngine
from app.services.market_data import intraday_repository
from app.services.kpi_calculator import KPICalculator

async def main():
    config = BacktestConfig(
        symbol="AAPL",
        start_date="2026-02-10",
        end_date="2026-02-19",
        run_bootstrap=True
    )
    runner = BacktestRunner(
        strategy=ORBFVGEngine(),
        repository=intraday_repository,
        kpi_calc=KPICalculator()
    )
    res = await runner.run(config)
    print("FINISHED")
    print(res.summary())

if __name__ == "__main__":
    asyncio.run(main())
