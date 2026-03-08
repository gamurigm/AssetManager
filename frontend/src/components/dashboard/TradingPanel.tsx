"use client";

import React, { useState, useEffect } from "react";
import {
    Zap, ShoppingCart, ArrowUpRight, ArrowDownRight,
    Link, Link2Off, RefreshCw, Layers, ShieldCheck,
    AlertCircle, CheckCircle2, ChevronRight, Hash, Activity
} from "lucide-react";

interface IBKRStatus {
    connected: boolean;
    host: string;
    configured_port: number;
    active_port: number | null;
    last_connection_error: string | null;
}

export default function TradingPanel() {
    const [symbol, setSymbol] = useState("");
    const [quantity, setQuantity] = useState<number>(1);
    const [side, setSide] = useState<"BUY" | "SELL">("BUY");
    const [loading, setLoading] = useState(false);
    const [status, setStatus] = useState<IBKRStatus | null>(null);
    const [result, setResult] = useState<any>(null);
    const [error, setError] = useState<string | null>(null);

    const fetchStatus = async () => {
        try {
            // Using localhost instead of 127.0.0.1 for browser compatibility
            const res = await fetch("http://localhost:8282/api/v1/trading/status/ibkr");
            if (res.ok) {
                const data = await res.json();
                setStatus(data);
            }
        } catch (e) {
            console.error("Failed to fetch IBKR status from localhost:8282", e);
            // Fallback attempt to 127.0.0.1 if localhost fails
            try {
                const res = await fetch("http://127.0.0.1:8282/api/v1/trading/status/ibkr");
                if (res.ok) setStatus(await res.json());
            } catch (p) {
                // Both failed, suppressed to avoid console noise on offline backend
            }
        }
    };

    useEffect(() => {
        fetchStatus();
        const interval = setInterval(fetchStatus, 5000);
        return () => clearInterval(interval);
    }, []);

    const handlePlaceOrder = async () => {
        if (!symbol) {
            setError("Symbol is required");
            return;
        }
        if (quantity <= 0) {
            setError("Quantity must be greater than 0");
            return;
        }

        setLoading(true);
        setError(null);
        setResult(null);

        try {
            const res = await fetch("http://localhost:8282/api/v1/trading/order/ibkr", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    symbol: symbol.toUpperCase(),
                    quantity,
                    side: side.toUpperCase(),
                    portfolio_id: "main"
                })
            });

            const data = await res.json();
            if (res.ok) {
                setResult(data);
                setSymbol(""); // Reset on success
            } else {
                setError(data.detail || "Order failed");
            }
        } catch (e) {
            setError("Network error or backend unreachable");
        } finally {
            setLoading(false);
        }
    };

    const handleConnect = async () => {
        setLoading(true);
        try {
            const res = await fetch("http://localhost:8282/api/v1/trading/connect/ibkr", { method: "POST" });
            if (res.ok) {
                const data = await res.json();
                setStatus(data);
            }
        } catch (e) {
            console.error("Failed to trigger IBKR connection", e);
        } finally {
            setLoading(false);
        }
    };

    const isConnected = status?.connected ?? false;

    return (
        <div className="flex-1 overflow-hidden flex flex-col">
            {/* Header */}
            <div className="px-6 py-4 border-b border-border/15 flex items-center justify-between bg-card/40 dark:bg-white/3">
                <div className="flex items-center gap-3">
                    <div className={`h-8 w-8 rounded-lg flex items-center justify-center border ${isConnected ? 'bg-emerald-500/10 border-emerald-500/20 text-emerald-400' : 'bg-red/10 border-red/20 text-red'}`}>
                        {isConnected ? <Zap size={16} /> : <Link2Off size={16} />}
                    </div>
                    <div>
                        <h3 className="text-xs font-black uppercase tracking-widest text-foreground leading-none">Order Terminal</h3>
                        <p className={`text-[9px] font-bold mt-1 uppercase tracking-tighter ${isConnected ? 'text-emerald-500/70' : 'text-red/70'}`}>
                            {isConnected ? `IBKR Connected @ ${status?.active_port}` : "Offline — TWS Link Inactive"}
                        </p>
                    </div>
                </div>
                <div className="flex items-center gap-2">
                    {!isConnected && (
                        <button
                            onClick={handleConnect}
                            disabled={loading}
                            className="px-3 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-[9px] font-black uppercase tracking-tighter hover:bg-emerald-500/20 transition-all flex items-center gap-2"
                        >
                            <Link size={10} />
                            Try Connect
                        </button>
                    )}
                    <button
                        onClick={fetchStatus}
                        className="h-8 w-8 rounded-lg bg-card-hover/40 border border-border/20 flex items-center justify-center text-muted hover:text-foreground transition-all active:rotate-180"
                    >
                        <RefreshCw size={14} className={loading ? "animate-spin" : ""} />
                    </button>
                </div>
            </div>

            <div className="flex-1 overflow-y-auto p-6 space-y-8 no-scrollbar">
                {/* Integration Status Card */}
                {!isConnected && (
                    <div className="p-4 rounded-2xl bg-red/5 border border-red/20 flex gap-4 animate-in fade-in slide-in-from-top-2 duration-300">
                        <div className="shrink-0 h-10 w-10 rounded-xl bg-red/10 border border-red/20 flex items-center justify-center text-red">
                            <Link2Off size={20} />
                        </div>
                        <div>
                            <h4 className="text-xs font-black text-red uppercase tracking-wider">Gateway Offline</h4>
                            <p className="text-[10px] text-muted font-bold mt-1 leading-relaxed">
                                Ensure Interactive Brokers **TWS** or **IB Gateway** is running on your machine and **API Access** is enabled in settings.
                            </p>
                            {status?.last_connection_error && (
                                <p className="text-[9px] font-mono text-muted/60 bg-black/20 p-2 mt-2 rounded border border-white/5 break-all">
                                    {status.last_connection_error}
                                </p>
                            )}
                        </div>
                    </div>
                )}

                {/* Main Order Form */}
                <div className={`space-y-6 transition-opacity duration-300 ${!isConnected ? 'opacity-50 pointer-events-none' : 'opacity-100'}`}>
                    {/* Side Switcher */}
                    <div className="flex p-1 bg-background/50 border border-border/40 rounded-2xl">
                        <button
                            onClick={() => setSide("BUY")}
                            className={`flex-1 py-3 rounded-xl text-xs font-black uppercase tracking-widest transition-all flex items-center justify-center gap-2 ${side === "BUY" ? 'bg-emerald-500 text-black shadow-lg shadow-emerald-500/20' : 'text-muted hover:text-foreground'}`}
                        >
                            <ArrowUpRight size={14} strokeWidth={3} />
                            Buy Order
                        </button>
                        <button
                            onClick={() => setSide("SELL")}
                            className={`flex-1 py-3 rounded-xl text-xs font-black uppercase tracking-widest transition-all flex items-center justify-center gap-2 ${side === "SELL" ? 'bg-red text-white shadow-lg shadow-red/20' : 'text-muted hover:text-foreground'}`}
                        >
                            <ArrowDownRight size={14} strokeWidth={3} />
                            Sell Order
                        </button>
                    </div>

                    <div className="space-y-4">
                        {/* Symbol Input */}
                        <div className="space-y-2">
                            <label className="text-[10px] font-black uppercase tracking-widest text-muted flex items-center gap-2">
                                <Layers size={12} className="text-accent" /> Asset Symbol
                            </label>
                            <div className="relative group">
                                <input
                                    type="text"
                                    value={symbol}
                                    onChange={(e) => setSymbol(e.target.value.toUpperCase())}
                                    placeholder="e.g. AAPL, TSLA, GC=F"
                                    className="w-full bg-background border border-border/40 focus:border-accent group-hover:border-border p-4 rounded-2xl text-sm font-black uppercase tracking-widest outline-none transition-all placeholder:text-[10px] placeholder:font-bold placeholder:opacity-30"
                                />
                            </div>
                        </div>

                        {/* Quantity / Logic Row */}
                        <div className="grid grid-cols-2 gap-4">
                            <div className="space-y-2">
                                <label className="text-[10px] font-black uppercase tracking-widest text-muted flex items-center gap-2">
                                    <Hash size={12} className="text-purple-400" /> Quantity
                                </label>
                                <input
                                    type="number"
                                    step="0.01"
                                    value={quantity}
                                    onChange={(e) => setQuantity(Number(e.target.value))}
                                    className="w-full bg-background border border-border/40 focus:border-purple-400 p-4 rounded-2xl text-sm font-mono font-black outline-none transition-all"
                                />
                            </div>
                            <div className="space-y-2">
                                <label className="text-[10px] font-black uppercase tracking-widest text-muted flex items-center gap-2">
                                    <ShieldCheck size={12} className="text-emerald-400" /> Order Type
                                </label>
                                <div className="w-full bg-black/20 border border-white/5 p-4 rounded-2xl text-[10px] font-black uppercase tracking-widest text-muted/60 flex items-center justify-center">
                                    Market (LMT N/A)
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Execution Button */}
                    <button
                        disabled={loading || !isConnected}
                        onClick={handlePlaceOrder}
                        className={`w-full py-5 rounded-2xl text-xs font-black uppercase tracking-[0.3em] transition-all flex items-center justify-center gap-4 active:scale-[0.98] shadow-2xl relative overflow-hidden group
                            ${side === "BUY"
                                ? 'bg-emerald-500 text-black shadow-emerald-500/20 hover:bg-emerald-400 disabled:bg-emerald-900/50'
                                : 'bg-red text-white shadow-red/20 hover:bg-red/90 disabled:bg-red-900/50'
                            }`}
                    >
                        {loading ? (
                            <RefreshCw size={18} className="animate-spin" />
                        ) : (
                            <>
                                <Zap size={18} fill="currentColor" />
                                {side === "BUY" ? "Transmit Market Buy" : "Transmit Market Sell"}
                                <ChevronRight size={16} className="group-hover:translate-x-1 transition-transform" />
                            </>
                        )}
                    </button>
                    <p className="text-[9px] text-center text-muted/40 font-bold uppercase tracking-widest">
                        Orders are transmitted via SmartRouting℠ to IBKR
                    </p>
                </div>

                {/* Feedback Area */}
                <div className="space-y-4 pt-4 border-t border-border/10">
                    {error && (
                        <div className="p-4 rounded-2xl bg-red/10 border border-red/20 flex items-start gap-4 animate-in zoom-in-95 duration-200">
                            <AlertCircle size={18} className="text-red shrink-0 mt-0.5" />
                            <div className="text-[10px] font-bold text-red break-words leading-relaxed">{error}</div>
                        </div>
                    )}

                    {result && (
                        <div className="p-4 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 flex items-start gap-4 animate-in zoom-in-95 duration-200">
                            <CheckCircle2 size={18} className="text-emerald-400 shrink-0 mt-0.5" />
                            <div className="space-y-2 flex-1">
                                <h5 className="text-[10px] font-black text-emerald-400 uppercase tracking-widest">Execution Confirmed</h5>
                                <div className="grid grid-cols-2 gap-y-2 text-[9px] font-mono">
                                    <span className="text-muted uppercase">Status:</span>
                                    <span className="text-foreground text-right font-black uppercase">{result.ibkr_result.status}</span>
                                    <span className="text-muted uppercase">Fill Avg:</span>
                                    <span className="text-emerald-400 text-right font-black">${result.recorded_price.toFixed(4)}</span>
                                    <span className="text-muted uppercase">ID:</span>
                                    <span className="text-foreground text-right">{result.ibkr_result.orderId}</span>
                                </div>
                            </div>
                        </div>
                    )}

                    {!error && !result && isConnected && (
                        <div className="p-6 rounded-2xl border border-dashed border-border/20 flex flex-col items-center justify-center text-center opacity-40">
                            <div className="h-12 w-12 rounded-full bg-muted/5 flex items-center justify-center mb-3">
                                <Activity size={20} className="text-muted" />
                            </div>
                            <p className="text-[9px] font-black uppercase tracking-widest text-muted">Ready for Transmission</p>
                        </div>
                    )}
                </div>
            </div>

            {/* Footer / Risk Warning */}
            <div className="p-6 bg-card/20 border-t border-border/10">
                <div className="flex items-center gap-3 text-amber-500/50 mb-2">
                    <AlertCircle size={14} />
                    <span className="text-[9px] font-black uppercase tracking-widest">Execution Disclosure</span>
                </div>
                <p className="text-[8px] text-muted/40 font-bold leading-relaxed uppercase tracking-tighter">
                    Trading financial instruments involves significant risk. This terminal uses Market Orders which execute at the next available price. High volatility can cause significant slippage. Use with caution in low-liquidity environments.
                </p>
            </div>
        </div>
    );
}
