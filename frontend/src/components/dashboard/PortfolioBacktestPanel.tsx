"use client";

import React, { useEffect, useMemo, useRef, useState } from "react";
import {
    Area,
    AreaChart,
    CartesianGrid,
    ResponsiveContainer,
    Tooltip,
    XAxis,
    YAxis,
} from "recharts";
import {
    Cpu,
    Loader2,
    Play,
    RefreshCw,
    Server,
    TriangleAlert,
    Wallet,
} from "lucide-react";

import { cachedFetch } from "@/lib/cachedFetch";
import { usePortfolio } from "@/context/PortfolioContext";
import { usePortfolioPolicy } from "@/hooks/usePortfolioPolicy";
import { MetricCard, BacktestPanel, DataSection } from "@/components/trading/BacktestUI";
import type { DashboardHolding } from "@/types/dashboard";

const API_BASE = "http://127.0.0.1:8282";

type SourceMode = "portfolio" | "manual";
type ExecutionMode = "auto" | "remote" | "cpp" | "python";

type EngineStatus = {
    default_mode: ExecutionMode;
    available_modes: ExecutionMode[];
    embedded_cpp_available: boolean;
    remote: {
        configured: boolean;
        url: string | null;
        healthy: boolean;
        service: string | null;
        error: string | null;
    };
};

type BacktestAsset = {
    symbol: string;
    name: string;
    target_weight: number;
    factor: number;
    shares: number;
    last_price: number;
    final_value: number;
    pnl_usd_vs_target_cost: number;
};

type BacktestTrade = {
    date: string;
    symbol: string;
    side: string;
    quantity: number;
    price: number;
    notional: number;
    fee: number;
};

type BacktestPoint = {
    date: string;
    equity: number;
    cash: number;
};

type BacktestKpis = {
    total_return_pct: number;
    cagr: number;
    max_drawdown_pct: number;
    volatility_ann_pct: number;
    sharpe_ratio: number;
    final_equity: number;
    trading_days: number;
};

type BacktestResult = {
    engine: string;
    execution_mode: ExecutionMode;
    start_date_used: string;
    end_date_used: string;
    rebalance_frequency: string;
    fee_bps: number;
    assets: BacktestAsset[];
    trades: BacktestTrade[];
    equity_curve: BacktestPoint[];
    kpis: BacktestKpis;
    engine_notes?: string[];
};

function toDateInput(date: Date) {
    return date.toISOString().slice(0, 10);
}

function formatCurrency(value: number) {
    return value.toLocaleString(undefined, {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
    });
}

function formatPercent(value: number, digits = 2) {
    return `${value.toFixed(digits)}%`;
}

function formatSignedPercent(value: number, digits = 2) {
    const prefix = value > 0 ? "+" : "";
    return `${prefix}${value.toFixed(digits)}%`;
}

function formatSignedCurrency(value: number) {
    const prefix = value > 0 ? "+" : "";
    return `${prefix}$${Math.abs(value).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
}

function modeLabel(mode: ExecutionMode) {
    if (mode === "remote") return "C++ Remote";
    if (mode === "cpp") return "C++ Embedded";
    if (mode === "python") return "Python";
    return "Auto";
}

function engineLabel(engine: string) {
    if (engine === "cpp-remote") return "C++ Remote";
    if (engine === "cpp") return "C++ Embedded";
    return "Python";
}

function parseManualBasket(text: string) {
    return text
        .split(/\r?\n/)
        .map((line) => line.trim())
        .filter(Boolean)
        .map((line) => {
            const [rawSymbol, rawWeight, rawFactor] = line.split(",").map((part) => part.trim());
            const symbol = String(rawSymbol || "").toUpperCase();
            if (!symbol) {
                throw new Error(`Invalid basket row: ${line}`);
            }

            const weight = rawWeight ? Number(rawWeight) : undefined;
            const factor = rawFactor ? Number(rawFactor) : 1.0;

            if (weight !== undefined && (!Number.isFinite(weight) || weight < 0)) {
                throw new Error(`Invalid weight for ${symbol}`);
            }
            if (!Number.isFinite(factor) || factor <= 0) {
                throw new Error(`Invalid factor for ${symbol}`);
            }

            return {
                symbol,
                weight,
                factor,
            };
        });
}

interface PortfolioBacktestPanelProps {
    activeHoldings: DashboardHolding[];
    totalValue: number;
}

export default function PortfolioBacktestPanel({
    activeHoldings,
    totalValue,
}: PortfolioBacktestPanelProps) {
    const { activePortfolio } = usePortfolio();
    const {
        data: livePolicy,
        loading: policyLoading,
        refreshing: policyRefreshing,
        error: policyError,
        connected: policyConnected,
    } = usePortfolioPolicy({
        holdings: activeHoldings,
        portfolioId: activePortfolio,
        enabled: activeHoldings.length > 0,
    });

    const today = useMemo(() => new Date(), []);
    const defaultEnd = useMemo(() => toDateInput(today), [today]);
    const defaultStart = useMemo(() => {
        const start = new Date(today);
        start.setFullYear(start.getFullYear() - 1);
        return toDateInput(start);
    }, [today]);

    const [sourceMode, setSourceMode] = useState<SourceMode>("portfolio");
    const [startDate, setStartDate] = useState(defaultStart);
    const [endDate, setEndDate] = useState(defaultEnd);
    const [initialCash, setInitialCash] = useState("10000");
    const [rebalanceFrequency, setRebalanceFrequency] = useState("none");
    const [feeBps, setFeeBps] = useState("0");
    const [executionMode, setExecutionMode] = useState<ExecutionMode>("auto");
    const [manualBasket, setManualBasket] = useState("");
    const [engineStatus, setEngineStatus] = useState<EngineStatus | null>(null);
    const [loadingEngines, setLoadingEngines] = useState(false);
    const [running, setRunning] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [result, setResult] = useState<BacktestResult | null>(null);
    const seededManualRef = useRef(false);

    const suggestedManualBasket = useMemo(() => {
        const baseValue = totalValue > 0
            ? totalValue
            : activeHoldings.reduce(
                (sum, holding) => sum + (Math.abs(holding.shares) * (holding.price || holding.entryPrice) * holding.factor),
                0,
            );

        if (baseValue <= 0) {
            return "AAPL,50\nMSFT,50";
        }

        return activeHoldings
            .slice(0, 8)
            .map((holding) => {
                const notional = Math.abs(holding.shares) * (holding.price || holding.entryPrice) * holding.factor;
                const weight = (notional / baseValue) * 100;
                return `${holding.symbol},${weight.toFixed(2)}${holding.factor !== 1 ? `,${holding.factor}` : ""}`;
            })
            .join("\n");
    }, [activeHoldings, totalValue]);

    const loadEngineStatus = async () => {
        setLoadingEngines(true);
        try {
            const response = await cachedFetch(`${API_BASE}/api/v1/portfolios/backtest/engines`);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }
            const data = await response.json();
            setEngineStatus(data);
        } catch (loadError) {
            setEngineStatus(null);
            console.error("[PortfolioBacktestPanel] engine status", loadError);
        } finally {
            setLoadingEngines(false);
        }
    };

    useEffect(() => {
        void loadEngineStatus();
    }, []);

    useEffect(() => {
        if (!seededManualRef.current && suggestedManualBasket) {
            setManualBasket(suggestedManualBasket);
            seededManualRef.current = true;
        }
    }, [suggestedManualBasket]);

    const equityChartData = useMemo(() => {
        return (result?.equity_curve ?? []).map((point) => ({
            label: point.date.slice(5),
            equity: point.equity,
            cash: point.cash,
        }));
    }, [result]);

    const allocationRows = useMemo(() => {
        const assets = result?.assets ?? [];
        const totalFinalValue = assets.reduce((sum, asset) => sum + asset.final_value, 0);
        return assets.map((asset) => ({
            ...asset,
            current_weight_pct: totalFinalValue > 0 ? (asset.final_value / totalFinalValue) * 100 : 0,
            target_weight_pct: asset.target_weight * 100,
        }));
    }, [result]);

    const recentTrades = useMemo(() => {
        return [...(result?.trades ?? [])].slice(-10).reverse();
    }, [result]);

    const activeBasketPreview = useMemo(() => {
        const baseValue = totalValue > 0
            ? totalValue
            : activeHoldings.reduce(
                (sum, holding) => sum + (Math.abs(holding.shares) * (holding.price || holding.entryPrice) * holding.factor),
                0,
            );

        return activeHoldings
            .map((holding) => {
                const notional = Math.abs(holding.shares) * (holding.price || holding.entryPrice) * holding.factor;
                return {
                    symbol: holding.symbol,
                    weightPct: baseValue > 0 ? (notional / baseValue) * 100 : 0,
                };
            })
            .sort((left, right) => right.weightPct - left.weightPct)
            .slice(0, 6);
    }, [activeHoldings, totalValue]);

    const livePolicyHighlights = useMemo(() => {
        return [...(livePolicy?.allocations ?? [])]
            .sort((left, right) => Math.abs(right.weight_delta_pct) - Math.abs(left.weight_delta_pct))
            .slice(0, 4);
    }, [livePolicy]);

    const policyComparisonRows = useMemo(() => {
        if (!livePolicy || !result) {
            return [];
        }

        const historicalAssets = result.assets ?? [];
        const finalValueTotal = historicalAssets.reduce((sum, asset) => sum + asset.final_value, 0);
        const liveMap = new Map(livePolicy.allocations.map((allocation) => [allocation.symbol, allocation]));
        const historicalMap = new Map(historicalAssets.map((asset) => [asset.symbol, asset]));
        const symbols = Array.from(new Set([...liveMap.keys(), ...historicalMap.keys()]));

        return symbols
            .map((symbol) => {
                const liveAllocation = liveMap.get(symbol);
                const historicalAsset = historicalMap.get(symbol);
                const backtestTargetPct = historicalAsset ? historicalAsset.target_weight * 100 : 0;
                const backtestFinalPct = historicalAsset && finalValueTotal > 0
                    ? (historicalAsset.final_value / finalValueTotal) * 100
                    : 0;

                return {
                    symbol,
                    action: liveAllocation?.action ?? "NO_SIGNAL",
                    liveTargetPct: liveAllocation?.target_weight_pct ?? 0,
                    liveCurrentPct: liveAllocation?.current_weight_pct ?? 0,
                    backtestTargetPct,
                    backtestFinalPct,
                    driftVsTargetPct: (liveAllocation?.target_weight_pct ?? 0) - backtestTargetPct,
                    driftVsFinalPct: (liveAllocation?.target_weight_pct ?? 0) - backtestFinalPct,
                    expectedReturnPct: liveAllocation?.expected_return_pct ?? 0,
                    confidence: liveAllocation?.confidence ?? 0,
                };
            })
            .sort((left, right) => Math.abs(right.driftVsTargetPct) - Math.abs(left.driftVsTargetPct));
    }, [livePolicy, result]);

    const policyComparisonSummary = useMemo(() => {
        if (policyComparisonRows.length === 0) {
            return null;
        }

        const avgTargetDrift = policyComparisonRows.reduce((sum, row) => sum + Math.abs(row.driftVsTargetPct), 0) / policyComparisonRows.length;
        const avgFinalDrift = policyComparisonRows.reduce((sum, row) => sum + Math.abs(row.driftVsFinalPct), 0) / policyComparisonRows.length;
        const changedCount = policyComparisonRows.filter((row) => Math.abs(row.driftVsTargetPct) >= 2).length;

        return {
            avgTargetDrift,
            avgFinalDrift,
            changedCount,
            leadSymbol: policyComparisonRows[0]?.symbol ?? null,
        };
    }, [policyComparisonRows]);

    const handleRun = async () => {
        const parsedCash = Number(initialCash);
        const parsedFeeBps = Number(feeBps);

        if (!Number.isFinite(parsedCash) || parsedCash <= 0) {
            setError("Initial cash must be greater than 0.");
            return;
        }
        if (!Number.isFinite(parsedFeeBps) || parsedFeeBps < 0) {
            setError("Fee bps must be 0 or greater.");
            return;
        }

        let assets: Array<{ symbol: string; weight?: number; factor: number }> = [];
        if (sourceMode === "manual") {
            try {
                assets = parseManualBasket(manualBasket);
            } catch (parseError) {
                setError(parseError instanceof Error ? parseError.message : "Invalid manual basket.");
                return;
            }

            if (assets.length === 0) {
                setError("Add at least one manual basket row before running the backtest.");
                return;
            }
        } else if (!activePortfolio) {
            setError("No active portfolio selected.");
            return;
        }

        setRunning(true);
        setError(null);
        setResult(null);

        try {
            const response = await fetch(`${API_BASE}/api/v1/portfolios/backtest`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    start_date: startDate,
                    end_date: endDate,
                    initial_cash: parsedCash,
                    portfolio_id: sourceMode === "portfolio" ? activePortfolio : null,
                    assets,
                    rebalance_frequency: rebalanceFrequency,
                    fee_bps: parsedFeeBps,
                    execution_mode: executionMode,
                }),
            });

            const data = await response.json();
            if (!response.ok) {
                setError(data?.detail || "Portfolio backtest failed.");
                return;
            }

            setResult(data);
            void loadEngineStatus();
        } catch (requestError) {
            setError(requestError instanceof Error ? requestError.message : "Backend unavailable.");
        } finally {
            setRunning(false);
        }
    };

    return (
        <div className="p-5 space-y-5">
            <div className="grid grid-cols-1 xl:grid-cols-[1.2fr_0.8fr] gap-5">
                <BacktestPanel
                    variant="cyan"
                    title="Portfolio Simulator"
                    subtitle="Buy On Start Date, Then Backtest"
                    headerRight={
                        <button
                            onClick={() => void loadEngineStatus()}
                            className="shrink-0 h-10 px-3 rounded-2xl border border-white/10 bg-black/20 text-xs font-black uppercase tracking-widest text-cyan-100/80 hover:bg-black/30 transition-colors flex items-center gap-2"
                        >
                            {loadingEngines ? <Loader2 size={14} className="animate-spin" /> : <RefreshCw size={14} />}
                            Engines
                        </button>
                    }
                >
                    <div className="space-y-5">
                        <div className="flex flex-wrap gap-2">
                            {(["portfolio", "manual"] as SourceMode[]).map((mode) => (
                                <button
                                    key={mode}
                                    onClick={() => setSourceMode(mode)}
                                    className={`px-3 py-2 rounded-2xl border text-[10px] font-black uppercase tracking-widest transition-colors ${sourceMode === mode
                                        ? "bg-cyan-500/15 border-cyan-400/40 text-cyan-200"
                                        : "bg-black/15 border-white/10 text-muted hover:text-white"
                                        }`}
                                >
                                    {mode === "portfolio" ? "Current Portfolio" : "Manual Basket"}
                                </button>
                            ))}
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-3">
                            <label className="space-y-1.5">
                                <span className="text-[10px] font-black uppercase tracking-widest text-muted">Start Date</span>
                                <input
                                    type="date"
                                    value={startDate}
                                    onChange={(event) => setStartDate(event.target.value)}
                                    className="w-full rounded-2xl border border-border bg-background/40 px-3 py-2.5 text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-cyan-400/30"
                                />
                            </label>
                            <label className="space-y-1.5">
                                <span className="text-[10px] font-black uppercase tracking-widest text-muted">End Date</span>
                                <input
                                    type="date"
                                    value={endDate}
                                    onChange={(event) => setEndDate(event.target.value)}
                                    className="w-full rounded-2xl border border-border bg-background/40 px-3 py-2.5 text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-cyan-400/30"
                                />
                            </label>
                            <label className="space-y-1.5">
                                <span className="text-[10px] font-black uppercase tracking-widest text-muted">Initial Cash</span>
                                <input
                                    type="number"
                                    min="100"
                                    step="100"
                                    value={initialCash}
                                    onChange={(event) => setInitialCash(event.target.value)}
                                    className="w-full rounded-2xl border border-border bg-background/40 px-3 py-2.5 text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-cyan-400/30"
                                />
                            </label>
                            <label className="space-y-1.5">
                                <span className="text-[10px] font-black uppercase tracking-widest text-muted">Execution Mode</span>
                                <select
                                    value={executionMode}
                                    onChange={(event) => setExecutionMode(event.target.value as ExecutionMode)}
                                    className="w-full rounded-2xl border border-border bg-background/40 px-3 py-2.5 text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-cyan-400/30"
                                >
                                    <option value="auto">Auto</option>
                                    <option value="remote">C++ Remote</option>
                                    <option value="cpp">C++ Embedded</option>
                                    <option value="python">Python</option>
                                </select>
                            </label>
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                            <label className="space-y-1.5">
                                <span className="text-[10px] font-black uppercase tracking-widest text-muted">Rebalance</span>
                                <select
                                    value={rebalanceFrequency}
                                    onChange={(event) => setRebalanceFrequency(event.target.value)}
                                    className="w-full rounded-2xl border border-border bg-background/40 px-3 py-2.5 text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-cyan-400/30"
                                >
                                    <option value="none">None</option>
                                    <option value="weekly">Weekly</option>
                                    <option value="monthly">Monthly</option>
                                    <option value="quarterly">Quarterly</option>
                                </select>
                            </label>
                            <label className="space-y-1.5">
                                <span className="text-[10px] font-black uppercase tracking-widest text-muted">Fees (bps)</span>
                                <input
                                    type="number"
                                    min="0"
                                    max="500"
                                    step="1"
                                    value={feeBps}
                                    onChange={(event) => setFeeBps(event.target.value)}
                                    className="w-full rounded-2xl border border-border bg-background/40 px-3 py-2.5 text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-cyan-400/30"
                                />
                            </label>
                        </div>

                        {sourceMode === "manual" ? (
                            <label className="block space-y-1.5">
                                <span className="text-[10px] font-black uppercase tracking-widest text-muted">Manual Basket</span>
                                <textarea
                                    value={manualBasket}
                                    onChange={(event) => setManualBasket(event.target.value)}
                                    rows={7}
                                    className="w-full rounded-3xl border border-border bg-background/40 px-4 py-3 text-sm text-foreground font-mono resize-y focus:outline-none focus:ring-2 focus:ring-cyan-400/30"
                                    placeholder={"AAPL,60\nMSFT,25\nGLD,15,1.0"}
                                />
                            </label>
                        ) : (
                            <div className="rounded-3xl border border-white/10 bg-black/15 px-4 py-4">
                                <div className="flex items-center justify-between gap-3 mb-3">
                                    <div>
                                        <p className="text-[10px] font-black uppercase tracking-widest text-cyan-100/80">Saved Portfolio Source</p>
                                        <p className="text-sm font-bold text-white mt-1">{activePortfolio} · {activeHoldings.length} live holdings</p>
                                    </div>
                                    <div className="text-right">
                                        <p className="text-[10px] text-muted uppercase tracking-widest">Current Gross Value</p>
                                        <p className="text-lg font-black text-white">${formatCurrency(totalValue)}</p>
                                    </div>
                                </div>
                                <div className="grid grid-cols-2 md:grid-cols-3 gap-2">
                                    {activeBasketPreview.map((holding) => (
                                        <div key={holding.symbol} className="rounded-2xl border border-white/5 bg-white/[0.03] px-3 py-2">
                                            <p className="text-xs font-black text-white">{holding.symbol}</p>
                                            <p className="text-[10px] font-mono text-cyan-200/80 mt-1">{holding.weightPct.toFixed(2)}%</p>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {error && (
                            <div className="rounded-2xl border border-red-500/25 bg-red-500/10 px-4 py-3 text-sm text-red-100 flex items-start gap-2">
                                <TriangleAlert size={16} className="mt-0.5 shrink-0 text-red-300" />
                                <span>{error}</span>
                            </div>
                        )}

                        <button
                            onClick={handleRun}
                            disabled={running}
                            className={`w-full rounded-3xl px-4 py-3.5 text-sm font-black uppercase tracking-[0.2em] transition-all flex items-center justify-center gap-2 ${running
                                ? "bg-cyan-500/40 text-white cursor-not-allowed"
                                : "bg-cyan-500 text-slate-950 hover:bg-cyan-400 shadow-[0_0_30px_rgba(34,211,238,0.18)]"
                                }`}
                        >
                            {running ? <Loader2 size={16} className="animate-spin" /> : <Play size={16} fill="currentColor" />}
                            {running ? "Running Backtest" : "Run Portfolio Backtest"}
                        </button>
                    </div>
                </BacktestPanel>

                <div className="rounded-3xl border border-white/10 bg-black/15 overflow-hidden">
                    <div className="px-5 py-4 border-b border-white/5 flex items-center justify-between gap-3">
                        <div>
                            <p className="text-[10px] font-black uppercase tracking-[0.3em] text-cyan-100/80">Engine Mesh</p>
                            <h3 className="text-base font-black text-white mt-1">Runtime Routing</h3>
                        </div>
                        <Cpu size={18} className="text-cyan-300" />
                    </div>

                    <div className="p-5 space-y-4">
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                            <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-4 py-3">
                                <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-muted">
                                    <Server size={12} /> Remote C++ Service
                                </div>
                                <p className={`text-sm font-black mt-2 ${engineStatus?.remote.healthy ? "text-green-300" : engineStatus?.remote.configured ? "text-amber-300" : "text-zinc-400"}`}>
                                    {engineStatus?.remote.healthy ? "Healthy" : engineStatus?.remote.configured ? "Configured but offline" : "Not configured"}
                                </p>
                                <p className="text-[10px] text-muted mt-2 break-all font-mono">{engineStatus?.remote.url ?? "PORTFOLIO_CPP_SERVICE_URL"}</p>
                            </div>
                            <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-4 py-3">
                                <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-muted">
                                    <Cpu size={12} /> Embedded Core
                                </div>
                                <p className={`text-sm font-black mt-2 ${engineStatus?.embedded_cpp_available ? "text-green-300" : "text-zinc-400"}`}>
                                    {engineStatus?.embedded_cpp_available ? "Available" : "Unavailable"}
                                </p>
                                <p className="text-[10px] text-muted mt-2">Python fallback remains available even when native paths are down.</p>
                            </div>
                        </div>

                        <div className="rounded-2xl border border-white/10 bg-gradient-to-br from-cyan-500/10 to-transparent px-4 py-4">
                            <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-cyan-100/80">
                                <Wallet size={12} /> Selected Run Mode
                            </div>
                            <p className="text-xl font-black text-white mt-2">{modeLabel(executionMode)}</p>
                            <p className="text-[11px] text-muted mt-2">
                                `auto` tries remote C++, then embedded C++, then Python. Force `remote` to validate the standalone microservice path end to end.
                            </p>
                        </div>

                        {engineStatus?.remote.error && (
                            <div className="rounded-2xl border border-amber-500/20 bg-amber-500/10 px-4 py-3 text-[11px] text-amber-100">
                                Remote health check: {engineStatus.remote.error}
                            </div>
                        )}

                        {result?.engine_notes && result.engine_notes.length > 0 && (
                            <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-4 py-3 space-y-2">
                                <p className="text-[10px] font-black uppercase tracking-widest text-muted">Engine Notes</p>
                                {result.engine_notes.map((note) => (
                                    <p key={note} className="text-[11px] text-zinc-300 font-mono break-all">{note}</p>
                                ))}
                            </div>
                        )}

                        <div className="rounded-2xl border border-cyan-500/20 bg-gradient-to-br from-cyan-500/10 to-transparent px-4 py-4 space-y-4">
                            <div className="flex items-start justify-between gap-3">
                                <div>
                                    <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-cyan-100/80">
                                        <RefreshCw size={12} className={policyRefreshing ? "animate-spin" : ""} /> Live EV Policy Stream
                                    </div>
                                    <p className="text-[11px] text-muted mt-2">
                                        Socket-driven portfolio policy snapshot aligned with the current live holdings.
                                    </p>
                                </div>
                                <span className={`rounded-full border px-2.5 py-1 text-[10px] font-black uppercase tracking-[0.2em] ${policyConnected ? "border-emerald-400/25 bg-emerald-500/10 text-emerald-200" : "border-amber-400/25 bg-amber-500/10 text-amber-200"}`}>
                                    {policyConnected ? "socket" : "fallback"}
                                </span>
                            </div>

                            {policyError && (
                                <div className="rounded-2xl border border-amber-500/20 bg-amber-500/10 px-4 py-3 text-[11px] text-amber-100">
                                    {policyError}
                                </div>
                            )}

                            {policyLoading && !livePolicy ? (
                                <div className="flex items-center gap-2 text-sm text-zinc-300">
                                    <Loader2 size={14} className="animate-spin text-cyan-300" />
                                    Loading live portfolio policy...
                                </div>
                            ) : livePolicy ? (
                                <>
                                    <div className="grid grid-cols-2 gap-3">
                                        <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-3 py-3">
                                            <p className="text-[10px] font-black uppercase tracking-widest text-muted">Target EV</p>
                                            <p className="text-lg font-black text-white mt-2">{formatSignedPercent(livePolicy.objective.target_expected_return_pct)}</p>
                                        </div>
                                        <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-3 py-3">
                                            <p className="text-[10px] font-black uppercase tracking-widest text-muted">EV Delta</p>
                                            <p className={`text-lg font-black mt-2 ${livePolicy.objective.ev_delta_pct >= 0 ? "text-green" : "text-red"}`}>{formatSignedPercent(livePolicy.objective.ev_delta_pct)}</p>
                                        </div>
                                        <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-3 py-3">
                                            <p className="text-[10px] font-black uppercase tracking-widest text-muted">Confidence</p>
                                            <p className="text-lg font-black text-cyan-100 mt-2">{livePolicy.summary.confidence_pct.toFixed(1)}%</p>
                                        </div>
                                        <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-3 py-3">
                                            <p className="text-[10px] font-black uppercase tracking-widest text-muted">Cash Buffer</p>
                                            <p className="text-lg font-black text-cyan-100 mt-2">{livePolicy.summary.target_cash_buffer_pct.toFixed(2)}%</p>
                                        </div>
                                    </div>

                                    <div className="space-y-2">
                                        {livePolicyHighlights.map((allocation) => (
                                            <div key={allocation.symbol} className="rounded-2xl border border-white/10 bg-black/20 px-3 py-3">
                                                <div className="flex items-center justify-between gap-3">
                                                    <div>
                                                        <p className="text-sm font-black text-white">{allocation.symbol}</p>
                                                        <p className="text-[10px] text-muted mt-1">{allocation.action} · target {allocation.target_weight_pct.toFixed(2)}%</p>
                                                    </div>
                                                    <div className="text-right">
                                                        <p className={`text-sm font-black ${allocation.weight_delta_pct >= 0 ? "text-green" : "text-red"}`}>{formatSignedPercent(allocation.weight_delta_pct)}</p>
                                                        <p className="text-[10px] text-cyan-200/80 mt-1">{formatSignedCurrency(allocation.delta_notional)}</p>
                                                    </div>
                                                </div>
                                            </div>
                                        ))}
                                    </div>

                                    {sourceMode !== "portfolio" && (
                                        <p className="text-[10px] text-muted font-mono">
                                            Historical comparison uses this live policy only when the backtest source is Current Portfolio.
                                        </p>
                                    )}
                                </>
                            ) : (
                                <p className="text-sm text-muted">No live policy snapshot available.</p>
                            )}
                        </div>
                    </div>
                </div>
            </div>

            {result && (
                <>
                <div className="grid grid-cols-2 xl:grid-cols-5 gap-3">
                    <MetricCard label="Engine" value={engineLabel(result.engine)} variant="cyan" />
                    <MetricCard label="Final Equity" value={`$${formatCurrency(result.kpis.final_equity)}`} />
                    <MetricCard
                        label="Total Return"
                        value={formatPercent(result.kpis.total_return_pct)}
                        variant={result.kpis.total_return_pct >= 0 ? "emerald" : "rose"}
                    />
                    <MetricCard label="Sharpe" value={result.kpis.sharpe_ratio.toFixed(2)} variant="amber" />
                    <MetricCard label="Max Drawdown" value={formatPercent(result.kpis.max_drawdown_pct)} variant="rose" />
                </div>

                    <div className="grid grid-cols-1 xl:grid-cols-[1.15fr_0.85fr] gap-5">
                        <div className="rounded-3xl border border-white/10 bg-card-hover/20 overflow-hidden">
                            <div className="px-5 py-4 border-b border-white/5 flex items-center justify-between gap-3">
                                <div>
                                    <p className="text-[10px] font-black uppercase tracking-[0.3em] text-cyan-100/80">Equity Trajectory</p>
                                    <p className="text-sm text-muted mt-1">{result.start_date_used} to {result.end_date_used} · {result.kpis.trading_days} sessions</p>
                                </div>
                                <p className="text-xs font-mono text-cyan-200/80">{result.rebalance_frequency}</p>
                            </div>
                            <div className="p-4 h-80">
                                <ResponsiveContainer width="100%" height="100%">
                                    <AreaChart data={equityChartData} margin={{ top: 10, right: 12, left: 0, bottom: 0 }}>
                                        <defs>
                                            <linearGradient id="portfolioBacktestEquity" x1="0" y1="0" x2="0" y2="1">
                                                <stop offset="5%" stopColor="#22d3ee" stopOpacity={0.35} />
                                                <stop offset="95%" stopColor="#22d3ee" stopOpacity={0.02} />
                                            </linearGradient>
                                        </defs>
                                        <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
                                        <XAxis dataKey="label" tick={{ fill: "#71717a", fontSize: 10 }} minTickGap={24} />
                                        <YAxis tick={{ fill: "#71717a", fontSize: 10 }} tickFormatter={(value) => `$${Number(value).toFixed(0)}`} width={70} />
                                        <Tooltip formatter={(value) => [`$${formatCurrency(Number(value ?? 0))}`, "Equity"]} />
                                        <Area type="monotone" dataKey="equity" stroke="#22d3ee" fill="url(#portfolioBacktestEquity)" strokeWidth={2} />
                                    </AreaChart>
                                </ResponsiveContainer>
                            </div>
                        </div>

                        <div className="rounded-3xl border border-white/10 bg-card-hover/20 overflow-hidden">
                            <div className="px-5 py-4 border-b border-white/5">
                                <p className="text-[10px] font-black uppercase tracking-[0.3em] text-cyan-100/80">Allocation Outcome</p>
                                <p className="text-sm text-muted mt-1">Target weight versus realized terminal weight</p>
                            </div>
                            <div className="p-4 space-y-3 max-h-80 overflow-y-auto">
                                {allocationRows.map((asset) => (
                                    <div key={asset.symbol} className="rounded-2xl border border-white/5 bg-white/[0.03] px-4 py-3">
                                        <div className="flex items-center justify-between gap-3">
                                            <div>
                                                <p className="text-sm font-black text-white">{asset.symbol}</p>
                                                <p className="text-[10px] text-muted mt-1 font-mono">{asset.shares.toFixed(4)} shares · factor {asset.factor}</p>
                                            </div>
                                            <div className="text-right">
                                                <p className="text-sm font-black text-white">${formatCurrency(asset.final_value)}</p>
                                                <p className={`text-[10px] font-mono mt-1 ${asset.pnl_usd_vs_target_cost >= 0 ? "text-green" : "text-red"}`}>
                                                    {asset.pnl_usd_vs_target_cost >= 0 ? "+" : ""}${formatCurrency(asset.pnl_usd_vs_target_cost)}
                                                </p>
                                            </div>
                                        </div>
                                        <div className="mt-3 space-y-2">
                                            <div>
                                                <div className="flex items-center justify-between text-[10px] font-black uppercase tracking-widest text-muted mb-1">
                                                    <span>Target</span>
                                                    <span>{asset.target_weight_pct.toFixed(2)}%</span>
                                                </div>
                                                <div className="h-2 rounded-full bg-white/5 overflow-hidden">
                                                    <div className="h-full bg-cyan-400" style={{ width: `${Math.min(asset.target_weight_pct, 100)}%` }} />
                                                </div>
                                            </div>
                                            <div>
                                                <div className="flex items-center justify-between text-[10px] font-black uppercase tracking-widest text-muted mb-1">
                                                    <span>Final</span>
                                                    <span>{asset.current_weight_pct.toFixed(2)}%</span>
                                                </div>
                                                <div className="h-2 rounded-full bg-white/5 overflow-hidden">
                                                    <div className="h-full bg-amber-400" style={{ width: `${Math.min(asset.current_weight_pct, 100)}%` }} />
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>

                    {sourceMode === "portfolio" && (
                        <div className="rounded-3xl border border-cyan-500/20 bg-[radial-gradient(circle_at_top_left,rgba(34,211,238,0.10),transparent_42%),rgba(15,23,42,0.35)] overflow-hidden">
                            <div className="px-5 py-4 border-b border-white/5 flex items-center justify-between gap-3">
                                <div>
                                    <p className="text-[10px] font-black uppercase tracking-[0.3em] text-cyan-100/80">Policy vs Historical Rebalance</p>
                                    <p className="text-sm text-muted mt-1">Live policy target weight versus backtest target and realized terminal allocation</p>
                                </div>
                                <p className="text-xs font-mono text-cyan-200/80">{policyComparisonRows.length} symbols</p>
                            </div>

                            <div className="p-4 space-y-4">
                                {policyError && (
                                    <div className="rounded-2xl border border-amber-500/20 bg-amber-500/10 px-4 py-3 text-[11px] text-amber-100">
                                        {policyError}
                                    </div>
                                )}

                                {policyLoading && !livePolicy ? (
                                    <div className="flex items-center gap-2 text-sm text-zinc-300">
                                        <Loader2 size={14} className="animate-spin text-cyan-300" />
                                        Building policy comparison...
                                    </div>
                                ) : livePolicy && policyComparisonSummary ? (
                                    <>
                                        <div className="grid grid-cols-2 xl:grid-cols-4 gap-3">
                                            <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-4 py-3">
                                                <p className="text-[10px] font-black uppercase tracking-widest text-muted">Avg Drift vs Target</p>
                                                <p className="text-lg font-black text-white mt-2">{policyComparisonSummary.avgTargetDrift.toFixed(2)}%</p>
                                            </div>
                                            <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-4 py-3">
                                                <p className="text-[10px] font-black uppercase tracking-widest text-muted">Avg Drift vs Final</p>
                                                <p className="text-lg font-black text-white mt-2">{policyComparisonSummary.avgFinalDrift.toFixed(2)}%</p>
                                            </div>
                                            <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-4 py-3">
                                                <p className="text-[10px] font-black uppercase tracking-widest text-muted">Policy Changes</p>
                                                <p className="text-lg font-black text-cyan-100 mt-2">{policyComparisonSummary.changedCount}</p>
                                            </div>
                                            <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-4 py-3">
                                                <p className="text-[10px] font-black uppercase tracking-widest text-muted">Lead Drift Symbol</p>
                                                <p className="text-lg font-black text-cyan-100 mt-2">{policyComparisonSummary.leadSymbol ?? "—"}</p>
                                            </div>
                                        </div>

                                        <div className="overflow-x-auto">
                                            <table className="w-full text-sm">
                                                <thead>
                                                    <tr className="text-left text-[10px] font-black uppercase tracking-widest text-muted border-b border-white/5">
                                                        <th className="px-4 py-3">Symbol</th>
                                                        <th className="px-4 py-3">Action</th>
                                                        <th className="px-4 py-3 text-right">Live Target</th>
                                                        <th className="px-4 py-3 text-right">Backtest Target</th>
                                                        <th className="px-4 py-3 text-right">Backtest Final</th>
                                                        <th className="px-4 py-3 text-right">Drift vs Target</th>
                                                        <th className="px-4 py-3 text-right">Drift vs Final</th>
                                                        <th className="px-4 py-3 text-right">Exp. Return</th>
                                                        <th className="px-4 py-3 text-right">Confidence</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    {policyComparisonRows.map((row) => (
                                                        <tr key={row.symbol} className="border-b border-white/5 last:border-b-0">
                                                            <td className="px-4 py-3 font-black text-white">{row.symbol}</td>
                                                            <td className="px-4 py-3 text-cyan-200 font-mono">{row.action}</td>
                                                            <td className="px-4 py-3 text-right font-mono text-white">{row.liveTargetPct.toFixed(2)}%</td>
                                                            <td className="px-4 py-3 text-right font-mono text-zinc-300">{row.backtestTargetPct.toFixed(2)}%</td>
                                                            <td className="px-4 py-3 text-right font-mono text-zinc-300">{row.backtestFinalPct.toFixed(2)}%</td>
                                                            <td className={`px-4 py-3 text-right font-mono ${row.driftVsTargetPct >= 0 ? "text-green" : "text-red"}`}>{formatSignedPercent(row.driftVsTargetPct)}</td>
                                                            <td className={`px-4 py-3 text-right font-mono ${row.driftVsFinalPct >= 0 ? "text-green" : "text-red"}`}>{formatSignedPercent(row.driftVsFinalPct)}</td>
                                                            <td className={`px-4 py-3 text-right font-mono ${row.expectedReturnPct >= 0 ? "text-cyan-200" : "text-red"}`}>{formatSignedPercent(row.expectedReturnPct)}</td>
                                                            <td className="px-4 py-3 text-right font-mono text-cyan-100">{row.confidence.toFixed(1)}%</td>
                                                        </tr>
                                                    ))}
                                                </tbody>
                                            </table>
                                        </div>
                                    </>
                                ) : (
                                    <p className="text-sm text-muted">Run the portfolio source path to compare the live policy against the historical rebalance outcome.</p>
                                )}
                            </div>
                        </div>
                    )}

                    <div className="rounded-3xl border border-white/10 bg-card-hover/20 overflow-hidden">
                        <div className="px-5 py-4 border-b border-white/5 flex items-center justify-between gap-3">
                            <div>
                                <p className="text-[10px] font-black uppercase tracking-[0.3em] text-cyan-100/80">Trade Tape</p>
                                <p className="text-sm text-muted mt-1">Latest rebalance and entry flow from the selected execution path</p>
                            </div>
                            <p className="text-xs font-mono text-zinc-400">{result.trades.length} trades</p>
                        </div>
                        <div className="overflow-x-auto">
                            <table className="w-full text-sm">
                                <thead>
                                    <tr className="text-left text-[10px] font-black uppercase tracking-widest text-muted border-b border-white/5">
                                        <th className="px-4 py-3">Date</th>
                                        <th className="px-4 py-3">Symbol</th>
                                        <th className="px-4 py-3">Side</th>
                                        <th className="px-4 py-3 text-right">Qty</th>
                                        <th className="px-4 py-3 text-right">Price</th>
                                        <th className="px-4 py-3 text-right">Notional</th>
                                        <th className="px-4 py-3 text-right">Fee</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {recentTrades.length === 0 && (
                                        <tr>
                                            <td colSpan={7} className="px-4 py-6 text-center text-muted">No trades were generated for this run.</td>
                                        </tr>
                                    )}
                                    {recentTrades.map((trade) => (
                                        <tr key={`${trade.date}-${trade.symbol}-${trade.side}-${trade.quantity}`} className="border-b border-white/5 last:border-b-0">
                                            <td className="px-4 py-3 font-mono text-xs text-zinc-400">{trade.date}</td>
                                            <td className="px-4 py-3 font-black text-white">{trade.symbol}</td>
                                            <td className={`px-4 py-3 font-black ${trade.side === "BUY" ? "text-green" : "text-red"}`}>{trade.side}</td>
                                            <td className="px-4 py-3 text-right font-mono">{trade.quantity.toFixed(4)}</td>
                                            <td className="px-4 py-3 text-right font-mono">${formatCurrency(trade.price)}</td>
                                            <td className="px-4 py-3 text-right font-mono">${formatCurrency(trade.notional)}</td>
                                            <td className="px-4 py-3 text-right font-mono text-zinc-400">${formatCurrency(trade.fee)}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </>
            )}
        </div>
    );
}