"use client"

import React from 'react';
import { Treemap, ResponsiveContainer, Tooltip } from 'recharts';

interface AssetData {
    name: string;
    value: number;
    symbol: string;
    change: number;
}

const COLORS = [
    '#3b82f6', // blue
    '#10b981', // emerald
    '#8b5cf6', // purple
    '#f59e0b', // amber
    '#ef4444', // red
    '#06b6d4', // cyan
    '#ec4899', // pink
];

const CustomizedContent = (props: any) => {
    const { root, depth, x, y, width, height, index, name, value, symbol, change } = props;

    if (depth !== 1) return null;

    return (
        <g>
            <rect
                x={x}
                y={y}
                width={width}
                height={height}
                style={{
                    fill: COLORS[index % COLORS.length],
                    stroke: '#000',
                    strokeWidth: 2 / (depth + 1),
                    strokeOpacity: 1 / (depth + 1),
                    fillOpacity: 0.8,
                }}
            />
            {width > 50 && height > 30 && (
                <text
                    x={x + width / 2}
                    y={y + height / 2 - 5}
                    textAnchor="middle"
                    fill="#fff"
                    fontSize={Math.min(width / 6, 12)}
                    fontWeight="bold"
                    className="select-none pointer-events-none uppercase tracking-tighter"
                >
                    {symbol}
                </text>
            )}
            {width > 50 && height > 45 && (
                <text
                    x={x + width / 2}
                    y={y + height / 2 + 12}
                    textAnchor="middle"
                    fill="#fff"
                    fillOpacity={0.7}
                    fontSize={Math.min(width / 10, 10)}
                    className="select-none pointer-events-none font-mono"
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
            <div className="bg-[#0f0f0f]/95 border border-white/10 p-3 rounded-xl shadow-2xl backdrop-blur-md">
                <p className="text-[10px] font-bold text-accent uppercase tracking-widest mb-1">{data.name}</p>
                <div className="flex items-center justify-between gap-4">
                    <span className="text-white font-mono font-bold">${(data.value || 0).toLocaleString()}</span>
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
    // Recharts Treemap expects a children structure for better coloring/nesting
    const treeData = [
        {
            name: 'Portfolio',
            children: data
        }
    ];

    return (
        <div className="w-full h-full min-h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
                <Treemap
                    data={treeData}
                    dataKey="value"
                    aspectRatio={4 / 3}
                    stroke="#000"
                    content={<CustomizedContent />}
                >
                    <Tooltip content={<CustomTooltip />} />
                </Treemap>
            </ResponsiveContainer>
        </div>
    );
}
