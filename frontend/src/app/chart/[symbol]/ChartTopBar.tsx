import React from "react";
import { ArrowLeft, ZoomIn, ZoomOut, TrendingUp, TrendingDown, Crosshair } from "lucide-react";
import { formatAssetPrice, formatAssetPriceFixed } from "@/lib/marketFormatting";

export const TIMEFRAMES = [
    { label: "1m", value: "1m" },
    { label: "5m", value: "5m" },
    { label: "15m", value: "15m" },
    { label: "1H", value: "1h" },
    { label: "4H", value: "4h" },
    { label: "1D", value: "daily" },
    { label: "1W", value: "weekly" },
    { label: "1M", value: "monthly" },
];

interface ChartTopBarProps {
    router: any;
    symbol: string;
    timeframe: string;
    setTimeframe: (tf: string) => void;
    quote: { price: number; changePercentage: number } | null;
    loading: boolean;
    zoomIn: () => void;
    zoomOut: () => void;
    measureActive: boolean;
    setMeasureActive: (v: boolean) => void;
    clearMeasurement: () => void;
    // Trading Props
    holding: any;
    openTrade: any;
    closePosition: any;
    updatePositionLevels: any;
    tradeQty: number;
    setTradeQty: (n: number) => void;
    slPrice: string;
    setSlPrice: (s: string) => void;
    tpPrice: string;
    setTpPrice: (s: string) => void;
}

import { X } from "lucide-react";

export function ChartTopBar({
    router, symbol, timeframe, setTimeframe, quote, loading, zoomIn, zoomOut,
    measureActive, setMeasureActive, clearMeasurement,
    holding, openTrade, closePosition, updatePositionLevels,
    tradeQty, setTradeQty, slPrice, setSlPrice, tpPrice, setTpPrice
}: ChartTopBarProps) {
    return (
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
                        <span className="text-xl font-mono font-black text-white">${formatAssetPrice(quote.price, { symbol })}</span>
                        <div className={`flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[10px] font-black uppercase tracking-tighter ${(quote.changePercentage ?? 0) >= 0 ? "bg-green/10 text-green" : "bg-red/10 text-red"}`}>
                            {(quote.changePercentage ?? 0) >= 0 ? <TrendingUp size={12} /> : <TrendingDown size={12} />}
                            {(quote.changePercentage ?? 0).toFixed(2)}%
                        </div>
                    </div>
                )}
            </div>

            <div className="flex items-center gap-3">
                {/* ─── Integrated Trading Controls ─── */}
                <div className="flex items-center bg-white/5 rounded-lg border border-white/10 overflow-hidden mr-2">
                    {!holding ? (
                        <div className="flex items-center h-8">
                            <button
                                onClick={async () => {
                                    if (quote) {
                                        await openTrade(symbol, symbol, tradeQty, quote.price, 1.0, "Technology", "stock");
                                        setSlPrice(formatAssetPriceFixed(quote.price * 1.05, { symbol }));
                                        setTpPrice(formatAssetPriceFixed(quote.price * 0.95, { symbol }));
                                    }
                                }}
                                className="px-3 h-full bg-red-500/20 hover:bg-red-500 text-red-500 hover:text-white transition-all text-[10px] font-black border-r border-white/5"
                            >
                                SELL
                            </button>
                            <input
                                type="number"
                                value={tradeQty}
                                onChange={e => setTradeQty(Math.max(0.0001, Number(e.target.value) || 0.0001))}
                                className="w-12 bg-transparent text-center text-[11px] font-mono font-bold text-white outline-none"
                            />
                            <button
                                onClick={async () => {
                                    if (quote) {
                                        const p = quote.price * 1.0001;
                                        await openTrade(symbol, symbol, tradeQty, p, 1.0, "Technology", "stock");
                                        setSlPrice(formatAssetPriceFixed(p * 0.95, { symbol }));
                                        setTpPrice(formatAssetPriceFixed(p * 1.05, { symbol }));
                                    }
                                }}
                                className="px-3 h-full bg-blue-500/20 hover:bg-blue-600 text-blue-500 hover:text-white transition-all text-[10px] font-black border-l border-white/5"
                            >
                                BUY
                            </button>
                        </div>
                    ) : (
                        <div className="flex items-center h-8 gap-3 px-3">
                            <span className="text-[10px] font-mono font-black text-green whitespace-nowrap">
                                {holding.shares.toFixed(2)} <span className="opacity-40">U</span>
                            </span>
                            <div className="flex items-center gap-2">
                                <div className="flex items-center gap-1">
                                    <span className="text-[9px] font-black text-red-500/50">S</span>
                                    <input type="number" value={slPrice} onChange={e => setSlPrice(e.target.value)} onBlur={() => updatePositionLevels(symbol, parseFloat(slPrice), parseFloat(tpPrice))} className="w-16 bg-white/5 border border-white/5 rounded px-1 text-[11px] font-mono font-bold text-white outline-none focus:border-red-500/30" />
                                </div>
                                <div className="flex items-center gap-1">
                                    <span className="text-[9px] font-black text-green-500/50">T</span>
                                    <input type="number" value={tpPrice} onChange={e => setTpPrice(e.target.value)} onBlur={() => updatePositionLevels(symbol, parseFloat(slPrice), parseFloat(tpPrice))} className="w-16 bg-white/5 border border-white/5 rounded px-1 text-[11px] font-mono font-bold text-white outline-none focus:border-green-500/30" />
                                </div>
                            </div>
                            <button onClick={() => { if (confirm(`Close ${symbol}?`)) closePosition(symbol); }} className="hover:text-red-500 transition-colors">
                                <X size={14} />
                            </button>
                        </div>
                    )}
                </div>

                {loading && <span className="text-[10px] animate-pulse font-mono font-bold text-accent uppercase tracking-widest">Syncing...</span>}
                <div className="flex items-center gap-0.5 bg-white/5 rounded-lg border border-white/10 p-0.5">
                    <button onClick={zoomIn} className="h-7 w-7 flex items-center justify-center rounded-md hover:bg-white/10 text-white/50 hover:text-white transition-all" title="Zoom In">
                        <ZoomIn size={14} />
                    </button>
                    <button onClick={zoomOut} className="h-7 w-7 flex items-center justify-center rounded-md hover:bg-white/10 text-white/50 hover:text-white transition-all" title="Zoom Out">
                        <ZoomOut size={14} />
                    </button>
                    <div className="w-px h-4 bg-white/10" />
                    <button
                        onClick={() => {
                            if (measureActive) { clearMeasurement(); }
                            setMeasureActive(!measureActive);
                        }}
                        className={`h-7 w-7 flex items-center justify-center rounded-md transition-all ${measureActive
                                ? 'bg-amber-500/20 text-amber-400 ring-1 ring-amber-500/40'
                                : 'hover:bg-white/10 text-white/50 hover:text-white'
                            }`}
                        title={measureActive ? 'Disable Measure Tool (Esc)' : 'Measure Price Change'}
                    >
                        <Crosshair size={14} />
                    </button>
                </div>
                <div className="flex items-center gap-1.5 px-2.5 py-1 bg-white/5 rounded-md border border-white/5">
                    <div className="h-1.5 w-1.5 rounded-full bg-green animate-pulse" />
                    <span className="text-[9px] font-black text-green uppercase tracking-[0.2em]">Liquid</span>
                </div>
            </div>
        </div>
    );
}
