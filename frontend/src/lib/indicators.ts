// ─── Technical Indicator Calculations ──────────────────────────────
// Pure functions — no React, no side effects. Easy to test and extend.

/**
 * Exponential Moving Average
 */
export function calcEMA(data: number[], period: number): number[] {
    const k = 2 / (period + 1);
    const ema: number[] = [data[0]];
    for (let i = 1; i < data.length; i++) {
        ema.push(data[i] * k + ema[i - 1] * (1 - k));
    }
    return ema;
}

/**
 * MACD (Moving Average Convergence Divergence)
 */
export function calcMACD(
    closes: number[],
    fast = 12,
    slow = 26,
    signal = 9
) {
    const emaFast = calcEMA(closes, fast);
    const emaSlow = calcEMA(closes, slow);
    const macdLine = emaFast.map((v, i) => v - emaSlow[i]);
    const signalLine = calcEMA(macdLine, signal);
    const histogram = macdLine.map((v, i) => v - signalLine[i]);
    return { macdLine, signalLine, histogram };
}

/**
 * Stochastic Oscillator (%K / %D)
 */
export function calcStochastic(
    highs: number[],
    lows: number[],
    closes: number[],
    kPeriod = 14,
    dPeriod = 3,
    smooth = 3
) {
    const rawK: number[] = [];
    for (let i = 0; i < closes.length; i++) {
        if (i < kPeriod - 1) { rawK.push(NaN); continue; }
        const hh = Math.max(...highs.slice(i - kPeriod + 1, i + 1));
        const ll = Math.min(...lows.slice(i - kPeriod + 1, i + 1));
        rawK.push(hh === ll ? 50 : ((closes[i] - ll) / (hh - ll)) * 100);
    }

    const kLine: number[] = [];
    for (let i = 0; i < rawK.length; i++) {
        if (i < kPeriod - 1 + smooth - 1 || isNaN(rawK[i])) { kLine.push(NaN); continue; }
        const sl = rawK.slice(i - smooth + 1, i + 1).filter(v => !isNaN(v));
        kLine.push(sl.reduce((s, v) => s + v, 0) / sl.length);
    }

    const dLine: number[] = [];
    for (let i = 0; i < kLine.length; i++) {
        if (isNaN(kLine[i]) || i < kPeriod - 1 + smooth - 1 + dPeriod - 1) { dLine.push(NaN); continue; }
        const sl = kLine.slice(i - dPeriod + 1, i + 1).filter(v => !isNaN(v));
        dLine.push(sl.reduce((s, v) => s + v, 0) / sl.length);
    }

    return { kLine, dLine };
}

/**
 * Fibonacci retracement levels from a price range
 */
export const FIBONACCI_LEVELS = [
    { level: 0, text: '0% (High)', color: '#71717a' },
    { level: 0.236, text: '23.6%', color: '#94a3b8' },
    { level: 0.382, text: '38.2%', color: '#64748b' },
    { level: 0.500, text: '50.0%', color: '#facc15' },
    { level: 0.618, text: '61.8%', color: '#fb923c' },
    { level: 0.786, text: '78.6%', color: '#f87171' },
    { level: 1.000, text: '100% (Low)', color: '#ef4444' },
] as const;

/**
 * Simple Moving Average
 */
export function calcSMA(data: number[], period: number): (number | null)[] {
    const result: (number | null)[] = [];
    for (let i = 0; i < data.length; i++) {
        if (i < period - 1) { result.push(null); continue; }
        const slice = data.slice(i - period + 1, i + 1);
        result.push(slice.reduce((s, v) => s + v, 0) / period);
    }
    return result;
}

/**
 * Bollinger Bands (SMA ± k * σ)
 */
export function calcBollingerBands(closes: number[], period = 20, multiplier = 2.0) {
    const middle = calcSMA(closes, period);
    const upper: (number | null)[] = [];
    const lower: (number | null)[] = [];
    for (let i = 0; i < closes.length; i++) {
        if (middle[i] === null) { upper.push(null); lower.push(null); continue; }
        const slice = closes.slice(i - period + 1, i + 1);
        const mean = middle[i]!;
        const variance = slice.reduce((s, v) => s + (v - mean) ** 2, 0) / period;
        const std = Math.sqrt(variance);
        upper.push(mean + multiplier * std);
        lower.push(mean - multiplier * std);
    }
    return { upper, middle, lower };
}

/**
 * Ichimoku Cloud
 * Tenkan-sen (9), Kijun-sen (26), Senkou A, Senkou B (52), Chikou (26 behind)
 */
function highLowMid(highs: number[], lows: number[], start: number, end: number): number | null {
    if (start < 0) return null;
    const hSlice = highs.slice(start, end + 1);
    const lSlice = lows.slice(start, end + 1);
    if (hSlice.length === 0) return null;
    return (Math.max(...hSlice) + Math.min(...lSlice)) / 2;
}

export function calcIchimoku(
    highs: number[],
    lows: number[],
    closes: number[],
    tenkanPeriod = 9,
    kijunPeriod = 26,
    senkouBPeriod = 52,
    displacement = 26
) {
    const len = closes.length;
    const tenkan: (number | null)[] = [];
    const kijun: (number | null)[] = [];
    const senkouA: (number | null)[] = [];
    const senkouB: (number | null)[] = [];
    const chikou: (number | null)[] = [];

    for (let i = 0; i < len; i++) {
        tenkan.push(i >= tenkanPeriod - 1 ? highLowMid(highs, lows, i - tenkanPeriod + 1, i) : null);
        kijun.push(i >= kijunPeriod - 1 ? highLowMid(highs, lows, i - kijunPeriod + 1, i) : null);
    }

    // Senkou A & B are displaced forward by `displacement` periods
    // We store them in arrays of length len + displacement, but for chart overlay we match by index
    for (let i = 0; i < len + displacement; i++) {
        const srcIdx = i - displacement;
        if (srcIdx >= 0 && srcIdx < len && tenkan[srcIdx] !== null && kijun[srcIdx] !== null) {
            senkouA.push((tenkan[srcIdx]! + kijun[srcIdx]!) / 2);
        } else {
            senkouA.push(null);
        }
        if (srcIdx >= 0 && srcIdx < len && srcIdx >= senkouBPeriod - 1) {
            senkouB.push(highLowMid(highs, lows, srcIdx - senkouBPeriod + 1, srcIdx));
        } else {
            senkouB.push(null);
        }
    }

    // Chikou = close displaced backwards
    for (let i = 0; i < len; i++) {
        chikou.push(i + displacement < len ? closes[i + displacement] : null);
    }

    return { tenkan, kijun, senkouA, senkouB, chikou };
}
