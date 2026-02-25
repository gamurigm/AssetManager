"use client"

import AppLayout from "@/components/layout/AppLayout";
import Watchlist from "@/components/watchlist/Watchlist";
import React, { useEffect, useState, useRef, useMemo } from "react";
import { TrendingUp, TrendingDown, DollarSign, BarChart3, ArrowUpRight, ArrowDownRight, X, PieChart as PieIcon, LayoutGrid, ChartPie, ChevronDown, ChevronUp, Star, Activity, FileText } from "lucide-react";
import AssetTreemap from "@/components/charts/AssetTreemap";
import SectorPieChart from "@/components/charts/SectorPieChart";
import AllocationDonut from "@/components/charts/AllocationDonut";
import { usePortfolio } from "@/context/PortfolioContext";
import { logger } from "@/lib/logger";




interface DashboardHolding {
    symbol: string;
    name: string;
    shares: number;
    price: number;
    entryPrice: number;
    factor: number;
    change: number;
    changePercent: number;
    source: string;
    sector: string;
    type: string;
}

export default function ClientDashboard() {
    const { holdings, setHoldings, totalValue, accountEquity, totalPnL, pnlPercent, closePosition } = usePortfolio();
    const [loading, setLoading] = useState(true);
    const [activeTab, setActiveTab] = useState("portfolio");
    const [openTabs, setOpenTabs] = useState<{ id: string; title: string; symbol: string | null }[]>([{ id: "portfolio", title: "My Portfolio", symbol: null }]);
    const [collapsed, setCollapsed] = useState<Record<string, boolean>>({});
    const [watchlistVisible, setWatchlistVisible] = useState(true);
    const [transactions, setTransactions] = useState<any[]>([]);

    const togglePanel = (id: string) => {
        setCollapsed(prev => ({ ...prev, [id]: !prev[id] }));
    };

    useEffect(() => {
        const fetchHistory = async () => {
            try {
                const res = await fetch('http://localhost:8282/api/v1/trading/history');
                const data = await res.json();
                setTransactions(data);
            } catch (err) {
                console.error("Failed to fetch history:", err);
            }
        };
        fetchHistory();
        const interval = setInterval(fetchHistory, 10000); // Poll every 10s
        return () => clearInterval(interval);
    }, []);

    useEffect(() => {
        logger.info("Dashboard", "Terminal Main Dashboard initialized");
    }, []);

    useEffect(() => {
        const fetchPrices = async () => {
            if (holdings.length === 0) {
                setLoading(false);
                return;
            }
            const currentHoldings = holdings;
            // Create a copy to mutate
            let newHoldings = [...currentHoldings];
            let changed = false;

            // Load sequentially to respect API/Browser limits
            for (let i = 0; i < newHoldings.length; i++) {
                const h = newHoldings[i];
                try {
                    const res = await fetch(`http://127.0.0.1:8282/api/v1/market/quote/${encodeURIComponent(h.symbol)}`);
                    if (!res.ok) {
                        console.warn(`404: ${h.symbol}`);
                        continue;
                    }

                    const data = await res.json();
                    if (data && !data.error) {
                        const currentPrice = data.price;
                        // Beneficio Neto = (Precio Actual - Precio Entrada) * Shares * Factor
                        const totalProfit = (currentPrice - (h as any).entryPrice) * h.shares * (h as any).factor;

                        // ChangePercent is relative to entry price
                        const changePercent = (h as any).entryPrice !== 0
                            ? ((currentPrice - (h as any).entryPrice) / (h as any).entryPrice) * 100
                            : 0;

                        newHoldings[i] = {
                            ...h,
                            price: currentPrice,
                            change: totalProfit,
                            changePercent: changePercent,
                            source: data.source || "Unknown"
                        };
                        changed = true;
                    }
                } catch (e: any) {
                    // Use console.warn instead of error to prevent Next.js Turbopack Error Overlay
                    console.warn(`Failed to sync ${h.symbol} - backend may be offline or syncing. Retrying later.`);
                }
            }
            // Batch update state so charts only re-render once
            if (changed) setHoldings([...newHoldings]);
            setLoading(false);
        };

        fetchPrices();
        const interval = setInterval(fetchPrices, 600000);
        return () => clearInterval(interval);
    }, [holdings.length]);

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

    const SECTOR_COLORS: Record<string, string> = {
        "Technology": "#3b82f6",
        "Digital Assets": "#06b6d4",
        "Forex": "#f97316",
        "Commodities": "#eab308",
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
                const value = Math.abs(h.shares) * h.price * h.factor;
                return {
                    name: h.name,
                    symbol: h.symbol,
                    value: value,
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
            const val = Math.abs(h.shares) * h.price * h.factor;
            sectors[sector] = (sectors[sector] || 0) + val;
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
                                    <button
                                        onClick={async () => {
                                            const res = await fetch('http://localhost:8282/api/v1/portfolios/report', {
                                                method: 'POST',
                                                headers: { 'Content-Type': 'application/json' },
                                                body: JSON.stringify({
                                                    holdings: activeHoldings,
                                                    total_value: totalValue,
                                                    total_pnl: totalPnL
                                                })
                                            });
                                            if (res.ok) {
                                                const data = await res.json();
                                                window.open(data.url, '_blank');
                                            } else {
                                                alert("Failed to generate report");
                                            }
                                        }}
                                        className="px-3 py-1.5 bg-accent hover:bg-accent-hover text-white text-[9px] font-black uppercase tracking-widest rounded-lg transition-all shadow-lg shadow-accent/20 flex items-center gap-2"
                                    >
                                        <Activity size={10} />
                                        Generate Executive PDF Report
                                    </button>
                                </div>

                                {/* Stat Cards */}
                                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 stagger">
                                    <StatCard
                                        label="AUM (TOTAL EQUITY)"
                                        value={`$${accountEquity.toLocaleString("en-US", { minimumFractionDigits: 3, maximumFractionDigits: 3 })}`}
                                        icon={<DollarSign size={14} />}
                                        accent="blue"
                                    />
                                    <StatCard
                                        label="P&L (YTD)"
                                        value={`${totalPnL >= 0 ? "+" : ""}$${totalPnL.toLocaleString("en-US", { minimumFractionDigits: 3, maximumFractionDigits: 3 })}`}
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
                                                <SectorPieChart data={sectorData} total={totalValue} />
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
                                                <button
                                                    onClick={async (e) => {
                                                        e.stopPropagation();
                                                        if (confirm("Are you sure you want to liquidate all positions?")) {
                                                            // Record each one as a SELL
                                                            for (const h of activeHoldings) {
                                                                try {
                                                                    await fetch('http://localhost:8282/api/v1/trading/record', {
                                                                        method: 'POST',
                                                                        headers: { 'Content-Type': 'application/json' },
                                                                        body: JSON.stringify({
                                                                            type_str: 'SELL',
                                                                            symbol: h.symbol,
                                                                            shares: h.shares,
                                                                            price: h.price
                                                                        })
                                                                    });
                                                                } catch (err) {
                                                                    console.error("Failed to record liquidation:", err);
                                                                }
                                                            }
                                                            setHoldings([]);
                                                        }
                                                    }}
                                                    className="px-2 py-0.5 rounded border border-red/40 bg-red/5 text-[9px] font-black text-red uppercase tracking-tighter hover:bg-red hover:text-white transition-all ml-2"
                                                >
                                                    Liquidate All
                                                </button>
                                                {collapsed['holdings'] ? <ChevronDown size={14} className="text-muted" /> : <ChevronUp size={14} className="text-muted" />}
                                            </div>
                                        </div>
                                        {!collapsed['holdings'] && (
                                            <div className="overflow-x-auto animate-in fade-in slide-in-from-top-2 duration-300">
                                                <table className="w-full text-sm">
                                                    <thead>
                                                        <tr className="text-left text-muted text-[10px] font-black uppercase tracking-widest border-b border-border bg-background/50">
                                                            <th className="px-6 py-3">Posicion</th>
                                                            <th className="px-4 py-3 text-right">Tipo</th>
                                                            <th className="px-4 py-3 text-right">Volumen</th>
                                                            <th className="px-4 py-3 text-right">Beneficio Neto</th>
                                                            <th className="px-4 py-3 text-right">Valor Mercado</th>
                                                            <th className="px-4 py-3 text-right">Precio Apertura</th>
                                                            <th className="px-4 py-3 text-right">Precio Mercado</th>
                                                            <th className="px-6 py-3 text-right">Acción</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody className="stagger">
                                                        {activeHoldings
                                                            .sort((a, b) => (b.shares * b.price) - (a.shares * a.price))
                                                            .map((h: any) => {
                                                                const changeValue = h.changePercent || 0;

                                                                // Synchronized Heatmap Color matching Treemap
                                                                const getHeatmapColor = (cv: number) => {
                                                                    if (cv > 5) return '#065f46';
                                                                    if (cv > 2.5) return '#10b981';
                                                                    if (cv > 1) return '#4ade80';
                                                                    if (cv >= 0.5) return '#fde047';
                                                                    if (cv >= 0.1) return '#facc15';
                                                                    if (cv > -0.1) return '#71717a';
                                                                    if (cv >= -0.5) return '#fbbf24';
                                                                    if (cv >= -1) return '#f97316';
                                                                    if (cv >= -3) return '#f43f5e';
                                                                    return '#ef4444';
                                                                };

                                                                const badgeColor = getHeatmapColor(changeValue);
                                                                const isBright = ['#fde047', '#facc15', '#fbbf24', '#4ade80'].includes(badgeColor);

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
                                                                        <td className="px-4 py-4 text-right font-bold text-xs uppercase tracking-tighter">
                                                                            {h.shares >= 0 ? "Buy" : "Sell"}
                                                                        </td>
                                                                        <td className="px-4 py-4 text-right font-mono text-xs font-bold">{Math.abs(h.shares)}</td>
                                                                        <td className={`px-4 py-4 text-right font-mono font-black text-sm ${h.change >= 0 ? 'text-green' : 'text-red'}`}>
                                                                            {h.change >= 0 ? "+" : ""}{h.change.toLocaleString("en-US", { minimumFractionDigits: 3, maximumFractionDigits: 3 })}
                                                                        </td>
                                                                        <td className={`px-4 py-4 text-right font-mono font-black text-sm ${h.change >= 0 ? 'text-green' : 'text-red'}`}>
                                                                            ${(Math.abs(h.shares) * h.price).toLocaleString("en-US", { minimumFractionDigits: 3, maximumFractionDigits: 3 })}
                                                                        </td>
                                                                        <td className="px-4 py-4 text-right font-mono text-xs text-muted">
                                                                            ${(h as any).entryPrice?.toLocaleString("en-US", { minimumFractionDigits: 3 })}
                                                                        </td>
                                                                        <td className="px-4 py-4 text-right font-mono text-xs text-muted">
                                                                            ${h.price.toLocaleString("en-US", { minimumFractionDigits: 3 })}
                                                                        </td>
                                                                        <td className="px-6 py-4 text-right">
                                                                            <button
                                                                                onClick={(e) => {
                                                                                    e.stopPropagation();
                                                                                    closePosition(h.symbol);
                                                                                }}
                                                                                className="opacity-0 group-hover:opacity-100 transition-all px-3 py-1.5 rounded-lg border border-red/20 text-[10px] font-black uppercase tracking-tighter text-red hover:bg-red/10 hover:border-red/40 hover:shadow-[0_0_12px_rgba(239,68,68,0.2)]"
                                                                            >
                                                                                Liquidate
                                                                            </button>
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

                                    {/* Recent Activity Panel */}
                                    <div className={`bg-card border border-border rounded-2xl overflow-hidden shadow-sm flex flex-col transition-all duration-300 ${collapsed['activity'] ? 'h-[50px]' : 'h-[400px]'}`}>
                                        <div
                                            onClick={() => togglePanel('activity')}
                                            className="px-5 py-3 border-b border-border flex items-center justify-between bg-card-hover/30 cursor-pointer hover:bg-card-hover/50 transition-colors"
                                        >
                                            <div className="flex items-center gap-2">
                                                <Activity size={12} className="text-accent" />
                                                <h2 className="text-xs font-black uppercase tracking-widest text-muted">Recent Activity</h2>
                                            </div>
                                            <div className="flex items-center gap-4">
                                                <span className="text-[10px] text-accent font-black">{transactions.length} Events</span>
                                                {collapsed['activity'] ? <ChevronDown size={14} className="text-muted" /> : <ChevronUp size={14} className="text-muted" />}
                                            </div>
                                        </div>
                                        {!collapsed['activity'] && (
                                            <div className="flex-1 overflow-y-auto p-0 animate-in fade-in slide-in-from-top-2 duration-300">
                                                {transactions.length === 0 ? (
                                                    <div className="h-full flex flex-col items-center justify-center p-8 text-center">
                                                        <Activity size={32} className="text-muted/20 mb-3" />
                                                        <p className="text-xs text-muted font-bold uppercase tracking-widest">No recent transactions</p>
                                                        <p className="text-[10px] text-muted/60 mt-1 max-w-[180px]">Automated and manual liquidations will appear here.</p>
                                                    </div>
                                                ) : (
                                                    <div className="divide-y divide-border/50">
                                                        {transactions.map((t, i) => (
                                                            <div key={i} className="px-5 py-3 hover:bg-card-hover/20 transition-colors flex items-center justify-between group">
                                                                <div className="flex items-center gap-3">
                                                                    <div className={`h-8 w-8 rounded-lg flex items-center justify-center font-black text-[10px] ${t.type === 'BUY' ? 'bg-green/10 text-green' : 'bg-red/10 text-red'}`}>
                                                                        {t.type.slice(0, 1)}
                                                                    </div>
                                                                    <div className="flex flex-col">
                                                                        <span className="text-xs font-black group-hover:text-accent transition-colors">{t.symbol}</span>
                                                                        <span className="text-[9px] text-muted font-bold uppercase tracking-tighter">{t.date} • {t.time}</span>
                                                                    </div>
                                                                </div>
                                                                <div className="text-right flex flex-col">
                                                                    <span className="text-xs font-mono font-black">${(t.price * t.shares).toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                                                                    <span className="text-[9px] text-muted font-bold tracking-tighter">{t.shares} units @ ${t.price.toFixed(2)}</span>
                                                                </div>
                                                            </div>
                                                        ))}
                                                    </div>
                                                )}
                                            </div>
                                        )}
                                    </div>

                                    {/* Watchlist Panel - Always Visible */}

                                    {/* REMOVED from here */}
                                </div>
                            </>
                        ) : (
                            <div className="h-full min-h-[900px] rounded-2xl overflow-hidden border border-border bg-card">
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

import { createChart, ColorType, CandlestickSeries, LineSeries, HistogramSeries } from "lightweight-charts";

/* ─── Indicator Math (Dashboard) ───────────────────────────────────── */
function calcEMADash(data: number[], period: number): number[] {
    const k = 2 / (period + 1);
    const ema: number[] = [data[0]];
    for (let i = 1; i < data.length; i++) ema.push(data[i] * k + ema[i - 1] * (1 - k));
    return ema;
}
function calcMACDDash(closes: number[], fast: number, slow: number, signal: number) {
    const emaFast = calcEMADash(closes, fast);
    const emaSlow = calcEMADash(closes, slow);
    const macdLine = emaFast.map((v, i) => v - emaSlow[i]);
    const signalLine = calcEMADash(macdLine, signal);
    const histogram = macdLine.map((v, i) => v - signalLine[i]);
    return { macdLine, signalLine, histogram };
}
function calcStochDash(highs: number[], lows: number[], closes: number[], kP: number, dP: number, smooth: number) {
    const rawK: number[] = [];
    for (let i = 0; i < closes.length; i++) {
        if (i < kP - 1) { rawK.push(NaN); continue; }
        const hh = Math.max(...highs.slice(i - kP + 1, i + 1));
        const ll = Math.min(...lows.slice(i - kP + 1, i + 1));
        rawK.push(hh === ll ? 50 : ((closes[i] - ll) / (hh - ll)) * 100);
    }
    const kLine: number[] = [];
    for (let i = 0; i < rawK.length; i++) {
        if (i < kP - 1 + smooth - 1 || isNaN(rawK[i])) { kLine.push(NaN); continue; }
        const sl = rawK.slice(i - smooth + 1, i + 1).filter(v => !isNaN(v));
        kLine.push(sl.reduce((s, v) => s + v, 0) / sl.length);
    }
    const dLine: number[] = [];
    for (let i = 0; i < kLine.length; i++) {
        if (isNaN(kLine[i]) || i < kP - 1 + smooth - 1 + dP - 1) { dLine.push(NaN); continue; }
        const sl = kLine.slice(i - dP + 1, i + 1).filter(v => !isNaN(v));
        dLine.push(sl.reduce((s, v) => s + v, 0) / sl.length);
    }
    return { kLine, dLine };
}

function InternalChart({ symbol }: { symbol: string }) {
    const { closePosition } = usePortfolio();
    const chartContainerRef = useRef<HTMLDivElement>(null);
    const macdRef = useRef<HTMLDivElement>(null);
    const stochRef = useRef<HTMLDivElement>(null);
    const [loading, setLoading] = useState(true);
    const [theme, setTheme] = useState<'light' | 'dark'>('dark');
    const [quote, setQuote] = useState<{ price: number; changePercentage: number } | null>(null);
    const [candles, setCandles] = useState<any[]>([]);

    // Indicator params
    const [macdFast, setMacdFast] = useState(12);
    const [macdSlow, setMacdSlow] = useState(26);
    const [macdSignal, setMacdSignal] = useState(9);
    const [stochK, setStochK] = useState(14);
    const [stochD, setStochD] = useState(3);
    const [stochSmooth, setStochSmooth] = useState(3);
    const [showMacd, setShowMacd] = useState(true);
    const [showStoch, setShowStoch] = useState(true);
    const [showEmas, setShowEmas] = useState(true);

    // EMA params
    const [ema1, setEma1] = useState(9);
    const [ema2, setEma2] = useState(21);
    const [ema3, setEma3] = useState(50);

    useEffect(() => {
        const checkTheme = () => setTheme(document.documentElement.classList.contains('light') ? 'light' : 'dark');
        checkTheme();
        const observer = new MutationObserver(checkTheme);
        observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
        return () => observer.disconnect();
    }, []);

    // Fetch data — historical + quote in PARALLEL
    useEffect(() => {
        const fetchData = async () => {
            try {
                const [histRes, quoteRes] = await Promise.all([
                    fetch(`http://127.0.0.1:8282/api/v1/market/historical/${encodeURIComponent(symbol)}?limit=10000`),
                    fetch(`http://127.0.0.1:8282/api/v1/market/quote/${encodeURIComponent(symbol)}`)
                ]);
                const histData = await histRes.json();
                if (histData.historical && histData.historical.length > 0) {
                    const sorted = histData.historical.sort((a: any, b: any) => a.date.localeCompare(b.date));
                    setCandles(sorted);
                } else {
                    setCandles([]);
                }
                const q = await quoteRes.json();
                if (q && !q.error) setQuote({ price: q.price, changePercentage: q.changePercentage });
            } catch (err) {
                console.error("Dashboard chart fetch error:", err);
                setCandles([]);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [symbol]);

    const isLight = theme === 'light';
    const chartOpts = (h: number) => ({
        layout: { background: { type: ColorType.Solid as const, color: 'transparent' }, textColor: isLight ? '#3f3f46' : '#71717a' },
        grid: { vertLines: { color: isLight ? '#f4f4f5' : '#1a1a1a' }, horzLines: { color: isLight ? '#f4f4f5' : '#1a1a1a' } },
        height: h,
        rightPriceScale: { borderVisible: false },
        timeScale: { borderVisible: false },
        crosshair: { horzLine: { visible: true, labelVisible: true }, vertLine: { visible: true, labelVisible: true } },
    });

    // Main chart
    useEffect(() => {
        if (!chartContainerRef.current || candles.length === 0) return;
        const el = chartContainerRef.current;
        const chart = createChart(el, { ...chartOpts(el.clientHeight), width: el.clientWidth });
        const series = chart.addSeries(CandlestickSeries, {
            upColor: '#22c55e', downColor: '#ef4444', borderVisible: false,
            wickUpColor: '#22c55e', wickDownColor: '#ef4444',
        });
        series.setData(candles.map(d => ({ time: d.date, open: d.open, high: d.high, low: d.low, close: d.close })));

        if (showEmas) {
            const closes = candles.map(d => d.close);
            const times = candles.map(d => d.date);

            const e1Data = calcEMADash(closes, ema1);
            const e1Series = chart.addSeries(LineSeries, { color: '#fbbf24', lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false });
            e1Series.setData(e1Data.map((v, i) => ({ time: times[i], value: v })));

            const e2Data = calcEMADash(closes, ema2);
            const e2Series = chart.addSeries(LineSeries, { color: '#f472b6', lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false });
            e2Series.setData(e2Data.map((v, i) => ({ time: times[i], value: v })));

            const e3Data = calcEMADash(closes, ema3);
            const e3Series = chart.addSeries(LineSeries, { color: '#38bdf8', lineWidth: 2, priceLineVisible: false, crosshairMarkerVisible: false });
            e3Series.setData(e3Data.map((v, i) => ({ time: times[i], value: v })));
        }

        chart.timeScale().fitContent();
        const handleResize = () => chart.applyOptions({ width: el.clientWidth });
        window.addEventListener('resize', handleResize);
        return () => { window.removeEventListener('resize', handleResize); chart.remove(); };
    }, [candles, theme, showEmas, ema1, ema2, ema3]);

    // MACD chart
    useEffect(() => {
        if (!macdRef.current || candles.length === 0 || !showMacd) return;
        const el = macdRef.current;
        const chart = createChart(el, { ...chartOpts(130), width: el.clientWidth });
        const closes = candles.map(d => d.close);
        const times = candles.map(d => d.date);
        const { macdLine, signalLine, histogram } = calcMACDDash(closes, macdFast, macdSlow, macdSignal);
        const histSeries = chart.addSeries(HistogramSeries, { color: '#3b82f6', priceLineVisible: false });
        histSeries.setData(times.map((t, i) => ({ time: t, value: histogram[i], color: histogram[i] >= 0 ? '#22c55e80' : '#ef444480' })));
        const macdS = chart.addSeries(LineSeries, { color: '#3b82f6', lineWidth: 1, priceLineVisible: false });
        macdS.setData(times.map((t, i) => ({ time: t, value: macdLine[i] })));
        const sigS = chart.addSeries(LineSeries, { color: '#f97316', lineWidth: 1, priceLineVisible: false });
        sigS.setData(times.map((t, i) => ({ time: t, value: signalLine[i] })));
        chart.timeScale().fitContent();
        const handleResize = () => chart.applyOptions({ width: el.clientWidth });
        window.addEventListener('resize', handleResize);
        return () => { window.removeEventListener('resize', handleResize); chart.remove(); };
    }, [candles, theme, macdFast, macdSlow, macdSignal, showMacd]);

    // Stochastic chart
    useEffect(() => {
        if (!stochRef.current || candles.length === 0 || !showStoch) return;
        const el = stochRef.current;
        const chart = createChart(el, { ...chartOpts(130), width: el.clientWidth });
        const closes = candles.map(d => d.close);
        const highs = candles.map(d => d.high);
        const lows = candles.map(d => d.low);
        const times = candles.map(d => d.date);
        const { kLine, dLine } = calcStochDash(highs, lows, closes, stochK, stochD, stochSmooth);
        const kS = chart.addSeries(LineSeries, { color: '#8b5cf6', lineWidth: 1, priceLineVisible: false });
        kS.setData(times.map((t, i) => ({ time: t, value: isNaN(kLine[i]) ? undefined : kLine[i] })).filter(d => d.value !== undefined));
        const dS = chart.addSeries(LineSeries, { color: '#ec4899', lineWidth: 1, priceLineVisible: false });
        dS.setData(times.map((t, i) => ({ time: t, value: isNaN(dLine[i]) ? undefined : dLine[i] })).filter(d => d.value !== undefined));
        chart.timeScale().fitContent();
        const handleResize = () => chart.applyOptions({ width: el.clientWidth });
        window.addEventListener('resize', handleResize);
        return () => { window.removeEventListener('resize', handleResize); chart.remove(); };
    }, [candles, theme, stochK, stochD, stochSmooth, showStoch]);

    return (
        <div className="flex flex-col h-full">
            {/* Header */}
            <div className="px-6 py-4 border-b border-border flex items-center justify-between bg-card-hover/20">
                <div className="flex items-center gap-4">
                    <div className="h-8 w-8 rounded-lg bg-accent/20 flex items-center justify-center text-accent text-xs font-bold">
                        {symbol.slice(0, 2)}
                    </div>
                    <div className="flex flex-col">
                        <h2 className="text-xl font-bold leading-none">{symbol}</h2>
                        <span className="text-muted text-[10px] uppercase font-bold tracking-widest mt-1">Institutional Performance</span>
                    </div>

                    {quote && (
                        <div className="flex items-center gap-3 ml-4 pl-4 border-l border-border">
                            <span className="text-xl font-mono font-black">${quote.price.toFixed(2)}</span>
                            <div className={`flex items-center gap-1 text-xs font-black px-2 py-0.5 rounded-md ${quote.changePercentage >= 0 ? "bg-green/20 text-green" : "bg-red/20 text-red"}`}>
                                {quote.changePercentage >= 0 ? <TrendingUp size={12} /> : <TrendingDown size={12} />}
                                {quote.changePercentage.toFixed(2)}%
                            </div>
                        </div>
                    )}
                </div>

                <div className="flex items-center gap-3">
                    <button
                        onClick={() => {
                            if (confirm(`Liquidate total ${symbol} position?`)) {
                                closePosition(symbol);
                            }
                        }}
                        className="px-4 py-2 bg-red/10 hover:bg-red/20 border border-red/20 hover:border-red/40 text-red text-xs font-black uppercase tracking-widest rounded-xl transition-all shadow-sm hover:shadow-red/10"
                    >
                        Liquidate Position
                    </button>
                    {loading && <span className="text-xs animate-pulse text-accent font-mono uppercase tracking-tighter">Syncing...</span>}
                </div>
            </div>

            {/* Main Candlestick */}
            <div className="relative w-full" style={{ height: 'calc(100% - 320px)', minHeight: 300 }}>
                <div ref={chartContainerRef} className="absolute inset-0" />

                {/* Overlay EMA Controls */}
                <div className="absolute top-2 left-2 z-10 flex flex-col gap-1">
                    <div
                        className="flex items-center gap-2 px-2 py-1 bg-card-hover/90 backdrop-blur-sm rounded border border-border/50 cursor-pointer hover:bg-card-hover transition-colors select-none"
                        onClick={() => setShowEmas(!showEmas)}
                    >
                        <span className="text-[10px] font-black uppercase tracking-[0.15em] text-muted">MOVING AVERAGES</span>
                        {showEmas ? <ChevronUp size={10} className="text-muted" /> : <ChevronDown size={10} className="text-muted" />}
                    </div>
                    {showEmas && (
                        <div className="flex flex-col gap-1.5 p-2 bg-card-hover/90 backdrop-blur-sm rounded border border-border/50" onClick={e => e.stopPropagation()}>
                            <div className="flex items-center gap-2">
                                <div className="h-2 w-2 rounded-full bg-[#fbbf24] shadow-[0_0_8px_#fbbf24]" />
                                <span className="text-[9px] font-mono text-muted font-bold w-12">EMA 1</span>
                                <input type="number" value={ema1} onChange={e => setEma1(+e.target.value || 9)} min={1} max={200} className="w-12 px-1 py-0.5 bg-background border border-border/50 rounded text-[10px] text-foreground font-mono text-center focus:outline-none" />
                            </div>
                            <div className="flex items-center gap-2">
                                <div className="h-2 w-2 rounded-full bg-[#f472b6] shadow-[0_0_8px_#f472b6]" />
                                <span className="text-[9px] font-mono text-muted font-bold w-12">EMA 2</span>
                                <input type="number" value={ema2} onChange={e => setEma2(+e.target.value || 21)} min={1} max={200} className="w-12 px-1 py-0.5 bg-background border border-border/50 rounded text-[10px] text-foreground font-mono text-center focus:outline-none" />
                            </div>
                            <div className="flex items-center gap-2">
                                <div className="h-2 w-2 rounded-full bg-[#38bdf8] shadow-[0_0_8px_#38bdf8]" />
                                <span className="text-[9px] font-mono text-muted font-bold w-12">EMA 3</span>
                                <input type="number" value={ema3} onChange={e => setEma3(+e.target.value || 50)} min={1} max={500} className="w-12 px-1 py-0.5 bg-background border border-border/50 rounded text-[10px] text-foreground font-mono text-center focus:outline-none" />
                            </div>
                        </div>
                    )}
                </div>
            </div>

            {/* MACD Panel */}
            <div className="border-t border-border/30 flex-shrink-0">
                <div
                    className="flex items-center justify-between px-3 py-1.5 bg-card-hover/30 cursor-pointer select-none"
                    onClick={() => setShowMacd(!showMacd)}
                >
                    <div className="flex items-center gap-2">
                        <span className="text-[10px] font-black uppercase tracking-[0.15em] text-muted">MACD ({macdFast},{macdSlow},{macdSignal})</span>
                        {showMacd ? <ChevronUp size={12} className="text-muted" /> : <ChevronDown size={12} className="text-muted" />}
                    </div>
                    {showMacd && (
                        <div className="flex items-center gap-2" onClick={e => e.stopPropagation()}>
                            <input type="number" value={macdFast} min={2} max={50} onChange={e => setMacdFast(+e.target.value || 12)} className="w-10 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[10px] text-white font-mono text-center focus:outline-none" />
                            <input type="number" value={macdSlow} min={2} max={100} onChange={e => setMacdSlow(+e.target.value || 26)} className="w-10 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[10px] text-white font-mono text-center focus:outline-none" />
                            <input type="number" value={macdSignal} min={2} max={50} onChange={e => setMacdSignal(+e.target.value || 9)} className="w-10 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[10px] text-white font-mono text-center focus:outline-none" />
                        </div>
                    )}
                </div>
                {showMacd && <div ref={macdRef} className="w-full" style={{ height: 130 }} />}
            </div>

            {/* Stochastic Panel */}
            <div className="border-t border-border/30 flex-shrink-0">
                <div
                    className="flex items-center justify-between px-3 py-1.5 bg-card-hover/30 cursor-pointer select-none"
                    onClick={() => setShowStoch(!showStoch)}
                >
                    <div className="flex items-center gap-2">
                        <span className="text-[10px] font-black uppercase tracking-[0.15em] text-muted">STOCH ({stochK},{stochD},{stochSmooth})</span>
                        {showStoch ? <ChevronUp size={12} className="text-muted" /> : <ChevronDown size={12} className="text-muted" />}
                    </div>
                    {showStoch && (
                        <div className="flex items-center gap-2" onClick={e => e.stopPropagation()}>
                            <input type="number" value={stochK} min={2} max={50} onChange={e => setStochK(+e.target.value || 14)} className="w-10 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[10px] text-white font-mono text-center focus:outline-none" />
                            <input type="number" value={stochD} min={2} max={50} onChange={e => setStochD(+e.target.value || 3)} className="w-10 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[10px] text-white font-mono text-center focus:outline-none" />
                            <input type="number" value={stochSmooth} min={1} max={20} onChange={e => setStochSmooth(+e.target.value || 3)} className="w-10 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[10px] text-white font-mono text-center focus:outline-none" />
                        </div>
                    )}
                </div>
                {showStoch && <div ref={stochRef} className="w-full" style={{ height: 130 }} />}
            </div>
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
                        {React.cloneElement(icon as React.ReactElement<any>, { size: 14 })}
                    </div>
                </div>
                <p className="text-xl font-black font-mono tracking-tighter">{value}</p>
                {sub && <p className={`text-[10px] font-bold mt-0.5 ${accent === "red" ? "text-red" : "text-green"}`}>{sub}</p>}
            </div>
        </div>
    );
}
