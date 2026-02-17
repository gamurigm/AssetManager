"use client"

import { useParams } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { createChart, ColorType, CandlestickSeries } from "lightweight-charts";

export default function ChartWindow() {
    const params = useParams();
    const symbol = typeof params.symbol === 'string' ? decodeURIComponent(params.symbol) : '';
    const chartContainerRef = useRef<HTMLDivElement>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (!chartContainerRef.current || !symbol) return;

        const chart = createChart(chartContainerRef.current, {
            layout: {
                background: { type: ColorType.Solid, color: '#0a0a0a' },
                textColor: '#d1d1d1',
            },
            grid: {
                vertLines: { color: '#1f1f1f' },
                horzLines: { color: '#1f1f1f' },
            },
            width: chartContainerRef.current.clientWidth,
            height: chartContainerRef.current.clientHeight || 500,
        });

        const candlestickSeries = chart.addSeries(CandlestickSeries, {
            upColor: '#26a69d',
            downColor: '#ef5350',
            borderVisible: false,
            wickUpColor: '#26a69d',
            wickDownColor: '#ef5350',
        });

        // Fetch historical data
        const fetchHistory = async () => {
            try {
                const res = await fetch(`http://127.0.0.1:8000/api/v1/market/historical/${encodeURIComponent(symbol)}?limit=300`);
                const data = await res.json();
                if (data.historical) {
                    const formattedData = data.historical.map((d: any) => ({
                        time: d.date,
                        open: d.open,
                        high: d.high,
                        low: d.low,
                        close: d.close,
                    })).sort((a: any, b: any) => a.time.localeCompare(b.time));

                    candlestickSeries.setData(formattedData);
                    chart.timeScale().fitContent();
                    setLoading(false);
                }
            } catch (e) {
                console.error("Failed to fetch history", e);
            }
        };

        fetchHistory();

        const handleResize = () => {
            if (chartContainerRef.current) {
                chart.applyOptions({ width: chartContainerRef.current.clientWidth });
            }
        };

        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
            chart.remove();
        };
    }, [symbol]);

    return (
        <div className="h-screen w-screen bg-[#0a0a0a] flex flex-col overflow-hidden">
            <div className="px-4 py-3 border-b border-white/5 flex items-center justify-between text-white/50 bg-[#0f0f0f] drag">
                <div className="flex items-center gap-3">
                    <div className="h-8 w-8 rounded-lg bg-accent/20 flex items-center justify-center text-accent text-xs font-bold">
                        {symbol.slice(0, 2)}
                    </div>
                    <div className="flex flex-col">
                        <span className="text-sm font-bold text-white leading-none">{symbol}</span>
                        <span className="text-[9px] uppercase font-bold tracking-widest text-muted mt-1">Interactive Trading Chart</span>
                    </div>
                </div>
                <div className="flex items-center gap-4">
                    <div className="flex items-center gap-1.5 px-2 py-1 bg-white/5 rounded-md">
                        <div className="h-1.5 w-1.5 rounded-full bg-green animate-pulse" />
                        <span className="text-[10px] font-bold text-green uppercase tracking-tighter">Live Feed</span>
                    </div>
                    {loading && <span className="text-xs animate-pulse font-mono tracking-tighter">Syncing...</span>}
                </div>
            </div>
            <div ref={chartContainerRef} className="flex-1 w-full" />
        </div>
    );
}
