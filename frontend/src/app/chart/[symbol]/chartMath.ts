/* ─── Indicator Math ──────────────────────────────────────────────────── */

export function calcEMA(data: number[], period: number): number[] {
    const k = 2 / (period + 1);
    const ema: number[] = [data[0]];
    for (let i = 1; i < data.length; i++) ema.push(data[i] * k + ema[i - 1] * (1 - k));
    return ema;
}

export function calcSMA(data: number[], period: number): number[] {
    return data.map((_, i) => {
        if (i < period - 1) return NaN;
        const slice = data.slice(i - period + 1, i + 1);
        return slice.reduce((s, v) => s + v, 0) / period;
    });
}

export function calcLWMA(data: number[], period: number): number[] {
    const weights = Array.from({ length: period }, (_, i) => i + 1);
    const sumW = weights.reduce((a, b) => a + b, 0);
    return data.map((_, i) => {
        if (i < period - 1) return NaN;
        const slice = data.slice(i - period + 1, i + 1);
        return slice.reduce((s, v, j) => s + v * weights[j], 0) / sumW;
    });
}

export function calcMACD(closes: number[], fast: number, slow: number, signal: number) {
    const emaFast = calcEMA(closes, fast);
    const emaSlow = calcEMA(closes, slow);
    const macdLine = emaFast.map((v, i) => v - emaSlow[i]);
    const signalLine = calcEMA(macdLine, signal);
    const histogram = macdLine.map((v, i) => v - signalLine[i]);
    return { macdLine, signalLine, histogram };
}

export function calcStochastic(highs: number[], lows: number[], closes: number[], kP: number, dP: number, smooth: number) {
    const rawK: number[] = [];
    for (let i = 0; i < closes.length; i++) {
        if (i < kP - 1) { rawK.push(NaN); continue; }
        const hh = Math.max(...highs.slice(i - kP + 1, i + 1));
        const ll = Math.min(...lows.slice(i - kP + 1, i + 1));
        rawK.push(hh === ll ? 50 : ((closes[i] - ll) / (hh - ll)) * 100);
    }
    const kLine: number[] = [];
    for (let i = 0; i < rawK.length; i++) {
        if (i < kP - 1 + smooth - 1 || isNaN(rawK[i])) { kLine.push(NaN); continue; }
        const sl = rawK.slice(i - smooth + 1, i + 1).filter(v => !isNaN(v));
        kLine.push(sl.reduce((s, v) => s + v, 0) / sl.length);
    }
    const dLine: number[] = [];
    for (let i = 0; i < kLine.length; i++) {
        if (isNaN(kLine[i]) || i < kP - 1 + smooth - 1 + dP - 1) { dLine.push(NaN); continue; }
        const sl = kLine.slice(i - dP + 1, i + 1).filter(v => !isNaN(v));
        dLine.push(sl.reduce((s, v) => s + v, 0) / sl.length);
    }
    return { kLine, dLine };
}

/* ─── Fibonacci Retracement ──────────────────────────────────────────── */

export const FIB_LEVELS = [
    { ratio: 0, label: '0%', color: '#787B86' },
    { ratio: 0.236, label: '23.6%', color: '#F44336' },
    { ratio: 0.382, label: '38.2%', color: '#FF9800' },
    { ratio: 0.5, label: '50%', color: '#FFEB3B' },
    { ratio: 0.618, label: '61.8%', color: '#4CAF50' },
    { ratio: 0.786, label: '78.6%', color: '#2196F3' },
    { ratio: 1, label: '100%', color: '#787B86' },
];

export function calcFibLevels(highs: number[], lows: number[], lookback: number) {
    const recentHighs = highs.slice(-lookback);
    const recentLows = lows.slice(-lookback);
    const high = Math.max(...recentHighs);
    const low = Math.min(...recentLows);
    const diff = high - low;
    return FIB_LEVELS.map(f => ({
        ...f,
        price: high - diff * f.ratio,
    }));
}

/* ─── Bollinger Bands ────────────────────────────────────────────────── */

export function calcBollingerBands(closes: number[], period: number, multiplier: number) {
    const middle: number[] = [];
    const upper: number[] = [];
    const lower: number[] = [];

    for (let i = 0; i < closes.length; i++) {
        if (i < period - 1) {
            middle.push(NaN);
            upper.push(NaN);
            lower.push(NaN);
            continue;
        }
        const slice = closes.slice(i - period + 1, i + 1);
        const mean = slice.reduce((s, v) => s + v, 0) / period;
        const variance = slice.reduce((s, v) => s + (v - mean) ** 2, 0) / period;
        const std = Math.sqrt(variance);
        middle.push(mean);
        upper.push(mean + multiplier * std);
        lower.push(mean - multiplier * std);
    }
    return { middle, upper, lower };
}

/* ─── ATR (Average True Range) ───────────────────────────────────────── */

export function calcATR(highs: number[], lows: number[], closes: number[], period: number): number[] {
    const tr: number[] = [highs[0] - lows[0]];
    for (let i = 1; i < closes.length; i++) {
        tr.push(Math.max(
            highs[i] - lows[i],
            Math.abs(highs[i] - closes[i - 1]),
            Math.abs(lows[i] - closes[i - 1])
        ));
    }
    const atr: number[] = [];
    let sum = 0;
    for (let i = 0; i < tr.length; i++) {
        if (i < period) {
            sum += tr[i];
            atr.push(i === period - 1 ? sum / period : NaN);
        } else {
            const prev = atr[i - 1];
            atr.push((prev * (period - 1) + tr[i]) / period);
        }
    }
    return atr;
}

/* ─── Parabolic SAR ───────────────────────────────────────────────────── */

export function calcParabolicSAR(highs: number[], lows: number[], step = 0.02, maxStep = 0.2) {
    const len = highs.length;
    const sar: (number | null)[] = Array(len).fill(null);
    if (len < 2) return sar;
    let isUp = true, ep = highs[0], currentSAR = lows[0], af = step;
    for (let i = 1; i < len; i++) {
        const prevSAR = currentSAR;
        if (isUp) {
            currentSAR = prevSAR + af * (ep - prevSAR);
            if (currentSAR > lows[i]) currentSAR = lows[i];
            if (i > 1 && currentSAR > lows[i - 1]) currentSAR = lows[i - 1];
            if (lows[i] < currentSAR) { isUp = false; currentSAR = Math.max(ep, highs[i]); ep = lows[i]; af = step; }
            else if (highs[i] > ep) { ep = highs[i]; af = Math.min(af + step, maxStep); }
        } else {
            currentSAR = prevSAR + af * (ep - prevSAR);
            if (currentSAR < highs[i]) currentSAR = highs[i];
            if (i > 1 && currentSAR < highs[i - 1]) currentSAR = highs[i - 1];
            if (highs[i] > currentSAR) { isUp = true; currentSAR = Math.min(ep, lows[i]); ep = highs[i]; af = step; }
            else if (lows[i] < ep) { ep = lows[i]; af = Math.min(af + step, maxStep); }
        }
        sar[i] = currentSAR;
    }
    return sar;
}

/* ─── Supertrend ──────────────────────────────────────────────────────── */

export function calcSupertrend(highs: number[], lows: number[], closes: number[], period = 10, multiplier = 3) {
    const atr = calcATR(highs, lows, closes, period);
    const supertrend: (number | null)[] = [];
    const dir: (1 | -1 | null)[] = [];
    if (closes.length === 0) return { supertrend, dir };
    let currentDir = 1, finalUpper = 0, finalLower = 0;
    for (let i = 0; i < closes.length; i++) {
        if (isNaN(atr[i])) { supertrend.push(null); dir.push(null); continue; }
        const basicUpper = (highs[i] + lows[i]) / 2 + multiplier * atr[i];
        const basicLower = (highs[i] + lows[i]) / 2 - multiplier * atr[i];
        if (i === 0 || isNaN(atr[i - 1])) { finalUpper = basicUpper; finalLower = basicLower; currentDir = 1; supertrend.push(finalLower); dir.push(1); continue; }
        const prevClose = closes[i - 1];
        finalUpper = (basicUpper < finalUpper || prevClose > finalUpper) ? basicUpper : finalUpper;
        finalLower = (basicLower > finalLower || prevClose < finalLower) ? basicLower : finalLower;
        if (currentDir === 1 && closes[i] < finalLower) currentDir = -1;
        else if (currentDir === -1 && closes[i] > finalUpper) currentDir = 1;
        supertrend.push(currentDir === 1 ? finalLower : finalUpper);
        dir.push(currentDir as 1 | -1);
    }
    return { supertrend, dir };
}

/* ─── Williams %R ─────────────────────────────────────────────────────── */

export function calcWilliamsR(highs: number[], lows: number[], closes: number[], period = 14): (number | null)[] {
    const res: (number | null)[] = [];
    for (let i = 0; i < closes.length; i++) {
        if (i < period - 1) { res.push(null); continue; }
        const hh = Math.max(...highs.slice(i - period + 1, i + 1));
        const ll = Math.min(...lows.slice(i - period + 1, i + 1));
        res.push((hh - closes[i]) / (hh - ll === 0 ? 1 : hh - ll) * -100);
    }
    return res;
}

/* ─── MFI (Money Flow Index) ──────────────────────────────────────────── */

export function calcMFI(highs: number[], lows: number[], closes: number[], volumes: number[], period = 14): (number | null)[] {
    const mfi: (number | null)[] = [];
    const typPrice = closes.map((c, i) => (highs[i] + lows[i] + c) / 3);
    const rawMF = typPrice.map((tp, i) => tp * (volumes[i] || 0));
    for (let i = 0; i < closes.length; i++) {
        if (i < period) { mfi.push(null); continue; }
        let pos = 0, neg = 0;
        for (let j = i - period + 1; j <= i; j++) {
            if (typPrice[j] > typPrice[j - 1]) pos += rawMF[j];
            else if (typPrice[j] < typPrice[j - 1]) neg += rawMF[j];
        }
        mfi.push(neg === 0 ? 100 : 100 - (100 / (1 + pos / neg)));
    }
    return mfi;
}

/* ─── CMF (Chaikin Money Flow) ────────────────────────────────────────── */

export function calcCMF(highs: number[], lows: number[], closes: number[], volumes: number[], period = 20): (number | null)[] {
    const cmf: (number | null)[] = [];
    const mfv = closes.map((c, i) => { const h = highs[i], l = lows[i], v = volumes[i] || 0; if (h === l) return 0; return ((c - l) - (h - c)) / (h - l) * v; });
    for (let i = 0; i < closes.length; i++) {
        if (i < period - 1) { cmf.push(null); continue; }
        let sumMFV = 0, sumV = 0;
        for (let j = i - period + 1; j <= i; j++) { sumMFV += mfv[j]; sumV += volumes[j] || 0; }
        cmf.push(sumV === 0 ? 0 : sumMFV / sumV);
    }
    return cmf;
}

/* ─── RSI (Relative Strength Index) ──────────────────────────────────── */

export function calcRSI(closes: number[], period = 14): (number | null)[] {
    const rsi: (number | null)[] = [];
    if (closes.length < period + 1) return closes.map(() => null);
    const changes: number[] = [];
    for (let i = 1; i < closes.length; i++) changes.push(closes[i] - closes[i - 1]);
    let avgGain = 0, avgLoss = 0;
    for (let i = 0; i < period; i++) { if (changes[i] >= 0) avgGain += changes[i]; else avgLoss += Math.abs(changes[i]); }
    avgGain /= period; avgLoss /= period;
    rsi.push(null);
    for (let i = 0; i < period - 1; i++) rsi.push(null);
    rsi.push(avgLoss === 0 ? 100 : 100 - 100 / (1 + avgGain / avgLoss));
    for (let i = period; i < changes.length; i++) {
        const gain = changes[i] >= 0 ? changes[i] : 0;
        const loss = changes[i] < 0 ? Math.abs(changes[i]) : 0;
        avgGain = (avgGain * (period - 1) + gain) / period;
        avgLoss = (avgLoss * (period - 1) + loss) / period;
        rsi.push(avgLoss === 0 ? 100 : 100 - 100 / (1 + avgGain / avgLoss));
    }
    return rsi;
}

/* ─── CCI (Commodity Channel Index) ──────────────────────────────────── */

export function calcCCI(highs: number[], lows: number[], closes: number[], period = 20): (number | null)[] {
    const cci: (number | null)[] = [];
    const tp = closes.map((c, i) => (highs[i] + lows[i] + c) / 3);
    for (let i = 0; i < closes.length; i++) {
        if (i < period - 1) { cci.push(null); continue; }
        const slice = tp.slice(i - period + 1, i + 1);
        const mean = slice.reduce((a, b) => a + b, 0) / period;
        let md = 0; for (const t of slice) md += Math.abs(t - mean); md /= period;
        cci.push(md === 0 ? 0 : (tp[i] - mean) / (0.015 * md));
    }
    return cci;
}

/* ─── ADX (Average Directional Index) ────────────────────────────────── */

export function calcADX(highs: number[], lows: number[], closes: number[], period = 14) {
    const len = closes.length;
    const adx: (number | null)[] = Array(len).fill(null);
    const pdi: (number | null)[] = Array(len).fill(null);
    const ndi: (number | null)[] = Array(len).fill(null);
    if (len < period + 1) return { adx, pdi, ndi };
    const tr = [0], pdm = [0], ndm = [0];
    for (let i = 1; i < len; i++) {
        tr.push(Math.max(highs[i] - lows[i], Math.abs(highs[i] - closes[i - 1]), Math.abs(lows[i] - closes[i - 1])));
        const up = highs[i] - highs[i - 1], dn = lows[i - 1] - lows[i];
        pdm.push(up > dn && up > 0 ? up : 0);
        ndm.push(dn > up && dn > 0 ? dn : 0);
    }
    let sTR = 0, sPDM = 0, sNDM = 0;
    for (let i = 1; i <= period; i++) { sTR += tr[i]; sPDM += pdm[i]; sNDM += ndm[i]; }
    let dxSum = 0;
    for (let i = period; i < len; i++) {
        if (i > period) { sTR = sTR - sTR / period + tr[i]; sPDM = sPDM - sPDM / period + pdm[i]; sNDM = sNDM - sNDM / period + ndm[i]; }
        const dp = sTR === 0 ? 0 : 100 * sPDM / sTR;
        const dm = sTR === 0 ? 0 : 100 * sNDM / sTR;
        pdi[i] = dp; ndi[i] = dm;
        const dx = (dp + dm === 0) ? 0 : 100 * Math.abs(dp - dm) / (dp + dm);
        if (i < 2 * period - 1) dxSum += dx;
        else if (i === 2 * period - 1) { dxSum += dx; adx[i] = dxSum / period; }
        else adx[i] = ((adx[i - 1]! * (period - 1)) + dx) / period;
    }
    return { adx, pdi, ndi };
}

/* ─── Frontend Volume Profile ─────────────────────────────────────────── */

export function calcVolumeProfile(highs: number[], lows: number[], volumes: number[], numBins = 60, vaPct = 0.70) {
    const minP = Math.min(...lows), maxP = Math.max(...highs);
    if (minP === maxP) return { poc: minP, vah: minP, val: minP, bins: [] as number[], binSize: 0, minP, pocIdx: 0, vaLo: 0, vaHi: 0 };

    // Fallback to TPO (Time Price Opportunity) if volume is zero (e.g., Forex)
    const sumVol = volumes.reduce((s, v) => s + (v || 0), 0);
    const effVols = sumVol === 0 ? volumes.map(() => 1) : volumes;

    const binSize = (maxP - minP) / numBins;
    const bins = new Array(numBins).fill(0);
    for (let k = 0; k < highs.length; k++) {
        const si = Math.max(0, Math.floor((lows[k] - minP) / binSize));
        const ei = Math.min(numBins - 1, Math.floor((highs[k] - minP) / binSize));
        const v = effVols[k] || 0;
        const perBin = si === ei ? v : v / (ei - si + 1);
        for (let b = si; b <= ei; b++) bins[b] += perBin;
    }
    const pocIdx = bins.indexOf(Math.max(...bins));
    const poc = minP + (pocIdx + 0.5) * binSize;
    const totalV = bins.reduce((s: number, v: number) => s + v, 0);
    const targetV = totalV * vaPct;
    let lo = pocIdx, hi = pocIdx, cur = bins[pocIdx];
    while (cur < targetV && (lo > 0 || hi < numBins - 1)) {
        const vu = hi < numBins - 1 ? bins[hi + 1] : -1;
        const vd = lo > 0 ? bins[lo - 1] : -1;
        if (vu >= vd && vu >= 0) { hi++; cur += vu; } else if (vd >= 0) { lo--; cur += vd; } else break;
    }
    return { poc, vah: minP + (hi + 1) * binSize, val: minP + lo * binSize, bins, binSize, minP, pocIdx, vaLo: lo, vaHi: hi };
}

/* ─── MA Types ────────────────────────────────────────────────────────── */

export type MAType = "EMA" | "SMA" | "LWMA";

export interface MAConfig {
    id: string;
    type: MAType;
    period: number;
    color: string;
    visible: boolean;
}

export const DEFAULT_MAS: MAConfig[] = [
    { id: "ma1", type: "EMA", period: 54, color: "#fbbf24", visible: true },
    { id: "ma2", type: "LWMA", period: 142, color: "#f472b6", visible: true },
    { id: "ma3", type: "SMA", period: 400, color: "#38bdf8", visible: true },
    { id: "ma4", type: "LWMA", period: 14, color: "#a78bfa", visible: true },
];

export function calcMA(type: MAType, data: number[], period: number): number[] {
    if (type === "EMA") return calcEMA(data, period);
    if (type === "SMA") return calcSMA(data, period);
    if (type === "LWMA") return calcLWMA(data, period);
    return [];
}
