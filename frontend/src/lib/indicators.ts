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

/**
 * RSI (Relative Strength Index) — Wilder's smoothing
 * Returns values 0-100. Overbought > 70, Oversold < 30.
 */
export function calcRSI(closes: number[], period = 14): (number | null)[] {
    const rsi: (number | null)[] = [];
    if (closes.length < period + 1) return closes.map(() => null);

    // Calculate price changes
    const changes: number[] = [];
    for (let i = 1; i < closes.length; i++) {
        changes.push(closes[i] - closes[i - 1]);
    }

    // First average gain/loss (simple average)
    let avgGain = 0;
    let avgLoss = 0;
    for (let i = 0; i < period; i++) {
        if (changes[i] >= 0) avgGain += changes[i];
        else avgLoss += Math.abs(changes[i]);
    }
    avgGain /= period;
    avgLoss /= period;

    // Fill nulls for the warm-up period
    rsi.push(null); // index 0 has no change
    for (let i = 0; i < period - 1; i++) rsi.push(null);

    // First RSI value
    const rs0 = avgLoss === 0 ? 100 : avgGain / avgLoss;
    rsi.push(avgLoss === 0 ? 100 : 100 - 100 / (1 + rs0));

    // Subsequent RSI values using Wilder's smoothing
    for (let i = period; i < changes.length; i++) {
        const gain = changes[i] >= 0 ? changes[i] : 0;
        const loss = changes[i] < 0 ? Math.abs(changes[i]) : 0;
        avgGain = (avgGain * (period - 1) + gain) / period;
        avgLoss = (avgLoss * (period - 1) + loss) / period;
        const rs = avgLoss === 0 ? 100 : avgGain / avgLoss;
        rsi.push(avgLoss === 0 ? 100 : 100 - 100 / (1 + rs));
    }

    return rsi;
}

/**
 * VWAP (Volume Weighted Average Price)
 * Cumulative (Typical Price × Volume) / Cumulative Volume
 * Resets each session (we treat the entire dataset as one session for daily data).
 */
export function calcVWAP(
    highs: number[],
    lows: number[],
    closes: number[],
    volumes: number[]
): (number | null)[] {
    const vwap: (number | null)[] = [];
    let cumTPV = 0;
    let cumVol = 0;

    for (let i = 0; i < closes.length; i++) {
        const tp = (highs[i] + lows[i] + closes[i]) / 3;
        const vol = volumes[i] || 0;
        cumTPV += tp * vol;
        cumVol += vol;
        vwap.push(cumVol > 0 ? cumTPV / cumVol : null);
    }

    return vwap;
}

/**
 * ATR (Average True Range) — Wilder's smoothing
 * Measures volatility as the smoothed average of True Range.
 */
export function calcATR(
    highs: number[],
    lows: number[],
    closes: number[],
    period = 14
): (number | null)[] {
    const atr: (number | null)[] = [];
    if (closes.length < 2) return closes.map(() => null);

    // True Range
    const tr: number[] = [highs[0] - lows[0]];
    for (let i = 1; i < closes.length; i++) {
        tr.push(Math.max(
            highs[i] - lows[i],
            Math.abs(highs[i] - closes[i - 1]),
            Math.abs(lows[i] - closes[i - 1])
        ));
    }

    // Warm-up
    for (let i = 0; i < period - 1; i++) atr.push(null);

    // First ATR = simple average of first `period` TRs
    let avg = tr.slice(0, period).reduce((s, v) => s + v, 0) / period;
    atr.push(avg);

    // Wilder's smoothing
    for (let i = period; i < tr.length; i++) {
        avg = (avg * (period - 1) + tr[i]) / period;
        atr.push(avg);
    }

    return atr;
}

/**
 * Keltner Channels
 * Middle = EMA. Upper/Lower = Middle ± Multiplier × ATR
 */
export function calcKeltner(
    highs: number[],
    lows: number[],
    closes: number[],
    emaPeriod = 20,
    atrPeriod = 10,
    multiplier = 2.0
) {
    const middle = calcEMA(closes, emaPeriod);
    const atr = calcATR(highs, lows, closes, atrPeriod);
    const upper: (number | null)[] = [];
    const lower: (number | null)[] = [];

    for (let i = 0; i < closes.length; i++) {
        if (i < Math.max(emaPeriod, atrPeriod) - 1 || atr[i] === null) {
            upper.push(null);
            lower.push(null);
        } else {
            upper.push(middle[i] + multiplier * atr[i]!);
            lower.push(middle[i] - multiplier * atr[i]!);
        }
    }

    return { middle, upper, lower };
}

/**
 * OBV (On-Balance Volume)
 * Cumulative measure of buying/selling pressure.
 */
export function calcOBV(closes: number[], volumes: number[]): (number | null)[] {
    const obv: (number | null)[] = [];
    if (closes.length === 0) return obv;

    let currentV = 0;
    obv.push(currentV);

    for (let i = 1; i < closes.length; i++) {
        const vol = volumes[i] || 0;
        if (closes[i] > closes[i - 1]) currentV += vol;
        else if (closes[i] < closes[i - 1]) currentV -= vol;
        obv.push(currentV);
    }

    return obv;
}

/**
 * ADX (Average Directional Index)
 * Measures trend strength (values typically 0-100). Includes +DI and -DI.
 */
export function calcADX(highs: number[], lows: number[], closes: number[], period = 14) {
    const len = closes.length;
    const adx: (number | null)[] = Array(len).fill(null);
    const pdi: (number | null)[] = Array(len).fill(null);
    const ndi: (number | null)[] = Array(len).fill(null);

    if (len < period + 1) return { adx, pdi, ndi };

    const tr = [0];
    const pdm = [0];
    const ndm = [0];

    for (let i = 1; i < len; i++) {
        tr.push(Math.max(
            highs[i] - lows[i],
            Math.abs(highs[i] - closes[i - 1]),
            Math.abs(lows[i] - closes[i - 1])
        ));
        const upMove = highs[i] - highs[i - 1];
        const downMove = lows[i - 1] - lows[i];

        pdm.push(upMove > downMove && upMove > 0 ? upMove : 0);
        ndm.push(downMove > upMove && downMove > 0 ? downMove : 0);
    }

    let smoothTR = 0, smoothPDM = 0, smoothNDM = 0;
    for (let i = 1; i <= period; i++) {
        smoothTR += tr[i];
        smoothPDM += pdm[i];
        smoothNDM += ndm[i];
    }

    let dxSum = 0;

    for (let i = period; i < len; i++) {
        if (i > period) {
            smoothTR = smoothTR - (smoothTR / period) + tr[i];
            smoothPDM = smoothPDM - (smoothPDM / period) + pdm[i];
            smoothNDM = smoothNDM - (smoothNDM / period) + ndm[i];
        }

        const diPlus = smoothTR === 0 ? 0 : 100 * (smoothPDM / smoothTR);
        const diMinus = smoothTR === 0 ? 0 : 100 * (smoothNDM / smoothTR);
        pdi[i] = diPlus;
        ndi[i] = diMinus;

        const dx = (diPlus + diMinus === 0) ? 0 : 100 * (Math.abs(diPlus - diMinus) / (diPlus + diMinus));

        if (i < 2 * period - 1) {
            dxSum += dx;
        } else if (i === 2 * period - 1) {
            dxSum += dx;
            adx[i] = dxSum / period;
        } else {
            adx[i] = ((adx[i - 1]! * (period - 1)) + dx) / period;
        }
    }

    return { adx, pdi, ndi };
}
