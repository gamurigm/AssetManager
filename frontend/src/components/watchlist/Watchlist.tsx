"use client"

import { useState, useEffect } from "react";
import { Star, Plus, X, ExternalLink, TrendingUp, TrendingDown } from "lucide-react";

declare global {
    interface Window {
        electronAPI: {
            openChart: (symbol: string) => void;
        };
    }
}

interface WatchlistItem {
    symbol: string;
    price: number;
    changePercent: number;
}

export default function Watchlist() {
    const [items, setItems] = useState<WatchlistItem[]>([]);
    const [newSymbol, setNewSymbol] = useState("");
    const [loading, setLoading] = useState(false);

    // Note: In a real app, we'd fetch this from the /watchlist API
    // Using a local default for the demo
    const [symbols, setSymbols] = useState(["AAPL", "BTC/USD", "NVDA", "ETH/USD"]);

    useEffect(() => {
        const fetchWatchlistData = async () => {
            const data = await Promise.all(
                symbols.map(async (s) => {
                    try {
                        const res = await fetch(`http://localhost:8000/api/v1/market/quote/${encodeURIComponent(s)}`);
                        const d = await res.json();
                        return {
                            symbol: s,
                            price: d.price || 0,
                            changePercent: d.changePercentage || 0,
                        };
                    } catch (e) {
                        return { symbol: s, price: 0, changePercent: 0 };
                    }
                })
            );
            setItems(data);
        };

        fetchWatchlistData();
        const timer = setInterval(fetchWatchlistData, 30000);
        return () => clearInterval(timer);
    }, [symbols]);

    const addSymbol = () => {
        if (newSymbol && !symbols.includes(newSymbol.toUpperCase())) {
            setSymbols([...symbols, newSymbol.toUpperCase()]);
            setNewSymbol("");
        }
    };

    const removeSymbol = (s: string) => {
        setSymbols(symbols.filter(item => item !== s));
    };

    const openChart = (symbol: string) => {
        // Call the Electron API exposed via preload.js
        if (window.electronAPI) {
            window.electronAPI.openChart(symbol);
        } else {
            // Fallback for browser (regular popup or just log)
            console.log(`Open chart for ${symbol}`);
            window.open(`/chart/${symbol}`, '_blank', 'width=800,height=600');
        }
    };

    return (
        <div className="bg-card border border-border rounded-2xl overflow-hidden shadow-sm flex flex-col h-full">
            <div className="px-5 py-4 border-b border-border flex items-center justify-between bg-card-hover/20">
                <div className="flex items-center gap-2">
                    <Star size={16} className="text-yellow-400 fill-yellow-400" />
                    <h2 className="text-sm font-bold uppercase tracking-wider">Watchlist</h2>
                </div>
                <div className="flex items-center gap-2">
                    <input
                        type="text"
                        value={newSymbol}
                        onChange={(e) => setNewSymbol(e.target.value)}
                        onKeyDown={(e) => e.key === 'Enter' && addSymbol()}
                        placeholder="Add ticker..."
                        className="bg-background border border-border rounded-lg px-2 py-1 text-xs w-24 focus:outline-none focus:ring-1 focus:ring-accent"
                    />
                    <button onClick={addSymbol} className="p-1 hover:bg-accent/10 rounded-md text-accent transition-colors">
                        <Plus size={16} />
                    </button>
                </div>
            </div>

            <div className="flex-1 overflow-y-auto p-2 space-y-1">
                {items.map((item) => (
                    <div
                        key={item.symbol}
                        className="group flex items-center justify-between p-3 rounded-xl hover:bg-card-hover transition-all border border-transparent hover:border-border/50"
                    >
                        <div className="flex items-center gap-3">
                            <div onClick={() => openChart(item.symbol)} className="cursor-pointer">
                                <p className="text-sm font-bold group-hover:text-accent transition-colors">{item.symbol}</p>
                                <div className="flex items-center gap-1">
                                    <span className={`text-[10px] font-bold ${item.changePercent >= 0 ? 'text-green' : 'text-red'}`}>
                                        {item.changePercent >= 0 ? '+' : ''}{item.changePercent.toFixed(2)}%
                                    </span>
                                </div>
                            </div>
                        </div>

                        <div className="flex items-center gap-3">
                            <p className="text-xs font-mono font-semibold">${item.price.toFixed(item.symbol.includes('/') ? 2 : 2)}</p>
                            <div className="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                                <button
                                    onClick={() => openChart(item.symbol)}
                                    className="p-1 text-muted hover:text-accent"
                                    title="Pop-out Chart"
                                >
                                    <ExternalLink size={14} />
                                </button>
                                <button
                                    onClick={() => removeSymbol(item.symbol)}
                                    className="p-1 text-muted hover:text-red"
                                >
                                    <X size={14} />
                                </button>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
