import torch
from .gpu import device

def torch_ema(data: torch.Tensor, period: int) -> torch.Tensor:
    """Vectorized EMA calculation on GPU."""
    alpha = 2.0 / (period + 1)
    # This is slightly complex to vectorize fully without a loop to maintain precision
    # but for large data, a custom kernel or a cumulative product approach works.
    # Simple recursive version for now (still uses GPU kernels for multiplication/addition)
    ema = torch.zeros_like(data)
    ema[0] = data[0]
    for i in range(1, len(data)):
        ema[i] = data[i] * alpha + ema[i-1] * (1 - alpha)
    return ema

def torch_sma(data: torch.Tensor, period: int) -> torch.Tensor:
    """Vectorized SMA calculation on GPU."""
    # Use 1D convolution for parallel window average
    weight = torch.ones(1, 1, period, device=device) / period
    x = data.view(1, 1, -1)
    # Padding to maintain length, although initial values will be inaccurate
    padded_x = torch.nn.functional.pad(x, (period-1, 0), mode='constant', value=data[0])
    res = torch.nn.functional.conv1d(padded_x, weight)
    return res.view(-1)

def torch_rsi(data: torch.Tensor, period: int = 14) -> torch.Tensor:
    """Parallelized RSI calculation on GPU."""
    delta = data[1:] - data[:-1]
    up = delta.clone()
    down = delta.clone()
    up[up < 0] = 0
    down[down > 0] = 0
    down = torch.abs(down)

    avg_gain = torch_sma(up, period)
    avg_loss = torch_sma(down, period)
    
    rs = avg_gain / (avg_loss + 1e-10)
    rsi = 100 - (100 / (1 + rs))
    return rsi

def torch_atr(high: torch.Tensor, low: torch.Tensor, close: torch.Tensor, period: int = 14) -> torch.Tensor:
    """Parallelized ATR calculation on GPU."""
    tr1 = high[1:] - low[1:]
    tr2 = torch.abs(high[1:] - close[:-1])
    tr3 = torch.abs(low[1:] - close[:-1])
    
    tr = torch.max(torch.stack([tr1, tr2, tr3]), dim=0)[0]
    # First TR value is just high-low
    first_tr = (high[0] - low[0]).view(1)
    tr_full = torch.cat([first_tr, tr])
    
    return torch_sma(tr_full, period)
