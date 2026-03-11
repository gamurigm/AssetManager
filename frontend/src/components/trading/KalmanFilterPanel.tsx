import {
    CartesianGrid,
    ComposedChart,
    Line,
    ResponsiveContainer,
    Tooltip,
    XAxis,
    YAxis,
} from "recharts";
import { KalmanFilterData } from "./types";

export function KalmanFilterPanel({ data }: { data: KalmanFilterData }) {
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
        <div className="bg-card/40 backdrop-blur-md rounded-3xl border border-border p-6 shadow-sm">
            <div className="flex flex-wrap items-center justify-between gap-3 mb-6">
                <div>
                    <h3 className="text-[10px] font-black uppercase tracking-[0.3em] text-foreground/80">Kalman State Filter — {data.symbol}</h3>
                    <p className="text-[9px] font-bold text-muted-foreground/60 mt-1 uppercase tracking-widest">
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
                        <CartesianGrid strokeDasharray="3 3" stroke="hsla(var(--border), 0.5)" />
                        <XAxis
                            dataKey="date"
                            tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 9 }}
                            tickLine={false}
                            axisLine={false}
                            tickFormatter={(v: string) => v.substring(5)}
                            interval="preserveStartEnd"
                        />
                        <YAxis
                            tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 9 }}
                            tickLine={false}
                            axisLine={false}
                            tickFormatter={(v: number) => `$${Number(v).toFixed(0)}`}
                            width={50}
                        />
                        <Tooltip
                            contentStyle={{ background: "var(--color-card)", border: "1px solid var(--color-border)", borderRadius: 8, fontSize: 11 }}
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
