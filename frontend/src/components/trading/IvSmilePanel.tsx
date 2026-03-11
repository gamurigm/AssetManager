import { useState } from "react";
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
import { IvSmileData } from "./types";

export function IvSmilePanel({ data }: { data: IvSmileData }) {
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
        <div className="bg-card/40 backdrop-blur-md rounded-3xl border border-border p-6 shadow-sm">
            {/* Header */}
            <div className="flex flex-wrap items-center justify-between gap-3 mb-6">
                <div>
                    <p className="text-[10px] font-black uppercase tracking-[0.3em] text-foreground/80">Implied Volatility Smile — {data.symbol}</p>
                    <p className="text-[9px] font-bold text-muted-foreground/60 mt-1 uppercase tracking-widest">Black-Scholes inversion · σ(K) curve · spot ${data.spot.toFixed(2)}</p>
                </div>
                <div className="flex items-center gap-3">
                    {exp.atm_iv != null && (
                        <div className="px-3 py-1.5 rounded-xl bg-accent/10 border border-accent/30 text-[10px] font-black uppercase tracking-widest text-accent">
                            ATM IV {exp.atm_iv.toFixed(1)}%
                        </div>
                    )}
                    <select
                        value={selectedIdx}
                        onChange={e => setSelectedIdx(Number(e.target.value))}
                        className="bg-background border border-border rounded-xl px-3 py-2 text-[10px] font-black uppercase tracking-widest focus:outline-none focus:ring-1 focus:ring-emerald-500/30 text-muted-foreground"
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
            <div className="flex items-center gap-5 mb-5 text-[9px] font-bold text-muted-foreground/50 uppercase tracking-[0.15em]">
                <span className="flex items-center gap-2"><span className="inline-block w-3 h-3 rounded-sm bg-emerald-500/20 border border-emerald-500/40" /> IV Calls</span>
                <span className="flex items-center gap-2"><span className="inline-block w-3 h-3 rounded-sm bg-amber-500/20 border border-amber-500/40" /> IV Puts</span>
                <span className="flex items-center gap-1.5 ml-2 text-border">|</span>
                <span className="flex items-center gap-1.5 text-foreground/80">Spot ≈ ${data.spot.toFixed(0)}</span>
                <span className="flex items-center gap-1.5 font-black text-emerald-500">r = {(data.rf * 100).toFixed(1)}%</span>
            </div>

            {/* Chart */}
            <div className="h-64">
                <ResponsiveContainer width="100%" height="100%">
                    <ComposedChart data={chartData} margin={{ top: 10, right: 10, bottom: 0, left: 0 }}>
                        <CartesianGrid strokeDasharray="3 3" stroke="hsla(var(--border), 0.5)" />
                        <XAxis
                            dataKey="label"
                            tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 9 }}
                            minTickGap={28}
                        />
                        <YAxis
                            tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 9 }}
                            tickFormatter={v => `${Number(v).toFixed(0)}%`}
                            width={42}
                            domain={[0, "auto"]}
                        />
                        <Tooltip
                            content={({ active, payload, label }) => {
                                if (!active || !payload?.length) return null;
                                const d: any = payload[0]?.payload;
                                return (
                                    <div className="bg-card border border-border rounded-xl px-4 py-3 text-[10px] font-black uppercase tracking-widest shadow-2xl space-y-2">
                                        <p className="text-foreground border-b border-border/50 pb-2 mb-2">{label}</p>
                                        <p className="text-muted-foreground">Moneyness: {d.moneyness > 0 ? "+" : ""}{d.moneyness?.toFixed(1)}%</p>
                                        {d.callIv != null && <p className="text-emerald-500">CALL IV: {d.callIv.toFixed(1)}%  ·  ${d.callPrice?.toFixed(2)}</p>}
                                        {d.putIv != null && <p className="text-amber-500">PUT  IV: {d.putIv.toFixed(1)}%  ·  ${d.putPrice?.toFixed(2)}</p>}
                                    </div>
                                );
                            }}
                        />
                        {/* Spot reference */}
                        <ReferenceArea
                            x1={`$${Math.floor(data.spot)}`}
                            x2={`$${Math.ceil(data.spot)}`}
                            fill="rgba(99,102,241,0.05)"
                            stroke="rgba(99,102,241,0.2)"
                            strokeWidth={1}
                        />
                        <Line type="monotone" dataKey="callIv" name="CALL IV" stroke="#10b981" strokeWidth={3} dot={false} connectNulls isAnimationActive={false} />
                        <Line type="monotone" dataKey="putIv" name="PUT IV" stroke="#f59e0b" strokeWidth={2} strokeDasharray="5 5" dot={false} connectNulls isAnimationActive={false} />
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
