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

import { 
    KpiSnapshot, LiveTrade, ProgressState, BootstrapLiveData, 
    CompletedResult, IVCurrentSignal, ArchVolData, KalmanFilterData, IvSmileData 
} from "@/components/trading/types";
import { 
    formatCurrency, formatRatio, formatFractionPercent, 
    formatTimestampLabel, buildEquityCurve, deriveLiveKpis, buildHistogramData 
} from "@/components/trading/utils";
import { IvSmilePanel } from "@/components/trading/IvSmilePanel";
import { ArchVolPanel } from "@/components/trading/ArchVolPanel";
import { KalmanFilterPanel } from "@/components/trading/KalmanFilterPanel";
import { BacktestPriceChart } from "@/components/trading/BacktestPriceChart";

import { cachedFetch } from "@/lib/cachedFetch";
import {
    getCachedIvSmile, setCachedIvSmile,
    getCachedArchVol, setCachedArchVol,
    getCachedKalman, setCachedKalman,
} from "@/components/trading/analyticsCache";

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

    // ── PREFETCH: eagerly load analytics as soon as the symbol changes ──────
    // This fires IMMEDIATELY on symbol change, not after backtest completion.
    // All 3 endpoints are fetched in parallel. Backend cache (10min TTL)
    // + frontend cache (5min TTL) ensures near-instant response on repeat.
    useEffect(() => {
        if (!symbol || symbol.length < 1) return;

        const sym = symbol.toUpperCase();

        // Debounce: wait 400ms after the user stops typing
        const timer = setTimeout(() => {
            // ── IV Smile ──
            const cachedIv = getCachedIvSmile(sym);
            if (cachedIv) {
                setIvData(cachedIv);
                setIvLoading(false);
            } else {
                setIvLoading(true);
                cachedFetch(`${API_BASE}/api/v1/analytics/implied-vol/${sym}`)
                    .then(r => r.ok ? r.json() : null)
                    .then(d => {
                        if (d?.expirations) {
                            setCachedIvSmile(sym, d);
                            setIvData(d);
                        }
                    })
                    .catch(() => { })
                    .finally(() => setIvLoading(false));
            }

            // ── ARCH / GARCH ──
            const cachedArch = getCachedArchVol(sym);
            if (cachedArch) {
                setArchData(cachedArch);
                setArchLoading(false);
            } else {
                setArchLoading(true);
                cachedFetch(`${API_BASE}/api/v1/analytics/arch-vol/${sym}`)
                    .then(r => r.ok ? r.json() : null)
                    .then(d => {
                        if (d?.conditional_vol) {
                            setCachedArchVol(sym, d);
                            setArchData(d);
                        }
                    })
                    .catch(() => { })
                    .finally(() => setArchLoading(false));
            }

            // ── Kalman Filter ──
            const cachedKalman = getCachedKalman(sym);
            if (cachedKalman) {
                setKalmanData(cachedKalman);
                setKalmanLoading(false);
            } else {
                setKalmanLoading(true);
                cachedFetch(`${API_BASE}/api/v1/analytics/kalman-filter/${sym}?days=300&measurement_noise_mult=4`)
                    .then(r => r.ok ? r.json() : null)
                    .then(d => {
                        if (d?.series) {
                            setCachedKalman(sym, d);
                            setKalmanData(d);
                        }
                    })
                    .catch(() => { })
                    .finally(() => setKalmanLoading(false));
            }
        }, 400);

        return () => clearTimeout(timer);
    }, [symbol]);


    useEffect(() => {
        if (!socket || !activeSim) return;

        const hydrateCompletedTrades = async (simId: string) => {
            try {
                const response = await cachedFetch(`${API_BASE}/api/v1/simulation/results/${encodeURIComponent(simId)}`);
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
                        <div className="h-10 w-10 rounded-xl bg-accent/10 flex items-center justify-center border border-accent/20">
                            <CandlestickChart size={20} className="text-accent" />
                        </div>
                        <div>
                            <h1 className="text-2xl font-black uppercase tracking-[0.25em] text-foreground">Advanced Simulation</h1>
                            <div className="flex items-center gap-3 mt-1">
                                <span className="text-[10px] font-bold text-accent/60 uppercase tracking-widest">Stable v2.4</span>
                                <div className="h-1 w-1 rounded-full bg-muted-foreground/30" />
                                <div className="flex items-center gap-1.5">
                                    <div className="h-1.5 w-1.5 rounded-full bg-accent animate-pulse" />
                                    <span className="text-[10px] font-bold text-muted-foreground/50 uppercase tracking-widest">Engine Connected</span>
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
                            : "bg-card border-border text-muted hover:text-foreground hover:border-accent/30"
                            }`}
                    >
                        Strategy Backtests
                    </button>
                    <button
                        onClick={() => setLabView("portfolio")}
                        className={`px-4 py-2 rounded-xl border text-xs font-black uppercase tracking-widest transition-all ${labView === "portfolio"
                            ? "bg-cyan-600 text-white border-cyan-500 shadow-cyan-600/20 shadow-lg"
                            : "bg-card border-border text-muted hover:text-foreground hover:border-cyan-400/30"
                            }`}
                    >
                        Portfolio Backtest
                    </button>
                </div>

                {labView === "strategy" ? (
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
                        <div className="lg:col-span-4 space-y-6">
                            <div className="dark:bg-[#050505] bg-white border dark:border-white/10 border-zinc-200 rounded-[2rem] p-8 relative overflow-hidden shadow-2xl">
                                <div className="absolute top-0 right-0 w-64 h-64 bg-[#00ffa3]/5 rounded-full blur-[100px] -mr-32 -mt-32" />

                                <div className="relative space-y-8">
                                    <div className="flex items-center gap-3 pb-6 border-b dark:border-white/5 border-zinc-200">
                                        <FileTerminal size={18} className="text-accent" />
                                        <h2 className="text-xs font-black uppercase tracking-[0.3em] dark:text-white/90 text-zinc-800">System Parameters</h2>
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
                                <div className="flex-1 dark:bg-card bg-zinc-50 border dark:border-border border-zinc-200 border-dashed rounded-3xl flex flex-col items-center justify-center text-muted-foreground p-10 min-h-[520px]">
                                    <Activity size={48} className="dark:text-muted/20 text-zinc-300 mb-6" />
                                    <h3 className="text-lg font-black uppercase tracking-[0.2em] dark:text-muted-foreground/40 text-zinc-400">Engine Offline</h3>
                                    <p className="text-[10px] mt-4 max-w-sm text-center font-bold uppercase tracking-widest dark:text-muted-foreground/20 text-zinc-400">Awaiting simulation parameters for real-time equity propagation.</p>
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
                                            { label: "Net Pnl", value: `${netProfit >= 0 ? "+" : ""}$${formatCurrency(netProfit)}`, color: netProfit >= 0 ? "text-emerald-500 drop-shadow-[0_0_8px_rgba(16,185,129,0.3)]" : "text-destructive drop-shadow-[0_0_8px_rgba(239,68,68,0.3)]", desc: `${displayKpis.total_r.toFixed(1)}R Drift`, icon: Activity },
                                            { label: "Win Rate", value: formatFractionPercent(displayKpis.win_rate), color: "text-foreground", desc: `${displayKpis.wins}W / ${displayKpis.losses}L`, icon: PieChart },
                                            { label: "Profit Factor", value: formatRatio(displayKpis.profit_factor), color: "text-yellow-500", desc: "Gross Ratio", icon: Zap },
                                            { label: "Max Drawdown", value: formatFractionPercent(displayKpis.max_drawdown_pct), color: "text-destructive", desc: "Equity Risk", icon: TrendingDown },
                                            { label: "Expectancy", value: `${displayKpis.expectancy_r.toFixed(2)}R`, color: "text-orange-500", desc: "Per Unit Risk", icon: Target },
                                            { label: "Efficiency", value: formatRatio(displayKpis.sharpe_ratio), color: "text-cyan-500", desc: "Sharpe Ratio", icon: ShieldCheck }
                                        ].map((kpi, i) => (
                                            <div key={i} className="bg-card border border-border rounded-2xl p-5 shadow-sm group hover:border-accent/40 transition-all">
                                                <div className="flex items-center justify-between mb-3">
                                                    <p className="text-[9px] font-black uppercase tracking-[0.3em] text-muted-foreground group-hover:text-accent/60 transition-colors">{kpi.label}</p>
                                                    <kpi.icon size={12} className="text-muted/40 group-hover:text-accent/40" />
                                                </div>
                                                <p className={`text-2xl font-black font-mono tracking-tighter mt-1 ${kpi.color}`}>
                                                    {kpi.value}
                                                </p>
                                                <p className="text-[9px] font-bold text-muted-foreground/60 mt-2 flex items-center gap-2 uppercase tracking-[0.15em]">
                                                    <span className={`h-1 w-1 rounded-full ${i === 0 ? (netProfit >= 0 ? "bg-emerald-500" : "bg-destructive") : "bg-muted-foreground/20"}`} />
                                                    {kpi.desc}
                                                </p>
                                            </div>
                                        ))}
                                    </div>

                                    <div className="bg-card border border-border rounded-2xl p-8 space-y-8 shadow-sm">
                                        <div className="flex flex-wrap items-center justify-between gap-4">
                                            <div>
                                                <h3 className="text-[10px] font-black uppercase tracking-[0.4em] text-foreground/90">Live Simulation Status</h3>
                                                <p className="text-[10px] font-bold text-muted-foreground/60 uppercase tracking-widest mt-1">
                                                    {activeSim ? `Identifier: ${activeSim}` : "Awaiting thread assignment..."}
                                                </p>
                                            </div>
                                            <div className={`px-4 py-2 rounded-xl text-[10px] font-black uppercase tracking-[0.2em] border shadow-sm ${isRunning ? "text-emerald-500 border-emerald-500/30 bg-emerald-500/5" : "text-cyan-500 border-cyan-500/30 bg-cyan-500/5"}`}>
                                                {isRunning ? "Engine Running" : completedResult ? "Audit Completed" : launching ? "Core Initializing" : "System Idle"}
                                            </div>
                                        </div>

                                        {(launching || isRunning) && (
                                            <div className="space-y-4">
                                                <div className="flex items-center justify-between text-[10px] font-black uppercase tracking-[0.2em]">
                                                    <span className="text-muted-foreground/60">Propagation Progress</span>
                                                    <span className="font-mono text-accent">{progress.day}/{progress.total || "?"} SESSIONS</span>
                                                </div>
                                                <div className="w-full h-2 rounded-full bg-muted border border-border overflow-hidden">
                                                    <div className="h-full bg-accent shadow-[0_0_15px_rgba(var(--color-accent),0.5)] transition-all duration-300" style={{ width: `${progress.pct}%` }} />
                                                </div>
                                            </div>
                                        )}
                                    </div>

                                    <div className="bg-card border border-border rounded-3xl p-6 shadow-sm">
                                        <div className="flex items-center justify-between mb-6">
                                            <div>
                                                <p className="text-[10px] font-black uppercase tracking-[0.3em] text-muted-foreground">Equity Trajectory</p>
                                                <p className="text-[9px] font-bold text-muted-foreground/40 mt-1 uppercase tracking-widest">Real-time capital propagation audit</p>
                                            </div>
                                            <p className="text-[10px] font-mono text-accent/60">{equityCurve.length} DATA_POINTS</p>
                                        </div>
                                        <div className="h-64">
                                            <ResponsiveContainer width="100%" height="100%">
                                                <AreaChart data={equityCurve} margin={{ top: 10, right: 12, left: 0, bottom: 0 }}>
                                                    <CartesianGrid strokeDasharray="3 3" stroke="hsla(var(--border), 0.15)" vertical={false} />
                                                    <XAxis dataKey="label" tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 9 }} minTickGap={40} axisLine={false} tickLine={false} />
                                                    <YAxis tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 9 }} tickFormatter={(value) => `$${Number(value).toFixed(0)}`} width={60} axisLine={false} tickLine={false} />
                                                    <Tooltip
                                                        contentStyle={{ backgroundColor: "var(--color-card)", border: "1px solid var(--color-border)", borderRadius: "12px" }}
                                                        itemStyle={{ color: "var(--color-accent)", fontSize: "11px", fontWeight: "bold" }}
                                                    />
                                                    <Area type="monotone" dataKey="equity" stroke="var(--color-accent)" fill="url(#neonGradient)" strokeWidth={3} />
                                                    <defs>
                                                        <linearGradient id="neonGradient" x1="0" y1="0" x2="0" y2="1">
                                                            <stop offset="5%" stopColor="var(--color-accent)" stopOpacity={0.25} />
                                                            <stop offset="95%" stopColor="var(--color-accent)" stopOpacity={0.02} />
                                                        </linearGradient>
                                                    </defs>
                                                </AreaChart>
                                            </ResponsiveContainer>
                                        </div>
                                    </div>

                                    {trades.length > 0 && (
                                        <div className="bg-card border border-border rounded-3xl p-6 shadow-sm">
                                            <div className="flex items-center justify-between mb-3">
                                                <div>
                                                    <p className="text-sm font-semibold text-foreground">Price Chart — {activeSymbol}</p>
                                                    <p className="text-xs text-muted-foreground">Daily closes · SMA 20 · Entry ▲▼ / Exit □ markers</p>
                                                </div>
                                                <p className="text-xs text-muted-foreground font-mono">{trades.length} trades</p>
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
                                            <div className="bg-card border border-border rounded-3xl p-6 shadow-sm">
                                                <p className="text-sm font-semibold mb-1 text-foreground">Bootstrap Net Profit</p>
                                                <p className="text-xs text-muted-foreground mb-4">95% CI: ${displayBootstrap?.net_profit_95_ci[0].toFixed(0)} to ${displayBootstrap?.net_profit_95_ci[1].toFixed(0)}</p>
                                                <div className="h-56">
                                                    <ResponsiveContainer width="100%" height="100%">
                                                        <BarChart data={profitHistogram} margin={{ top: 8, right: 8, left: -18, bottom: 0 }}>
                                                            <CartesianGrid strokeDasharray="3 3" stroke="hsla(var(--border), 0.1)" />
                                                            <XAxis dataKey="label" tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 10 }} minTickGap={20} />
                                                            <YAxis tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 10 }} allowDecimals={false} width={42} />
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

                                            <div className="bg-card border border-border rounded-3xl p-6 shadow-sm">
                                                <p className="text-sm font-semibold mb-1 text-foreground">Bootstrap Max Drawdown</p>
                                                <p className="text-xs text-muted-foreground mb-4">95% CI: {displayBootstrap?.max_drawdown_95_ci_pct[0].toFixed(2)}% to {displayBootstrap?.max_drawdown_95_ci_pct[1].toFixed(2)}%</p>
                                                <div className="h-56">
                                                    <ResponsiveContainer width="100%" height="100%">
                                                        <BarChart data={drawdownHistogram} margin={{ top: 8, right: 8, left: -18, bottom: 0 }}>
                                                            <CartesianGrid strokeDasharray="3 3" stroke="hsla(var(--border), 0.1)" />
                                                            <XAxis dataKey="label" tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 10 }} minTickGap={20} />
                                                            <YAxis tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 10 }} allowDecimals={false} width={42} />
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

                                    <div className="bg-card border border-border rounded-3xl p-6 shadow-sm overflow-hidden">
                                        <div className="flex items-center justify-between mb-6">
                                            <div>
                                                <p className="text-[10px] font-black uppercase tracking-[0.3em] text-muted-foreground">Execution Audit</p>
                                                <p className="text-[9px] font-bold text-muted-foreground/40 mt-1 uppercase tracking-widest">Verifying mechanical entry/exit precision</p>
                                            </div>
                                            <p className="text-[10px] font-mono text-muted-foreground/50">{trades.length} TRANSACTIONS</p>
                                        </div>
                                        <div className="max-h-80 overflow-y-auto custom-scrollbar">
                                            <table className="w-full text-left border-collapse">
                                                <thead className="sticky top-0 bg-muted/20 z-10">
                                                    <tr className="text-[9px] font-black uppercase tracking-[0.2em] text-muted-foreground border-b border-border">
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
                                                            <td colSpan={7} className="px-4 py-12 text-center text-[10px] font-bold uppercase tracking-widest dark:text-white/10 text-zinc-300">Awaiting initial execution cycle...</td>
                                                        </tr>
                                                    )}
                                                    {trades.map((trade) => (
                                                        <tr key={`${trade.signal_id}-${trade.exit_timestamp || trade.timestamp}`} className="border-b dark:border-white/5 border-zinc-100 dark:hover:bg-white/[0.02] hover:bg-zinc-50 transition-colors group">
                                                            <td className="px-4 py-4 font-mono text-[10px] dark:text-white/40 text-zinc-500">{formatTimestampLabel(trade.exit_timestamp || trade.timestamp)}</td>
                                                            <td className="px-4 py-4 text-center">
                                                                <span className={`text-[9px] font-black px-2 py-0.5 rounded-sm border ${trade.direction === "LONG" ? "text-emerald-600 dark:text-[#00ffa3] bg-emerald-50 dark:bg-[#00ffa3]/5 border-emerald-200 dark:border-[#00ffa3]/20" : "text-red-600 dark:text-[#ff2e2e] bg-red-50 dark:bg-[#ff2e2e]/5 border-red-200 dark:border-[#ff2e2e]/20"}`}>
                                                                    {trade.direction}
                                                                </span>
                                                            </td>
                                                            <td className="px-4 py-4 font-mono text-[11px] dark:text-white/80 text-zinc-700">${formatCurrency(trade.entry)}</td>
                                                            <td className="px-4 py-4 font-mono text-[11px] dark:text-white/60 text-zinc-500">${formatCurrency(trade.exit_price ?? trade.tp)}</td>
                                                            <td className="px-4 py-4 text-[9px] font-bold uppercase tracking-widest dark:text-white/30 text-zinc-400">{trade.outcome}</td>
                                                            <td className={`px-4 py-4 font-mono text-[11px] font-black ${trade.pnl_r >= 0 ? "text-emerald-600 dark:text-[#00ffa3]" : "text-red-600 dark:text-[#ff2e2e]"}`}>{trade.pnl_r >= 0 ? "+" : ""}{trade.pnl_r.toFixed(2)}R</td>
                                                            <td className={`px-4 py-4 font-mono text-[11px] text-right font-black ${trade.pnl_usd >= 0 ? "text-emerald-600 dark:text-[#00ffa3]" : "text-red-600 dark:text-[#ff2e2e]"}`}>
                                                                {trade.pnl_usd >= 0 ? "+" : ""}${formatCurrency(trade.pnl_usd)}
                                                            </td>
                                                        </tr>
                                                    ))}
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>

                                    {displayBootstrap && (
                                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 dark:bg-[#050505] bg-white rounded-3xl p-6 border dark:border-white/10 border-zinc-200 shadow-lg">
                                            <div>
                                                <p className="text-[10px] font-black uppercase tracking-[0.3em] dark:text-white/40 text-zinc-500 mb-3">Expected Profit Range</p>
                                                <p className="text-2xl font-black font-mono text-emerald-600 dark:text-[#00ffa3]">
                                                    ${displayBootstrap.net_profit_95_ci[0].toLocaleString(undefined, { maximumFractionDigits: 0 })}
                                                    <span className="dark:text-white/20 text-zinc-300 mx-3 font-normal">—</span>
                                                    ${displayBootstrap.net_profit_95_ci[1].toLocaleString(undefined, { maximumFractionDigits: 0 })}
                                                </p>
                                            </div>
                                            <div>
                                                <p className="text-[10px] font-black uppercase tracking-[0.3em] dark:text-white/40 text-zinc-500 mb-3">Mechanical Tail Risk</p>
                                                <p className="text-2xl font-black font-mono text-red-600 dark:text-[#ff2e2e]">
                                                    MAX {displayBootstrap.max_drawdown_95_ci_pct[1].toFixed(2)}%
                                                </p>
                                            </div>
                                        </div>
                                    )}

                                    {(ivData || ivLoading) && (
                                        <div className="space-y-6">
                                            {ivLoading && (
                                                <div className="dark:bg-[#050505] bg-white rounded-[2rem] border dark:border-white/10 border-zinc-200 p-8 flex items-center justify-center gap-4 shadow-lg relative overflow-hidden">
                                                    <div className="absolute inset-0 bg-gradient-to-r from-transparent via-black/[0.01] dark:via-white/[0.02] to-transparent animate-pulse" />
                                                    <div className="h-5 w-5 border-3 border-accent border-t-transparent rounded-full animate-spin" />
                                                    <span className="text-[11px] font-black uppercase tracking-[0.4em] dark:text-white/40 text-zinc-500 animate-pulse">Core Engine: Constructing IV Surface Audit…</span>
                                                </div>
                                            )}
                                            {ivData && <IvSmilePanel data={ivData} />}
                                        </div>
                                    )}

                                    {/* ARCH / GARCH Volatility Audit */}
                                    {(archData || archLoading) && (
                                        <div className="dark:bg-[#050505] bg-white rounded-3xl border dark:border-white/10 border-zinc-200 p-8 shadow-lg space-y-6">
                                            {archLoading ? (
                                                <div className="flex items-center justify-center py-12 gap-4">
                                                    <Loader2 className="animate-spin text-accent" size={24} />
                                                    <span className="text-[11px] font-black uppercase tracking-[0.4em] dark:text-white/30 text-zinc-500 animate-pulse">Fitting GARCH(1,1) Mechanical Model…</span>
                                                </div>
                                            ) : archData ? (
                                                <ArchVolPanel data={archData} />
                                            ) : null}
                                        </div>
                                    )}

                                    {/* Kalman Filter State Estimation */}
                                    {(kalmanData || kalmanLoading) && (
                                        <div className="dark:bg-[#050505] bg-white rounded-3xl border dark:border-white/10 border-zinc-200 p-8 shadow-lg space-y-6">
                                            {kalmanLoading ? (
                                                <div className="flex items-center justify-center py-12 gap-4">
                                                    <Loader2 className="animate-spin text-accent" size={24} />
                                                    <span className="text-[11px] font-black uppercase tracking-[0.4em] dark:text-white/30 text-zinc-500 animate-pulse">Running Kalman State Audit…</span>
                                                </div>
                                            ) : kalmanData ? (
                                                <KalmanFilterPanel data={kalmanData} />
                                            ) : null}
                                        </div>
                                    )}

                                    {/* IV Regime Current Signal Audit */}
                                    {ivCurrentSignal && (
                                        <div className="bg-card/40 backdrop-blur-md rounded-[2.5rem] p-10 border border-border shadow-sm relative overflow-hidden">
                                            <div className="absolute top-0 right-0 p-8">
                                                <div className={`px-5 py-2 rounded-full border text-[10px] font-black uppercase tracking-[0.3em] shadow-lg ${ivCurrentSignal.direction === "LONG" ? "text-emerald-500 border-emerald-500/20 bg-emerald-500/5" : ivCurrentSignal.direction === "SHORT" ? "text-destructive border-destructive/20 bg-destructive/5" : "text-muted-foreground border-border"}`}>
                                                    {ivCurrentSignal.direction} SIGNAL
                                                </div>
                                            </div>

                                            <div className="flex items-center gap-6 mb-10 pb-8 border-b dark:border-white/5 border-zinc-200">
                                                <div className="h-16 w-16 rounded-[1.5rem] bg-accent/10 border border-accent/20 flex items-center justify-center">
                                                    <Activity className="text-accent" size={32} />
                                                </div>
                                                <div>
                                                    <h3 className="text-xl font-black uppercase tracking-[0.4em] dark:text-white text-zinc-900">Execution Feedback</h3>
                                                    <p className="text-[10px] font-bold dark:text-white/20 text-zinc-400 mt-1 uppercase tracking-widest">Mechanical Signal Drift • {ivCurrentSignal.date}</p>
                                                </div>
                                            </div>

                                            <div className="grid grid-cols-2 lg:grid-cols-4 gap-8">
                                                {[
                                                    { label: "Close_Snapshot", val: `$${formatCurrency(ivCurrentSignal.close)}`, sub: "Price Level", color: "text-foreground" },
                                                    { label: "IV_Rank_Index", val: ivCurrentSignal.iv_rank.toFixed(1), sub: "Volatility Decile", color: "text-amber-500" },
                                                    { label: "Equity_Momentum", val: `${ivCurrentSignal.momentum_pct > 0 ? "+" : ""}${ivCurrentSignal.momentum_pct.toFixed(2)}%`, sub: "Trend Magnitude", color: ivCurrentSignal.momentum_pct >= 0 ? "text-emerald-500" : "text-destructive" },
                                                    { label: "System_Regime", val: ivCurrentSignal.regime, sub: "Market Context", color: "text-cyan-500" }
                                                ].map((item, i) => (
                                                    <div key={i} className="space-y-2">
                                                        <p className="text-[9px] font-black uppercase tracking-[0.3em] text-muted-foreground">{item.label}</p>
                                                        <p className={`text-2xl font-black font-mono tracking-tighter ${item.color}`}>{item.val}</p>
                                                        <p className="text-[9px] font-bold text-muted-foreground/40 uppercase tracking-widest">{item.sub}</p>
                                                    </div>
                                                ))}
                                            </div>

                                            {ivCurrentSignal.option_context && (
                                                <div className="mt-12 pt-8 border-t dark:border-white/5 border-zinc-200">
                                                    <div className="flex items-center justify-between mb-6">
                                                        <p className="text-[10px] font-black uppercase tracking-[0.4em] dark:text-white/50 text-zinc-500">Market Liquidity Audit</p>
                                                        <p className="text-[9px] font-bold text-accent/60 uppercase tracking-widest">Source: {ivCurrentSignal.option_context.source}</p>
                                                    </div>
                                                    <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
                                                        {ivCurrentSignal.option_context.iv_realized_ratio != null && (
                                                            <div className="dark:bg-white/5 bg-zinc-50 rounded-2xl p-4 border dark:border-white/5 border-zinc-200">
                                                                <p className="text-[9px] font-black uppercase tracking-widest dark:text-white/30 text-zinc-400 mb-1">IV/RV Ratio</p>
                                                                <p className="text-base font-black font-mono text-emerald-500">{ivCurrentSignal.option_context.iv_realized_ratio.toFixed(2)}x</p>
                                                            </div>
                                                        )}
                                                        {ivCurrentSignal.option_context.skew_pct != null && (
                                                            <div className="dark:bg-white/5 bg-zinc-50 rounded-2xl p-4 border dark:border-white/5 border-zinc-200">
                                                                <p className="text-[9px] font-black uppercase tracking-widest dark:text-white/30 text-zinc-400 mb-1">Skew Factor</p>
                                                                <p className={`text-base font-black font-mono ${ivCurrentSignal.option_context.skew_pct >= 0 ? "text-destructive" : "text-emerald-500"}`}>
                                                                    {ivCurrentSignal.option_context.skew_pct >= 0 ? "+" : ""}{ivCurrentSignal.option_context.skew_pct.toFixed(2)}pts
                                                                </p>
                                                            </div>
                                                        )}
                                                        {ivCurrentSignal.option_context.exp_date && (
                                                            <div className="dark:bg-white/5 bg-zinc-50 rounded-2xl p-4 border dark:border-white/5 border-zinc-200">
                                                                <p className="text-[9px] font-black uppercase tracking-widest dark:text-white/30 text-zinc-400 mb-1">Audit Expiry</p>
                                                                <p className="text-base font-black font-mono dark:text-white/80 text-zinc-700">{ivCurrentSignal.option_context.exp_date}</p>
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
                                                className="inline-flex items-center gap-4 px-8 py-4 bg-emerald-500 text-black font-black uppercase tracking-[0.3em] rounded-2xl transition-all shadow-[0_0_40px_rgba(16,185,129,0.4)] hover:scale-[1.05] group"
                                            >
                                                <Download size={20} />
                                                Export mechanical audit pdf
                                                <ExternalLinkIcon size={16} className="text-black/40 group-hover:text-black" />
                                            </a>
                                        ) : (
                                            <div className="text-[10px] font-bold dark:text-white/20 text-zinc-400 uppercase tracking-[0.2em] dark:bg-white/5 bg-zinc-100 px-6 py-4 rounded-2xl border dark:border-white/5 border-zinc-200">
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