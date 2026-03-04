"use client"

import { useParams, useRouter } from "next/navigation";
import { useEffect, useRef, useState, useCallback } from "react";
import { createChart, ColorType, CandlestickSeries, LineSeries, HistogramSeries, IChartApi } from "lightweight-charts";
import { TrendingUp, TrendingDown, ChevronDown, ChevronUp, ArrowLeft, BarChart2, X } from "lucide-react";

/* ─── Indicator Math ──────────────────────────────────────────────────── */

function calcEMA(data: number[], period: number): number[] {
    const k = 2 / (period + 1);
    const ema: number[] = [data[0]];
    for (let i = 1; i < data.length; i++) ema.push(data[i] * k + ema[i - 1] * (1 - k));
    return ema;
}

function calcSMA(data: number[], period: number): number[] {
    return data.map((_, i) => {
        if (i < period - 1) return NaN;
        const slice = data.slice(i - period + 1, i + 1);
        return slice.reduce((s, v) => s + v, 0) / period;
    });
}

function calcLWMA(data: number[], period: number): number[] {
    const weights = Array.from({ length: period }, (_, i) => i + 1);
    const sumW = weights.reduce((a, b) => a + b, 0);
    return data.map((_, i) => {
        if (i < period - 1) return NaN;
        const slice = data.slice(i - period + 1, i + 1);
        return slice.reduce((s, v, j) => s + v * weights[j], 0) / sumW;
    });
}

function calcMACD(closes: number[], fast: number, slow: number, signal: number) {
    const emaFast = calcEMA(closes, fast);
    const emaSlow = calcEMA(closes, slow);
    const macdLine = emaFast.map((v, i) => v - emaSlow[i]);
    const signalLine = calcEMA(macdLine, signal);
    const histogram = macdLine.map((v, i) => v - signalLine[i]);
    return { macdLine, signalLine, histogram };
}

function calcStochastic(highs: number[], lows: number[], closes: number[], kP: number, dP: number, smooth: number) {
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

const FIB_LEVELS = [
    { ratio: 0, label: '0%', color: '#787B86' },
    { ratio: 0.236, label: '23.6%', color: '#F44336' },
    { ratio: 0.382, label: '38.2%', color: '#FF9800' },
    { ratio: 0.5, label: '50%', color: '#FFEB3B' },
    { ratio: 0.618, label: '61.8%', color: '#4CAF50' },
    { ratio: 0.786, label: '78.6%', color: '#2196F3' },
    { ratio: 1, label: '100%', color: '#787B86' },
];

function calcFibLevels(highs: number[], lows: number[], lookback: number) {
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

function calcBollingerBands(closes: number[], period: number, multiplier: number) {
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

function calcATR(highs: number[], lows: number[], closes: number[], period: number): number[] {
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

function calcParabolicSAR(highs: number[], lows: number[], step = 0.02, maxStep = 0.2) {
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

function calcSupertrend(highs: number[], lows: number[], closes: number[], period = 10, multiplier = 3) {
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

function calcWilliamsR(highs: number[], lows: number[], closes: number[], period = 14): (number | null)[] {
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

function calcMFI(highs: number[], lows: number[], closes: number[], volumes: number[], period = 14): (number | null)[] {
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

function calcCMF(highs: number[], lows: number[], closes: number[], volumes: number[], period = 20): (number | null)[] {
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

/* ─── Frontend Volume Profile ─────────────────────────────────────────── */

function calcVolumeProfile(highs: number[], lows: number[], volumes: number[], numBins = 50, vaPct = 0.70) {
    const minP = Math.min(...lows), maxP = Math.max(...highs);
    if (minP === maxP) return { poc: minP, vah: minP, val: minP };
    const binSize = (maxP - minP) / numBins;
    const bins = new Array(numBins).fill(0);
    for (let k = 0; k < highs.length; k++) {
        const si = Math.max(0, Math.floor((lows[k] - minP) / binSize));
        const ei = Math.min(numBins - 1, Math.floor((highs[k] - minP) / binSize));
        const perBin = si === ei ? volumes[k] : volumes[k] / (ei - si + 1);
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
    return { poc, vah: minP + (hi + 1) * binSize, val: minP + lo * binSize };
}

/* ─── MA Types ────────────────────────────────────────────────────────── */

type MAType = "EMA" | "SMA" | "LWMA";

interface MAConfig {
    id: string;
    type: MAType;
    period: number;
    color: string;
    visible: boolean;
}

const DEFAULT_MAS: MAConfig[] = [
    { id: "ma1", type: "EMA", period: 54, color: "#fbbf24", visible: true },
    { id: "ma2", type: "LWMA", period: 142, color: "#f472b6", visible: true },
    { id: "ma3", type: "SMA", period: 400, color: "#38bdf8", visible: true },
    { id: "ma4", type: "LWMA", period: 14, color: "#a78bfa", visible: true },
];

function calcMA(type: MAType, data: number[], period: number): number[] {
    if (type === "EMA") return calcEMA(data, period);
    if (type === "SMA") return calcSMA(data, period);
    if (type === "LWMA") return calcLWMA(data, period);
    return [];
}

/* ─── MA Chip (individual control in toolbar) ────────────────────────── */

function MAChip({ ma, onChange, onRemove }: {
    ma: MAConfig;
    onChange: (updated: MAConfig) => void;
    onRemove: () => void;
}) {
    const [editing, setEditing] = useState(false);
    const types: MAType[] = ["EMA", "SMA", "LWMA"];

    return (
        <div className="relative flex items-center gap-1.5">
            <div
                onClick={() => setEditing(!editing)}
                className={`flex items-center gap-1.5 px-2.5 py-1 rounded-md border cursor-pointer select-none transition-all text-[11px] font-bold uppercase tracking-wide ${ma.visible ? "bg-white/5 border-white/10 text-white hover:bg-white/10" : "bg-transparent border-white/5 text-white/30"}`}
            >
                <div className="h-2 w-2 rounded-full flex-shrink-0" style={{ backgroundColor: ma.visible ? ma.color : "#333", boxShadow: ma.visible ? `0 0 6px ${ma.color}` : "none" }} />
                <span style={{ color: ma.visible ? ma.color : "#555" }}>{ma.type}({ma.period})</span>
            </div>

            {editing && (
                <div className="absolute top-8 left-0 z-50 bg-[#111] border border-white/10 rounded-lg p-3 shadow-2xl flex flex-col gap-3 min-w-[180px]" onClick={e => e.stopPropagation()}>
                    {/* Toggle visibility */}
                    <div className="flex items-center justify-between">
                        <span className="text-[9px] font-black text-white/40 uppercase tracking-widest">Visible</span>
                        <button
                            onClick={() => onChange({ ...ma, visible: !ma.visible })}
                            className={`relative w-8 h-4 rounded-full transition-all ${ma.visible ? "bg-accent" : "bg-white/10"}`}
                        >
                            <div className={`absolute top-0.5 h-3 w-3 rounded-full bg-white transition-all ${ma.visible ? "left-4.5" : "left-0.5"}`} />
                        </button>
                    </div>

                    {/* Type selector */}
                    <div>
                        <span className="text-[9px] font-black text-white/40 uppercase tracking-widest">Type</span>
                        <div className="flex gap-1 mt-1">
                            {types.map(t => (
                                <button
                                    key={t}
                                    onClick={() => onChange({ ...ma, type: t })}
                                    className={`flex-1 py-0.5 text-[10px] font-bold rounded transition-all ${ma.type === t ? "bg-accent text-black" : "bg-white/5 text-white/50 hover:bg-white/10"}`}
                                >{t}</button>
                            ))}
                        </div>
                    </div>

                    {/* Period */}
                    <div>
                        <span className="text-[9px] font-black text-white/40 uppercase tracking-widest">Period</span>
                        <input
                            type="number"
                            value={ma.period}
                            min={1}
                            max={1000}
                            onChange={e => onChange({ ...ma, period: Number(e.target.value) || 1 })}
                            className="mt-1 w-full px-2 py-1 bg-white/5 border border-white/10 rounded text-xs text-white font-mono text-center focus:outline-none focus:border-accent/50"
                        />
                    </div>

                    {/* Color + Remove */}
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-2">
                            <span className="text-[9px] font-black text-white/40 uppercase tracking-widest">Color</span>
                            <input
                                type="color"
                                value={ma.color}
                                onChange={e => onChange({ ...ma, color: e.target.value })}
                                className="w-6 h-6 rounded cursor-pointer border-0 bg-transparent"
                            />
                        </div>
                        <button onClick={onRemove} className="text-red-400 hover:text-red-300 transition-colors p-1">
                            <X size={12} />
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}

/* ─── Param Input ─────────────────────────────────────────────────────── */

function ParamInput({ label, value, onChange, min = 1, max = 200 }: { label: string; value: number; onChange: (v: number) => void; min?: number; max?: number }) {
    return (
        <div className="flex items-center gap-1.5">
            <label className="text-[10px] font-bold uppercase tracking-wider text-white/40 whitespace-nowrap">{label}</label>
            <input
                type="number"
                value={value}
                min={min}
                max={max}
                onChange={(e) => onChange(Math.max(min, Math.min(max, Number(e.target.value) || min)))}
                className="w-14 px-1.5 py-0.5 bg-white/5 border border-white/10 rounded text-xs text-white font-mono text-center focus:outline-none focus:border-accent/50"
            />
        </div>
    );
}

/* ─── Main Component ──────────────────────────────────────────────────── */

export default function ChartWindow() {
    const params = useParams();
    const router = useRouter();
    const symbol = typeof params.symbol === 'string' ? decodeURIComponent(params.symbol) : '';

    const mainChartRef = useRef<HTMLDivElement>(null);
    const macdChartRef = useRef<HTMLDivElement>(null);
    const stochChartRef = useRef<HTMLDivElement>(null);
    const mainChartApi = useRef<IChartApi | null>(null);
    const macdChartApi = useRef<IChartApi | null>(null);
    const stochChartApi = useRef<IChartApi | null>(null);

    const [loading, setLoading] = useState(true);
    const [quote, setQuote] = useState<{ price: number; changePercentage: number } | null>(null);
    const [rawData, setRawData] = useState<any[]>([]);

    // Moving averages
    const [mas, setMas] = useState<MAConfig[]>(DEFAULT_MAS);
    const [indicatorsOpen, setIndicatorsOpen] = useState(false);

    // Oscillator visibility
    const [showMACD, setShowMACD] = useState(true);
    const [showStoch, setShowStoch] = useState(true);

    // Volume Profile visibility
    const [showVP, setShowVP] = useState(false);

    // MACD params
    const [macdFast, setMacdFast] = useState(12);
    const [macdSlow, setMacdSlow] = useState(26);
    const [macdSignal, setMacdSignal] = useState(9);

    // Stochastic params
    const [stochK, setStochK] = useState(14);
    const [stochD, setStochD] = useState(3);
    const [stochSmooth, setStochSmooth] = useState(3);

    // Fibonacci params
    const [showFib, setShowFib] = useState(false);
    const [fibLookback, setFibLookback] = useState(120);

    // Bollinger Bands params
    const [showBB, setShowBB] = useState(false);
    const [bbPeriod, setBbPeriod] = useState(20);
    const [bbMult, setBbMult] = useState(2.0);

    // ATR params
    const [showATR, setShowATR] = useState(false);
    const [atrPeriod, setAtrPeriod] = useState(14);
    const atrChartRef = useRef<HTMLDivElement>(null);
    const atrChartApi = useRef<IChartApi | null>(null);

    // Parabolic SAR
    const [showPSAR, setShowPSAR] = useState(false);

    // Supertrend
    const [showSupertrend, setShowSupertrend] = useState(false);

    // Williams %R
    const [showWilliams, setShowWilliams] = useState(false);
    const williamsChartRef = useRef<HTMLDivElement>(null);
    const williamsChartApi = useRef<IChartApi | null>(null);

    // MFI
    const [showMFI, setShowMFI] = useState(false);
    const mfiChartRef = useRef<HTMLDivElement>(null);
    const mfiChartApi = useRef<IChartApi | null>(null);

    // CMF
    const [showCMF, setShowCMF] = useState(false);
    const cmfChartRef = useRef<HTMLDivElement>(null);
    const cmfChartApi = useRef<IChartApi | null>(null);

    // Timeframe
    const [timeframe, setTimeframe] = useState("daily");
    const TIMEFRAMES = [
        { label: "5m", value: "5m" },
        { label: "15m", value: "15m" },
        { label: "1H", value: "1h" },
        { label: "4H", value: "4h" },
        { label: "1D", value: "daily" },
        { label: "1W", value: "weekly" },
        { label: "1M", value: "monthly" },
    ];

    const isIntradayTF = ["5m", "15m", "1h", "4h"].includes(timeframe);

    // Normalize time: intraday datetimes → Unix timestamp (seconds), daily → YYYY-MM-DD string
    const normalizeTime = (dateStr: string) => {
        if (!dateStr) return 0;
        // If it contains a space or T, it's a datetime → convert to UTC epoch seconds
        if (dateStr.includes(' ') || dateStr.includes('T')) {
            return Math.floor(new Date(dateStr).getTime() / 1000);
        }
        // YYYY-MM-DD string is fine for business-day charts
        return dateStr;
    };

    const chartOpts = useCallback((height?: number) => ({
        layout: {
            background: { type: ColorType.Solid as const, color: '#0a0a0a' },
            textColor: '#71717a',
            fontSize: 10,
        },
        grid: {
            vertLines: { color: '#141414' },
            horzLines: { color: '#141414' },
        },
        timeScale: { borderColor: '#1f1f1f', timeVisible: isIntradayTF },
        rightPriceScale: { borderColor: '#1f1f1f' },
        crosshair: {
            vertLine: { labelBackgroundColor: '#2962FF' },
            horzLine: { labelBackgroundColor: '#2962FF' },
        },
        ...(height ? { height } : {}),
    }), [isIntradayTF]);

    // Fetch data — historical + quote in PARALLEL
    useEffect(() => {
        if (!symbol) return;
        const fetchData = async () => {
            try {
                const isIntraday = ["5m", "15m", "1h", "4h"].includes(timeframe);
                const periodMap: Record<string, string> = { "5m": "5d", "15m": "5d", "1h": "1mo", "4h": "3mo" };
                const dataUrl = isIntraday
                    ? `http://localhost:8282/api/v1/market/intraday/${encodeURIComponent(symbol)}?interval=${timeframe}&period=${periodMap[timeframe] || "1mo"}`
                    : `http://localhost:8282/api/v1/market/historical/${encodeURIComponent(symbol)}?limit=10000`;

                const [res, qRes] = await Promise.all([
                    fetch(dataUrl),
                    fetch(`http://localhost:8282/api/v1/market/quote/${encodeURIComponent(symbol)}`)
                ]);
                const data = await res.json();
                if (data.historical) {
                    const mapped = data.historical.map((d: any) => ({
                        ...d,
                        date: d.date || d.timestamp || d.time || d.ts || ""
                    }));
                    setRawData(mapped.sort((a: any, b: any) => String(a.date).localeCompare(String(b.date))));
                } else {
                    setRawData([]);
                }
                const q = await qRes.json();
                if (q && !q.error && typeof q.price === 'number') {
                    setQuote({ price: q.price, changePercentage: q.changePercentage ?? 0 });
                }
            } catch (err) {
                console.error("Fetch error:", err);
                setRawData([]);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [symbol, timeframe]);

    // Compute Volume Profile from loaded data (frontend)
    const vpData = showVP && rawData.length > 20 ? (() => {
        const highs = rawData.map((d: any) => d.high);
        const lows = rawData.map((d: any) => d.low);
        const volumes = rawData.map((d: any) => d.volume ?? 0);
        return calcVolumeProfile(highs, lows, volumes);
    })() : null;

    // Main Chart + MAs
    useEffect(() => {
        if (!mainChartRef.current || rawData.length === 0) return;
        if (mainChartApi.current) { mainChartApi.current.remove(); mainChartApi.current = null; }

        const chart = createChart(mainChartRef.current, {
            ...chartOpts(),
            width: mainChartRef.current.clientWidth,
            height: mainChartRef.current.clientHeight || 400,
        });
        mainChartApi.current = chart;

        const candleSeries = chart.addSeries(CandlestickSeries, {
            upColor: '#26a69d', downColor: '#ef5350',
            borderVisible: false, wickUpColor: '#26a69d', wickDownColor: '#ef5350',
        });
        candleSeries.setData(rawData.map(d => ({ time: normalizeTime(d.date) as any, open: d.open, high: d.high, low: d.low, close: d.close })));

        // Render Volume Profile Price Lines (frontend computed)
        if (showVP && vpData && typeof vpData.poc === 'number') {
            candleSeries.createPriceLine({ price: vpData.poc, color: '#FFD700', lineWidth: 2, lineStyle: 0, axisLabelVisible: true, title: 'POC' });
            candleSeries.createPriceLine({ price: vpData.vah, color: '#FF6D00', lineWidth: 1, lineStyle: 1, axisLabelVisible: true, title: 'VAH' });
            candleSeries.createPriceLine({ price: vpData.val, color: '#FF6D00', lineWidth: 1, lineStyle: 1, axisLabelVisible: true, title: 'VAL' });
        }

        // Render Moving Averages
        const closes = rawData.map(d => d.close);
        const times = rawData.map(d => normalizeTime(d.date) as any);
        const highs = rawData.map(d => d.high);
        const lows = rawData.map(d => d.low);
        const volumes = rawData.map(d => d.volume ?? 0);

        for (const ma of mas) {
            if (!ma.visible) continue;
            const values = calcMA(ma.type, closes, ma.period);
            const series = chart.addSeries(LineSeries, { color: ma.color, lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false });
            series.setData(values.map((v, i) => ({ time: times[i], value: v })).filter(d => !isNaN(d.value)) as any);
        }

        // Render Fibonacci Retracement
        if (showFib && rawData.length > 0) {
            const fibs = calcFibLevels(highs, lows, fibLookback);
            for (const fib of fibs) {
                candleSeries.createPriceLine({ price: fib.price, color: fib.color, lineWidth: 1, lineStyle: 2, axisLabelVisible: true, title: `Fib ${fib.label}` });
            }
        }

        // Render Bollinger Bands
        if (showBB) {
            const { middle, upper, lower } = calcBollingerBands(closes, bbPeriod, bbMult);
            chart.addSeries(LineSeries, { color: 'rgba(33,150,243,0.5)', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(upper.map((v, i) => ({ time: times[i], value: v })).filter(d => !isNaN(d.value)) as any);
            chart.addSeries(LineSeries, { color: 'rgba(33,150,243,0.3)', lineWidth: 1, lineStyle: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(middle.map((v, i) => ({ time: times[i], value: v })).filter(d => !isNaN(d.value)) as any);
            chart.addSeries(LineSeries, { color: 'rgba(33,150,243,0.5)', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(lower.map((v, i) => ({ time: times[i], value: v })).filter(d => !isNaN(d.value)) as any);
        }

        // Parabolic SAR (dotted line)
        if (showPSAR && rawData.length > 5) {
            const sar = calcParabolicSAR(highs, lows);
            chart.addSeries(LineSeries, { color: '#ec4899', lineWidth: 1, lineStyle: 3, pointMarkersVisible: true, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(times.map((t, i) => sar[i] !== null ? { time: t, value: sar[i]! } : null).filter(Boolean) as any);
        }

        // Supertrend overlay
        if (showSupertrend && rawData.length > 20) {
            const { supertrend, dir } = calcSupertrend(highs, lows, closes);
            const upData = times.map((t, i) => dir[i] === 1 && supertrend[i] !== null ? { time: t, value: supertrend[i]! } : null).filter(Boolean);
            const downData = times.map((t, i) => dir[i] === -1 && supertrend[i] !== null ? { time: t, value: supertrend[i]! } : null).filter(Boolean);
            chart.addSeries(LineSeries, { color: '#2dd4bf', lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(upData as any);
            chart.addSeries(LineSeries, { color: '#ef4444', lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(downData as any);
        }

        chart.timeScale().fitContent();

        const handleResize = () => {
            if (mainChartRef.current) chart.applyOptions({ width: mainChartRef.current.clientWidth });
        };
        window.addEventListener('resize', handleResize);
        return () => { window.removeEventListener('resize', handleResize); chart.remove(); mainChartApi.current = null; };
    }, [rawData, chartOpts, mas, showVP, showFib, fibLookback, showBB, bbPeriod, bbMult, showPSAR, showSupertrend]);

    // MACD
    useEffect(() => {
        if (!macdChartRef.current || rawData.length === 0 || !showMACD) return;
        if (macdChartApi.current) { macdChartApi.current.remove(); macdChartApi.current = null; }

        const chart = createChart(macdChartRef.current, { ...chartOpts(146), width: macdChartRef.current.clientWidth });
        macdChartApi.current = chart;

        const closes = rawData.map(d => d.close);
        const times = rawData.map(d => normalizeTime(d.date) as any);
        const { macdLine, signalLine, histogram } = calcMACD(closes, macdFast, macdSlow, macdSignal);

        const histSeries = chart.addSeries(HistogramSeries, { priceLineVisible: false, lastValueVisible: false });
        histSeries.setData(histogram.map((v, i) => ({ time: times[i], value: v, color: v >= 0 ? 'rgba(38,166,157,0.5)' : 'rgba(239,83,80,0.5)' })));

        const macdSeries = chart.addSeries(LineSeries, { color: '#2962FF', lineWidth: 1, priceLineVisible: false, lastValueVisible: false });
        macdSeries.setData(macdLine.map((v, i) => ({ time: times[i], value: v })));

        const signalSeries = chart.addSeries(LineSeries, { color: '#FF6D00', lineWidth: 1, priceLineVisible: false, lastValueVisible: false });
        signalSeries.setData(signalLine.map((v, i) => ({ time: times[i], value: v })));

        chart.timeScale().fitContent();

        if (mainChartApi.current) {
            mainChartApi.current.timeScale().subscribeVisibleLogicalRangeChange(r => { if (r && macdChartApi.current) macdChartApi.current.timeScale().setVisibleLogicalRange(r); });
            chart.timeScale().subscribeVisibleLogicalRangeChange(r => { if (r && mainChartApi.current) mainChartApi.current.timeScale().setVisibleLogicalRange(r); });
        }

        const hr = () => { if (macdChartRef.current) chart.applyOptions({ width: macdChartRef.current.clientWidth }); };
        window.addEventListener('resize', hr);
        return () => { window.removeEventListener('resize', hr); chart.remove(); macdChartApi.current = null; };
    }, [rawData, showMACD, macdFast, macdSlow, macdSignal, chartOpts]);

    // Stochastic
    useEffect(() => {
        if (!stochChartRef.current || rawData.length === 0 || !showStoch) return;
        if (stochChartApi.current) { stochChartApi.current.remove(); stochChartApi.current = null; }

        const chart = createChart(stochChartRef.current, { ...chartOpts(146), width: stochChartRef.current.clientWidth });
        stochChartApi.current = chart;

        const highs = rawData.map(d => d.high);
        const lows = rawData.map(d => d.low);
        const closes = rawData.map(d => d.close);
        const times = rawData.map(d => normalizeTime(d.date) as any);
        const { kLine, dLine } = calcStochastic(highs, lows, closes, stochK, stochD, stochSmooth);

        const kSeries = chart.addSeries(LineSeries, { color: '#2962FF', lineWidth: 1, priceLineVisible: false, lastValueVisible: false, title: '%K' });
        kSeries.setData(kLine.map((v, i) => ({ time: times[i], value: v })).filter((_, i) => !isNaN(kLine[i])));

        const dSeries = chart.addSeries(LineSeries, { color: '#FF6D00', lineWidth: 1, priceLineVisible: false, lastValueVisible: false, title: '%D' });
        dSeries.setData(dLine.map((v, i) => ({ time: times[i], value: v })).filter((_, i) => !isNaN(dLine[i])));

        chart.timeScale().fitContent();

        if (mainChartApi.current) {
            mainChartApi.current.timeScale().subscribeVisibleLogicalRangeChange(r => { if (r && stochChartApi.current) stochChartApi.current.timeScale().setVisibleLogicalRange(r); });
            chart.timeScale().subscribeVisibleLogicalRangeChange(r => { if (r && mainChartApi.current) mainChartApi.current.timeScale().setVisibleLogicalRange(r); });
        }

        const hr = () => { if (stochChartRef.current) chart.applyOptions({ width: stochChartRef.current.clientWidth }); };
        window.addEventListener('resize', hr);
        return () => { window.removeEventListener('resize', hr); chart.remove(); stochChartApi.current = null; };
    }, [rawData, showStoch, stochK, stochD, stochSmooth, chartOpts]);

    // ATR
    useEffect(() => {
        if (!atrChartRef.current || rawData.length === 0 || !showATR) return;
        if (atrChartApi.current) { atrChartApi.current.remove(); atrChartApi.current = null; }

        const chart = createChart(atrChartRef.current, { ...chartOpts(146), width: atrChartRef.current.clientWidth });
        atrChartApi.current = chart;

        const highs = rawData.map(d => d.high);
        const lows = rawData.map(d => d.low);
        const closes = rawData.map(d => d.close);
        const times = rawData.map(d => normalizeTime(d.date) as any);
        const atrValues = calcATR(highs, lows, closes, atrPeriod);

        const atrSeries = chart.addSeries(LineSeries, { color: '#e040fb', lineWidth: 2, priceLineVisible: false, lastValueVisible: true, title: 'ATR' });
        atrSeries.setData(atrValues.map((v, i) => ({ time: times[i], value: v })).filter(d => !isNaN(d.value)));

        chart.timeScale().fitContent();

        if (mainChartApi.current) {
            mainChartApi.current.timeScale().subscribeVisibleLogicalRangeChange(r => { if (r && atrChartApi.current) atrChartApi.current.timeScale().setVisibleLogicalRange(r); });
            chart.timeScale().subscribeVisibleLogicalRangeChange(r => { if (r && mainChartApi.current) mainChartApi.current.timeScale().setVisibleLogicalRange(r); });
        }

        const hr = () => { if (atrChartRef.current) chart.applyOptions({ width: atrChartRef.current.clientWidth }); };
        window.addEventListener('resize', hr);
        return () => { window.removeEventListener('resize', hr); chart.remove(); atrChartApi.current = null; };
    }, [rawData, showATR, atrPeriod, chartOpts]);

    // Williams %R
    useEffect(() => {
        if (!williamsChartRef.current || rawData.length === 0 || !showWilliams) return;
        if (williamsChartApi.current) { williamsChartApi.current.remove(); williamsChartApi.current = null; }
        const chart = createChart(williamsChartRef.current, { ...chartOpts(146), width: williamsChartRef.current.clientWidth });
        williamsChartApi.current = chart;
        const highs = rawData.map(d => d.high), lows = rawData.map(d => d.low), closes = rawData.map(d => d.close), times = rawData.map(d => normalizeTime(d.date) as any);
        const w = calcWilliamsR(highs, lows, closes, 14);
        chart.addSeries(LineSeries, { color: '#22d3ee', lineWidth: 2, priceLineVisible: false, lastValueVisible: true, title: '%R' })
            .setData(times.map((t, i) => w[i] !== null ? { time: t, value: w[i]! } : null).filter(Boolean) as any);
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: -20 })));
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: -80 })));
        chart.timeScale().fitContent();
        if (mainChartApi.current) {
            mainChartApi.current.timeScale().subscribeVisibleLogicalRangeChange(r => { if (r && williamsChartApi.current) williamsChartApi.current.timeScale().setVisibleLogicalRange(r); });
            chart.timeScale().subscribeVisibleLogicalRangeChange(r => { if (r && mainChartApi.current) mainChartApi.current.timeScale().setVisibleLogicalRange(r); });
        }
        const hr = () => { if (williamsChartRef.current) chart.applyOptions({ width: williamsChartRef.current.clientWidth }); };
        window.addEventListener('resize', hr);
        return () => { window.removeEventListener('resize', hr); chart.remove(); williamsChartApi.current = null; };
    }, [rawData, showWilliams, chartOpts]);

    // MFI
    useEffect(() => {
        if (!mfiChartRef.current || rawData.length === 0 || !showMFI) return;
        if (mfiChartApi.current) { mfiChartApi.current.remove(); mfiChartApi.current = null; }
        const chart = createChart(mfiChartRef.current, { ...chartOpts(146), width: mfiChartRef.current.clientWidth });
        mfiChartApi.current = chart;
        const highs = rawData.map(d => d.high), lows = rawData.map(d => d.low), closes = rawData.map(d => d.close), volumes = rawData.map(d => d.volume ?? 0), times = rawData.map(d => normalizeTime(d.date) as any);
        const mfi = calcMFI(highs, lows, closes, volumes, 14);
        chart.addSeries(LineSeries, { color: '#a855f7', lineWidth: 2, priceLineVisible: false, lastValueVisible: true, title: 'MFI' })
            .setData(times.map((t, i) => mfi[i] !== null ? { time: t, value: mfi[i]! } : null).filter(Boolean) as any);
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 80 })));
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 20 })));
        chart.timeScale().fitContent();
        if (mainChartApi.current) {
            mainChartApi.current.timeScale().subscribeVisibleLogicalRangeChange(r => { if (r && mfiChartApi.current) mfiChartApi.current.timeScale().setVisibleLogicalRange(r); });
            chart.timeScale().subscribeVisibleLogicalRangeChange(r => { if (r && mainChartApi.current) mainChartApi.current.timeScale().setVisibleLogicalRange(r); });
        }
        const hr = () => { if (mfiChartRef.current) chart.applyOptions({ width: mfiChartRef.current.clientWidth }); };
        window.addEventListener('resize', hr);
        return () => { window.removeEventListener('resize', hr); chart.remove(); mfiChartApi.current = null; };
    }, [rawData, showMFI, chartOpts]);

    // CMF
    useEffect(() => {
        if (!cmfChartRef.current || rawData.length === 0 || !showCMF) return;
        if (cmfChartApi.current) { cmfChartApi.current.remove(); cmfChartApi.current = null; }
        const chart = createChart(cmfChartRef.current, { ...chartOpts(146), width: cmfChartRef.current.clientWidth });
        cmfChartApi.current = chart;
        const highs = rawData.map(d => d.high), lows = rawData.map(d => d.low), closes = rawData.map(d => d.close), volumes = rawData.map(d => d.volume ?? 0), times = rawData.map(d => normalizeTime(d.date) as any);
        const cmf = calcCMF(highs, lows, closes, volumes, 20);
        chart.addSeries(HistogramSeries, { priceLineVisible: false, lastValueVisible: true })
            .setData(times.map((t, i) => cmf[i] !== null ? { time: t, value: cmf[i]!, color: cmf[i]! > 0 ? 'rgba(38,166,157,0.5)' : 'rgba(239,83,80,0.5)' } : null).filter(Boolean) as any);
        chart.timeScale().fitContent();
        if (mainChartApi.current) {
            mainChartApi.current.timeScale().subscribeVisibleLogicalRangeChange(r => { if (r && cmfChartApi.current) cmfChartApi.current.timeScale().setVisibleLogicalRange(r); });
            chart.timeScale().subscribeVisibleLogicalRangeChange(r => { if (r && mainChartApi.current) mainChartApi.current.timeScale().setVisibleLogicalRange(r); });
        }
        const hr = () => { if (cmfChartRef.current) chart.applyOptions({ width: cmfChartRef.current.clientWidth }); };
        window.addEventListener('resize', hr);
        return () => { window.removeEventListener('resize', hr); chart.remove(); cmfChartApi.current = null; };
    }, [rawData, showCMF, chartOpts]);

    const updateMA = (id: string, updated: MAConfig) => setMas(prev => prev.map(m => m.id === id ? updated : m));
    const removeMA = (id: string) => setMas(prev => prev.filter(m => m.id !== id));
    const addMA = () => {
        const colors = ['#fbbf24', '#f472b6', '#38bdf8', '#a78bfa', '#34d399', '#fb923c'];
        setMas(prev => [...prev, {
            id: `ma${Date.now()}`, type: "EMA", period: 20,
            color: colors[prev.length % colors.length], visible: true
        }]);
    };

    const oscillatorPanelH = (showMACD ? 170 : 24) + (showStoch ? 170 : 24) + (showATR ? 170 : 24) + (showWilliams ? 170 : 0) + (showMFI ? 170 : 0) + (showCMF ? 170 : 0);
    const mainH = `calc(100vh - 48px - 38px - ${oscillatorPanelH}px)`;

    return (
        <div className="h-screen w-screen bg-[#0a0a0a] flex flex-col overflow-hidden" onClick={() => setIndicatorsOpen(false)}>

            {/* ─── Top Bar ──────────────────────────────────────────────── */}
            <div className="px-5 border-b border-white/5 flex items-center justify-between bg-[#0c0c0c] flex-shrink-0" style={{ height: 48 }}>
                <div className="flex items-center gap-3">
                    <button onClick={() => router.back()} className="h-8 w-8 rounded-lg bg-white/5 hover:bg-accent/20 flex items-center justify-center text-white/40 hover:text-accent transition-all" title="Back">
                        <ArrowLeft size={16} />
                    </button>
                    <div className="h-8 w-8 rounded-lg bg-accent/20 flex items-center justify-center text-accent text-xs font-bold">
                        {symbol.slice(0, 2).toUpperCase()}
                    </div>
                    <div>
                        <span className="text-sm font-bold text-white leading-none">{symbol}</span>
                        <p className="text-[9px] uppercase font-bold tracking-widest text-white/30 mt-0.5">{timeframe} Chart</p>
                    </div>

                    {/* Timeframe Selector */}
                    <div className="flex items-center gap-0.5 ml-3 pl-3 border-l border-white/10">
                        {TIMEFRAMES.map(tf => (
                            <button key={tf.value} onClick={() => setTimeframe(tf.value)}
                                className={`px-2.5 py-1 text-[10px] font-bold uppercase tracking-wider rounded transition-all ${timeframe === tf.value ? "bg-accent/20 text-accent border border-accent/30" : "text-white/40 hover:text-white/70 hover:bg-white/5 border border-transparent"}`}
                            >{tf.label}</button>
                        ))}
                    </div>

                    {quote && typeof quote.price === 'number' && (
                        <div className="flex items-center gap-3 ml-4 pl-4 border-l border-white/10">
                            <span className="text-xl font-mono font-black text-white">${quote.price.toFixed(2)}</span>
                            <div className={`flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[10px] font-black uppercase tracking-tighter ${(quote.changePercentage ?? 0) >= 0 ? "bg-green/10 text-green" : "bg-red/10 text-red"}`}>
                                {(quote.changePercentage ?? 0) >= 0 ? <TrendingUp size={12} /> : <TrendingDown size={12} />}
                                {(quote.changePercentage ?? 0).toFixed(2)}%
                            </div>
                        </div>
                    )}
                </div>

                <div className="flex items-center gap-3">
                    {loading && <span className="text-[10px] animate-pulse font-mono font-bold text-accent uppercase tracking-widest">Syncing...</span>}
                    <div className="flex items-center gap-1.5 px-2.5 py-1 bg-white/5 rounded-md border border-white/5">
                        <div className="h-1.5 w-1.5 rounded-full bg-green animate-pulse" />
                        <span className="text-[9px] font-black text-green uppercase tracking-[0.2em]">Liquid</span>
                    </div>
                </div>
            </div>

            {/* ─── Indicators Toolbar ────────────────────────────────────── */}
            <div className="px-4 border-b border-white/5 bg-[#0d0d0d] flex items-center gap-2 flex-shrink-0 flex-wrap" style={{ minHeight: 38 }} onClick={e => e.stopPropagation()}>
                {/* Indicators button */}
                <button
                    onClick={() => setIndicatorsOpen(!indicatorsOpen)}
                    className="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-white/5 border border-white/10 text-white/60 hover:text-white hover:bg-white/10 transition-all text-[11px] font-bold uppercase tracking-wide"
                >
                    <BarChart2 size={13} />
                    Indicators
                    {indicatorsOpen ? <ChevronUp size={11} /> : <ChevronDown size={11} />}
                </button>

                <button
                    onClick={() => setShowVP(!showVP)}
                    className={`flex items-center gap-1.5 px-2.5 py-1 rounded-md border transition-all text-[11px] font-bold uppercase tracking-wide ${showVP ? "bg-accent/20 border-accent/40 text-accent" : "bg-white/5 border-white/10 text-white/60 hover:text-white hover:bg-white/10"}`}
                >
                    VP
                </button>

                {/* Indicator add panel (dropdown) */}
                {indicatorsOpen && (
                    <div className="absolute top-[86px] left-4 z-50 bg-[#0f0f0f] border border-white/10 rounded-xl p-4 shadow-2xl flex flex-col gap-3 w-72">
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] font-black uppercase tracking-widest text-white/60">Moving Averages</span>
                            <button onClick={addMA} className="text-[10px] font-bold text-accent hover:text-white transition-colors px-2 py-0.5 bg-accent/10 rounded">+ Add</button>
                        </div>
                        {mas.map(ma => (
                            <div key={ma.id} className="flex items-center gap-2">
                                <div className="h-2.5 w-2.5 rounded-full flex-shrink-0" style={{ backgroundColor: ma.color, boxShadow: `0 0 6px ${ma.color}` }} />
                                <div className="flex gap-1 flex-1">
                                    {(["EMA", "SMA", "LWMA"] as MAType[]).map(t => (
                                        <button key={t} onClick={() => updateMA(ma.id, { ...ma, type: t })}
                                            className={`flex-1 py-0.5 text-[10px] font-bold rounded transition-all ${ma.type === t ? "bg-accent text-black" : "bg-white/5 text-white/40 hover:bg-white/10"}`}>{t}</button>
                                    ))}
                                </div>
                                <input type="number" value={ma.period} min={1} max={1000}
                                    onChange={e => updateMA(ma.id, { ...ma, period: Number(e.target.value) || 1 })}
                                    className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                                <input type="color" value={ma.color}
                                    onChange={e => updateMA(ma.id, { ...ma, color: e.target.value })}
                                    className="w-6 h-6 cursor-pointer bg-transparent border-0" />
                                <button onClick={() => updateMA(ma.id, { ...ma, visible: !ma.visible })}
                                    className={`w-6 h-6 rounded flex items-center justify-center text-[10px] font-bold transition-all ${ma.visible ? "bg-accent/20 text-accent" : "bg-white/5 text-white/30"}`}>
                                    {ma.visible ? "●" : "○"}
                                </button>
                                <button onClick={() => removeMA(ma.id)} className="text-white/20 hover:text-red-400 transition-colors">
                                    <X size={12} />
                                </button>
                            </div>
                        ))}

                        <div className="pt-2 border-t border-white/5 flex flex-col gap-2">
                            <span className="text-[11px] font-black uppercase tracking-widest text-white/60">Oscillators &amp; Overlays</span>
                            <div className="flex items-center justify-between">
                                <span className="text-[11px] text-white/50 font-mono">VP (POC, VAH/VAL)</span>
                                <button onClick={() => setShowVP(!showVP)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${showVP ? "bg-accent/20 text-accent" : "bg-white/5 text-white/30"}`}>{showVP ? "ON" : "OFF"}</button>
                            </div>
                            <div className="flex items-center justify-between">
                                <span className="text-[11px] text-white/50 font-mono">MACD ({macdFast},{macdSlow},{macdSignal})</span>
                                <button onClick={() => setShowMACD(!showMACD)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${showMACD ? "bg-accent/20 text-accent" : "bg-white/5 text-white/30"}`}>{showMACD ? "ON" : "OFF"}</button>
                            </div>
                            <div className="flex items-center justify-between">
                                <span className="text-[11px] text-white/50 font-mono">STOCH ({stochK},{stochD},{stochSmooth})</span>
                                <button onClick={() => setShowStoch(!showStoch)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${showStoch ? "bg-accent/20 text-accent" : "bg-white/5 text-white/30"}`}>{showStoch ? "ON" : "OFF"}</button>
                            </div>
                        </div>

                        <div className="pt-2 border-t border-white/5 flex flex-col gap-2">
                            <span className="text-[11px] font-black uppercase tracking-widest text-amber-400/80">Advanced Indicators</span>
                            {/* Fibonacci */}
                            <div className="flex items-center justify-between">
                                <span className="text-[11px] text-white/50 font-mono">Fibonacci Retracement</span>
                                <button onClick={() => setShowFib(!showFib)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${showFib ? "bg-amber-500/20 text-amber-400" : "bg-white/5 text-white/30"}`}>{showFib ? "ON" : "OFF"}</button>
                            </div>
                            {showFib && (
                                <div className="flex items-center gap-2 pl-2">
                                    <span className="text-[9px] text-white/30 uppercase font-bold">Lookback</span>
                                    <input type="number" value={fibLookback} min={10} max={1000}
                                        onChange={e => setFibLookback(Math.max(10, Number(e.target.value) || 120))}
                                        className="w-16 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                                </div>
                            )}
                            {/* Bollinger Bands */}
                            <div className="flex items-center justify-between">
                                <span className="text-[11px] text-white/50 font-mono">Bollinger Bands ({bbPeriod},{bbMult}x)</span>
                                <button onClick={() => setShowBB(!showBB)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${showBB ? "bg-blue-500/20 text-blue-400" : "bg-white/5 text-white/30"}`}>{showBB ? "ON" : "OFF"}</button>
                            </div>
                            {showBB && (
                                <div className="flex items-center gap-3 pl-2">
                                    <div className="flex items-center gap-1">
                                        <span className="text-[9px] text-white/30 uppercase font-bold">Period</span>
                                        <input type="number" value={bbPeriod} min={5} max={200}
                                            onChange={e => setBbPeriod(Math.max(5, Number(e.target.value) || 20))}
                                            className="w-12 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                                    </div>
                                    <div className="flex items-center gap-1">
                                        <span className="text-[9px] text-white/30 uppercase font-bold">Mult</span>
                                        <input type="number" value={bbMult} min={0.5} max={5} step={0.1}
                                            onChange={e => setBbMult(Math.max(0.5, Number(e.target.value) || 2))}
                                            className="w-12 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                                    </div>
                                </div>
                            )}
                            {/* ATR */}
                            <div className="flex items-center justify-between">
                                <span className="text-[11px] text-white/50 font-mono">ATR ({atrPeriod})</span>
                                <button onClick={() => setShowATR(!showATR)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${showATR ? "bg-purple-500/20 text-purple-400" : "bg-white/5 text-white/30"}`}>{showATR ? "ON" : "OFF"}</button>
                            </div>
                            {showATR && (
                                <div className="flex items-center gap-2 pl-2">
                                    <span className="text-[9px] text-white/30 uppercase font-bold">Period</span>
                                    <input type="number" value={atrPeriod} min={1} max={100}
                                        onChange={e => setAtrPeriod(Math.max(1, Number(e.target.value) || 14))}
                                        className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                                </div>
                            )}
                            {/* Parabolic SAR */}
                            <div className="flex items-center justify-between">
                                <span className="text-[11px] text-white/50 font-mono">Parabolic SAR</span>
                                <button onClick={() => setShowPSAR(!showPSAR)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${showPSAR ? "bg-pink-500/20 text-pink-400" : "bg-white/5 text-white/30"}`}>{showPSAR ? "ON" : "OFF"}</button>
                            </div>
                            {/* Supertrend */}
                            <div className="flex items-center justify-between">
                                <span className="text-[11px] text-white/50 font-mono">Supertrend (10,3)</span>
                                <button onClick={() => setShowSupertrend(!showSupertrend)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${showSupertrend ? "bg-teal-500/20 text-teal-400" : "bg-white/5 text-white/30"}`}>{showSupertrend ? "ON" : "OFF"}</button>
                            </div>
                            {/* Williams %R */}
                            <div className="flex items-center justify-between">
                                <span className="text-[11px] text-white/50 font-mono">Williams %R (14)</span>
                                <button onClick={() => setShowWilliams(!showWilliams)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${showWilliams ? "bg-cyan-500/20 text-cyan-400" : "bg-white/5 text-white/30"}`}>{showWilliams ? "ON" : "OFF"}</button>
                            </div>
                            {/* MFI */}
                            <div className="flex items-center justify-between">
                                <span className="text-[11px] text-white/50 font-mono">MFI (14)</span>
                                <button onClick={() => setShowMFI(!showMFI)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${showMFI ? "bg-violet-500/20 text-violet-400" : "bg-white/5 text-white/30"}`}>{showMFI ? "ON" : "OFF"}</button>
                            </div>
                            {/* CMF */}
                            <div className="flex items-center justify-between">
                                <span className="text-[11px] text-white/50 font-mono">CMF (20)</span>
                                <button onClick={() => setShowCMF(!showCMF)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${showCMF ? "bg-blue-500/20 text-blue-400" : "bg-white/5 text-white/30"}`}>{showCMF ? "ON" : "OFF"}</button>
                            </div>
                        </div>
                    </div>
                )}

                {/* MA chips inline */}
                {mas.filter(m => m.visible).map(ma => (
                    <div key={ma.id} className="flex items-center gap-1 px-2 py-0.5 rounded bg-white/3 border border-white/8 text-[11px] font-bold" style={{ color: ma.color }}>
                        <div className="h-1.5 w-1.5 rounded-full" style={{ backgroundColor: ma.color }} />
                        {ma.type}({ma.period})
                    </div>
                ))}
            </div>

            {/* ─── Main Chart ─────────────────────────────────────────────── */}
            <div ref={mainChartRef} className="w-full flex-1" style={{ height: mainH }} />

            {/* ─── MACD Panel ─────────────────────────────────────────────── */}
            <div className="flex-shrink-0 border-t border-white/5" style={{ height: showMACD ? 170 : 24 }}>
                <div className="flex items-center justify-between px-3 bg-[#0c0c0c] cursor-pointer select-none" style={{ height: 24 }} onClick={() => setShowMACD(!showMACD)}>
                    <div className="flex items-center gap-2">
                        <span className="text-[10px] font-black uppercase tracking-[0.15em] text-white/50">MACD</span>
                        <span className="text-[9px] font-mono text-white/30">({macdFast},{macdSlow},{macdSignal})</span>
                        {showMACD ? <ChevronUp size={10} className="text-white/30" /> : <ChevronDown size={10} className="text-white/30" />}
                    </div>
                    {showMACD && (
                        <div className="flex items-center gap-3" onClick={e => e.stopPropagation()}>
                            <ParamInput label="Fast" value={macdFast} onChange={setMacdFast} />
                            <ParamInput label="Slow" value={macdSlow} onChange={setMacdSlow} />
                            <ParamInput label="Signal" value={macdSignal} onChange={setMacdSignal} />
                        </div>
                    )}
                </div>
                {showMACD && <div ref={macdChartRef} style={{ width: '100%', height: 146 }} />}
            </div>

            {/* ─── Stochastic Panel ───────────────────────────────────────── */}
            <div className="flex-shrink-0 border-t border-white/5" style={{ height: showStoch ? 170 : 24 }}>
                <div className="flex items-center justify-between px-3 bg-[#0c0c0c] cursor-pointer select-none" style={{ height: 24 }} onClick={() => setShowStoch(!showStoch)}>
                    <div className="flex items-center gap-2">
                        <span className="text-[10px] font-black uppercase tracking-[0.15em] text-white/50">STOCHASTIC</span>
                        <span className="text-[9px] font-mono text-white/30">({stochK},{stochD},{stochSmooth})</span>
                        {showStoch ? <ChevronUp size={10} className="text-white/30" /> : <ChevronDown size={10} className="text-white/30" />}
                    </div>
                    {showStoch && (
                        <div className="flex items-center gap-3" onClick={e => e.stopPropagation()}>
                            <ParamInput label="%K" value={stochK} onChange={setStochK} />
                            <ParamInput label="%D" value={stochD} onChange={setStochD} />
                            <ParamInput label="Smooth" value={stochSmooth} onChange={setStochSmooth} />
                        </div>
                    )}
                </div>
                {showStoch && <div ref={stochChartRef} style={{ width: '100%', height: 146 }} />}
            </div>

            {/* ─── ATR Panel ─────────────────────────────────────────────── */}
            <div className="flex-shrink-0 border-t border-white/5" style={{ height: showATR ? 170 : 24 }}>
                <div className="flex items-center justify-between px-3 bg-[#0c0c0c] cursor-pointer select-none" style={{ height: 24 }} onClick={() => setShowATR(!showATR)}>
                    <div className="flex items-center gap-2">
                        <span className="text-[10px] font-black uppercase tracking-[0.15em] text-purple-400/70">ATR</span>
                        <span className="text-[9px] font-mono text-white/30">({atrPeriod})</span>
                        {showATR ? <ChevronUp size={10} className="text-white/30" /> : <ChevronDown size={10} className="text-white/30" />}
                    </div>
                    {showATR && (
                        <div className="flex items-center gap-3" onClick={e => e.stopPropagation()}>
                            <ParamInput label="Period" value={atrPeriod} onChange={setAtrPeriod} max={100} />
                        </div>
                    )}
                </div>
                {showATR && <div ref={atrChartRef} style={{ width: '100%', height: 146 }} />}
            </div>

            {/* ─── Williams %R Panel ──────────────────────────────────────── */}
            {showWilliams && (
                <div className="flex-shrink-0 border-t border-white/5" style={{ height: 170 }}>
                    <div className="flex items-center justify-between px-3 bg-[#0c0c0c] select-none" style={{ height: 24 }}>
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-cyan-400/70">Williams %R</span>
                            <span className="text-[9px] font-mono text-white/30">(14)</span>
                        </div>
                    </div>
                    <div ref={williamsChartRef} style={{ width: '100%', height: 146 }} />
                </div>
            )}

            {/* ─── MFI Panel ──────────────────────────────────────────────── */}
            {showMFI && (
                <div className="flex-shrink-0 border-t border-white/5" style={{ height: 170 }}>
                    <div className="flex items-center justify-between px-3 bg-[#0c0c0c] select-none" style={{ height: 24 }}>
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-violet-400/70">MFI</span>
                            <span className="text-[9px] font-mono text-white/30">(14)</span>
                        </div>
                    </div>
                    <div ref={mfiChartRef} style={{ width: '100%', height: 146 }} />
                </div>
            )}

            {/* ─── CMF Panel ──────────────────────────────────────────────── */}
            {showCMF && (
                <div className="flex-shrink-0 border-t border-white/5" style={{ height: 170 }}>
                    <div className="flex items-center justify-between px-3 bg-[#0c0c0c] select-none" style={{ height: 24 }}>
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-blue-400/70">CMF</span>
                            <span className="text-[9px] font-mono text-white/30">(20)</span>
                        </div>
                    </div>
                    <div ref={cmfChartRef} style={{ width: '100%', height: 146 }} />
                </div>
            )}
        </div>
    );
}
