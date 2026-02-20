"use client"

import AppLayout from "@/components/layout/AppLayout";
import { useState } from "react";
import { Search, MoreHorizontal, Activity, Cpu, Play, Plus, ServerCog } from "lucide-react";

const STRATEGIES = [
    {
        id: 1,
        name: "ORB FVG Engulfing M5 M1",
        type: "Quantitative Scalping",
        status: "Active (C++ / Rust Core)",
        accuracy: "98.5% (High Freq)",
        winRate: "72.4%",
        latency: "<2ms"
    }
];

export default function StrategiesPage() {
    const [search, setSearch] = useState("");

    const filtered = STRATEGIES.filter(s => s.name.toLowerCase().includes(search.toLowerCase()));

    return (
        <AppLayout>
            <div className="p-6 lg:p-8 space-y-6 animate-fade-in">
                {/* Header */}
                <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
                    <div>
                        <p className="text-accent text-xs font-bold uppercase tracking-[0.2em] mb-1">Strategy Engine Nexus</p>
                        <h1 className="text-3xl font-bold tracking-tight mt-1">Algorithmic Strategies</h1>
                    </div>
                    <button
                        onClick={() => alert(`New Strategy Builder coming soon.\nCurrently running native C++ and Rust compiled engines.`)}
                        className="flex items-center gap-2 px-4 py-2.5 bg-accent hover:bg-accent-hover text-white text-sm font-semibold rounded-xl transition-all shadow-lg shadow-accent/20"
                    >
                        <Plus size={16} />
                        Deploy New Engine
                    </button>
                </div>

                {/* Summary Cards */}
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 stagger">
                    <div className="bg-card border border-border rounded-2xl p-5 relative overflow-hidden">
                        <Cpu className="absolute -right-4 -bottom-4 text-border opacity-20" size={100} />
                        <p className="text-xs text-muted uppercase tracking-wider font-medium">Active Agents</p>
                        <p className="text-2xl font-bold font-mono mt-2">{STRATEGIES.length}</p>
                    </div>
                    <div className="bg-card border border-border rounded-2xl p-5 relative overflow-hidden">
                        <Activity className="absolute -right-4 -bottom-4 text-green/20" size={100} />
                        <p className="text-xs text-muted uppercase tracking-wider font-medium">Avg Win Rate (Sim)</p>
                        <p className="text-2xl font-bold font-mono mt-2 text-green">72.4%</p>
                    </div>
                    <div className="bg-card border border-border rounded-2xl p-5 relative overflow-hidden">
                        <ServerCog className="absolute -right-4 -bottom-4 text-accent/20 opacity-20" size={100} />
                        <p className="text-xs text-muted uppercase tracking-wider font-medium">Core Engine</p>
                        <p className="text-2xl font-bold font-mono mt-2 text-accent">C++ / Rust</p>
                    </div>
                </div>

                {/* Search */}
                <div className="relative w-full md:w-1/2">
                    <Search size={14} className="absolute left-4 top-1/2 -translate-y-1/2 text-muted" />
                    <input
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                        className="w-full bg-card border border-border rounded-xl pl-10 pr-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all placeholder:text-muted/50"
                        placeholder="Search deployed strategies..."
                    />
                </div>

                {/* Table */}
                <div className="bg-card border border-border rounded-2xl overflow-hidden shadow-sm">
                    <div className="overflow-x-auto">
                        <table className="w-full text-sm">
                            <thead>
                                <tr className="text-left text-muted text-xs border-b border-border bg-card-hover/20">
                                    <th className="px-6 py-4 font-bold tracking-wider uppercase">Strategy Kernel</th>
                                    <th className="px-4 py-4 font-bold tracking-wider uppercase text-center">Class</th>
                                    <th className="px-4 py-4 font-bold tracking-wider uppercase text-center">Engine Latency</th>
                                    <th className="px-4 py-4 font-bold tracking-wider uppercase text-center">Expected WR</th>
                                    <th className="px-4 py-4 font-bold tracking-wider uppercase text-center">Status</th>
                                    <th className="px-6 py-4 font-bold tracking-wider uppercase text-right">Actions</th>
                                </tr>
                            </thead>
                            <tbody className="stagger">
                                {filtered.map((strategy) => (
                                    <tr key={strategy.id} className="border-b border-border/50 hover:bg-card-hover/50 transition-colors">
                                        <td className="px-6 py-4">
                                            <div className="flex items-center gap-3">
                                                <div className="h-10 w-10 flex-shrink-0 rounded-xl bg-accent/10 flex items-center justify-center text-accent font-bold text-xs border border-accent/20">
                                                    <Cpu size={18} />
                                                </div>
                                                <div>
                                                    <p className="font-semibold">{strategy.name}</p>
                                                    <div className="flex items-center gap-1.5 mt-0.5">
                                                        <span className="h-1.5 w-1.5 rounded-full bg-green animate-pulse" />
                                                        <p className="text-[10px] text-muted uppercase tracking-wider">Fix8 / Jesse-Rust Linked</p>
                                                    </div>
                                                </div>
                                            </div>
                                        </td>
                                        <td className="px-4 py-4 text-center">
                                            <span className="text-[10px] font-black uppercase tracking-widest px-3 py-1 rounded-full text-blue-400/80 bg-blue-500/10 border border-blue-500/20">
                                                {strategy.type}
                                            </span>
                                        </td>
                                        <td className="px-4 py-4 text-center font-mono font-bold text-green">
                                            {strategy.latency}
                                        </td>
                                        <td className="px-4 py-4 text-center font-mono text-muted text-xs">
                                            {strategy.winRate}
                                        </td>
                                        <td className="px-4 py-4 text-center">
                                            <span className="text-[9px] font-black uppercase tracking-tighter px-2.5 py-1 rounded-md border text-green bg-green/10 border-green/20">
                                                {strategy.status}
                                            </span>
                                        </td>
                                        <td className="px-6 py-4 text-right">
                                            <div className="flex items-center justify-end gap-2">
                                                <button
                                                    onClick={() => window.location.href = '/client/trading'}
                                                    className="h-8 w-8 rounded-lg bg-accent/10 hover:bg-accent/20 flex items-center justify-center text-accent transition-all"
                                                    title="Run Backtest"
                                                >
                                                    <Play size={14} />
                                                </button>
                                                <button className="h-8 w-8 rounded-lg hover:bg-card-hover flex items-center justify-center text-muted transition-all">
                                                    <MoreHorizontal size={16} />
                                                </button>
                                            </div>
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
