"use client";

import React, { useRef, useState, useEffect, useCallback } from "react";
import { TrendingUp, TrendingDown, ChevronDown, ChevronUp, Activity, ZoomIn, ZoomOut } from "lucide-react";
import { createChart, ColorType, CandlestickSeries, LineSeries, HistogramSeries, createSeriesMarkers, IChartApi } from "lightweight-charts";
import { usePortfolio } from "@/context/PortfolioContext";
import { useChartData } from "@/hooks/useChartData";
import { calcEMA, calcMACD, calcStochastic, FIBONACCI_LEVELS, calcBollingerBands, calcIchimoku, calcRSI, calcVWAP, calcATR, calcKeltner, calcCCI, calcADX, calcParabolicSAR, calcSupertrend, calcWilliamsR, calcMFI, calcCMF } from "@/lib/indicators";

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
    showCci?: boolean;
    showAdx?: boolean;
    showPsar?: boolean;
    showSupertrend?: boolean;
    showWilliams?: boolean;
    showMfi?: boolean;
    showCmf?: boolean;
}

// Helper: sync a sub-chart's time scale with the main chart
function syncToMain(mainChart: IChartApi, subChart: IChartApi) {
    const mainTS = mainChart.timeScale();
    const subTS = subChart.timeScale();
    const r = mainTS.getVisibleLogicalRange();
    if (r) subTS.setVisibleLogicalRange(r);

    const onMain = (range: any) => { if (range) subTS.setVisibleLogicalRange(range); };
    const onSub = (range: any) => { if (range && mainChart) mainTS.setVisibleLogicalRange(range); };
    mainTS.subscribeVisibleLogicalRangeChange(onMain);
    subTS.subscribeVisibleLogicalRangeChange(onSub);
    return () => {
        mainTS.unsubscribeVisibleLogicalRangeChange(onMain);
        subTS.unsubscribeVisibleLogicalRangeChange(onSub);
    };
}

// Global variable to hold subcharts across renders so they can be grouped for crosshair sync in the portfolio chart
let symbolSubChartsRegistry: IChartApi[] = [];

// Helper: safe line data (skip NaN)
function safeLine(times: string[], values: (number | null)[]): any[] {
    return times.map((t, i) => {
        const v = values[i];
        return (v === null || v === undefined || isNaN(v)) ? { time: t } : { time: t, value: v };
    });
}

// ─── Component ──────────────────────────────────────────────────────
export default function SymbolChart({ symbol, showFib: propShowFib, showBollinger = false, showIchimoku = false, showVwap = false, showRsi = false, showAtr = false, showKeltner = false, showCci = false, showAdx = false, showPsar = false, showSupertrend = false, showWilliams = false, showMfi = false, showCmf = false }: SymbolChartProps) {
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
    const mainChartApi = useRef<IChartApi | null>(null);
    const macdRef = useRef<HTMLDivElement>(null);
    const stochRef = useRef<HTMLDivElement>(null);
    const rsiRef = useRef<HTMLDivElement>(null);
    const atrRef = useRef<HTMLDivElement>(null);
    const cciRef = useRef<HTMLDivElement>(null);
    const adxRef = useRef<HTMLDivElement>(null);
    const williamsRef = useRef<HTMLDivElement>(null);
    const mfiRef = useRef<HTMLDivElement>(null);
    const cmfRef = useRef<HTMLDivElement>(null);

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
                price, color: level.color, lineWidth: 1, lineStyle: 1, axisLabelVisible: true, title: level.text,
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

    // Zoom helpers
    const zoomIn = useCallback(() => {
        if (!mainChartApi.current) return;
        const ts = mainChartApi.current.timeScale();
        const range = ts.getVisibleLogicalRange();
        if (!range) return;
        const center = (range.from + range.to) / 2;
        const halfSpan = (range.to - range.from) / 2 * 0.7;
        ts.setVisibleLogicalRange({ from: center - halfSpan, to: center + halfSpan });
    }, []);

    const zoomOut = useCallback(() => {
        if (!mainChartApi.current) return;
        const ts = mainChartApi.current.timeScale();
        const range = ts.getVisibleLogicalRange();
        if (!range) return;
        const center = (range.from + range.to) / 2;
        const halfSpan = (range.to - range.from) / 2 * 1.4;
        ts.setVisibleLogicalRange({ from: center - halfSpan, to: center + halfSpan });
    }, []);

    // ─── Chart Options Builder ──────────────────────────────────
    const chartOpts = useCallback((h: number) => ({
        layout: { background: { type: ColorType.Solid as const, color: 'transparent' }, textColor: isLight ? '#3f3f46' : '#71717a' },
        grid: { vertLines: { visible: false }, horzLines: { visible: false } },
        height: h,
        rightPriceScale: { borderVisible: false },
        timeScale: { borderVisible: false },
        crosshair: { horzLine: { visible: true, labelVisible: true }, vertLine: { visible: true, labelVisible: true } },
    }), [isLight]);

    // ─── Main Candlestick Effect ────────────────────────────────
    useEffect(() => {
        if (!chartContainerRef.current || candles.length === 0) return;
        const el = chartContainerRef.current;

        let savedRange: any = null;
        if (mainChartApi.current) {
            savedRange = mainChartApi.current.timeScale().getVisibleLogicalRange();
            setTimeout(() => { try { mainChartApi.current?.remove(); } catch (e) { } }, 10);
            mainChartApi.current = null;
        }

        const chart = createChart(el, { ...chartOpts(el.clientHeight), width: el.clientWidth });
        mainChartApi.current = chart;
        const series = chart.addSeries(CandlestickSeries, {
            upColor: '#22c55e', downColor: '#ef4444', borderVisible: false,
            wickUpColor: '#22c55e', wickDownColor: '#ef4444',
        });
        mainSeriesRef.current = series;
        series.setData(candles.map(d => ({ time: d.date, open: d.open, high: d.high, low: d.low, close: d.close })));

        // Re-draw any existing custom fib if chart recreated
        const st = drawStateRef.current;
        if (st.p1 !== null && st.p2 !== null) drawFibLines(st.p1, st.p2);

        const closes = candles.map(d => d.close);
        const times = candles.map(d => d.date);
        const highs = candles.map(d => d.high);
        const lows = candles.map(d => d.low);

        // EMA overlays
        if (showEmas) {
            [{ period: ema1, color: '#fbbf24' }, { period: ema2, color: '#f472b6' }, { period: ema3, color: '#38bdf8' }].forEach(({ period, color }) => {
                const emaData = calcEMA(closes, period);
                chart.addSeries(LineSeries, { color, lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false })
                    .setData(safeLine(times, emaData) as any);
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
                chart.addSeries(LineSeries, { color: l.color, lineWidth: 1, lineStyle: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                    .setData(candles.map(c => ({ time: c.date, value: price })));
            });
        }

        // Bollinger Bands
        if (showBollinger && candles.length > 20) {
            const { upper, middle, lower } = calcBollingerBands(closes, 20, 2.0);
            chart.addSeries(LineSeries, { color: '#a855f7', lineWidth: 1, lineStyle: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(safeLine(times, upper) as any);
            chart.addSeries(LineSeries, { color: '#a855f780', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(safeLine(times, middle) as any);
            chart.addSeries(LineSeries, { color: '#a855f7', lineWidth: 1, lineStyle: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(safeLine(times, lower) as any);
        }

        // Ichimoku Cloud
        if (showIchimoku && candles.length > 52) {
            const { tenkan, kijun, senkouA, senkouB } = calcIchimoku(highs, lows, closes);
            chart.addSeries(LineSeries, { color: '#22d3ee', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(safeLine(times, tenkan) as any);
            chart.addSeries(LineSeries, { color: '#f97316', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(safeLine(times, kijun) as any);
            chart.addSeries(LineSeries, { color: '#22c55e80', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(safeLine(times, senkouA) as any);
            chart.addSeries(LineSeries, { color: '#ef444480', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(safeLine(times, senkouB) as any);
        }

        // VWAP
        if (showVwap && candles.length > 10) {
            const volumes = candles.map(d => (d as any).volume ?? 0) as number[];
            const vwap = calcVWAP(highs, lows, closes, volumes);
            chart.addSeries(LineSeries, { color: '#eab308', lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: true })
                .setData(safeLine(times, vwap) as any);
        }

        // Keltner Channels
        if (showKeltner && candles.length > 20) {
            const { upper, middle, lower } = calcKeltner(highs, lows, closes, 20, 10, 2.0);
            chart.addSeries(LineSeries, { color: '#3b82f6', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(safeLine(times, upper) as any);
            chart.addSeries(LineSeries, { color: '#3b82f680', lineWidth: 1, lineStyle: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(safeLine(times, middle) as any);
            chart.addSeries(LineSeries, { color: '#3b82f6', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(safeLine(times, lower) as any);
        }

        // Parabolic SAR
        if (showPsar && candles.length > 5) {
            const sar = calcParabolicSAR(highs, lows);
            chart.addSeries(LineSeries, { color: '#ec4899', lineWidth: 2, lineStyle: 3, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: true })
                .setData(safeLine(times, sar) as any);
        }

        // Supertrend
        if (showSupertrend && candles.length > 20) {
            const { supertrend, dir } = calcSupertrend(highs, lows, closes);
            const upData = times.map((t, i) => (dir[i] === 1 && supertrend[i] !== null && !isNaN(supertrend[i]!)) ? { time: t, value: supertrend[i]! } : { time: t });
            const downData = times.map((t, i) => (dir[i] === -1 && supertrend[i] !== null && !isNaN(supertrend[i]!)) ? { time: t, value: supertrend[i]! } : { time: t });
            chart.addSeries(LineSeries, { color: '#2dd4bf', lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(upData as any);
            chart.addSeries(LineSeries, { color: '#ef4444', lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(downData as any);
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

        if (savedRange) {
            chart.timeScale().setVisibleLogicalRange(savedRange);
        } else {
            chart.timeScale().fitContent();
        }

        // ResizeObserver for smooth resize
        let isMounted = true;
        const ro = new ResizeObserver(() => {
            if (!isMounted || !el) return;
            try { chart.applyOptions({ width: el.clientWidth, height: el.clientHeight || 400 }); } catch (e) { }
        });
        ro.observe(el);
        return () => {
            isMounted = false;
            ro.disconnect();
            try { chart.remove(); } catch (e) { }
            mainChartApi.current = null;
        };
    }, [candles, chartOpts, showEmas, showFib, showBollinger, showIchimoku, showVwap, showKeltner, showPsar, showSupertrend, ema1, ema2, ema3, holdings, transactions]);

    // ─── Sub-chart builder helper ─────────────────────────────────
    const buildSubChart = (ref: React.RefObject<HTMLDivElement | null>, height: number, builder: (chart: IChartApi, times: string[]) => void, deps: any[]) => {
        useEffect(() => {
            if (!ref.current || candles.length === 0) return;
            const el = ref.current;
            const chart = createChart(el, { ...chartOpts(height), width: el.clientWidth });
            const times = candles.map(d => d.date);
            builder(chart, times);
            chart.timeScale().fitContent();

            // Register for crosshair sync
            symbolSubChartsRegistry.push(chart);

            let isMounted = true;
            let unsync: (() => void) | undefined;
            // Retry syncing if main chart isn't ready immediately
            let attempts = 0;
            const trySync = () => {
                if (!isMounted) return;
                if (mainChartApi.current) {
                    unsync = syncToMain(mainChartApi.current, chart);
                } else if (attempts < 10) {
                    attempts++;
                    setTimeout(trySync, 50);
                }
            };
            trySync();

            // Crosshair sync logic
            const syncId = Math.random().toString();
            (chart as any)._syncId = syncId;
            let isSyncing = false;

            const onCrosshair = (param: any) => {
                if (isSyncing || !param.time || param.point?.x < 0) return;
                isSyncing = true;
                const siblings = mainChartApi.current ? [mainChartApi.current, ...symbolSubChartsRegistry] : symbolSubChartsRegistry;
                siblings.forEach(sibling => {
                    if ((sibling as any)._syncId !== syncId) {
                        try { sibling.setCrosshairPosition(0, param.time, sibling.timeScale() as any); } catch (e) { sibling.clearCrosshairPosition(); }
                    }
                });
                isSyncing = false;
            };
            chart.subscribeCrosshairMove(onCrosshair);

            const ro = new ResizeObserver(() => {
                if (!isMounted || !el) return;
                try { chart.applyOptions({ width: el.clientWidth }); } catch (e) { }
            });
            ro.observe(el);

            return () => {
                isMounted = false;
                symbolSubChartsRegistry = symbolSubChartsRegistry.filter(c => c !== chart);
                chart.unsubscribeCrosshairMove(onCrosshair);
                unsync?.();
                ro.disconnect();
                try { chart.remove(); } catch (e) { }
            };
        }, [candles, chartOpts, ...deps]);
    };

    // ─── MACD Effect ────────────────────────────────────────────
    buildSubChart(macdRef, 130, (chart, times) => {
        if (!showMacd) return;
        const closes = candles.map(d => d.close);
        const { macdLine, signalLine, histogram } = calcMACD(closes, macdFast, macdSlow, macdSignal);
        chart.addSeries(HistogramSeries, { priceLineVisible: false, lastValueVisible: false })
            .setData(times.map((t, i) => (histogram[i] === null || isNaN(histogram[i])) ? { time: t } : { time: t, value: histogram[i], color: histogram[i] >= 0 ? '#22c55e80' : '#ef444480' }) as any);
        chart.addSeries(LineSeries, { color: '#3b82f6', lineWidth: 1, priceLineVisible: false })
            .setData(safeLine(times, macdLine) as any);
        chart.addSeries(LineSeries, { color: '#f97316', lineWidth: 1, priceLineVisible: false })
            .setData(safeLine(times, signalLine) as any);
    }, [showMacd, macdFast, macdSlow, macdSignal]);

    // ─── Stochastic Effect ──────────────────────────────────────
    buildSubChart(stochRef, 130, (chart, times) => {
        if (!showStoch) return;
        const closes = candles.map(d => d.close);
        const highs = candles.map(d => d.high);
        const lows = candles.map(d => d.low);
        const { kLine, dLine } = calcStochastic(highs, lows, closes, stochK, stochD, stochSmooth);
        chart.addSeries(LineSeries, { color: '#8b5cf6', lineWidth: 1, priceLineVisible: false })
            .setData(safeLine(times, kLine) as any);
        chart.addSeries(LineSeries, { color: '#ec4899', lineWidth: 1, priceLineVisible: false })
            .setData(safeLine(times, dLine) as any);
    }, [showStoch, stochK, stochD, stochSmooth]);

    // ─── RSI Effect ─────────────────────────────────────────────
    buildSubChart(rsiRef, 120, (chart, times) => {
        if (!showRsi) return;
        const closes = candles.map(d => d.close);
        const rsi = calcRSI(closes, 14);
        chart.addSeries(LineSeries, { color: '#f59e0b', lineWidth: 2, priceLineVisible: false })
            .setData(safeLine(times, rsi) as any);
        chart.addSeries(LineSeries, { color: '#ef444460', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 70 })));
        chart.addSeries(LineSeries, { color: '#22c55e60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 30 })));
        chart.addSeries(LineSeries, { color: '#71717a30', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 50 })));
    }, [showRsi]);

    // ─── ATR Effect ──────────────────────────────────────────────
    buildSubChart(atrRef, 100, (chart, times) => {
        if (!showAtr) return;
        const highs = candles.map(d => d.high); const lows = candles.map(d => d.low); const closes = candles.map(d => d.close);
        const atr = calcATR(highs, lows, closes, 14);
        chart.addSeries(LineSeries, { color: '#06b6d4', lineWidth: 2, priceLineVisible: false })
            .setData(safeLine(times, atr) as any);
    }, [showAtr]);

    // ─── CCI Effect ──────────────────────────────────────────────
    buildSubChart(cciRef, 100, (chart, times) => {
        if (!showCci) return;
        const highs = candles.map(d => d.high); const lows = candles.map(d => d.low); const closes = candles.map(d => d.close);
        const cci = calcCCI(highs, lows, closes, 20);
        chart.addSeries(LineSeries, { color: '#8b5cf6', lineWidth: 2, priceLineVisible: false })
            .setData(safeLine(times, cci) as any);
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 100 })));
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: -100 })));
    }, [showCci]);

    // ─── ADX Effect ──────────────────────────────────────────────
    buildSubChart(adxRef, 120, (chart, times) => {
        if (!showAdx) return;
        const highs = candles.map(d => d.high); const lows = candles.map(d => d.low); const closes = candles.map(d => d.close);
        const { adx, pdi, ndi } = calcADX(highs, lows, closes, 14);
        chart.addSeries(LineSeries, { color: '#ec4899', lineWidth: 2, priceLineVisible: false })
            .setData(safeLine(times, adx) as any);
        chart.addSeries(LineSeries, { color: '#22c55e', lineWidth: 1, priceLineVisible: false })
            .setData(safeLine(times, pdi) as any);
        chart.addSeries(LineSeries, { color: '#ef4444', lineWidth: 1, priceLineVisible: false })
            .setData(safeLine(times, ndi) as any);
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 25 })));
    }, [showAdx]);

    // ─── Williams %R Effect ──────────────────────────────────────
    buildSubChart(williamsRef, 100, (chart, times) => {
        if (!showWilliams) return;
        const highs = candles.map(d => d.high); const lows = candles.map(d => d.low); const closes = candles.map(d => d.close);
        const williams = calcWilliamsR(highs, lows, closes, 14);
        chart.addSeries(LineSeries, { color: '#22d3ee', lineWidth: 2, priceLineVisible: false })
            .setData(safeLine(times, williams) as any);
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: -20 })));
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: -80 })));
    }, [showWilliams]);

    // ─── MFI Effect ──────────────────────────────────────────────
    buildSubChart(mfiRef, 100, (chart, times) => {
        if (!showMfi) return;
        const highs = candles.map(d => d.high); const lows = candles.map(d => d.low); const closes = candles.map(d => d.close);
        const volumes = candles.map(d => (d as any).volume ?? 0) as number[];
        const mfi = calcMFI(highs, lows, closes, volumes, 14);
        chart.addSeries(LineSeries, { color: '#a855f7', lineWidth: 2, priceLineVisible: false })
            .setData(safeLine(times, mfi) as any);
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 80 })));
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 20 })));
    }, [showMfi]);

    // ─── CMF Effect ──────────────────────────────────────────────
    buildSubChart(cmfRef, 100, (chart, times) => {
        if (!showCmf) return;
        const highs = candles.map(d => d.high); const lows = candles.map(d => d.low); const closes = candles.map(d => d.close);
        const volumes = candles.map(d => (d as any).volume ?? 0) as number[];
        const cmf = calcCMF(highs, lows, closes, volumes, 20);
        chart.addSeries(HistogramSeries, { priceLineVisible: false, lastValueVisible: true })
            .setData(times.map((t, i) => (cmf[i] === null || isNaN(cmf[i]!)) ? { time: t } : { time: t, value: cmf[i]!, color: cmf[i]! > 0 ? '#22c55e80' : '#ef444480' }) as any);
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 0 })));
    }, [showCmf]);

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
                    {/* Zoom buttons */}
                    <div className="flex items-center gap-0.5 bg-white/5 rounded-lg border border-white/10 p-0.5">
                        <button onClick={zoomIn} className="h-7 w-7 flex items-center justify-center rounded-md hover:bg-white/10 text-white/50 hover:text-white transition-all" title="Zoom In">
                            <ZoomIn size={14} />
                        </button>
                        <button onClick={zoomOut} className="h-7 w-7 flex items-center justify-center rounded-md hover:bg-white/10 text-white/50 hover:text-white transition-all" title="Zoom Out">
                            <ZoomOut size={14} />
                        </button>
                    </div>
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
            <div className="relative w-full flex-1" style={{ minHeight: 300 }}>
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

            {/* CCI Panel */}
            {showCci && (
                <div className="border-t border-border/30 flex-shrink-0">
                    <div className="flex items-center justify-between px-3 py-1.5 bg-card-hover/30">
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-violet-400/80">CCI (20)</span>
                            <span className="text-[8px] text-muted font-bold">+100 / -100</span>
                        </div>
                    </div>
                    <div ref={cciRef} className="w-full" style={{ height: 100 }} />
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

            {/* Williams %R Panel */}
            {showWilliams && (
                <div className="border-t border-border/30 flex-shrink-0">
                    <div className="flex items-center justify-between px-3 py-1.5 bg-card-hover/30">
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-cyan-400/80">Williams %R (14)</span>
                            <span className="text-[8px] text-muted font-bold">-20 / -80</span>
                        </div>
                    </div>
                    <div ref={williamsRef} className="w-full" style={{ height: 100 }} />
                </div>
            )}

            {/* MFI Panel */}
            {showMfi && (
                <div className="border-t border-border/30 flex-shrink-0">
                    <div className="flex items-center justify-between px-3 py-1.5 bg-card-hover/30">
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-purple-400/80">MFI (14)</span>
                            <span className="text-[8px] text-muted font-bold">80 / 20</span>
                        </div>
                    </div>
                    <div ref={mfiRef} className="w-full" style={{ height: 100 }} />
                </div>
            )}

            {/* CMF Panel */}
            {showCmf && (
                <div className="border-t border-border/30 flex-shrink-0">
                    <div className="flex items-center justify-between px-3 py-1.5 bg-card-hover/30">
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-blue-400/80">CMF (20)</span>
                            <span className="text-[8px] text-muted font-bold">Accumulation/Dist</span>
                        </div>
                    </div>
                    <div ref={cmfRef} className="w-full" style={{ height: 100 }} />
                </div>
            )}
        </div>
    );
}
