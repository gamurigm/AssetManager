import {
    Area,
    AreaChart,
    CartesianGrid,
    ResponsiveContainer,
    Tooltip,
    XAxis,
    YAxis,
} from "recharts";
import { ArchVolData } from "./types";

export function ArchVolPanel({ data }: { data: ArchVolData }) {
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
        <div className="bg-card/40 backdrop-blur-md rounded-3xl border border-border p-6 shadow-sm">
            <div className="flex flex-wrap items-center justify-between gap-3 mb-6">
                <div>
                    <h3 className="text-[10px] font-black uppercase tracking-[0.3em] text-foreground/80">{data.model} Dynamic Volatility — {data.symbol}</h3>
                    <p className="text-[9px] font-bold text-muted-foreground/60 mt-1 uppercase tracking-widest">
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
                                <stop offset="5%" stopColor="#10b981" stopOpacity={0.2} />
                                <stop offset="95%" stopColor="#10b981" stopOpacity={0} />
                            </linearGradient>
                        </defs>
                        <CartesianGrid strokeDasharray="3 3" stroke="hsla(var(--border), 0.5)" />
                        <XAxis dataKey="date" tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 9 }} tickLine={false} axisLine={false}
                            tickFormatter={(v: string) => v.substring(5)} interval="preserveStartEnd" />
                        <YAxis tick={{ fill: "hsla(var(--muted-foreground))", fontSize: 9 }} tickLine={false} axisLine={false}
                            tickFormatter={(v: number) => `${v.toFixed(0)}%`} />
                        <Tooltip
                            contentStyle={{ background: "var(--color-card)", border: "1px solid var(--color-border)", borderRadius: 8, fontSize: 11 }}
                            formatter={(value: number | string | undefined) => [`${Number(value ?? 0).toFixed(2)}%`, "Ann. Vol σ"]}
                            labelFormatter={(label) => `Date: ${String(label ?? "")}`}
                            content={({ active, payload }) => {
                                if (!active || !payload?.length) return null;
                                const d = payload[0].payload;
                                return (
                                    <div className="bg-card border border-border rounded-xl px-4 py-3 text-[10px] font-black uppercase tracking-widest shadow-2xl space-y-2">
                                        <p className="text-foreground border-b border-border/50 pb-2 mb-2">{d.date}</p>
                                        <p className="text-emerald-500">ANN VOL: {d.sigma_ann_pct.toFixed(2)}%</p>
                                        <p className="text-muted-foreground">DAILY σ: {d.sigma_pct.toFixed(2)}%</p>
                                        <p className={d.ret_pct >= 0 ? "text-emerald-500" : "text-destructive"}>RETURN: {d.ret_pct.toFixed(2)}%</p>
                                    </div>
                                );
                            }}
                        />
                        <Area type="monotone" dataKey="sigma_ann_pct" stroke="#10b981" strokeWidth={3} fill="url(#volGradient)" isAnimationActive={false} />
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
