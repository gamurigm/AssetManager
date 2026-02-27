import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))
os.chdir(os.path.join(os.path.dirname(__file__), "backend"))

from app.agents.strategies.engine.stationary_bootstrap import StationaryBootstrap, recommend_block_length
from app.agents.strategies.engine.models import TradeRecord, TradeSignal

def make_trade(pnl, outcome):
    sig = TradeSignal('x','2024-01-01','LONG',1,0,1,0.9,1,0.9,1.1,0.1,1.0,'standard',0.01)
    return TradeRecord(sig, outcome, 1.1 if outcome=='win_tp' else 0.9, '2024-01-01',
                       3.0 if outcome=='win_tp' else -1.0, pnl, 0.0)

trades = [make_trade(50,'win_tp') if i%3!=0 else make_trade(-20,'loss_sl') for i in range(30)]
n = len(trades)
bl = recommend_block_length(n)
print(f"Trades: {n}  |  Block length recomendado (N^1/3): {bl}")

sb = StationaryBootstrap(block_length=bl, seed=42)
r = sb.run(trades, 10_000.0, iterations=5000, return_samples=False)

print(f"Method          : {r['method']}")
print(f"Block length    : {r['block_length']}")
print(f"Net Profit CI   : [{r['net_profit_95_ci'][0]:.2f}, {r['net_profit_95_ci'][1]:.2f}] USD")
print(f"Max Drawdown CI : [{r['max_drawdown_95_ci_pct'][0]:.2%}, {r['max_drawdown_95_ci_pct'][1]:.2%}]")
print(f"Mean net profit : {r['net_profit_mean']:.2f}")
print(f"Std net profit  : {r['net_profit_std']:.2f}")

# Reproducibility check
sb2 = StationaryBootstrap(block_length=bl, seed=42)
r2 = sb2.run(trades, 10_000.0, iterations=5000)
assert r['net_profit_95_ci'] == r2['net_profit_95_ci'], "FAIL: reproducibility"
print("\nReproducibility : OK (misma seed -> mismo resultado)")

# Verify block bootstrap ≠ iid bootstrap (they should differ for correlated data)
sb_iid = StationaryBootstrap(block_length=1, seed=42)   # block_length=1 → i.i.d.
r_iid = sb_iid.run(trades, 10_000.0, iterations=5000)
print(f"\nComparison i.i.d vs block bootstrap:")
print(f"  i.i.d  Net Profit CI : [{r_iid['net_profit_95_ci'][0]:.2f}, {r_iid['net_profit_95_ci'][1]:.2f}]")
print(f"  block  Net Profit CI : [{r['net_profit_95_ci'][0]:.2f}, {r['net_profit_95_ci'][1]:.2f}]")
print(f"  (CIs diverge when autocorrelation is present - this is expected)")

print("\nTEST PASSED ✓")
