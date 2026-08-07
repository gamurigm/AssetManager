import { useEffect, useState } from "react";
import {
    CartesianGrid,
    ComposedChart,
    Line,
    ReferenceArea,
    ResponsiveContainer,
    Tooltip,
    XAxis,
    YAxis,
} from "recharts";
import { LiveTrade, RegimeData } from "./types";
import { buildRegimeRuns, REGIME_FILL } from "./utils";
import { getCachedOHLCV, setCachedOHLCV, getCachedRegime, setCachedRegime } from "./analyticsCache";
import { cachedFetch } from "@/lib/cachedFetch";

const API_BASE = "http://127.0.0.1:8282";

function mergeHistWithTrades(hist: any[], trades: LiveTrade[]) {
    const closes = hist.map((c: any) => c.close as number);
    const toDate = (ts: string | undefined) => ts ? ts.substring(0, 10) : "";

    return hist.map((c: any, i: number) => {
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
}

export function BacktestPriceChart({
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

    // ── fetch OHLCV (with cache) ─────────────────────────────────────────────
    useEffect(() => {
        if (!symbol || !startDate || !endDate || trades.length === 0) return;

        const cachedHist = getCachedOHLCV(symbol);
        if (cachedHist) {
            const hist = cachedHist
                .filter((c: any) => c.date >= startDate && c.date <= endDate)
                .sort((a: any, b: any) => a.date.localeCompare(b.date));
            if (hist.length > 0) {
                setChartData(mergeHistWithTrades(hist, trades));
                return;
            }
        }

        setLoading(true);
        let isMounted = true;
        cachedFetch(`${API_BASE}/api/v1/market/historical/${symbol}?limit=600`)
            .then(res => res.json())
            .then(d => {
                if (!isMounted) return;
                const raw = d.historical ?? [];
                if (raw.length > 0) setCachedOHLCV(symbol, raw);

                const hist = raw
                    .filter((c: any) => c.date >= startDate && c.date <= endDate)
                    .sort((a: any, b: any) => a.date.localeCompare(b.date));

                if (hist.length === 0) {
                    console.warn(`[BacktestPriceChart] No OHLC data for ${symbol} between ${startDate} and ${endDate}`);
                    setLoading(false);
                    return;
                }

                setChartData(mergeHistWithTrades(hist, trades));
            })
            .catch(err => {
                if (!isMounted) return;
                console.error("[BacktestPriceChart] Fetch error:", err);
            })
            .finally(() => {
                if (isMounted) setLoading(false);
            });

        return () => { isMounted = false; };
    }, [symbol, startDate, endDate, trades.length]);

    // ── fetch volatility regimes (with cache) ────────────────────────────────
    useEffect(() => {
        if (!symbol) return;
        const cached = getCachedRegime(symbol); 
        if (cached) {
            setRegimeData(cached);
            return;
        }
        let isMounted = true;
        cachedFetch(`${API_BASE}/api/v1/analytics/volatility-regimes/${symbol}?days=600&window=20`)
            .then(r => r.ok ? r.json() : null)
            .then((d: RegimeData) => {
                if (!isMounted) return;
                setCachedRegime(symbol, d); 
                setRegimeData(d);
            })
            .catch(() => {/* regime overlay is optional – silently skip */ });

        return () => { isMounted = false; };
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
        const fill = won ? "#10b981" : "#ef4444"; 
        return isLong
            ? <polygon key={payload._entryId} points={`${cx},${cy - 10} ${cx - 6},${cy + 2} ${cx + 6},${cy + 2}`} fill={fill} stroke="var(--color-background)" strokeWidth={0.8} opacity={0.95} />
            : <polygon key={payload._entryId} points={`${cx},${cy + 10} ${cx - 6},${cy - 2} ${cx + 6},${cy - 2}`} fill={fill} stroke="var(--color-background)" strokeWidth={0.8} opacity={0.95} />;
    };

    const ExitDot = (props: any) => {
        const { cx, cy, payload } = props;
        if (!payload || payload.exitPrice == null || cx == null || cy == null) return null;
        const won = payload._exitOutcome === "win_tp";
        const fill = won ? "#10b981" : "#ef4444"; 
        return <rect key={payload._entryId + "_exit"} x={cx - 4} y={cy - 4} width={8} height={8} fill={fill} stroke="var(--color-background)" strokeWidth={0.8} opacity={0.9} />;
    };

    return (
        <div className="bg-card/40 backdrop-blur-md rounded-3xl border border-border p-6 shadow-sm overflow-hidden min-h-[420px]">
            <div className="flex items-center justify-between mb-8 pb-6 border-b border-border/50">
                <div>
                    <h3 className="text-[10px] font-black uppercase tracking-[0.3em] text-foreground/80">Mechanical Precision Audit — {symbol}</h3>
                    <p className="text-[9px] font-bold text-muted-foreground/60 mt-1 uppercase tracking-widest">
                        Daily close propagation · SMA(20) baseline · Signal Magnitude Analysis
                    </p>
                </div>
                <div className="flex items-center gap-4">
                    <div className="flex items-center gap-2 text-[9px] font-black uppercase tracking-widest">
                        <span className="h-2 w-2 rounded-full bg-emerald-500 shadow-[0_0_8px_rgba(16,185,129,0.5)]" />
                        <span className="text-muted-foreground">Long Entry</span>
                    </div>
                    <div className="flex items-center gap-2 text-[9px] font-black uppercase tracking-widest">
                        <span className="h-2 w-2 rounded-full bg-destructive shadow-[0_0_8px_rgba(239,68,68,0.5)]" />
                        <span className="text-muted-foreground">Short Entry</span>
                    </div>
                </div>
            </div>

            <div className="h-80">
                <ResponsiveContainer width="100%" height="100%">
                    <ComposedChart data={chartData} margin={{ top: 10, right: 10, bottom: 0, left: 0 }}>
                        <CartesianGrid strokeDasharray="3 3" stroke="hsla(var(--border), 0.5)" vertical={false} />
                        <XAxis
                            dataKey="label"
                            tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 9 }}
                            minTickGap={40}
                            axisLine={false}
                            tickLine={false}
                        />
                        <YAxis
                            tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 9 }}
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
                                    <div className="bg-card border border-border rounded-xl px-4 py-3 text-[10px] font-black uppercase tracking-widest shadow-2xl space-y-2">
                                        <p className="border-b border-border/50 pb-2 mb-2 text-foreground">{d.label}</p>
                                        <p className="text-muted-foreground">CLOSE: <span className="text-foreground">${d.close.toFixed(2)}</span></p>
                                        <p className="text-muted-foreground">SMA20: <span className="text-muted-foreground/80">${d.sma20.toFixed(2)}</span></p>
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
                        <Line type="monotone" dataKey="close" stroke="var(--color-primary)" strokeOpacity={0.4} strokeWidth={1} dot={false} isAnimationActive={false} />
                        <Line type="monotone" dataKey="sma20" stroke="var(--color-primary)" strokeOpacity={0.2} strokeWidth={1} strokeDasharray="3 3" dot={false} isAnimationActive={false} />
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
                                <p className="text-[10px] text-muted-foreground/80 font-mono">
                                    μ {d.annualized_ret_pct > 0 ? "+" : ""}{d.annualized_ret_pct.toFixed(1)}% / yr
                                </p>
                                <p className="text-[10px] text-muted-foreground/80 font-mono">σ {d.annualized_vol_pct.toFixed(1)}% ann.</p>
                                <p className="text-[10px] text-muted-foreground/80 font-mono">Sharpe {d.sharpe.toFixed(2)}</p>
                                <p className="text-[10px] text-muted-foreground/50 font-mono">{d.count} days</p>
                            </div>
                        );
                    })}
                </div>
            )}
        </div>
    );
}
