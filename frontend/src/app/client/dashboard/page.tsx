"use client"

import AppLayout from "@/components/layout/AppLayout";
import Watchlist from "@/components/watchlist/Watchlist";
import { useEffect, useState, useRef, useMemo } from "react";
import { TrendingUp, TrendingDown, DollarSign, BarChart3, ArrowUpRight, ArrowDownRight, X, PieChart as PieIcon, LayoutGrid } from "lucide-react";
import AssetTreemap from "@/components/charts/AssetTreemap";
import AllocationDonut from "@/components/charts/AllocationDonut";

const INITIAL_HOLDINGS = [
    { symbol: "AAPL", name: "Apple Inc.", shares: 45, price: 0, change: 0, changePercent: 0, source: "Loading..." },
    { symbol: "MSFT", name: "Microsoft Corp.", shares: 30, price: 0, change: 0, changePercent: 0, source: "Loading..." },
    { symbol: "BTC/USD", name: "Bitcoin", shares: 0.5, price: 0, change: 0, changePercent: 0, source: "Loading..." },
    { symbol: "NVDA", name: "NVIDIA Corp.", shares: 20, price: 0, change: 0, changePercent: 0, source: "Loading..." },
    { symbol: "EUR/USD", name: "Euro / US Dollar", shares: 5000, price: 0, change: 0, changePercent: 0, source: "Loading..." },
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

    // Treemap Data
    const treemapData = useMemo(() => {
        return holdings
            .filter(h => h.price > 0)
            .map(h => ({
                name: h.name,
                symbol: h.symbol,
                value: h.shares * h.price,
                change: h.changePercent
            }))
            .sort((a, b) => b.value - a.value);
    }, [holdings]);

    // Donut Data (By Class)
    const allocationData = useMemo(() => {
        const classes: Record<string, number> = {};
        holdings.forEach(h => {
            let category = "Equities";
            if (h.symbol.includes("BTC") || h.symbol.includes("ETH")) category = "Digital Assets";
            else if (h.symbol.includes("/")) category = "FX / Commodities";

            classes[category] = (classes[category] || 0) + (h.shares * h.price);
        });
        return Object.entries(classes).map(([name, value]) => ({ name, value }));
    }, [holdings]);

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

                <div className="flex-1 overflow-y-auto p-6 lg:p-8 space-y-6">
                    {activeTab === "portfolio" ? (
                        <>
                            {/* Header */}
                            <div className="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-4">
                                <div>
                                    <p className="text-accent text-xs font-bold uppercase tracking-[0.2em] mb-1">Portfolio Oversight</p>
                                    <h1 className="text-3xl font-bold tracking-tight mt-1">Multi-Asset Mandate</h1>
                                </div>
                                <div className="flex items-center gap-2">
                                    <span className={`flex h-2 w-2 rounded-full ${loading ? 'bg-yellow-400' : 'bg-green animate-pulse'}`} />
                                    <span className="text-xs text-muted font-medium">{loading ? 'Syncing...' : 'Live Real-time Feed'}</span>
                                </div>
                            </div>

                            {/* Stat Cards */}
                            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 stagger">
                                <StatCard
                                    label="Net Liquidation Value"
                                    value={`$${totalValue.toLocaleString("en-US", { minimumFractionDigits: 2 })}`}
                                    icon={<DollarSign size={18} />}
                                    accent="blue"
                                />
                                <StatCard
                                    label="YTD Unrealized P&L"
                                    value={`${totalPnL >= 0 ? "+" : ""}$${totalPnL.toLocaleString("en-US", { minimumFractionDigits: 2 })}`}
                                    sub={`${pnlPercent >= 0 ? "+" : ""}${pnlPercent.toFixed(2)}% vs Bench.`}
                                    icon={totalPnL >= 0 ? <TrendingUp size={18} /> : <TrendingDown size={18} />}
                                    accent={totalPnL >= 0 ? "green" : "red"}
                                />
                                <StatCard
                                    label="Portfolio VaR (95%)"
                                    value="4.2%"
                                    sub="Critical: 7.5%"
                                    icon={<BarChart3 size={18} />}
                                    accent="purple"
                                />
                                <StatCard
                                    label="Adjusted Beta"
                                    value="1.14"
                                    sub="Aggressive Exposure"
                                    icon={<TrendingUp size={18} />}
                                    accent="emerald"
                                />
                            </div>

                            {/* Advanced Visualizations Row */}
                            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 animate-slide-up" style={{ animationDelay: '0.2s' }}>
                                {/* Allocation Donut */}
                                <div className="bg-card border border-border rounded-2xl overflow-hidden shadow-sm flex flex-col h-[380px]">
                                    <div className="px-6 py-4 border-b border-border flex items-center justify-between bg-card-hover/20">
                                        <div className="flex items-center gap-2">
                                            <PieIcon size={16} className="text-accent" />
                                            <h2 className="text-sm font-bold uppercase tracking-widest text-muted">Asset Allocation</h2>
                                        </div>
                                    </div>
                                    <div className="p-4 flex-1 flex items-center justify-center overflow-hidden">
                                        <AllocationDonut data={allocationData} />
                                    </div>
                                </div>

                                {/* Treemap Visualizer */}
                                <div className="lg:col-span-2 bg-card border border-border rounded-2xl overflow-hidden shadow-sm flex flex-col h-[380px]">
                                    <div className="px-6 py-4 border-b border-border flex items-center justify-between bg-card-hover/20">
                                        <div className="flex items-center gap-2">
                                            <LayoutGrid size={16} className="text-accent" />
                                            <h2 className="text-sm font-bold uppercase tracking-widest text-muted">Portfolio Intensity (Treemap)</h2>
                                        </div>
                                        <span className="text-[10px] text-muted font-bold px-2 py-0.5 bg-background rounded border border-border">VALUE WEIGHTED</span>
                                    </div>
                                    <div className="p-2 flex-1 overflow-hidden">
                                        <AssetTreemap data={treemapData} />
                                    </div>
                                </div>
                            </div>

                            {/* Main Grid */}
                            <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
                                {/* Holdings Table */}
                                <div className="xl:col-span-2 bg-card border border-border rounded-2xl overflow-hidden shadow-sm transition-shadow">
                                    <div className="px-6 py-4 border-b border-border flex items-center justify-between bg-card-hover/30">
                                        <h2 className="text-base font-semibold">Holdings</h2>
                                        <span className="text-xs text-muted">{holdings.length} positions · Multi-Source</span>
                                    </div>
                                    <div className="overflow-x-auto">
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
                                                {holdings.map((h) => (
                                                    <tr
                                                        key={h.symbol}
                                                        onClick={() => openSymbolTab(h.symbol)}
                                                        className="border-b border-border/50 hover:bg-card-hover transition-colors group cursor-pointer"
                                                    >
                                                        <td className="px-6 py-4">
                                                            <div className="flex items-center gap-3">
                                                                <div className="h-9 w-9 rounded-lg bg-accent/10 flex items-center justify-center text-accent font-bold text-xs group-hover:scale-110 transition-transform">
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
                                                            <div className={`inline-flex items-center gap-1 text-[10px] font-bold px-2 py-0.5 rounded-full ${h.changePercent >= 0
                                                                ? "text-green bg-green/10"
                                                                : "text-red bg-red/10"
                                                                }`}>
                                                                {h.changePercent >= 0 ? <TrendingUp size={10} /> : <TrendingDown size={10} />}
                                                                {Math.abs(h.changePercent).toFixed(2)}%
                                                            </div>
                                                        </td>
                                                        <td className="px-6 py-4 text-right">
                                                            <span className="text-[10px] bg-background border border-border px-2 py-0.5 rounded-md text-muted font-mono">
                                                                {h.source}
                                                            </span>
                                                        </td>
                                                    </tr>
                                                ))}
                                            </tbody>
                                        </table>
                                    </div>
                                </div>

                                {/* Fee Analysis Panel */}
                                <div className="bg-card border border-border rounded-2xl overflow-hidden shadow-sm flex flex-col">
                                    <div className="px-6 py-4 border-b border-border flex items-center justify-between bg-card-hover/30">
                                        <h2 className="text-base font-semibold">Mandate Economics</h2>
                                        <span className="text-[10px] text-muted font-black uppercase tracking-widest">Fiduciary Billing</span>
                                    </div>
                                    <div className="p-6 space-y-6 flex-1">
                                        <div className="space-y-2">
                                            <div className="flex justify-between text-xs">
                                                <span className="text-muted">Management Fee (1.0% p.a.)</span>
                                                <span className="font-mono text-accent">${(totalValue * 0.01 / 12).toFixed(2)} / mo</span>
                                            </div>
                                            <div className="w-full bg-background rounded-full h-1.5 overflow-hidden">
                                                <div className="h-full bg-accent w-1/4" />
                                            </div>
                                        </div>

                                        <div className="space-y-2">
                                            <div className="flex justify-between text-xs">
                                                <span className="text-muted">High-Water Mark (HWM)</span>
                                                <span className="font-mono text-white">$1,250,500.00</span>
                                            </div>
                                            <div className="p-3 rounded-lg bg-green/5 border border-green/10 flex items-center justify-between">
                                                <span className="text-[10px] text-green font-bold uppercase">Performance Fee Accrued</span>
                                                <span className="text-sm font-black text-green font-mono">+$1,420.50</span>
                                            </div>
                                        </div>

                                        <div className="mt-auto pt-4 border-t border-border/50">
                                            <p className="text-[10px] text-muted leading-relaxed">
                                                Fees are calculated based on the <span className="text-foreground">Net Asset Value (NAV)</span> at the end of each billing cycle. Performance fees are subject to HWM principles as per the investment mandate.
                                            </p>
                                        </div>
                                    </div>
                                </div>

                                {/* Watchlist Panel */}
                                <div className="h-[500px] xl:h-[600px] xl:col-span-2">
                                    <Watchlist onSelectSymbol={openSymbolTab} />
                                </div>
                            </div>
                        </>
                    ) : (
                        <div className="h-full min-h-[600px] rounded-2xl overflow-hidden border border-border bg-card">
                            <InternalChart symbol={activeTab} />
                        </div>
                    )}
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
        <div className="bg-card border border-border rounded-2xl p-5 hover:border-border-hover transition-all group relative overflow-hidden shadow-sm">
            <div className="shimmer absolute inset-0 pointer-events-none opacity-0 group-hover:opacity-100 transition-opacity" />
            <div className="relative z-10">
                <div className="flex items-center justify-between mb-3">
                    <span className="text-xs text-muted font-medium uppercase tracking-wider">{label}</span>
                    <div className={`h-7 w-7 rounded-lg flex items-center justify-center ${colors[accent] || colors.blue}`}>
                        {icon}
                    </div>
                </div>
                <p className="text-2xl font-bold font-mono">{value}</p>
                {sub && <p className={`text-xs font-semibold mt-1 ${accent === "red" ? "text-red" : "text-green"}`}>{sub}</p>}
            </div>
        </div>
    );
}
