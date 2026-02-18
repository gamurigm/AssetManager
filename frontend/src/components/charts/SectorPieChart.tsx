"use client"

import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from 'recharts';

interface SectorData {
    name: string;
    value: number;
    percent: number;
    color: string;
}

const SECTOR_COLORS: Record<string, string> = {
    "Technology": "#3b82f6",     // Blue
    "Communication Services": "#8b5cf6", // Purple
    "Financials": "#10b981",    // Emerald
    "Energy": "#f59e0b",        // Amber
    "Health Care": "#ef4444",   // Red
    "Consumer Discretionary": "#ec4899", // Pink
    "Industrials": "#64748b",   // Slate
    "Digital Assets": "#06b6d4", // Cyan
    "FX / Commodities": "#f97316", // Orange
};

const CustomTooltip = ({ active, payload }: any) => {
    if (active && payload && payload.length) {
        return (
            <div className="bg-[#0f0f0f]/95 border border-white/10 p-3 rounded-xl shadow-2xl backdrop-blur-md">
                <p className="text-[10px] font-bold text-muted uppercase tracking-widest mb-1">{payload[0].name}</p>
                <p className="text-white font-mono font-bold">${payload[0].value.toLocaleString()}</p>
            </div>
        );
    }
    return null;
};

const renderCustomizedLabel = (props: any) => {
    const { cx, cy, midAngle, innerRadius, outerRadius, percent, name, value, color } = props;
    const RADIAN = Math.PI / 180;
    const labelRadius = outerRadius * 1.35;
    const x = cx + labelRadius * Math.cos(-midAngle * RADIAN);
    const y = cy + labelRadius * Math.sin(-midAngle * RADIAN);

    const displayPercent = percent < 1 ? percent * 100 : percent;

    return (
        <text
            x={x}
            y={y}
            fill={color}
            textAnchor={x > cx ? 'start' : 'end'}
            dominantBaseline="central"
            className="text-[17px] font-black uppercase tracking-tighter drop-shadow-sm" // Ultra-bold 17px
        >
            {name}
            <tspan
                x={x}
                dy="1.2em"
                className="text-[14px] font-mono font-black fill-muted-foreground opacity-100" // Stronger 14px
            >
                {`$${(value / 1000).toFixed(1)}K · ${displayPercent.toFixed(1)}%`}
            </tspan>
        </text>
    );
};

export default function SectorPieChart({ data }: { data: SectorData[] }) {
    const [isMounted, setIsMounted] = React.useState(false);

    React.useEffect(() => {
        setIsMounted(true);
    }, []);

    if (!isMounted) {
        return <div className="w-full h-[350px] bg-accent/5 rounded-xl animate-pulse" />;
    }

    return (
        <div className="flex flex-col md:flex-row items-center gap-12 w-full h-full p-6">
            {/* Pie Chart Section */}
            <div className="w-full md:w-3/5 h-[350px] relative">
                <ResponsiveContainer width="100%" height="100%" minWidth={0} minHeight={0}>
                    <PieChart>
                        <Pie
                            data={data}
                            cx="50%"
                            cy="50%"
                            innerRadius={80}
                            outerRadius={110}
                            paddingAngle={3}
                            dataKey="value"
                            label={renderCustomizedLabel}
                            labelLine={{ stroke: 'currentColor', strokeWidth: 1, opacity: 0.3 }}
                        >
                            {data.map((entry, index) => (
                                <Cell key={`cell-${index}`} fill={entry.color} stroke="rgba(0,0,0,0.3)" strokeWidth={2} />
                            ))}
                        </Pie>
                        <Tooltip content={<CustomTooltip />} />
                    </PieChart>
                </ResponsiveContainer>
                {/* Center Text - High Contrast */}
                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-center pointer-events-none">
                    <p className="text-[11px] text-foreground/60 font-black uppercase tracking-widest bg-accent/10 px-3 py-1 rounded-full border border-accent/20">Portfolio NAV</p>
                    <p className="text-3xl font-black text-foreground font-mono mt-2 drop-shadow-sm">
                        ${data.reduce((a, b) => a + b.value, 0).toLocaleString(undefined, { maximumFractionDigits: 0 })}
                    </p>
                </div>
            </div>

            {/* Legend Section - Refined for Clarity */}
            <div className="flex-1 w-full space-y-4">
                <div className="flex items-center justify-between px-3 pb-2 border-b border-border mx-2">
                    <span className="text-[11px] font-bold uppercase tracking-[0.1em] text-muted-foreground">Business Sector</span>
                    <span className="text-[11px] font-bold uppercase tracking-[0.1em] text-muted-foreground">Weight %</span>
                </div>
                <div className="max-h-[280px] overflow-y-auto px-2 custom-scrollbar">
                    {data.sort((a, b) => b.value - a.value).map((item, index) => (
                        <div key={index} className="flex items-center justify-between py-2.5 px-3 hover:bg-accent/5 rounded-xl transition-all group">
                            <div className="flex items-center gap-4">
                                <div className="w-3 h-3 rounded-full shadow-sm transition-transform group-hover:scale-110" style={{ backgroundColor: item.color }} />
                                <span className="text-[14px] font-bold text-foreground/90 group-hover:text-foreground transition-colors">{item.name}</span>
                            </div>
                            <span className="text-[14px] font-mono font-bold text-accent">{item.percent.toFixed(1)}%</span>
                        </div>
                    ))}
                </div>
                <div className="mx-2 pt-4 border-t border-border flex justify-between items-center px-3">
                    <span className="text-[12px] font-bold text-foreground uppercase tracking-tight opacity-80">Active Exposure</span>
                    <span className="text-[14px] font-bold text-accent font-mono">100.0%</span>
                </div>
            </div>
        </div>
    );
}
