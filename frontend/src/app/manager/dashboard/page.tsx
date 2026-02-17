"use client"

import AppLayout from "@/components/layout/AppLayout";
import { Briefcase, TrendingUp, Users, DollarSign, ArrowUpRight, ArrowDownRight, Activity } from "lucide-react";

const MOCK_AUM_BREAKDOWN = [
    { asset: "US Equities", value: 4250000, allocation: 42.5, change: 2.1 },
    { asset: "Fixed Income", value: 2800000, allocation: 28.0, change: -0.3 },
    { asset: "International", value: 1500000, allocation: 15.0, change: 1.8 },
    { asset: "Alternatives", value: 950000, allocation: 9.5, change: 3.2 },
    { asset: "Cash & Equiv.", value: 500000, allocation: 5.0, change: 0.0 },
];

const MOCK_TOP_PERFORMERS = [
    { symbol: "NVDA", client: "Portfolio A", return: 145.2 },
    { symbol: "MSFT", client: "Portfolio B", return: 32.8 },
    { symbol: "AAPL", client: "Portfolio C", return: 28.4 },
    { symbol: "GOOGL", client: "Portfolio D", return: 22.1 },
];

const MOCK_ALERTS = [
    { id: 1, type: "warning", message: "Portfolio 'Alpha Growth' approaching risk threshold", time: "2m ago" },
    { id: 2, type: "info", message: "Client John D. requests portfolio rebalance", time: "15m ago" },
    { id: 3, type: "success", message: "Q1 performance report generated", time: "1h ago" },
    { id: 4, type: "info", message: "New regulatory compliance update available", time: "2h ago" },
];

export default function ManagerDashboard() {
    const totalAUM = MOCK_AUM_BREAKDOWN.reduce((sum, a) => sum + a.value, 0);

    return (
        <AppLayout>
            <div className="p-6 lg:p-8 space-y-6 animate-fade-in">
                {/* Header */}
                <div className="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-4">
                    <div>
                        <p className="text-accent text-xs font-bold uppercase tracking-[0.2em] mb-1">Institutional Intelligence</p>
                        <h1 className="text-3xl font-bold tracking-tight mt-1">Global AUM Overview</h1>
                    </div>
                    <div className="flex items-center gap-3">
                        <div className="px-3 py-1.5 bg-card rounded-lg border border-border text-xs text-muted">
                            System Status: <span className="text-green font-bold uppercase">Optimal</span>
                        </div>
                    </div>
                </div>

                {/* Stats */}
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 stagger">
                    <AUMStatCard
                        label="Total Assets"
                        value={`$${(totalAUM / 1000000).toFixed(1)}M`}
                        sub="+8.2% vs Benchmark"
                        icon={<Briefcase size={18} />}
                        color="blue"
                    />
                    <AUMStatCard
                        label="Active Portfolios"
                        value="147"
                        sub="+12 new mandates MTD"
                        icon={<Users size={18} />}
                        color="purple"
                    />
                    <AUMStatCard
                        label="Weighted Return"
                        value="14.7%"
                        sub="Alpha: +3.5%"
                        icon={<TrendingUp size={18} />}
                        color="green"
                    />
                    <AUMStatCard
                        label="Management Fees"
                        value="$42.8K"
                        sub="Projected Q1: $135K"
                        icon={<DollarSign size={18} />}
                        color="emerald"
                    />
                </div>

                <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
                    {/* AUM Breakdown */}
                    <div className="xl:col-span-2 bg-card border border-border rounded-2xl overflow-hidden shadow-sm">
                        <div className="px-6 py-4 border-b border-border flex items-center justify-between">
                            <h2 className="text-base font-semibold">Asset Allocation</h2>
                            <span className="text-xs text-muted">{MOCK_AUM_BREAKDOWN.length} categories</span>
                        </div>
                        <div className="p-6 space-y-4 stagger">
                            {MOCK_AUM_BREAKDOWN.map((item) => (
                                <div key={item.asset} className="space-y-2">
                                    <div className="flex items-center justify-between">
                                        <div className="flex items-center gap-3">
                                            <span className="text-sm font-semibold">{item.asset}</span>
                                            <span className={`text-xs font-semibold flex items-center gap-0.5 ${item.change > 0 ? "text-green" : item.change < 0 ? "text-red" : "text-muted"
                                                }`}>
                                                {item.change > 0 ? <ArrowUpRight size={10} /> : item.change < 0 ? <ArrowDownRight size={10} /> : null}
                                                {item.change > 0 ? "+" : ""}{item.change}%
                                            </span>
                                        </div>
                                        <div className="text-right">
                                            <span className="text-sm font-mono font-semibold">
                                                ${(item.value / 1000000).toFixed(2)}M
                                            </span>
                                            <span className="text-xs text-muted ml-2">
                                                ({item.allocation}%)
                                            </span>
                                        </div>
                                    </div>
                                    <div className="w-full bg-background rounded-full h-2 overflow-hidden">
                                        <div
                                            className="h-full rounded-full bg-gradient-to-r from-accent to-blue-400 transition-all duration-700"
                                            style={{ width: `${item.allocation}%` }}
                                        />
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>

                    {/* Sidebar: Top Performers + Alerts */}
                    <div className="space-y-6">
                        {/* Risk Exposure */}
                        <div className="bg-card border border-border rounded-2xl overflow-hidden shadow-sm">
                            <div className="px-6 py-4 border-b border-border">
                                <h3 className="text-sm font-semibold flex items-center gap-2">
                                    <Activity size={14} className="text-red" />
                                    Aggregate Risk Exposure
                                </h3>
                            </div>
                            <div className="p-6 space-y-4">
                                <div className="space-y-1">
                                    <div className="flex justify-between text-[10px] font-bold uppercase tracking-wider">
                                        <span className="text-blue-400">Low Risk (VaR &lt; 2%)</span>
                                        <span>45%</span>
                                    </div>
                                    <div className="h-1.5 w-full bg-background rounded-full overflow-hidden">
                                        <div className="h-full bg-blue-400 w-[45%]" />
                                    </div>
                                </div>
                                <div className="space-y-1">
                                    <div className="flex justify-between text-[10px] font-bold uppercase tracking-wider">
                                        <span className="text-yellow-400">Moderate (VaR 2-5%)</span>
                                        <span>38%</span>
                                    </div>
                                    <div className="h-1.5 w-full bg-background rounded-full overflow-hidden">
                                        <div className="h-full bg-yellow-400 w-[38%]" />
                                    </div>
                                </div>
                                <div className="space-y-1">
                                    <div className="flex justify-between text-[10px] font-bold uppercase tracking-wider">
                                        <span className="text-red">High Risk (VaR &gt; 5%)</span>
                                        <span>17%</span>
                                    </div>
                                    <div className="h-1.5 w-full bg-background rounded-full overflow-hidden">
                                        <div className="h-full bg-red w-[17%]" />
                                    </div>
                                </div>
                            </div>
                        </div>

                        {/* Top Performers */}
                        <div className="bg-card border border-border rounded-2xl overflow-hidden shadow-sm">
                            <div className="px-6 py-4 border-b border-border">
                                <h3 className="text-sm font-semibold flex items-center gap-2">
                                    <TrendingUp size={14} className="text-green" />
                                    Mandate Alpha
                                </h3>
                            </div>
                            <div className="p-4 space-y-2 stagger">
                                {MOCK_TOP_PERFORMERS.map((p, i) => (
                                    <div
                                        key={p.symbol}
                                        className="flex items-center justify-between p-3 rounded-xl bg-background hover:bg-card-hover transition-colors"
                                    >
                                        <div className="flex items-center gap-3">
                                            <div className="h-8 w-8 rounded-lg bg-green/10 text-green flex items-center justify-center text-xs font-bold">
                                                #{i + 1}
                                            </div>
                                            <div>
                                                <p className="text-sm font-semibold">{p.symbol}</p>
                                                <p className="text-[10px] text-muted truncate max-w-[80px]">{p.client}</p>
                                            </div>
                                        </div>
                                        <span className="text-sm font-mono font-semibold text-green">
                                            +{p.return}%
                                        </span>
                                    </div>
                                ))}
                            </div>
                        </div>

                        {/* Alerts */}
                        <div className="bg-card border border-border rounded-2xl overflow-hidden shadow-sm">
                            <div className="px-6 py-4 border-b border-border">
                                <h3 className="text-sm font-semibold flex items-center gap-2">
                                    <Activity size={14} className="text-accent" />
                                    Alerts
                                </h3>
                            </div>
                            <div className="p-4 space-y-2 stagger">
                                {MOCK_ALERTS.map((alert) => {
                                    const dotColor = alert.type === "warning" ? "bg-yellow-400" :
                                        alert.type === "success" ? "bg-green" : "bg-accent";
                                    return (
                                        <div key={alert.id} className="flex gap-3 p-3 rounded-xl bg-background hover:bg-card-hover transition-colors">
                                            <div className={`h-2 w-2 rounded-full mt-1.5 shrink-0 ${dotColor}`} />
                                            <div>
                                                <p className="text-xs leading-relaxed">{alert.message}</p>
                                                <p className="text-[10px] text-muted mt-1">{alert.time}</p>
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </AppLayout>
    );
}

function AUMStatCard({ label, value, sub, icon, color }: {
    label: string; value: string; sub: string; icon: React.ReactNode; color: string;
}) {
    const colors: Record<string, string> = {
        blue: "text-blue-400 bg-blue-500/10",
        green: "text-green bg-green/10",
        purple: "text-purple-400 bg-purple-500/10",
        emerald: "text-emerald-400 bg-emerald-500/10",
    };
    return (
        <div className="bg-card border border-border rounded-2xl p-5 hover:border-border-hover transition-all group relative overflow-hidden shadow-sm">
            <div className="shimmer absolute inset-0 pointer-events-none opacity-0 group-hover:opacity-100 transition-opacity" />
            <div className="relative z-10">
                <div className="flex items-center justify-between mb-3">
                    <span className="text-xs text-muted font-medium uppercase tracking-wider">{label}</span>
                    <div className={`h-7 w-7 rounded-lg flex items-center justify-center ${colors[color]}`}>
                        {icon}
                    </div>
                </div>
                <p className="text-2xl font-bold font-mono">{value}</p>
                <p className="text-xs text-muted mt-1">{sub}</p>
            </div>
        </div>
    );
}
