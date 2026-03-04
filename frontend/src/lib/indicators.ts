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
 * CCI (Commodity Channel Index)
 * Identifies cyclical turns in commodities, equities, and currencies.
 */
export function calcCCI(highs: number[], lows: number[], closes: number[], period = 20): (number | null)[] {
    const cci: (number | null)[] = [];
    if (closes.length < period) return closes.map(() => null);

    const formatTP = (h: number, l: number, c: number) => (h + l + c) / 3;
    const tpArr = closes.map((c, i) => formatTP(highs[i], lows[i], c));

    for (let i = 0; i < closes.length; i++) {
        if (i < period - 1) {
            cci.push(null);
            continue;
        }

        const slice = tpArr.slice(i - period + 1, i + 1);
        const smaTP = slice.reduce((a, b) => a + b, 0) / period;

        let meanDeviation = 0;
        for (const t of slice) {
            meanDeviation += Math.abs(t - smaTP);
        }
        meanDeviation /= period;

        if (meanDeviation === 0) {
            cci.push(0);
        } else {
            cci.push((tpArr[i] - smaTP) / (0.015 * meanDeviation));
        }
    }

    return cci;
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

export function calcWilliamsR(highs: number[], lows: number[], closes: number[], period = 14): (number | null)[] {
    const res: (number | null)[] = [];
    if (closes.length < period) return closes.map(() => null);

    for (let i = 0; i < closes.length; i++) {
        if (i < period - 1) {
            res.push(null);
            continue;
        }
        const sliceH = highs.slice(i - period + 1, i + 1);
        const sliceL = lows.slice(i - period + 1, i + 1);
        const hh = Math.max(...sliceH);
        const ll = Math.min(...sliceL);
        const w = (hh - closes[i]) / (hh - ll === 0 ? 1 : hh - ll) * -100;
        res.push(w);
    }
    return res;
}

export function calcSupertrend(highs: number[], lows: number[], closes: number[], period = 10, multiplier = 3) {
    const atr = calcATR(highs, lows, closes, period);
    const supertrend: (number | null)[] = [];
    const dir: (1 | -1 | null)[] = []; // 1 = up, -1 = down

    if (closes.length === 0) return { supertrend, dir };

    let currentDir = 1;
    let finalUpper = 0;
    let finalLower = 0;

    for (let i = 0; i < closes.length; i++) {
        if (atr[i] === null) {
            supertrend.push(null);
            dir.push(null);
            continue;
        }

        const basicUpper = (highs[i] + lows[i]) / 2 + multiplier * atr[i]!;
        const basicLower = (highs[i] + lows[i]) / 2 - multiplier * atr[i]!;

        if (i === 0 || atr[i - 1] === null) {
            finalUpper = basicUpper;
            finalLower = basicLower;
            currentDir = 1;
            supertrend.push(finalLower);
            dir.push(currentDir as 1);
            continue;
        }

        const prevClose = closes[i - 1];

        finalUpper = (basicUpper < finalUpper || prevClose > finalUpper) ? basicUpper : finalUpper;
        finalLower = (basicLower > finalLower || prevClose < finalLower) ? basicLower : finalLower;

        if (currentDir === 1 && closes[i] < finalLower) {
            currentDir = -1;
        } else if (currentDir === -1 && closes[i] > finalUpper) {
            currentDir = 1;
        }

        supertrend.push(currentDir === 1 ? finalLower : finalUpper);
        dir.push(currentDir as 1 | -1);
    }
    return { supertrend, dir };
}

export function calcParabolicSAR(highs: number[], lows: number[], step = 0.02, maxStep = 0.2) {
    const len = highs.length;
    const sar: (number | null)[] = Array(len).fill(null);
    if (len < 2) return sar;

    let isUp = true;
    let ep = highs[0];
    let currentSAR = lows[0];
    let af = step;

    for (let i = 1; i < len; i++) {
        const prevSAR = currentSAR;

        if (isUp) {
            currentSAR = prevSAR + af * (ep - prevSAR);
            if (currentSAR > lows[i]) currentSAR = lows[i];
            if (i > 1 && currentSAR > lows[i - 1]) currentSAR = lows[i - 1];

            if (lows[i] < currentSAR) {
                isUp = false;
                currentSAR = Math.max(ep, highs[i]); // Revert to recent extreme
                ep = lows[i];
                af = step;
            } else if (highs[i] > ep) {
                ep = highs[i];
                af = Math.min(af + step, maxStep);
            }
        } else {
            currentSAR = prevSAR + af * (ep - prevSAR);
            if (currentSAR < highs[i]) currentSAR = highs[i];
            if (i > 1 && currentSAR < highs[i - 1]) currentSAR = highs[i - 1];

            if (highs[i] > currentSAR) {
                isUp = true;
                currentSAR = Math.min(ep, lows[i]); // Revert to recent extreme
                ep = highs[i];
                af = step;
            } else if (lows[i] < ep) {
                ep = lows[i];
                af = Math.min(af + step, maxStep);
            }
        }
        sar[i] = currentSAR;
    }
    sar[0] = null; // No SAR on first element
    return sar;
}

export function calcMFI(highs: number[], lows: number[], closes: number[], volumes: number[], period = 14): (number | null)[] {
    const mfi: (number | null)[] = [];
    if (closes.length < period) return closes.map(() => null);

    const typPrice = closes.map((c, i) => (highs[i] + lows[i] + c) / 3);
    const rawMoneyFlow = typPrice.map((tp, i) => tp * (volumes[i] || 0));

    for (let i = 0; i < closes.length; i++) {
        if (i < period) {
            mfi.push(null);
            continue;
        }

        let positiveFlow = 0;
        let negativeFlow = 0;

        for (let j = i - period + 1; j <= i; j++) {
            if (typPrice[j] > typPrice[j - 1]) {
                positiveFlow += rawMoneyFlow[j];
            } else if (typPrice[j] < typPrice[j - 1]) {
                negativeFlow += rawMoneyFlow[j];
            }
        }

        if (negativeFlow === 0) {
            mfi.push(100);
        } else {
            const mfr = positiveFlow / negativeFlow;
            mfi.push(100 - (100 / (1 + mfr)));
        }
    }
    return mfi;
}

export function calcCMF(highs: number[], lows: number[], closes: number[], volumes: number[], period = 20): (number | null)[] {
    const cmf: (number | null)[] = [];
    if (closes.length < period) return closes.map(() => null);

    const mfv = closes.map((c, i) => {
        const h = highs[i];
        const l = lows[i];
        const v = volumes[i] || 0;
        if (h === l) return 0;
        const multiplier = ((c - l) - (h - c)) / (h - l);
        return multiplier * v;
    });

    for (let i = 0; i < closes.length; i++) {
        if (i < period - 1) {
            cmf.push(null);
            continue;
        }
        let sumMFV = 0;
        let sumV = 0;
        for (let j = i - period + 1; j <= i; j++) {
            sumMFV += mfv[j];
            sumV += volumes[j] || 0;
        }
        cmf.push(sumV === 0 ? 0 : sumMFV / sumV);
    }
    return cmf;
}
