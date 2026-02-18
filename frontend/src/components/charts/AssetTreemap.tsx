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
    // Adjusted palette: < 1% Yellow tones, > 1% Green tones
    const getHeatmapColor = (changeValue: number) => {
        // POSITIVE SPECTRUM (> 1%)
        if (changeValue > 5) return '#065f46';      // Dark Emerald
        if (changeValue > 2.5) return '#10b981';    // Emerald
        if (changeValue > 1) return '#4ade80';      // Light Green

        // NEUTRAL/STALE SPECTRUM (< 1% and > -1%) - Yellow/Orange tones
        if (changeValue >= 0.5) return '#fde047';   // Bright Yellow
        if (changeValue >= 0.1) return '#facc15';   // Golden Yellow
        if (changeValue > -0.1) return '#71717a';   // Grey (True Neutral)
        if (changeValue >= -0.5) return '#fbbf24';  // Amber
        if (changeValue >= -1) return '#f97316';    // Orange

        // NEGATIVE SPECTRUM (< -1%)
        if (changeValue >= -3) return '#f43f5e';    // Rose
        return '#ef4444';                           // Red (Crisis)
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
                    stroke: 'black',
                    strokeWidth: 0.5,
                }}
                className="hover:brightness-110 transition-all cursor-pointer"
            />
            {width > 40 && height > 20 && (
                <text
                    x={x + width / 2}
                    y={y + height / 2 - 2}
                    textAnchor="middle"
                    fill="#fff"
                    fontSize={Math.max(Math.min(width / 6, 24), 12)}
                    fontWeight="900"
                    className="select-none pointer-events-none drop-shadow-[0_2px_2px_rgba(0,0,0,0.8)]"
                >
                    {symbol}
                </text>
            )}
            {width > 60 && height > 40 && (
                <text
                    x={x + width / 2}
                    y={y + height / 2 + 18}
                    textAnchor="middle"
                    fill="#fff"
                    fontSize={Math.max(Math.min(width / 10, 16), 10)}
                    fontWeight="700"
                    className="select-none pointer-events-none drop-shadow-[0_1px_2px_rgba(0,0,0,0.8)]"
                >
                    {(change || 0) >= 0 ? '+' : ''}{(change || 0).toFixed(2)}%
                </text>
            )}
        </g>
    );
};

const CustomTooltip = ({ active, payload }: any) => {
    if (active && payload && payload.length) {
        const data = payload[0].payload;
        return (
            <div className="bg-slate-900 border border-slate-700 p-2 rounded shadow-lg text-white text-xs">
                <p className="font-bold">{data.symbol}</p>
                <p>Valor: ${data.value.toLocaleString()}</p>
                <p className={(data.change || 0) >= 0 ? 'text-green-400' : 'text-red-400'}>
                    Cambio: {(data.change || 0).toFixed(2)}%
                </p>
            </div>
        );
    }
    return null;
};

export default function AssetTreemap({ data }: { data: AssetData[] }) {
    const [isMounted, setIsMounted] = React.useState(false);

    React.useEffect(() => {
        setIsMounted(true);
    }, []);

    if (!isMounted) {
        return <div className="w-full h-[400px] bg-slate-900/50 rounded-xl animate-pulse" />;
    }

    return (
        <div className="w-full h-[400px] bg-background rounded-xl overflow-hidden border border-border">
            <ResponsiveContainer width="100%" height="100%">
                <Treemap
                    data={data}
                    dataKey="value"
                    aspectRatio={4 / 3}
                    stroke="#fff"
                    content={<CustomizedContent />}
                >
                    <Tooltip content={<CustomTooltip />} />
                </Treemap>
            </ResponsiveContainer>
        </div>
    );
}
