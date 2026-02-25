"use client"

import AppLayout from "@/components/layout/AppLayout";
import { TrendingUp, Activity, DollarSign, RefreshCw } from "lucide-react";
import React, { useEffect, useState, useRef } from "react";
import { createChart, ColorType, BaselineSeries } from "lightweight-charts";

export default function ManagerDashboard() {
    const chartContainerRef = useRef<HTMLDivElement>(null);
    const chartApi = useRef<any>(null);
    const [history, setHistory] = useState<{ time: number; realized: number; total: number }[]>([]);
    const [loading, setLoading] = useState(true);
    const [currentBalance, setCurrentBalance] = useState(0);
    const [currentEquity, setCurrentEquity] = useState(0);

    const fetchHistory = async () => {
        try {
            const res = await fetch('http://localhost:8282/api/v1/portfolios/history');
            const data = await res.json();
            setHistory(data);
            if (data.length > 0) {
                const latest = data[data.length - 1];
                setCurrentBalance(latest.realized);
                setCurrentEquity(latest.total);
            }
        } catch (err) {
            console.error("Failed to fetch equity history:", err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchHistory();
        const interval = setInterval(fetchHistory, 30000); // 30s refresh
        return () => clearInterval(interval);
    }, []);

    useEffect(() => {
        if (!chartContainerRef.current || history.length === 0) return;

        const chart = createChart(chartContainerRef.current, {
            layout: {
                background: { type: ColorType.Solid, color: 'transparent' },
                textColor: '#71717a',
            },
            grid: {
                vertLines: { color: 'rgba(39, 39, 42, 0.4)' },
                horzLines: { color: 'rgba(39, 39, 42, 0.4)' },
            },
            width: chartContainerRef.current.clientWidth,
            height: 500,
            rightPriceScale: { borderVisible: false, autoScale: true },
            timeScale: { borderVisible: false, timeVisible: true, secondsVisible: false },
            crosshair: {
                horzLine: { labelVisible: true },
                vertLine: { labelVisible: true },
            },
        });

        // 1. Total Equity Series (Area)
        const totalSeries = chart.addSeries(BaselineSeries, {
            baseValue: { type: 'price', price: 50000 },
            topFillColor1: 'rgba(34, 197, 94, 0.25)',
            topFillColor2: 'rgba(34, 197, 94, 0.05)',
            topLineColor: 'rgba(34, 197, 94, 1)',
            bottomFillColor1: 'rgba(239, 68, 68, 0.05)',
            bottomFillColor2: 'rgba(239, 68, 68, 0.25)',
            bottomLineColor: 'rgba(239, 68, 68, 1)',
            lineWidth: 3,
            title: 'Total Equity',
        });

        // 2. Realized Balance Series (Line)
        const realizedSeries = chart.addSeries(BaselineSeries, {
            baseValue: { type: 'price', price: 50000 },
            topLineColor: '#3b82f6',
            bottomLineColor: '#3b82f6',
            lineWidth: 2,
            lineStyle: 1, // Dotted
            title: 'Realized Balance',
        });

        const totalData = history.map(d => ({ time: d.time as any, value: d.total }));
        const realizedData = history.map(d => ({ time: d.time as any, value: d.realized }));

        totalSeries.setData(totalData);
        realizedSeries.setData(realizedData);

        chart.timeScale().fitContent();
        chartApi.current = chart;

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
    }, [history]);

    return (
        <AppLayout>
            <div className="p-6 lg:p-12 space-y-8 animate-fade-in max-w-7xl mx-auto">
                {/* Header Section */}
                <div className="flex flex-col md:flex-row md:items-end justify-between gap-6 border-b border-border/50 pb-8">
                    <div className="space-y-1">
                        <div className="flex items-center gap-2 text-accent">
                            <Activity size={16} />
                            <span className="text-[10px] font-black uppercase tracking-[0.3em]">Equity Oracle v2</span>
                        </div>
                        <h1 className="text-4xl font-black tracking-tight text-white">Dual Equity Analysis</h1>
                        <p className="text-muted text-sm font-medium">Tracking Realized Capital vs Market-Adjusted Exposure.</p>
                    </div>

                    <div className="flex gap-4">
                        <div className="bg-card/40 backdrop-blur-md border border-border/50 p-4 rounded-xl shadow-xl flex items-center gap-4">
                            <div className="text-right border-r border-border/50 pr-4">
                                <p className="text-[9px] text-blue-400 font-black uppercase tracking-widest">Realized Balance</p>
                                <p className="text-xl font-mono font-black text-white">
                                    ${currentBalance.toLocaleString(undefined, { minimumFractionDigits: 2 })}
                                </p>
                            </div>
                            <div className="text-right">
                                <p className="text-[9px] text-accent font-black uppercase tracking-widest">Account Equity</p>
                                <p className={`text-xl font-mono font-black ${currentEquity >= 1200 ? 'text-green' : 'text-red'}`}>
                                    ${currentEquity.toLocaleString(undefined, { minimumFractionDigits: 2 })}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>

                {/* Main Chart Card */}
                <div className="bg-card/30 border border-border/50 rounded-3xl overflow-hidden shadow-2xl backdrop-blur-sm relative group">
                    <div className="absolute top-6 left-6 z-10 flex items-center gap-3">
                        <div className="px-3 py-1.5 bg-background/80 backdrop-blur-xl border border-border/50 rounded-xl flex items-center gap-2 shadow-lg">
                            <div className="h-1.5 w-1.5 rounded-full bg-green animate-pulse" />
                            <span className="text-[9px] font-black uppercase tracking-widest text-muted">Live Feed</span>
                        </div>
                        <button
                            onClick={() => { setLoading(true); fetchHistory(); }}
                            className="p-2 bg-background/80 backdrop-blur-xl border border-border/50 rounded-xl text-muted hover:text-accent transition-all hover:scale-105 active:scale-95 shadow-lg"
                        >
                            <RefreshCw size={14} className={loading ? 'animate-spin' : ''} />
                        </button>
                    </div>

                    <div className="p-8 pt-20">
                        {history.length === 0 && !loading ? (
                            <div className="h-[500px] flex flex-col items-center justify-center text-center space-y-4">
                                <div className="h-20 w-20 rounded-full bg-white/5 flex items-center justify-center border border-white/10">
                                    <TrendingUp size={32} className="text-muted/40" />
                                </div>
                                <div className="space-y-1">
                                    <p className="text-sm font-black uppercase tracking-widest text-white">No historical data recorded</p>
                                    <p className="text-xs text-muted max-w-xs">Start trading or wait for the system to generate value snapshots to visualize your equity curve.</p>
                                </div>
                            </div>
                        ) : (
                            <div ref={chartContainerRef} className="w-full" />
                        )}
                    </div>

                    {/* Footer Info */}
                    <div className="px-8 py-4 bg-background/20 border-t border-border/20 flex items-center justify-between">
                        <div className="flex items-center gap-4 text-[10px] font-bold text-muted uppercase tracking-tighter">
                            <span>Points: {history.length}</span>
                            <span className="h-1 w-1 rounded-full bg-border" />
                            <span>Last Sync: {history.length > 0 ? history[history.length - 1].time : 'Never'}</span>
                        </div>
                        <div className="flex items-center gap-2 text-[10px] font-bold text-accent uppercase tracking-widest">
                            <TrendingUp size={10} />
                            <span>Mandate Performance Delta</span>
                        </div>
                    </div>
                </div>

                {/* Legend/Context */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div className="bg-card/20 border border-border/30 p-6 rounded-2xl space-y-2">
                        <p className="text-[10px] font-black text-muted uppercase tracking-widest">Growth Metric</p>
                        <p className="text-xs text-white leading-relaxed">The <span className="text-green font-bold">Baseline Chart</span> visualizes your performance relative to your initial starting point. Green zones represent profit expansion, while red zones indicate periods of drawdown.</p>
                    </div>
                    <div className="bg-card/20 border border-border/30 p-6 rounded-2xl space-y-2">
                        <p className="text-[10px] font-black text-muted uppercase tracking-widest">Audit Period</p>
                        <p className="text-xs text-white leading-relaxed">This view captures every transition in your net value, providing a high-fidelity audit trail for institutional reporting and risk management.</p>
                    </div>
                    <div className="bg-card/20 border border-border/30 p-6 rounded-2xl space-y-2">
                        <p className="text-[10px] font-black text-muted uppercase tracking-widest">Update Frequency</p>
                        <p className="text-xs text-white leading-relaxed">Snapshots are automatically synchronized every 30 seconds or upon significant portfolio mutations (liquidations, acquisitions).</p>
                    </div>
                </div>
            </div>
        </AppLayout>
    );
}
