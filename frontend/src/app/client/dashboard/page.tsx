"use client"

import AppLayout from "@/components/layout/AppLayout";
import { useEffect, useState } from "react";
import { TrendingUp, TrendingDown, DollarSign, BarChart3, ArrowUpRight, ArrowDownRight } from "lucide-react";

const MOCK_HOLDINGS = [
    { symbol: "AAPL", name: "Apple Inc.", shares: 45, price: 178.72, change: 2.34, changePercent: 1.32 },
    { symbol: "MSFT", name: "Microsoft Corp.", shares: 30, price: 415.60, change: -1.20, changePercent: -0.29 },
    { symbol: "GOOGL", name: "Alphabet Inc.", shares: 12, price: 173.98, change: 3.15, changePercent: 1.84 },
    { symbol: "NVDA", name: "NVIDIA Corp.", shares: 20, price: 875.28, change: 15.40, changePercent: 1.79 },
    { symbol: "AMZN", name: "Amazon.com Inc.", shares: 25, price: 185.07, change: -0.93, changePercent: -0.50 },
    { symbol: "TSLA", name: "Tesla Inc.", shares: 15, price: 248.42, change: 5.16, changePercent: 2.12 },
];

const MOCK_TRANSACTIONS = [
    { id: 1, type: "BUY", symbol: "NVDA", shares: 5, price: 860.00, date: "2026-02-16", time: "10:32 AM" },
    { id: 2, type: "SELL", symbol: "AAPL", shares: 10, price: 176.50, date: "2026-02-15", time: "3:45 PM" },
    { id: 3, type: "BUY", symbol: "GOOGL", shares: 8, price: 170.85, date: "2026-02-14", time: "11:15 AM" },
    { id: 4, type: "BUY", symbol: "MSFT", shares: 5, price: 417.20, date: "2026-02-13", time: "9:50 AM" },
];

export default function ClientDashboard() {
    const totalValue = MOCK_HOLDINGS.reduce((sum, h) => sum + h.shares * h.price, 0);
    const totalPnL = MOCK_HOLDINGS.reduce((sum, h) => sum + h.shares * h.change, 0);
    const pnlPercent = (totalPnL / (totalValue - totalPnL)) * 100;

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
                        <span className="flex h-2 w-2 rounded-full bg-green animate-pulse" />
                        <span className="text-xs text-muted font-medium">Markets Open</span>
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
                        value={MOCK_HOLDINGS.length.toString()}
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
                    <div className="xl:col-span-2 bg-card border border-border rounded-2xl overflow-hidden">
                        <div className="px-6 py-4 border-b border-border flex items-center justify-between">
                            <h2 className="text-base font-semibold">Holdings</h2>
                            <span className="text-xs text-muted">{MOCK_HOLDINGS.length} positions</span>
                        </div>
                        <div className="overflow-x-auto">
                            <table className="w-full text-sm">
                                <thead>
                                    <tr className="text-left text-muted text-xs border-b border-border">
                                        <th className="px-6 py-3 font-medium">Asset</th>
                                        <th className="px-4 py-3 font-medium text-right">Shares</th>
                                        <th className="px-4 py-3 font-medium text-right">Price</th>
                                        <th className="px-4 py-3 font-medium text-right">Value</th>
                                        <th className="px-6 py-3 font-medium text-right">Change</th>
                                    </tr>
                                </thead>
                                <tbody className="stagger">
                                    {MOCK_HOLDINGS.map((h) => (
                                        <tr key={h.symbol} className="border-b border-border/50 hover:bg-card-hover transition-colors">
                                            <td className="px-6 py-4">
                                                <div className="flex items-center gap-3">
                                                    <div className="h-9 w-9 rounded-lg bg-accent/10 flex items-center justify-center text-accent font-bold text-xs">
                                                        {h.symbol.slice(0, 2)}
                                                    </div>
                                                    <div>
                                                        <p className="font-semibold">{h.symbol}</p>
                                                        <p className="text-xs text-muted">{h.name}</p>
                                                    </div>
                                                </div>
                                            </td>
                                            <td className="px-4 py-4 text-right font-mono">{h.shares}</td>
                                            <td className="px-4 py-4 text-right font-mono">${h.price.toFixed(2)}</td>
                                            <td className="px-4 py-4 text-right font-mono font-semibold">
                                                ${(h.shares * h.price).toLocaleString("en-US", { minimumFractionDigits: 2 })}
                                            </td>
                                            <td className="px-6 py-4 text-right">
                                                <div className={`inline-flex items-center gap-1 text-xs font-semibold px-2 py-1 rounded-md ${h.change >= 0
                                                        ? "text-green bg-green/10"
                                                        : "text-red bg-red/10"
                                                    }`}>
                                                    {h.change >= 0 ? <ArrowUpRight size={12} /> : <ArrowDownRight size={12} />}
                                                    {h.changePercent >= 0 ? "+" : ""}{h.changePercent.toFixed(2)}%
                                                </div>
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
