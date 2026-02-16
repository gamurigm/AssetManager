"use client"

import AppLayout from "@/components/layout/AppLayout";
import { useState } from "react";
import { Search, MoreHorizontal, ArrowUpRight, ArrowDownRight, User, Filter, Plus } from "lucide-react";

const MOCK_CLIENTS = [
    { id: 1, name: "Alexander Hamilton", email: "alex.h@email.com", aum: 2450000, return: 18.4, risk: "Aggressive", status: "active", positions: 24 },
    { id: 2, name: "Benjamin Franklin", email: "ben.f@email.com", aum: 1870000, return: 12.1, risk: "Moderate", status: "active", positions: 18 },
    { id: 3, name: "Catherine Johnson", email: "cat.j@email.com", aum: 3210000, return: 22.7, risk: "Aggressive", status: "active", positions: 31 },
    { id: 4, name: "David Chen", email: "david.c@email.com", aum: 890000, return: -2.3, risk: "Conservative", status: "review", positions: 8 },
    { id: 5, name: "Elena Martinez", email: "elena.m@email.com", aum: 1560000, return: 9.8, risk: "Moderate", status: "active", positions: 15 },
    { id: 6, name: "Frank Williams", email: "frank.w@email.com", aum: 4120000, return: 25.3, risk: "Aggressive", status: "active", positions: 42 },
    { id: 7, name: "Grace Lee", email: "grace.l@email.com", aum: 720000, return: 5.1, risk: "Conservative", status: "active", positions: 6 },
    { id: 8, name: "Henry Thompson", email: "henry.t@email.com", aum: 2080000, return: -0.8, risk: "Moderate", status: "review", positions: 20 },
];

export default function ManagerClients() {
    const [search, setSearch] = useState("");
    const [filter, setFilter] = useState("all");

    const filtered = MOCK_CLIENTS
        .filter(c => c.name.toLowerCase().includes(search.toLowerCase()) || c.email.toLowerCase().includes(search.toLowerCase()))
        .filter(c => filter === "all" || c.status === filter);

    const totalAUM = MOCK_CLIENTS.reduce((s, c) => s + c.aum, 0);

    return (
        <AppLayout>
            <div className="p-6 lg:p-8 space-y-6 animate-fade-in">
                {/* Header */}
                <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
                    <div>
                        <p className="text-muted text-sm font-medium">Asset Manager</p>
                        <h1 className="text-3xl font-bold tracking-tight mt-1">Client Management</h1>
                    </div>
                    <button className="flex items-center gap-2 px-4 py-2.5 bg-accent hover:bg-accent-hover text-white text-sm font-semibold rounded-xl transition-all shadow-lg shadow-accent/20">
                        <Plus size={16} />
                        Add Client
                    </button>
                </div>

                {/* Summary Cards */}
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 stagger">
                    <div className="bg-card border border-border rounded-2xl p-5">
                        <p className="text-xs text-muted uppercase tracking-wider font-medium">Total Clients</p>
                        <p className="text-2xl font-bold font-mono mt-2">{MOCK_CLIENTS.length}</p>
                    </div>
                    <div className="bg-card border border-border rounded-2xl p-5">
                        <p className="text-xs text-muted uppercase tracking-wider font-medium">Combined AUM</p>
                        <p className="text-2xl font-bold font-mono mt-2">${(totalAUM / 1000000).toFixed(1)}M</p>
                    </div>
                    <div className="bg-card border border-border rounded-2xl p-5">
                        <p className="text-xs text-muted uppercase tracking-wider font-medium">Needs Review</p>
                        <p className="text-2xl font-bold font-mono mt-2 text-yellow-400">
                            {MOCK_CLIENTS.filter(c => c.status === "review").length}
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
                            placeholder="Search clients..."
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
                                {f === "all" ? "All" : f}
                            </button>
                        ))}
                    </div>
                </div>

                {/* Clients Table */}
                <div className="bg-card border border-border rounded-2xl overflow-hidden">
                    <div className="overflow-x-auto">
                        <table className="w-full text-sm">
                            <thead>
                                <tr className="text-left text-muted text-xs border-b border-border">
                                    <th className="px-6 py-3.5 font-medium">Client</th>
                                    <th className="px-4 py-3.5 font-medium text-right">AUM</th>
                                    <th className="px-4 py-3.5 font-medium text-right">Return</th>
                                    <th className="px-4 py-3.5 font-medium text-center">Risk Profile</th>
                                    <th className="px-4 py-3.5 font-medium text-center">Positions</th>
                                    <th className="px-4 py-3.5 font-medium text-center">Status</th>
                                    <th className="px-6 py-3.5 font-medium text-right"></th>
                                </tr>
                            </thead>
                            <tbody className="stagger">
                                {filtered.map((client) => (
                                    <tr key={client.id} className="border-b border-border/50 hover:bg-card-hover transition-colors">
                                        <td className="px-6 py-4">
                                            <div className="flex items-center gap-3">
                                                <div className="h-10 w-10 rounded-full bg-gradient-to-br from-accent/20 to-purple-500/20 flex items-center justify-center text-accent font-bold text-xs">
                                                    {client.name.split(" ").map(n => n[0]).join("")}
                                                </div>
                                                <div>
                                                    <p className="font-semibold">{client.name}</p>
                                                    <p className="text-xs text-muted">{client.email}</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td className="px-4 py-4 text-right font-mono font-semibold">
                                            ${(client.aum / 1000000).toFixed(2)}M
                                        </td>
                                        <td className="px-4 py-4 text-right">
                                            <span className={`inline-flex items-center gap-1 text-xs font-semibold px-2 py-1 rounded-md ${client.return >= 0
                                                    ? "text-green bg-green/10"
                                                    : "text-red bg-red/10"
                                                }`}>
                                                {client.return >= 0 ? <ArrowUpRight size={10} /> : <ArrowDownRight size={10} />}
                                                {client.return >= 0 ? "+" : ""}{client.return}%
                                            </span>
                                        </td>
                                        <td className="px-4 py-4 text-center">
                                            <span className={`text-xs font-semibold px-3 py-1 rounded-full ${client.risk === "Aggressive"
                                                    ? "text-red/80 bg-red/5 border border-red/10"
                                                    : client.risk === "Moderate"
                                                        ? "text-yellow-400/80 bg-yellow-500/5 border border-yellow-500/10"
                                                        : "text-blue-400/80 bg-blue-500/5 border border-blue-500/10"
                                                }`}>
                                                {client.risk}
                                            </span>
                                        </td>
                                        <td className="px-4 py-4 text-center font-mono text-muted">
                                            {client.positions}
                                        </td>
                                        <td className="px-4 py-4 text-center">
                                            <span className={`text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full ${client.status === "active"
                                                    ? "text-green bg-green/10"
                                                    : "text-yellow-400 bg-yellow-500/10"
                                                }`}>
                                                {client.status}
                                            </span>
                                        </td>
                                        <td className="px-6 py-4 text-right">
                                            <button className="h-8 w-8 rounded-lg hover:bg-card flex items-center justify-center text-muted hover:text-foreground transition-all">
                                                <MoreHorizontal size={16} />
                                            </button>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                    {filtered.length === 0 && (
                        <div className="p-12 text-center text-muted text-sm">
                            No clients found matching your search.
                        </div>
                    )}
                </div>
            </div>
        </AppLayout>
    );
}
