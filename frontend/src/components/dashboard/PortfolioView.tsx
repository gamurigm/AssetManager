"use client";

import React, { useState, useEffect } from "react";
import dynamic from "next/dynamic";
import {
    TrendingUp, TrendingDown, DollarSign, BarChart3,
    Activity, FileText, ShieldCheck, Star,
    ChevronDown, ChevronUp, LayoutGrid, ChartPie
} from "lucide-react";
import { usePortfolio } from "@/context/PortfolioContext";
import { getHeatmapColor, BRIGHT_BADGE_COLORS } from "@/lib/colors";
import type { DashboardHolding, TransactionRecord, TreemapItem, SectorItem } from "@/types/dashboard";
import AssetSparkline from "@/components/dashboard/AssetSparkline";

const AssetTreemap = dynamic(() => import("@/components/charts/AssetTreemap"), {
    ssr: false,
    loading: () => <div className="h-[300px] flex items-center justify-center"><div className="h-6 w-6 border-2 border-accent border-t-transparent rounded-full animate-spin" /></div>,
});
const SectorPieChart = dynamic(() => import("@/components/charts/SectorPieChart"), {
    ssr: false,
    loading: () => <div className="h-[300px] flex items-center justify-center"><div className="h-6 w-6 border-2 border-accent border-t-transparent rounded-full animate-spin" /></div>,
});
const PortfolioEquityChart = dynamic(() => import("@/components/charts/PortfolioEquityChart"), {
    ssr: false,
    loading: () => (
        <div className="h-[300px] flex items-center justify-center text-muted text-xs">
            <div className="flex flex-col items-center gap-3">
                <div className="h-6 w-6 border-2 border-accent border-t-transparent rounded-full animate-spin" />
                <span className="font-mono text-[10px] tracking-widest uppercase">Loading NAV</span>
            </div>
        </div>
    ),
});

// ─── Props ──────────────────────────────────────────────────────────
interface PortfolioViewProps {
    activeHoldings: DashboardHolding[];
    totalValue: number;
    accountEquity: number;
    totalPnL: number;
    pnlPercent: number;
    riskData: any;
    transactions: TransactionRecord[];
    treemapData: TreemapItem[];
    sectorData: SectorItem[];
    collapsed: Record<string, boolean>;
    togglePanel: (id: string) => void;
    onSelectSymbol: (symbol: string) => void;
}

// ─── Component ──────────────────────────────────────────────────────
export default function PortfolioView({
    activeHoldings, totalValue, accountEquity, totalPnL, pnlPercent,
    riskData, transactions, treemapData, sectorData,
    collapsed, togglePanel, onSelectSymbol,
}: PortfolioViewProps) {
    const { holdings, setHoldings, closePosition, realizedPnL, unrealizedPnL } = usePortfolio();
    const [isLight, setIsLight] = useState(false);

    useEffect(() => {
        const check = () => setIsLight(document.documentElement.classList.contains("light"));
        check();
        const obs = new MutationObserver(check);
        obs.observe(document.documentElement, { attributes: true, attributeFilter: ["class"] });
        return () => obs.disconnect();
    }, []);

    // ── Derived Metrics ─────────────────────────────────────────
    const winners = activeHoldings.filter(h => h.change > 0).length;
    const winRate = activeHoldings.length > 0 ? ((winners / activeHoldings.length) * 100) : 0;
    const exposure = totalValue;
    const cash = Math.max(0, accountEquity - exposure);
    const leverage = accountEquity > 0 ? totalValue / accountEquity : 0;
    const topHolding = activeHoldings.length > 0
        ? activeHoldings.reduce((max, h) => (Math.abs(h.shares) * h.price * h.factor) > (Math.abs(max.shares) * max.price * max.factor) ? h : max, activeHoldings[0])
        : null;
    const topWeight = topHolding && totalValue > 0 ? ((Math.abs(topHolding.shares) * topHolding.price * topHolding.factor) / totalValue * 100) : 0;
    const sectors = new Set(activeHoldings.map(h => h.sector)).size;
    const avgChange = activeHoldings.length > 0 ? activeHoldings.reduce((sum, h) => sum + h.changePercent, 0) / activeHoldings.length : 0;
    const sectorWeights: Record<string, number> = {};
    activeHoldings.forEach(h => { const val = Math.abs(h.shares) * h.price * h.factor; sectorWeights[h.sector] = (sectorWeights[h.sector] || 0) + val; });
    const topSectorVal = Object.values(sectorWeights).length > 0 ? Math.max(...Object.values(sectorWeights)) : 0;
    const maxConcentration = totalValue > 0 ? (topSectorVal / totalValue) * 100 : 0;

    return (
        <div className="flex-1 flex flex-col min-h-0 gap-4">
            {/* ── Header + Metrics Ribbon ── */}
            <div className="shrink-0 relative overflow-hidden rounded-2xl bg-card/40 border border-border/50">
                <div className="absolute inset-0 bg-gradient-to-r from-accent/[0.03] via-transparent to-purple-500/[0.03]" />
                <div className="absolute bottom-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-accent/20 to-transparent" />

                {/* Top Row: Branding + Actions */}
                <div className="relative z-10 px-6 py-4 flex items-center justify-between">
                    <div className="flex items-center gap-4">
                        <div className="relative">
                            <div className="h-12 w-12 rounded-2xl bg-accent/15 border border-accent/30 flex items-center justify-center shadow-lg shadow-accent/5">
                                <Activity size={24} className="text-accent animate-pulse" />
                            </div>
                            <div className="absolute -top-1 -right-1 h-3.5 w-3.5 rounded-full bg-green border-2 border-background animate-pulse shadow-[0_0_10px_rgba(16,185,129,0.5)]" />
                        </div>
                        <div>
                            <div className="flex items-center gap-3">
                                <h1 className="text-3xl font-black tracking-tighter dark:text-white text-zinc-900 drop-shadow-sm">Alpha Core</h1>
                                <span className="text-[10px] font-black uppercase tracking-[0.4em] text-accent font-mono bg-accent/10 px-3 py-1 rounded-lg border border-accent/20">NODE:ALPHA-9</span>
                            </div>
                            <div className="flex items-center gap-5 text-[11px] font-bold text-muted/80 mt-1">
                                <span className="flex items-center gap-1.5"><Star size={10} className="text-yellow-500" /> Tier 1 Liquidity</span>
                                <span className="flex items-center gap-1.5"><ShieldCheck size={10} className="text-emerald-500" /> Institutional Audit</span>
                                <span className="flex items-center gap-1.5"><div className="h-2 w-2 rounded-full bg-green animate-pulse" /> Real-time Node</span>
                            </div>
                        </div>
                    </div>

                    <button
                        onClick={async () => {
                            const btn = document.getElementById('audit-btn');
                            if (btn) { btn.textContent = '⏳ Processing...'; (btn as any).disabled = true; }
                            try {
                                const res = await fetch('http://127.0.0.1:8282/api/v1/portfolios/report', {
                                    method: 'POST', headers: { 'Content-Type': 'application/json' },
                                    body: JSON.stringify({ holdings: activeHoldings, total_value: totalValue, total_pnl: totalPnL })
                                });
                                if (res.ok) { const data = await res.json(); window.open(data.url, '_blank'); }
                                else alert("Report failed.");
                            } catch { alert("Backend unreachable."); }
                            finally { if (btn) { btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/></svg> Generate Audit'; (btn as any).disabled = false; } }
                        }}
                        id="audit-btn"
                        className="px-6 py-2.5 bg-white dark:bg-zinc-50 text-black hover:bg-zinc-200 text-xs font-black uppercase tracking-widest rounded-2xl transition-all shadow-xl flex items-center gap-3 active:scale-95 disabled:opacity-50"
                    >
                        <FileText size={14} /> Generate Audit
                    </button>
                </div>

                {/* Metrics Ribbon */}
                <MetricsRibbon
                    accountEquity={accountEquity} totalPnL={totalPnL} pnlPercent={pnlPercent}
                    unrealizedPnL={unrealizedPnL} realizedPnL={realizedPnL}
                    exposure={exposure} leverage={leverage} cash={cash}
                    riskData={riskData} activeHoldings={activeHoldings}
                    sectors={sectors} winRate={winRate}
                    maxConcentration={maxConcentration} topHolding={topHolding}
                    topWeight={topWeight} avgChange={avgChange} isLight={isLight}
                />
            </div>

            {/* BENTO GRID */}
            <div className="shrink-0 min-w-0 flex flex-col gap-4">
                {/* NAV Chart (Full Width) */}
                <div className={`relative bg-card/30 border border-border/40 rounded-3xl overflow-hidden shadow-2xl flex flex-col transition-all duration-300 ${collapsed['equity-curve'] ? 'min-h-[60px]' : ''}`}>
                    <div onClick={() => togglePanel('equity-curve')} className="px-6 py-4 flex items-center justify-between bg-card-hover/20 cursor-pointer border-b border-white/5 active:bg-card-hover/40 transition-colors">
                        <div className="flex items-center gap-3">
                            <div className="h-8 w-8 rounded-lg bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center"><TrendingUp size={16} className="text-cyan-400" /></div>
                            <div className="flex flex-col">
                                <h2 className="text-xs font-black uppercase tracking-[0.2em] text-cyan-100 leading-none">Net Asset Value (NAV) Evolution</h2>
                                <span className="text-[9px] font-bold text-muted/60 mt-1 uppercase tracking-widest">Realized vs. Total Equity (Historical)</span>
                            </div>
                        </div>
                        <div className="flex items-center gap-4">
                            <div className="hidden sm:flex items-center gap-4">
                                <div className="flex items-center gap-2"><div className="h-2 w-2 rounded-full bg-cyan-400 shadow-[0_0_8px_rgba(34,211,238,0.8)]" /><span className="text-[10px] font-black uppercase text-cyan-100/70 tracking-tighter">Total Equity</span></div>
                                <div className="flex items-center gap-2"><div className="h-2 w-2 rounded-full bg-zinc-600 border border-zinc-400/30" /><span className="text-[10px] font-black uppercase text-zinc-500 tracking-tighter">Realized Balance</span></div>
                            </div>
                            {collapsed['equity-curve'] ? <ChevronDown size={14} className="text-muted" /> : <ChevronUp size={14} className="text-muted" />}
                        </div>
                    </div>
                    {!collapsed['equity-curve'] && (
                        <div className="p-6 flex-1 min-h-[350px] flex flex-col animate-in fade-in slide-in-from-top-4 duration-700 delay-150"><PortfolioEquityChart /></div>
                    )}
                </div>

                {/* Sector Chart (Full Width) */}
                <div className="flex flex-col">
                    <CollapsiblePanel id="sector" collapsed={collapsed} toggle={togglePanel} title="Sector Exposure" icon={<ChartPie size={14} className="text-accent" />}>
                        <div className="p-4 flex-1 min-h-[350px]"><SectorPieChart data={sectorData} total={totalValue} /></div>
                    </CollapsiblePanel>
                </div>

                {/* Treemap (Full Width) */}
                <div className="flex flex-col">
                    <CollapsiblePanel id="treemap" collapsed={collapsed} toggle={togglePanel} title="Allocation Intensity" icon={<LayoutGrid size={14} className="text-accent" />}
                        badge={<span className="hidden sm:block text-[9px] text-muted font-black px-2 py-0.5 bg-background rounded border border-border tracking-tighter uppercase">Hi-Density</span>}
                        minHeight="400px"
                    >
                        <div className="p-4 flex-1 min-h-[400px]"><AssetTreemap data={treemapData} /></div>
                    </CollapsiblePanel>
                </div>
            </div>

            {/* Positions Table */}
            <div className="space-y-6 shrink-0 mt-4">
                <PositionsTable
                    activeHoldings={activeHoldings} holdings={holdings} collapsed={collapsed}
                    togglePanel={togglePanel} onSelectSymbol={onSelectSymbol}
                    closePosition={closePosition} setHoldings={setHoldings}
                />
            </div>

            {/* Bottom Widgets */}
            <div className="grid grid-cols-1 xl:grid-cols-2 gap-4 shrink-0 mb-14">
                <EconomicsPanel totalValue={totalValue} collapsed={collapsed} togglePanel={togglePanel} />
                <ActivityPanel transactions={transactions} collapsed={collapsed} togglePanel={togglePanel} />
            </div>
        </div>
    );
}

// ─── Sub-Components ─────────────────────────────────────────────────

function MetricsRibbon({ accountEquity, totalPnL, pnlPercent, unrealizedPnL, realizedPnL, exposure, leverage, cash, riskData, activeHoldings, sectors, winRate, maxConcentration, topHolding, topWeight, avgChange, isLight }: any) {
    return (
        <div className="relative z-10 px-6 py-3 border-t border-border/40 flex items-center gap-2 overflow-x-auto scrollbar-none bg-accent/[0.02]">
            <div className={`flex items-center gap-2 px-3 py-1.5 rounded-xl shrink-0 ${isLight ? "bg-blue-100 border border-blue-200" : "bg-blue-500/10 border border-blue-500/20"}`}>
                <DollarSign size={14} className={isLight ? "text-blue-600" : "text-blue-400"} /><span className={`text-[10px] font-black uppercase ${isLight ? "text-blue-800/80" : "text-blue-400/60"}`}>Equity</span>
                <span className={`text-lg font-black tracking-tighter ${isLight ? "text-blue-900" : "text-blue-100"}`}>${accountEquity.toLocaleString("en-US", { maximumFractionDigits: 0 })}</span>
            </div>
            <div className={`flex items-center gap-2 px-3 py-1.5 rounded-xl shrink-0 ${totalPnL >= 0 ? (isLight ? 'bg-green-100 border border-green-200' : 'bg-green/10 border border-green/20') : (isLight ? 'bg-red-100 border border-red-200' : 'bg-red/10 border border-red/20')}`}>
                {totalPnL >= 0 ? <TrendingUp size={14} className={isLight ? "text-green-700" : "text-green/80"} /> : <TrendingDown size={14} className={isLight ? "text-red-700" : "text-red/80"} />}
                <span className="text-[10px] text-muted font-black uppercase tracking-tight">Net P&L</span>
                <div className="flex flex-col">
                    <span className={`text-lg font-black tracking-tighter leading-none ${totalPnL >= 0 ? (isLight ? 'text-green-800' : 'text-green') : (isLight ? 'text-red-800' : 'text-red')}`}>{totalPnL >= 0 ? '+' : ''}${Math.abs(totalPnL).toLocaleString("en-US", { maximumFractionDigits: 0 })}</span>
                    <span className={`text-[10px] font-black tracking-tighter ${totalPnL >= 0 ? (isLight ? 'text-green-700' : 'text-green/60') : (isLight ? 'text-red-700' : 'text-red/60')}`}>{pnlPercent >= 0 ? '+' : ''}{pnlPercent.toFixed(2)}%</span>
                </div>
            </div>
            <div className="h-8 w-[1px] bg-border/40 mx-1 shrink-0" />
            <div className={`flex flex-col gap-1 px-3 py-1.5 rounded-xl border shrink-0 ${isLight ? "bg-zinc-100 border-zinc-200" : "bg-zinc-500/5 border-border/20"}`}>
                <div className="flex items-center gap-2"><span className="text-[9px] text-muted font-black uppercase w-12">Unreal'd</span><span className={`text-sm font-bold ${unrealizedPnL >= 0 ? (isLight ? 'text-green-700' : 'text-green/80') : (isLight ? 'text-red-700' : 'text-red/80')}`}>${Math.abs(unrealizedPnL).toLocaleString("en-US", { maximumFractionDigits: 0 })}</span></div>
                <div className="flex items-center gap-2"><span className="text-[9px] text-muted font-black uppercase w-12">Real'd</span><span className={`text-sm font-bold ${realizedPnL >= 0 ? (isLight ? 'text-green-700' : 'text-green/80') : (isLight ? 'text-red-700' : 'text-red/80')}`}>${Math.abs(realizedPnL).toLocaleString("en-US", { maximumFractionDigits: 0 })}</span></div>
            </div>
            <div className={`flex flex-col gap-1 px-3 py-1.5 rounded-xl border shrink-0 ${isLight ? "bg-orange-100 border-orange-200" : "bg-orange-500/10 border-orange-500/20"}`}>
                <div className="flex items-center gap-2"><span className={`text-[9px] font-black uppercase w-12 ${isLight ? "text-orange-700" : "text-orange-400"}`}>Exposure</span><span className={`text-sm font-bold ${isLight ? "text-orange-900" : "text-orange-200"}`}>${exposure.toLocaleString("en-US", { maximumFractionDigits: 0 })}</span></div>
                <div className="flex items-center gap-2"><span className={`text-[9px] font-black uppercase w-12 ${isLight ? "text-orange-700" : "text-orange-400"}`}>Leverage</span><span className={`text-sm font-bold ${leverage > 1.5 ? (isLight ? 'text-red-700' : 'text-red') : (isLight ? 'text-orange-900' : 'text-orange-200')}`}>{leverage.toFixed(2)}x</span></div>
            </div>
            <div className={`flex items-center gap-2 px-3 py-1.5 rounded-xl border shrink-0 ${isLight ? "bg-cyan-100 border-cyan-200" : "bg-cyan-500/10 border-cyan-500/20"}`}>
                <DollarSign size={14} className={isLight ? "text-cyan-600" : "text-cyan-400"} /><span className={`text-[10px] font-black uppercase ${isLight ? "text-cyan-800/80" : "text-cyan-400/60"}`}>Liquidity</span>
                <span className={`text-lg font-black tracking-tighter ${isLight ? "text-cyan-900" : "text-cyan-100"}`}>${cash.toLocaleString("en-US", { maximumFractionDigits: 0 })}</span>
            </div>
            <div className={`flex flex-col gap-1 px-3 py-1.5 rounded-xl border shrink-0 ${isLight ? "bg-purple-100 border-purple-200" : "bg-purple-500/10 border-purple-500/20"}`}>
                <div className="flex items-center gap-3">
                    <div className="flex items-center gap-2"><span className={`text-[9px] font-black uppercase w-8 ${isLight ? "text-purple-700" : "text-purple-400"}`}>mVaR</span><span className={`text-sm font-bold ${isLight ? "text-purple-900" : "text-purple-200"}`}>{riskData ? `${riskData.mvar_95_percent ?? riskData.var_95_percent ?? '—'}%` : '…'}</span></div>
                    <div className="flex items-center gap-2"><span className={`text-[9px] font-black uppercase w-8 ${isLight ? "text-purple-700" : "text-purple-400"}`}>Vol(σ)</span><span className={`text-sm font-bold ${isLight ? "text-purple-900" : "text-purple-200"}`}>{riskData ? `${riskData.annualized_volatility ?? '—'}%` : '…'}</span></div>
                </div>
                <div className="flex items-center gap-2"><span className={`text-[9px] font-black uppercase w-8 ${isLight ? "text-purple-700" : "text-purple-400"}`}>Sharpe</span><span className={`text-sm font-bold ${riskData && riskData.sharpe_ratio > 1 ? (isLight ? 'text-green-700' : 'text-green') : riskData && riskData.sharpe_ratio > 0 ? (isLight ? 'text-purple-900' : 'text-purple-200') : (isLight ? 'text-red-700' : 'text-red/80')}`}>{riskData ? (riskData.sharpe_ratio ?? '—') : '…'}</span></div>
            </div>
            <div className={`flex flex-col gap-1 px-3 py-1.5 rounded-xl border shrink-0 ${isLight ? "bg-indigo-100 border-indigo-200" : "bg-indigo-500/10 border-border/30"}`}>
                <div className="flex items-center gap-3">
                    <div className="flex items-center gap-1"><span className="text-[9px] text-muted font-black uppercase">Holdings:</span><span className={`text-sm font-bold ${isLight ? "text-indigo-900" : "text-indigo-100"}`}>{activeHoldings.length}</span></div>
                    <div className="flex items-center gap-1"><span className="text-[9px] text-muted font-black uppercase">Sectors:</span><span className={`text-sm font-bold ${isLight ? "text-indigo-900" : "text-indigo-100"}`}>{sectors}</span></div>
                </div>
                <div className="flex items-center gap-1"><span className="text-[9px] text-muted font-black uppercase">Win Rate:</span><span className={`text-sm font-bold ${winRate >= 50 ? (isLight ? 'text-green-700' : 'text-green') : (isLight ? 'text-amber-600' : 'text-amber-400')}`}>{winRate.toFixed(0)}%</span></div>
            </div>
            <div className={`flex flex-col gap-1 px-3 py-1.5 rounded-xl border shrink-0 ${isLight ? "bg-pink-100 border-pink-200" : "bg-pink-500/10 border-pink-500/20"}`}>
                <div className="flex items-center gap-2"><span className={`text-[9px] font-black uppercase w-10 ${isLight ? "text-pink-700" : "text-pink-400"}`}>Concen.</span><span className={`text-sm font-bold ${isLight ? "text-pink-900" : "text-pink-100"}`}>{maxConcentration.toFixed(1)}%</span></div>
                <div className="flex items-center gap-2"><span className={`text-[9px] font-black uppercase w-10 ${isLight ? "text-pink-700" : "text-pink-400"}`}>Drawdn</span><span className={`text-sm font-bold ${riskData && riskData.max_drawdown > 10 ? (isLight ? 'text-red-700' : 'text-red') : (isLight ? 'text-pink-900' : 'text-pink-100')}`}>{riskData ? `-${riskData.max_drawdown}%` : '—'}</span></div>
            </div>
            {topHolding && (
                <div className={`flex items-center gap-3 px-4 py-1.5 rounded-xl border shrink-0 shadow-lg ${isLight ? "bg-blue-50 border-blue-200 shadow-blue-500/10" : "bg-accent/10 border-accent/30 shadow-accent/5"}`}>
                    <div className="flex flex-col"><span className={`text-[9px] font-black uppercase tracking-tighter ${isLight ? "text-blue-700" : "text-accent"}`}>Top Focus Asset</span><span className={`text-lg font-black tracking-tighter ${isLight ? "text-zinc-900" : "text-white"}`}>{topHolding.symbol}</span></div>
                    <div className="flex flex-col items-end"><span className={`text-[10px] font-bold ${isLight ? "text-blue-600" : "text-accent/60"}`}>{topWeight.toFixed(1)}% Weight</span><span className={`text-xs font-black ${avgChange >= 0 ? (isLight ? 'text-green-700' : 'text-green') : (isLight ? 'text-red-700' : 'text-red')}`}>Avg Δ {avgChange >= 0 ? '+' : ''}{avgChange.toFixed(2)}%</span></div>
                </div>
            )}
        </div>
    );
}

function PositionsTable({ activeHoldings, holdings, collapsed, togglePanel, onSelectSymbol, closePosition, setHoldings }: any) {
    return (
        <div className={`xl:col-span-2 xl:row-span-1 bg-card border border-border rounded-2xl overflow-hidden shadow-sm flex flex-col transition-all duration-300 ${collapsed['holdings'] ? 'h-[60px]' : ''}`}>
            <div onClick={() => togglePanel('holdings')} className="px-5 py-3 border-b border-border flex items-center justify-between bg-card-hover/30 cursor-pointer hover:bg-card-hover/50 transition-colors">
                <h2 className="text-xs font-bold uppercase tracking-widest text-muted">Positions</h2>
                <div className="flex items-center gap-4">
                    <div className="flex items-center gap-2">
                        {holdings.length > activeHoldings.length && (
                            <div className="flex items-center gap-1.5 bg-yellow-400/5 px-2 py-0.5 rounded border border-yellow-400/20">
                                <span className="h-1 w-1 rounded-full bg-yellow-400 animate-pulse" />
                                <span className="text-[9px] text-yellow-400 font-black uppercase">{holdings.length - activeHoldings.length} Sync</span>
                            </div>
                        )}
                        <span className="text-[10px] text-accent font-bold">{activeHoldings.length} Active</span>
                    </div>
                    <button
                        onClick={async (e) => {
                            e.stopPropagation();
                            if (confirm("Are you sure you want to liquidate all positions?")) {
                                for (const h of activeHoldings) {
                                    try { await fetch('http://127.0.0.1:8282/api/v1/trading/record', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ type_str: 'SELL', symbol: h.symbol, shares: h.shares, price: h.price }) }); } catch (err) { console.error(err); }
                                }
                                setHoldings([]);
                            }
                        }}
                        className="px-2 py-0.5 rounded border border-red/40 bg-red/5 text-[9px] font-bold text-red uppercase tracking-tighter hover:bg-red hover:text-white transition-all ml-2"
                    >Liquidate All</button>
                    {collapsed['holdings'] ? <ChevronDown size={14} className="text-muted" /> : <ChevronUp size={14} className="text-muted" />}
                </div>
            </div>
            {!collapsed['holdings'] && (
                <div className="overflow-y-auto flex-1 min-h-0 animate-in fade-in slide-in-from-top-2 duration-300">
                    <table className="w-full text-sm">
                        <thead>
                            <tr className="text-left text-muted text-[10px] font-bold uppercase tracking-widest border-b border-border bg-background/50">
                                <th className="px-6 py-3">Posicion</th><th className="px-4 py-3 text-right">Tipo</th>
                                <th className="px-4 py-3 text-right">Volumen</th><th className="px-4 py-3 text-right">Beneficio Neto</th>
                                <th className="px-4 py-3 text-right">Valor Mercado</th><th className="px-4 py-3 text-right">Fecha Adq.</th>
                                <th className="px-4 py-3 text-right">Evolución</th><th className="px-6 py-3 text-right">Acción</th>
                            </tr>
                        </thead>
                        <tbody className="stagger">
                            {activeHoldings.sort((a: any, b: any) => (b.shares * b.price) - (a.shares * a.price)).map((h: any) => {
                                const changeValue = h.changePercent || 0;
                                const badgeColor = getHeatmapColor(changeValue);
                                const isBright = BRIGHT_BADGE_COLORS.includes(badgeColor);
                                return (
                                    <tr key={h.symbol} onClick={() => onSelectSymbol(h.symbol)} className="border-b border-border/50 hover:bg-card-hover transition-colors group cursor-pointer">
                                        <td className="px-6 py-4">
                                            <div className="flex items-center gap-3">
                                                <div className="h-9 w-9 rounded-lg flex items-center justify-center text-white font-bold text-xs group-hover:scale-110 transition-all shadow-sm" style={{ backgroundColor: badgeColor }}>{h.symbol.slice(0, 2)}</div>
                                                <div><div className="font-bold group-hover:text-accent transition-colors">{h.symbol}</div><div className="text-[10px] text-muted font-bold tracking-tighter mt-0.5 truncate max-w-[130px]">{h.name}</div></div>
                                            </div>
                                        </td>
                                        <td className="px-4 py-4 text-right"><span className="text-[10px] font-black uppercase tracking-widest px-2 py-0.5 bg-card-hover rounded border border-border/50">{h.type}</span></td>
                                        <td className="px-4 py-4 text-right font-mono text-xs font-bold">{h.shares.toLocaleString()} <span className="text-muted text-[9px] font-black">× ${h.price.toLocaleString(undefined, { minimumFractionDigits: 2 })}</span></td>
                                        <td className="px-4 py-4 text-right">
                                            <div className="flex flex-col items-end gap-0.5">
                                                <span className={`text-sm font-black font-mono ${h.change >= 0 ? "text-green" : "text-red"}`}>{h.change >= 0 ? "+" : ""}${h.change.toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                                                <span className="inline-flex items-center gap-1 text-[10px] font-black px-2 py-0.5 rounded-lg" style={{ backgroundColor: `${badgeColor}20`, color: isBright ? '#18181b' : badgeColor, border: `1px solid ${badgeColor}40` }}>
                                                    {h.changePercent >= 0 ? <TrendingUp size={10} /> : <TrendingDown size={10} />}{h.changePercent.toFixed(2)}%
                                                </span>
                                            </div>
                                        </td>
                                        <td className="px-4 py-4 text-right font-mono text-xs font-bold">${(h.shares * h.price).toLocaleString(undefined, { minimumFractionDigits: 2 })}</td>
                                        <td className="px-4 py-4 text-right text-xs text-muted font-bold">{h.purchaseDate || 'N/A'}</td>
                                        <td className="px-4 py-4 pr-6 flex justify-end"><AssetSparkline symbol={h.symbol} color={badgeColor} entryPrice={h.entryPrice} /></td>
                                        <td className="px-6 py-4 text-right">
                                            <button onClick={(e) => { e.stopPropagation(); closePosition(h.symbol); }} className="opacity-0 group-hover:opacity-100 transition-all px-3 py-1.5 rounded-lg border border-red/20 text-[10px] font-black uppercase tracking-tighter text-red hover:bg-red/10 hover:border-red/40 hover:shadow-[0_0_12px_rgba(239,68,68,0.2)]">Liquidate</button>
                                        </td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}

function CollapsiblePanel({ id, collapsed, toggle, title, icon, badge, children, minHeight = "350px" }: {
    id: string; collapsed: Record<string, boolean>; toggle: (id: string) => void;
    title: string; icon: React.ReactNode; badge?: React.ReactNode; children: React.ReactNode; minHeight?: string;
}) {
    return (
        <div className={`bg-card border border-border rounded-2xl overflow-hidden shadow-sm flex flex-col shrink-0 transition-all duration-300`} style={{ minHeight: collapsed[id] ? '50px' : minHeight }}>
            <div onClick={() => toggle(id)} className="px-5 py-3 border-b border-border flex items-center justify-between bg-card-hover/20 cursor-pointer hover:bg-card-hover/40 transition-colors">
                <div className="flex items-center gap-2">{icon}<h2 className="text-xs font-black uppercase tracking-widest text-muted">{title}</h2></div>
                <div className="flex items-center gap-4">
                    {badge}
                    {collapsed[id] ? <ChevronDown size={14} className="text-muted" /> : <ChevronUp size={14} className="text-muted" />}
                </div>
            </div>
            {!collapsed[id] && <div className="flex-1 min-h-0 animate-in fade-in slide-in-from-top-2 duration-300">{children}</div>}
        </div>
    );
}

function EconomicsPanel({ totalValue, collapsed, togglePanel }: { totalValue: number; collapsed: Record<string, boolean>; togglePanel: (id: string) => void }) {
    return (
        <div className={`bg-card border border-border rounded-2xl overflow-hidden shadow-sm flex flex-col shrink-0 transition-all duration-300 ${collapsed['economics'] ? 'min-h-[50px]' : 'min-h-[250px]'}`}>
            <div onClick={() => togglePanel('economics')} className="px-5 py-3 border-b border-border flex items-center justify-between bg-card-hover/30 cursor-pointer hover:bg-card-hover/50 transition-colors">
                <h2 className="text-xs font-bold uppercase tracking-widest text-muted">Economics</h2>
                {collapsed['economics'] ? <ChevronDown size={14} className="text-muted" /> : <ChevronUp size={14} className="text-muted" />}
            </div>
            {!collapsed['economics'] && (
                <div className="p-6 space-y-5 flex-1 overflow-y-auto animate-in fade-in slide-in-from-top-2 duration-300">
                    <div className="space-y-3">
                        <FeeRow label="Management Fee (2.75%)" value={`$${(totalValue * 0.0275 / 12).toLocaleString(undefined, { minimumFractionDigits: 2 })}`} />
                        <FeeRow label="Service Fee (0.75%)" value={`$${(totalValue * 0.0075 / 12).toLocaleString(undefined, { minimumFractionDigits: 2 })}`} />
                        <FeeRow label="Other Exp. & Interest (0.59%)" value={`$${(totalValue * 0.0059 / 12).toLocaleString(undefined, { minimumFractionDigits: 2 })}`} />
                        <FeeRow label="Reimbursements & Waivers" value={`-$${(totalValue * 0.0059 / 12).toLocaleString(undefined, { minimumFractionDigits: 2 })}`} isGreen />
                        <div className="pt-2 border-t border-border/50 flex justify-between text-xs font-bold">
                            <span className="text-accent uppercase tracking-tighter">Total Net Expenses (3.50%)</span>
                            <span className="font-mono text-accent">~${(totalValue * 0.0350 / 12).toLocaleString(undefined, { minimumFractionDigits: 2 })} / mo</span>
                        </div>
                    </div>
                    <div className="space-y-2 pt-4 border-t border-border/20">
                        <FeeRow label="High-Water Mark (HWM)" value={`$${totalValue > 1250500 ? totalValue.toLocaleString() : "1,250,500.00"}`} />
                        <div className="p-3 rounded-lg bg-green/5 border border-green/10 flex items-center justify-between">
                            <span className="text-[10px] text-green font-bold uppercase tracking-tight">Accrued Perf. Fee (20% above HWM)</span>
                            <span className="text-sm font-bold text-green font-mono">${totalValue > 1250500 ? ((totalValue - 1250500) * 0.20).toFixed(2) : "0.00"}</span>
                        </div>
                    </div>
                    <div className="mt-auto pt-4 border-t border-border/50">
                        <p className="text-[10px] text-muted leading-relaxed">Fees are calculated based on the <span className="text-foreground">Net Asset Value (NAV)</span> at the end of each billing cycle.</p>
                    </div>
                </div>
            )}
        </div>
    );
}

function FeeRow({ label, value, isGreen }: { label: string; value: string; isGreen?: boolean }) {
    return (
        <div className="flex justify-between text-xs">
            <span className="text-muted font-medium">{label}</span>
            <span className={`font-mono ${isGreen ? 'text-green-500' : 'dark:text-white text-zinc-900'}`}>{value}</span>
        </div>
    );
}

function ActivityPanel({ transactions, collapsed, togglePanel }: { transactions: TransactionRecord[]; collapsed: Record<string, boolean>; togglePanel: (id: string) => void }) {
    return (
        <div className={`bg-card border border-border rounded-2xl overflow-hidden shadow-sm flex flex-col shrink-0 transition-all duration-300 ${collapsed['activity'] ? 'min-h-[50px]' : 'min-h-[350px]'}`}>
            <div onClick={() => togglePanel('activity')} className="px-5 py-3 border-b border-border flex items-center justify-between bg-card-hover/30 cursor-pointer hover:bg-card-hover/50 transition-colors">
                <div className="flex items-center gap-2"><Activity size={12} className="text-accent" /><h2 className="text-xs font-bold uppercase tracking-widest text-muted">Recent Activity</h2></div>
                <div className="flex items-center gap-4">
                    <span className="text-[10px] text-accent font-bold">{transactions.length} Events</span>
                    {collapsed['activity'] ? <ChevronDown size={14} className="text-muted" /> : <ChevronUp size={14} className="text-muted" />}
                </div>
            </div>
            {!collapsed['activity'] && (
                <div className="flex-1 overflow-y-auto p-0 animate-in fade-in slide-in-from-top-2 duration-300">
                    {transactions.length === 0 ? (
                        <div className="h-full flex flex-col items-center justify-center p-8 text-center">
                            <Activity size={32} className="text-muted/20 mb-3" />
                            <p className="text-xs text-muted font-bold uppercase tracking-widest">No recent transactions</p>
                        </div>
                    ) : (
                        <div className="divide-y divide-border/50">
                            {transactions.map((t, i) => (
                                <div key={i} className="px-5 py-3 hover:bg-card-hover/20 transition-colors flex items-center justify-between group">
                                    <div className="flex items-center gap-3">
                                        <div className={`h-8 w-8 rounded-lg flex items-center justify-center font-bold text-[10px] ${t.type === 'BUY' ? 'bg-green/10 text-green' : 'bg-red/10 text-red'}`}>{t.type.slice(0, 1)}</div>
                                        <div className="flex flex-col">
                                            <span className="text-xs font-bold group-hover:text-accent transition-colors">{t.symbol}</span>
                                            <span className="text-[9px] text-muted font-bold uppercase tracking-tighter">{t.date} • {t.time}</span>
                                        </div>
                                    </div>
                                    <div className="text-right flex flex-col">
                                        <span className="text-xs font-mono font-bold">${(t.price * t.shares).toLocaleString(undefined, { minimumFractionDigits: 2 })}</span>
                                        <span className="text-[9px] text-muted font-bold tracking-tighter">{t.shares} units @ ${t.price.toFixed(2)}</span>
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}
