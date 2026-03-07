import React, { useEffect, useRef } from "react";
import { createChart, IChartApi, HistogramSeries, LineSeries } from "lightweight-charts";
import { Plus, Minus } from "lucide-react";
import { ParamInput } from "./ChartUIComponents";
import { calcMACD, calcStochastic, calcATR, calcWilliamsR, calcMFI, calcCMF, calcRSI, calcCCI, calcADX } from "./chartMath";

export interface ChartSubPanelsProps {
    rawData: any[];
    chartOpts: (h?: number) => any;
    mainChartApi: React.MutableRefObject<IChartApi | null>;

    showMACD: boolean; setShowMACD: (v: boolean) => void;
    macdFast: number; setMacdFast: (v: number) => void;
    macdSlow: number; setMacdSlow: (v: number) => void;
    macdSignal: number; setMacdSignal: (v: number) => void;

    showStoch: boolean; setShowStoch: (v: boolean) => void;
    stochK: number; setStochK: (v: number) => void;
    stochD: number; setStochD: (v: number) => void;
    stochSmooth: number; setStochSmooth: (v: number) => void;

    showATR: boolean; setShowATR: (v: boolean) => void;
    atrPeriod: number; setAtrPeriod: (v: number) => void;

    showWilliams: boolean;
    williamsPeriod: number;
    showMFI: boolean;
    mfiPeriod: number;
    showCMF: boolean;
    cmfPeriod: number;
    showRSI: boolean;
    rsiPeriod: number;
    showCCI: boolean;
    cciPeriod: number;
    showADX: boolean;
    adxPeriod: number;
}

export function ChartSubPanels({
    rawData, chartOpts, mainChartApi,
    showMACD, setShowMACD, macdFast, setMacdFast, macdSlow, setMacdSlow, macdSignal, setMacdSignal,
    showStoch, setShowStoch, stochK, setStochK, stochD, setStochD, stochSmooth, setStochSmooth,
    showATR, setShowATR, atrPeriod, setAtrPeriod,
    showWilliams, williamsPeriod, showMFI, mfiPeriod, showCMF, cmfPeriod,
    showRSI, rsiPeriod, showCCI, cciPeriod, showADX, adxPeriod
}: ChartSubPanelsProps) {

    const macdChartRef = useRef<HTMLDivElement>(null);
    const macdChartApi = useRef<IChartApi | null>(null);

    const stochChartRef = useRef<HTMLDivElement>(null);
    const stochChartApi = useRef<IChartApi | null>(null);

    const atrChartRef = useRef<HTMLDivElement>(null);
    const atrChartApi = useRef<IChartApi | null>(null);

    const williamsChartRef = useRef<HTMLDivElement>(null);
    const williamsChartApi = useRef<IChartApi | null>(null);

    const mfiChartRef = useRef<HTMLDivElement>(null);
    const mfiChartApi = useRef<IChartApi | null>(null);

    const cmfChartRef = useRef<HTMLDivElement>(null);
    const cmfChartApi = useRef<IChartApi | null>(null);

    const rsiChartRef = useRef<HTMLDivElement>(null);
    const rsiChartApi = useRef<IChartApi | null>(null);

    const cciChartRef = useRef<HTMLDivElement>(null);
    const cciChartApi = useRef<IChartApi | null>(null);

    const adxChartRef = useRef<HTMLDivElement>(null);
    const adxChartApi = useRef<IChartApi | null>(null);

    const syncPanelRangeToMain = (chart: IChartApi) => {
        try {
            const mainRange = mainChartApi.current?.timeScale().getVisibleLogicalRange();
            if (mainRange) {
                chart.timeScale().setVisibleLogicalRange(mainRange);
                return;
            }
        } catch {
            // Fall through to fitContent when the main chart is mid-teardown.
        }

        try {
            chart.timeScale().fitContent();
        } catch {
            // Ignore teardown races.
        }
    };

    // MACD
    useEffect(() => {
        if (!macdChartRef.current || rawData.length === 0 || !showMACD) return;
        if (macdChartApi.current) { try { macdChartApi.current.remove(); } catch (e) { } macdChartApi.current = null; }

        const chart = createChart(macdChartRef.current, { ...chartOpts(146), width: macdChartRef.current.clientWidth });
        macdChartApi.current = chart;

        const closes = rawData.map(d => d.close);
        const times = rawData.map(d => d.time as any);
        const { macdLine, signalLine, histogram } = calcMACD(closes, macdFast, macdSlow, macdSignal);

        const histSeries = chart.addSeries(HistogramSeries, { priceLineVisible: false, lastValueVisible: false });
        histSeries.setData(histogram.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v, color: v >= 0 ? '#26a69d' : '#ef5350' }) as any);

        const macdSeries = chart.addSeries(LineSeries, { color: '#2962FF', lineWidth: 1, priceLineVisible: false, lastValueVisible: false });
        macdSeries.setData(macdLine.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);

        const signalSeries = chart.addSeries(LineSeries, { color: '#FF6D00', lineWidth: 1, priceLineVisible: false, lastValueVisible: false });
        signalSeries.setData(signalLine.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);

        syncPanelRangeToMain(chart);
        const ro = new ResizeObserver(() => { if (macdChartRef.current) chart.applyOptions({ width: macdChartRef.current.clientWidth }); });
        ro.observe(macdChartRef.current);
        return () => { ro.disconnect(); try { chart.remove(); } catch (e) { } macdChartApi.current = null; };
    }, [rawData, showMACD, macdFast, macdSlow, macdSignal, chartOpts]);

    // Stochastic
    useEffect(() => {
        if (!stochChartRef.current || rawData.length === 0 || !showStoch) return;
        if (stochChartApi.current) { try { stochChartApi.current.remove(); } catch (e) { } stochChartApi.current = null; }

        const chart = createChart(stochChartRef.current, { ...chartOpts(146), width: stochChartRef.current.clientWidth });
        stochChartApi.current = chart;

        const highs = rawData.map(d => d.high);
        const lows = rawData.map(d => d.low);
        const closes = rawData.map(d => d.close);
        const times = rawData.map(d => d.time as any);
        const { kLine, dLine } = calcStochastic(highs, lows, closes, stochK, stochD, stochSmooth);

        const kSeries = chart.addSeries(LineSeries, { color: '#2962FF', lineWidth: 1, priceLineVisible: false, lastValueVisible: false, title: '%K' });
        kSeries.setData(kLine.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);

        const dSeries = chart.addSeries(LineSeries, { color: '#FF6D00', lineWidth: 1, priceLineVisible: false, lastValueVisible: false, title: '%D' });
        dSeries.setData(dLine.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);

        syncPanelRangeToMain(chart);
        const ro = new ResizeObserver(() => { if (stochChartRef.current) chart.applyOptions({ width: stochChartRef.current.clientWidth }); });
        ro.observe(stochChartRef.current);
        return () => { ro.disconnect(); try { chart.remove(); } catch (e) { } stochChartApi.current = null; };
    }, [rawData, showStoch, stochK, stochD, stochSmooth, chartOpts]);

    // ATR
    useEffect(() => {
        if (!atrChartRef.current || rawData.length === 0 || !showATR) return;
        if (atrChartApi.current) { try { atrChartApi.current.remove(); } catch (e) { } atrChartApi.current = null; }

        const chart = createChart(atrChartRef.current, { ...chartOpts(146), width: atrChartRef.current.clientWidth });
        atrChartApi.current = chart;

        const highs = rawData.map(d => d.high);
        const lows = rawData.map(d => d.low);
        const closes = rawData.map(d => d.close);
        const times = rawData.map(d => d.time as any);
        const atrValues = calcATR(highs, lows, closes, atrPeriod);

        const atrSeries = chart.addSeries(LineSeries, { color: '#e040fb', lineWidth: 2, priceLineVisible: false, lastValueVisible: true, title: 'ATR' });
        atrSeries.setData(atrValues.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);

        syncPanelRangeToMain(chart);
        const ro = new ResizeObserver(() => { if (atrChartRef.current) chart.applyOptions({ width: atrChartRef.current.clientWidth }); });
        ro.observe(atrChartRef.current);
        return () => { ro.disconnect(); try { chart.remove(); } catch (e) { } atrChartApi.current = null; };
    }, [rawData, showATR, atrPeriod, chartOpts]);

    // Williams %R
    useEffect(() => {
        if (!williamsChartRef.current || rawData.length === 0 || !showWilliams) return;
        if (williamsChartApi.current) { try { williamsChartApi.current.remove(); } catch (e) { } williamsChartApi.current = null; }
        const chart = createChart(williamsChartRef.current, { ...chartOpts(146), width: williamsChartRef.current.clientWidth });
        williamsChartApi.current = chart;
        const highs = rawData.map(d => d.high), lows = rawData.map(d => d.low), closes = rawData.map(d => d.close), times = rawData.map(d => d.time as any);
        const w = calcWilliamsR(highs, lows, closes, williamsPeriod);

        chart.addSeries(LineSeries, { color: '#0ea5e9', lineWidth: 2, priceLineVisible: false, lastValueVisible: true, title: 'Williams %R' })
            .setData(w.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);

        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: -20 })));
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: -80 })));

        syncPanelRangeToMain(chart);
        const ro = new ResizeObserver(() => { if (williamsChartRef.current) chart.applyOptions({ width: williamsChartRef.current.clientWidth }); });
        ro.observe(williamsChartRef.current);
        return () => { ro.disconnect(); try { chart.remove(); } catch (e) { } williamsChartApi.current = null; };
    }, [rawData, showWilliams, williamsPeriod, chartOpts]);

    // MFI
    useEffect(() => {
        if (!mfiChartRef.current || rawData.length === 0 || !showMFI) return;
        if (mfiChartApi.current) { try { mfiChartApi.current.remove(); } catch (e) { } mfiChartApi.current = null; }
        const chart = createChart(mfiChartRef.current, { ...chartOpts(146), width: mfiChartRef.current.clientWidth });
        mfiChartApi.current = chart;
        const highs = rawData.map(d => d.high), lows = rawData.map(d => d.low), closes = rawData.map(d => d.close), volumes = rawData.map(d => d.volume ?? 0), times = rawData.map(d => d.time as any);
        const mfi = calcMFI(highs, lows, closes, volumes, mfiPeriod);

        chart.addSeries(LineSeries, { color: '#a855f7', lineWidth: 2, priceLineVisible: false, lastValueVisible: true, title: 'MFI' })
            .setData(mfi.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);

        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 80 })));
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 20 })));

        syncPanelRangeToMain(chart);
        const ro = new ResizeObserver(() => { if (mfiChartRef.current) chart.applyOptions({ width: mfiChartRef.current.clientWidth }); });
        ro.observe(mfiChartRef.current);
        return () => { ro.disconnect(); try { chart.remove(); } catch (e) { } mfiChartApi.current = null; };
    }, [rawData, showMFI, mfiPeriod, chartOpts]);

    // CMF
    useEffect(() => {
        if (!cmfChartRef.current || rawData.length === 0 || !showCMF) return;
        if (cmfChartApi.current) { try { cmfChartApi.current.remove(); } catch (e) { } cmfChartApi.current = null; }
        const chart = createChart(cmfChartRef.current, { ...chartOpts(146), width: cmfChartRef.current.clientWidth });
        cmfChartApi.current = chart;
        const highs = rawData.map(d => d.high), lows = rawData.map(d => d.low), closes = rawData.map(d => d.close), volumes = rawData.map(d => d.volume), times = rawData.map(d => d.time as any);
        const cmf = calcCMF(highs, lows, closes, volumes, cmfPeriod);

        const cmfSeries = chart.addSeries(HistogramSeries, { priceLineVisible: false, lastValueVisible: true });
        cmfSeries.setData(cmf.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v, color: v > 0 ? 'rgba(38,166,157,0.7)' : 'rgba(239,83,80,0.7)' }) as any);

        // Add 0-line for CMF
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 0 })));
        const ro = new ResizeObserver(() => { if (cmfChartRef.current) chart.applyOptions({ width: cmfChartRef.current.clientWidth }); });
        ro.observe(cmfChartRef.current);
        return () => { ro.disconnect(); try { chart.remove(); } catch (e) { } cmfChartApi.current = null; };
    }, [rawData, showCMF, cmfPeriod, chartOpts]);

    // RSI
    useEffect(() => {
        if (!rsiChartRef.current || rawData.length === 0 || !showRSI) return;
        if (rsiChartApi.current) { try { rsiChartApi.current.remove(); } catch (e) { } rsiChartApi.current = null; }
        const chart = createChart(rsiChartRef.current, { ...chartOpts(146), width: rsiChartRef.current.clientWidth });
        rsiChartApi.current = chart;
        const closes = rawData.map(d => d.close), times = rawData.map(d => d.time as any);
        const rsi = calcRSI(closes, rsiPeriod);

        chart.addSeries(LineSeries, { color: '#f43f5e', lineWidth: 2, priceLineVisible: false, lastValueVisible: true, title: 'RSI' })
            .setData(rsi.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);

        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 70 })));
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 30 })));

        syncPanelRangeToMain(chart);
        const ro = new ResizeObserver(() => { if (rsiChartRef.current) chart.applyOptions({ width: rsiChartRef.current.clientWidth }); });
        ro.observe(rsiChartRef.current);
        return () => { ro.disconnect(); try { chart.remove(); } catch (e) { } rsiChartApi.current = null; };
    }, [rawData, showRSI, rsiPeriod, chartOpts]);

    // CCI
    useEffect(() => {
        if (!cciChartRef.current || rawData.length === 0 || !showCCI) return;
        if (cciChartApi.current) { try { cciChartApi.current.remove(); } catch (e) { } cciChartApi.current = null; }
        const chart = createChart(cciChartRef.current, { ...chartOpts(146), width: cciChartRef.current.clientWidth });
        cciChartApi.current = chart;
        const highs = rawData.map(d => d.high), lows = rawData.map(d => d.low), closes = rawData.map(d => d.close), times = rawData.map(d => d.time as any);
        const cci = calcCCI(highs, lows, closes, cciPeriod);

        chart.addSeries(LineSeries, { color: '#84cc16', lineWidth: 2, priceLineVisible: false, lastValueVisible: true, title: 'CCI' })
            .setData(cci.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);

        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 100 })));
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: -100 })));

        syncPanelRangeToMain(chart);
        const ro = new ResizeObserver(() => { if (cciChartRef.current) chart.applyOptions({ width: cciChartRef.current.clientWidth }); });
        ro.observe(cciChartRef.current);
        return () => { ro.disconnect(); try { chart.remove(); } catch (e) { } cciChartApi.current = null; };
    }, [rawData, showCCI, cciPeriod, chartOpts]);

    // ADX
    useEffect(() => {
        if (!adxChartRef.current || rawData.length === 0 || !showADX) return;
        if (adxChartApi.current) { try { adxChartApi.current.remove(); } catch (e) { } adxChartApi.current = null; }
        const chart = createChart(adxChartRef.current, { ...chartOpts(146), width: adxChartRef.current.clientWidth });
        adxChartApi.current = chart;
        const highs = rawData.map(d => d.high), lows = rawData.map(d => d.low), closes = rawData.map(d => d.close), times = rawData.map(d => d.time as any);
        const { adx, pdi, ndi } = calcADX(highs, lows, closes, adxPeriod);

        chart.addSeries(LineSeries, { color: '#d946ef', lineWidth: 2, priceLineVisible: false, lastValueVisible: true, title: 'ADX' })
            .setData(adx.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);
        chart.addSeries(LineSeries, { color: '#22c55e', lineWidth: 1, priceLineVisible: false, lastValueVisible: false, title: '+DI' })
            .setData(pdi.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);
        chart.addSeries(LineSeries, { color: '#ef4444', lineWidth: 1, priceLineVisible: false, lastValueVisible: false, title: '-DI' })
            .setData(ndi.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);

        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 25 })));

        syncPanelRangeToMain(chart);
        const ro = new ResizeObserver(() => { if (adxChartRef.current) chart.applyOptions({ width: adxChartRef.current.clientWidth }); });
        ro.observe(adxChartRef.current);
        return () => { ro.disconnect(); try { chart.remove(); } catch (e) { } adxChartApi.current = null; };
    }, [rawData, showADX, adxPeriod, chartOpts]);

    // ─── Unified Chart Syncing ─────────────────────────────────────────────
    useEffect(() => {
        let cleanups: (() => void)[] = [];

        const doSync = () => {
            // clean up old unsubs
            cleanups.forEach(c => c());
            cleanups = [];

            if (!mainChartApi.current) return;
            const main = mainChartApi.current;
            const subApis = [
                macdChartApi.current, stochChartApi.current, atrChartApi.current,
                williamsChartApi.current, mfiChartApi.current, cmfChartApi.current,
                rsiChartApi.current, cciChartApi.current, adxChartApi.current
            ].filter(Boolean) as IChartApi[];

            if (subApis.length === 0) return;

            subApis.forEach(sub => {
                try {
                    const mainTS = main.timeScale();
                    const subTS = sub.timeScale();
                    const r = mainTS.getVisibleLogicalRange();
                    if (r) subTS.setVisibleLogicalRange(r);

                    const onMain = (range: any) => { if (range) subTS.setVisibleLogicalRange(range); };
                    const onSub = (range: any) => { if (range) mainTS.setVisibleLogicalRange(range); };

                    mainTS.subscribeVisibleLogicalRangeChange(onMain);
                    subTS.subscribeVisibleLogicalRangeChange(onSub);

                    cleanups.push(() => {
                        mainTS.unsubscribeVisibleLogicalRangeChange(onMain);
                        subTS.unsubscribeVisibleLogicalRangeChange(onSub);
                    });
                } catch (e) { }
            });

            // Sync crosshairs
            let isSyncing = false;
            const charts = [main, ...subApis];
            charts.forEach((chart, idx) => {
                const onCrosshair = (param: any) => {
                    if (isSyncing) return;
                    isSyncing = true;
                    charts.forEach((otherChart, otherIdx) => {
                        if (idx === otherIdx) return;
                        if (param.time === undefined || param.point === undefined || param.point.x < 0 || param.point.y < 0) {
                            otherChart.clearCrosshairPosition();
                        } else {
                            // Horizontal panning is synced, crosshair moves with cursor.
                            // setCrosshairPosition can throw if out of bounds, so just clearing is safest fallback,
                            // but we can try to apply it to match 'time' to snap across charts vertically.
                            try {
                                // Lightweight Charts v4 expects crosshair positions. If we just leave it to default 'crosshair: { horzLine: {visible: false}}' in the layout, the vertLine syncs natively via logicalRange mostly, but to force the exact vertical line we can check if it supports it.
                                // If the user wants precise crosshair sync, we do:
                                otherChart.setCrosshairPosition(0, param.time, otherChart.timeScale() as any);
                            } catch (err) {
                                otherChart.clearCrosshairPosition();
                            }
                        }
                    });
                    isSyncing = false;
                };
                chart.subscribeCrosshairMove(onCrosshair);
                cleanups.push(() => chart.unsubscribeCrosshairMove(onCrosshair));
            });
        };

        doSync();
        window.addEventListener('mainChartReady', doSync);
        return () => {
            window.removeEventListener('mainChartReady', doSync);
            cleanups.forEach(c => c());
        };
    }, [rawData, showMACD, showStoch, showATR, showWilliams, williamsPeriod, showMFI, mfiPeriod, showCMF, cmfPeriod, showRSI, rsiPeriod, showCCI, cciPeriod, showADX, adxPeriod]);

    return (
        <>
            {/* ─── MACD Panel ─────────────────────────────────────────────── */}
            <div className="flex-shrink-0 border-t border-white/5" style={{ height: showMACD ? 170 : 24 }}>
                <div className="flex items-center justify-between px-3 bg-[#0c0c0c] cursor-pointer select-none" style={{ height: 24 }} onClick={() => setShowMACD(!showMACD)}>
                    <div className="flex items-center gap-2">
                        <span className="text-[10px] font-black uppercase tracking-[0.15em] text-white/50">MACD</span>
                        <span className="text-[9px] font-mono text-white/30">({macdFast},{macdSlow},{macdSignal})</span>
                        {showMACD ? <Minus size={12} strokeWidth={3} className="text-white/60 hover:text-white" /> : <Plus size={12} strokeWidth={3} className="text-white/60 hover:text-white" />}
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
                        {showStoch ? <Minus size={12} strokeWidth={3} className="text-white/60 hover:text-white" /> : <Plus size={12} strokeWidth={3} className="text-white/60 hover:text-white" />}
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
                        {showATR ? <Minus size={12} strokeWidth={3} className="text-white/60 hover:text-white" /> : <Plus size={12} strokeWidth={3} className="text-white/60 hover:text-white" />}
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
                            <span className="text-[9px] font-mono text-white/30">({williamsPeriod})</span>
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
                            <span className="text-[9px] font-mono text-white/30">({mfiPeriod})</span>
                        </div>
                    </div>
                    <div ref={mfiChartRef} style={{ width: '100%', height: 146 }} />
                </div>
            )}

            {/* CMF Panel */}
            {showCMF && (
                <div className="flex-shrink-0 border-t border-white/5" style={{ height: 170 }}>
                    <div className="flex items-center justify-between px-3 bg-[#0c0c0c] select-none" style={{ height: 24 }}>
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-blue-400/70">CMF</span>
                            <span className="text-[9px] font-mono text-white/30">({cmfPeriod})</span>
                        </div>
                    </div>
                    <div ref={cmfChartRef} style={{ width: '100%', height: 146 }} />
                </div>
            )}

            {/* RSI Panel */}
            {showRSI && (
                <div className="flex-shrink-0 border-t border-white/5" style={{ height: 170 }}>
                    <div className="flex items-center justify-between px-3 bg-[#0c0c0c] select-none" style={{ height: 24 }}>
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-rose-400/70">RSI</span>
                            <span className="text-[9px] font-mono text-white/30">({rsiPeriod})</span>
                        </div>
                    </div>
                    <div ref={rsiChartRef} style={{ width: '100%', height: 146 }} />
                </div>
            )}

            {/* CCI Panel */}
            {showCCI && (
                <div className="flex-shrink-0 border-t border-white/5" style={{ height: 170 }}>
                    <div className="flex items-center justify-between px-3 bg-[#0c0c0c] select-none" style={{ height: 24 }}>
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-lime-400/70">CCI</span>
                            <span className="text-[9px] font-mono text-white/30">({cciPeriod})</span>
                        </div>
                    </div>
                    <div ref={cciChartRef} style={{ width: '100%', height: 146 }} />
                </div>
            )}

            {/* ADX Panel */}
            {showADX && (
                <div className="flex-shrink-0 border-t border-white/5" style={{ height: 170 }}>
                    <div className="flex items-center justify-between px-3 bg-[#0c0c0c] select-none" style={{ height: 24 }}>
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-black uppercase tracking-[0.15em] text-fuchsia-400/70">ADX</span>
                            <span className="text-[9px] font-mono text-white/30">({adxPeriod})</span>
                        </div>
                    </div>
                    <div ref={adxChartRef} style={{ width: '100%', height: 146 }} />
                </div>
            )}
        </>
    );
}
