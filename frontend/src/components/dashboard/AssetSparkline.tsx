"use client";

import React, { useEffect, useState } from "react";
import { LineChart, Line, ResponsiveContainer, YAxis } from "recharts";

const sparklineCache: Record<string, any[]> = {};

interface AssetSparklineProps {
    symbol: string;
    color: string;
}

const AssetSparkline = React.memo(({ symbol, color }: AssetSparklineProps) => {
    const [data, setData] = useState<any[]>(sparklineCache[symbol] || []);

    useEffect(() => {
        if (sparklineCache[symbol]?.length > 0) return;
        let isMounted = true;
        fetch(`http://127.0.0.1:8282/api/v1/market/historical/${encodeURIComponent(symbol)}?limit=60`)
            .then(r => r.json())
            .then(d => {
                if (!isMounted) return;
                if (d.historical && d.historical.length > 0) {
                    const finalData = d.historical
                        .sort((a: any, b: any) => a.date.localeCompare(b.date))
                        .map((p: any) => ({ v: p.close }));
                    sparklineCache[symbol] = finalData;
                    setData(finalData);
                }
            })
            .catch(() => { });
        return () => { isMounted = false; };
    }, [symbol]);

    return (
        <div className="h-8 w-24 ml-auto">
            {data.length > 0 ? (
                <ResponsiveContainer width="100%" height="100%">
                    <LineChart data={data}>
                        <YAxis domain={['dataMin', 'dataMax']} hide />
                        <Line type="monotone" dataKey="v" stroke={color} strokeWidth={1.5} dot={false} isAnimationActive={false} />
                    </LineChart>
                </ResponsiveContainer>
            ) : (
                <div className="h-full w-full flex items-center justify-end">
                    <div className="h-1 w-8 bg-border/50 rounded animate-pulse" />
                </div>
            )}
        </div>
    );
});

AssetSparkline.displayName = "AssetSparkline";

export default AssetSparkline;
