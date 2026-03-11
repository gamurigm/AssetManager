"""
CUDA math helpers — lazily imports torch.
Falls back gracefully when torch is not installed.
"""
from .gpu import _get_torch, device


def torch_ema(data, period: int):
    """Vectorized EMA calculation on GPU."""
    torch = _get_torch()
    if torch is None:
        raise ImportError("torch is required for torch_ema")
    alpha = 2.0 / (period + 1)
    ema = torch.zeros_like(data)
    ema[0] = data[0]
    for i in range(1, len(data)):
        ema[i] = data[i] * alpha + ema[i-1] * (1 - alpha)
    return ema


def torch_sma(data, period: int):
    """Vectorized SMA calculation on GPU."""
    torch = _get_torch()
    if torch is None:
        raise ImportError("torch is required for torch_sma")
    weight = torch.ones(1, 1, period, device=device) / period
    x = data.view(1, 1, -1)
    padded_x = torch.nn.functional.pad(x, (period-1, 0), mode='constant', value=data[0])
    res = torch.nn.functional.conv1d(padded_x, weight)
    return res.view(-1)


def torch_rsi(data, period: int = 14):
    """Parallelized RSI calculation on GPU."""
    torch = _get_torch()
    if torch is None:
        raise ImportError("torch is required for torch_rsi")
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


def torch_atr(high, low, close, period: int = 14):
    """Parallelized ATR calculation on GPU."""
    torch = _get_torch()
    if torch is None:
        raise ImportError("torch is required for torch_atr")
    tr1 = high[1:] - low[1:]
    tr2 = torch.abs(high[1:] - close[:-1])
    tr3 = torch.abs(low[1:] - close[:-1])
    
    tr = torch.max(torch.stack([tr1, tr2, tr3]), dim=0)[0]
    first_tr = (high[0] - low[0]).view(1)
    tr_full = torch.cat([first_tr, tr])
    
    return torch_sma(tr_full, period)
