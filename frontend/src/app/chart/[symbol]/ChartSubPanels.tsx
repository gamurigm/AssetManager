import React, { useEffect, useRef } from "react";
import { createChart, IChartApi, HistogramSeries, LineSeries } from "lightweight-charts";
import { Plus, Minus } from "lucide-react";
import { ParamInput } from "./ChartUIComponents";
import { calcMACD, calcStochastic, calcATR, calcWilliamsR, calcMFI, calcCMF } from "./chartMath";

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
    showMFI: boolean;
    showCMF: boolean;
}

export function ChartSubPanels({
    rawData, chartOpts, mainChartApi,
    showMACD, setShowMACD, macdFast, setMacdFast, macdSlow, setMacdSlow, macdSignal, setMacdSignal,
    showStoch, setShowStoch, stochK, setStochK, stochD, setStochD, stochSmooth, setStochSmooth,
    showATR, setShowATR, atrPeriod, setAtrPeriod,
    showWilliams, showMFI, showCMF
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

    // MACD
    useEffect(() => {
        if (!macdChartRef.current || rawData.length === 0 || !showMACD) return;
        if (macdChartApi.current) { setTimeout(() => { try { macdChartApi.current?.remove(); } catch(e){} }, 10); macdChartApi.current = null; }

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

        chart.timeScale().fitContent();

        if (mainChartApi.current) {
            const r = mainChartApi.current.timeScale().getVisibleLogicalRange();
            if (r) chart.timeScale().setVisibleLogicalRange(r);

            const mainTimeScale = mainChartApi.current.timeScale();
            const subTimeScale = chart.timeScale();

            const handleMainChange = (range: any) => { if (range) subTimeScale.setVisibleLogicalRange(range); };
            const handleSubChange = (range: any) => { if (range && mainChartApi.current) mainChartApi.current.timeScale().setVisibleLogicalRange(range); };

            mainTimeScale.subscribeVisibleLogicalRangeChange(handleMainChange);
            subTimeScale.subscribeVisibleLogicalRangeChange(handleSubChange);

            const hr = () => { if (macdChartRef.current) chart.applyOptions({ width: macdChartRef.current.clientWidth }); };
            window.addEventListener('resize', hr);

            return () => {
                mainTimeScale.unsubscribeVisibleLogicalRangeChange(handleMainChange);
                subTimeScale.unsubscribeVisibleLogicalRangeChange(handleSubChange);
                window.removeEventListener('resize', hr);
                setTimeout(() => { try { chart.remove(); } catch(e){} }, 10);
                macdChartApi.current = null;
            };
        }
        return () => { setTimeout(() => { try { chart.remove(); } catch(e){} }, 10); macdChartApi.current = null; };
    }, [rawData, showMACD, macdFast, macdSlow, macdSignal, chartOpts]);

    // Stochastic
    useEffect(() => {
        if (!stochChartRef.current || rawData.length === 0 || !showStoch) return;
        if (stochChartApi.current) { setTimeout(() => { try { stochChartApi.current?.remove(); } catch(e){} }, 10); stochChartApi.current = null; }

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

        chart.timeScale().fitContent();

        if (mainChartApi.current) {
            const r = mainChartApi.current.timeScale().getVisibleLogicalRange();
            if (r) chart.timeScale().setVisibleLogicalRange(r);

            const mainTimeScale = mainChartApi.current.timeScale();
            const subTimeScale = chart.timeScale();
            const handleMainChange = (range: any) => { if (range) subTimeScale.setVisibleLogicalRange(range); };
            const handleSubChange = (range: any) => { if (range && mainChartApi.current) mainChartApi.current.timeScale().setVisibleLogicalRange(range); };

            mainTimeScale.subscribeVisibleLogicalRangeChange(handleMainChange);
            subTimeScale.subscribeVisibleLogicalRangeChange(handleSubChange);

            const hr = () => { if (stochChartRef.current) chart.applyOptions({ width: stochChartRef.current.clientWidth }); };
            window.addEventListener('resize', hr);

            return () => {
                mainTimeScale.unsubscribeVisibleLogicalRangeChange(handleMainChange);
                subTimeScale.unsubscribeVisibleLogicalRangeChange(handleSubChange);
                window.removeEventListener('resize', hr);
                setTimeout(() => { try { chart.remove(); } catch(e){} }, 10);
                stochChartApi.current = null;
            };
        }
        return () => { setTimeout(() => { try { chart.remove(); } catch(e){} }, 10); stochChartApi.current = null; };
    }, [rawData, showStoch, stochK, stochD, stochSmooth, chartOpts]);

    // ATR
    useEffect(() => {
        if (!atrChartRef.current || rawData.length === 0 || !showATR) return;
        if (atrChartApi.current) { setTimeout(() => { try { atrChartApi.current?.remove(); } catch(e){} }, 10); atrChartApi.current = null; }

        const chart = createChart(atrChartRef.current, { ...chartOpts(146), width: atrChartRef.current.clientWidth });
        atrChartApi.current = chart;

        const highs = rawData.map(d => d.high);
        const lows = rawData.map(d => d.low);
        const closes = rawData.map(d => d.close);
        const times = rawData.map(d => d.time as any);
        const atrValues = calcATR(highs, lows, closes, atrPeriod);

        const atrSeries = chart.addSeries(LineSeries, { color: '#e040fb', lineWidth: 2, priceLineVisible: false, lastValueVisible: true, title: 'ATR' });
        atrSeries.setData(atrValues.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);

        chart.timeScale().fitContent();

        if (mainChartApi.current) {
            const r = mainChartApi.current.timeScale().getVisibleLogicalRange();
            if (r) chart.timeScale().setVisibleLogicalRange(r);

            const mainTimeScale = mainChartApi.current.timeScale();
            const subTimeScale = chart.timeScale();
            const handleMainChange = (range: any) => { if (range) subTimeScale.setVisibleLogicalRange(range); };
            const handleSubChange = (range: any) => { if (range && mainChartApi.current) mainChartApi.current.timeScale().setVisibleLogicalRange(range); };

            mainTimeScale.subscribeVisibleLogicalRangeChange(handleMainChange);
            subTimeScale.subscribeVisibleLogicalRangeChange(handleSubChange);

            const hr = () => { if (atrChartRef.current) chart.applyOptions({ width: atrChartRef.current.clientWidth }); };
            window.addEventListener('resize', hr);

            return () => {
                mainTimeScale.unsubscribeVisibleLogicalRangeChange(handleMainChange);
                subTimeScale.unsubscribeVisibleLogicalRangeChange(handleSubChange);
                window.removeEventListener('resize', hr);
                setTimeout(() => { try { chart.remove(); } catch(e){} }, 10);
                atrChartApi.current = null;
            };
        }
        return () => { setTimeout(() => { try { chart.remove(); } catch(e){} }, 10); atrChartApi.current = null; };
    }, [rawData, showATR, atrPeriod, chartOpts]);

    // Williams %R
    useEffect(() => {
        if (!williamsChartRef.current || rawData.length === 0 || !showWilliams) return;
        if (williamsChartApi.current) { setTimeout(() => { try { williamsChartApi.current?.remove(); } catch(e){} }, 10); williamsChartApi.current = null; }
        const chart = createChart(williamsChartRef.current, { ...chartOpts(146), width: williamsChartRef.current.clientWidth });
        williamsChartApi.current = chart;
        const highs = rawData.map(d => d.high), lows = rawData.map(d => d.low), closes = rawData.map(d => d.close), times = rawData.map(d => d.time as any);
        const w = calcWilliamsR(highs, lows, closes, 14);

        chart.addSeries(LineSeries, { color: '#0ea5e9', lineWidth: 2, priceLineVisible: false, lastValueVisible: true, title: 'Williams %R' })
            .setData(w.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);

        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: -20 })));
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: -80 })));

        chart.timeScale().fitContent();
        if (mainChartApi.current) {
            const r = mainChartApi.current.timeScale().getVisibleLogicalRange();
            if (r) chart.timeScale().setVisibleLogicalRange(r);

            const mainTimeScale = mainChartApi.current.timeScale();
            const subTimeScale = chart.timeScale();
            const handleMainChange = (range: any) => { if (range) subTimeScale.setVisibleLogicalRange(range); };
            const handleSubChange = (range: any) => { if (range && mainChartApi.current) mainChartApi.current.timeScale().setVisibleLogicalRange(range); };

            mainTimeScale.subscribeVisibleLogicalRangeChange(handleMainChange);
            subTimeScale.subscribeVisibleLogicalRangeChange(handleSubChange);

            const hr = () => { if (williamsChartRef.current) chart.applyOptions({ width: williamsChartRef.current.clientWidth }); };
            window.addEventListener('resize', hr);

            return () => {
                mainTimeScale.unsubscribeVisibleLogicalRangeChange(handleMainChange);
                subTimeScale.unsubscribeVisibleLogicalRangeChange(handleSubChange);
                window.removeEventListener('resize', hr);
                setTimeout(() => { try { chart.remove(); } catch(e){} }, 10);
                williamsChartApi.current = null;
            };
        }
        return () => { setTimeout(() => { try { chart.remove(); } catch(e){} }, 10); williamsChartApi.current = null; };
    }, [rawData, showWilliams, chartOpts]);

    // MFI
    useEffect(() => {
        if (!mfiChartRef.current || rawData.length === 0 || !showMFI) return;
        if (mfiChartApi.current) { setTimeout(() => { try { mfiChartApi.current?.remove(); } catch(e){} }, 10); mfiChartApi.current = null; }
        const chart = createChart(mfiChartRef.current, { ...chartOpts(146), width: mfiChartRef.current.clientWidth });
        mfiChartApi.current = chart;
        const highs = rawData.map(d => d.high), lows = rawData.map(d => d.low), closes = rawData.map(d => d.close), volumes = rawData.map(d => d.volume ?? 0), times = rawData.map(d => d.time as any);
        const mfi = calcMFI(highs, lows, closes, volumes, 14);

        chart.addSeries(LineSeries, { color: '#a855f7', lineWidth: 2, priceLineVisible: false, lastValueVisible: true, title: 'MFI' })
            .setData(mfi.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v }) as any);

        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 80 })));
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 20 })));

        chart.timeScale().fitContent();
        if (mainChartApi.current) {
            const r = mainChartApi.current.timeScale().getVisibleLogicalRange();
            if (r) chart.timeScale().setVisibleLogicalRange(r);

            const mainTimeScale = mainChartApi.current.timeScale();
            const subTimeScale = chart.timeScale();
            const handleMainChange = (range: any) => { if (range) subTimeScale.setVisibleLogicalRange(range); };
            const handleSubChange = (range: any) => { if (range && mainChartApi.current) mainChartApi.current.timeScale().setVisibleLogicalRange(range); };

            mainTimeScale.subscribeVisibleLogicalRangeChange(handleMainChange);
            subTimeScale.subscribeVisibleLogicalRangeChange(handleSubChange);

            const hr = () => { if (mfiChartRef.current) chart.applyOptions({ width: mfiChartRef.current.clientWidth }); };
            window.addEventListener('resize', hr);

            return () => {
                mainTimeScale.unsubscribeVisibleLogicalRangeChange(handleMainChange);
                subTimeScale.unsubscribeVisibleLogicalRangeChange(handleSubChange);
                window.removeEventListener('resize', hr);
                setTimeout(() => { try { chart.remove(); } catch(e){} }, 10);
                mfiChartApi.current = null;
            };
        }
        return () => { setTimeout(() => { try { chart.remove(); } catch(e){} }, 10); mfiChartApi.current = null; };
    }, [rawData, showMFI, chartOpts]);

    // CMF
    useEffect(() => {
        if (!cmfChartRef.current || rawData.length === 0 || !showCMF) return;
        if (cmfChartApi.current) { setTimeout(() => { try { cmfChartApi.current?.remove(); } catch(e){} }, 10); cmfChartApi.current = null; }
        const chart = createChart(cmfChartRef.current, { ...chartOpts(146), width: cmfChartRef.current.clientWidth });
        cmfChartApi.current = chart;
        const highs = rawData.map(d => d.high), lows = rawData.map(d => d.low), closes = rawData.map(d => d.close), volumes = rawData.map(d => d.volume), times = rawData.map(d => d.time as any);
        const cmf = calcCMF(highs, lows, closes, volumes, 20);

        const cmfSeries = chart.addSeries(HistogramSeries, { priceLineVisible: false, lastValueVisible: true });
        cmfSeries.setData(cmf.map((v, i) => v === null || isNaN(v) ? { time: times[i] } : { time: times[i], value: v, color: v > 0 ? 'rgba(38,166,157,0.7)' : 'rgba(239,83,80,0.7)' }) as any);

        // Add 0-line for CMF
        chart.addSeries(LineSeries, { color: '#71717a60', lineWidth: 1, lineStyle: 2, priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false })
            .setData(times.map(t => ({ time: t, value: 0 })));

        if (mainChartApi.current) {
            const r = mainChartApi.current.timeScale().getVisibleLogicalRange();
            if (r) chart.timeScale().setVisibleLogicalRange(r);

            const mainTimeScale = mainChartApi.current.timeScale();
            const subTimeScale = chart.timeScale();
            const handleMainChange = (range: any) => { if (range) subTimeScale.setVisibleLogicalRange(range); };
            const handleSubChange = (range: any) => { if (range && mainChartApi.current) mainChartApi.current.timeScale().setVisibleLogicalRange(range); };

            mainTimeScale.subscribeVisibleLogicalRangeChange(handleMainChange);
            subTimeScale.subscribeVisibleLogicalRangeChange(handleSubChange);

            const hr = () => { if (cmfChartRef.current) chart.applyOptions({ width: cmfChartRef.current.clientWidth }); };
            window.addEventListener('resize', hr);

            return () => {
                mainTimeScale.unsubscribeVisibleLogicalRangeChange(handleMainChange);
                subTimeScale.unsubscribeVisibleLogicalRangeChange(handleSubChange);
                window.removeEventListener('resize', hr);
                setTimeout(() => { try { chart.remove(); } catch(e){} }, 10);
                cmfChartApi.current = null;
            };
        }
        return () => { setTimeout(() => { try { chart.remove(); } catch(e){} }, 10); cmfChartApi.current = null; };
    }, [rawData, showCMF, chartOpts]);

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
        </>
    );
}
