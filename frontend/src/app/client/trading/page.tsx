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
    PieChart,
    Play,
    ShieldCheck,
    Target,
    TrendingDown,
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
        color: (bucket.from + bucket.to) / 2 >= 0 ? "#00ffa3" : "#ff2e2e",
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

const REGIME_FILL: Record<number, string> = { 0: "#00ffa3", 1: "#ffa300", 2: "#ff2e2e" };

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
        <div className="bg-[#050505] rounded-3xl border border-white/10 p-6 shadow-2xl">
            {/* Header */}
            <div className="flex flex-wrap items-center justify-between gap-3 mb-6">
                <div>
                    <p className="text-[10px] font-black uppercase tracking-[0.3em] text-white/50">Implied Volatility Smile — {data.symbol}</p>
                    <p className="text-[9px] font-bold text-white/20 mt-1 uppercase tracking-widest">Black-Scholes inversion · σ(K) curve · spot ${data.spot.toFixed(2)}</p>
                </div>
                <div className="flex items-center gap-3">
                    {exp.atm_iv != null && (
                        <div className="px-3 py-1.5 rounded-xl bg-[#d1ff00]/5 border border-[#d1ff00]/20 text-[10px] font-black uppercase tracking-widest text-[#d1ff00]">
                            ATM IV {exp.atm_iv.toFixed(1)}%
                        </div>
                    )}
                    <select
                        value={selectedIdx}
                        onChange={e => setSelectedIdx(Number(e.target.value))}
                        className="bg-black border border-white/10 rounded-xl px-3 py-2 text-[10px] font-black uppercase tracking-widest focus:outline-none focus:ring-1 focus:ring-[#00ffa3]/30 text-white/50"
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
            <div className="flex items-center gap-5 mb-5 text-[9px] font-bold text-white/20 uppercase tracking-[0.15em]">
                <span className="flex items-center gap-2"><span className="inline-block w-3 h-3 rounded-sm bg-[#00ffa3]/20 border border-[#00ffa3]/40" /> IV Calls</span>
                <span className="flex items-center gap-2"><span className="inline-block w-3 h-3 rounded-sm bg-[#ffa300]/20 border border-[#ffa300]/40" /> IV Puts</span>
                <span className="flex items-center gap-1.5 ml-2 text-white/5">|</span>
                <span className="flex items-center gap-1.5">Spot ≈ ${data.spot.toFixed(0)}</span>
                <span className="flex items-center gap-1.5 font-black text-[#00ffa3]">r = {(data.rf * 100).toFixed(1)}%</span>
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
                                    <div className="bg-black border border-white/10 rounded-xl px-4 py-3 text-[10px] font-black uppercase tracking-widest shadow-2xl space-y-2">
                                        <p className="text-white border-b border-white/5 pb-2 mb-2">{label}</p>
                                        <p className="text-white/30">Moneyness: {d.moneyness > 0 ? "+" : ""}{d.moneyness?.toFixed(1)}%</p>
                                        {d.callIv != null && <p className="text-[#00ffa3]">CALL IV: {d.callIv.toFixed(1)}%  ·  ${d.callPrice?.toFixed(2)}</p>}
                                        {d.putIv != null && <p className="text-[#ffa300]">PUT  IV: {d.putIv.toFixed(1)}%  ·  ${d.putPrice?.toFixed(2)}</p>}
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
                        <Line type="monotone" dataKey="callIv" name="CALL IV" stroke="#00ffa3" strokeWidth={3} dot={false} connectNulls isAnimationActive={false} />
                        <Line type="monotone" dataKey="putIv" name="PUT IV" stroke="#ffa300" strokeWidth={2} strokeDasharray="5 5" dot={false} connectNulls isAnimationActive={false} />
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
        <div className="bg-[#050505] rounded-3xl border border-white/10 p-6 shadow-2xl">
            <div className="flex flex-wrap items-center justify-between gap-3 mb-6">
                <div>
                    <h3 className="text-[10px] font-black uppercase tracking-[0.3em] text-white/50">{data.model} Dynamic Volatility — {data.symbol}</h3>
                    <p className="text-[9px] font-bold text-white/20 mt-1 uppercase tracking-widest">
                        MLE parameter audit · α={data.params.alpha.toFixed(3)} β={data.params.beta.toFixed(3)} · persistence {(data.params.persistence * 100).toFixed(1)}%
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
                            <linearGradient id="volGradient" x1="0" y1="0" x2="0" y2="1">
                                <stop offset="5%" stopColor="#00ffa3" stopOpacity={0.2} />
                                <stop offset="95%" stopColor="#00ffa3" stopOpacity={0} />
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
                            content={({ active, payload }) => {
                                if (!active || !payload?.length) return null;
                                const d = payload[0].payload;
                                return (
                                    <div className="bg-black border border-white/10 rounded-xl px-4 py-3 text-[10px] font-black uppercase tracking-widest shadow-2xl space-y-2">
                                        <p className="text-white border-b border-white/5 pb-2 mb-2">{d.date}</p>
                                        <p className="text-[#00ffa3]">ANN VOL: {d.sigma_ann_pct.toFixed(2)}%</p>
                                        <p className="text-white/40">DAILY σ: {d.sigma_pct.toFixed(2)}%</p>
                                        <p className={d.ret_pct >= 0 ? "text-[#00ffa3]" : "text-[#ff2e2e]"}>RETURN: {d.ret_pct.toFixed(2)}%</p>
                                    </div>
                                );
                            }}
                        />
                        <Area type="monotone" dataKey="sigma_ann_pct" stroke="#00ffa3" strokeWidth={3} fill="url(#volGradient)" isAnimationActive={false} />
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
        <div className="bg-[#050505] rounded-3xl border border-white/10 p-6 shadow-2xl">
            <div className="flex flex-wrap items-center justify-between gap-3 mb-6">
                <div>
                    <h3 className="text-[10px] font-black uppercase tracking-[0.3em] text-white/50">Kalman State Filter — {data.symbol}</h3>
                    <p className="text-[9px] font-bold text-white/20 mt-1 uppercase tracking-widest">
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
        const fill = won ? "#00ffa3" : "#ff2e2e"; // Neon green for win, neon red for loss
        return isLong
            ? <polygon key={payload._entryId} points={`${cx},${cy - 10} ${cx - 6},${cy + 2} ${cx + 6},${cy + 2}`} fill={fill} stroke="#0f172a" strokeWidth={0.8} opacity={0.95} />
            : <polygon key={payload._entryId} points={`${cx},${cy + 10} ${cx - 6},${cy - 2} ${cx + 6},${cy - 2}`} fill={fill} stroke="#0f172a" strokeWidth={0.8} opacity={0.95} />;
    };

    const ExitDot = (props: any) => {
        const { cx, cy, payload } = props;
        if (!payload || payload.exitPrice == null || cx == null || cy == null) return null;
        const won = payload._exitOutcome === "win_tp";
        const fill = won ? "#00ffa3" : "#ff2e2e"; // Neon green for win, neon red for loss
        return <rect key={payload._entryId + "_exit"} x={cx - 4} y={cy - 4} width={8} height={8} fill={fill} stroke="#0f172a" strokeWidth={0.8} opacity={0.9} />;
    };

    return (
        <div className="bg-[#050505] rounded-3xl border border-white/10 p-6 shadow-2xl overflow-hidden min-h-[420px]">
            <div className="flex items-center justify-between mb-8 pb-6 border-b border-white/5">
                <div>
                    <h3 className="text-[10px] font-black uppercase tracking-[0.3em] text-white/50">Mechanical Precision Audit — {symbol}</h3>
                    <p className="text-[9px] font-bold text-white/20 mt-1 uppercase tracking-widest">
                        Daily close propagation · SMA(20) baseline · Signal Magnitude Analysis
                    </p>
                </div>
                <div className="flex items-center gap-4">
                    <div className="flex items-center gap-2 text-[9px] font-black uppercase tracking-widest">
                        <span className="h-2 w-2 rounded-full bg-[#00ffa3] shadow-[0_0_8px_#00ffa3]" />
                        <span className="text-white/60">Long Entry</span>
                    </div>
                    <div className="flex items-center gap-2 text-[9px] font-black uppercase tracking-widest">
                        <span className="h-2 w-2 rounded-full bg-[#ff2e2e] shadow-[0_0_8px_#ff2e2e]" />
                        <span className="text-white/60">Short Entry</span>
                    </div>
                </div>
            </div>

            <div className="h-80">
                <ResponsiveContainer width="100%" height="100%">
                    <ComposedChart data={chartData} margin={{ top: 10, right: 10, bottom: 0, left: 0 }}>
                        <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.03)" vertical={false} />
                        <XAxis
                            dataKey="label"
                            tick={{ fill: "#ffffff", fontSize: 9, opacity: 0.3 }}
                            minTickGap={40}
                            axisLine={false}
                            tickLine={false}
                        />
                        <YAxis
                            tick={{ fill: "#ffffff", fontSize: 9, opacity: 0.3 }}
                            tickFormatter={(v) => `$${v.toFixed(0)}`}
                            width={50}
                            domain={["auto", "auto"]}
                            axisLine={false}
                            tickLine={false}
                        />
                        <Tooltip
                            content={({ active, payload }) => {
                                if (!active || !payload?.length) return null;
                                const d = payload[0].payload;
                                return (
                                    <div className="bg-black border border-white/10 rounded-xl px-4 py-3 text-[10px] font-black uppercase tracking-widest shadow-2xl space-y-2">
                                        <p className="text-white border-b border-white/5 pb-2 mb-2">{d.label}</p>
                                        <p className="text-white/40">CLOSE: <span className="text-white">${d.close.toFixed(2)}</span></p>
                                        <p className="text-white/40">SMA20: <span className="text-white/60">${d.sma20.toFixed(2)}</span></p>
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
                        <Line type="monotone" dataKey="close" stroke="#ffffff" strokeOpacity={0.1} strokeWidth={1} dot={false} isAnimationActive={false} />
                        <Line type="monotone" dataKey="sma20" stroke="#ffffff" strokeOpacity={0.05} strokeWidth={1} strokeDasharray="3 3" dot={false} isAnimationActive={false} />
                        <Line
                            type="monotone"
                            dataKey="entryPrice"
                            stroke="transparent"
                            dot={<EntryDot />}
                            isAnimationActive={false}
                            connectNulls={false}
                        />
                        <Line
                            type="monotone"
                            dataKey="exitPrice"
                            stroke="transparent"
                            dot={<ExitDot />}
                            isAnimationActive={false}
                            connectNulls={false}
                        />
                    </ComposedChart>
                </ResponsiveContainer>
            </div>

            {/* Regime distribution summary */}
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
                        <div className="h-10 w-10 rounded-xl bg-[#00ffa3]/10 flex items-center justify-center border border-[#00ffa3]/20">
                            <CandlestickChart size={20} className="text-[#00ffa3]" />
                        </div>
                        <div>
                            <h1 className="text-2xl font-black uppercase tracking-[0.25em] text-white">Advanced Simulation</h1>
                            <div className="flex items-center gap-3 mt-1">
                                <span className="text-[10px] font-bold text-[#00ffa3]/60 uppercase tracking-widest">Stable v2.4</span>
                                <div className="h-1 w-1 rounded-full bg-white/20" />
                                <div className="flex items-center gap-1.5">
                                    <div className="h-1.5 w-1.5 rounded-full bg-[#00ffa3] animate-pulse" />
                                    <span className="text-[10px] font-bold text-white/50 uppercase tracking-widest">Engine Connected</span>
                                </div>
                            </div>
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
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
                        <div className="lg:col-span-4 space-y-6">
                            <div className="bg-[#050505] border border-white/10 rounded-[2rem] p-8 relative overflow-hidden shadow-2xl">
                                <div className="absolute top-0 right-0 w-64 h-64 bg-[#00ffa3]/5 rounded-full blur-[100px] -mr-32 -mt-32" />

                                <div className="relative space-y-8">
                                    <div className="flex items-center gap-3 pb-6 border-b border-white/5">
                                        <FileTerminal size={18} className="text-[#00ffa3]" />
                                        <h2 className="text-xs font-black uppercase tracking-[0.3em] text-white/90">System Parameters</h2>
                                    </div>

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
                                        disabled={launching || isRunning}
                                        className="w-full py-5 rounded-2xl bg-[#00ffa3] text-black font-black uppercase tracking-[0.3em] text-sm hover:scale-[1.02] active:scale-[0.98] transition-all shadow-[0_0_30px_rgba(0,255,163,0.3)] disabled:opacity-50 disabled:hover:scale-100 flex items-center justify-center gap-3"
                                    >
                                        {launching || isRunning ? <Loader2 className="animate-spin" size={20} /> : <Play size={18} className="fill-current" />}
                                        {launching ? "Starting..." : isRunning ? "Running..." : strategyName === "IV_REGIME" ? "Execute IV Regime" : "Launch Engine"}
                                    </button>
                                </div>
                            </div>
                        </div>

                        <div className="lg:col-span-8 flex flex-col gap-6">
                            {!launching && !isRunning && !completedResult && !errorMessage && (
                                <div className="flex-1 bg-[#050505] border border-white/5 border-dashed rounded-3xl flex flex-col items-center justify-center text-muted p-10 min-h-[520px]">
                                    <Activity size={48} className="text-white/10 mb-6" />
                                    <h3 className="text-lg font-black uppercase tracking-[0.2em] text-white/40">Engine Offline</h3>
                                    <p className="text-[10px] mt-4 max-w-sm text-center font-bold uppercase tracking-widest text-white/20">Awaiting simulation parameters for real-time equity propagation.</p>
                                </div>
                            )}

                            {(launching || isRunning || completedResult || errorMessage) && (
                                <>
                                    {errorMessage && (
                                        <div className="bg-[#ff2e2e]/5 border border-[#ff2e2e]/20 rounded-2xl p-5 flex items-start gap-4 text-[#ff2e2e]">
                                            <TriangleAlert size={20} className="mt-0.5" />
                                            <div>
                                                <p className="font-black uppercase tracking-widest text-xs">Critical Exception</p>
                                                <p className="text-[11px] font-bold mt-1 text-[#ff2e2e]/80 uppercase tracking-widest">{errorMessage}</p>
                                            </div>
                                        </div>
                                    )}

                                    <div className="grid grid-cols-2 lg:grid-cols-3 gap-6">
                                        {[
                                            { label: "Net Pnl", value: `${netProfit >= 0 ? "+" : ""}$${formatCurrency(netProfit)}`, color: netProfit >= 0 ? "text-[#00ffa3] drop-shadow-[0_0_8px_rgba(0,255,163,0.4)]" : "text-[#ff2e2e] drop-shadow-[0_0_8px_rgba(255,46,46,0.4)]", desc: `${displayKpis.total_r.toFixed(1)}R Drift`, icon: Activity },
                                            { label: "Win Rate", value: formatFractionPercent(displayKpis.win_rate), color: "text-white", desc: `${displayKpis.wins}W / ${displayKpis.losses}L`, icon: PieChart },
                                            { label: "Profit Factor", value: formatRatio(displayKpis.profit_factor), color: "text-[#d1ff00]", desc: "Gross Ratio", icon: Zap },
                                            { label: "Max Drawdown", value: formatFractionPercent(displayKpis.max_drawdown_pct), color: "text-[#ff2e2e]", desc: "Equity Risk", icon: TrendingDown },
                                            { label: "Expectancy", value: `${displayKpis.expectancy_r.toFixed(2)}R`, color: "text-[#ffa300]", desc: "Per Unit Risk", icon: Target },
                                            { label: "Efficiency", value: formatRatio(displayKpis.sharpe_ratio), color: "text-[#00e0ff]", desc: "Sharpe Ratio", icon: ShieldCheck }
                                        ].map((kpi, i) => (
                                            <div key={i} className="bg-[#050505] border border-white/10 rounded-2xl p-5 shadow-2xl group hover:border-[#00ffa3]/30 transition-all">
                                                <div className="flex items-center justify-between mb-3">
                                                    <p className="text-[9px] font-black uppercase tracking-[0.3em] text-white/40 group-hover:text-[#00ffa3]/60 transition-colors">{kpi.label}</p>
                                                    <kpi.icon size={12} className="text-white/20 group-hover:text-[#00ffa3]/40" />
                                                </div>
                                                <p className={`text-2xl font-black font-mono tracking-tighter mt-1 ${kpi.color}`}>
                                                    {kpi.value}
                                                </p>
                                                <p className="text-[9px] font-bold text-white/20 mt-2 flex items-center gap-2 uppercase tracking-[0.15em]">
                                                    <span className={`h-1 w-1 rounded-full ${i === 0 ? (netProfit >= 0 ? "bg-[#00ffa3]" : "bg-[#ff2e2e]") : "bg-white/20"}`} />
                                                    {kpi.desc}
                                                </p>
                                            </div>
                                        ))}
                                    </div>

                                    <div className="bg-[#050505] border border-white/10 rounded-2xl p-8 space-y-8 shadow-2xl">
                                        <div className="flex flex-wrap items-center justify-between gap-4">
                                            <div>
                                                <h3 className="text-[10px] font-black uppercase tracking-[0.4em] text-white/90">Live Simulation Status</h3>
                                                <p className="text-[10px] font-bold text-white/30 uppercase tracking-widest mt-1">
                                                    {activeSim ? `Identifier: ${activeSim}` : "Awaiting thread assignment..."}
                                                </p>
                                            </div>
                                            <div className={`px-4 py-2 rounded-xl text-[10px] font-black uppercase tracking-[0.2em] border shadow-[0_0_15px_rgba(0,0,0,0.5)] ${isRunning ? "text-[#00ffa3] border-[#00ffa3]/30 bg-[#00ffa3]/5" : "text-[#00e0ff] border-[#00e0ff]/30 bg-[#00e0ff]/5"}`}>
                                                {isRunning ? "Engine Running" : completedResult ? "Audit Completed" : launching ? "Core Initializing" : "System Idle"}
                                            </div>
                                        </div>

                                        {(launching || isRunning) && (
                                            <div className="space-y-4">
                                                <div className="flex items-center justify-between text-[10px] font-black uppercase tracking-[0.2em]">
                                                    <span className="text-white/40">Propagation Progress</span>
                                                    <span className="font-mono text-[#00ffa3]">{progress.day}/{progress.total || "?"} SESSIONS</span>
                                                </div>
                                                <div className="w-full h-2 rounded-full bg-black border border-white/10 overflow-hidden">
                                                    <div className="h-full bg-[#00ffa3] shadow-[0_0_15px_rgba(0,255,163,0.5)] transition-all duration-300" style={{ width: `${progress.pct}%` }} />
                                                </div>
                                            </div>
                                        )}
                                    </div>

                                    <div className="bg-[#050505] rounded-3xl border border-white/10 p-6 shadow-2xl">
                                        <div className="flex items-center justify-between mb-6">
                                            <div>
                                                <p className="text-[10px] font-black uppercase tracking-[0.3em] text-white/50">Equity Trajectory</p>
                                                <p className="text-[9px] font-bold text-white/20 mt-1 uppercase tracking-widest">Real-time capital propagation audit</p>
                                            </div>
                                            <p className="text-[10px] font-mono text-[#00ffa3]/60">{equityCurve.length} DATA_POINTS</p>
                                        </div>
                                        <div className="h-64">
                                            <ResponsiveContainer width="100%" height="100%">
                                                <AreaChart data={equityCurve} margin={{ top: 10, right: 12, left: 0, bottom: 0 }}>
                                                    <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.03)" vertical={false} />
                                                    <XAxis dataKey="label" tick={{ fill: "#ffffff", fontSize: 9, opacity: 0.3 }} minTickGap={40} axisLine={false} tickLine={false} />
                                                    <YAxis tick={{ fill: "#ffffff", fontSize: 9, opacity: 0.3 }} tickFormatter={(value) => `$${Number(value).toFixed(0)}`} width={60} axisLine={false} tickLine={false} />
                                                    <Tooltip
                                                        contentStyle={{ backgroundColor: "#000", border: "1px solid rgba(255,255,255,0.1)", borderRadius: "12px" }}
                                                        itemStyle={{ color: "#00ffa3", fontSize: "11px", fontWeight: "bold" }}
                                                    />
                                                    <Area type="monotone" dataKey="equity" stroke="#00ffa3" fill="url(#neonGradient)" strokeWidth={3} />
                                                    <defs>
                                                        <linearGradient id="neonGradient" x1="0" y1="0" x2="0" y2="1">
                                                            <stop offset="5%" stopColor="#00ffa3" stopOpacity={0.2} />
                                                            <stop offset="95%" stopColor="#00ffa3" stopOpacity={0} />
                                                        </linearGradient>
                                                    </defs>
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

                                    <div className="bg-[#050505] rounded-3xl border border-white/10 p-6 shadow-2xl overflow-hidden">
                                        <div className="flex items-center justify-between mb-6">
                                            <div>
                                                <p className="text-[10px] font-black uppercase tracking-[0.3em] text-white/50">Execution Audit</p>
                                                <p className="text-[9px] font-bold text-white/20 mt-1 uppercase tracking-widest">Verifying mechanical entry/exit precision</p>
                                            </div>
                                            <p className="text-[10px] font-mono text-white/40">{trades.length} TRANSACTIONS</p>
                                        </div>
                                        <div className="max-h-80 overflow-y-auto custom-scrollbar">
                                            <table className="w-full text-left border-collapse">
                                                <thead className="sticky top-0 bg-[#000] z-10">
                                                    <tr className="text-[9px] font-black uppercase tracking-[0.2em] text-white/30 border-b border-white/5">
                                                        <th className="px-4 py-4">Timestamp</th>
                                                        <th className="px-4 py-4 text-center">Bias</th>
                                                        <th className="px-4 py-4">Strike</th>
                                                        <th className="px-4 py-4">Exit</th>
                                                        <th className="px-4 py-4">Status</th>
                                                        <th className="px-4 py-4">Magnitude</th>
                                                        <th className="px-4 py-4 text-right">PnL_USD</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    {trades.length === 0 && (
                                                        <tr>
                                                            <td colSpan={7} className="px-4 py-12 text-center text-[10px] font-bold uppercase tracking-widest text-white/10">Awaiting initial execution cycle...</td>
                                                        </tr>
                                                    )}
                                                    {trades.map((trade) => (
                                                        <tr key={`${trade.signal_id}-${trade.exit_timestamp || trade.timestamp}`} className="border-b border-white/5 hover:bg-white/[0.02] transition-colors group">
                                                            <td className="px-4 py-4 font-mono text-[10px] text-white/40">{formatTimestampLabel(trade.exit_timestamp || trade.timestamp)}</td>
                                                            <td className="px-4 py-4 text-center">
                                                                <span className={`text-[9px] font-black px-2 py-0.5 rounded-sm border ${trade.direction === "LONG" ? "text-[#00ffa3] bg-[#00ffa3]/5 border-[#00ffa3]/20" : "text-[#ff2e2e] bg-[#ff2e2e]/5 border-[#ff2e2e]/20"}`}>
                                                                    {trade.direction}
                                                                </span>
                                                            </td>
                                                            <td className="px-4 py-4 font-mono text-[11px] text-white/80">${formatCurrency(trade.entry)}</td>
                                                            <td className="px-4 py-4 font-mono text-[11px] text-white/60">${formatCurrency(trade.exit_price ?? trade.tp)}</td>
                                                            <td className="px-4 py-4 text-[9px] font-bold uppercase tracking-widest text-white/30">{trade.outcome}</td>
                                                            <td className={`px-4 py-4 font-mono text-[11px] font-black ${trade.pnl_r >= 0 ? "text-[#00ffa3]" : "text-[#ff2e2e]"}`}>{trade.pnl_r >= 0 ? "+" : ""}{trade.pnl_r.toFixed(2)}R</td>
                                                            <td className={`px-4 py-4 font-mono text-[11px] text-right font-black ${trade.pnl_usd >= 0 ? "text-[#00ffa3]" : "text-[#ff2e2e]"}`}>
                                                                {trade.pnl_usd >= 0 ? "+" : ""}${formatCurrency(trade.pnl_usd)}
                                                            </td>
                                                        </tr>
                                                    ))}
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>

                                    {displayBootstrap && (
                                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 bg-[#050505] rounded-3xl p-6 border border-white/10 shadow-2xl">
                                            <div>
                                                <p className="text-[10px] font-black uppercase tracking-[0.3em] text-white/40 mb-3">Expected Profit Range</p>
                                                <p className="text-2xl font-black font-mono text-[#00ffa3] drop-shadow-[0_0_8px_rgba(0,255,163,0.3)]">
                                                    ${displayBootstrap.net_profit_95_ci[0].toLocaleString(undefined, { maximumFractionDigits: 0 })}
                                                    <span className="text-white/20 mx-3 font-normal">—</span>
                                                    ${displayBootstrap.net_profit_95_ci[1].toLocaleString(undefined, { maximumFractionDigits: 0 })}
                                                </p>
                                            </div>
                                            <div>
                                                <p className="text-[10px] font-black uppercase tracking-[0.3em] text-white/40 mb-3">Mechanical Tail Risk</p>
                                                <p className="text-2xl font-black font-mono text-[#ff2e2e] drop-shadow-[0_0_8px_rgba(255,46,46,0.3)]">
                                                    MAX {displayBootstrap.max_drawdown_95_ci_pct[1].toFixed(2)}%
                                                </p>
                                            </div>
                                        </div>
                                    )}

                                    {(ivData || ivLoading) && (
                                        <div className="space-y-6">
                                            {ivLoading && (
                                                <div className="bg-[#050505] rounded-[2rem] border border-white/10 p-8 flex items-center justify-center gap-4 shadow-2xl relative overflow-hidden">
                                                    <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/[0.02] to-transparent animate-pulse" />
                                                    <div className="h-5 w-5 border-3 border-[#00ffa3] border-t-transparent rounded-full animate-spin shadow-[0_0_10px_#00ffa3]" />
                                                    <span className="text-[11px] font-black uppercase tracking-[0.4em] text-white/40 animate-pulse">Core Engine: Constructing IV Surface Audit…</span>
                                                </div>
                                            )}
                                            {ivData && <IvSmilePanel data={ivData} />}
                                        </div>
                                    )}

                                    {/* ARCH / GARCH Volatility Audit */}
                                    {(archData || archLoading) && (
                                        <div className="bg-[#050505] rounded-3xl border border-white/10 p-8 shadow-2xl space-y-6">
                                            {archLoading ? (
                                                <div className="flex items-center justify-center py-12 gap-4">
                                                    <Loader2 className="animate-spin text-[#00ffa3]" size={24} />
                                                    <span className="text-[11px] font-black uppercase tracking-[0.4em] text-white/30 animate-pulse">Fitting GARCH(1,1) Mechanical Model…</span>
                                                </div>
                                            ) : archData ? (
                                                <ArchVolPanel data={archData} />
                                            ) : null}
                                        </div>
                                    )}

                                    {/* Kalman Filter State Estimation */}
                                    {(kalmanData || kalmanLoading) && (
                                        <div className="bg-[#050505] rounded-3xl border border-white/10 p-8 shadow-2xl space-y-6">
                                            {kalmanLoading ? (
                                                <div className="flex items-center justify-center py-12 gap-4">
                                                    <Loader2 className="animate-spin text-[#00ffa3]" size={24} />
                                                    <span className="text-[11px] font-black uppercase tracking-[0.4em] text-white/30 animate-pulse">Running Kalman State Audit…</span>
                                                </div>
                                            ) : kalmanData ? (
                                                <KalmanFilterPanel data={kalmanData} />
                                            ) : null}
                                        </div>
                                    )}

                                    {/* IV Regime Current Signal Audit */}
                                    {ivCurrentSignal && (
                                        <div className="bg-[#050505] rounded-[2.5rem] p-10 border border-white/10 shadow-[0_0_50px_rgba(0,0,0,0.5)] relative overflow-hidden">
                                            <div className="absolute top-0 right-0 p-8">
                                                <div className={`px-5 py-2 rounded-full border text-[10px] font-black uppercase tracking-[0.3em] shadow-lg ${ivCurrentSignal.direction === "LONG" ? "text-[#00ffa3] border-[#00ffa3]/20 bg-[#00ffa3]/5" : ivCurrentSignal.direction === "SHORT" ? "text-[#ff2e2e] border-[#ff2e2e]/20 bg-[#ff2e2e]/5" : "text-white/30 border-white/10"}`}>
                                                    {ivCurrentSignal.direction} SIGNAL
                                                </div>
                                            </div>

                                            <div className="flex items-center gap-6 mb-10 pb-8 border-b border-white/5">
                                                <div className="h-16 w-16 rounded-[1.5rem] bg-[#00ffa3]/10 border border-[#00ffa3]/20 flex items-center justify-center">
                                                    <Activity className="text-[#00ffa3]" size={32} />
                                                </div>
                                                <div>
                                                    <h3 className="text-xl font-black uppercase tracking-[0.4em] text-white">Execution Feedback</h3>
                                                    <p className="text-[10px] font-bold text-white/20 mt-1 uppercase tracking-widest">Mechanical Signal Drift • {ivCurrentSignal.date}</p>
                                                </div>
                                            </div>

                                            <div className="grid grid-cols-2 lg:grid-cols-4 gap-8">
                                                {[
                                                    { label: "Close_Snapshot", val: `$${formatCurrency(ivCurrentSignal.close)}`, sub: "Price Level", color: "text-white" },
                                                    { label: "IV_Rank_Index", val: ivCurrentSignal.iv_rank.toFixed(1), sub: "Volatility Decile", color: "text-[#d1ff00]" },
                                                    { label: "Equity_Momentum", val: `${ivCurrentSignal.momentum_pct > 0 ? "+" : ""}${ivCurrentSignal.momentum_pct.toFixed(2)}%`, sub: "Trend Magnitude", color: ivCurrentSignal.momentum_pct >= 0 ? "text-[#00ffa3]" : "text-[#ff2e2e]" },
                                                    { label: "System_Regime", val: ivCurrentSignal.regime, sub: "Market Context", color: "text-[#00e0ff]" }
                                                ].map((item, i) => (
                                                    <div key={i} className="space-y-2">
                                                        <p className="text-[9px] font-black uppercase tracking-[0.3em] text-white/30">{item.label}</p>
                                                        <p className={`text-2xl font-black font-mono tracking-tighter ${item.color}`}>{item.val}</p>
                                                        <p className="text-[9px] font-bold text-white/10 uppercase tracking-widest">{item.sub}</p>
                                                    </div>
                                                ))}
                                            </div>

                                            {ivCurrentSignal.option_context && (
                                                <div className="mt-12 pt-8 border-t border-white/5">
                                                    <div className="flex items-center justify-between mb-6">
                                                        <p className="text-[10px] font-black uppercase tracking-[0.4em] text-white/50">Market Liquidity Audit</p>
                                                        <p className="text-[9px] font-bold text-[#00ffa3]/60 uppercase tracking-widest">Source: {ivCurrentSignal.option_context.source}</p>
                                                    </div>
                                                    <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
                                                        {ivCurrentSignal.option_context.iv_realized_ratio != null && (
                                                            <div className="bg-white/5 rounded-2xl p-4 border border-white/5">
                                                                <p className="text-[9px] font-black uppercase tracking-widest text-white/30 mb-1">IV/RV Ratio</p>
                                                                <p className="text-base font-black font-mono text-[#00ffa3]">{ivCurrentSignal.option_context.iv_realized_ratio.toFixed(2)}x</p>
                                                            </div>
                                                        )}
                                                        {ivCurrentSignal.option_context.skew_pct != null && (
                                                            <div className="bg-white/5 rounded-2xl p-4 border border-white/5">
                                                                <p className="text-[9px] font-black uppercase tracking-widest text-white/30 mb-1">Skew Factor</p>
                                                                <p className={`text-base font-black font-mono ${ivCurrentSignal.option_context.skew_pct >= 0 ? "text-[#ff2e2e]" : "text-[#00ffa3]"}`}>
                                                                    {ivCurrentSignal.option_context.skew_pct >= 0 ? "+" : ""}{ivCurrentSignal.option_context.skew_pct.toFixed(2)}pts
                                                                </p>
                                                            </div>
                                                        )}
                                                        {ivCurrentSignal.option_context.exp_date && (
                                                            <div className="bg-white/5 rounded-2xl p-4 border border-white/5">
                                                                <p className="text-[9px] font-black uppercase tracking-widest text-white/30 mb-1">Audit Expiry</p>
                                                                <p className="text-base font-black font-mono text-white/80">{ivCurrentSignal.option_context.exp_date}</p>
                                                            </div>
                                                        )}
                                                    </div>
                                                </div>
                                            )}
                                        </div>
                                    )}

                                    {/* Report Generation Area */}
                                    <div className="pt-8 flex flex-wrap items-center gap-4">
                                        {reportUrl ? (
                                            <a
                                                href={reportUrl}
                                                target="_blank"
                                                rel="noreferrer"
                                                className="inline-flex items-center gap-4 px-8 py-4 bg-[#00ffa3] text-black font-black uppercase tracking-[0.3em] rounded-2xl transition-all shadow-[0_0_40px_rgba(0,255,163,0.3)] hover:scale-[1.05] group"
                                            >
                                                <Download size={20} />
                                                Export mechanical audit pdf
                                                <ExternalLinkIcon size={16} className="text-black/40 group-hover:text-black" />
                                            </a>
                                        ) : (
                                            <div className="text-[10px] font-bold text-white/20 uppercase tracking-[0.2em] bg-white/5 px-6 py-4 rounded-2xl border border-white/5">
                                                {isRunning ? "Engine: Finalizing PDF propagation..." : "Mechanical audit unavailable / not generated."}
                                            </div>
                                        )}
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
        </AppLayout>
    );
}