"use client"

import AppLayout from "@/components/layout/AppLayout";
import { useState } from "react";
import { Search, MoreHorizontal, ArrowUpRight, ArrowDownRight, User, Filter, Plus } from "lucide-react";

const MOCK_PORTFOLIOS = [
    { id: 1, name: "Alpha Core Growth", type: "Quantitative", aum: 2450000, return: 18.4, risk: "Aggressive", status: "active", positions: 24 },
    { id: 2, name: "Market Neutral XIV", type: "Hedge Fund", aum: 1870000, return: 12.1, risk: "Moderate", status: "active", positions: 18 },
    { id: 3, name: "Global Dynamic Opp", type: "Discretionary", aum: 3210000, return: 22.7, risk: "Aggressive", status: "active", positions: 31 },
    { id: 4, name: "Fixed Income Overlay", type: "Conservative", aum: 890000, return: -2.3, risk: "Conservative", status: "review", positions: 8 },
    { id: 5, name: "Tech Momentum", type: "Thematic", aum: 1560000, return: 9.8, risk: "Moderate", status: "active", positions: 15 },
    { id: 6, name: "ESG Impact Alpha", type: "Sustainability", aum: 4120000, return: 25.3, risk: "Aggressive", status: "active", positions: 42 },
];

export default function ManagerPortfolios() {
    const [search, setSearch] = useState("");
    const [filter, setFilter] = useState("all");

    const filtered = MOCK_PORTFOLIOS
        .filter(c => c.name.toLowerCase().includes(search.toLowerCase()))
        .filter(c => filter === "all" || c.status === filter);

    const totalAUM = MOCK_PORTFOLIOS.reduce((s, c) => s + c.aum, 0);

    return (
        <AppLayout>
            <div className="p-6 lg:p-8 space-y-6 animate-fade-in">
                {/* Header */}
                <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
                    <div>
                        <p className="text-accent text-xs font-bold uppercase tracking-[0.2em] mb-1">Institutional Oversight</p>
                        <h1 className="text-3xl font-bold tracking-tight mt-1">Managed Portfolio Matrix</h1>
                    </div>
                    <button
                        onClick={() => {
                            const name = prompt("Mandate Name:");
                            if (name) alert(`Deploying Mandate: ${name}\nType: Discretionary\nFee Structure: 1.5% Mgmt / 20% Perf (HWM)`);
                        }}
                        className="flex items-center gap-2 px-4 py-2.5 bg-accent hover:bg-accent-hover text-white text-sm font-semibold rounded-xl transition-all shadow-lg shadow-accent/20"
                    >
                        <Plus size={16} />
                        Deploy Mandate
                    </button>
                </div>

                {/* Summary Cards */}
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 stagger">
                    <div className="bg-card border border-border rounded-2xl p-5">
                        <p className="text-xs text-muted uppercase tracking-wider font-medium">Total Mandates</p>
                        <p className="text-2xl font-bold font-mono mt-2">{MOCK_PORTFOLIOS.length}</p>
                    </div>
                    <div className="bg-card border border-border rounded-2xl p-5">
                        <p className="text-xs text-muted uppercase tracking-wider font-medium">Aggregate AUM</p>
                        <p className="text-2xl font-bold font-mono mt-2">${(totalAUM / 1000000).toFixed(1)}M</p>
                    </div>
                    <div className="bg-card border border-border rounded-2xl p-5">
                        <p className="text-xs text-muted uppercase tracking-wider font-medium">Risk Review</p>
                        <p className="text-2xl font-bold font-mono mt-2 text-yellow-400">
                            {MOCK_PORTFOLIOS.filter(c => c.status === "review").length}
                        </p>
                    </div>
                </div>

                {/* Search + Filter */}
                <div className="flex flex-col sm:flex-row gap-3">
                    <div className="relative flex-1">
                        <Search size={14} className="absolute left-4 top-1/2 -translate-y-1/2 text-muted" />
                        <input
                            value={search}
                            onChange={(e) => setSearch(e.target.value)}
                            className="w-full bg-card border border-border rounded-xl pl-10 pr-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all placeholder:text-muted/50"
                            placeholder="Search portfolios or strategies..."
                        />
                    </div>
                    <div className="flex gap-2">
                        {["all", "active", "review"].map(f => (
                            <button
                                key={f}
                                onClick={() => setFilter(f)}
                                className={`px-4 py-2.5 rounded-xl text-xs font-semibold capitalize transition-all border ${filter === f
                                    ? "border-accent text-accent bg-accent/5"
                                    : "border-border text-muted hover:border-border-hover hover:text-foreground"
                                    }`}
                            >
                                {f === "all" ? "All Strategies" : f}
                            </button>
                        ))}
                    </div>
                </div>

                {/* Table */}
                <div className="bg-card border border-border rounded-2xl overflow-hidden shadow-sm">
                    <div className="overflow-x-auto">
                        <table className="w-full text-sm">
                            <thead>
                                <tr className="text-left text-muted text-xs border-b border-border bg-card-hover/20">
                                    <th className="px-6 py-4 font-bold tracking-wider uppercase">Mandate Name</th>
                                    <th className="px-4 py-4 font-bold tracking-wider uppercase text-right">AUM</th>
                                    <th className="px-4 py-4 font-bold tracking-wider uppercase text-right">YTD Performance</th>
                                    <th className="px-4 py-4 font-bold tracking-wider uppercase text-center">Strategy Class</th>
                                    <th className="px-4 py-4 font-bold tracking-wider uppercase text-center">Positions</th>
                                    <th className="px-4 py-4 font-bold tracking-wider uppercase text-center">Status</th>
                                    <th className="px-6 py-4 font-bold tracking-wider uppercase text-right"></th>
                                </tr>
                            </thead>
                            <tbody className="stagger">
                                {filtered.map((portfolio) => (
                                    <tr key={portfolio.id} className="border-b border-border/50 hover:bg-card-hover/50 transition-colors">
                                        <td className="px-6 py-4">
                                            <div className="flex items-center gap-3">
                                                <div className="h-10 w-10 rounded-xl bg-accent/10 flex items-center justify-center text-accent font-bold text-xs border border-accent/20">
                                                    {portfolio.name.slice(0, 2).toUpperCase()}
                                                </div>
                                                <div>
                                                    <p className="font-semibold">{portfolio.name}</p>
                                                    <p className="text-[10px] text-muted uppercase tracking-wider">{portfolio.type}</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td className="px-4 py-4 text-right font-mono font-semibold">
                                            ${(portfolio.aum / 1000000).toFixed(2)}M
                                        </td>
                                        <td className="px-4 py-4 text-right">
                                            <span className={`inline-flex items-center gap-1 text-xs font-bold px-2.5 py-1 rounded-full ${portfolio.return >= 0
                                                ? "text-green bg-green/10"
                                                : "text-red bg-red/10"
                                                }`}>
                                                {portfolio.return >= 0 ? <ArrowUpRight size={10} /> : <ArrowDownRight size={10} />}
                                                {portfolio.return >= 0 ? "+" : ""}{portfolio.return}%
                                            </span>
                                        </td>
                                        <td className="px-4 py-4 text-center">
                                            <span className={`text-[10px] font-black uppercase tracking-widest px-3 py-1 rounded-full ${portfolio.risk === "Aggressive"
                                                ? "text-red/80 bg-red/5 border border-red/20"
                                                : portfolio.risk === "Moderate"
                                                    ? "text-yellow-400/80 bg-yellow-500/5 border border-yellow-500/20"
                                                    : "text-blue-400/80 bg-blue-500/10 border border-blue-500/20"
                                                }`}>
                                                {portfolio.risk}
                                            </span>
                                        </td>
                                        <td className="px-4 py-4 text-center font-mono text-muted text-xs">
                                            {portfolio.positions}
                                        </td>
                                        <td className="px-4 py-4 text-center">
                                            <span className={`text-[9px] font-black uppercase tracking-tighter px-2.5 py-1 rounded-md border ${portfolio.status === "active"
                                                ? "text-green bg-green/10 border-green/20"
                                                : "text-yellow-400 bg-yellow-400/10 border-yellow-400/20"
                                                }`}>
                                                {portfolio.status}
                                            </span>
                                        </td>
                                        <td className="px-6 py-4 text-right">
                                            <button className="h-8 w-8 rounded-lg hover:bg-accent/10 flex items-center justify-center text-muted hover:text-accent transition-all">
                                                <MoreHorizontal size={16} />
                                            </button>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </AppLayout>
    );
}
