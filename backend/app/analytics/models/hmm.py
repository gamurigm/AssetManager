import numpy as np
import pandas as pd
from hmmlearn.hmm import GaussianHMM
from typing import Dict, Any

class MarketRegimeModel:
    """
    Hidden Markov Model for Market Regime Detection.
    Identifies latent states (e.g., Bull, Bear, Choppy) based on:
    - Log Returns
    - Range Volatility
    - Volume Change
    """
    
    def __init__(self, n_components: int = 3, n_iter: int = 100):
        self.n_components = n_components
        self.n_iter = n_iter
        self.model = GaussianHMM(
            n_components=n_components, 
            covariance_type="full", 
            n_iter=n_iter,
            random_state=42
        )
        self.state_map: Dict[int, str] = {}

    def prepare_features(self, df: pd.DataFrame) -> tuple[np.ndarray, pd.Index]:
        """
        Extracts features from OHLCV DataFrame.
        Expected columns: 'date', 'open', 'high', 'low', 'close', 'volume'
        """
        # Ensure data is sorted by date and copy to avoid modifying original
        if 'date' in df.columns:
            df = df.sort_values('date').copy()
        else:
            df = df.copy() # Assume index is date or sorted
            
        # Ensure numeric types
        numeric_cols = ['open', 'high', 'low', 'close', 'volume']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col])

        # 1. Daily Log Returns: ln(Pt / Pt-1)
        df['log_ret'] = np.log(df['close'] / df['close'].shift(1))
        
        # 2. Daily Range Volatility (Normalized): (High - Low) / Close
        df['range_vol'] = (df['high'] - df['low']) / df['close']
        
        # 3. Log Volume Change: ln(Vt / Vt-1)
        # Add epsilon to avoid log(0)
        df['log_vol_change'] = np.log((df['volume'] + 1e-9) / (df['volume'].shift(1) + 1e-9))
        
        # Drop NaN values created by shifting (first row)
        df.dropna(inplace=True)
        
        # Return features for HMM (n_samples, n_features) and the corresponding index (dates)
        # We assume the index of the dataframe was preserved or is useful
        return df[['log_ret', 'range_vol', 'log_vol_change']].values, df.index

    def fit_predict(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Fits the HMM specific to this single asset's history and predicts the current state.
        Why fit every time? Market regimes define themselves relative to the asset's specific volatility profile.
        """
        if len(df) < 50:
            return {"error": "Not enough data points for HMM Training (need > 50)"}

        try:
            X, valid_indices = self.prepare_features(df)
            
            # Fit model to the data
            self.model.fit(X)
            
            # Predict the hidden state sequence
            hidden_states = self.model.predict(X)
            
            # Interpret what state 0, 1, 2 actually mean
            self._interpret_states(X, hidden_states)
            
            # Get the most recent state (today/yesterday)
            latest_state = hidden_states[-1]
            regime = self.state_map.get(latest_state, "Unknown")
            
            # Calculate posterior probabilities for the last observation
            posteriors = self.model.predict_proba(X)
            last_probs = posteriors[-1].tolist()
            
            return {
                "current_regime": regime,
                "current_state_id": int(latest_state),
                "regime_probs": {self.state_map.get(i, str(i)): p for i, p in enumerate(last_probs)},
                "state_definitions": self.state_map,
                "means": self.model.means_.tolist(),
            }
        except Exception as e:
            return {"error": f"HMM Analysis failed: {str(e)}"}

    def _interpret_states(self, X: np.ndarray, hidden_states: np.ndarray):
        """
        Dynamically labels states based on their statistical properties.
        Heuristics:
        - Bull: Positive returns, Low/Medium volatility
        - Bear: Negative returns, High volatility
        - Choppy/Neutral: Low returns, Mixed volatility
        """
        # map state_id -> {'ret': mean, 'vol': mean}
        state_stats = {}
        
        for i in range(self.n_components):
            mask = (hidden_states == i)
            if not np.any(mask):
                continue
            
            # X columns: 0:log_ret, 1:range_vol, 2:log_vol_change
            comp_data = X[mask]
            
            mean_ret = np.mean(comp_data[:, 0]) # Annualize? Keep daily for relative comparison
            mean_vol = np.mean(comp_data[:, 1])
            
            state_stats[i] = {'ret': mean_ret, 'vol': mean_vol}
            
        # Sort by Returns
        # But simply sorting by returns might confuse a "crash" (high vol, neg ret) with "correction"
        # Let's try a simple sorting approach first:
        
        ordered_states = sorted(state_stats.items(), key=lambda item: item[1]['ret'])
        # ordered_states[0] = Lowest Return (Bear)
        # ordered_states[-1] = Highest Return (Bull)
        
        if not ordered_states:
            return

        bear_id = ordered_states[0][0]
        bull_id = ordered_states[-1][0]
        
        # Identify the remaining one
        all_ids = set(range(self.n_components))
        remaining = all_ids - {bear_id, bull_id}
        neutral_id = list(remaining)[0] if remaining else -1
        
        # Refinement: If the "Bull" state has massive volatility and negative returns (unlikely if sorted by ret), swap?
        # For now, trust the returns sorting for basic definition.
        
        self.state_map = {
            bull_id: "Bullish",
            bear_id: "Bearish",
            neutral_id: "Neutral/Choppy"
        }
