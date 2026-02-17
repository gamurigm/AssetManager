"use client"

import React from 'react';
import { Treemap, ResponsiveContainer, Tooltip } from 'recharts';

interface AssetData {
    name: string;
    value: number;
    symbol: string;
    change: number;
    [key: string]: any;
}

const CustomizedContent = (props: any) => {
    const { x, y, width, height, index, symbol, value, change } = props;

    // Ultra-nuanced Heatmap: High granularity around 0%
    const getHeatmapColor = (changeValue: number) => {
        // POSITIVE SPECTRUM
        if (changeValue > 5) return '#10b981';      // Vibrant Esmerald (Moonshot)
        if (changeValue > 2.5) return '#22c55e';    // Success Green (Strong)
        if (changeValue > 1) return '#4ade80';      // Soft Green (Solid)
        if (changeValue > 0.4) return '#86efac';    // Pale Green (Positive Flat)
        if (changeValue > 0.1) return '#064e3b';    // Deep Forest (Barely Positive)

        // ABSOLUTE NEUTRAL
        if (changeValue >= -0.1 && changeValue <= 0.1) return '#374151'; // Slate Grey (Flat)

        // NEGATIVE SPECTRUM
        if (changeValue >= -0.4) return '#78350f';  // Deep Bronze (Barely Negative)
        if (changeValue >= -1.2) return '#facc15';  // Vibrant Yellow (Flat Negative)
        if (changeValue >= -2.5) return '#fbbf24';  // Amber (Moderate Dip)
        if (changeValue >= -4) return '#f97316';    // Orange/Tomate (Significant Dip)
        if (changeValue >= -6) return '#f43f5e';    // Rose (Heavy Dip)
        return '#ef4444';                           // Pure Red (Crisis)
    };

    const color = getHeatmapColor(change || 0);

    return (
        <g>
            <rect
                x={x}
                y={y}
                width={width}
                height={height}
                style={{
                    fill: color,
                    stroke: 'rgba(0,0,0,0.5)',
                    strokeWidth: 1.5,
                }}
                className="hover:brightness-125 transition-all cursor-crosshair"
            />
            {width > 40 && height > 20 && (
                <text
                    x={x + 10}
                    y={y + 26}
                    fill="#ffffff"
                    fontSize={Math.max(Math.min(width / 4, 20), 15)}
                    fontWeight="950"
                    className="select-none pointer-events-none uppercase tracking-tight drop-shadow-[0_2px_3px_rgba(0,0,0,0.8)]"
                >
                    {symbol}
                </text>
            )}
            {width > 80 && height > 60 && (
                <text
                    x={x + 10}
                    y={y + 48}
                    fill="#ffffff"
                    fillOpacity={1}
                    fontSize={14}
                    fontWeight="bold"
                    className="select-none pointer-events-none font-mono drop-shadow-[0_1px_2px_rgba(0,0,0,0.8)]"
                >
                    ${value.toLocaleString(undefined, { maximumFractionDigits: 0 })}
                </text>
            )}
        </g>
    );
};

const CustomTooltip = ({ active, payload }: any) => {
    if (active && payload && payload.length) {
        const data = payload[0].payload;
        return (
            <div className="bg-card/95 border border-border p-3 rounded-xl shadow-2xl backdrop-blur-md">
                <p className="text-[10px] font-bold text-muted uppercase tracking-widest mb-1">{data.name}</p>
                <div className="flex items-center justify-between gap-4">
                    <span className="text-foreground font-mono font-bold">${(data.value || 0).toLocaleString()}</span>
                    <span className={`text-[10px] font-bold ${(data.change || 0) >= 0 ? 'text-green' : 'text-red'}`}>
                        {(data.change || 0) >= 0 ? '+' : ''}{(data.change || 0).toFixed(2)}%
                    </span>
                </div>
            </div>
        );
    }
    return null;
};

export default function AssetTreemap({ data }: { data: AssetData[] }) {
    return (
        <div className="w-full h-full min-h-[400px] bg-background rounded-xl overflow-hidden border border-border">
            <ResponsiveContainer width="100%" height="100%">
                <Treemap
                    data={data}
                    dataKey="value"
                    aspectRatio={16 / 9}
                    stroke="rgba(0,0,0,0.5)"
                    content={<CustomizedContent />}
                >
                    <Tooltip content={<CustomTooltip />} />
                </Treemap>
            </ResponsiveContainer>
        </div>
    );
}
