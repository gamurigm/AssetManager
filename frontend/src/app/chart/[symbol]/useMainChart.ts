import React, { useEffect, useRef } from "react";
import {
    createChart,
    CandlestickSeries,
    LineSeries,
    IChartApi,
    ISeriesApi
} from "lightweight-charts";
import {
    calcMA,
    calcFibLevels,
    calcBollingerBands,
    calcParabolicSAR,
    calcSupertrend,
    MAConfig
} from "./chartMath";
import { getChartPriceFormat } from "@/lib/marketFormatting";

export function useMainChart(
    symbol: string,
    rawData: any[],
    chartOpts: () => any,
    mas: MAConfig[],
    showFib: boolean,
    fibLookback: number,
    showBB: boolean,
    bbPeriod: number,
    bbMult: number,
    showPSAR: boolean,
    psarStep: number,
    psarMax: number,
    showSupertrend: boolean,
    supertrendPeriod: number,
    supertrendMult: number,
    mainChartRef: React.MutableRefObject<HTMLDivElement | null>,
    mainChartApi: React.MutableRefObject<IChartApi | null>,
    candleSeriesRef: React.MutableRefObject<ISeriesApi<"Candlestick"> | null>,
) {
    const overlaySeriesRefs = useRef<any[]>([]);
    const fibLineRefs = useRef<any[]>([]);
    const resizeObserverRef = useRef<ResizeObserver | null>(null);
    const hasFitContentRef = useRef(false);

    useEffect(() => {
        if (!mainChartRef.current || mainChartApi.current) return;

        const chart = createChart(mainChartRef.current, {
            ...chartOpts(),
            width: mainChartRef.current.clientWidth,
            height: mainChartRef.current.clientHeight || 400,
        });
        mainChartApi.current = chart;

        const candleSeries = chart.addSeries(CandlestickSeries, {
            upColor: '#26a69d', downColor: '#ef5350',
            borderVisible: false, wickUpColor: '#26a69d', wickDownColor: '#ef5350',
            priceFormat: getChartPriceFormat({ symbol }),
        });

        candleSeriesRef.current = candleSeries;
        window.dispatchEvent(new CustomEvent('mainChartReady'));

        const handleResize = () => {
            if (!mainChartApi.current || !mainChartRef.current) return;
            try {
                mainChartApi.current.applyOptions({
                    width: mainChartRef.current.clientWidth,
                    height: mainChartRef.current.clientHeight || 400,
                });
            } catch {
                // Chart may be in teardown during route changes.
            }
        };

        const observer = new ResizeObserver(handleResize);
        observer.observe(mainChartRef.current);
        resizeObserverRef.current = observer;

        return () => {
            resizeObserverRef.current?.disconnect();
            resizeObserverRef.current = null;

            const activeChart = mainChartApi.current;
            if (activeChart) {
                overlaySeriesRefs.current.forEach(series => {
                    try { activeChart.removeSeries(series); } catch { }
                });
            }
            overlaySeriesRefs.current = [];

            fibLineRefs.current.forEach(line => {
                try { candleSeriesRef.current?.removePriceLine(line); } catch { }
            });
            fibLineRefs.current = [];

            if (activeChart) {
                try { activeChart.remove(); } catch { }
            }

            candleSeriesRef.current = null;
            mainChartApi.current = null;
            hasFitContentRef.current = false;
        };
    }, [chartOpts, mainChartRef, mainChartApi, candleSeriesRef]);

    useEffect(() => {
        const chart = mainChartApi.current;
        const candleSeries = candleSeriesRef.current;
        if (!chart || !candleSeries) return;

        try {
            chart.applyOptions({
                ...chartOpts(),
                width: mainChartRef.current?.clientWidth,
                height: mainChartRef.current?.clientHeight || 400,
            });
        } catch {
            // Ignore mid-teardown updates.
        }

        if (rawData.length === 0) return;

        const savedRange = chart.timeScale().getVisibleLogicalRange();

        candleSeries.setData(rawData.map(d => ({
            time: d.time as any,
            open: d.open,
            high: d.high,
            low: d.low,
            close: d.close
        })));

        overlaySeriesRefs.current.forEach(series => {
            try { chart.removeSeries(series); } catch { }
        });
        overlaySeriesRefs.current = [];

        fibLineRefs.current.forEach(line => {
            try { candleSeries.removePriceLine(line); } catch { }
        });
        fibLineRefs.current = [];

        const closes = rawData.map(d => d.close);
        const times = rawData.map(d => d.time as any);
        const highs = rawData.map(d => d.high);
        const lows = rawData.map(d => d.low);

        // Render Moving Averages
        for (const ma of mas) {
            if (!ma.visible) continue;
            const values = calcMA(ma.type, closes, ma.period);
            const series = chart.addSeries(LineSeries, {
                color: ma.color,
                lineWidth: 1,
                priceLineVisible: false,
                crosshairMarkerVisible: false,
                priceFormat: getChartPriceFormat({ symbol }),
            });
            series.setData(values.map((v, i) => isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);
            overlaySeriesRefs.current.push(series);
        }

        // Render Fibonacci Retracement
        if (showFib && rawData.length > 0) {
            const fibs = calcFibLevels(highs, lows, fibLookback);
            for (const fib of fibs) {
                const line = candleSeries.createPriceLine({
                    price: fib.price,
                    color: fib.color,
                    lineWidth: 1,
                    lineStyle: 2,
                    axisLabelVisible: true,
                    title: `Fib ${fib.label}`
                });
                fibLineRefs.current.push(line);
            }
        }

        // Render Bollinger Bands
        if (showBB) {
            const { middle, upper, lower } = calcBollingerBands(closes, bbPeriod, bbMult);
            const upperSeries = chart.addSeries(LineSeries, { color: 'rgba(33,150,243,0.5)', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false, priceFormat: getChartPriceFormat({ symbol }) });
            upperSeries.setData(upper.map((v, i) => isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);
            overlaySeriesRefs.current.push(upperSeries);

            const middleSeries = chart.addSeries(LineSeries, { color: 'rgba(33,150,243,0.3)', lineWidth: 1, lineStyle: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false, priceFormat: getChartPriceFormat({ symbol }) });
            middleSeries.setData(middle.map((v, i) => isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);
            overlaySeriesRefs.current.push(middleSeries);

            const lowerSeries = chart.addSeries(LineSeries, { color: 'rgba(33,150,243,0.5)', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false, priceFormat: getChartPriceFormat({ symbol }) });
            lowerSeries.setData(lower.map((v, i) => isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);
            overlaySeriesRefs.current.push(lowerSeries);
        }

        // Parabolic SAR
        if (showPSAR && rawData.length > 5) {
            const sar = calcParabolicSAR(highs, lows, psarStep, psarMax);
            const sarSeries = chart.addSeries(LineSeries, { color: '#ec4899', lineWidth: 1, lineStyle: 3, pointMarkersVisible: true, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false, priceFormat: getChartPriceFormat({ symbol }) });
            sarSeries.setData(times.map((t, i) => (sar[i] === null || isNaN(sar[i]!)) ? { time: t } : { time: t, value: sar[i]! }) as any);
            overlaySeriesRefs.current.push(sarSeries);
        }

        // Supertrend
        if (showSupertrend && rawData.length > 20) {
            const { supertrend, dir } = calcSupertrend(highs, lows, closes, supertrendPeriod, supertrendMult);
            const upData = times.map((t, i) => (dir[i] === 1 && supertrend[i] !== null && !isNaN(supertrend[i]!)) ? { time: t, value: supertrend[i]! } : { time: t });
            const downData = times.map((t, i) => (dir[i] === -1 && supertrend[i] !== null && !isNaN(supertrend[i]!)) ? { time: t, value: supertrend[i]! } : { time: t });
            const upSeries = chart.addSeries(LineSeries, { color: '#2dd4bf', lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false, priceFormat: getChartPriceFormat({ symbol }) });
            upSeries.setData(upData as any);
            overlaySeriesRefs.current.push(upSeries);

            const downSeries = chart.addSeries(LineSeries, { color: '#ef4444', lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false, priceFormat: getChartPriceFormat({ symbol }) });
            downSeries.setData(downData as any);
            overlaySeriesRefs.current.push(downSeries);
        }

        if (savedRange) {
            chart.timeScale().setVisibleLogicalRange(savedRange);
        } else if (!hasFitContentRef.current) {
            chart.timeScale().fitContent();
            hasFitContentRef.current = true;
        }
    }, [symbol, rawData, chartOpts, mas, showFib, fibLookback, showBB, bbPeriod, bbMult, showPSAR, psarStep, psarMax, showSupertrend, supertrendPeriod, supertrendMult]);
}
