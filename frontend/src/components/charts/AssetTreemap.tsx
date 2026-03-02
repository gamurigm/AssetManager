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

    const getHeatmapColor = (changeValue: number) => {
        if (changeValue >= 2.5) return '#30cc5a';         // +3% (Bright Green)
        if (changeValue >= 1.5) return '#2bb05b';         // +2% (Medium Green)
        if (changeValue > 0.2) return '#35764e';          // +1% (Dark Green)
        if (changeValue > -0.2 && changeValue <= 0.2) return '#414554'; // 0% (Neutral Grey)
        if (changeValue > -1.5) return '#8b444e';         // -1% (Dark Red)
        if (changeValue > -2.5) return '#bf4045';         // -2% (Medium Red)
        return '#f63538';                                 // -3% (Bright Red)
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
                    fontWeight="700"
                    className="select-none pointer-events-none drop-shadow-md"
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
                    fontWeight="500"
                    className="select-none pointer-events-none drop-shadow-sm"
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
            <div className="dark:bg-[#0f0f0f]/95 bg-white border dark:border-white/10 border-zinc-200 p-3 rounded-xl shadow-2xl backdrop-blur-md">
                <p className="text-[10px] font-bold text-muted uppercase tracking-widest mb-1">{data.symbol}</p>
                <p className="dark:text-white text-zinc-900 font-mono font-bold">Value: ${data.value.toLocaleString()}</p>
                <p className={`text-[11px] font-black ${(data.change || 0) >= 0 ? 'text-green' : 'text-red'}`}>
                    Delta: {(data.change || 0).toFixed(2)}%
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
