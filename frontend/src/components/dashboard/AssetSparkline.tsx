"use client";

import React, { useEffect, useState } from "react";
import { LineChart, Line, ResponsiveContainer, YAxis, ReferenceLine } from "recharts";
import { useSocket } from "@/context/SocketContext";
import { formatAssetPriceFixed } from "@/lib/marketFormatting";

const sparklineCache: Record<string, any[]> = {};

interface AssetSparklineProps {
    symbol: string;
    color: string;
    entryPrice?: number;
}

const AssetSparkline = React.memo(({ symbol, color, entryPrice }: AssetSparklineProps) => {
    const [data, setData] = useState<any[]>(sparklineCache[symbol] || []);
    const { socket, connected } = useSocket();

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

    useEffect(() => {
        if (!socket || !connected || !symbol) return;

        socket.emit("join_symbol", symbol);

        const onPriceUpdate = (payload: any) => {
            if (String(payload?.symbol || "").toUpperCase() !== symbol.toUpperCase()) return;
            if (typeof payload?.price !== "number") return;

            setData(prev => {
                const next = prev.length > 0
                    ? [...prev.slice(0, -1), { v: payload.price }]
                    : [{ v: payload.price }];
                sparklineCache[symbol] = next;
                return next;
            });
        };

        socket.on("price_update", onPriceUpdate);

        return () => {
            socket.emit("leave_symbol", symbol);
            socket.off("price_update", onPriceUpdate);
        };
    }, [socket, connected, symbol]);

    return (
        <div className="h-10 w-32 ml-auto relative group">
            {data.length > 0 ? (
                <>
                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={data}>
                            <YAxis domain={['auto', 'auto']} hide />
                            {entryPrice && entryPrice > 0 && (
                                <ReferenceLine
                                    y={entryPrice}
                                    stroke={color}
                                    strokeOpacity={0.3}
                                    strokeDasharray="2 2"
                                />
                            )}
                            <Line
                                type="monotone"
                                dataKey="v"
                                stroke={color}
                                strokeWidth={2}
                                dot={false}
                                isAnimationActive={false}
                            />
                        </LineChart>
                    </ResponsiveContainer>
                    {/* Tooltip Overlay */}
                    {entryPrice && entryPrice > 0 && (
                        <div className="absolute -top-7 right-0 opacity-0 group-hover:opacity-100 transition-opacity bg-black/80 backdrop-blur-md px-2 py-1 flex items-center gap-2 rounded border border-border/50 text-[9px] font-mono whitespace-nowrap z-50 pointer-events-none shadow-xl">
                            <span className="text-muted font-bold uppercase tracking-tighter">Entry</span>
                            <span style={{ color: color }}>${formatAssetPriceFixed(entryPrice, { symbol })}</span>
                        </div>
                    )}
                </>
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
