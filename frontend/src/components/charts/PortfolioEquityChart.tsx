"use client"

import React, { useEffect, useState, useCallback, useMemo } from "react";
import {
    AreaChart,
    Area,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer,
    Brush,
    ReferenceLine,
} from "recharts";

interface EquityPoint {
    time: number;
    realized: number;
    total: number;
    pnl: number;
}

export default function PortfolioEquityChart() {
    const [data, setData] = useState<EquityPoint[]>([]);
    const [loading, setLoading] = useState(true);
    const [brushRange, setBrushRange] = useState<{ startIndex: number; endIndex: number } | null>(null);

    useEffect(() => {
        const fetchHistory = async () => {
            try {
                const res = await fetch("http://127.0.0.1:8282/api/v1/portfolios/history");
                const json = await res.json();
                if (Array.isArray(json)) {
                    const baseRealized = json[0]?.realized || 0;
                    const enriched = json.map(pt => ({
                        ...pt,
                        pnl: pt.realized - baseRealized
                    }));
                    setData(enriched);
                }
            } catch (err) {
                console.error("Failed to fetch equity history:", err);
            } finally {
                setLoading(false);
            }
        };
        fetchHistory();
    }, []);

    const handleBrushChange = useCallback((range: any) => {
        if (range && typeof range.startIndex === 'number') {
            setBrushRange({ startIndex: range.startIndex, endIndex: range.endIndex });
        }
    }, []);

    // Derive the visible slice of data for the sub-chart
    const visibleData = useMemo(() => {
        if (!brushRange || data.length === 0) return data;
        return data.slice(brushRange.startIndex, brushRange.endIndex + 1);
    }, [data, brushRange]);

    const formatXAxis = (tick: number) => {
        const date = new Date(tick * 1000);
        return date.toLocaleDateString("en-US", { month: "short", day: "numeric" });
    };

    const CustomTooltip = ({ active, payload, label }: any) => {
        if (active && payload && payload.length) {
            const date = new Date(label * 1000).toLocaleDateString("en-US", {
                year: "numeric",
                month: "long",
                day: "numeric",
            });
            return (
                <div className="bg-zinc-950/90 border border-white/10 p-4 rounded-xl shadow-2xl backdrop-blur-md">
                    <p className="text-[10px] text-zinc-500 font-black uppercase tracking-widest mb-2 border-b border-white/5 pb-1">
                        {date}
                    </p>
                    <div className="flex flex-col gap-1">
                        <div className="flex items-center justify-between gap-8">
                            <span className="text-xs font-bold text-cyan-400">Total Equity</span>
                            <span className="text-xs font-black text-white">
                                ${payload[0]?.value?.toLocaleString() ?? '—'}
                            </span>
                        </div>
                        <div className="flex items-center justify-between gap-8">
                            <span className="text-xs font-bold text-zinc-400">Realized Balance</span>
                            <span className="text-xs font-black text-zinc-100">
                                ${payload[1]?.value?.toLocaleString() ?? '—'}
                            </span>
                        </div>
                        <div className="mt-2 pt-2 border-t border-white/5">
                            <span className="text-[9px] font-black uppercase text-zinc-500">Unrealized P&L: </span>
                            <span className={`text-[9px] font-black ${(payload[0]?.value - payload[1]?.value) >= 0 ? "text-green" : "text-red"}`}>
                                ${((payload[0]?.value ?? 0) - (payload[1]?.value ?? 0)).toLocaleString()}
                            </span>
                        </div>
                    </div>
                </div>
            );
        }
        return null;
    };

    if (loading) {
        return (
            <div className="h-full w-full flex flex-col items-center justify-center gap-4">
                <div className="h-8 w-8 border-2 border-accent border-t-transparent rounded-full animate-spin" />
                <span className="text-[10px] text-muted font-black uppercase tracking-widest animate-pulse">
                    Computing NAV Histories...
                </span>
            </div>
        );
    }

    // Compute pnl domain for zero-line
    const pnlValues = visibleData.map(d => d.pnl);
    const hasPnlData = pnlValues.length > 0 && pnlValues.some(v => v !== 0);

    return (
        <div className="h-full w-full p-2 flex flex-col">
            {/* ── MAIN NAV CHART ── */}
            <div className="flex-1 min-h-0 relative">
                <ResponsiveContainer width="100%" height="100%">
                    <AreaChart data={data} margin={{ top: 10, right: 10, left: 10, bottom: 0 }} syncId="portfolio-nav">
                        <defs>
                            <linearGradient id="colorTotal" x1="0" y1="0" x2="0" y2="1">
                                <stop offset="5%" stopColor="#22d3ee" stopOpacity={0.3} />
                                <stop offset="95%" stopColor="#22d3ee" stopOpacity={0} />
                            </linearGradient>
                            <linearGradient id="colorRealized" x1="0" y1="0" x2="0" y2="1">
                                <stop offset="5%" stopColor="#71717a" stopOpacity={0.2} />
                                <stop offset="95%" stopColor="#71717a" stopOpacity={0} />
                            </linearGradient>
                        </defs>
                        <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="rgba(255,255,255,0.05)" />
                        <XAxis
                            dataKey="time"
                            tickFormatter={formatXAxis}
                            axisLine={false}
                            tickLine={false}
                            tick={{ fontSize: 10, fill: "#71717a", fontWeight: "bold" }}
                            minTickGap={30}
                        />
                        <YAxis
                            hide
                            domain={["auto", "auto"]}
                        />
                        <Tooltip content={<CustomTooltip />} />
                        <Area
                            type="monotone"
                            dataKey="total"
                            stroke="#22d3ee"
                            strokeWidth={3}
                            fillOpacity={1}
                            fill="url(#colorTotal)"
                            isAnimationActive={true}
                            animationDuration={1500}
                        />
                        <Area
                            type="monotone"
                            dataKey="realized"
                            stroke="#71717a"
                            strokeWidth={2}
                            strokeDasharray="5 5"
                            fillOpacity={1}
                            fill="url(#colorRealized)"
                            isAnimationActive={true}
                        />
                        {/* Brush for zoom — syncs both charts */}
                        <Brush
                            dataKey="time"
                            height={20}
                            stroke="#22d3ee40"
                            fill="#0a0a0a"
                            tickFormatter={formatXAxis}
                            onChange={handleBrushChange}
                        />
                    </AreaChart>
                </ResponsiveContainer>
            </div>

            {/* ── LOGARITHMIC REALIZED PNL (Lower Ribbon) ── aligned with the same syncId */}
            <div className="flex-shrink-0 mt-2 pt-2 border-t border-border/40 h-[110px] flex flex-col">
                <div className="mb-1 flex items-center justify-between">
                    <span className="text-[10px] font-black uppercase tracking-widest text-[#a855f7]">Logarithmic Realized P&L</span>
                </div>
                <ResponsiveContainer width="100%" height="100%">
                    <AreaChart data={data} margin={{ top: 0, right: 10, left: 10, bottom: 0 }} syncId="portfolio-nav">
                        <defs>
                            <linearGradient id="colorPnl" x1="0" y1="0" x2="0" y2="1">
                                <stop offset="5%" stopColor="#a855f7" stopOpacity={0.4} />
                                <stop offset="95%" stopColor="#a855f7" stopOpacity={0} />
                            </linearGradient>
                        </defs>
                        <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="rgba(255,255,255,0.03)" />
                        <XAxis
                            dataKey="time"
                            tickFormatter={formatXAxis}
                            axisLine={false}
                            tickLine={false}
                            tick={{ fontSize: 9, fill: "#52525b", fontWeight: "bold" }}
                            minTickGap={50}
                        />
                        <YAxis scale="symlog" hide domain={["auto", "auto"]} />
                        {/* Zero reference line */}
                        {hasPnlData && <ReferenceLine y={0} stroke="#71717a40" strokeDasharray="3 3" />}
                        <Tooltip content={({ active, payload, label }: any) => {
                            if (active && payload && payload.length) {
                                const date = new Date(label * 1000).toLocaleDateString("en-US", { month: "short", day: "numeric" });
                                const val = payload[0].value;
                                return (
                                    <div className="bg-zinc-950/90 border border-[#a855f7]/20 p-2 rounded shadow-xl">
                                        <div className="text-[9px] text-zinc-500 uppercase">{date}</div>
                                        <div className={`text-xs font-black ${val >= 0 ? "text-[#a855f7]" : "text-red"}`}>
                                            {val >= 0 ? "+" : ""}${val.toLocaleString(undefined, { maximumFractionDigits: 0 })}
                                        </div>
                                    </div>
                                );
                            }
                            return null;
                        }} />
                        <Area
                            type="monotone"
                            dataKey="pnl"
                            stroke="#a855f7"
                            strokeWidth={2}
                            fillOpacity={1}
                            fill="url(#colorPnl)"
                            isAnimationActive={true}
                            animationDuration={1500}
                        />
                    </AreaChart>
                </ResponsiveContainer>
            </div>
        </div>
    );

}
