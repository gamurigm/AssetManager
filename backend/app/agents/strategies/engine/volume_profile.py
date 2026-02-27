from typing import List, Dict, Any, Tuple
import numpy as np
from dataclasses import dataclass

@dataclass
class VolumeProfileNode:
    price_low: float
    price_high: float
    volume: float

@dataclass
class VolumeProfileResult:
    poc: float  # Point of Control
    vah: float  # Value Area High
    val: float  # Value Area Low
    hvn_edges: List[Tuple[float, float]]  # List of High Volume Node (low, high) edges
    profile: List[VolumeProfileNode]  # Full distribution

class VolumeProfileCalculator:
    """
    Computes Volume Profile over a given set of candles.
    Uses typical price (H+L+C)/3 and distributes volume across price bins.
    """
    def __init__(self, num_bins: int = 50, value_area_pct: float = 0.70, hvn_threshold_pct: float = 0.5):
        self.num_bins = num_bins
        self.value_area_pct = value_area_pct
        self.hvn_threshold_pct = hvn_threshold_pct

    def compute(self, candles: List[Dict[str, Any]]) -> VolumeProfileResult:
        if not candles:
            return VolumeProfileResult(0.0, 0.0, 0.0, [], [])

        # 1. Extract high, low, close, volume
        highs = np.array([c["high"] for c in candles])
        lows = np.array([c["low"] for c in candles])
        closes = np.array([c["close"] for c in candles])
        volumes = np.array([c["volume"] for c in candles])

        min_price = np.min(lows)
        max_price = np.max(highs)

        if min_price == max_price:
            # Flat market edge case
            return VolumeProfileResult(min_price, min_price, min_price, [(min_price, min_price)], [])

        # 2. Create Price Bins
        bins = np.linspace(min_price, max_price, self.num_bins + 1)
        bin_size = (max_price - min_price) / self.num_bins
        
        # Array to hold volume accumulated in each bin
        # 3. Distribute Volume
        from app.core.acceleration import accelerant
        if accelerant.is_available():
            profile_vol, _, _ = accelerant.compute_volume_profile(highs, lows, volumes, self.num_bins)
        else:
            profile_vol = np.zeros(self.num_bins)
            for h, l, v in zip(highs, lows, volumes):
                start_idx = np.searchsorted(bins, l, side="right") - 1
                end_idx = np.searchsorted(bins, h, side="left")
                start_idx = max(0, start_idx)
                end_idx = min(self.num_bins - 1, end_idx)
                if start_idx == end_idx:
                    profile_vol[start_idx] += v
                else:
                    bins_touched = end_idx - start_idx + 1
                    vol_per_bin = v / bins_touched if bins_touched > 0 else 0
                    profile_vol[start_idx:end_idx+1] += vol_per_bin

        # 4. Find POC (Point of Control)
        poc_idx = np.argmax(profile_vol)
        poc_price = bins[poc_idx] + (bin_size / 2)

        # 5. Calculate Value Area (VAH, VAL)
        total_vol = np.sum(profile_vol)
        target_vol = total_vol * self.value_area_pct
        
        current_vol = profile_vol[poc_idx]
        va_low_idx = poc_idx
        va_high_idx = poc_idx

        # Expand VA upwards and downwards from POC
        while current_vol < target_vol and (va_low_idx > 0 or va_high_idx < self.num_bins - 1):
            vol_up = profile_vol[va_high_idx + 1] if va_high_idx < self.num_bins - 1 else -1.0
            vol_down = profile_vol[va_low_idx - 1] if va_low_idx > 0 else -1.0

            if vol_up >= vol_down and vol_up >= 0:
                va_high_idx += 1
                current_vol += vol_up
            elif vol_down > vol_up and vol_down >= 0:
                va_low_idx -= 1
                current_vol += vol_down
            else:
                break # Should not happen unless both are 0

        val_price = bins[va_low_idx]
        vah_price = bins[va_high_idx + 1] # Upper bound of the top bin

        # 6. Identify High Volume Nodes (HVNs)
        hvn_edges = []
        max_vol = profile_vol[poc_idx]
        threshold_vol = max_vol * self.hvn_threshold_pct

        # Find continuous blocks of bins above threshold
        in_node = False
        node_start_idx = -1
        
        for i in range(self.num_bins):
            if profile_vol[i] >= threshold_vol:
                if not in_node:
                    in_node = True
                    node_start_idx = i
            else:
                if in_node:
                    in_node = False
                    hvn_edges.append((bins[node_start_idx], bins[i])) # Low, High

        # Close node if it extends to the top
        if in_node:
            hvn_edges.append((bins[node_start_idx], bins[-1]))

        # Format complete profile
        nodes = []
        for i in range(self.num_bins):
            nodes.append(VolumeProfileNode(
                price_low=bins[i],
                price_high=bins[i+1],
                volume=profile_vol[i]
            ))

        return VolumeProfileResult(
            poc=poc_price,
            vah=vah_price,
            val=val_price,
            hvn_edges=hvn_edges,
            profile=nodes
        )
