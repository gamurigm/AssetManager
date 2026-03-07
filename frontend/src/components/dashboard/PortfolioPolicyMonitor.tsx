"use client";

import React from "react";
import {
    Activity,
    ArrowRightLeft,
    BrainCircuit,
    CheckCircle2,
    Loader2,
    Play,
    RefreshCw,
    ShieldAlert,
    Target,
    TrendingUp,
} from "lucide-react";
import { usePortfolio } from "@/context/PortfolioContext";
import { usePortfolioPolicy } from "@/hooks/usePortfolioPolicy";
import type { DashboardHolding } from "@/types/dashboard";
import type { PortfolioPolicyHolding } from "@/types/portfolioPolicy";

const API_BASE = "http://127.0.0.1:8282";

function formatSignedPercent(value: number): string {
    const prefix = value > 0 ? "+" : "";
    return `${prefix}${value.toFixed(2)}%`;
}

function formatSignedCurrency(value: number): string {
    const prefix = value > 0 ? "+" : "";
    return `${prefix}$${Math.abs(value).toLocaleString("en-US", { maximumFractionDigits: 0 })}`;
}

function actionTone(action: string): string {
    if (action === "HOLD" || action === "LOCK") return "text-zinc-300 bg-zinc-500/10 border-zinc-400/20";
    if (action === "BUY" || action === "REVERSE_LONG") return "text-emerald-300 bg-emerald-500/10 border-emerald-400/20";
    if (action === "ADD_SHORT" || action === "REVERSE_SHORT") return "text-amber-300 bg-amber-500/10 border-amber-400/20";
    return "text-rose-300 bg-rose-500/10 border-rose-400/20";
}

export default function PortfolioPolicyMonitor({ holdings, portfolioId }: { holdings: DashboardHolding[]; portfolioId: string }) {
    const { refreshPortfolio } = usePortfolio();
    const activeHoldings = holdings.filter((holding) => Math.abs(holding.shares) > 0);
    const { data, loading, refreshing, error, connected, refresh } = usePortfolioPolicy({
        holdings,
        portfolioId,
        enabled: activeHoldings.length > 0,
    });
    const [applyState, setApplyState] = React.useState<string | null>(null);
    const [applyMessage, setApplyMessage] = React.useState<string | null>(null);
    const [applyError, setApplyError] = React.useState<string | null>(null);

    const actionableAllocations = React.useMemo(
        () => (data?.allocations || []).filter((allocation) => allocation.action !== "HOLD" && allocation.action !== "LOCK" && Math.abs(allocation.delta_shares || 0) > 0.0001),
        [data],
    );

    const applyPolicy = async (symbols?: string[]) => {
        if (!data) {
            return;
        }

        setApplyState(symbols && symbols.length === 1 ? symbols[0] : "ALL");
        setApplyMessage(null);
        setApplyError(null);

        try {
            const response = await fetch(`${API_BASE}/api/v1/portfolios/policy/apply`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    portfolio_id: portfolioId,
                    holdings,
                    allocations: data.allocations,
                    symbols,
                }),
            });
            const payload = await response.json().catch(() => ({}));
            if (!response.ok) {
                throw new Error(payload.detail || "Failed to apply portfolio policy");
            }

            await refreshPortfolio();
            await refresh();
            setApplyMessage(
                symbols && symbols.length === 1
                    ? `Applied live rebalance for ${symbols[0]}.`
                    : `Applied live rebalance for ${payload.applied_symbols?.length || 0} symbols.`,
            );
        } catch (requestError) {
            setApplyError(requestError instanceof Error ? requestError.message : "Failed to apply portfolio policy");
        } finally {
            setApplyState(null);
        }
    };

    if (activeHoldings.length === 0) {
        return null;
    }

    return (
        <section className="relative overflow-hidden rounded-[28px] border border-cyan-400/15 bg-[radial-gradient(circle_at_top_left,rgba(34,211,238,0.16),transparent_28%),radial-gradient(circle_at_80%_20%,rgba(59,130,246,0.12),transparent_24%),rgba(9,14,24,0.92)] shadow-[0_24px_90px_rgba(0,0,0,0.35)]">
            <div className="absolute inset-0 bg-[linear-gradient(135deg,rgba(255,255,255,0.03),transparent_42%,rgba(34,211,238,0.05))]" />
            <div className="relative z-10 p-6 lg:p-7">
                <div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
                    <div className="flex items-start gap-4">
                        <div className="flex h-14 w-14 items-center justify-center rounded-2xl border border-cyan-400/20 bg-cyan-400/10 shadow-[0_0_40px_rgba(34,211,238,0.15)]">
                            <BrainCircuit size={24} className="text-cyan-300" />
                        </div>
                        <div className="space-y-2">
                            <div className="flex flex-wrap items-center gap-2">
                                <span className="rounded-full border border-cyan-400/20 bg-cyan-400/10 px-3 py-1 text-[10px] font-black uppercase tracking-[0.35em] text-cyan-200">EV policy function</span>
                                <span className="rounded-full border border-emerald-400/20 bg-emerald-400/10 px-3 py-1 text-[10px] font-black uppercase tracking-[0.28em] text-emerald-200">continuous monitor</span>
                            </div>
                            <div>
                                <h2 className="text-2xl font-black tracking-tight text-white">Portfolio EV Monitor</h2>
                                <p className="max-w-3xl text-sm leading-relaxed text-cyan-50/70">
                                    Observa en tiempo real la policy objetivo, el cambio de EV esperado y el rebalance sugerido sobre el estado vivo del portafolio.
                                </p>
                            </div>
                        </div>
                    </div>

                    <div className="flex flex-wrap items-center gap-2 text-[10px] font-black uppercase tracking-[0.28em] text-cyan-100/70">
                        <button
                            onClick={() => void applyPolicy()}
                            disabled={!data || actionableAllocations.length === 0 || applyState !== null}
                            className={`inline-flex items-center gap-2 rounded-full border px-3 py-2 transition-colors ${!data || actionableAllocations.length === 0 || applyState !== null ? "border-white/10 bg-white/5 text-cyan-100/40 cursor-not-allowed" : "border-cyan-400/20 bg-cyan-400/10 text-cyan-100 hover:bg-cyan-400/20"}`}
                        >
                            {applyState === "ALL" ? <Loader2 size={12} className="animate-spin" /> : <Play size={12} />}
                            apply rebalance
                        </button>
                        <span className="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-3 py-2">
                            <Activity size={12} className="text-emerald-300" />
                            {data?.summary.rebalance_required ? "rebalance active" : "tracking stable"}
                        </span>
                        <span className="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-3 py-2">
                            <RefreshCw size={12} className={refreshing ? "animate-spin text-cyan-300" : "text-cyan-300"} />
                            {connected ? (refreshing ? "tick sync" : "socket live") : "http fallback"}
                        </span>
                    </div>
                </div>

                {error && (
                    <div className="mt-4 flex items-center gap-3 rounded-2xl border border-rose-400/20 bg-rose-500/10 px-4 py-3 text-sm text-rose-100">
                        <ShieldAlert size={16} className="text-rose-300" />
                        <span>{error}</span>
                    </div>
                )}

                {applyError && (
                    <div className="mt-4 flex items-center gap-3 rounded-2xl border border-rose-400/20 bg-rose-500/10 px-4 py-3 text-sm text-rose-100">
                        <ShieldAlert size={16} className="text-rose-300" />
                        <span>{applyError}</span>
                    </div>
                )}

                {applyMessage && (
                    <div className="mt-4 flex items-center gap-3 rounded-2xl border border-emerald-400/20 bg-emerald-500/10 px-4 py-3 text-sm text-emerald-100">
                        <CheckCircle2 size={16} className="text-emerald-300" />
                        <span>{applyMessage}</span>
                    </div>
                )}

                <div className="mt-5 grid grid-cols-1 gap-3 md:grid-cols-2 xl:grid-cols-5">
                    <MetricCard icon={<TrendingUp size={16} className="text-cyan-300" />} label="Current EV" value={data ? formatSignedPercent(data.objective.current_expected_return_pct) : loading ? "..." : "--"} tone="cyan" />
                    <MetricCard icon={<Target size={16} className="text-emerald-300" />} label="Target EV" value={data ? formatSignedPercent(data.objective.target_expected_return_pct) : loading ? "..." : "--"} tone="emerald" />
                    <MetricCard icon={<ArrowRightLeft size={16} className="text-amber-300" />} label="EV Delta" value={data ? formatSignedPercent(data.objective.ev_delta_pct) : loading ? "..." : "--"} tone="amber" />
                    <MetricCard icon={<ShieldAlert size={16} className="text-rose-300" />} label="Target Risk" value={data ? `${data.objective.target_risk_pct.toFixed(2)}%` : loading ? "..." : "--"} tone="rose" />
                    <MetricCard icon={<Activity size={16} className="text-indigo-300" />} label="Confidence" value={data ? `${data.summary.confidence_pct.toFixed(1)}%` : loading ? "..." : "--"} tone="indigo" />
                </div>

                <div className="mt-4 grid grid-cols-1 gap-3 lg:grid-cols-[1.2fr_0.8fr]">
                    <div className="rounded-3xl border border-white/10 bg-white/[0.03] p-4 backdrop-blur-sm">
                        <div className="mb-3 flex items-center justify-between gap-4">
                            <div>
                                <h3 className="text-xs font-black uppercase tracking-[0.28em] text-cyan-100">Suggested Rotation</h3>
                                <p className="mt-1 text-xs text-cyan-50/60">Current weight, target weight, delta and action per asset.</p>
                            </div>
                            <span className="text-[10px] font-black uppercase tracking-[0.28em] text-cyan-100/60">
                                {data?.allocations.length ?? activeHoldings.length} assets
                            </span>
                        </div>

                        <div className="space-y-2">
                            {(data?.allocations || []).map((allocation) => (
                                <div key={allocation.symbol} className="grid grid-cols-1 gap-3 rounded-2xl border border-white/6 bg-black/20 px-4 py-3 lg:grid-cols-[1.4fr_0.9fr_0.9fr_0.9fr_0.8fr_1.2fr] lg:items-center">
                                    <div className="min-w-0">
                                        <div className="flex items-center gap-3">
                                            <span className="text-sm font-black tracking-tight text-white">{allocation.symbol}</span>
                                            <span className="text-[10px] font-black uppercase tracking-[0.24em] text-cyan-100/50">{allocation.sector}</span>
                                        </div>
                                        <p className="mt-1 truncate text-xs text-cyan-50/60">{allocation.rationale}</p>
                                    </div>
                                    <PolicyMiniStat label="Current" value={`${allocation.current_weight_pct.toFixed(2)}%`} />
                                    <PolicyMiniStat label="Target" value={`${allocation.target_weight_pct.toFixed(2)}%`} />
                                    <PolicyMiniStat label="Delta" value={formatSignedPercent(allocation.weight_delta_pct)} emphasis={allocation.weight_delta_pct >= 0 ? "positive" : "negative"} />
                                    <div className="flex flex-col gap-1">
                                        <span className="text-[10px] font-black uppercase tracking-[0.24em] text-cyan-100/50">Action</span>
                                        <div className="flex items-center gap-2 flex-wrap">
                                            <span className={`inline-flex w-fit items-center rounded-full border px-2.5 py-1 text-[10px] font-black uppercase tracking-[0.24em] ${actionTone(allocation.action)}`}>
                                                {allocation.action}
                                            </span>
                                            {allocation.action !== "HOLD" && allocation.action !== "LOCK" && Math.abs(allocation.delta_shares || 0) > 0.0001 && (
                                                <button
                                                    onClick={() => void applyPolicy([allocation.symbol])}
                                                    disabled={applyState !== null}
                                                    className={`inline-flex items-center gap-1 rounded-full border px-2.5 py-1 text-[10px] font-black uppercase tracking-[0.2em] transition-colors ${applyState !== null ? "border-white/10 bg-white/5 text-cyan-100/40 cursor-not-allowed" : "border-cyan-400/20 bg-cyan-400/10 text-cyan-100 hover:bg-cyan-400/20"}`}
                                                >
                                                    {applyState === allocation.symbol ? <Loader2 size={10} className="animate-spin" /> : <Play size={10} />}
                                                    apply
                                                </button>
                                            )}
                                        </div>
                                    </div>
                                    <div className="grid grid-cols-2 gap-2 lg:grid-cols-1">
                                        <PolicyMiniStat label="EV" value={formatSignedPercent(allocation.expected_value_pct)} emphasis={allocation.expected_value_pct >= 0 ? "positive" : "negative"} />
                                        <PolicyMiniStat label="Notional" value={formatSignedCurrency(allocation.delta_notional)} emphasis={allocation.delta_notional >= 0 ? "positive" : "negative"} />
                                    </div>
                                </div>
                            ))}

                            {!loading && data && data.allocations.length === 0 && (
                                <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-4 py-6 text-center text-sm text-cyan-50/60">
                                    No hay activos elegibles para policy monitoring.
                                </div>
                            )}
                        </div>
                    </div>

                    <div className="grid grid-cols-1 gap-3">
                        <aside className="rounded-3xl border border-white/10 bg-white/[0.03] p-4 backdrop-blur-sm">
                            <h3 className="text-xs font-black uppercase tracking-[0.28em] text-cyan-100">State Vector</h3>
                            <div className="mt-3 space-y-3 text-sm text-cyan-50/70">
                                <KeyValue label="Coverage" value={data ? `${data.summary.coverage_percent.toFixed(1)}%` : "--"} />
                                <KeyValue label="Cash buffer" value={data ? `${data.summary.target_cash_buffer_pct.toFixed(2)}%` : "--"} />
                                <KeyValue label="Risk delta" value={data ? formatSignedPercent(data.objective.risk_delta_pct) : "--"} />
                                <KeyValue label="Realized trade EV" value={data ? `$${data.objective.realized_trade_ev.toFixed(2)}` : "--"} />
                            </div>
                        </aside>

                        <aside className="rounded-3xl border border-white/10 bg-white/[0.03] p-4 backdrop-blur-sm">
                            <h3 className="text-xs font-black uppercase tracking-[0.28em] text-cyan-100">High Conviction</h3>
                            <div className="mt-3 flex flex-wrap gap-2">
                                {(data?.summary.high_conviction_symbols || []).map((symbol) => (
                                    <span key={symbol} className="rounded-full border border-emerald-400/20 bg-emerald-400/10 px-3 py-1.5 text-[10px] font-black uppercase tracking-[0.28em] text-emerald-200">
                                        {symbol}
                                    </span>
                                ))}
                                {data && data.summary.high_conviction_symbols.length === 0 && (
                                    <span className="text-xs text-cyan-50/50">No high-conviction assets yet.</span>
                                )}
                            </div>
                        </aside>

                        <aside className="rounded-3xl border border-white/10 bg-white/[0.03] p-4 backdrop-blur-sm">
                            <h3 className="text-xs font-black uppercase tracking-[0.28em] text-cyan-100">Last Snapshot</h3>
                            <p className="mt-3 text-sm text-cyan-50/70">
                                {data?.generated_at ? new Date(data.generated_at).toLocaleString() : loading ? "Loading policy snapshot..." : "No snapshot"}
                            </p>
                        </aside>
                    </div>
                </div>
            </div>
        </section>
    );
}

function MetricCard({ icon, label, value, tone }: { icon: React.ReactNode; label: string; value: string; tone: "cyan" | "emerald" | "amber" | "rose" | "indigo" }) {
    const tones: Record<string, string> = {
        cyan: "border-cyan-400/15 bg-cyan-400/8",
        emerald: "border-emerald-400/15 bg-emerald-400/8",
        amber: "border-amber-400/15 bg-amber-400/8",
        rose: "border-rose-400/15 bg-rose-400/8",
        indigo: "border-indigo-400/15 bg-indigo-400/8",
    };

    return (
        <div className={`rounded-2xl border p-4 ${tones[tone]}`}>
            <div className="flex items-center justify-between gap-3">
                <span className="text-[10px] font-black uppercase tracking-[0.28em] text-cyan-100/60">{label}</span>
                {icon}
            </div>
            <p className="mt-3 text-2xl font-black tracking-tight text-white">{value}</p>
        </div>
    );
}

function PolicyMiniStat({ label, value, emphasis = "neutral" }: { label: string; value: string; emphasis?: "neutral" | "positive" | "negative" }) {
    const emphasisClass = emphasis === "positive"
        ? "text-emerald-200"
        : emphasis === "negative"
            ? "text-rose-200"
            : "text-white";

    return (
        <div className="flex flex-col gap-1">
            <span className="text-[10px] font-black uppercase tracking-[0.24em] text-cyan-100/50">{label}</span>
            <span className={`text-sm font-black tracking-tight ${emphasisClass}`}>{value}</span>
        </div>
    );
}

function KeyValue({ label, value }: { label: string; value: string }) {
    return (
        <div className="flex items-center justify-between gap-4 rounded-2xl border border-white/6 bg-black/20 px-3 py-2.5">
            <span className="text-[10px] font-black uppercase tracking-[0.24em] text-cyan-100/50">{label}</span>
            <span className="text-sm font-black tracking-tight text-white">{value}</span>
        </div>
    );
}