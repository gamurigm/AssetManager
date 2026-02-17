"use client"

import AppLayout from "@/components/layout/AppLayout";
import Watchlist from "@/components/watchlist/Watchlist";
import React, { useEffect, useState, useRef, useMemo } from "react";
import { TrendingUp, TrendingDown, DollarSign, BarChart3, ArrowUpRight, ArrowDownRight, X, PieChart as PieIcon, LayoutGrid, ChartPie, ChevronDown, ChevronUp, Star } from "lucide-react";
import AssetTreemap from "@/components/charts/AssetTreemap";
import SectorPieChart from "@/components/charts/SectorPieChart";
import AllocationDonut from "@/components/charts/AllocationDonut";

const INITIAL_HOLDINGS = [
    { symbol: "AAPL", name: "Apple Inc.", shares: 45, price: 0, change: 0, changePercent: 0, source: "Loading...", sector: "Technology" },
    { symbol: "MSFT", name: "Microsoft Corp.", shares: 30, price: 0, change: 0, changePercent: 0, source: "Loading...", sector: "Technology" },
    { symbol: "BTC/USD", name: "Bitcoin", shares: 0.5, price: 0, change: 0, changePercent: 0, source: "Loading...", sector: "Digital Assets" },
    { symbol: "NVDA", name: "NVIDIA Corp.", shares: 20, price: 0, change: 0, changePercent: 0, source: "Loading...", sector: "Technology" },
    { symbol: "EUR/USD", name: "Euro / US Dollar", shares: 5000, price: 0, change: 0, changePercent: 0, source: "Loading...", sector: "FX / Commodities" },
    { symbol: "JPM", name: "JPMorgan Chase & Co.", shares: 25, price: 0, change: 0, changePercent: 0, source: "Loading...", sector: "Financials" },
    { symbol: "XOM", name: "Exxon Mobil Corp.", shares: 40, price: 0, change: 0, changePercent: 0, source: "Loading...", sector: "Energy" },
    { symbol: "PFE", name: "Pfizer Inc.", shares: 100, price: 0, change: 0, changePercent: 0, source: "Loading...", sector: "Health Care" },
    { symbol: "TSLA", name: "Tesla, Inc.", shares: 15, price: 0, change: 0, changePercent: 0, source: "Loading...", sector: "Consumer Discretionary" },
    { symbol: "AMZN", name: "Amazon.com, Inc.", shares: 20, price: 0, change: 0, changePercent: 0, source: "Loading...", sector: "Consumer Discretionary" },
];

const MOCK_TRANSACTIONS = [
    { id: 1, type: "BUY", symbol: "NVDA", shares: 5, price: 860.00, date: "2026-02-16", time: "10:32 AM" },
    { id: 2, type: "SELL", symbol: "AAPL", shares: 10, price: 176.50, date: "2026-02-15", time: "3:45 PM" },
    { id: 3, type: "BUY", symbol: "GOOGL", shares: 8, price: 170.85, date: "2026-02-14", time: "11:15 AM" },
    { id: 4, type: "BUY", symbol: "MSFT", shares: 5, price: 417.20, date: "2026-02-13", time: "9:50 AM" },
];

export default function ClientDashboard() {
    const [holdings, setHoldings] = useState(INITIAL_HOLDINGS);
    const [loading, setLoading] = useState(true);
    const [activeTab, setActiveTab] = useState("portfolio");
    const [openTabs, setOpenTabs] = useState([{ id: "portfolio", title: "My Portfolio", symbol: null }]);
    const [collapsed, setCollapsed] = useState<Record<string, boolean>>({});
    const [watchlistVisible, setWatchlistVisible] = useState(true);

    const togglePanel = (id: string) => {
        setCollapsed(prev => ({ ...prev, [id]: !prev[id] }));
    };

    useEffect(() => {
        const fetchPrices = async () => {
            const updatedHoldings = await Promise.all(
                holdings.map(async (h) => {
                    try {
                        const res = await fetch(`http://127.0.0.1:8000/api/v1/market/quote/${encodeURIComponent(h.symbol)}`);
                        if (!res.ok) {
                            console.warn(`Market data 404 for ${h.symbol}: ${res.status}`);
                            return h;
                        }
                        const data = await res.json();
                        if (data && !data.error) {
                            return {
                                ...h,
                                price: data.price,
                                change: data.change || 0,
                                changePercent: data.changePercentage || 0,
                                source: data.source || "Unknown"
                            };
                        }
                    } catch (e) {
                        console.error(`Error fetching ${h.symbol}:`, e);
                    }
                    return h;
                })
            );
            setHoldings(updatedHoldings);
            setLoading(false);
        };

        fetchPrices();
        const interval = setInterval(fetchPrices, 30000);
        return () => clearInterval(interval);
    }, []);

    const openSymbolTab = (symbol: string) => {
        if (!openTabs.find(t => t.id === symbol)) {
            setOpenTabs([...openTabs, { id: symbol, title: symbol, symbol: symbol }]);
        }
        setActiveTab(symbol);
    };

    const closeTab = (e: React.MouseEvent, id: string) => {
        e.stopPropagation();
        if (id === "portfolio") return;
        const newTabs = openTabs.filter(t => t.id !== id);
        setOpenTabs(newTabs);
        if (activeTab === id) setActiveTab("portfolio");
    };

    const totalValue = holdings.reduce((sum, h) => sum + h.shares * h.price, 0);
    const totalPnL = holdings.reduce((sum, h) => sum + h.shares * h.change, 0);
    const pnlPercent = totalValue > 0 ? (totalPnL / (totalValue - totalPnL)) * 100 : 0;

    const SECTOR_COLORS: Record<string, string> = {
        "Technology": "#3b82f6",
        "Digital Assets": "#06b6d4",
        "FX / Commodities": "#f97316",
        "Financials": "#10b981",
        "Energy": "#f59e0b",
        "Health Care": "#ef4444",
        "Consumer Discretionary": "#ec4899",
    };

    // Filtered Holdings - The source of truth for all charts and the table
    const activeHoldings = useMemo(() => {
        return holdings.filter(h => h.price > 0);
    }, [holdings]);

    // Treemap Data - Derived from active holdings
    const treemapData = useMemo(() => {
        return activeHoldings
            .map(h => {
                const sector = (h as any).sector || "Other";
                return {
                    name: h.name,
                    symbol: h.symbol,
                    value: h.shares * h.price,
                    change: h.changePercent,
                    sector: sector,
                    baseColor: SECTOR_COLORS[sector] || "#64748b"
                };
            })
            .sort((a, b) => b.value - a.value);
    }, [activeHoldings]);

    // Donut Data (By Class)
    const sectorData = useMemo(() => {
        const sectors: Record<string, number> = {};

        activeHoldings.forEach(h => {
            const sector = (h as any).sector || "Other";
            sectors[sector] = (sectors[sector] || 0) + (h.shares * h.price);
        });

        const totalVal = Object.values(sectors).reduce((a, b) => a + b, 0);

        return Object.entries(sectors)
            .filter(([_, value]) => value > 0)
            .map(([name, value]) => ({
                name,
                value,
                percent: totalVal > 0 ? (value / totalVal) * 100 : 0,
                color: SECTOR_COLORS[name] || "#64748b"
            }));
    }, [activeHoldings]);

    return (
        <AppLayout>
            <div className="flex flex-col h-full bg-background animate-fade-in">
                {/* Tabs Bar */}
                <div className="flex items-center gap-1 px-4 pt-4 border-b border-border bg-card/30">
                    {openTabs.map((tab) => (
                        <div
                            key={tab.id}
                            onClick={() => setActiveTab(tab.id)}
                            className={`group flex items-center gap-2 px-4 py-2 text-xs font-bold uppercase tracking-wider cursor-pointer transition-all rounded-t-xl border-t border-x border-transparent translate-y-[1px] ${activeTab === tab.id
                                ? "bg-background border-border text-accent"
                                : "text-muted hover:text-foreground hover:bg-card/50"
                                }`}
                        >
                            {tab.id === "portfolio" ? "Portfolio Alpha" : tab.title}
                            {tab.id !== "portfolio" && (
                                <X
                                    size={12}
                                    onClick={(e) => closeTab(e, tab.id)}
                                    className="opacity-0 group-hover:opacity-100 hover:text-red transition-opacity p-0.5 rounded-md hover:bg-red/10"
                                />
                            )}
                        </div>
                    ))}
                </div>

                <div className="flex-1 flex overflow-hidden">
                    {/* Main Content Area */}
                    <div className="flex-1 overflow-y-auto p-4 lg:px-8 lg:py-6 space-y-4">
                        {activeTab === "portfolio" ? (
                            <>
                                {/* Condensed Header */}
                                <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 border-b border-border/10 pb-3">
                                    <div className="flex items-center gap-3">
                                        <div className="h-2 w-2 rounded-full bg-accent animate-pulse" />
                                        <div>
                                            <p className="text-muted text-[9px] font-black uppercase tracking-[0.4em]">Portfolio</p>
                                            <h1 className="text-lg font-black tracking-tight mt-px">Asset Mandate Alpha</h1>
                                        </div>
                                    </div>
                                    <div className="flex items-center gap-2 px-2 py-1 rounded-md border border-border/30 bg-card/40">
                                        <span className={`flex h-1.5 w-1.5 rounded-full ${loading ? 'bg-yellow-400' : 'bg-green animate-pulse'}`} />
                                        <span className="text-[9px] text-muted font-black tracking-widest uppercase">{loading ? 'Syncing...' : 'Live'}</span>
                                    </div>
                                </div>

                                {/* Stat Cards */}
                                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 stagger">
                                    <StatCard
                                        label="NAV (NET ASSETS)"
                                        value={`$${totalValue.toLocaleString("en-US", { minimumFractionDigits: 2 })}`}
                                        icon={<DollarSign size={14} />}
                                        accent="blue"
                                    />
                                    <StatCard
                                        label="P&L (YTD)"
                                        value={`${totalPnL >= 0 ? "+" : ""}$${totalPnL.toLocaleString("en-US", { minimumFractionDigits: 2 })}`}
                                        sub={`${pnlPercent >= 0 ? "+" : ""}${pnlPercent.toFixed(2)}%`}
                                        icon={totalPnL >= 0 ? <TrendingUp size={14} /> : <TrendingDown size={14} />}
                                        accent={totalPnL >= 0 ? "green" : "red"}
                                    />
                                    <StatCard
                                        label="VAR (RISK)"
                                        value="4.20%"
                                        sub="LIMIT 7.5%"
                                        icon={<BarChart3 size={14} />}
                                        accent="purple"
                                    />
                                    <StatCard
                                        label="BETA (S&P 500)"
                                        value="1.14"
                                        sub="HIGH VOL."
                                        icon={<TrendingUp size={14} />}
                                        accent="emerald"
                                    />
                                </div>

                                {/* Advanced Visualizations Row - Professional Stacked Layout */}
                                <div className="grid grid-cols-1 gap-6 animate-slide-up" style={{ animationDelay: '0.2s' }}>
                                    {/* Sector Allocation Chart - TOP */}
                                    <div className={`bg-card border border-border rounded-2xl overflow-hidden shadow-sm flex flex-col transition-all duration-300 ${collapsed['sector'] ? 'min-h-[50px]' : 'min-h-[450px]'}`}>
                                        <div
                                            onClick={() => togglePanel('sector')}
                                            className="px-5 py-3 border-b border-border flex items-center justify-between bg-card-hover/20 cursor-pointer hover:bg-card-hover/40 transition-colors"
                                        >
                                            <div className="flex items-center gap-2">
                                                <ChartPie size={14} className="text-accent" />
                                                <h2 className="text-xs font-black uppercase tracking-widest text-muted">Sector Exposure</h2>
                                            </div>
                                            {collapsed['sector'] ? <ChevronDown size={14} className="text-muted" /> : <ChevronUp size={14} className="text-muted" />}
                                        </div>
                                        {!collapsed['sector'] && (
                                            <div className="flex-1 animate-in fade-in slide-in-from-top-2 duration-300">
                                                <SectorPieChart data={sectorData} />
                                            </div>
                                        )}
                                    </div>

                                    {/* Treemap Visualizer - BOTTOM */}
                                    <div className={`bg-card border border-border rounded-2xl overflow-hidden shadow-sm flex flex-col transition-all duration-300 ${collapsed['treemap'] ? 'min-h-[50px]' : 'min-h-[400px]'}`}>
                                        <div
                                            onClick={() => togglePanel('treemap')}
                                            className="px-5 py-3 border-b border-border flex items-center justify-between bg-card-hover/20 cursor-pointer hover:bg-card-hover/40 transition-colors"
                                        >
                                            <div className="flex items-center gap-2">
                                                <LayoutGrid size={14} className="text-accent" />
                                                <h2 className="text-xs font-black uppercase tracking-widest text-muted">Allocation Intensity</h2>
                                            </div>
                                            <div className="flex items-center gap-4">
                                                <span className="hidden sm:block text-[9px] text-muted font-black px-2 py-0.5 bg-background rounded border border-border tracking-tighter uppercase">Hi-Density</span>
                                                {collapsed['treemap'] ? <ChevronDown size={14} className="text-muted" /> : <ChevronUp size={14} className="text-muted" />}
                                            </div>
                                        </div>
                                        {!collapsed['treemap'] && (
                                            <div className="p-4 flex-1 animate-in fade-in slide-in-from-top-2 duration-300">
                                                <AssetTreemap data={treemapData} />
                                            </div>
                                        )}
                                    </div>
                                </div>

                                {/* Main Grid */}
                                <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
                                    {/* Holdings Table */}
                                    <div className={`xl:col-span-2 bg-card border border-border rounded-2xl overflow-hidden shadow-sm transition-all duration-300 ${collapsed['holdings'] ? 'h-[60px]' : ''}`}>
                                        <div
                                            onClick={() => togglePanel('holdings')}
                                            className="px-5 py-3 border-b border-border flex items-center justify-between bg-card-hover/30 cursor-pointer hover:bg-card-hover/50 transition-colors"
                                        >
                                            <h2 className="text-xs font-black uppercase tracking-widest text-muted">Positions</h2>
                                            <div className="flex items-center gap-4">
                                                <div className="flex items-center gap-2">
                                                    {holdings.length > activeHoldings.length && (
                                                        <div className="flex items-center gap-1.5 bg-yellow-400/5 px-2 py-0.5 rounded border border-yellow-400/20">
                                                            <span className="h-1 w-1 rounded-full bg-yellow-400 animate-pulse" />
                                                            <span className="text-[9px] text-yellow-400 font-black uppercase">{holdings.length - activeHoldings.length} Sync</span>
                                                        </div>
                                                    )}
                                                    <span className="text-[10px] text-accent font-black">{activeHoldings.length} Active</span>
                                                </div>
                                                {collapsed['holdings'] ? <ChevronDown size={14} className="text-muted" /> : <ChevronUp size={14} className="text-muted" />}
                                            </div>
                                        </div>
                                        {!collapsed['holdings'] && (
                                            <div className="overflow-x-auto animate-in fade-in slide-in-from-top-2 duration-300">
                                                <table className="w-full text-sm">
                                                    <thead>
                                                        <tr className="text-left text-muted text-xs border-b border-border bg-background/50">
                                                            <th className="px-6 py-3 font-medium">Asset</th>
                                                            <th className="px-4 py-3 font-medium text-right">Shares</th>
                                                            <th className="px-4 py-3 font-medium text-right">Price</th>
                                                            <th className="px-4 py-3 font-medium text-right">Value</th>
                                                            <th className="px-4 py-3 font-medium text-right">Change</th>
                                                            <th className="px-6 py-3 font-medium text-right">Source</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody className="stagger">
                                                        {[...activeHoldings]
                                                            .sort((a, b) => (b.shares * b.price) - (a.shares * a.price))
                                                            .map((h) => {
                                                                const changeValue = h.changePercent || 0;

                                                                // Accurate Heatmap Color matching Treemap
                                                                const getHeatmapColor = (cv: number) => {
                                                                    if (cv > 5) return '#10b981'; if (cv > 2.5) return '#22c55e';
                                                                    if (cv > 1) return '#4ade80'; if (cv > 0.4) return '#86efac';
                                                                    if (cv > 0.1) return '#0b3d2e';
                                                                    if (cv >= -0.1 && cv <= 0.1) return '#374151';
                                                                    if (cv >= -0.4) return '#78350f'; if (cv >= -1.2) return '#facc15';
                                                                    if (cv >= -2.5) return '#fbbf24'; if (cv >= -4) return '#f97316';
                                                                    if (cv >= -6) return '#f43f5e'; return '#ef4444';
                                                                };

                                                                const badgeColor = getHeatmapColor(changeValue);
                                                                const isBright = ['#facc15', '#fbbf24', '#86efac'].includes(badgeColor);

                                                                return (
                                                                    <tr
                                                                        key={h.symbol}
                                                                        onClick={() => openSymbolTab(h.symbol)}
                                                                        className="border-b border-border/50 hover:bg-card-hover transition-colors group cursor-pointer"
                                                                    >
                                                                        <td className="px-6 py-4">
                                                                            <div className="flex items-center gap-3">
                                                                                <div
                                                                                    className="h-9 w-9 rounded-lg flex items-center justify-center text-white font-bold text-xs group-hover:scale-110 transition-all shadow-sm"
                                                                                    style={{ backgroundColor: badgeColor }}
                                                                                >
                                                                                    {h.symbol.slice(0, 2)}
                                                                                </div>
                                                                                <div>
                                                                                    <p className="font-semibold group-hover:text-accent transition-colors">{h.symbol}</p>
                                                                                    <p className="text-xs text-muted truncate max-w-[120px]">{h.name}</p>
                                                                                </div>
                                                                            </div>
                                                                        </td>
                                                                        <td className="px-4 py-4 text-right font-mono text-xs">{h.shares}</td>
                                                                        <td className="px-4 py-4 text-right font-mono font-medium">${h.price.toFixed(h.symbol.includes('/') ? 4 : 2)}</td>
                                                                        <td className="px-4 py-4 text-right font-mono font-semibold text-accent">
                                                                            ${(h.shares * h.price).toLocaleString("en-US", { minimumFractionDigits: 2 })}
                                                                        </td>
                                                                        <td className="px-4 py-4 text-right">
                                                                            <div
                                                                                className="inline-flex items-center gap-1 text-[10px] font-black px-2.5 py-1 rounded-full shadow-sm"
                                                                                style={{
                                                                                    backgroundColor: badgeColor,
                                                                                    color: isBright ? '#000000' : '#ffffff'
                                                                                }}
                                                                            >
                                                                                {changeValue >= 0 ? <TrendingUp size={10} /> : <TrendingDown size={10} />}
                                                                                {Math.abs(changeValue).toFixed(2)}%
                                                                            </div>
                                                                        </td>
                                                                        <td className="px-6 py-4 text-right">
                                                                            <span className="text-[10px] bg-background border border-border px-2 py-0.5 rounded-md text-muted font-mono">
                                                                                {h.source}
                                                                            </span>
                                                                        </td>
                                                                    </tr>
                                                                );
                                                            })}
                                                    </tbody>
                                                </table>
                                            </div>
                                        )}
                                    </div>

                                    {/* Fee Analysis Panel */}
                                    <div className={`bg-card border border-border rounded-2xl overflow-hidden shadow-sm flex flex-col transition-all duration-300 ${collapsed['economics'] ? 'h-[50px]' : ''}`}>
                                        <div
                                            onClick={() => togglePanel('economics')}
                                            className="px-5 py-3 border-b border-border flex items-center justify-between bg-card-hover/30 cursor-pointer hover:bg-card-hover/50 transition-colors"
                                        >
                                            <h2 className="text-xs font-black uppercase tracking-widest text-muted">Economics</h2>
                                            <div className="flex items-center gap-4">
                                                {collapsed['economics'] ? <ChevronDown size={14} className="text-muted" /> : <ChevronUp size={14} className="text-muted" />}
                                            </div>
                                        </div>
                                        {!collapsed['economics'] && (
                                            <div className="p-6 space-y-5 flex-1 overflow-y-auto animate-in fade-in slide-in-from-top-2 duration-300">
                                                <div className="space-y-3">
                                                    <div className="flex justify-between text-[11px]">
                                                        <span className="text-muted">Management Fee (2.75%)</span>
                                                        <span className="font-mono text-white">${(totalValue * 0.0275 / 12).toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                                                    </div>
                                                    <div className="flex justify-between text-[11px]">
                                                        <span className="text-muted">Service Fee (0.75%)</span>
                                                        <span className="font-mono text-white">${(totalValue * 0.0075 / 12).toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                                                    </div>
                                                    <div className="flex justify-between text-[11px]">
                                                        <span className="text-muted">Other Exp. & Interest (0.59%)</span>
                                                        <span className="font-mono text-white">${(totalValue * 0.0059 / 12).toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                                                    </div>
                                                    <div className="flex justify-between text-[11px]">
                                                        <span className="text-muted">Reimbursements & Waivers</span>
                                                        <span className="font-mono text-green-400">-${(totalValue * 0.0059 / 12).toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                                                    </div>
                                                    <div className="pt-2 border-t border-border/50 flex justify-between text-xs font-bold">
                                                        <span className="text-accent uppercase tracking-tighter">Total Net Expenses (3.50%)</span>
                                                        <span className="font-mono text-accent">~${(totalValue * 0.0350 / 12).toLocaleString(undefined, { minimumFractionDigits: 2 })} / mo</span>
                                                    </div>
                                                </div>

                                                <div className="space-y-2 pt-4 border-t border-border/20">
                                                    <div className="flex justify-between text-xs">
                                                        <span className="text-muted">High-Water Mark (HWM)</span>
                                                        <span className="font-mono text-white">${totalValue > 1250500 ? totalValue.toLocaleString() : "1,250,500.00"}</span>
                                                    </div>
                                                    <div className="p-3 rounded-lg bg-green/5 border border-green/10 flex items-center justify-between">
                                                        <span className="text-[10px] text-green font-bold uppercase tracking-tight">Accrued Perf. Fee (20% above HWM)</span>
                                                        <span className="text-sm font-black text-green font-mono">
                                                            ${totalValue > 1250500 ? ((totalValue - 1250500) * 0.20).toFixed(2) : "0.00"}
                                                        </span>
                                                    </div>
                                                </div>

                                                <div className="mt-auto pt-4 border-t border-border/50">
                                                    <p className="text-[10px] text-muted leading-relaxed">
                                                        Fees are calculated based on the <span className="text-foreground">Net Asset Value (NAV)</span> at the end of each billing cycle. Performance fees are subject to HWM principles as per the investment mandate.
                                                    </p>
                                                </div>
                                            </div>
                                        )}
                                    </div>

                                    {/* Watchlist Panel - Always Visible */}
                                    {/* REMOVED from here */}
                                </div>
                            </>
                        ) : (
                            <div className="h-full min-h-[600px] rounded-2xl overflow-hidden border border-border bg-card">
                                <InternalChart symbol={activeTab} />
                            </div>
                        )}
                    </div>

                    {/* TradingView-style Watchlist Sidebar */}
                    {watchlistVisible && (
                        <div className="w-[300px] border-l border-border bg-card/10 animate-in slide-in-from-right duration-300 hidden xl:flex flex-col shadow-2xl z-20">
                            <Watchlist onSelectSymbol={openSymbolTab} />
                        </div>
                    )}

                    {/* Minimalist Vertical Toggle Bar */}
                    <div className="w-[45px] border-l border-border bg-card/20 flex flex-col items-center py-4 gap-6 z-30">
                        <button
                            onClick={() => setWatchlistVisible(!watchlistVisible)}
                            className={`p-2 rounded-lg transition-all ${watchlistVisible ? 'bg-accent/10 text-accent' : 'text-muted hover:text-foreground hover:bg-card/50'}`}
                            title="Toggle Watchlist"
                        >
                            <Star size={18} className={watchlistVisible ? 'fill-accent' : ''} />
                        </button>
                        <div className="h-px w-6 bg-border" />
                        <button className="text-muted hover:text-foreground transition-colors p-2 rounded-lg hover:bg-card/50">
                            <ChartPie size={18} />
                        </button>
                        <button className="text-muted hover:text-foreground transition-colors p-2 rounded-lg hover:bg-card/50">
                            <LayoutGrid size={18} />
                        </button>
                    </div>
                </div>
            </div>
        </AppLayout>
    );
}

import { createChart, ColorType, CandlestickSeries } from "lightweight-charts";

function InternalChart({ symbol }: { symbol: string }) {
    const chartContainerRef = useRef<HTMLDivElement>(null);
    const [loading, setLoading] = useState(true);
    const [theme, setTheme] = useState<'light' | 'dark'>('dark');

    useEffect(() => {
        const checkTheme = () => {
            setTheme(document.documentElement.classList.contains('light') ? 'light' : 'dark');
        };
        checkTheme();

        const observer = new MutationObserver(checkTheme);
        observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
        return () => observer.disconnect();
    }, []);

    useEffect(() => {
        if (!chartContainerRef.current) return;

        const isLight = theme === 'light';
        const chart = createChart(chartContainerRef.current, {
            layout: {
                background: { type: ColorType.Solid, color: 'transparent' },
                textColor: isLight ? '#3f3f46' : '#d1d1d1',
            },
            grid: {
                vertLines: { color: isLight ? '#f4f4f5' : '#1f1f1f' },
                horzLines: { color: isLight ? '#f4f4f5' : '#1f1f1f' },
            },
            width: chartContainerRef.current.clientWidth,
            height: 600,
        });

        const candlestickSeries = chart.addSeries(CandlestickSeries, {
            upColor: '#22c55e',
            downColor: '#ef4444',
            borderVisible: false,
            wickUpColor: '#22c55e',
            wickDownColor: '#ef4444',
        });

        const fetchHistory = async () => {
            try {
                const res = await fetch(`http://127.0.0.1:8000/api/v1/market/historical/${encodeURIComponent(symbol)}?limit=300`);
                const data = await res.json();
                if (data.historical) {
                    const formattedData = data.historical.map((d: any) => ({
                        time: d.date,
                        open: d.open,
                        high: d.high,
                        low: d.low,
                        close: d.close,
                    })).sort((a: any, b: any) => a.time.localeCompare(b.time));

                    candlestickSeries.setData(formattedData);
                    chart.timeScale().fitContent();
                    setLoading(false);
                }
            } catch (e) {
                console.error("Failed to fetch history", e);
            }
        };

        fetchHistory();
        const handleResize = () => chart.applyOptions({ width: chartContainerRef.current?.clientWidth || 800 });
        window.addEventListener('resize', handleResize);
        return () => {
            window.removeEventListener('resize', handleResize);
            chart.remove();
        };
    }, [symbol]);

    return (
        <div className="flex flex-col h-full">
            <div className="px-6 py-4 border-b border-border flex items-center justify-between bg-card-hover/20">
                <div className="flex items-center gap-3">
                    <div className="h-8 w-8 rounded-lg bg-accent/20 flex items-center justify-center text-accent text-xs font-bold">
                        {symbol.slice(0, 2)}
                    </div>
                    <h2 className="text-xl font-bold">{symbol} <span className="text-muted text-sm font-normal">/ Historical Performance</span></h2>
                </div>
                {loading && <span className="text-xs animate-pulse text-accent font-mono">Loading Data...</span>}
            </div>
            <div ref={chartContainerRef} className="flex-1 w-full" />
        </div>
    );
}

function StatCard({ label, value, sub, icon, accent }: {
    label: string;
    value: string;
    sub?: string;
    icon: React.ReactNode;
    accent: string;
}) {
    const colors: Record<string, string> = {
        blue: "text-blue-400 bg-blue-500/10",
        green: "text-green bg-green/10",
        red: "text-red bg-red/10",
        purple: "text-purple-400 bg-purple-500/10",
        emerald: "text-emerald-400 bg-emerald-500/10",
    };
    return (
        <div className="bg-card border border-border rounded-xl p-4 hover:border-accent/30 transition-all group relative overflow-hidden shadow-sm">
            <div className="shimmer absolute inset-0 pointer-events-none opacity-0 group-hover:opacity-100 transition-opacity" />
            <div className="relative z-10">
                <div className="flex items-center justify-between mb-2">
                    <span className="text-[10px] text-muted font-black uppercase tracking-[0.1em]">{label}</span>
                    <div className={`h-6 w-6 rounded-md flex items-center justify-center ${colors[accent] || colors.blue}`}>
                        {React.cloneElement(icon as React.ReactElement, { size: 14 })}
                    </div>
                </div>
                <p className="text-xl font-black font-mono tracking-tighter">{value}</p>
                {sub && <p className={`text-[10px] font-bold mt-0.5 ${accent === "red" ? "text-red" : "text-green"}`}>{sub}</p>}
            </div>
        </div>
    );
}
