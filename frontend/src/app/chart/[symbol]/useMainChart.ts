import React, { useEffect } from "react";
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

export function useMainChart(
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
    useEffect(() => {
        if (!mainChartRef.current || rawData.length === 0) return;

        let savedRange: any = null;
        if (mainChartApi.current) {
            savedRange = mainChartApi.current.timeScale().getVisibleLogicalRange();
            const oldChart = mainChartApi.current;
            try { oldChart.remove(); } catch (e) { }
            mainChartApi.current = null;
        }

        const chart = createChart(mainChartRef.current, {
            ...chartOpts(),
            width: mainChartRef.current.clientWidth,
            height: mainChartRef.current.clientHeight || 400,
        });
        mainChartApi.current = chart;
        window.dispatchEvent(new CustomEvent('mainChartReady'));

        const candleSeries = chart.addSeries(CandlestickSeries, {
            upColor: '#26a69d', downColor: '#ef5350',
            borderVisible: false, wickUpColor: '#26a69d', wickDownColor: '#ef5350',
        });

        candleSeriesRef.current = candleSeries;
        candleSeries.setData(rawData.map(d => ({
            time: d.time as any,
            open: d.open,
            high: d.high,
            low: d.low,
            close: d.close
        })));

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
                crosshairMarkerVisible: false
            });
            series.setData(values.map((v, i) => isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);
        }

        // Render Fibonacci Retracement
        if (showFib && rawData.length > 0) {
            const fibs = calcFibLevels(highs, lows, fibLookback);
            for (const fib of fibs) {
                candleSeries.createPriceLine({
                    price: fib.price,
                    color: fib.color,
                    lineWidth: 1,
                    lineStyle: 2,
                    axisLabelVisible: true,
                    title: `Fib ${fib.label}`
                });
            }
        }

        // Render Bollinger Bands
        if (showBB) {
            const { middle, upper, lower } = calcBollingerBands(closes, bbPeriod, bbMult);
            chart.addSeries(LineSeries, { color: 'rgba(33,150,243,0.5)', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(upper.map((v, i) => isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);
            chart.addSeries(LineSeries, { color: 'rgba(33,150,243,0.3)', lineWidth: 1, lineStyle: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(middle.map((v, i) => isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);
            chart.addSeries(LineSeries, { color: 'rgba(33,150,243,0.5)', lineWidth: 1, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(lower.map((v, i) => isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);
        }

        // Parabolic SAR
        if (showPSAR && rawData.length > 5) {
            const sar = calcParabolicSAR(highs, lows, psarStep, psarMax);
            chart.addSeries(LineSeries, { color: '#ec4899', lineWidth: 1, lineStyle: 3, pointMarkersVisible: true, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(times.map((t, i) => (sar[i] === null || isNaN(sar[i]!)) ? { time: t } : { time: t, value: sar[i]! }) as any);
        }

        // Supertrend
        if (showSupertrend && rawData.length > 20) {
            const { supertrend, dir } = calcSupertrend(highs, lows, closes, supertrendPeriod, supertrendMult);
            const upData = times.map((t, i) => (dir[i] === 1 && supertrend[i] !== null && !isNaN(supertrend[i]!)) ? { time: t, value: supertrend[i]! } : { time: t });
            const downData = times.map((t, i) => (dir[i] === -1 && supertrend[i] !== null && !isNaN(supertrend[i]!)) ? { time: t, value: supertrend[i]! } : { time: t });
            chart.addSeries(LineSeries, { color: '#2dd4bf', lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(upData as any);
            chart.addSeries(LineSeries, { color: '#ef4444', lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false, lastValueVisible: false })
                .setData(downData as any);
        }

        if (savedRange) {
            chart.timeScale().setVisibleLogicalRange(savedRange);
        } else {
            chart.timeScale().fitContent();
        }

        const handleResize = () => {
            if (mainChartApi.current && mainChartRef.current) {
                mainChartApi.current.applyOptions({ width: mainChartRef.current.clientWidth, height: mainChartRef.current.clientHeight || 400 });
            }
        };

        const ro = new ResizeObserver(handleResize);
        ro.observe(mainChartRef.current);

        return () => {
            ro.disconnect();
            if (mainChartApi.current) {
                const oldChart = mainChartApi.current;
                try { oldChart.remove(); } catch (e) { }
                mainChartApi.current = null;
            }
        };
    }, [rawData, chartOpts, mas, showFib, fibLookback, showBB, bbPeriod, bbMult, showPSAR, psarStep, psarMax, showSupertrend, supertrendPeriod, supertrendMult]);
}
