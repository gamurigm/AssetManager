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
    const [vpData, setVpData] = useState<any>(null);

    // MACD params
    const [macdFast, setMacdFast] = useState(12);
    const [macdSlow, setMacdSlow] = useState(26);
    const [macdSignal, setMacdSignal] = useState(9);

    // Stochastic params
    const [stochK, setStochK] = useState(14);
    const [stochD, setStochD] = useState(3);
    const [stochSmooth, setStochSmooth] = useState(3);

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
        timeScale: { borderColor: '#1f1f1f', timeVisible: false },
        rightPriceScale: { borderColor: '#1f1f1f' },
        crosshair: {
            vertLine: { labelBackgroundColor: '#2962FF' },
            horzLine: { labelBackgroundColor: '#2962FF' },
        },
        ...(height ? { height } : {}),
    }), []);

    // Fetch data — historical + quote in PARALLEL
    useEffect(() => {
        if (!symbol) return;
        const fetchData = async () => {
            try {
                const [res, qRes] = await Promise.all([
                    fetch(`http://localhost:8282/api/v1/market/historical/${encodeURIComponent(symbol)}?limit=10000`),
                    fetch(`http://localhost:8282/api/v1/market/quote/${encodeURIComponent(symbol)}`)
                ]);
                const data = await res.json();
                if (data.historical) {
                    setRawData([...data.historical].sort((a: any, b: any) => a.date.localeCompare(b.date)));
                } else {
                    setRawData([]);
                }
                const q = await qRes.json();
                if (q && !q.error) setQuote({ price: q.price, changePercentage: q.changePercentage });
            } catch (err) {
                console.error("Fetch error:", err);
                setRawData([]);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [symbol]);

    // Fetch Volume Profile
    useEffect(() => {
        if (!symbol || !showVP) return;
        const fetchVP = async () => {
            try {
                const res = await fetch(`http://localhost:8282/api/v1/market/volume-profile/${encodeURIComponent(symbol)}?days=7`);
                const data = await res.json();
                if (res.ok && !data.error && !data.detail) {
                    setVpData(data);
                } else {
                    console.warn("VP Fetch Error:", data.detail || data.error || "Unknown error");
                    setVpData(null);
                }
            } catch (err) {
                console.error("Fetch VP error:", err);
                setVpData(null);
            }
        };
        fetchVP();
    }, [symbol, showVP]);

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
        candleSeries.setData(rawData.map(d => ({ time: d.date, open: d.open, high: d.high, low: d.low, close: d.close })));

        // Render Volume Profile Price Lines
        if (showVP && vpData && typeof vpData.poc === 'number' && typeof vpData.vah === 'number' && typeof vpData.val === 'number') {
            candleSeries.createPriceLine({
                price: vpData.poc,
                color: '#FFD700',
                lineWidth: 2,
                lineStyle: 0,
                axisLabelVisible: true,
                title: 'POC',
            });
            candleSeries.createPriceLine({
                price: vpData.vah,
                color: '#FF6D00',
                lineWidth: 1,
                lineStyle: 1,
                axisLabelVisible: true,
                title: 'VAH',
            });
            candleSeries.createPriceLine({
                price: vpData.val,
                color: '#FF6D00',
                lineWidth: 1,
                lineStyle: 1,
                axisLabelVisible: true,
                title: 'VAL',
            });

            // Render HVN Edges
            if (Array.isArray(vpData.hvn_edges)) {
                vpData.hvn_edges.forEach((edge: any) => {
                    if (typeof edge.high === 'number') {
                        candleSeries.createPriceLine({ price: edge.high, color: 'rgba(255, 255, 255, 0.2)', lineWidth: 1, lineStyle: 2, title: 'HVN H' });
                    }
                    if (typeof edge.low === 'number') {
                        candleSeries.createPriceLine({ price: edge.low, color: 'rgba(255, 255, 255, 0.2)', lineWidth: 1, lineStyle: 2, title: 'HVN L' });
                    }
                });
            }
        }

        // Render Moving Averages
        const closes = rawData.map(d => d.close);
        const times = rawData.map(d => d.date);
        for (const ma of mas) {
            if (!ma.visible) continue;
            const values = calcMA(ma.type, closes, ma.period);
            const series = chart.addSeries(LineSeries, {
                color: ma.color,
                lineWidth: 1,
                priceLineVisible: false,
                crosshairMarkerVisible: false,
            });
            const validData = values
                .map((v, i) => ({ time: times[i], value: v }))
                .filter(d => !isNaN(d.value));
            series.setData(validData as any);
        }

        chart.timeScale().fitContent();

        const handleResize = () => {
            if (mainChartRef.current) chart.applyOptions({ width: mainChartRef.current.clientWidth });
        };
        window.addEventListener('resize', handleResize);
        return () => { window.removeEventListener('resize', handleResize); chart.remove(); mainChartApi.current = null; };
    }, [rawData, chartOpts, mas, showVP, vpData]);

    // MACD
    useEffect(() => {
        if (!macdChartRef.current || rawData.length === 0 || !showMACD) return;
        if (macdChartApi.current) { macdChartApi.current.remove(); macdChartApi.current = null; }

        const chart = createChart(macdChartRef.current, { ...chartOpts(146), width: macdChartRef.current.clientWidth });
        macdChartApi.current = chart;

        const closes = rawData.map(d => d.close);
        const times = rawData.map(d => d.date);
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
        const times = rawData.map(d => d.date);
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

    const updateMA = (id: string, updated: MAConfig) => setMas(prev => prev.map(m => m.id === id ? updated : m));
    const removeMA = (id: string) => setMas(prev => prev.filter(m => m.id !== id));
    const addMA = () => {
        const colors = ['#fbbf24', '#f472b6', '#38bdf8', '#a78bfa', '#34d399', '#fb923c'];
        setMas(prev => [...prev, {
            id: `ma${Date.now()}`, type: "EMA", period: 20,
            color: colors[prev.length % colors.length], visible: true
        }]);
    };

    const oscillatorPanelH = (showMACD ? 170 : 24) + (showStoch ? 170 : 24);
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
                        <p className="text-[9px] uppercase font-bold tracking-widest text-white/30 mt-0.5">Daily Chart</p>
                    </div>

                    {quote && (
                        <div className="flex items-center gap-3 ml-4 pl-4 border-l border-white/10">
                            <span className="text-xl font-mono font-black text-white">${quote.price.toFixed(2)}</span>
                            <div className={`flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[10px] font-black uppercase tracking-tighter ${quote.changePercentage >= 0 ? "bg-green/10 text-green" : "bg-red/10 text-red"}`}>
                                {quote.changePercentage >= 0 ? <TrendingUp size={12} /> : <TrendingDown size={12} />}
                                {quote.changePercentage.toFixed(2)}%
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
                            <span className="text-[11px] font-black uppercase tracking-widest text-white/60">Oscillators</span>
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
        </div>
    );
}
