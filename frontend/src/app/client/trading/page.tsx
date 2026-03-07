"use client"

import dynamic from "next/dynamic";
import AppLayout from "@/components/layout/AppLayout";
import { useEffect, useState } from "react";
import {
    Activity,
    Calendar,
    CandlestickChart,
    Download,
    ExternalLink as ExternalLinkIcon,
    FileTerminal,
    Loader2,
    Play,
    TriangleAlert,
    Zap,
} from "lucide-react";
import {
    Area,
    AreaChart,
    Bar,
    BarChart,
    CartesianGrid,
    Cell,
    ComposedChart,
    Line,
    ReferenceArea,
    ResponsiveContainer,
    Tooltip,
    XAxis,
    YAxis,
} from "recharts";

import { usePortfolio } from "@/context/PortfolioContext";
import { useSocket } from "@/context/SocketContext";

const PortfolioBacktestPanel = dynamic(() => import("@/components/dashboard/PortfolioBacktestPanel"), {
    ssr: false,
    loading: () => (
        <div className="h-[280px] flex items-center justify-center">
            <div className="h-6 w-6 border-2 border-accent border-t-transparent rounded-full animate-spin" />
        </div>
    ),
});

const API_BASE = "http://127.0.0.1:8282";

type KpiSnapshot = {
    total_trades: number;
    wins: number;
    losses: number;
    win_rate: number;
    expectancy_r: number;
    profit_factor: number;
    max_drawdown_pct: number;
    sharpe_ratio: number;
    avg_rr_realized: number;
    total_r: number;
    final_equity: number;
    cagr: number;
};

type LiveTrade = {
    signal_id: string;
    timestamp: string;
    direction: string;
    entry: number;
    stop: number;
    tp: number;
    outcome: string;
    pnl_r: number;
    pnl_usd: number;
    exit_price?: number;
    exit_timestamp?: string;
};

type ProgressState = {
    day: number;
    total: number;
    pct: number;
};

type BootstrapLiveData = {
    iterations: number;
    net_profit_95_ci: [number, number];
    max_drawdown_95_ci_pct: [number, number];
    net_profit_samples: number[];
    max_drawdown_samples: number[];
};

type CompletedResult = {
    sim_id: string;
    symbol: string;
    strategy: string;
    status: string;
    kpis: KpiSnapshot;
    trading_days: number;
    total_trades: number;
    bootstrap?: {
        iterations: number;
        net_profit_95_ci: [number, number];
        max_drawdown_95_ci_pct: [number, number];
    } | null;
    report_url?: string | null;
};

type EquityPoint = {
    label: string;
    equity: number;
};

function formatCurrency(value: number) {
    return value.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function formatRatio(value: number) {
    if (!Number.isFinite(value)) return "Inf";
    return value.toFixed(2);
}

function formatFractionPercent(value: number) {
    return `${(value * 100).toFixed(2)}%`;
}

function formatTimestampLabel(value?: string, index?: number) {
    if (!value) return index === 0 ? "Start" : `Trade ${index}`;
    return value.replace("T", " ").slice(5, 16);
}

function buildEquityCurve(trades: LiveTrade[], initialEquity: number): EquityPoint[] {
    const points: EquityPoint[] = [{ label: "Start", equity: initialEquity }];
    let runningEquity = initialEquity;

    trades.forEach((trade, index) => {
        runningEquity += Number(trade.pnl_usd || 0);
        points.push({
            label: formatTimestampLabel(trade.exit_timestamp || trade.timestamp, index + 1),
            equity: Number(runningEquity.toFixed(2)),
        });
    });

    return points;
}

function deriveLiveKpis(trades: LiveTrade[], initialEquity: number): KpiSnapshot {
    if (trades.length === 0) {
        return {
            total_trades: 0,
            wins: 0,
            losses: 0,
            win_rate: 0,
            expectancy_r: 0,
            profit_factor: 0,
            max_drawdown_pct: 0,
            sharpe_ratio: 0,
            avg_rr_realized: 0,
            total_r: 0,
            final_equity: initialEquity,
            cagr: 0,
        };
    }

    const wins = trades.filter((trade) => trade.pnl_usd > 0);
    const losses = trades.filter((trade) => trade.pnl_usd < 0);
    const totalTrades = trades.length;
    const winRate = wins.length / totalTrades;
    const avgWinR = wins.length ? wins.reduce((sum, trade) => sum + trade.pnl_r, 0) / wins.length : 0;
    const avgLossR = losses.length ? losses.reduce((sum, trade) => sum + Math.abs(trade.pnl_r), 0) / losses.length : 0;
    const expectancy = (winRate * avgWinR) - ((1 - winRate) * avgLossR);
    const grossProfit = wins.reduce((sum, trade) => sum + trade.pnl_usd, 0);
    const grossLoss = losses.reduce((sum, trade) => sum + Math.abs(trade.pnl_usd), 0);
    const profitFactor = grossLoss > 0 ? grossProfit / grossLoss : (grossProfit > 0 ? Number.POSITIVE_INFINITY : 0);

    let equity = initialEquity;
    let peak = initialEquity;
    let maxDrawdown = 0;
    const returns: number[] = [];

    trades.forEach((trade) => {
        const previousEquity = equity;
        equity += trade.pnl_usd;
        returns.push(previousEquity > 0 ? (equity - previousEquity) / previousEquity : 0);
        if (equity > peak) peak = equity;
        const drawdown = peak > 0 ? (peak - equity) / peak : 0;
        if (drawdown > maxDrawdown) maxDrawdown = drawdown;
    });

    let sharpe = 0;
    if (returns.length > 1) {
        const avg = returns.reduce((sum, value) => sum + value, 0) / returns.length;
        const variance = returns.reduce((sum, value) => sum + ((value - avg) ** 2), 0) / (returns.length - 1);
        const std = Math.sqrt(variance);
        sharpe = std > 0 ? (avg / std) * Math.sqrt(252) : 0;
    }

    const totalR = trades.reduce((sum, trade) => sum + trade.pnl_r, 0);
    const avgRR = wins.length ? wins.reduce((sum, trade) => sum + Math.abs(trade.pnl_r), 0) / wins.length : 0;

    return {
        total_trades: totalTrades,
        wins: wins.length,
        losses: losses.length,
        win_rate: Number(winRate.toFixed(4)),
        expectancy_r: Number(expectancy.toFixed(4)),
        profit_factor: Number.isFinite(profitFactor) ? Number(profitFactor.toFixed(4)) : Number.POSITIVE_INFINITY,
        max_drawdown_pct: Number(maxDrawdown.toFixed(4)),
        sharpe_ratio: Number(sharpe.toFixed(4)),
        avg_rr_realized: Number(avgRR.toFixed(4)),
        total_r: Number(totalR.toFixed(4)),
        final_equity: Number(equity.toFixed(2)),
        cagr: 0,
    };
}

function buildHistogramData(samples: number[], bins = 18) {
    if (samples.length === 0) return [];

    const min = Math.min(...samples);
    const max = Math.max(...samples);
    if (min === max) {
        return [{ label: min.toFixed(0), count: samples.length, color: min >= 0 ? "#22c55e" : "#ef4444" }];
    }

    const width = (max - min) / bins;
    const histogram = Array.from({ length: bins }, (_, index) => ({
        from: min + index * width,
        to: min + (index + 1) * width,
        count: 0,
    }));

    samples.forEach((sample) => {
        const bucket = Math.min(bins - 1, Math.floor((sample - min) / width));
        histogram[bucket].count += 1;
    });

    return histogram.map((bucket) => ({
        label: bucket.from.toFixed(0),
        count: bucket.count,
        color: (bucket.from + bucket.to) / 2 >= 0 ? "#22c55e" : "#ef4444",
    }));
}

// ─── Regime types ─────────────────────────────────────────────────────────────
type RegimeDist = {
    mean_ret: number;
    std_ret: number;
    annualized_vol_pct: number;
    annualized_ret_pct: number;
    sharpe: number;
    count: number;
    label: string;
    color: string;
};
type RegimeData = {
    regime_sequence: { date: string; state: number; vol: number; ret: number }[];
    state_colors: Record<string, string>;
    state_labels: Record<string, string>;
    distributions: Record<string, RegimeDist>;
    transition_matrix: number[][];
    current_label: string;
    next_probs: Record<string, number>;
};

const REGIME_FILL: Record<number, string> = { 0: "#22c55e", 1: "#eab308", 2: "#ef4444" };

// ─── IV Smile types ──────────────────────────────────────────────────────────
type IvContract = {
    strike: number;
    moneyness_pct: number;
    type: string;
    iv: number;
    iv_pct: number;
    market_price: number;
    bid: number;
    ask: number;
    volume: number;
    open_interest: number;
};
type IvExpiration = {
    exp_date: string;
    dte: number;
    atm_iv: number | null;
    smile: IvContract[];
};
type IvSmileData = {
    symbol: string;
    spot: number;
    rf: number;
    as_of: string;
    expirations: IvExpiration[];
};

function IvSmilePanel({ data }: { data: IvSmileData }) {
    const [selectedIdx, setSelectedIdx] = useState(0);

    const exp = data.expirations[selectedIdx];
    if (!exp) return null;

    const calls = exp.smile.filter(c => c.type === "CALL").sort((a, b) => a.strike - b.strike);
    const puts = exp.smile.filter(c => c.type === "PUT").sort((a, b) => a.strike - b.strike);

    // Build unified strike axis
    const allStrikes = Array.from(new Set([...calls.map(c => c.strike), ...puts.map(c => c.strike)])).sort((a, b) => a - b);
    const callMap = Object.fromEntries(calls.map(c => [c.strike, c]));
    const putMap = Object.fromEntries(puts.map(c => [c.strike, c]));
    const chartData = allStrikes.map(k => ({
        strike: k,
        label: `$${k}`,
        callIv: callMap[k]?.iv_pct ?? null,
        putIv: putMap[k]?.iv_pct ?? null,
        callPrice: callMap[k]?.market_price ?? null,
        putPrice: putMap[k]?.market_price ?? null,
        moneyness: putMap[k]?.moneyness_pct ?? callMap[k]?.moneyness_pct ?? 0,
    }));

    return (
        <div className="bg-background rounded-2xl border border-border p-4">
            {/* Header */}
            <div className="flex flex-wrap items-center justify-between gap-3 mb-4">
                <div>
                    <p className="text-sm font-semibold">Implied Volatility Smile — {data.symbol}</p>
                    <p className="text-xs text-muted">Black-Scholes inversion · σ(K) curve · spot ${data.spot.toFixed(2)}</p>
                </div>
                <div className="flex items-center gap-3">
                    {exp.atm_iv != null && (
                        <div className="px-3 py-1.5 rounded-lg bg-purple-500/10 border border-purple-500/30 text-xs font-mono font-bold text-purple-300">
                            ATM IV {exp.atm_iv.toFixed(1)}%
                        </div>
                    )}
                    <select
                        value={selectedIdx}
                        onChange={e => setSelectedIdx(Number(e.target.value))}
                        className="bg-card border border-border rounded-xl px-3 py-2 text-xs font-mono focus:outline-none focus:ring-2 focus:ring-accent/30 text-muted"
                    >
                        {data.expirations.map((ex, i) => (
                            <option key={ex.exp_date} value={i}>
                                {ex.exp_date} &nbsp;({ex.dte}d)
                            </option>
                        ))}
                    </select>
                </div>
            </div>

            {/* Legend */}
            <div className="flex items-center gap-5 mb-3 text-[10px] font-mono text-muted/70">
                <span className="flex items-center gap-1.5"><span className="inline-block w-5 h-0.5 bg-cyan-400" /> IV Calls</span>
                <span className="flex items-center gap-1.5"><span className="inline-block w-5 h-0.5 bg-amber-400" /> IV Puts</span>
                <span className="flex items-center gap-1.5 ml-2">|</span>
                <span className="flex items-center gap-1.5">Spot ≈ ${data.spot.toFixed(0)}</span>
                <span className="flex items-center gap-1.5">r = {(data.rf * 100).toFixed(1)}%</span>
            </div>

            {/* Chart */}
            <div className="h-64">
                <ResponsiveContainer width="100%" height="100%">
                    <ComposedChart data={chartData} margin={{ top: 10, right: 10, bottom: 0, left: 0 }}>
                        <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
                        <XAxis
                            dataKey="label"
                            tick={{ fill: "#9ca3af", fontSize: 9 }}
                            minTickGap={28}
                        />
                        <YAxis
                            tick={{ fill: "#9ca3af", fontSize: 9 }}
                            tickFormatter={v => `${Number(v).toFixed(0)}%`}
                            width={42}
                            domain={[0, "auto"]}
                        />
                        <Tooltip
                            content={({ active, payload, label }) => {
                                if (!active || !payload?.length) return null;
                                const d: any = payload[0]?.payload;
                                return (
                                    <div className="bg-card border border-border rounded-xl px-3 py-2 text-[10px] font-mono shadow-xl space-y-0.5">
                                        <p className="font-bold text-foreground">{label}</p>
                                        <p className="text-muted">Moneyness: {d.moneyness > 0 ? "+" : ""}{d.moneyness?.toFixed(1)}%</p>
                                        {d.callIv != null && <p className="text-cyan-400">CALL IV: {d.callIv.toFixed(1)}%  ·  ${d.callPrice?.toFixed(2)}</p>}
                                        {d.putIv != null && <p className="text-amber-400">PUT  IV: {d.putIv.toFixed(1)}%  ·  ${d.putPrice?.toFixed(2)}</p>}
                                    </div>
                                );
                            }}
                        />
                        {/* Spot reference */}
                        <ReferenceArea
                            x1={`$${Math.floor(data.spot)}`}
                            x2={`$${Math.ceil(data.spot)}`}
                            fill="rgba(99,102,241,0.12)"
                            stroke="rgba(99,102,241,0.4)"
                            strokeWidth={1}
                        />
                        <Line type="monotone" dataKey="callIv" name="CALL IV" stroke="#22d3ee" strokeWidth={1.5} dot={false} connectNulls isAnimationActive={false} />
                        <Line type="monotone" dataKey="putIv" name="PUT IV" stroke="#f59e0b" strokeWidth={1.5} dot={false} connectNulls isAnimationActive={false} />
                    </ComposedChart>
                </ResponsiveContainer>
            </div>

            {/* Per-expiration stats */}
            <div className="mt-3 flex flex-wrap gap-4 text-[10px] font-mono text-muted">
                <span>Calls: <span className="text-white">{calls.length}</span></span>
                <span>Puts: <span className="text-white">{puts.length}</span></span>
                <span>DTE: <span className="text-white">{exp.dte}d</span></span>
                {calls.length > 2 && (() => {
                    const ivs = calls.map(c => c.iv_pct);
                    const skew = ivs[0] - ivs[ivs.length - 1];
                    return <span>Put-Call Skew: <span className={skew > 0 ? "text-red-400" : "text-emerald-400"}>{skew.toFixed(1)}%</span></span>;
                })()}
                <span className="text-muted/50">as of {data.as_of}</span>
            </div>
        </div>
    );
}

function buildRegimeRuns(
    sequence: { date: string; state: number }[],
    startDate: string,
    endDate: string,
): { x1: string; x2: string; state: number }[] {
    const filtered = sequence.filter(p => p.date >= startDate && p.date <= endDate);
    if (filtered.length === 0) return [];
    const runs: { x1: string; x2: string; state: number }[] = [];
    let runStart = filtered[0].date.substring(5);
    let runState = filtered[0].state;
    for (let i = 1; i < filtered.length; i++) {
        if (filtered[i].state !== runState) {
            runs.push({ x1: runStart, x2: filtered[i - 1].date.substring(5), state: runState });
            runStart = filtered[i].date.substring(5);
            runState = filtered[i].state;
        }
    }
    runs.push({ x1: runStart, x2: filtered[filtered.length - 1].date.substring(5), state: runState });
    return runs;
}

// ─── IV Regime Strategy types ────────────────────────────────────────────────
type IVOptionContext = {
    available: boolean;
    error?: string;
    signal_mode?: string;
    direction_bias?: "LONG" | "SHORT" | "FLAT";
    exp_date?: string;
    dte?: number;
    strike?: number;
    moneyness_pct?: number | null;
    atm_iv_pct?: number | null;
    atm_call_iv_pct?: number | null;
    atm_put_iv_pct?: number | null;
    skew_pct?: number | null;
    call_price?: number | null;
    put_price?: number | null;
    iv_realized_spread_pct?: number | null;
    iv_realized_ratio?: number | null;
    source?: string;
    as_of?: string;
};

type IVCurrentSignal = {
    date: string;
    close: number;
    iv_rank: number;
    regime: string;
    momentum_pct: number;
    direction: "LONG" | "SHORT" | "FLAT";
    proxy_direction?: "LONG" | "SHORT" | "FLAT";
    signal_source?: string;
    daily_vol_pct?: number;
    realized_vol_ann_pct?: number;
    option_context?: IVOptionContext;
};

// ─── ARCH / GARCH types ───────────────────────────────────────────────────────
type ArchVolPoint = {
    date: string;
    sigma_pct: number;      // daily conditional vol %
    sigma_ann_pct: number;  // annualised conditional vol %
    ret_pct: number;        // log-return %
};
type ArchVolData = {
    symbol: string;
    n_obs: number;
    model: string;
    params: {
        mu: number;
        omega: string;
        alpha: number;
        beta: number;
        persistence: number;
    };
    fit: { log_likelihood: number; aic: number; bic: number };
    long_run_vol_ann_pct: number;
    current_sigma_ann_pct: number;
    forecast: { h1_ann_pct: number; h5_ann_pct: number; h21_ann_pct: number };
    var_daily: { var_95_pct: number; var_99_pct: number };
    arch_lm_test: { stat: number; p_value: number; adequate: boolean | null };
    conditional_vol: ArchVolPoint[];
};

type KalmanFilterPoint = {
    date: string;
    observed: number;
    predicted: number;
    filtered: number;
    innovation: number;
    innovation_z: number;
    gain: number;
    variance: number;
    lower_1sigma: number;
    upper_1sigma: number;
    mean_gap_pct: number | null;
};

type KalmanFilterData = {
    symbol: string;
    n_obs: number;
    model: string;
    ou_interpretation: boolean;
    calibration: {
        alpha: number;
        beta: number;
        residual_std: number;
        process_noise_q: number;
        measurement_noise_r: number;
        measurement_noise_mult: number;
        stationary: boolean;
        long_run_mean: number | null;
        half_life_days: number | null;
    };
    diagnostics: {
        rmse_filtered_vs_observed: number;
        mean_abs_innovation: number;
        avg_gain: number;
        last_gain: number;
        last_innovation_z: number;
        smoothness_ratio: number;
    };
    current_state: {
        observed: number;
        predicted: number;
        filtered: number;
        innovation: number;
        innovation_z: number;
        gain: number;
        variance: number;
        lower_1sigma: number;
        upper_1sigma: number;
        spread_pct: number;
        pull_signal: "UP" | "DOWN" | "NEUTRAL";
        mean_gap_pct: number | null;
    };
    series: KalmanFilterPoint[];
};

function ArchVolPanel({ data }: { data: ArchVolData }) {
    // ── Thin the series for chart performance (max 300 points)
    const thinned = (() => {
        const n = data.conditional_vol.length;
        if (n <= 300) return data.conditional_vol;
        const step = Math.ceil(n / 300);
        return data.conditional_vol.filter((_, i) => i % step === 0 || i === n - 1);
    })();

    const persist = data.params.persistence;
    const halflife = persist < 1
        ? Math.round(Math.log(0.5) / Math.log(persist))
        : Infinity;

    const adequate = data.arch_lm_test.adequate;
    const lmBadge = adequate === null
        ? { label: "LM test N/A", cls: "bg-zinc-700/40 border-zinc-600/30 text-zinc-400" }
        : adequate
            ? { label: "Model adequate (LM p=" + data.arch_lm_test.p_value + ")", cls: "bg-emerald-500/10 border-emerald-500/30 text-emerald-300" }
            : { label: "ARCH effects remain (p=" + data.arch_lm_test.p_value + ")", cls: "bg-amber-500/10 border-amber-500/30 text-amber-300" };

    return (
        <div className="bg-background rounded-2xl border border-border p-4 mt-3">
            {/* Header */}
            <div className="flex flex-wrap items-center justify-between gap-3 mb-4">
                <div>
                    <p className="text-sm font-semibold">GARCH(1,1) Conditional Volatility — {data.symbol}</p>
                    <p className="text-xs text-muted">
                        σ²_t = ω + α·ε²_(t-1) + β·σ²_(t-1) &nbsp;·&nbsp; {data.n_obs.toLocaleString()} observations
                    </p>
                </div>
                <div className="flex flex-wrap items-center gap-2">
                    <span className={`px-3 py-1.5 rounded-lg border text-xs font-mono font-bold ${lmBadge.cls}`}>
                        {lmBadge.label}
                    </span>
                    <span className="px-3 py-1.5 rounded-lg bg-violet-500/10 border border-violet-500/30 text-violet-300 text-xs font-mono font-bold">
                        Current σ {data.current_sigma_ann_pct.toFixed(1)}% p.a.
                    </span>
                </div>
            </div>

            {/* Conditional Vol chart */}
            <div className="h-44 mb-5">
                <ResponsiveContainer width="100%" height="100%">
                    <AreaChart data={thinned} margin={{ top: 4, right: 8, bottom: 0, left: 32 }}>
                        <defs>
                            <linearGradient id="garchGrad" x1="0" y1="0" x2="0" y2="1">
                                <stop offset="5%" stopColor="#a78bfa" stopOpacity={0.35} />
                                <stop offset="95%" stopColor="#a78bfa" stopOpacity={0.02} />
                            </linearGradient>
                        </defs>
                        <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
                        <XAxis dataKey="date" tick={{ fontSize: 9 }} tickLine={false} axisLine={false}
                            tickFormatter={(v: string) => v.substring(5)} interval="preserveStartEnd" />
                        <YAxis tick={{ fontSize: 9 }} tickLine={false} axisLine={false}
                            tickFormatter={(v: number) => `${v.toFixed(0)}%`} />
                        <Tooltip
                            contentStyle={{ background: "#1a1a2e", border: "1px solid rgba(255,255,255,0.1)", borderRadius: 8, fontSize: 11 }}
                            formatter={(value: number | string | undefined) => [`${Number(value ?? 0).toFixed(2)}%`, "Ann. Vol σ"]}
                            labelFormatter={(label) => `Date: ${String(label ?? "")}`}
                        />
                        <Area type="monotone" dataKey="sigma_ann_pct" stroke="#a78bfa" strokeWidth={1.5}
                            fill="url(#garchGrad)" dot={false} name="Ann. Vol σ" />
                    </AreaChart>
                </ResponsiveContainer>
            </div>

            {/* Params row */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-4">
                {[
                    { label: "α (ARCH)", value: data.params.alpha.toFixed(4), hint: "shock sensitivity" },
                    { label: "β (GARCH)", value: data.params.beta.toFixed(4), hint: "vol persistence" },
                    { label: "α + β", value: data.params.persistence.toFixed(4), hint: `half-life ~${halflife}d` },
                    { label: "Long-run σ", value: `${data.long_run_vol_ann_pct.toFixed(1)}%`, hint: "unconditional ann." },
                ].map(({ label, value, hint }) => (
                    <div key={label} className="bg-muted/10 rounded-xl p-3 border border-border/50">
                        <p className="text-xs text-muted mb-1">{label}</p>
                        <p className="text-lg font-bold font-mono text-foreground">{value}</p>
                        <p className="text-[10px] text-muted/70">{hint}</p>
                    </div>
                ))}
            </div>

            {/* Forecast + VaR row */}
            <div className="grid grid-cols-2 sm:grid-cols-5 gap-3">
                {[
                    { label: "1-day forecast", value: `${data.forecast.h1_ann_pct.toFixed(1)}%` },
                    { label: "5-day forecast", value: `${data.forecast.h5_ann_pct.toFixed(1)}%` },
                    { label: "21-day forecast", value: `${data.forecast.h21_ann_pct.toFixed(1)}%` },
                    { label: "VaR 95% (daily)", value: `−${data.var_daily.var_95_pct.toFixed(2)}%`, cls: "text-amber-400" },
                    { label: "VaR 99% (daily)", value: `−${data.var_daily.var_99_pct.toFixed(2)}%`, cls: "text-red-400" },
                ].map(({ label, value, cls }) => (
                    <div key={label} className="bg-muted/10 rounded-xl p-3 border border-border/50">
                        <p className="text-xs text-muted mb-1">{label}</p>
                        <p className={`text-base font-bold font-mono ${cls ?? "text-violet-300"}`}>{value}</p>
                    </div>
                ))}
            </div>

            {/* Fit quality */}
            <div className="mt-3 flex flex-wrap gap-4 text-[10px] text-muted font-mono">
                <span>LL = {data.fit.log_likelihood.toFixed(1)}</span>
                <span>AIC = {data.fit.aic.toFixed(1)}</span>
                <span>BIC = {data.fit.bic.toFixed(1)}</span>
                <span>ω = {data.params.omega}</span>
            </div>
        </div>
    );
}

function KalmanFilterPanel({ data }: { data: KalmanFilterData }) {
    const thinned = (() => {
        const n = data.series.length;
        if (n <= 300) return data.series;
        const step = Math.ceil(n / 300);
        return data.series.filter((_, i) => i % step === 0 || i === n - 1);
    })();

    const regimeBadge = data.ou_interpretation
        ? { label: "OU-compatible mean reversion", cls: "bg-emerald-500/10 border-emerald-500/30 text-emerald-300" }
        : { label: "AR(1) latent-state filter", cls: "bg-sky-500/10 border-sky-500/30 text-sky-300" };

    const spreadCls = data.current_state.spread_pct > 0.0
        ? "text-emerald-300"
        : data.current_state.spread_pct < 0.0
            ? "text-red-300"
            : "text-zinc-300";

    return (
        <div className="bg-background rounded-2xl border border-border p-4 mt-3">
            <div className="flex flex-wrap items-center justify-between gap-3 mb-4">
                <div>
                    <p className="text-sm font-semibold">Kalman State Filter — {data.symbol}</p>
                    <p className="text-xs text-muted">
                        AR(1) latent state on closes · {data.n_obs.toLocaleString()} observations · best interpreted on mean-reverting instruments
                    </p>
                </div>
                <div className="flex flex-wrap items-center gap-2">
                    <span className={`px-3 py-1.5 rounded-lg border text-xs font-mono font-bold ${regimeBadge.cls}`}>
                        {regimeBadge.label}
                    </span>
                    <span className="px-3 py-1.5 rounded-lg bg-fuchsia-500/10 border border-fuchsia-500/30 text-fuchsia-300 text-xs font-mono font-bold">
                        K {data.current_state.gain.toFixed(3)}
                    </span>
                </div>
            </div>

            <div className="h-44 mb-5">
                <ResponsiveContainer width="100%" height="100%">
                    <ComposedChart data={thinned} margin={{ top: 4, right: 8, bottom: 0, left: 24 }}>
                        <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
                        <XAxis
                            dataKey="date"
                            tick={{ fontSize: 9 }}
                            tickLine={false}
                            axisLine={false}
                            tickFormatter={(v: string) => v.substring(5)}
                            interval="preserveStartEnd"
                        />
                        <YAxis
                            tick={{ fontSize: 9 }}
                            tickLine={false}
                            axisLine={false}
                            tickFormatter={(v: number) => `$${Number(v).toFixed(0)}`}
                            width={50}
                        />
                        <Tooltip
                            contentStyle={{ background: "#1a1a2e", border: "1px solid rgba(255,255,255,0.1)", borderRadius: 8, fontSize: 11 }}
                            formatter={(value, name) => {
                                const numericValue = Number(value ?? 0);
                                const seriesName = String(name ?? "");
                                if (seriesName === "Observed") return [`$${numericValue.toFixed(2)}`, seriesName];
                                if (seriesName === "Predicted") return [`$${numericValue.toFixed(2)}`, seriesName];
                                if (seriesName === "Filtered") return [`$${numericValue.toFixed(2)}`, seriesName];
                                return [numericValue, seriesName];
                            }}
                            labelFormatter={(label) => `Date: ${String(label ?? "")}`}
                        />
                        <Line
                            type="monotone"
                            dataKey="observed"
                            name="Observed"
                            stroke="rgba(148,163,184,0.95)"
                            strokeWidth={1.1}
                            dot={false}
                            isAnimationActive={false}
                        />
                        <Line
                            type="monotone"
                            dataKey="predicted"
                            name="Predicted"
                            stroke="rgba(244,114,182,0.7)"
                            strokeWidth={1.1}
                            strokeDasharray="4 3"
                            dot={false}
                            isAnimationActive={false}
                        />
                        <Line
                            type="monotone"
                            dataKey="filtered"
                            name="Filtered"
                            stroke="#34d399"
                            strokeWidth={1.8}
                            dot={false}
                            isAnimationActive={false}
                        />
                    </ComposedChart>
                </ResponsiveContainer>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 mb-4">
                {[
                    { label: "β / ϕ", value: data.calibration.beta.toFixed(4), hint: data.calibration.stationary ? "stationary transition" : "near-unit / trending" },
                    { label: "Half-life", value: data.calibration.half_life_days != null ? `${data.calibration.half_life_days.toFixed(1)}d` : "N/A", hint: "OU only" },
                    { label: "Long-run mean θ", value: data.calibration.long_run_mean != null ? `$${data.calibration.long_run_mean.toFixed(2)}` : "N/A", hint: "offline calibration" },
                    { label: "Latest Gain K", value: data.current_state.gain.toFixed(3), hint: `${(data.current_state.gain * 100).toFixed(1)}% trust in quote` },
                    { label: "Filtered Spread", value: `${data.current_state.spread_pct >= 0 ? "+" : ""}${data.current_state.spread_pct.toFixed(2)}%`, hint: data.current_state.pull_signal, cls: spreadCls },
                    { label: "Innovation z", value: `${data.current_state.innovation_z >= 0 ? "+" : ""}${data.current_state.innovation_z.toFixed(2)}`, hint: "last standardized surprise" },
                ].map(({ label, value, hint, cls }) => (
                    <div key={label} className="bg-muted/10 rounded-xl p-3 border border-border/50">
                        <p className="text-xs text-muted mb-1">{label}</p>
                        <p className={`text-lg font-bold font-mono ${cls ?? "text-foreground"}`}>{value}</p>
                        <p className="text-[10px] text-muted/70">{hint}</p>
                    </div>
                ))}
            </div>

            <div className="flex flex-wrap gap-4 text-[10px] text-muted font-mono">
                <span>α = {data.calibration.alpha.toFixed(4)}</span>
                <span>Q = {data.calibration.process_noise_q.toFixed(4)}</span>
                <span>R = {data.calibration.measurement_noise_r.toFixed(4)}</span>
                <span>R/Q mult = {data.calibration.measurement_noise_mult.toFixed(2)}x</span>
                <span>RMSE = {data.diagnostics.rmse_filtered_vs_observed.toFixed(3)}</span>
                <span>Smoothness = {data.diagnostics.smoothness_ratio.toFixed(3)}</span>
            </div>
        </div>
    );
}

// ─── Backtest Price Chart with Trade Markers ──────────────────────────────────
function BacktestPriceChart({
    trades, symbol, startDate, endDate,
}: {
    trades: LiveTrade[];
    symbol: string;
    startDate: string;
    endDate: string;
}) {
    const [chartData, setChartData] = useState<any[]>([]);
    const [loading, setLoading] = useState(false);
    const [regimeData, setRegimeData] = useState<RegimeData | null>(null);

    // ── fetch OHLCV ──────────────────────────────────────────────────────────
    useEffect(() => {
        if (!symbol || !startDate || !endDate || trades.length === 0) return;
        setLoading(true);
        fetch(`${API_BASE}/api/v1/market/historical/${symbol}?limit=600`)
            .then(r => r.json())
            .then(d => {
                const hist = (d.historical ?? [])
                    .filter((c: any) => c.date >= startDate && c.date <= endDate)
                    .sort((a: any, b: any) => a.date.localeCompare(b.date));

                if (hist.length === 0) {
                    console.warn(`[BacktestPriceChart] No OHLC data for ${symbol} between ${startDate} and ${endDate}`);
                    setLoading(false);
                    return;
                }

                const closes = hist.map((c: any) => c.close as number);
                const toDate = (ts: string | undefined) => ts ? ts.substring(0, 10) : "";

                const merged = hist.map((c: any, i: number) => {
                    const dateStr: string = c.date;
                    const win = closes.slice(Math.max(0, i - 19), i + 1);
                    const sma20 = win.reduce((s: number, v: number) => s + v, 0) / win.length;
                    const entriesHere = trades.filter(t => toDate(t.timestamp) === dateStr);
                    const exitsHere = trades.filter(t =>
                        toDate(t.exit_timestamp || t.timestamp) === dateStr && t.exit_price != null
                    );
                    const entry = entriesHere[0];
                    const exit = exitsHere[0];
                    return {
                        date: dateStr,
                        label: dateStr.substring(5),
                        close: c.close,
                        sma20: Math.round(sma20 * 100) / 100,
                        entryPrice: entry?.entry ?? null,
                        _entryDir: entry?.direction ?? null,
                        _entryOutcome: entry?.outcome ?? null,
                        _entryId: entry?.signal_id ?? null,
                        exitPrice: exit?.exit_price ?? null,
                        _exitOutcome: exit?.outcome ?? null,
                    };
                });
                setChartData(merged);
            })
            .catch(err => console.error("[BacktestPriceChart] Fetch error:", err))
            .finally(() => setLoading(false));
    }, [symbol, startDate, endDate, trades.length]);

    // ── fetch volatility regimes ─────────────────────────────────────────────
    useEffect(() => {
        if (!symbol) return;
        fetch(`${API_BASE}/api/v1/analytics/volatility-regimes/${symbol}?days=600&window=20`)
            .then(r => r.json())
            .then((d: RegimeData) => setRegimeData(d))
            .catch(() => {/* regime overlay is optional – silently skip */ });
    }, [symbol]);

    if (loading) {
        return (
            <div className="h-48 flex items-center justify-center gap-3">
                <div className="h-4 w-4 border-2 border-accent border-t-transparent rounded-full animate-spin" />
                <span className="text-xs text-muted font-mono uppercase tracking-widest animate-pulse">Loading price data…</span>
            </div>
        );
    }

    if (chartData.length === 0) return null;

    const wins = trades.filter(t => t.outcome === "win_tp").length;
    const losses = trades.filter(t => t.outcome === "loss_sl").length;

    const regimeRuns = regimeData
        ? buildRegimeRuns(regimeData.regime_sequence, startDate, endDate)
        : [];

    const dists = regimeData?.distributions ?? {};

    // Custom dot renderers
    const EntryDot = (props: any) => {
        const { cx, cy, payload } = props;
        if (!payload || payload.entryPrice == null || cx == null || cy == null) return null;
        const isLong = payload._entryDir === "LONG";
        const won = payload._entryOutcome === "win_tp";
        const fill = won ? "#22c55e" : "#ef4444";
        return isLong
            ? <polygon key={payload._entryId} points={`${cx},${cy - 10} ${cx - 6},${cy + 2} ${cx + 6},${cy + 2}`} fill={fill} stroke="#0f172a" strokeWidth={0.8} opacity={0.95} />
            : <polygon key={payload._entryId} points={`${cx},${cy + 10} ${cx - 6},${cy - 2} ${cx + 6},${cy - 2}`} fill={fill} stroke="#0f172a" strokeWidth={0.8} opacity={0.95} />;
    };

    const ExitDot = (props: any) => {
        const { cx, cy, payload } = props;
        if (!payload || payload.exitPrice == null || cx == null || cy == null) return null;
        const won = payload._exitOutcome === "win_tp";
        const fill = won ? "#22c55e" : "#ef4444";
        return <rect key={payload._entryId + "_exit"} x={cx - 4} y={cy - 4} width={8} height={8} fill={fill} stroke="#0f172a" strokeWidth={0.8} opacity={0.9} />;
    };

    return (
        <div>
            {/* ── Legend ─────────────────────────────────────────────────── */}
            <div className="flex flex-wrap items-center gap-x-5 gap-y-1 mb-3 text-[10px] font-mono text-muted/70">
                <span className="flex items-center gap-1.5"><span className="inline-block w-5 h-0.5 bg-cyan-400" /> Price</span>
                <span className="flex items-center gap-1.5"><span className="inline-block w-5 h-0.5 border-t border-dashed border-yellow-400/70" /> SMA 20</span>
                <span className="flex items-center gap-1.5 text-emerald-400 font-bold">▲ Long (Win)</span>
                <span className="flex items-center gap-1.5 text-red-400 font-bold">▲ Long (Loss)</span>
                <span className="flex items-center gap-1.5"><span className="inline-block w-2.5 h-2.5 bg-green" /> Exit Win ({wins})</span>
                <span className="flex items-center gap-1.5"><span className="inline-block w-2.5 h-2.5 bg-red" /> Exit Loss ({losses})</span>
                {/* regime legend */}
                <span className="flex items-center gap-1.5"><span className="inline-block w-3 h-3 rounded-sm" style={{ background: "rgba(34,197,94,0.25)" }} /> Low Vol</span>
                <span className="flex items-center gap-1.5"><span className="inline-block w-3 h-3 rounded-sm" style={{ background: "rgba(234,179,8,0.25)" }} /> Med Vol</span>
                <span className="flex items-center gap-1.5"><span className="inline-block w-3 h-3 rounded-sm" style={{ background: "rgba(239,68,68,0.25)" }} /> High Vol</span>
            </div>

            {/* ── Price chart ─────────────────────────────────────────────── */}
            <div className="h-72">
                <ResponsiveContainer width="100%" height="100%">
                    <ComposedChart data={chartData} margin={{ top: 10, right: 10, bottom: 0, left: 0 }}>
                        <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
                        <XAxis dataKey="label" tick={{ fill: "#9ca3af", fontSize: 9 }} minTickGap={30} />
                        <YAxis
                            domain={["auto", "auto"]}
                            tick={{ fill: "#9ca3af", fontSize: 9 }}
                            tickFormatter={v => `$${Number(v).toFixed(0)}`}
                            width={55}
                        />
                        <Tooltip
                            content={({ active, payload }) => {
                                if (!active || !payload?.length) return null;
                                const d = payload[0]?.payload;
                                // find regime for this date
                                const rp = regimeData?.regime_sequence.find(r => r.date === d.date);
                                const regimeLabel = rp != null ? (regimeData?.state_labels?.[String(rp.state)] ?? "") : null;
                                const regimeColor = rp != null ? REGIME_FILL[rp.state] : "#9ca3af";
                                return (
                                    <div className="bg-card border border-border rounded-xl px-3 py-2 text-[10px] font-mono shadow-xl space-y-0.5">
                                        <p className="font-bold text-foreground">{d.date}</p>
                                        <p>Close: <span className="text-accent">${d.close?.toFixed(2)}</span></p>
                                        {regimeLabel && (
                                            <p style={{ color: regimeColor }}>
                                                Regime: {regimeLabel}{rp ? ` · σ={${(rp.vol * 100).toFixed(1)}%}` : ""}
                                            </p>
                                        )}
                                        {d.entryPrice != null && (
                                            <p className={d._entryDir === "LONG" ? "text-emerald-400" : "text-red-400"}>
                                                Entry ({d._entryDir}) @ ${d.entryPrice?.toFixed(2)} — {d._entryOutcome}
                                            </p>
                                        )}
                                        {d.exitPrice != null && (
                                            <p className={d._exitOutcome === "win_tp" ? "text-emerald-400" : "text-red-400"}>
                                                Exit @ ${d.exitPrice?.toFixed(2)}
                                            </p>
                                        )}
                                    </div>
                                );
                            }}
                        />
                        {/* Regime background bands — rendered first so they sit behind price */}
                        {regimeRuns.map((run, i) => (
                            <ReferenceArea
                                key={`regime-${i}`}
                                x1={run.x1}
                                x2={run.x2}
                                fill={REGIME_FILL[run.state]}
                                fillOpacity={0.10}
                                stroke="none"
                                ifOverflow="visible"
                            />
                        ))}
                        {/* Price line */}
                        <Line type="monotone" dataKey="close" stroke="#22d3ee" strokeWidth={1.5} dot={false} isAnimationActive={false} />
                        {/* SMA 20 */}
                        <Line type="monotone" dataKey="sma20" stroke="rgba(234,179,8,0.55)" strokeWidth={1} strokeDasharray="4 3" dot={false} isAnimationActive={false} />
                        {/* Entry markers */}
                        <Line
                            type="monotone" dataKey="entryPrice"
                            stroke="transparent" strokeWidth={0}
                            dot={<EntryDot />} activeDot={false}
                            isAnimationActive={false} connectNulls={false}
                        />
                        {/* Exit markers */}
                        <Line
                            type="monotone" dataKey="exitPrice"
                            stroke="transparent" strokeWidth={0}
                            dot={<ExitDot />} activeDot={false}
                            isAnimationActive={false} connectNulls={false}
                        />
                    </ComposedChart>
                </ResponsiveContainer>
            </div>

            {/* ── Regime distribution summary ──────────────────────────────── */}
            {Object.keys(dists).length > 0 && (
                <div className="mt-4 grid grid-cols-3 gap-2">
                    {[0, 1, 2].map(s => {
                        const d = dists[String(s)];
                        if (!d) return null;
                        return (
                            <div
                                key={s}
                                className="rounded-xl border p-3 space-y-1"
                                style={{ borderColor: `${REGIME_FILL[s]}40`, background: `${REGIME_FILL[s]}0a` }}
                            >
                                <p className="text-[10px] font-bold uppercase tracking-widest" style={{ color: REGIME_FILL[s] }}>
                                    {d.label}
                                </p>
                                <p className="text-[10px] text-muted font-mono">
                                    μ {d.annualized_ret_pct > 0 ? "+" : ""}{d.annualized_ret_pct.toFixed(1)}% / yr
                                </p>
                                <p className="text-[10px] text-muted font-mono">σ {d.annualized_vol_pct.toFixed(1)}% ann.</p>
                                <p className="text-[10px] text-muted font-mono">Sharpe {d.sharpe.toFixed(2)}</p>
                                <p className="text-[10px] text-muted/60 font-mono">{d.count} days</p>
                            </div>
                        );
                    })}
                </div>
            )}
        </div>
    );
}


export default function BacktestLab() {
    const { socket, connected, reconnect } = useSocket();
    const { holdings, totalValue } = usePortfolio();
    const [labView, setLabView] = useState<"strategy" | "portfolio">("strategy");

    const [symbol, setSymbol] = useState("AAPL");
    const [startDate, setStartDate] = useState("2024-01-01");
    const [endDate, setEndDate] = useState("2024-03-31");

    const handleQuickDate = (months: number | 'ytd') => {
        const end = new Date();
        const start = new Date();

        if (months === 'ytd') {
            start.setMonth(0, 1); // Jan 1st of current year
        } else {
            start.setMonth(start.getMonth() - months);
        }

        setEndDate(end.toISOString().split('T')[0]);
        setStartDate(start.toISOString().split('T')[0]);
    };
    const [account, setAccount] = useState("10000");
    const [bootstrap, setBootstrap] = useState(true);
    const [iterations, setIterations] = useState("1000");

    const [launching, setLaunching] = useState(false);
    const [isRunning, setIsRunning] = useState(false);
    const [activeSim, setActiveSim] = useState<string | null>(null);
    const [activeAccountSize, setActiveAccountSize] = useState(10_000);
    const [activeSymbol, setActiveSymbol] = useState("AAPL");
    const [progress, setProgress] = useState<ProgressState>({ day: 0, total: 0, pct: 0 });
    const [trades, setTrades] = useState<LiveTrade[]>([]);
    const [bootstrapLive, setBootstrapLive] = useState<BootstrapLiveData | null>(null);
    const [completedResult, setCompletedResult] = useState<CompletedResult | null>(null);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const [ivData, setIvData] = useState<IvSmileData | null>(null);
    const [ivLoading, setIvLoading] = useState(false);
    const [archData, setArchData] = useState<ArchVolData | null>(null);
    const [archLoading, setArchLoading] = useState(false);
    const [kalmanData, setKalmanData] = useState<KalmanFilterData | null>(null);
    const [kalmanLoading, setKalmanLoading] = useState(false);

    // Strategy selector
    const [strategyName, setStrategyName] = useState("ORB_FVG_ENGULFING");

    // IV Regime parameters
    const [ivrLow, setIvrLow] = useState("30");
    const [ivrRR, setIvrRR] = useState("2.0");
    const [ivrRisk, setIvrRisk] = useState("1.0");   // %
    const [ivrHigh, setIvrHigh] = useState("70");
    const [ivrMom, setIvrMom] = useState("20");
    const [ivrHold, setIvrHold] = useState("5");
    const [ivrSlMult, setIvrSlMult] = useState("2.0");
    const [ivrMarkov, setIvrMarkov] = useState(true);
    const [ivrShort, setIvrShort] = useState(true);
    const [ivCurrentSignal, setIvCurrentSignal] = useState<IVCurrentSignal | null>(null);

    const equityCurve = buildEquityCurve(trades, activeAccountSize);
    const liveKpis = deriveLiveKpis(trades, activeAccountSize);
    const displayKpis = completedResult?.kpis ?? liveKpis;
    const activeHoldings = holdings.filter((holding) => Math.abs(holding.shares) > 0);
    const displayBootstrap = completedResult?.bootstrap ?? (bootstrapLive ? {
        iterations: bootstrapLive.iterations,
        net_profit_95_ci: bootstrapLive.net_profit_95_ci,
        max_drawdown_95_ci_pct: bootstrapLive.max_drawdown_95_ci_pct,
    } : null);
    const profitHistogram = buildHistogramData(bootstrapLive?.net_profit_samples ?? []);
    const drawdownHistogram = buildHistogramData(bootstrapLive?.max_drawdown_samples ?? []);

    // Fetch IV smile whenever a backtest completes on a new symbol
    useEffect(() => {
        if (!completedResult) return;
        setIvLoading(true);
        setIvData(null);
        fetch(`${API_BASE}/api/v1/analytics/implied-vol/${completedResult.symbol}`)
            .then(r => r.ok ? r.json() : null)
            .then(d => d?.expirations ? setIvData(d) : null)
            .catch(() => { })
            .finally(() => setIvLoading(false));
    }, [completedResult?.symbol]);

    // Fetch ARCH/GARCH conditional vol whenever a backtest completes
    useEffect(() => {
        if (!completedResult) return;
        setArchLoading(true);
        setArchData(null);
        fetch(`${API_BASE}/api/v1/analytics/arch-vol/${completedResult.symbol}`)
            .then(r => r.ok ? r.json() : null)
            .then(d => d?.conditional_vol ? setArchData(d) : null)
            .catch(() => { })
            .finally(() => setArchLoading(false));
    }, [completedResult?.symbol]);

    useEffect(() => {
        if (!completedResult) return;
        setKalmanLoading(true);
        setKalmanData(null);
        fetch(`${API_BASE}/api/v1/analytics/kalman-filter/${completedResult.symbol}?days=300&measurement_noise_mult=4`)
            .then(r => r.ok ? r.json() : null)
            .then(d => d?.series ? setKalmanData(d) : null)
            .catch(() => { })
            .finally(() => setKalmanLoading(false));
    }, [completedResult?.symbol]);

    useEffect(() => {
        if (!socket || !activeSim) return;

        const hydrateCompletedTrades = async (simId: string) => {
            try {
                const response = await fetch(`${API_BASE}/api/v1/simulation/results/${encodeURIComponent(simId)}`);
                if (!response.ok) return;
                const detail = await response.json();
                if (Array.isArray(detail?.trades)) {
                    setTrades(detail.trades);
                }
            } catch {
                // Ignore hydration failures; live socket events already provide the key information.
            }
        };

        const onProgress = (data: any) => {
            if (data?.sim_id !== activeSim) return;
            setProgress({
                day: Number(data.day || 0),
                total: Number(data.total || 0),
                pct: Number(data.pct || 0),
            });
        };

        const onTrade = (data: any) => {
            if (data?.sim_id !== activeSim || !data.trade) return;
            setTrades((prev) => {
                const alreadyExists = prev.some((trade) => trade.signal_id === data.trade.signal_id && trade.exit_timestamp === data.trade.exit_timestamp);
                if (alreadyExists) return prev;
                return [...prev, data.trade as LiveTrade];
            });
        };

        const onBootstrapReady = (data: any) => {
            if (data?.sim_id !== activeSim) return;
            setBootstrapLive({
                iterations: Number(data.iterations || 0),
                net_profit_95_ci: data.net_profit_95_ci ?? [0, 0],
                max_drawdown_95_ci_pct: data.max_drawdown_95_ci_pct ?? [0, 0],
                net_profit_samples: Array.isArray(data.net_profit_samples) ? data.net_profit_samples : [],
                max_drawdown_samples: Array.isArray(data.max_drawdown_samples) ? data.max_drawdown_samples : [],
            });
        };

        const onComplete = (data: any) => {
            if (data?.sim_id !== activeSim) return;
            setIsRunning(false);
            setProgress((prev) => ({
                day: prev.total || data.trading_days || prev.day,
                total: prev.total || data.trading_days || prev.total,
                pct: 100,
            }));
            setCompletedResult({
                sim_id: data.sim_id,
                symbol: activeSymbol,
                strategy: strategyName,
                status: "completed",
                kpis: data.kpis,
                trading_days: Number(data.trading_days || 0),
                total_trades: Number(data.total_trades || 0),
                bootstrap: data.bootstrap ?? null,
                report_url: data.report_url,
            });
            void hydrateCompletedTrades(data.sim_id);
        };

        const onError = (data: any) => {
            if (data?.sim_id !== activeSim) return;
            setIsRunning(false);
            setErrorMessage(data?.error || "Backtest execution failed.");
        };

        socket.on("backtest_progress", onProgress);
        socket.on("backtest_trade", onTrade);
        socket.on("backtest_bootstrap_ready", onBootstrapReady);
        socket.on("backtest_complete", onComplete);
        socket.on("backtest_error", onError);

        return () => {
            socket.off("backtest_progress", onProgress);
            socket.off("backtest_trade", onTrade);
            socket.off("backtest_bootstrap_ready", onBootstrapReady);
            socket.off("backtest_complete", onComplete);
            socket.off("backtest_error", onError);
        };
    }, [socket, activeSim, activeSymbol]);

    const handleRunIVRegime = async () => {
        const parsedAccount = parseFloat(account);
        if (!Number.isFinite(parsedAccount) || parsedAccount <= 0) {
            setErrorMessage("Initial capital must be greater than 0.");
            return;
        }

        setLaunching(true);
        setIsRunning(true);
        setActiveSim(null);
        setActiveAccountSize(parsedAccount);
        setActiveSymbol(symbol);
        setProgress({ day: 0, total: 0, pct: 0 });
        setTrades([]);
        setBootstrapLive(null);
        setCompletedResult(null);
        setErrorMessage(null);
        setIvCurrentSignal(null);

        try {
            const response = await fetch(`${API_BASE}/api/v1/simulation/iv-regime`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    symbol,
                    start_date: startDate,
                    end_date: endDate,
                    account_size: parsedAccount,
                    iv_rank_low: parseFloat(ivrLow),
                    iv_rank_high: parseFloat(ivrHigh),
                    momentum_window: parseInt(ivrMom, 10),
                    hold_days: parseInt(ivrHold, 10),
                    sl_vol_mult: parseFloat(ivrSlMult),
                    rr_target: parseFloat(ivrRR),
                    risk_pct: parseFloat(ivrRisk) / 100,
                    use_markov_filter: ivrMarkov,
                    allow_short: ivrShort,
                }),
            });

            const data = await response.json();
            if (!response.ok) {
                setErrorMessage(data?.detail || "IV Regime backtest failed.");
                return;
            }

            const tradeList = (data.trades || []).map((t: any) => ({
                signal_id: t.signal_id,
                timestamp: t.timestamp,
                direction: t.direction,
                entry: t.entry,
                stop: t.stop,
                tp: t.tp,
                exit_price: t.exit_price ?? null,
                exit_timestamp: t.exit_timestamp ?? null,
                outcome: t.outcome,
                pnl_r: t.pnl_r,
                pnl_usd: t.pnl_usd,
            }));

            setTrades(tradeList);
            setIvCurrentSignal(data.current_signal ?? null);
            setProgress({ day: data.n_trading_days, total: data.n_trading_days, pct: 100 });
            setCompletedResult({
                sim_id: `ivr-${Date.now()}`,
                symbol,
                strategy: "IV_REGIME",
                status: "completed",
                kpis: data.kpis,
                trading_days: data.n_trading_days,
                total_trades: data.kpis?.total_trades ?? 0,
                bootstrap: null,
                report_url: null,
            });
        } catch {
            setErrorMessage("Failed to connect to backend.");
        } finally {
            setLaunching(false);
            setIsRunning(false);
        }
    };

    const handleRunBacktest = async () => {
        const parsedAccount = parseFloat(account);
        if (!Number.isFinite(parsedAccount) || parsedAccount <= 0) {
            setErrorMessage("Initial capital must be greater than 0.");
            return;
        }

        setLaunching(true);
        setIsRunning(false);
        setActiveSim(null);
        setActiveAccountSize(parsedAccount);
        setActiveSymbol(symbol);
        setProgress({ day: 0, total: 0, pct: 0 });
        setTrades([]);
        setBootstrapLive(null);
        setCompletedResult(null);
        setErrorMessage(null);

        try {
            const response = await fetch(`${API_BASE}/api/v1/simulation/run`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    symbol,
                    start_date: startDate,
                    end_date: endDate,
                    account_size: parsedAccount,
                    strategy_name: strategyName,
                    run_bootstrap: bootstrap,
                    bootstrap_iterations: parseInt(iterations, 10),
                }),
            });

            const data = await response.json();
            if (!response.ok) {
                setErrorMessage(data?.detail || "Failed to launch simulation.");
                return;
            }

            setActiveSim(data.sim_id);
            setIsRunning(true);
        } catch (error) {
            console.error("Backtest Error:", error);
            setErrorMessage("Failed to connect to backend.");
        } finally {
            setLaunching(false);
        }
    };

    const netProfit = displayKpis.final_equity - activeAccountSize;
    const reportUrl = completedResult?.report_url;

    return (
        <AppLayout>
            <div className="p-6 lg:p-8 space-y-6 animate-fade-in relative">
                <div className="flex items-center justify-between">
                    <div className="flex items-center gap-4">
                        <div className="h-10 w-10 rounded-xl bg-accent/10 flex items-center justify-center">
                            <CandlestickChart size={20} className="text-accent" />
                        </div>
                        <div>
                            <h1 className="text-2xl font-bold tracking-tight">Backtest Lab</h1>
                            <p className="text-sm text-muted">
                                {labView === "strategy"
                                    ? "Live strategy simulation monitor + PDF reporting"
                                    : "Portfolio buy-in backtests with remote C++ routing"
                                }
                            </p>
                        </div>
                    </div>
                    <div className={`flex items-center gap-2 px-3 py-1.5 rounded-lg border text-xs font-semibold ${connected ? "text-green border-green/30 bg-green/10" : "text-yellow-300 border-yellow-500/30 bg-yellow-500/10"}`}>
                        <span className={`inline-block w-1.5 h-1.5 rounded-full ${connected ? "bg-green-400" : "bg-yellow-400 animate-pulse"}`} />
                        {connected ? "Socket online" : "Socket offline"}
                        {!connected && (
                            <button
                                onClick={() => reconnect()}
                                className="ml-1 underline underline-offset-2 hover:text-white transition-colors"
                                title="Force reconnect"
                            >
                                reconnect
                            </button>
                        )}
                    </div>
                </div>

                <div className="flex flex-wrap items-center gap-2">
                    <button
                        onClick={() => setLabView("strategy")}
                        className={`px-4 py-2 rounded-xl border text-xs font-black uppercase tracking-widest transition-all ${labView === "strategy"
                            ? "bg-accent text-white border-accent shadow-accent/20 shadow-lg"
                            : "bg-card border-border text-muted hover:text-white hover:border-accent/30"
                            }`}
                    >
                        Strategy Backtests
                    </button>
                    <button
                        onClick={() => setLabView("portfolio")}
                        className={`px-4 py-2 rounded-xl border text-xs font-black uppercase tracking-widest transition-all ${labView === "portfolio"
                            ? "bg-cyan-600 text-white border-cyan-500 shadow-cyan-600/20 shadow-lg"
                            : "bg-card border-border text-muted hover:text-white hover:border-cyan-400/30"
                            }`}
                    >
                        Portfolio Backtest
                    </button>
                </div>

                {labView === "strategy" ? (
                <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
                    <div className="lg:col-span-4 bg-card border border-border rounded-2xl p-6 h-fit shadow-sm relative overflow-hidden">
                        <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-accent to-purple-500" />

                        <h2 className="text-lg font-semibold flex items-center gap-2 mb-6">
                            <FileTerminal size={18} className="text-accent" />
                            Simulation Parameters
                        </h2>

                        <div className="space-y-5">
                            <div>
                                <label className="text-[10px] text-muted uppercase tracking-widest font-semibold block mb-2">Asset Symbol</label>
                                <input
                                    type="text"
                                    value={symbol}
                                    onChange={(event) => setSymbol(event.target.value.toUpperCase())}
                                    className="w-full bg-background border border-border rounded-xl p-3 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all uppercase"
                                    placeholder="AAPL"
                                />
                            </div>

                            <div>
                                <label className="text-[10px] text-muted uppercase tracking-widest font-semibold block mb-2">Strategy</label>
                                <select
                                    value={strategyName}
                                    onChange={(e) => setStrategyName(e.target.value)}
                                    className="w-full bg-background border border-border rounded-xl p-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all"
                                >
                                    <option value="ORB_FVG_ENGULFING">ORB FVG Engulfing (M1/M5)</option>
                                    <option value="ICT_VP">ICT Liquidity + Volume Profile</option>
                                    <option value="IV_REGIME">IV Regime (Daily · BS Implied Vol)</option>
                                </select>
                            </div>

                            {strategyName === "IV_REGIME" && (
                                <div className="p-4 rounded-xl border border-cyan-500/20 bg-cyan-500/5 space-y-3 animate-fade-in">
                                    <p className="text-[10px] font-bold uppercase tracking-widest text-cyan-400 flex items-center gap-1.5">
                                        <CandlestickChart size={12} /> IV Regime Parameters
                                    </p>

                                    <div className="grid grid-cols-2 gap-3">
                                        <div>
                                            <label className="text-[10px] text-muted uppercase tracking-wider block mb-1">IV Rank Low %</label>
                                            <input type="number" value={ivrLow} onChange={e => setIvrLow(e.target.value)} min="0" max="50"
                                                className="w-full bg-background border border-border rounded-lg p-2 text-xs font-mono focus:outline-none focus:ring-1 focus:ring-cyan-400/40" />
                                        </div>
                                        <div>
                                            <label className="text-[10px] text-muted uppercase tracking-wider block mb-1">IV Rank High %</label>
                                            <input type="number" value={ivrHigh} onChange={e => setIvrHigh(e.target.value)} min="50" max="100"
                                                className="w-full bg-background border border-border rounded-lg p-2 text-xs font-mono focus:outline-none focus:ring-1 focus:ring-cyan-400/40" />
                                        </div>
                                        <div>
                                            <label className="text-[10px] text-muted uppercase tracking-wider block mb-1">Momentum (days)</label>
                                            <input type="number" value={ivrMom} onChange={e => setIvrMom(e.target.value)} min="1" max="60"
                                                className="w-full bg-background border border-border rounded-lg p-2 text-xs font-mono focus:outline-none focus:ring-1 focus:ring-cyan-400/40" />
                                        </div>
                                        <div>
                                            <label className="text-[10px] text-muted uppercase tracking-wider block mb-1">Max Hold (days)</label>
                                            <input type="number" value={ivrHold} onChange={e => setIvrHold(e.target.value)} min="1" max="60"
                                                className="w-full bg-background border border-border rounded-lg p-2 text-xs font-mono focus:outline-none focus:ring-1 focus:ring-cyan-400/40" />
                                        </div>
                                        <div>
                                            <label className="text-[10px] text-muted uppercase tracking-wider block mb-1">SL Vol Mult ×</label>
                                            <input type="number" value={ivrSlMult} onChange={e => setIvrSlMult(e.target.value)} min="0.5" max="10" step="0.5"
                                                className="w-full bg-background border border-border rounded-lg p-2 text-xs font-mono focus:outline-none focus:ring-1 focus:ring-cyan-400/40" />
                                        </div>
                                        <div>
                                            <label className="text-[10px] text-muted uppercase tracking-wider block mb-1">R:R Target</label>
                                            <input type="number" value={ivrRR} onChange={e => setIvrRR(e.target.value)} min="0.5" max="10" step="0.5"
                                                className="w-full bg-background border border-border rounded-lg p-2 text-xs font-mono focus:outline-none focus:ring-1 focus:ring-cyan-400/40" />
                                        </div>
                                        <div className="col-span-2">
                                            <label className="text-[10px] text-muted uppercase tracking-wider block mb-1">Risk per Trade %</label>
                                            <input type="number" value={ivrRisk} onChange={e => setIvrRisk(e.target.value)} min="0.1" max="25" step="0.1"
                                                className="w-full bg-background border border-border rounded-lg p-2 text-xs font-mono focus:outline-none focus:ring-1 focus:ring-cyan-400/40" />
                                        </div>
                                    </div>

                                    <div className="flex flex-col gap-2 pt-1">
                                        <div className="flex items-center justify-between">
                                            <span className="text-[10px] text-muted uppercase tracking-wider">Markov State Filter</span>
                                            <button onClick={() => setIvrMarkov(!ivrMarkov)}
                                                className={`w-8 h-4 rounded-full relative transition-colors ${ivrMarkov ? "bg-cyan-500" : "bg-border"}`}>
                                                <div className={`w-3 h-3 rounded-full bg-white absolute top-0.5 transition-all ${ivrMarkov ? "left-4" : "left-0.5"}`} />
                                            </button>
                                        </div>
                                        <div className="flex items-center justify-between">
                                            <span className="text-[10px] text-muted uppercase tracking-wider">Allow Short</span>
                                            <button onClick={() => setIvrShort(!ivrShort)}
                                                className={`w-8 h-4 rounded-full relative transition-colors ${ivrShort ? "bg-cyan-500" : "bg-border"}`}>
                                                <div className={`w-3 h-3 rounded-full bg-white absolute top-0.5 transition-all ${ivrShort ? "left-4" : "left-0.5"}`} />
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            )}

                            <div className="space-y-4 pt-2 border-t border-border/40">
                                <div className="flex items-center justify-between">
                                    <label className="text-[10px] text-muted uppercase tracking-widest font-bold">Time Window</label>
                                    <div className="flex gap-1.5">
                                        {[
                                            { label: "1M", value: 1 },
                                            { label: "3M", value: 3 },
                                            { label: "6M", value: 6 },
                                            { label: "1Y", value: 12 },
                                            { label: "YTD", value: 'ytd' as const }
                                        ].map(range => (
                                            <button
                                                key={range.label}
                                                onClick={() => handleQuickDate(range.value)}
                                                className="px-2 py-1 text-[9px] font-bold bg-muted/10 border border-border/50 rounded-md hover:bg-accent/20 hover:border-accent/40 hover:text-accent transition-all text-muted/70 uppercase"
                                            >
                                                {range.label}
                                            </button>
                                        ))}
                                    </div>
                                </div>
                                <div className="grid grid-cols-2 gap-4">
                                    <div>
                                        <label className="text-[10px] text-muted uppercase tracking-widest font-semibold block mb-2 flex items-center gap-1">
                                            <Calendar size={10} /> Start Date
                                        </label>
                                        <input
                                            type="date"
                                            value={startDate}
                                            onChange={(event) => setStartDate(event.target.value)}
                                            className="w-full bg-background border border-border rounded-xl p-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all text-muted"
                                        />
                                    </div>
                                    <div>
                                        <label className="text-[10px] text-muted uppercase tracking-widest font-semibold block mb-2 flex items-center gap-1">
                                            <Calendar size={10} /> End Date
                                        </label>
                                        <input
                                            type="date"
                                            value={endDate}
                                            onChange={(event) => setEndDate(event.target.value)}
                                            className="w-full bg-background border border-border rounded-xl p-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all text-muted"
                                        />
                                    </div>
                                </div>
                            </div>

                            <div>
                                <label className="text-[10px] text-muted uppercase tracking-widest font-semibold block mb-2">Initial Capital ($)</label>
                                <input
                                    type="number"
                                    min="100"
                                    value={account}
                                    onChange={(event) => setAccount(event.target.value)}
                                    className="w-full bg-background border border-border rounded-xl p-3 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all"
                                />
                            </div>

                            <div className="p-4 rounded-xl border border-accent/20 bg-accent/5 space-y-4">
                                <div className="flex items-center justify-between">
                                    <div className="flex items-center gap-2">
                                        <Zap size={14} className="text-yellow-400" />
                                        <label className="text-sm font-semibold">Bootstrap Resampling</label>
                                    </div>
                                    <button
                                        onClick={() => setBootstrap(!bootstrap)}
                                        className={`w-10 h-5 rounded-full relative transition-colors ${bootstrap ? "bg-accent" : "bg-card-hover"}`}
                                    >
                                        <div className={`w-4 h-4 rounded-full bg-white absolute top-0.5 transition-all ${bootstrap ? "left-5" : "left-0.5"}`} />
                                    </button>
                                </div>

                                {bootstrap && (
                                    <div className="animate-fade-in space-y-2">
                                        <label className="text-[10px] text-accent uppercase tracking-widest font-bold block">Monte Carlo Iterations</label>
                                        <select
                                            value={iterations}
                                            onChange={(event) => setIterations(event.target.value)}
                                            className="w-full bg-background border border-border rounded-xl p-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-accent/30 text-muted"
                                        >
                                            <option value="1000">1,000 (Fast)</option>
                                            <option value="5000">5,000 (Detailed)</option>
                                            <option value="10000">10,000 (Deep Analysis)</option>
                                        </select>
                                    </div>
                                )}
                            </div>
                        </div>

                        <button
                            onClick={strategyName === "IV_REGIME" ? handleRunIVRegime : handleRunBacktest}
                            disabled={launching || isRunning || !symbol || !startDate || !endDate}
                            className={`w-full py-3.5 mt-6 rounded-xl font-bold text-sm transition-all shadow-lg flex justify-center items-center gap-2 ${launching || isRunning ? "bg-accent/50 cursor-not-allowed text-white"
                                : strategyName === "IV_REGIME" ? "bg-cyan-600 hover:bg-cyan-500 text-white shadow-cyan-600/20"
                                    : "bg-accent hover:bg-accent-hover text-white shadow-accent/20"
                                }`}
                        >
                            {launching || isRunning ? <Loader2 size={16} className="animate-spin" /> : <Play fill="currentColor" size={14} />}
                            {launching ? "Starting..." : isRunning ? "Running..." : strategyName === "IV_REGIME" ? "Run IV Regime Backtest" : "Run Backtest Analysis"}
                        </button>
                    </div>

                    <div className="lg:col-span-8 flex flex-col gap-6">
                        {!launching && !isRunning && !completedResult && !errorMessage && (
                            <div className="flex-1 bg-card border border-border border-dashed rounded-2xl flex flex-col items-center justify-center text-muted p-10 min-h-[520px]">
                                <Activity size={48} className="text-muted/30 mb-4" />
                                <h3 className="text-lg font-semibold text-foreground">Awaiting Simulation</h3>
                                <p className="text-sm mt-2 max-w-sm text-center">Launch a backtest to watch equity, trades, KPI drift and bootstrap distributions update in real time.</p>
                            </div>
                        )}

                        {(launching || isRunning || completedResult || errorMessage) && (
                            <>
                                {errorMessage && (
                                    <div className="bg-red/10 border border-red/30 rounded-2xl p-4 flex items-start gap-3 text-red-100">
                                        <TriangleAlert size={18} className="mt-0.5 text-red-300" />
                                        <div>
                                            <p className="font-semibold">Simulation error</p>
                                            <p className="text-sm text-red-100/80 mt-1">{errorMessage}</p>
                                        </div>
                                    </div>
                                )}

                                <div className="grid grid-cols-2 lg:grid-cols-3 gap-4">
                                    <div className="bg-card border border-border rounded-xl p-4">
                                        <p className="text-[10px] text-muted uppercase tracking-wider font-semibold">Net Profit</p>
                                        <p className={`text-xl font-mono font-bold mt-1 ${netProfit >= 0 ? "text-green" : "text-red"}`}>
                                            ${formatCurrency(netProfit)}
                                        </p>
                                    </div>
                                    <div className="bg-card border border-border rounded-xl p-4">
                                        <p className="text-[10px] text-muted uppercase tracking-wider font-semibold">Win Rate</p>
                                        <p className="text-xl font-mono font-bold mt-1 text-white">{formatFractionPercent(displayKpis.win_rate)}</p>
                                        <p className="text-xs text-muted mt-1">{displayKpis.wins}W / {displayKpis.losses}L</p>
                                    </div>
                                    <div className="bg-card border border-border rounded-xl p-4">
                                        <p className="text-[10px] text-muted uppercase tracking-wider font-semibold">Profit Factor</p>
                                        <p className="text-xl font-mono font-bold mt-1 text-purple-400">{formatRatio(displayKpis.profit_factor)}</p>
                                    </div>
                                    <div className="bg-card border border-border rounded-xl p-4">
                                        <p className="text-[10px] text-muted uppercase tracking-wider font-semibold">Max Drawdown</p>
                                        <p className="text-xl font-mono font-bold mt-1 text-red">{formatFractionPercent(displayKpis.max_drawdown_pct)}</p>
                                    </div>
                                    <div className="bg-card border border-border rounded-xl p-4">
                                        <p className="text-[10px] text-muted uppercase tracking-wider font-semibold">Expectancy</p>
                                        <p className="text-xl font-mono font-bold mt-1 text-yellow-300">{displayKpis.expectancy_r.toFixed(2)}R</p>
                                    </div>
                                    <div className="bg-card border border-border rounded-xl p-4">
                                        <p className="text-[10px] text-muted uppercase tracking-wider font-semibold">Trades</p>
                                        <p className="text-xl font-mono font-bold mt-1 text-white">{displayKpis.total_trades}</p>
                                        <p className="text-xs text-muted mt-1">Sharpe {formatRatio(displayKpis.sharpe_ratio)}</p>
                                    </div>
                                </div>

                                <div className="bg-card border border-border rounded-2xl p-6 space-y-6 shadow-sm">
                                    <div className="flex flex-wrap items-center justify-between gap-3">
                                        <div>
                                            <h3 className="text-lg font-semibold">Live Backtest Monitor</h3>
                                            <p className="text-sm text-muted">
                                                {activeSim ? `Simulation ${activeSim}` : "Preparing simulation..."}
                                            </p>
                                        </div>
                                        <div className={`px-3 py-1.5 rounded-lg border text-xs font-semibold ${isRunning ? "text-accent border-accent/30 bg-accent/10" : "text-green border-green/30 bg-green/10"}`}>
                                            {isRunning ? "Running" : completedResult ? "Completed" : launching ? "Launching" : "Idle"}
                                        </div>
                                    </div>

                                    {(launching || isRunning) && (
                                        <div className="space-y-3">
                                            <div className="flex items-center justify-between text-sm">
                                                <span className="text-muted">Progress</span>
                                                <span className="font-mono text-white">{progress.day}/{progress.total || "?"} sessions</span>
                                            </div>
                                            <div className="w-full h-3 rounded-full bg-background overflow-hidden border border-border">
                                                <div className="h-full bg-gradient-to-r from-accent to-cyan-400 transition-all duration-300" style={{ width: `${progress.pct}%` }} />
                                            </div>
                                        </div>
                                    )}

                                    <div className="bg-background rounded-2xl border border-border p-4">
                                        <div className="flex items-center justify-between mb-4">
                                            <div>
                                                <p className="text-sm font-semibold">Equity Curve</p>
                                                <p className="text-xs text-muted">Trade-by-trade capital trajectory</p>
                                            </div>
                                            <p className="text-xs text-muted">{equityCurve.length} points</p>
                                        </div>
                                        <div className="h-64">
                                            <ResponsiveContainer width="100%" height="100%">
                                                <AreaChart data={equityCurve} margin={{ top: 10, right: 12, left: 0, bottom: 0 }}>
                                                    <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.06)" />
                                                    <XAxis dataKey="label" tick={{ fill: "#9ca3af", fontSize: 11 }} minTickGap={24} />
                                                    <YAxis tick={{ fill: "#9ca3af", fontSize: 11 }} tickFormatter={(value) => `$${Number(value).toFixed(0)}`} width={70} />
                                                    <Tooltip formatter={(value: any) => [`$${formatCurrency(Number(value))}`, "Equity"]} />
                                                    <Area type="monotone" dataKey="equity" stroke="#22c55e" fill="rgba(34,197,94,0.16)" strokeWidth={2} />
                                                </AreaChart>
                                            </ResponsiveContainer>
                                        </div>
                                    </div>

                                    {trades.length > 0 && (
                                        <div className="bg-background rounded-2xl border border-border p-4">
                                            <div className="flex items-center justify-between mb-3">
                                                <div>
                                                    <p className="text-sm font-semibold">Price Chart — {activeSymbol}</p>
                                                    <p className="text-xs text-muted">Daily closes · SMA 20 · Entry ▲▼ / Exit □ markers</p>
                                                </div>
                                                <p className="text-xs text-muted font-mono">{trades.length} trades</p>
                                            </div>
                                            <BacktestPriceChart
                                                trades={trades}
                                                symbol={activeSymbol}
                                                startDate={startDate}
                                                endDate={endDate}
                                            />
                                        </div>
                                    )}

                                    {bootstrapLive && (profitHistogram.length > 0 || drawdownHistogram.length > 0) && (
                                        <div className="grid grid-cols-1 xl:grid-cols-2 gap-4">
                                            <div className="bg-background rounded-2xl border border-border p-4">
                                                <p className="text-sm font-semibold mb-1">Bootstrap Net Profit</p>
                                                <p className="text-xs text-muted mb-4">95% CI: ${displayBootstrap?.net_profit_95_ci[0].toFixed(0)} to ${displayBootstrap?.net_profit_95_ci[1].toFixed(0)}</p>
                                                <div className="h-56">
                                                    <ResponsiveContainer width="100%" height="100%">
                                                        <BarChart data={profitHistogram} margin={{ top: 8, right: 8, left: -18, bottom: 0 }}>
                                                            <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.06)" />
                                                            <XAxis dataKey="label" tick={{ fill: "#9ca3af", fontSize: 10 }} minTickGap={20} />
                                                            <YAxis tick={{ fill: "#9ca3af", fontSize: 10 }} allowDecimals={false} width={42} />
                                                            <Tooltip formatter={(value: number | string | undefined) => [Number(value ?? 0), "Count"]} />
                                                            <Bar dataKey="count" radius={[3, 3, 0, 0]}>
                                                                {profitHistogram.map((entry, index) => (
                                                                    <Cell key={`profit-${index}`} fill={entry.color} />
                                                                ))}
                                                            </Bar>
                                                        </BarChart>
                                                    </ResponsiveContainer>
                                                </div>
                                            </div>

                                            <div className="bg-background rounded-2xl border border-border p-4">
                                                <p className="text-sm font-semibold mb-1">Bootstrap Max Drawdown</p>
                                                <p className="text-xs text-muted mb-4">95% CI: {displayBootstrap?.max_drawdown_95_ci_pct[0].toFixed(2)}% to {displayBootstrap?.max_drawdown_95_ci_pct[1].toFixed(2)}%</p>
                                                <div className="h-56">
                                                    <ResponsiveContainer width="100%" height="100%">
                                                        <BarChart data={drawdownHistogram} margin={{ top: 8, right: 8, left: -18, bottom: 0 }}>
                                                            <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.06)" />
                                                            <XAxis dataKey="label" tick={{ fill: "#9ca3af", fontSize: 10 }} minTickGap={20} />
                                                            <YAxis tick={{ fill: "#9ca3af", fontSize: 10 }} allowDecimals={false} width={42} />
                                                            <Tooltip formatter={(value: number | string | undefined) => [Number(value ?? 0), "Count"]} />
                                                            <Bar dataKey="count" radius={[3, 3, 0, 0]}>
                                                                {drawdownHistogram.map((entry, index) => (
                                                                    <Cell key={`drawdown-${index}`} fill={entry.color} />
                                                                ))}
                                                            </Bar>
                                                        </BarChart>
                                                    </ResponsiveContainer>
                                                </div>
                                            </div>
                                        </div>
                                    )}

                                    <div className="bg-background rounded-2xl border border-border p-4">
                                        <div className="flex items-center justify-between mb-4">
                                            <div>
                                                <p className="text-sm font-semibold">Trade Log</p>
                                                <p className="text-xs text-muted">Every resolved trade arrives here in real time</p>
                                            </div>
                                            <p className="text-xs text-muted">{trades.length} rows</p>
                                        </div>
                                        <div className="max-h-80 overflow-y-auto rounded-xl border border-border">
                                            <table className="w-full text-sm">
                                                <thead className="sticky top-0 bg-card z-10">
                                                    <tr className="text-left text-[10px] uppercase tracking-wider text-muted">
                                                        <th className="px-3 py-3">Time</th>
                                                        <th className="px-3 py-3">Dir</th>
                                                        <th className="px-3 py-3">Entry</th>
                                                        <th className="px-3 py-3">Exit</th>
                                                        <th className="px-3 py-3">Outcome</th>
                                                        <th className="px-3 py-3">R</th>
                                                        <th className="px-3 py-3 text-right">PnL $</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    {trades.length === 0 && (
                                                        <tr>
                                                            <td colSpan={7} className="px-3 py-6 text-center text-sm text-muted">Waiting for the first closed trade...</td>
                                                        </tr>
                                                    )}
                                                    {trades.map((trade) => (
                                                        <tr key={`${trade.signal_id}-${trade.exit_timestamp || trade.timestamp}`} className="border-t border-border/60">
                                                            <td className="px-3 py-2 font-mono text-xs text-muted">{formatTimestampLabel(trade.exit_timestamp || trade.timestamp)}</td>
                                                            <td className={`px-3 py-2 font-semibold ${trade.direction === "LONG" ? "text-green" : "text-red"}`}>{trade.direction}</td>
                                                            <td className="px-3 py-2 font-mono">{formatCurrency(trade.entry)}</td>
                                                            <td className="px-3 py-2 font-mono">{formatCurrency(trade.exit_price ?? trade.tp)}</td>
                                                            <td className="px-3 py-2 text-xs text-muted">{trade.outcome}</td>
                                                            <td className={`px-3 py-2 font-mono ${trade.pnl_r >= 0 ? "text-green" : "text-red"}`}>{trade.pnl_r.toFixed(2)}R</td>
                                                            <td className={`px-3 py-2 font-mono text-right ${trade.pnl_usd >= 0 ? "text-green" : "text-red"}`}>${formatCurrency(trade.pnl_usd)}</td>
                                                        </tr>
                                                    ))}
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>

                                    {displayBootstrap && (
                                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 bg-background rounded-2xl p-5 border border-border">
                                            <div>
                                                <p className="text-xs text-muted uppercase tracking-wider mb-1">Expected Profit Range</p>
                                                <p className="text-lg font-mono font-bold text-white">
                                                    ${displayBootstrap.net_profit_95_ci[0].toLocaleString(undefined, { maximumFractionDigits: 0 })}
                                                    <span className="text-muted mx-2">to</span>
                                                    ${displayBootstrap.net_profit_95_ci[1].toLocaleString(undefined, { maximumFractionDigits: 0 })}
                                                </p>
                                            </div>
                                            <div>
                                                <p className="text-xs text-muted uppercase tracking-wider mb-1">Worst Case Drawdown</p>
                                                <p className="text-lg font-mono font-bold text-red">
                                                    Up to {displayBootstrap.max_drawdown_95_ci_pct[1].toFixed(2)}%
                                                </p>
                                            </div>
                                        </div>
                                    )}

                                    {/* IV Smile panel — appears after backtest completes */}
                                    {(ivData || ivLoading) && (
                                        <div>
                                            {ivLoading && (
                                                <div className="bg-background rounded-2xl border border-border p-4 flex items-center gap-3">
                                                    <div className="h-4 w-4 border-2 border-purple-500 border-t-transparent rounded-full animate-spin" />
                                                    <span className="text-xs text-muted font-mono uppercase tracking-widest animate-pulse">Computing Implied Volatility Smile…</span>
                                                </div>
                                            )}
                                            {ivData && <IvSmilePanel data={ivData} />}
                                        </div>
                                    )}

                                    {/* GARCH(1,1) conditional vol panel */}
                                    {(archData || archLoading) && (
                                        <div>
                                            {archLoading && (
                                                <div className="bg-background rounded-2xl border border-border p-4 flex items-center gap-3 mt-3">
                                                    <div className="h-4 w-4 border-2 border-violet-500 border-t-transparent rounded-full animate-spin" />
                                                    <span className="text-xs text-muted font-mono uppercase tracking-widest animate-pulse">Fitting GARCH(1,1) model…</span>
                                                </div>
                                            )}
                                            {archData && <ArchVolPanel data={archData} />}
                                        </div>
                                    )}

                                    {(kalmanData || kalmanLoading) && (
                                        <div>
                                            {kalmanLoading && (
                                                <div className="bg-background rounded-2xl border border-border p-4 flex items-center gap-3 mt-3">
                                                    <div className="h-4 w-4 border-2 border-emerald-500 border-t-transparent rounded-full animate-spin" />
                                                    <span className="text-xs text-muted font-mono uppercase tracking-widest animate-pulse">Running Kalman state filter…</span>
                                                </div>
                                            )}
                                            {kalmanData && <KalmanFilterPanel data={kalmanData} />}
                                        </div>
                                    )}

                                    {/* IV Regime — current signal badge */}
                                    {ivCurrentSignal && (
                                        <div className="bg-background rounded-2xl border border-cyan-500/30 p-4 mt-3">
                                            <p className="text-[10px] font-bold uppercase tracking-widest text-cyan-400 mb-3">
                                                IV Regime — Current Signal ({ivCurrentSignal.date})
                                            </p>
                                            <p className="text-[10px] text-muted mb-3">
                                                Historical backtest uses proxy IV rank. Live option context below comes from real option prices inverted through Black-Scholes.
                                            </p>
                                            <div className="flex flex-wrap gap-3 items-center">
                                                <span className={`px-4 py-2 rounded-xl font-bold text-sm border ${ivCurrentSignal.direction === "LONG"
                                                    ? "bg-emerald-500/15 border-emerald-500/40 text-emerald-300"
                                                    : ivCurrentSignal.direction === "SHORT"
                                                        ? "bg-red-500/15 border-red-500/40 text-red-300"
                                                        : "bg-zinc-700/40 border-zinc-600/30 text-zinc-400"
                                                    }`}>
                                                    {ivCurrentSignal.direction}
                                                </span>
                                                <div className="bg-muted/10 rounded-xl px-3 py-2 border border-border/50">
                                                    <p className="text-[9px] text-muted uppercase tracking-wider">Proxy IV Rank</p>
                                                    <p className="text-sm font-bold font-mono text-cyan-300">{ivCurrentSignal.iv_rank.toFixed(1)}%</p>
                                                </div>
                                                {ivCurrentSignal.signal_source && (
                                                    <div className="bg-muted/10 rounded-xl px-3 py-2 border border-border/50">
                                                        <p className="text-[9px] text-muted uppercase tracking-wider">Signal Source</p>
                                                        <p className="text-sm font-bold font-mono text-sky-300">{ivCurrentSignal.signal_source.replace(/_/g, " ")}</p>
                                                    </div>
                                                )}
                                                <div className="bg-muted/10 rounded-xl px-3 py-2 border border-border/50">
                                                    <p className="text-[9px] text-muted uppercase tracking-wider">Regime</p>
                                                    <p className={`text-sm font-bold font-mono ${ivCurrentSignal.regime === "Low" ? "text-emerald-400"
                                                        : ivCurrentSignal.regime === "Mid" ? "text-yellow-400"
                                                            : "text-red-400"
                                                        }`}>{ivCurrentSignal.regime}</p>
                                                </div>
                                                <div className="bg-muted/10 rounded-xl px-3 py-2 border border-border/50">
                                                    <p className="text-[9px] text-muted uppercase tracking-wider">Momentum</p>
                                                    <p className={`text-sm font-bold font-mono ${ivCurrentSignal.momentum_pct >= 0 ? "text-emerald-400" : "text-red-400"}`}>
                                                        {ivCurrentSignal.momentum_pct >= 0 ? "+" : ""}{ivCurrentSignal.momentum_pct.toFixed(2)}%
                                                    </p>
                                                </div>
                                                <div className="bg-muted/10 rounded-xl px-3 py-2 border border-border/50">
                                                    <p className="text-[9px] text-muted uppercase tracking-wider">Close</p>
                                                    <p className="text-sm font-bold font-mono text-foreground">${ivCurrentSignal.close.toFixed(2)}</p>
                                                </div>
                                                {ivCurrentSignal.daily_vol_pct != null && (
                                                    <div className="bg-muted/10 rounded-xl px-3 py-2 border border-border/50">
                                                        <p className="text-[9px] text-muted uppercase tracking-wider">Daily Vol σ</p>
                                                        <p className="text-sm font-bold font-mono text-violet-300">{ivCurrentSignal.daily_vol_pct.toFixed(2)}%</p>
                                                    </div>
                                                )}
                                                {ivCurrentSignal.realized_vol_ann_pct != null && (
                                                    <div className="bg-muted/10 rounded-xl px-3 py-2 border border-border/50">
                                                        <p className="text-[9px] text-muted uppercase tracking-wider">Realized Vol Ann.</p>
                                                        <p className="text-sm font-bold font-mono text-fuchsia-300">{ivCurrentSignal.realized_vol_ann_pct.toFixed(2)}%</p>
                                                    </div>
                                                )}
                                            </div>

                                            {ivCurrentSignal.option_context?.available && (
                                                <div className="mt-4 pt-4 border-t border-border/60">
                                                    <p className="text-[10px] font-bold uppercase tracking-widest text-amber-400 mb-3">
                                                        Live Option IV Context
                                                    </p>
                                                    <div className="flex flex-wrap gap-3 items-center">
                                                        {ivCurrentSignal.option_context.direction_bias && (
                                                            <span className={`px-4 py-2 rounded-xl font-bold text-sm border ${ivCurrentSignal.option_context.direction_bias === "LONG"
                                                                ? "bg-emerald-500/15 border-emerald-500/40 text-emerald-300"
                                                                : ivCurrentSignal.option_context.direction_bias === "SHORT"
                                                                    ? "bg-red-500/15 border-red-500/40 text-red-300"
                                                                    : "bg-zinc-700/40 border-zinc-600/30 text-zinc-400"
                                                                }`}>
                                                                Live Bias {ivCurrentSignal.option_context.direction_bias}
                                                            </span>
                                                        )}
                                                        {ivCurrentSignal.option_context.atm_iv_pct != null && (
                                                            <div className="bg-muted/10 rounded-xl px-3 py-2 border border-border/50">
                                                                <p className="text-[9px] text-muted uppercase tracking-wider">ATM IV</p>
                                                                <p className="text-sm font-bold font-mono text-amber-300">{ivCurrentSignal.option_context.atm_iv_pct.toFixed(2)}%</p>
                                                            </div>
                                                        )}
                                                        {ivCurrentSignal.option_context.iv_realized_spread_pct != null && (
                                                            <div className="bg-muted/10 rounded-xl px-3 py-2 border border-border/50">
                                                                <p className="text-[9px] text-muted uppercase tracking-wider">IV - RV Spread</p>
                                                                <p className={`text-sm font-bold font-mono ${ivCurrentSignal.option_context.iv_realized_spread_pct >= 0 ? "text-red-300" : "text-emerald-300"}`}>
                                                                    {ivCurrentSignal.option_context.iv_realized_spread_pct >= 0 ? "+" : ""}{ivCurrentSignal.option_context.iv_realized_spread_pct.toFixed(2)} pts
                                                                </p>
                                                            </div>
                                                        )}
                                                        {ivCurrentSignal.option_context.iv_realized_ratio != null && (
                                                            <div className="bg-muted/10 rounded-xl px-3 py-2 border border-border/50">
                                                                <p className="text-[9px] text-muted uppercase tracking-wider">IV / RV Ratio</p>
                                                                <p className="text-sm font-bold font-mono text-sky-300">{ivCurrentSignal.option_context.iv_realized_ratio.toFixed(2)}x</p>
                                                            </div>
                                                        )}
                                                        {ivCurrentSignal.option_context.skew_pct != null && (
                                                            <div className="bg-muted/10 rounded-xl px-3 py-2 border border-border/50">
                                                                <p className="text-[9px] text-muted uppercase tracking-wider">Put-Call Skew</p>
                                                                <p className={`text-sm font-bold font-mono ${ivCurrentSignal.option_context.skew_pct >= 0 ? "text-red-300" : "text-emerald-300"}`}>
                                                                    {ivCurrentSignal.option_context.skew_pct >= 0 ? "+" : ""}{ivCurrentSignal.option_context.skew_pct.toFixed(2)} pts
                                                                </p>
                                                            </div>
                                                        )}
                                                        {ivCurrentSignal.option_context.exp_date && (
                                                            <div className="bg-muted/10 rounded-xl px-3 py-2 border border-border/50">
                                                                <p className="text-[9px] text-muted uppercase tracking-wider">Expiry</p>
                                                                <p className="text-sm font-bold font-mono text-foreground">
                                                                    {ivCurrentSignal.option_context.exp_date}
                                                                    {ivCurrentSignal.option_context.dte != null ? ` (${ivCurrentSignal.option_context.dte}d)` : ""}
                                                                </p>
                                                            </div>
                                                        )}
                                                    </div>
                                                </div>
                                            )}

                                            {ivCurrentSignal.option_context && !ivCurrentSignal.option_context.available && (
                                                <div className="mt-4 pt-4 border-t border-border/60">
                                                    <p className="text-[10px] text-muted">
                                                        Live option IV unavailable: {ivCurrentSignal.option_context.error || "No listed options or insufficient chain liquidity."}
                                                    </p>
                                                </div>
                                            )}
                                        </div>
                                    )}

                                    <div className="pt-2 flex flex-wrap items-center gap-3">
                                        {reportUrl ? (
                                            <a
                                                href={reportUrl}
                                                target="_blank"
                                                rel="noreferrer"
                                                className="inline-flex items-center gap-3 px-4 py-3 bg-zinc-800 hover:bg-zinc-700 text-white font-bold rounded-xl transition-all border border-zinc-600 hover:border-accent group"
                                            >
                                                <Download size={18} className="group-hover:text-accent transition-colors" />
                                                Open PDF Report
                                                <ExternalLinkIcon size={16} className="text-muted group-hover:text-white" />
                                            </a>
                                        ) : (
                                            <div className="text-sm text-muted">
                                                {isRunning ? "PDF report will appear here when the run completes." : "No PDF generated for this run."}
                                            </div>
                                        )}
                                    </div>
                                </div>
                            </>
                        )}
                    </div>
                </div>
                ) : (
                    <div className="bg-card border border-border rounded-2xl overflow-hidden shadow-sm">
                        <PortfolioBacktestPanel activeHoldings={activeHoldings} totalValue={totalValue} />
                    </div>
                )}
            </div>
        </AppLayout >
    );
}