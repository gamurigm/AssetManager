"""
Backend Accelerant — CUDA-accelerated operations with graceful fallback.
If torch is not installed, is_available() returns False and callers should
use their NumPy/Rust fallback paths.
"""
from .gpu import gpu_manager, device, _get_torch
import numpy as np
from typing import List, Dict, Any


class BackendAccelerant:
    """
    Unified entry point for CUDA-accelerated backend processes.
    Provides vectorized implementations of heavy math operations.
    """
    
    @staticmethod
    def is_available() -> bool:
        torch = _get_torch()
        if torch is None:
            return False
        return torch.cuda.is_available()

    @staticmethod
    def compute_volume_profile(highs: np.ndarray, lows: np.ndarray, volumes: np.ndarray, num_bins: int = 50):
        """
        CUDA-accelerated Volume Profile calculation.
        Distributes volume across price bins in parallel.
        """
        torch = _get_torch()
        if torch is None or not torch.cuda.is_available():
            return None

        h = torch.tensor(highs, device=device, dtype=torch.float32)
        l = torch.tensor(lows, device=device, dtype=torch.float32)
        v = torch.tensor(volumes, device=device, dtype=torch.float32)

        min_p = torch.min(l)
        max_p = torch.max(h)
        if min_p == max_p:
            return torch.zeros(num_bins, device=device), min_p, max_p

        bin_edges = torch.linspace(min_p, max_p, num_bins + 1, device=device)
        bin_width = (max_p - min_p) / num_bins

        profile_vol = torch.zeros(num_bins, device=device)
        typical_p = (h + l + (h+l)/2) / 3
        indices = torch.bucketize(typical_p, bin_edges) - 1
        indices = torch.clamp(indices, 0, num_bins - 1)
        profile_vol.scatter_add_(0, indices, v)
        
        return profile_vol.cpu().numpy(), min_p.item(), max_p.item()

    @staticmethod
    def run_bootstrap_parallel(pnl_array: np.ndarray, iterations: int, block_length: int, initial_equity: float):
        """
        Massively parallel Stationary Bootstrap on GPU.
        Runs all N iterations in a single vectorized operation.
        """
        torch = _get_torch()
        if torch is None:
            raise ImportError("torch is required for GPU bootstrap")

        n = len(pnl_array)
        p = 1.0 / block_length
        
        pnl_t = torch.tensor(pnl_array, device=device, dtype=torch.float32)
        all_indices = torch.zeros((iterations, n), device=device, dtype=torch.long)
        
        curr_indices = torch.randint(0, n, (iterations,), device=device)
        all_indices[:, 0] = curr_indices
        
        for i in range(1, n):
            new_block_mask = torch.rand(iterations, device=device) < p
            next_idx = (curr_indices + 1) % n
            rand_idx = torch.randint(0, n, (iterations,), device=device)
            curr_indices = torch.where(new_block_mask, rand_idx, next_idx)
            all_indices[:, i] = curr_indices
            
        res_pnl = pnl_t.unsqueeze(0).expand(iterations, -1).gather(1, all_indices)
        net_profits = res_pnl.sum(dim=1)
        
        equity_curves = torch.zeros((iterations, n + 1), device=device)
        equity_curves[:, 0] = initial_equity
        equity_curves[:, 1:] = initial_equity + torch.cumsum(res_pnl, dim=1)
        
        running_max, _ = torch.cummax(equity_curves, dim=1)
        drawdowns = (running_max - equity_curves) / (running_max + 1e-10)
        max_drawdowns, _ = torch.max(drawdowns, dim=1)
        
        return net_profits.cpu().numpy(), max_drawdowns.cpu().numpy()

accelerant = BackendAccelerant()
