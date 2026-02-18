from fastapi import APIRouter, HTTPException, Depends
import pandas as pd
from ...core.container import get_historical
from ...analytics.models.hmm import MarketRegimeModel

router = APIRouter()

@router.get("/regime/{symbol}")
async def get_market_regime(symbol: str):
    """
    Analyzes historical data to detect the current market regime using a Hidden Markov Model (HMM).
    Returns: Current regime (Bullish/Bearish/Neutral) and transition probabilities.
    """
    # 1. Fetch Historical Data (Last 500 candles for solid regime detection)
    # Using existing UseCase to leverage cache/provider fallback
    data = await get_historical.execute(symbol, limit=500)
    
    if not data or "error" in data:
        raise HTTPException(status_code=404, detail=data.get("error", "Data not found"))
        
    candles = data.get("historical", [])
    if not candles:
        raise HTTPException(status_code=404, detail="No historical data found for HMM analysis")
        
    # 2. Convert to DataFrame for Analysis
    try:
        df = pd.DataFrame(candles)
        
        # 3. Predict Regime
        # Instantiate fresh model for this asset to learn its specific volatility patterns
        model = MarketRegimeModel()
        result = model.fit_predict(df)
        
        if result.get("error"):
            raise HTTPException(status_code=422, detail=result["error"])

        return {
            "symbol": symbol,
            "regime_analysis": result,
            "data_source": data.get("source", "Unknown"),
            "data_points_analyzed": len(df)
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
