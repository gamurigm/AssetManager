"use client"

import { useParams, useRouter } from "next/navigation";
import { useEffect, useRef, useState, useCallback } from "react";
import { X } from "lucide-react";
import { usePortfolio } from "@/context/PortfolioContext";

import { MAConfig } from "./chartMath";
import { ChartTopBar } from "./ChartTopBar";
import { ChartIndicatorsToolbar } from "./ChartIndicatorsToolbar";
import { ChartSubPanels } from "./ChartSubPanels";

// Custom Hooks
import { useChartState } from "./useChartState";
import { useChartData } from "./useChartData";
import { useMainChart } from "./useMainChart";
import { useVolumeProfile } from "./useVolumeProfile";
import { useTradingLines } from "./useTradingLines";
import { useMeasureTool } from "./useMeasureTool";

/* ─── Main Component ──────────────────────────────────────────────────── */

export default function ChartWindow() {
    const params = useParams();
    const router = useRouter();
    const symbol = typeof params.symbol === 'string' ? decodeURIComponent(params.symbol) : '';
    const { holdings, openTrade, closePosition, updatePositionLevels } = usePortfolio();
    const [tradeQty, setTradeQty] = useState(1);

    // Refs
    const mainChartRef = useRef<HTMLDivElement>(null);
    const mainChartApi = useRef<any>(null);
    const vpCanvasRef = useRef<HTMLCanvasElement>(null);
    const measureCanvasRef = useRef<HTMLCanvasElement>(null);
    const candleSeriesRef = useRef<any>(null);

    // Measure tool state
    const [measureActive, setMeasureActive] = useState(false);

    // SL/TP UI State
    const [slPrice, setSlPrice] = useState<string>('');
    const [tpPrice, setTpPrice] = useState<string>('');
    const slTpLoadedRef = useRef(false);

    // Color Theme
    const [theme, setTheme] = useState<'light' | 'dark'>('dark');
    useEffect(() => {
        const checkTheme = () => setTheme(document.documentElement.classList.contains('light') ? 'light' : 'dark');
        checkTheme();
        const obs = new MutationObserver(checkTheme);
        obs.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
        return () => obs.disconnect();
    }, []);
    const isLight = theme === 'light';

    // Timeframe
    const [timeframe, setTimeframe] = useState("daily");

    // ─── Custom Hooks ───────────────────────────────────────────────────
    const chartState = useChartState();
    const { loading, quote, rawData, chartOpts } = useChartData(symbol, timeframe, isLight);

    useMainChart(
        rawData, chartOpts, chartState.mas,
        chartState.showFib, chartState.fibLookback,
        chartState.showBB, chartState.bbPeriod, chartState.bbMult,
        chartState.showPSAR, chartState.psarStep, chartState.psarMax,
        chartState.showSupertrend, chartState.supertrendPeriod, chartState.supertrendMult,
        mainChartRef, mainChartApi, candleSeriesRef
    );

    useVolumeProfile(
        chartState.showVP, rawData, mainChartApi, candleSeriesRef, vpCanvasRef, mainChartRef
    );

    useTradingLines(
        symbol, holdings, quote,
        slPrice, setSlPrice, tpPrice, setTpPrice,
        mainChartApi, mainChartRef, candleSeriesRef,
        updatePositionLevels, closePosition
    );

    const { clearMeasurement } = useMeasureTool(
        measureActive,
        mainChartRef,
        mainChartApi,
        candleSeriesRef,
        measureCanvasRef
    );

    // Sync SL/TP from persisted backend on initial load
    const holding = holdings.find(h => h.symbol === symbol);
    useEffect(() => {
        if (holding && !slTpLoadedRef.current) {
            if (holding.sl != null && holding.sl > 0) setSlPrice(holding.sl.toFixed(4));
            if (holding.tp != null && holding.tp > 0) setTpPrice(holding.tp.toFixed(4));
            slTpLoadedRef.current = true;
        }
        if (!holding) slTpLoadedRef.current = false;
    }, [holding]);

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

    const updateMA = (id: string, updated: MAConfig) => chartState.setMas(prev => prev.map(m => m.id === id ? updated : m));
    const removeMA = (id: string) => chartState.setMas(prev => prev.filter(m => m.id !== id));
    const addMA = () => {
        const colors = ['#fbbf24', '#f472b6', '#38bdf8', '#a78bfa', '#34d399', '#fb923c'];
        chartState.setMas(prev => [...prev, {
            id: `ma${Date.now()}`, type: "EMA", period: 20,
            color: colors[prev.length % colors.length], visible: true
        }]);
    };

    const oscillatorPanelH = (chartState.showMACD ? 170 : 24) + (chartState.showStoch ? 170 : 24) + (chartState.showATR ? 170 : 24) + (chartState.showWilliams ? 170 : 0) + (chartState.showMFI ? 170 : 0) + (chartState.showCMF ? 170 : 0);
    const mainH = `calc(100vh - 48px - 38px - ${oscillatorPanelH}px)`;

    return (
        <div className="h-screen w-screen bg-[#0a0a0a] flex flex-col overflow-hidden" onClick={() => chartState.setIndicatorsOpen(false)}>

            <ChartTopBar
                router={router}
                symbol={symbol}
                timeframe={timeframe}
                setTimeframe={setTimeframe}
                quote={quote}
                loading={loading}
                zoomIn={zoomIn}
                zoomOut={zoomOut}
                holding={holding}
                openTrade={openTrade}
                closePosition={closePosition}
                updatePositionLevels={updatePositionLevels}
                tradeQty={tradeQty}
                setTradeQty={setTradeQty}
                slPrice={slPrice}
                setSlPrice={setSlPrice}
                tpPrice={tpPrice}
                setTpPrice={setTpPrice}
                measureActive={measureActive}
                setMeasureActive={setMeasureActive}
                clearMeasurement={clearMeasurement}
            />

            <ChartIndicatorsToolbar
                indicatorsOpen={chartState.indicatorsOpen}
                setIndicatorsOpen={chartState.setIndicatorsOpen}
                showVP={chartState.showVP}
                setShowVP={chartState.setShowVP}
                mas={chartState.mas}
                addMA={addMA}
                updateMA={updateMA}
                removeMA={removeMA}
                showMACD={chartState.showMACD}
                setShowMACD={chartState.setShowMACD}
                macdFast={chartState.macdFast}
                macdSlow={chartState.macdSlow}
                macdSignal={chartState.macdSignal}
                showStoch={chartState.showStoch}
                setShowStoch={chartState.setShowStoch}
                stochK={chartState.stochK}
                stochD={chartState.stochD}
                stochSmooth={chartState.stochSmooth}
                showFib={chartState.showFib}
                setShowFib={chartState.setShowFib}
                fibLookback={chartState.fibLookback}
                setFibLookback={chartState.setFibLookback}
                showBB={chartState.showBB}
                setShowBB={chartState.setShowBB}
                bbPeriod={chartState.bbPeriod}
                setBbPeriod={chartState.setBbPeriod}
                bbMult={chartState.bbMult}
                setBbMult={chartState.setBbMult}
                showATR={chartState.showATR}
                setShowATR={chartState.setShowATR}
                atrPeriod={chartState.atrPeriod}
                setAtrPeriod={chartState.setAtrPeriod}
                showPSAR={chartState.showPSAR}
                setShowPSAR={chartState.setShowPSAR}
                psarStep={chartState.psarStep}
                setPsarStep={chartState.setPsarStep}
                psarMax={chartState.psarMax}
                setPsarMax={chartState.setPsarMax}
                showSupertrend={chartState.showSupertrend}
                setShowSupertrend={chartState.setShowSupertrend}
                supertrendPeriod={chartState.supertrendPeriod}
                setSupertrendPeriod={chartState.setSupertrendPeriod}
                supertrendMult={chartState.supertrendMult}
                setSupertrendMult={chartState.setSupertrendMult}
                showWilliams={chartState.showWilliams}
                setShowWilliams={chartState.setShowWilliams}
                williamsPeriod={chartState.williamsPeriod}
                setWilliamsPeriod={chartState.setWilliamsPeriod}
                showMFI={chartState.showMFI}
                setShowMFI={chartState.setShowMFI}
                mfiPeriod={chartState.mfiPeriod}
                setMfiPeriod={chartState.setMfiPeriod}
                showCMF={chartState.showCMF}
                setShowCMF={chartState.setShowCMF}
                cmfPeriod={chartState.cmfPeriod}
                setCmfPeriod={chartState.setCmfPeriod}
                showRSI={chartState.showRSI}
                setShowRSI={chartState.setShowRSI}
                rsiPeriod={chartState.rsiPeriod}
                setRsiPeriod={chartState.setRsiPeriod}
                showCCI={chartState.showCCI}
                setShowCCI={chartState.setShowCCI}
                cciPeriod={chartState.cciPeriod}
                setCciPeriod={chartState.setCciPeriod}
                showADX={chartState.showADX}
                setShowADX={chartState.setShowADX}
                adxPeriod={chartState.adxPeriod}
                setAdxPeriod={chartState.setAdxPeriod}
            />


            {/* ─── Main Chart ─────────────────────────────────────────────── */}
            <div className={`w-full flex-1 relative ${measureActive ? 'cursor-crosshair' : ''}`} style={{ height: mainH }}>

                {loading && rawData.length === 0 && (
                    <div className="absolute inset-0 z-50 flex items-center justify-center bg-background/50 backdrop-blur-sm">
                        <div className="text-muted tracking-widest uppercase font-mono animate-pulse text-xs">Loading Market Data...</div>
                    </div>
                )}

                {!loading && rawData.length === 0 && (
                    <div className="absolute inset-0 z-50 flex items-center justify-center bg-background/80 backdrop-blur-md">
                        <div className="flex flex-col items-center">
                            <span className="text-red-400 font-bold text-lg mb-2">No Market Data</span>
                            <span className="text-muted text-xs">The symbol <span className="text-white font-mono">{symbol}</span> may be invalid, delisted, or missing data.</span>
                            <span className="text-muted text-[10px] mt-2">Try using Yahoo Finance format (e.g., EURUSD=X instead of EURUSD)</span>
                        </div>
                    </div>
                )}

                <div ref={mainChartRef} className="absolute inset-0" />
                {chartState.showVP && <canvas ref={vpCanvasRef} className="absolute inset-0 pointer-events-none z-10" />}
                <canvas ref={measureCanvasRef} className="absolute inset-0 pointer-events-none z-20" />
            </div>

            <ChartSubPanels
                rawData={rawData} chartOpts={chartOpts} mainChartApi={mainChartApi}
                showMACD={chartState.showMACD} setShowMACD={chartState.setShowMACD} macdFast={chartState.macdFast} setMacdFast={chartState.setMacdFast} macdSlow={chartState.macdSlow} setMacdSlow={chartState.setMacdSlow} macdSignal={chartState.macdSignal} setMacdSignal={chartState.setMacdSignal}
                showStoch={chartState.showStoch} setShowStoch={chartState.setShowStoch} stochK={chartState.stochK} setStochK={chartState.setStochK} stochD={chartState.stochD} setStochD={chartState.setStochD} stochSmooth={chartState.stochSmooth} setStochSmooth={chartState.setStochSmooth}
                showATR={chartState.showATR} setShowATR={chartState.setShowATR} atrPeriod={chartState.atrPeriod} setAtrPeriod={chartState.setAtrPeriod}
                showWilliams={chartState.showWilliams} williamsPeriod={chartState.williamsPeriod}
                showMFI={chartState.showMFI} mfiPeriod={chartState.mfiPeriod}
                showCMF={chartState.showCMF} cmfPeriod={chartState.cmfPeriod}
                showRSI={chartState.showRSI} rsiPeriod={chartState.rsiPeriod}
                showCCI={chartState.showCCI} cciPeriod={chartState.cciPeriod}
                showADX={chartState.showADX} adxPeriod={chartState.adxPeriod}
            />
        </div>
    );
}
