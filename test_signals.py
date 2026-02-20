import asyncio
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
from app.services.market_data import market_data_service
from app.agents.strategies.engine.orb_fvg_engine import ORBFVGEngine
from app.agents.strategies.engine.models import StrategyConfig
from app.agents.strategies.backtest_runner import BacktestRunner

async def main():
    m1_res = await market_data_service.get_intraday("AAPL", "1m", "7d")
    m5_res = await market_data_service.get_intraday("AAPL", "5m", "1mo")
    
    m1 = m1_res.get("candles", [])
    m5 = m5_res.get("candles", [])
    
    sessions = BacktestRunner._split_into_sessions(m1, m5)
    
    engine = ORBFVGEngine()
    
    # Very loose rules
    cfg = StrategyConfig(
        min_range_pips=0.1,
        body_ratio_breakout=0.1,
        vol_ruptura_ratio=0.5,
        min_fvg_size_atr=0.1,
        p_cuerpo_min=0.1,
        p_vol_min=0.5
    )
    
    print(f"Total sessions to evaluate: {len(sessions)}")
    
    for s in sessions:
        if len(s["m5"]) == 0 or len(s["m1"]) == 0:
            continue
        print(f"\n--- Evaluating Session {s['date']} ---")
        
        # Manually trace ORB detection
        m5_candles = s["m5"]
        if m5_candles:
            orb = engine._detect_orb(m5_candles[0], cfg.min_range_pips)
            print(f"ORB: High={orb.high}, Low={orb.low}, Range={orb.range_}, Valid={orb.valid}")
        
        signal = engine.run_session(s["m5"], s["m1"], 10000, cfg)
        
        # Track internally
        import numpy as np
        from app.agents.strategies.engine.indicators import compute_avg_volume
        avg_vol = compute_avg_volume(s["m1"], period=20)
        
        breakouts = 0
        fvgs = 0
        state = engine.run_session(s["m5"], s["m1"], 10000, cfg)
        
        # Test engulfing directly using a mockup logic
        import copy
        from app.agents.strategies.engine.models import SessionState
        from app.agents.strategies.engine.indicators import compute_ATR
        atr_m1 = compute_ATR(s["m1"], 14)

        my_state = SessionState()
        my_state.orb = orb
        prev_candle = None
        for idx, candle in enumerate(s["m1"]):
            if not my_state.fvg:
                if prev_candle is not None:
                    bk = engine._detect_breakout(candle, prev_candle, orb.high, orb.low, avg_vol, cfg)
                    if bk["valid"] and not my_state.breakout_detected:
                        my_state.breakout_detected = True
                        my_state.breakout_direction = bk["direction"]
                        if idx >= 2:
                            fvg = engine._compute_fvg(s["m1"][idx-2], s["m1"][idx-1], candle, bk["direction"], atr_m1, cfg)
                            if fvg:
                                my_state.fvg = fvg
                                my_state.retest_countdown = cfg.wait_retest_max_m1
            elif not my_state.setup_active:
                if my_state.retest_countdown <= 0:
                    pass
                else:
                    my_state.retest_countdown -= 1
                    invalid = engine._setup_invalidated(candle, my_state.fvg, orb, cfg)
                    if invalid:
                        print(f"Setup invalidated at {candle['timestamp']}")
                        my_state = SessionState() # reset state to continue search? wait no engine returns None
                    else:
                        if engine._price_in_fvg(candle, my_state.fvg):
                            if prev_candle is not None:
                                is_eng = engine._is_engulfing(candle, prev_candle, my_state.fvg.direction, atr_m1, avg_vol, cfg)
                                if is_eng:
                                    print(f"ENGULFING Confirmed at {candle['timestamp']}")
                                else:
                                    # print why it failed
                                    body_size = abs(candle["close"] - candle["open"])
                                    dir_pass = "bullish" if my_state.fvg.direction == 'bullish' else "bearish"
                                    print(f"Candle touched FVG but not engulfing {dir_pass} body_size: {body_size} vs min {cfg.p_cuerpo_min * atr_m1}, vol: {candle['volume']} vs min {cfg.p_vol_min * avg_vol}")

            prev_candle = candle
            
        print(f"Total Breakouts: {breakouts}")
        print(f"Total FVGs: {fvgs}")
        
        if state:
            print(f"SIGNAL FOUND: {state}")
        else:
            print(f"No signal found for {s['date']}")

if __name__ == "__main__":
    asyncio.run(main())
