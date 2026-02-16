"use client"

import AppLayout from "@/components/layout/AppLayout";
import { useState } from "react";
import { ArrowUpRight, ArrowDownRight, Search, TrendingUp, CandlestickChart, Zap } from "lucide-react";

const MOCK_ORDERBOOK = {
    asks: [
        { price: 179.50, size: 120 },
        { price: 179.45, size: 340 },
        { price: 179.40, size: 200 },
        { price: 179.35, size: 580 },
        { price: 179.30, size: 150 },
    ],
    bids: [
        { price: 179.25, size: 420 },
        { price: 179.20, size: 680 },
        { price: 179.15, size: 310 },
        { price: 179.10, size: 190 },
        { price: 179.05, size: 550 },
    ]
};

const WATCHLIST = [
    { symbol: "AAPL", price: 178.72, change: 1.32 },
    { symbol: "MSFT", price: 415.60, change: -0.29 },
    { symbol: "NVDA", price: 875.28, change: 1.79 },
    { symbol: "GOOGL", price: 173.98, change: 1.84 },
    { symbol: "TSLA", price: 248.42, change: 2.12 },
    { symbol: "AMZN", price: 185.07, change: -0.50 },
    { symbol: "META", price: 582.15, change: 0.95 },
];

export default function TradingPage() {
    const [symbol, setSymbol] = useState("AAPL");
    const [quantity, setQuantity] = useState(1);
    const [orderType, setOrderType] = useState("market");
    const [limitPrice, setLimitPrice] = useState(178.72);
    const [side, setSide] = useState<"buy" | "sell">("buy");
    const [searchQuery, setSearchQuery] = useState("");

    const maxAskSize = Math.max(...MOCK_ORDERBOOK.asks.map(a => a.size));
    const maxBidSize = Math.max(...MOCK_ORDERBOOK.bids.map(b => b.size));

    const handleTrade = () => {
        alert(`${side.toUpperCase()} ${quantity} ${symbol} @ ${orderType === "market" ? "Market" : `$${limitPrice}`}`);
    };

    return (
        <AppLayout>
            <div className="p-6 lg:p-8 space-y-6 animate-fade-in">
                {/* Header */}
                <div className="flex items-center justify-between">
                    <div className="flex items-center gap-4">
                        <div className="h-10 w-10 rounded-xl bg-accent/10 flex items-center justify-center">
                            <CandlestickChart size={20} className="text-accent" />
                        </div>
                        <div>
                            <h1 className="text-2xl font-bold tracking-tight">{symbol}</h1>
                            <p className="text-sm text-muted">Trading Terminal</p>
                        </div>
                    </div>
                    <div className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-green/10 text-green text-xs font-semibold">
                        <Zap size={12} />
                        Low Latency · C++ Engine
                    </div>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
                    {/* Watchlist */}
                    <div className="lg:col-span-3 bg-card border border-border rounded-2xl overflow-hidden">
                        <div className="p-4 border-b border-border">
                            <div className="relative">
                                <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2 text-muted" />
                                <input
                                    value={searchQuery}
                                    onChange={(e) => setSearchQuery(e.target.value)}
                                    className="w-full bg-background border border-border rounded-xl pl-9 pr-3 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all placeholder:text-muted/50"
                                    placeholder="Search symbol..."
                                />
                            </div>
                        </div>
                        <div className="overflow-y-auto max-h-[500px]">
                            {WATCHLIST.filter(w => w.symbol.includes(searchQuery.toUpperCase())).map((w) => (
                                <button
                                    key={w.symbol}
                                    onClick={() => setSymbol(w.symbol)}
                                    className={`w-full flex items-center justify-between px-4 py-3.5 hover:bg-card-hover transition-colors border-b border-border/30 ${symbol === w.symbol ? "bg-accent/5 border-l-2 border-l-accent" : ""
                                        }`}
                                >
                                    <div className="flex items-center gap-3">
                                        <div className="h-8 w-8 rounded-lg bg-card-hover flex items-center justify-center text-xs font-bold text-muted">
                                            {w.symbol.slice(0, 2)}
                                        </div>
                                        <span className="font-semibold text-sm">{w.symbol}</span>
                                    </div>
                                    <div className="text-right">
                                        <p className="text-sm font-mono">${w.price.toFixed(2)}</p>
                                        <p className={`text-xs font-semibold flex items-center gap-0.5 justify-end ${w.change >= 0 ? "text-green" : "text-red"}`}>
                                            {w.change >= 0 ? <ArrowUpRight size={10} /> : <ArrowDownRight size={10} />}
                                            {w.change >= 0 ? "+" : ""}{w.change.toFixed(2)}%
                                        </p>
                                    </div>
                                </button>
                            ))}
                        </div>
                    </div>

                    {/* Chart Placeholder + Order Book */}
                    <div className="lg:col-span-5 space-y-6">
                        {/* Chart */}
                        <div className="bg-card border border-border rounded-2xl overflow-hidden">
                            <div className="px-6 py-4 border-b border-border flex items-center justify-between">
                                <div className="flex items-center gap-3">
                                    <h2 className="text-base font-semibold">{symbol}</h2>
                                    <span className="text-xs text-muted px-2 py-0.5 bg-card-hover rounded-md">1D</span>
                                </div>
                                <div className="flex gap-1">
                                    {["1m", "5m", "1H", "1D", "1W"].map(tf => (
                                        <button key={tf} className="text-[10px] px-2 py-1 rounded-md text-muted hover:text-foreground hover:bg-card-hover transition-all">
                                            {tf}
                                        </button>
                                    ))}
                                </div>
                            </div>
                            <div className="h-64 flex items-center justify-center text-muted text-sm relative overflow-hidden">
                                <div className="absolute inset-0 bg-gradient-to-t from-card to-transparent opacity-50" />
                                {/* Fake chart lines */}
                                <svg className="absolute inset-0 w-full h-full" preserveAspectRatio="none">
                                    <polyline
                                        fill="none"
                                        stroke="rgba(59,130,246,0.3)"
                                        strokeWidth="2"
                                        points="0,180 40,160 80,170 120,140 160,120 200,130 240,100 280,90 320,110 360,80 400,85 440,60 480,70 520,50 560,65 600,40 640,55 680,30 720,45 760,25"
                                    />
                                    <linearGradient id="chartGrad" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="0%" stopColor="rgba(59,130,246,0.15)" />
                                        <stop offset="100%" stopColor="rgba(59,130,246,0)" />
                                    </linearGradient>
                                    <polygon
                                        fill="url(#chartGrad)"
                                        points="0,180 40,160 80,170 120,140 160,120 200,130 240,100 280,90 320,110 360,80 400,85 440,60 480,70 520,50 560,65 600,40 640,55 680,30 720,45 760,25 760,256 0,256"
                                    />
                                </svg>
                                <span className="relative z-10 text-xs text-muted/60">TradingView integration ready</span>
                            </div>
                        </div>

                        {/* Order Book */}
                        <div className="bg-card border border-border rounded-2xl overflow-hidden">
                            <div className="px-6 py-3 border-b border-border">
                                <h3 className="text-sm font-semibold">Order Book</h3>
                            </div>
                            <div className="grid grid-cols-2 divide-x divide-border text-xs font-mono">
                                {/* Bids */}
                                <div className="p-3 space-y-0.5">
                                    <div className="flex justify-between text-muted text-[10px] pb-1 uppercase tracking-wider">
                                        <span>Price</span><span>Size</span>
                                    </div>
                                    {MOCK_ORDERBOOK.bids.map((b, i) => (
                                        <div key={i} className="flex justify-between py-1 relative">
                                            <div
                                                className="absolute right-0 top-0 bottom-0 bg-green/5"
                                                style={{ width: `${(b.size / maxBidSize) * 100}%` }}
                                            />
                                            <span className="text-green relative z-10">${b.price.toFixed(2)}</span>
                                            <span className="text-muted relative z-10">{b.size}</span>
                                        </div>
                                    ))}
                                </div>
                                {/* Asks */}
                                <div className="p-3 space-y-0.5">
                                    <div className="flex justify-between text-muted text-[10px] pb-1 uppercase tracking-wider">
                                        <span>Price</span><span>Size</span>
                                    </div>
                                    {MOCK_ORDERBOOK.asks.map((a, i) => (
                                        <div key={i} className="flex justify-between py-1 relative">
                                            <div
                                                className="absolute right-0 top-0 bottom-0 bg-red/5"
                                                style={{ width: `${(a.size / maxAskSize) * 100}%` }}
                                            />
                                            <span className="text-red relative z-10">${a.price.toFixed(2)}</span>
                                            <span className="text-muted relative z-10">{a.size}</span>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Order Form */}
                    <div className="lg:col-span-4 bg-card border border-border rounded-2xl p-6 space-y-5 h-fit">
                        <h2 className="text-base font-semibold">Place Order</h2>

                        {/* Buy/Sell Toggle */}
                        <div className="flex gap-1 bg-background rounded-xl p-1">
                            <button
                                onClick={() => setSide("buy")}
                                className={`flex-1 py-2.5 rounded-lg text-sm font-bold transition-all ${side === "buy"
                                        ? "bg-green text-white shadow-lg shadow-green/20"
                                        : "text-muted hover:text-foreground"
                                    }`}
                            >
                                Buy
                            </button>
                            <button
                                onClick={() => setSide("sell")}
                                className={`flex-1 py-2.5 rounded-lg text-sm font-bold transition-all ${side === "sell"
                                        ? "bg-red text-white shadow-lg shadow-red/20"
                                        : "text-muted hover:text-foreground"
                                    }`}
                            >
                                Sell
                            </button>
                        </div>

                        {/* Order Type */}
                        <div>
                            <label className="text-[10px] text-muted uppercase tracking-widest font-semibold block mb-2">Order Type</label>
                            <div className="flex gap-2">
                                {["market", "limit"].map(t => (
                                    <button
                                        key={t}
                                        onClick={() => setOrderType(t)}
                                        className={`flex-1 py-2 rounded-lg text-xs font-semibold capitalize transition-all border ${orderType === t
                                                ? "border-accent text-accent bg-accent/5"
                                                : "border-border text-muted hover:border-border-hover"
                                            }`}
                                    >
                                        {t}
                                    </button>
                                ))}
                            </div>
                        </div>

                        {/* Quantity */}
                        <div>
                            <label className="text-[10px] text-muted uppercase tracking-widest font-semibold block mb-2">Quantity</label>
                            <input
                                type="number"
                                value={quantity}
                                onChange={(e) => setQuantity(Number(e.target.value))}
                                className="w-full bg-background border border-border rounded-xl p-3 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all"
                            />
                            <div className="flex gap-2 mt-2">
                                {[1, 5, 10, 25, 50, 100].map(q => (
                                    <button
                                        key={q}
                                        onClick={() => setQuantity(q)}
                                        className="text-[10px] text-muted hover:text-foreground px-2 py-1 rounded-md bg-background hover:bg-card-hover transition-all border border-border/50"
                                    >
                                        {q}
                                    </button>
                                ))}
                            </div>
                        </div>

                        {/* Limit Price */}
                        {orderType === "limit" && (
                            <div className="animate-fade-in">
                                <label className="text-[10px] text-muted uppercase tracking-widest font-semibold block mb-2">Limit Price</label>
                                <input
                                    type="number"
                                    step="0.01"
                                    value={limitPrice}
                                    onChange={(e) => setLimitPrice(Number(e.target.value))}
                                    className="w-full bg-background border border-border rounded-xl p-3 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all"
                                />
                            </div>
                        )}

                        {/* Summary */}
                        <div className="bg-background rounded-xl p-4 space-y-2 border border-border/50">
                            <div className="flex justify-between text-xs">
                                <span className="text-muted">Estimated Total</span>
                                <span className="font-mono font-semibold">
                                    ${(quantity * (orderType === "limit" ? limitPrice : 178.72)).toLocaleString("en-US", { minimumFractionDigits: 2 })}
                                </span>
                            </div>
                            <div className="flex justify-between text-xs">
                                <span className="text-muted">Commission</span>
                                <span className="font-mono text-green">$0.00</span>
                            </div>
                        </div>

                        {/* Submit */}
                        <button
                            onClick={handleTrade}
                            className={`w-full py-3.5 rounded-xl font-bold text-sm transition-all shadow-lg ${side === "buy"
                                    ? "bg-green hover:bg-green/90 text-white shadow-green/20"
                                    : "bg-red hover:bg-red/90 text-white shadow-red/20"
                                }`}
                        >
                            {side === "buy" ? "Buy" : "Sell"} {symbol}
                        </button>
                    </div>
                </div>
            </div>
        </AppLayout>
    );
}
