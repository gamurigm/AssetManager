"use client";

import React, { useRef, useState, useEffect } from "react";
import { TrendingUp, TrendingDown, ChevronDown, ChevronUp, Activity } from "lucide-react";
import { createChart, ColorType, CandlestickSeries, LineSeries, HistogramSeries, createSeriesMarkers } from "lightweight-charts";
import { usePortfolio } from "@/context/PortfolioContext";
import { useChartData } from "@/hooks/useChartData";
import { calcEMA, calcMACD, calcStochastic, FIBONACCI_LEVELS, calcBollingerBands, calcIchimoku, calcRSI, calcVWAP, calcATR, calcKeltner, calcOBV, calcADX } from "@/lib/indicators";

// ─── Props ──────────────────────────────────────────────────────────
interface SymbolChartProps {
    symbol: string;
    showFib?: boolean;
    showBollinger?: boolean;
    showIchimoku?: boolean;
    showVwap?: boolean;
    showRsi?: boolean;
    showAtr?: boolean;
    showKeltner?: boolean;
    showObv?: boolean;
    showAdx?: boolean;
}

// ─── Component ──────────────────────────────────────────────────────
export default function SymbolChart({ symbol, showFib: propShowFib, showBollinger = false, showIchimoku = false, showVwap = false, showRsi = false, showAtr = false, showKeltner = false, showObv = false, showAdx = false }: SymbolChartProps) {
    const { holdings, closePosition, openTrade } = usePortfolio();
    const { candles, quote, loading, theme, isLight } = useChartData(symbol);

    // Transaction markers
    const [transactions, setTransactions] = useState<any[]>([]);
    useEffect(() => {
        fetch("http://127.0.0.1:8282/api/v1/trading/history")
            .then(r => r.json())
            .then(data => { if (Array.isArray(data)) setTransactions(data); })
            .catch(() => { });
    }, []);

    // Chart refs
    const chartContainerRef = useRef<HTMLDivElement>(null);
    const macdRef = useRef<HTMLDivElement>(null);
    const stochRef = useRef<HTMLDivElement>(null);
    const rsiRef = useRef<HTMLDivElement>(null);
    const atrRef = useRef<HTMLDivElement>(null);
    const obvRef = useRef<HTMLDivElement>(null);
    const adxRef = useRef<HTMLDivElement>(null);

    // Dynamic Fib State
    const [fibMode, setFibMode] = useState(false);
    const [hasUserFib, setHasUserFib] = useState(false);
    const mainSeriesRef = useRef<any>(null);
    const drawStateRef = useRef<{ isDrawing: boolean, p1: number | null, p2: number | null }>({ isDrawing: false, p1: null, p2: null });
    const userFibLinesRef = useRef<any[]>([]);

    const clearUserFibLines = () => {
        if (mainSeriesRef.current && userFibLinesRef.current.length > 0) {
            userFibLinesRef.current.forEach(line => {
                try { mainSeriesRef.current.removePriceLine(line); } catch (e) { }
            });
        }
        userFibLinesRef.current = [];
        setHasUserFib(false);
        drawStateRef.current = { isDrawing: false, p1: null, p2: null };
    };

    const drawFibLines = (p1: number, p2: number) => {
        if (!mainSeriesRef.current) return;
        if (userFibLinesRef.current.length > 0) {
            userFibLinesRef.current.forEach(line => {
                try { mainSeriesRef.current.removePriceLine(line); } catch (e) { }
            });
            userFibLinesRef.current = [];
        }

        const diff = p2 - p1;
        FIBONACCI_LEVELS.forEach(level => {
            const price = p1 + (diff * level.level);
            const line = mainSeriesRef.current.createPriceLine({
                price,
                color: level.color,
                lineWidth: 1,
                lineStyle: 1,
                axisLabelVisible: true,
                title: level.text,
            });
            userFibLinesRef.current.push(line);
        });
        if (!hasUserFib) setHasUserFib(true);
    };

    const handleFibMouseDown = (e: React.MouseEvent) => {
        if (!fibMode || !mainSeriesRef.current || !chartContainerRef.current) return;
        const rect = chartContainerRef.current.getBoundingClientRect();
        const y = e.clientY - rect.top;
        const price = mainSeriesRef.current.coordinateToPrice(y as any);
        if (price !== null) {
            drawStateRef.current = { isDrawing: true, p1: price, p2: price };
            drawFibLines(price, price);
        }
    };

    const handleFibMouseMove = (e: React.MouseEvent) => {
        const state = drawStateRef.current;
        if (!state.isDrawing || state.p1 === null || !mainSeriesRef.current || !chartContainerRef.current) return;
        const rect = chartContainerRef.current.getBoundingClientRect();
        const y = e.clientY - rect.top;
        const price = mainSeriesRef.current.coordinateToPrice(y as any);
        if (price !== null) {
            state.p2 = price;
            drawFibLines(state.p1, price);
        }
    };

    const handleFibMouseUp = () => {
        if (drawStateRef.current.isDrawing) {
            drawStateRef.current.isDrawing = false;
            setFibMode(false);
        }
    };

    // Indicator params
    const [macdFast, setMacdFast] = useState(12);
    const [macdSlow, setMacdSlow] = useState(26);
    const [macdSignal, setMacdSignal] = useState(9);
    const [stochK, setStochK] = useState(14);
    const [stochD, setStochD] = useState(3);
    const [stochSmooth, setStochSmooth] = useState(3);
    const [showMacd, setShowMacd] = useState(true);
    const [showStoch, setShowStoch] = useState(true);
    const [showEmas, setShowEmas] = useState(true);
    const [internalShowFib, setInternalShowFib] = useState(false);
    const showFib = propShowFib ?? internalShowFib;
    const [ema1, setEma1] = useState(9);
    const [ema2, setEma2] = useState(21);
    const [ema3, setEma3] = useState(50);

    // ─── Chart Options Builder ──────────────────────────────────
    const chartOpts = (h: number) => ({
        layout: { background: { type: ColorType.Solid as const, color: 'transparent' }, textColor: isLight ? '#3f3f46' : '#71717a' },
        grid: { vertLines: { color: isLight ? '#f4f4f5' : '#1a1a1a' }, horzLines: { color: isLight ? '#f4f4f5' : '#1a1a1a' } },
        height: h,
        rightPriceScale: { borderVisible: false },
        timeScale: { borderVisible: false },
        crosshair: { horzLine: { visible: true, labelVisible: true }, vertLine: { visible: true, labelVisible: true } },
    });

    // ─── Main Candlestick Effect ────────────────────────────────
    useEffect(() => {
        if (!chartContainerRef.current || candles.length === 0) return;
        const el = chartContainerRef.current;
        const chart = createChart(el, { ...chartOpts(el.clientHeight), width: el.clientWidth });
        const series = chart.addSeries(CandlestickSeries, {
            upColor: '#22c55e', downColor: '#ef4444', borderVisible: false,
            wickUpColor: '#22c55e', wickDownColor: '#ef4444',
        });
        mainSeriesRef.current = series;
        series.setData(candles.map(d => ({ time: d.date, open: d.open, high: d.high, low: d.low, close: d.close })));

        // Re-draw any existing custom fib if chart recreated
        const st = drawStateRef.current;
        if (st.p1 !== null && st.p2 !== null) {
            drawFibLines(st.p1, st.p2);
        }

        // EMA overlays
        if (showEmas) {
            const closes = candles.map(d => d.close);
            const times = candles.map(d => d.date);
            const emaConfigs = [
                { period: ema1, color: '#fbbf24' },
                { period: ema2, color: '#f472b6' },
                { period: ema3, color: '#38bdf8' },
            ];
            emaConfigs.forEach(({ period, color }) => {
                const emaData = calcEMA(closes, period);
                chart.addSeries(LineSeries, { color, lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false })
                    .setData(emaData.map((v, i) => ({ time: times[i], value: v })));
            });
        }

        // Fibonacci levels
        if (showFib && candles.length > 30) {
            const range = candles.slice(-100);
            const high = Math.max(...range.map(c => c.high));
            const low = Math.min(...range.map(c => c.low));
            const diff = high - low;
            FIBONACCI_LEVELS.forEach(l => {
                const price = high - (diff * l.level);
                chart.addSeries(LineSeries, {
                    color: l.color, lineWidth: 1, lineStyle: 2,
                    priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false,
                }).setData(candles.map(c => ({ time: c.date, value: price })));
            });
        }

        // Bollinger Bands overlay
        if (showBollinger && candles.length > 20) {
            const closes = candles.map(d => d.close);
            const times = candles.map(d => d.date);
            const { upper, middle, lower } = calcBollingerBands(closes, 20, 2.0);
            // Upper band
            chart.addSeries(LineSeries, { color: '#a855f7', lineWidth: 1, lineStyle: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(times.map((t, i) => upper[i] !== null ? { time: t, value: upper[i]! } : null).filter(Boolean) as any);
            // Middle SMA
            chart.addSeries(LineSeries, { color: '#a855f780', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(times.map((t, i) => middle[i] !== null ? { time: t, value: middle[i]! } : null).filter(Boolean) as any);
            // Lower band
            chart.addSeries(LineSeries, { color: '#a855f7', lineWidth: 1, lineStyle: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(times.map((t, i) => lower[i] !== null ? { time: t, value: lower[i]! } : null).filter(Boolean) as any);
        }

        // Ichimoku Cloud overlay
        if (showIchimoku && candles.length > 52) {
            const highs = candles.map(d => d.high);
            const lows = candles.map(d => d.low);
            const closes = candles.map(d => d.close);
            const times = candles.map(d => d.date);
            const { tenkan, kijun, senkouA, senkouB } = calcIchimoku(highs, lows, closes);
            // Tenkan-sen (conversion line)
            chart.addSeries(LineSeries, { color: '#22d3ee', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(times.map((t, i) => tenkan[i] !== null ? { time: t, value: tenkan[i]! } : null).filter(Boolean) as any);
            // Kijun-sen (base line)
            chart.addSeries(LineSeries, { color: '#f97316', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(times.map((t, i) => kijun[i] !== null ? { time: t, value: kijun[i]! } : null).filter(Boolean) as any);
            // Senkou A (leading span A) — trimmed to match candle times
            chart.addSeries(LineSeries, { color: '#22c55e80', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(times.map((t, i) => senkouA[i] !== null ? { time: t, value: senkouA[i]! } : null).filter(Boolean) as any);
            // Senkou B (leading span B)
            chart.addSeries(LineSeries, { color: '#ef444480', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(times.map((t, i) => senkouB[i] !== null ? { time: t, value: senkouB[i]! } : null).filter(Boolean) as any);
        }

        // VWAP overlay
        if (showVwap && candles.length > 10) {
            const highs = candles.map(d => d.high);
            const lows = candles.map(d => d.low);
            const closes = candles.map(d => d.close);
            const volumes = candles.map(d => (d as any).volume ?? 0) as number[];
            const times = candles.map(d => d.date);
            const vwap = calcVWAP(highs, lows, closes, volumes);
            chart.addSeries(LineSeries, { color: '#eab308', lineWidth: 2, lineStyle: 0, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: true })
                .setData(times.map((t, i) => vwap[i] !== null ? { time: t, value: vwap[i]! } : null).filter(Boolean) as any);
        }

        // Keltner Channels overlay
        if (showKeltner && candles.length > 20) {
            const highs = candles.map(d => d.high);
            const lows = candles.map(d => d.low);
            const closes = candles.map(d => d.close);
            const times = candles.map(d => d.date);
            const { upper, middle, lower } = calcKeltner(highs, lows, closes, 20, 10, 2.0);
            // Upper band
            chart.addSeries(LineSeries, { color: '#3b82f6', lineWidth: 1, lineStyle: 0, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(times.map((t, i) => upper[i] !== null ? { time: t, value: upper[i]! } : null).filter(Boolean) as any);
            // Middle EMA
            chart.addSeries(LineSeries, { color: '#3b82f680', lineWidth: 1, lineStyle: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(times.map((t, i) => middle[i] !== null ? { time: t, value: middle[i]! } : null).filter(Boolean) as any);
            // Lower band
            chart.addSeries(LineSeries, { color: '#3b82f6', lineWidth: 1, lineStyle: 0, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(times.map((t, i) => lower[i] !== null ? { time: t, value: lower[i]! } : null).filter(Boolean) as any);
        }

        // Trade markers
        const myHolding = holdings.find(h => h.symbol === symbol);
        const markers: any[] = [];
        if (myHolding && myHolding.purchaseDate) {
            markers.push({ time: myHolding.purchaseDate, position: 'belowBar', color: '#22c55e', shape: 'arrowUp', text: `BOT @ ${myHolding.entryPrice.toFixed(2)}` });
        }
        transactions.filter(t => t.symbol === symbol && t.type === 'SELL').forEach(t => {
            markers.push({ time: t.date, position: 'aboveBar', color: '#ef4444', shape: 'arrowDown', text: `SOLD @ ${t.price.toFixed(2)}` });
        });
        createSeriesMarkers(series, markers.sort((a, b) => {
            const timeA = typeof a.time === 'string' ? a.time : '';
            const timeB = typeof b.time === 'string' ? b.time : '';
            return timeA.localeCompare(timeB);
        }));

        chart.timeScale().fitContent();
        const handleResize = () => chart.applyOptions({ width: el.clientWidth });
        window.addEventListener('resize', handleResize);
        return () => { window.removeEventListener('resize', handleResize); chart.remove(); };
    }, [candles, theme, showEmas, showFib, showBollinger, showIchimoku, showVwap, showKeltner, ema1, ema2, ema3, holdings, transactions]);

    // ─── MACD Effect ────────────────────────────────────────────
    useEffect(() => {
        if (!macdRef.current || candles.length === 0 || !showMacd) return;
        const el = macdRef.current;
        const chart = createChart(el, { ...chartOpts(130), width: el.clientWidth });
        const closes = candles.map(d => d.close);
        const times = candles.map(d => d.date);
        const { macdLine, signalLine, histogram } = calcMACD(closes, macdFast, macdSlow, macdSignal);
        chart.addSeries(HistogramSeries, { color: '#3b82f6', priceLineVisible: false })
            .setData(times.map((t, i) => ({ time: t, value: histogram[i], color: histogram[i] >= 0 ? '#22c55e80' : '#ef444480' })));
        chart.addSeries(LineSeries, { color: '#3b82f6', lineWidth: 1, priceLineVisible: false })
            .setData(times.map((t, i) => ({ time: t, value: macdLine[i] })));
        chart.addSeries(LineSeries, { color: '#f97316', lineWidth: 1, priceLineVisible: false })
            .setData(times.map((t, i) => ({ time: t, value: signalLine[i] })));
        chart.timeScale().fitContent();
        const handleResize = () => chart.applyOptions({ width: el.clientWidth });
        window.addEventListener('resize', handleResize);
        return () => { window.removeEventListener('resize', handleResize); chart.remove(); };
    }, [candles, theme, macdFast, macdSlow, macdSignal, showMacd]);

    // ─── Stochastic Effect ──────────────────────────────────────
    useEffect(() => {
        if (!stochRef.current || candles.length === 0 || !showStoch) return;
        const el = stochRef.current;
        const chart = createChart(el, { ...chartOpts(130), width: el.clientWidth });
        const closes = candles.map(d => d.close);
        const highs = candles.map(d => d.high);
        const lows = candles.map(d => d.low);
        const times = candles.map(d => d.date);
        const { kLine, dLine } = calcStochastic(highs, lows, closes, stochK, stochD, stochSmooth);
        chart.addSeries(LineSeries, { color: '#8b5cf6', lineWidth: 1, priceLineVisible: false })
            .setData(times.map((t, i) => ({ time: t, value: isNaN(kLine[i]) ? undefined : kLine[i] })).filter(d => d.value !== undefined) as any);
        chart.addSeries(LineSeries, { color: '#ec4899', lineWidth: 1, priceLineVisible: false })
            .setData(times.map((t, i) => ({ time: t, value: isNaN(dLine[i]) ? undefined : dLine[i] })).filter(d => d.value !== undefined) as any);
        chart.timeScale().fitContent();
        const handleResize = () => chart.applyOptions({ width: el.clientWidth });
        window.addEventListener('resize', handleResize);
        return () => { window.removeEventListener('resize', handleResize); chart.remove(); };
    }, [candles, theme, stochK, stochD, stochSmooth, showStoch]);

    // ─── RSI Effect ─────────────────────────────────────────────
    useEffect(() => {
        if (!rsiRef.current || candles.length === 0 || !showRsi) return;
        const el = rsiRef.current;
        const chart = createChart(el, { ...chartOpts(120), width: el.clientWidth });
        const closes = candles.map(d => d.close);
        const times = candles.map(d => d.date);
        const rsi = calcRSI(closes, 14);
        // RSI line
        chart.addSeries(LineSeries, { color: '#f59e0b', lineWidth: 2, priceLineVisible: false })
            .setData(times.map((t, i) => rsi[i] !== null ? { time: t, value: rsi[i]! } : null).filter(Boolean) as any);
        // Overbought line (70)
        chart.addSeries(LineSeries, { color: '#ef444460', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 70 })));
        // Oversold line (30)
        chart.addSeries(LineSeries, { color: '#22c55e60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 30 })));
        // Midline (50)
        chart.addSeries(LineSeries, { color: '#71717a30', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 50 })));
        chart.timeScale().fitContent();
        const handleResize = () => chart.applyOptions({ width: el.clientWidth });
        window.addEventListener('resize', handleResize);
        return () => { window.removeEventListener('resize', handleResize); chart.remove(); };
    }, [candles, theme, showRsi]);

    // ─── ATR Effect ──────────────────────────────────────────────
    useEffect(() => {
        if (!atrRef.current || candles.length === 0 || !showAtr) return;
        const el = atrRef.current;
        const chart = createChart(el, { ...chartOpts(100), width: el.clientWidth });
        const highs = candles.map(d => d.high);
        const lows = candles.map(d => d.low);
        const closes = candles.map(d => d.close);
        const times = candles.map(d => d.date);
        const atr = calcATR(highs, lows, closes, 14);
        chart.addSeries(LineSeries, { color: '#06b6d4', lineWidth: 2, priceLineVisible: false })
            .setData(times.map((t, i) => atr[i] !== null ? { time: t, value: atr[i]! } : null).filter(Boolean) as any);
        chart.timeScale().fitContent();
        const handleResize = () => chart.applyOptions({ width: el.clientWidth });
        window.addEventListener('resize', handleResize);
        return () => { window.removeEventListener('resize', handleResize); chart.remove(); };
    }, [candles, theme, showAtr]);

    // ─── OBV Effect ──────────────────────────────────────────────
    useEffect(() => {
        if (!obvRef.current || candles.length === 0 || !showObv) return;
        const el = obvRef.current;
        const chart = createChart(el, { ...chartOpts(100), width: el.clientWidth });
        const closes = candles.map(d => d.close);
        const volumes = candles.map(d => (d as any).volume ?? 0) as number[];
        const times = candles.map(d => d.date);
        const obv = calcOBV(closes, volumes);
        chart.addSeries(LineSeries, { color: '#8b5cf6', lineWidth: 2, priceLineVisible: false })
            .setData(times.map((t, i) => obv[i] !== null ? { time: t, value: obv[i]! } : null).filter(Boolean) as any);
        chart.timeScale().fitContent();
        const handleResize = () => chart.applyOptions({ width: el.clientWidth });
        window.addEventListener('resize', handleResize);
        return () => { window.removeEventListener('resize', handleResize); chart.remove(); };
    }, [candles, theme, showObv]);

    // ─── ADX Effect ──────────────────────────────────────────────
    useEffect(() => {
        if (!adxRef.current || candles.length === 0 || !showAdx) return;
        const el = adxRef.current;
        const chart = createChart(el, { ...chartOpts(120), width: el.clientWidth });
        const highs = candles.map(d => d.high);
        const lows = candles.map(d => d.low);
        const closes = candles.map(d => d.close);
        const times = candles.map(d => d.date);
        const { adx, pdi, ndi } = calcADX(highs, lows, closes, 14);
        chart.addSeries(LineSeries, { color: '#ec4899', lineWidth: 2, priceLineVisible: false })
            .setData(times.map((t, i) => adx[i] !== null ? { time: t, value: adx[i]! } : null).filter(Boolean) as any);
        chart.addSeries(LineSeries, { color: '#22c55e', lineWidth: 1, priceLineVisible: false })
            .setData(times.map((t, i) => pdi[i] !== null ? { time: t, value: pdi[i]! } : null).filter(Boolean) as any);
        chart.addSeries(LineSeries, { color: '#ef4444', lineWidth: 1, priceLineVisible: false })
            .setData(times.map((t, i) => ndi[i] !== null ? { time: t, value: ndi[i]! } : null).filter(Boolean) as any);
        // Trend threshold line (25)
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 25 })));
        chart.timeScale().fitContent();
        const handleResize = () => chart.applyOptions({ width: el.clientWidth });
        window.addEventListener('resize', handleResize);
        return () => { window.removeEventListener('resize', handleResize); chart.remove(); };
    }, [candles, theme, showAdx]);

    // ─── Input class helper ─────────────────────────────────────
    const inputClass = `w-10 px-1 py-0.5 border rounded text-[10px] font-mono text-center focus:outline-none ${isLight ? "bg-zinc-100 border-zinc-200 text-zinc-900" : "bg-white/5 border-white/10 text-white"}`;

    // ─── Render ─────────────────────────────────────────────────
    return (
        <div className="flex flex-col h-full">
            {/* Header */}
            <div className="px-6 py-4 border-b border-border flex items-center justify-between bg-card-hover/20">
                <div className="flex items-center gap-4">
                    <div className="h-8 w-8 rounded-lg bg-accent/20 flex items-center justify-center text-accent text-xs font-bold">
                        {symbol.slice(0, 2)}
                    </div>
                    <div className="flex flex-col">
                        <h2 className="text-xl font-bold leading-none">{symbol}</h2>
                        <span className="text-muted text-[10px] uppercase font-bold tracking-widest mt-1">Institutional Performance</span>
                    </div>
                    {quote && (
                        <div className="flex items-center gap-3 ml-4 pl-4 border-l border-border">
                            <span className="text-xl font-mono font-black">${quote.price.toFixed(2)}</span>
                            <div className={`flex items-center gap-1 text-xs font-black px-2 py-0.5 rounded-md ${quote.changePercentage >= 0 ? "bg-green/20 text-green" : "bg-red/20 text-red"}`}>
                                {quote.changePercentage >= 0 ? <TrendingUp size={12} /> : <TrendingDown size={12} />}
                                {quote.changePercentage.toFixed(2)}%
                            </div>
                        </div>
                    )}
                </div>
                <div className="flex items-center gap-3">
                    {!holdings.find(h => h.symbol === symbol) ? (
                        <button
                            onClick={async () => { if (quote) await openTrade(symbol, symbol, 10, quote.price, 1.0, "Technology", "stock"); }}
                            className="px-4 py-2 bg-green/10 hover:bg-green/20 border border-green/20 hover:border-green/40 text-green text-xs font-black uppercase tracking-widest rounded-xl transition-all shadow-sm hover:shadow-green/10"
                        >
                            Open Position (10 Units)
                        </button>
                    ) : (
                        <button
                            onClick={() => { if (confirm(`Liquidate total ${symbol} position?`)) closePosition(symbol); }}
                            className="px-4 py-2 bg-red/10 hover:bg-red/20 border border-red/20 hover:border-red/40 text-red text-xs font-black uppercase tracking-widest rounded-xl transition-all shadow-sm hover:shadow-red/10"
                        >
                            Liquidate Position
                        </button>
                    )}
                    {loading && <span className="text-xs animate-pulse text-accent font-mono uppercase tracking-tighter">Syncing...</span>}
                    <button
                        onClick={() => setInternalShowFib(!showFib)}
                        className={`p-2 rounded-lg border transition-all ${showFib ? 'bg-cyan-400/20 border-cyan-400/40 text-cyan-400' : 'bg-white/5 border-white/10 text-muted'}`}
                        title="Toggle Fibonacci"
                    >
                        <Activity size={16} />
                    </button>
                </div>
            </div>

            {/* Main Candlestick */}
            <div className="relative w-full" style={{ height: 'calc(100% - 320px)', minHeight: 400 }}>
                {fibMode && (
                    <div
                        className="absolute inset-0 z-40 cursor-crosshair bg-white/5"
                        onMouseDown={handleFibMouseDown}
                        onMouseMove={handleFibMouseMove}
                        onMouseUp={handleFibMouseUp}
                        onMouseLeave={handleFibMouseUp}
                    />
                )}
                <div ref={chartContainerRef} className="absolute inset-0 z-10" />
                {/* Overlay EMA Controls */}
                <div className="absolute top-2 left-2 z-20 flex flex-col gap-1">
                    <div
                        className={`flex items-center gap-2 px-2 py-1 bg-card-hover/90 backdrop-blur-sm rounded border cursor-pointer hover:bg-card-hover transition-colors select-none ${fibMode ? 'border-amber-400/50 shadow-[0_0_10px_rgba(251,191,36,0.2)]' : 'border-border/50'}`}
                        onClick={() => {
                            if (!fibMode) clearUserFibLines();
                            setFibMode(!fibMode);
                        }}
                    >
                        <span className={`text-[10px] font-black uppercase tracking-[0.15em] ${fibMode ? 'text-amber-400' : 'text-muted'}`}>DRAW FIB</span>
                    </div>

                    <div
                        className="flex items-center gap-2 px-2 py-1 bg-card-hover/90 backdrop-blur-sm rounded border border-border/50 cursor-pointer hover:bg-card-hover transition-colors select-none"
                        onClick={() => setShowEmas(!showEmas)}
                    >
                        <span className="text-[10px] font-black uppercase tracking-[0.15em] text-muted">MOVING AVERAGES</span>
                        {showEmas ? <ChevronUp size={10} className="text-muted" /> : <ChevronDown size={10} className="text-muted" />}
                    </div>
                    {showEmas && (
                        <div className="flex flex-col gap-1.5 p-2 bg-card-hover/90 backdrop-blur-sm rounded border border-border/50" onClick={e => e.stopPropagation()}>
                            {[
                                { color: '#fbbf24', label: 'EMA 1', value: ema1, set: setEma1, fallback: 9, max: 200 },
                                { color: '#f472b6', label: 'EMA 2', value: ema2, set: setEma2, fallback: 21, max: 200 },
                                { color: '#38bdf8', label: 'EMA 3', value: ema3, set: setEma3, fallback: 50, max: 500 },
                            ].map(({ color, label, value, set, fallback, max }) => (
                                <div key={label} className="flex items-center gap-2">
                                    <div className="h-2 w-2 rounded-full" style={{ backgroundColor: color, boxShadow: `0 0 8px ${color}` }} />
                                    <span className="text-[9px] font-mono text-muted font-bold w-12">{label}</span>
                                    <input type="number" value={value} onChange={e => set(+e.target.value || fallback)} min={1} max={max} className="w-12 px-1 py-0.5 bg-background border border-border/50 rounded text-[10px] text-foreground font-mono text-center focus:outline-none" />
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            </div>

            {/* MACD Panel */}
            <div className="border-t border-border/30 flex-shrink-0">
                <div className="flex items-center justify-between px-3 py-1.5 bg-card-hover/30 cursor-pointer select-none" onClick={() => setShowMacd(!showMacd)}>
                    <div className="flex items-center gap-2">
                        <span className="text-[10px] font-black uppercase tracking-[0.15em] text-muted">MACD ({macdFast},{macdSlow},{macdSignal})</span>
                        {showMacd ? <ChevronUp size={12} className="text-muted" /> : <ChevronDown size={12} className="text-muted" />}
                    </div>
                    {showMacd && (
                        <div className="flex items-center gap-2" onClick={e => e.stopPropagation()}>
                            <input type="number" value={macdFast} min={2} max={50} onChange={e => setMacdFast(+e.target.value || 12)} className={inputClass} />
                            <input type="number" value={macdSlow} min={2} max={100} onChange={e => setMacdSlow(+e.target.value || 26)} className={inputClass} />
                            <input type="number" value={macdSignal} min={2} max={50} onChange={e => setMacdSignal(+e.target.value || 9)} className={inputClass} />
                        </div>
                    )}
                </div>
                {showMacd && <div ref={macdRef} className="w-full" style={{ height: 130 }} />}
            </div>

            {/* Stochastic Panel */}
            <div className="border-t border-border/30 flex-shrink-0">
                <div className="flex items-center justify-between px-3 py-1.5 bg-card-hover/30 cursor-pointer select-none" onClick={() => setShowStoch(!showStoch)}>
                    <div className="flex items-center gap-2">
                        <span className="text-[10px] font-black uppercase tracking-[0.15em] text-muted">STOCH ({stochK},{stochD},{stochSmooth})</span>
                        {showStoch ? <ChevronUp size={12} className="text-muted" /> : <ChevronDown size={12} className="text-muted" />}
                    </div>
                    {showStoch && (
                        <div className="flex items-center gap-2" onClick={e => e.stopPropagation()}>
                            <input type="number" value={stochK} min={2} max={50} onChange={e => setStochK(+e.target.value || 14)} className={inputClass} />
                            <input type="number" value={stochD} min={2} max={50} onChange={e => setStochD(+e.target.value || 3)} className={inputClass} />
                            <input type="number" value={stochSmooth} min={1} max={20} onChange={e => setStochSmooth(+e.target.value || 3)} className={inputClass} />
                        </div>
                    )}
                </div>
                {showStoch && <div ref={stochRef} className="w-full" style={{ height: 130 }} />}
            </div>

            {/* RSI Panel */}
            {showRsi && (
                <div className="border-t border-border/30 flex-shrink-0">
                    <div className="flex items-center justify-between px-3 py-1.5 bg-card-hover/30">
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-amber-400/80">RSI (14)</span>
                            <span className="text-[8px] text-muted font-bold">70 / 30</span>
                        </div>
                    </div>
                    <div ref={rsiRef} className="w-full" style={{ height: 120 }} />
                </div>
            )}

            {/* ATR Panel */}
            {showAtr && (
                <div className="border-t border-border/30 flex-shrink-0">
                    <div className="flex items-center justify-between px-3 py-1.5 bg-card-hover/30">
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-cyan-400/80">ATR (14)</span>
                            <span className="text-[8px] text-muted font-bold">Volatility</span>
                        </div>
                    </div>
                    <div ref={atrRef} className="w-full" style={{ height: 100 }} />
                </div>
            )}

            {/* OBV Panel */}
            {showObv && (
                <div className="border-t border-border/30 flex-shrink-0">
                    <div className="flex items-center justify-between px-3 py-1.5 bg-card-hover/30">
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-violet-400/80">OBV</span>
                            <span className="text-[8px] text-muted font-bold">Volume Flow</span>
                        </div>
                    </div>
                    <div ref={obvRef} className="w-full" style={{ height: 100 }} />
                </div>
            )}

            {/* ADX Panel */}
            {showAdx && (
                <div className="border-t border-border/30 flex-shrink-0">
                    <div className="flex items-center justify-between px-3 py-1.5 bg-card-hover/30">
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-pink-400/80">ADX (14)</span>
                            <span className="text-[8px] text-muted font-bold">Trend Strength</span>
                        </div>
                    </div>
                    <div ref={adxRef} className="w-full" style={{ height: 120 }} />
                </div>
            )}
        </div>
    );
}
