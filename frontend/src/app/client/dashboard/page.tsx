"use client"

import AppLayout from "@/components/layout/AppLayout";
import { useEffect, useState } from "react";
import { TrendingUp, TrendingDown, DollarSign, BarChart3, ArrowUpRight, ArrowDownRight } from "lucide-react";

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

    useEffect(() => {
        const fetchPrices = async () => {
            const updatedHoldings = await Promise.all(
                holdings.map(async (h) => {
                    try {
                        const res = await fetch(`http://localhost:8000/api/v1/market/quote/${encodeURIComponent(h.symbol)}`);
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
        const interval = setInterval(fetchPrices, 30000); // 30s refresh
        return () => clearInterval(interval);
    }, []);

    const totalValue = holdings.reduce((sum, h) => sum + h.shares * h.price, 0);
    const totalPnL = holdings.reduce((sum, h) => sum + h.shares * h.change, 0);
    const pnlPercent = totalValue > 0 ? (totalPnL / (totalValue - totalPnL)) * 100 : 0;

    return (
        <AppLayout>
            <div className="p-6 lg:p-8 space-y-6 animate-fade-in">
                {/* Header */}
                <div className="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-4">
                    <div>
                        <p className="text-muted text-sm font-medium">Good afternoon</p>
                        <h1 className="text-3xl font-bold tracking-tight mt-1">My Portfolio</h1>
                    </div>
                    <div className="flex items-center gap-2">
                        <span className={`flex h-2 w-2 rounded-full ${loading ? 'bg-yellow-400' : 'bg-green animate-pulse'}`} />
                        <span className="text-xs text-muted font-medium">{loading ? 'Updating...' : 'Live Real-time Data'}</span>
                    </div>
                </div>

                {/* Stats Cards */}
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 stagger">
                    <StatCard
                        label="Total Value"
                        value={`$${totalValue.toLocaleString("en-US", { minimumFractionDigits: 2 })}`}
                        icon={<DollarSign size={18} />}
                        accent="blue"
                    />
                    <StatCard
                        label="Today's P&L"
                        value={`${totalPnL >= 0 ? "+" : ""}$${totalPnL.toLocaleString("en-US", { minimumFractionDigits: 2 })}`}
                        sub={`${pnlPercent >= 0 ? "+" : ""}${pnlPercent.toFixed(2)}%`}
                        icon={totalPnL >= 0 ? <TrendingUp size={18} /> : <TrendingDown size={18} />}
                        accent={totalPnL >= 0 ? "green" : "red"}
                    />
                    <StatCard
                        label="Holdings"
                        value={holdings.length.toString()}
                        icon={<BarChart3 size={18} />}
                        accent="purple"
                    />
                    <StatCard
                        label="Win Rate"
                        value="72.4%"
                        icon={<TrendingUp size={18} />}
                        accent="emerald"
                    />
                </div>

                {/* Main Grid */}
                <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
                    {/* Holdings Table */}
                    <div className="xl:col-span-2 bg-card border border-border rounded-2xl overflow-hidden shadow-sm">
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
                                        <tr key={h.symbol} className="border-b border-border/50 hover:bg-card-hover transition-colors group">
                                            <td className="px-6 py-4">
                                                <div className="flex items-center gap-3">
                                                    <div className="h-9 w-9 rounded-lg bg-accent/10 flex items-center justify-center text-accent font-bold text-xs group-hover:scale-110 transition-transform">
                                                        {h.symbol.slice(0, 2)}
                                                    </div>
                                                    <div>
                                                        <p className="font-semibold">{h.symbol}</p>
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

                    {/* Recent Transactions */}
                    <div className="bg-card border border-border rounded-2xl overflow-hidden">
                        <div className="px-6 py-4 border-b border-border">
                            <h2 className="text-base font-semibold">Recent Activity</h2>
                        </div>
                        <div className="p-4 space-y-3 stagger">
                            {MOCK_TRANSACTIONS.map((tx) => (
                                <div
                                    key={tx.id}
                                    className="flex items-center justify-between p-3 rounded-xl bg-background hover:bg-card-hover transition-colors"
                                >
                                    <div className="flex items-center gap-3">
                                        <div className={`h-8 w-8 rounded-lg flex items-center justify-center text-xs font-bold ${tx.type === "BUY"
                                            ? "bg-green/10 text-green"
                                            : "bg-red/10 text-red"
                                            }`}>
                                            {tx.type === "BUY" ? <ArrowUpRight size={14} /> : <ArrowDownRight size={14} />}
                                        </div>
                                        <div>
                                            <p className="text-sm font-semibold">
                                                {tx.type} {tx.symbol}
                                            </p>
                                            <p className="text-xs text-muted">{tx.date} · {tx.time}</p>
                                        </div>
                                    </div>
                                    <div className="text-right">
                                        <p className="text-sm font-mono font-semibold">
                                            {tx.shares} shares
                                        </p>
                                        <p className="text-xs text-muted font-mono">
                                            @${tx.price.toFixed(2)}
                                        </p>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </AppLayout>
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
        <div className="bg-card border border-border rounded-2xl p-5 hover:border-border-hover transition-all group relative overflow-hidden">
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
