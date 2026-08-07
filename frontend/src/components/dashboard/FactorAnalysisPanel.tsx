"use client";

import React, { useEffect, useState, useMemo } from "react";
import {
    ScatterChart, Scatter, XAxis, YAxis, ZAxis, Tooltip,
    ResponsiveContainer, ComposedChart, Bar, Line,
    CartesianGrid, ReferenceLine, Legend,
} from "recharts";
import { Maximize2, X, Info, BrainCircuit } from "lucide-react";
import { cachedFetch } from "@/lib/cachedFetch";

// ─── Types ──────────────────────────────────────────────────────────
interface AssetMetric {
    ticker: string;
    beta: number;
    alpha_daily: number;
    expected_return_pct: number;
    idiosyncratic_risk_pct: number;
    systematic_risk_pct: number;
    total_volatility_pct: number;
    scatter: { x: number; y: number }[];
    fit_line: { x: number; y: number }[];
}

interface SectorCorrelation {
    ticker: string;
    sector_etf: string;
    sector_name: string;
    industry_group: string;
    industry: string;
    sub_industry: string;
    correlation: number | null;
    r_squared: number | null;
}

interface PCAData {
    eigenvalues: number[];
    explained_variance_pct: number[];
    cumulative_variance_pct: number[];
    components_labels: string[];
}

interface FactorData {
    tickers: string[];
    benchmark: string;
    lookback_days: number;
    asset_metrics: AssetMetric[];
    sector_correlations: SectorCorrelation[];
    correlation_matrix: Record<string, any>[];
    pca: PCAData;
}

const ACCENT_COLOR = "#22d3ee";
const COLORS = ["#22d3ee", "#a78bfa", "#34d399", "#f59e0b", "#f87171", "#60a5fa", "#e879f9", "#4ade80"];

const CHART_DETAILS = {
    capm: {
        id: "capm",
        title: "CAPM Regression & Sensitivity",
        subtitle: "Asset Returns vs. Market Benchmark",
        explanation: "Este gráfico muestra la regresión lineal entre los retornos diarios del activo y el índice de referencia (SPY). La pendiente de la línea roja representa el Beta (β), que mide la sensibilidad del activo al riesgo de mercado. El intercepto representa el Alpha (α) diario, indicando el retorno excedente generado por encima de lo que el riesgo de mercado justificaría.",
        math: "R_i - R_f = α + β(R_m - R_f) + ε"
    },
    pca: {
        id: "pca",
        title: "PCA Scree Projection",
        subtitle: "Variance Decomposition by Eigenvalues",
        explanation: "El Análisis de Componentes Principales (PCA) descompone los movimientos de la cartera en factores comunes. El primer componente (PC1) suele representar el riesgo sistémico del mercado. Si el PC1 explica una gran parte de la varianza (>60%), significa que sus activos están altamente acoplados y diversificar es más difícil.",
        math: "Matrix Covariance (Σ) → eigenvectors (W) + eigenvalues (Λ)"
    },
    correlation: {
        id: "correlation",
        title: "Correlation Matrix Dynamics",
        subtitle: "Cross-Asset Synergy Assessment",
        explanation: "Mide el coeficiente de correlación de Pearson (ρ) entre todos los pares de activos. Un valor de 1.0 (Esmeralda) significa movimiento idéntico, mientras que valores cercanos a 0 o negativos (Rojo) indican desvinculación o cobertura. Una cartera robusta busca activos con baja correlación para optimizar la frontera eficiente.",
        math: "ρ(X,Y) = Cov(X,Y) / (σ_X * σ_Y)"
    },
    riskReturn: {
        id: "riskReturn",
        title: "Efficient Frontier Projection",
        subtitle: "Beta vs. Expected Return Framework",
        explanation: "Este scatter plot posiciona cada activo según su riesgo sistémico (Beta) y su retorno esperado según el modelo CAPM. El tamaño de la burbuja refleja el riesgo idiosincrásico (volatilidad no explicada por el mercado). Los activos situados excesivamente a la derecha tienen alta exposición a eventos sistémicos.",
        math: "E[R_i] = R_f + β_i(E[R_m] - R_f)"
    }
};

// ─── Reusable panel header ────────────────────────────────────────────
function ChartHeader({ title, subtitle, onExpand }: { title: string; subtitle: string; onExpand: () => void }) {
    return (
        <div className="flex items-start justify-between mb-4">
            <div>
                <h3 className="text-[10px] font-black uppercase tracking-[0.25em] text-cyan-100/90">{title}</h3>
                <p className="text-[9px] text-muted/60 mt-0.5 font-mono uppercase tracking-wider">{subtitle}</p>
            </div>
            <button
                onClick={(e) => { e.stopPropagation(); onExpand(); }}
                className="p-1.5 rounded-lg bg-white/5 hover:bg-accent/20 text-muted/60 hover:text-accent transition-all group"
                title="Zoom & Details"
            >
                <Maximize2 size={12} className="group-hover:scale-110 transition-transform" />
            </button>
        </div>
    );
}

// ─── Custom Scatter Tooltip ───────────────────────────────────────────
const ScatterTip = ({ active, payload }: any) => {
    if (!active || !payload?.length) return null;
    const d = payload[0]?.payload;
    return (
        <div className="bg-card border border-border rounded-lg px-3 py-2 text-[10px] font-mono shadow-xl bg-background/80 backdrop-blur-md">
            <p>Market: <span className="text-accent">{d?.x?.toFixed(4)}</span></p>
            <p>Asset:  <span className="text-emerald-400">{d?.y?.toFixed(4)}</span></p>
        </div>
    );
};

// ─── Main Component ──────────────────────────────────────────────────
export default function FactorAnalysisPanel({
    tickers,
}: {
    tickers: string[];
}) {
    const [data, setData] = useState<FactorData | null>(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [selectedTicker, setSelectedTicker] = useState<string | null>(null);
    const [focusedChart, setFocusedChart] = useState<string | null>(null);

    const tickerStr = tickers.slice(0, 12).join(",");

    useEffect(() => {
        if (!tickerStr) return;
        setLoading(true);
        setError(null);
        cachedFetch(`http://127.0.0.1:8282/api/v1/analytics/factor-analysis?tickers=${tickerStr}&benchmark=SPY&days=252`)
            .then(r => r.ok ? r.json() : r.json().then(e => Promise.reject(e.detail)))
            .then(d => { setData(d); setSelectedTicker(d.tickers[0] ?? null); })
            .catch(e => setError(typeof e === "string" ? e : "Analysis failed"))
            .finally(() => setLoading(false));
    }, [tickerStr]);

    const screeData = useMemo(() => {
        if (!data) return [];
        return data.pca.components_labels.map((label, i) => ({
            name: label,
            explained: data.pca.explained_variance_pct[i],
            cumulative: data.pca.cumulative_variance_pct[i],
        }));
    }, [data]);

    const bubbleData = useMemo(() => {
        if (!data) return [];
        return data.asset_metrics.map(m => ({
            name: m.ticker,
            beta: m.beta,
            expected_return: m.expected_return_pct,
            idio_risk: m.idiosyncratic_risk_pct,
            total_vol: m.total_volatility_pct,
        }));
    }, [data]);

    const activeMeta = useMemo(() => data?.asset_metrics.find(m => m.ticker === selectedTicker), [data, selectedTicker]);

    if (loading) {
        return (
            <div className="flex items-center justify-center py-16 gap-3">
                <div className="h-5 w-5 border-2 border-accent border-t-transparent rounded-full animate-spin" />
                <span className="text-[10px] font-mono uppercase tracking-widest text-muted animate-pulse">Running Factor Analysis…</span>
            </div>
        );
    }

    if (error) {
        return (
            <div className="flex items-center justify-center py-10">
                <span className="text-[11px] text-red-400 font-mono bg-red-900/20 px-4 py-2 rounded-lg border border-red-500/20">⚠ {error}</span>
            </div>
        );
    }

    if (!data) return null;

    const renderChart = (type: string, height: number = 240, isExpanded: boolean = false) => {
        const textClass = isExpanded ? "text-sm" : "text-[9px]";
        const cellPadding = isExpanded ? "p-4" : "p-1";

        switch (type) {
            case 'capm':
                return (
                    <ResponsiveContainer width="100%" height={height}>
                        <ScatterChart margin={isExpanded ? { top: 20, right: 40, bottom: 40, left: 20 } : { top: 4, right: 8, bottom: 4, left: 0 }}>
                            <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
                            <XAxis dataKey="x" type="number" name={data.benchmark} tick={{ fontSize: isExpanded ? 12 : 8, fill: "#9ca3af" }} tickFormatter={v => `${(v * 100).toFixed(1)}%`} label={isExpanded ? { value: data.benchmark, position: 'insideBottom', offset: -20, fill: '#6b7280', fontSize: 12 } : undefined} />
                            <YAxis dataKey="y" type="number" name={selectedTicker ?? ""} tick={{ fontSize: isExpanded ? 12 : 8, fill: "#9ca3af" }} tickFormatter={v => `${(v * 100).toFixed(1)}%`} label={isExpanded ? { value: selectedTicker ?? "", angle: -90, position: 'insideLeft', fill: '#6b7280', fontSize: 12 } : undefined} />
                            <Tooltip content={<ScatterTip />} />
                            <ReferenceLine x={0} stroke="rgba(255,255,255,0.15)" />
                            <ReferenceLine y={0} stroke="rgba(255,255,255,0.15)" />
                            <Scatter name="Daily Returns" data={activeMeta?.scatter ?? []} fill={ACCENT_COLOR} fillOpacity={0.4} r={isExpanded ? 4 : 2} />
                            <Scatter name="CAPM Fit" data={activeMeta?.fit_line ?? []} fill="#f87171" line={{ stroke: "#f87171", strokeWidth: 3 }} r={0} />
                        </ScatterChart>
                    </ResponsiveContainer>
                );
            case 'pca':
                return (
                    <ResponsiveContainer width="100%" height={height}>
                        <ComposedChart data={screeData} margin={isExpanded ? { top: 20, right: 40, bottom: 40, left: 20 } : { top: 4, right: 24, bottom: 4, left: 0 }}>
                            <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
                            <XAxis dataKey="name" tick={{ fontSize: isExpanded ? 12 : 8, fill: "#9ca3af" }} />
                            <YAxis yAxisId="left" tick={{ fontSize: isExpanded ? 12 : 8, fill: "#9ca3af" }} domain={[0, 100]} tickFormatter={v => `${v}%`} />
                            <YAxis yAxisId="right" orientation="right" tick={{ fontSize: isExpanded ? 12 : 8, fill: "#9ca3af" }} domain={[0, 100]} tickFormatter={v => `${v}%`} />
                            <Tooltip formatter={(v: any) => `${Number(v).toFixed(2)}%`} contentStyle={{ background: "#1a1b1e", border: "1px solid rgba(255,255,255,0.1)", fontSize: 12 }} />
                            <Legend wrapperStyle={{ fontSize: isExpanded ? 14 : 9, paddingTop: isExpanded ? 20 : 0 }} />
                            <Bar yAxisId="left" dataKey="explained" name="Variance %" fill={ACCENT_COLOR} fillOpacity={0.7} radius={[4, 4, 0, 0]} />
                            <Line yAxisId="right" dataKey="cumulative" name="Cumulative %" stroke="#a78bfa" strokeWidth={3} dot={{ r: isExpanded ? 5 : 3, fill: "#a78bfa" }} />
                        </ComposedChart>
                    </ResponsiveContainer>
                );
            case 'riskReturn':
                return (
                    <ResponsiveContainer width="100%" height={height}>
                        <ScatterChart margin={isExpanded ? { top: 20, right: 40, bottom: 40, left: 20 } : { top: 8, right: 16, bottom: 16, left: 0 }}>
                            <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
                            <XAxis dataKey="beta" type="number" name="Beta" tick={{ fontSize: isExpanded ? 12 : 8, fill: "#9ca3af" }} label={isExpanded ? { value: 'Beta (Sistémico)', position: 'insideBottom', offset: -20, fill: '#6b7280', fontSize: 12 } : undefined} />
                            <YAxis dataKey="expected_return" type="number" name="Exp. Return %" tick={{ fontSize: isExpanded ? 12 : 8, fill: "#9ca3af" }} tickFormatter={v => `${v.toFixed(0)}%`} label={isExpanded ? { value: 'Exp. Return %', angle: -90, position: 'insideLeft', fill: '#6b7280', fontSize: 12 } : undefined} />
                            <ZAxis dataKey="idio_risk" range={isExpanded ? [100, 1000] : [40, 400]} name="Idiosyncratic Risk" />
                            <ReferenceLine x={1} stroke="rgba(255,255,255,0.15)" strokeDasharray="4 4" />
                            <ReferenceLine y={0} stroke="rgba(255,255,255,0.15)" />
                            <Tooltip cursor={{ strokeDasharray: "3 3" }} content={({ active, payload }) => {
                                if (!active || !payload?.length) return null;
                                const d = payload[0]?.payload;
                                return (
                                    <div className="bg-card border border-border rounded-lg px-4 py-3 text-xs font-mono shadow-2xl space-y-1 bg-background/95 backdrop-blur-md">
                                        <p className="font-black text-accent text-sm pb-1 border-b border-border">{d.name}</p>
                                        <p>β = <span className="text-sky-300 font-bold">{d.beta?.toFixed(4)}</span></p>
                                        <p>CAPM Ret = <span className="text-emerald-300 font-bold">{d.expected_return?.toFixed(2)}%</span></p>
                                        <p>Idio Risk = <span className="text-amber-300 font-bold">{d.idio_risk?.toFixed(2)}%</span></p>
                                        <p>Total Vol = <span className="text-muted font-bold">{d.total_vol?.toFixed(2)}%</span></p>
                                    </div>
                                );
                            }} />
                            {bubbleData.map((d, i) => (
                                <Scatter key={d.name} name={d.name} data={[d]} fill={COLORS[i % COLORS.length]} fillOpacity={0.8} />
                            ))}
                        </ScatterChart>
                    </ResponsiveContainer>
                );
            case 'correlation':
                return (
                    <div className={`w-full h-full flex flex-col items-center justify-center ${isExpanded ? 'p-4' : 'mt-2'} overflow-auto`}>
                        <table className={`w-full max-w-5xl ${textClass} font-mono text-center border-collapse shadow-2xl`}>
                            <thead>
                                <tr>
                                    <th className={`${cellPadding} font-black text-muted/50 border-b border-white/10 bg-white/5`}>—</th>
                                    {data.tickers.map(ticker => <th key={ticker} className={`${cellPadding} font-black text-muted/80 border-b border-white/10 bg-white/5`}>{ticker}</th>)}
                                </tr>
                            </thead>
                            <tbody>
                                {data.correlation_matrix?.map(row => (
                                    <tr key={row.ticker} className="hover:bg-white/5 transition-colors">
                                        <td className={`${cellPadding} font-black text-muted/80 text-left border-r border-white/10 bg-white/5`}>{row.ticker}</td>
                                        {data.tickers.map(t2 => {
                                            const val = row[t2] as number;
                                            const isSelf = row.ticker === t2;
                                            const color = val > 0 ? `rgba(52, 211, 153, ${Math.abs(val) * 0.9})` : `rgba(248, 113, 113, ${Math.abs(val) * 0.9})`;
                                            return (
                                                <td key={t2} className={`${cellPadding} font-bold border border-white/10 transition-transform hover:scale-105 cursor-default`} style={{ background: isSelf ? "rgba(255,255,255,0.1)" : (val !== undefined ? color : "transparent"), color: isSelf ? "#9ca3af" : (Math.abs(val) > 0.4 ? "#000" : "#fff") }}>
                                                    {isSelf ? "1.00" : (val !== undefined ? val.toFixed(2) : "—")}
                                                </td>
                                            );
                                        })}
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                );
            default: return null;
        }
    };

    return (
        <div className="flex flex-col gap-6 p-5 relative">
            {/* ── Zoom Modal Overlay ── */}
            {focusedChart && (
                <div className="fixed inset-0 z-[100] flex items-center justify-center p-4 md:p-8 animate-in fade-in duration-300">
                    <div className="absolute inset-0 bg-background/80 backdrop-blur-xl" onClick={() => setFocusedChart(null)} />
                    <div className="relative bg-card border border-border rounded-[40px] w-full max-w-7xl h-[90vh] flex flex-col md:flex-row overflow-hidden shadow-[0_128px_256px_-32px_rgba(0,0,0,0.8)] animate-in zoom-in-95 duration-500">
                        {/* Modal Header (Mobile/Header) */}
                        <button onClick={() => setFocusedChart(null)} className="absolute top-6 right-6 z-20 h-10 w-10 flex items-center justify-center rounded-xl bg-background/50 border border-border text-muted hover:text-foreground transition-all hover:rotate-90">
                            <X size={20} />
                        </button>

                        {/* Chart Area - Expanded space */}
                        <div className="flex-[3] p-6 md:p-10 flex flex-col border-b md:border-b-0 md:border-r border-border bg-background/20 h-full overflow-hidden">
                            <div className="mb-6">
                                <h2 className="text-3xl font-black text-foreground mb-1">{(CHART_DETAILS as any)[focusedChart].title}</h2>
                                <p className="text-xs font-black text-accent uppercase tracking-[0.4em]">{(CHART_DETAILS as any)[focusedChart].subtitle}</p>
                            </div>
                            <div className="flex-1 w-full flex items-center justify-center bg-black/40 rounded-[32px] overflow-hidden border border-white/5 shadow-[inset_0_2px_20px_rgba(0,0,0,0.5)]">
                                {renderChart(focusedChart, 650, true)}
                            </div>
                        </div>

                        {/* Detail Area - More compact */}
                        <div className="flex-1 p-8 md:p-10 overflow-y-auto no-scrollbar bg-card/40 flex flex-col h-full">
                            <div className="space-y-10">
                                <div className="space-y-6">
                                    <div className="flex items-center gap-3 text-accent mb-2">
                                        <BrainCircuit size={20} />
                                        <span className="text-[11px] font-black uppercase tracking-[0.3em]">Quantitative Logic</span>
                                    </div>
                                    <p className="text-lg text-foreground/80 leading-relaxed font-serif">
                                        {(CHART_DETAILS as any)[focusedChart].explanation}
                                    </p>
                                </div>

                                <div className="space-y-6">
                                    <div className="flex items-center gap-3 text-muted">
                                        <Info size={16} />
                                        <span className="text-[11px] font-black uppercase tracking-[0.3em]">Model Formulation</span>
                                    </div>
                                    <div className="p-8 rounded-[32px] bg-background/80 border border-border shadow-inner group">
                                        <p className="text-xl font-mono text-center text-accent/90 break-all leading-relaxed tracking-wider group-hover:scale-105 transition-transform">
                                            {(CHART_DETAILS as any)[focusedChart].math}
                                        </p>
                                    </div>
                                </div>

                                <div className="p-8 rounded-[32px] bg-accent/5 border border-accent/20">
                                    <p className="text-xs text-muted-foreground leading-relaxed uppercase tracking-widest font-black opacity-60">
                                        Este modelo está basado en datos históricos de 252 días con una ventana de lookback adaptativa para capturar regímenes de mercado recientes.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* ── Table Summary ── */}
            <div className="overflow-x-auto">
                <table className="w-full text-[10px] font-mono">
                    <thead>
                        <tr className="border-b border-white/10 text-muted/70">
                            <th className="text-left py-2 pr-4 uppercase tracking-wider font-black">Asset</th>
                            <th className="text-right py-2 px-3 uppercase tracking-wider font-black">Beta (β)</th>
                            <th className="text-right py-2 px-3 uppercase tracking-wider font-black">α Daily</th>
                            <th className="text-right py-2 px-3 uppercase tracking-wider font-black">CAPM Ret%</th>
                            <th className="text-right py-2 px-3 uppercase tracking-wider font-black">Idio Risk%</th>
                            <th className="text-right py-2 px-3 uppercase tracking-wider font-black">Sys Risk%</th>
                            <th className="text-right py-2 pl-3 uppercase tracking-wider font-black">Tot Vol%</th>
                        </tr>
                    </thead>
                    <tbody>
                        {data.asset_metrics.map((m, i) => (
                            <tr key={m.ticker} onClick={() => setSelectedTicker(m.ticker)} className={`border-b border-white/5 cursor-pointer transition-colors hover:bg-white/5 ${selectedTicker === m.ticker ? "bg-accent/10" : ""}`}>
                                <td className="py-2 pr-4 font-black" style={{ color: COLORS[i % COLORS.length] }}>{m.ticker}</td>
                                <td className={`text-right px-3 ${m.beta > 1.2 ? "text-red-400" : m.beta < 0 ? "text-purple-400" : "text-foreground"}`}>{m.beta.toFixed(4)}</td>
                                <td className={`text-right px-3 ${m.alpha_daily > 0 ? "text-emerald-400" : "text-red-400"}`}>{(m.alpha_daily * 100).toFixed(4)}%</td>
                                <td className="text-right px-3 text-cyan-300">{m.expected_return_pct.toFixed(2)}%</td>
                                <td className="text-right px-3 text-amber-400">{m.idiosyncratic_risk_pct.toFixed(2)}%</td>
                                <td className="text-right px-3 text-sky-400">{m.systematic_risk_pct.toFixed(2)}%</td>
                                <td className="text-right pl-3 text-muted/80">{m.total_volatility_pct.toFixed(2)}%</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            {/* ── Grid: All Charts with Expand functionality ── */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                {/* 1. CAPM */}
                <div
                    className="bg-card/30 border border-border/40 rounded-2xl p-4 cursor-pointer hover:border-accent/30 transition-all group"
                    onClick={() => setFocusedChart('capm')}
                >
                    <ChartHeader title={CHART_DETAILS.capm.title} subtitle={CHART_DETAILS.capm.subtitle} onExpand={() => setFocusedChart('capm')} />
                    {renderChart('capm')}
                </div>

                {/* 2. PCA */}
                <div
                    className="bg-card/30 border border-border/40 rounded-2xl p-4 cursor-pointer hover:border-accent/30 transition-all group"
                    onClick={() => setFocusedChart('pca')}
                >
                    <ChartHeader title={CHART_DETAILS.pca.title} subtitle={CHART_DETAILS.pca.subtitle} onExpand={() => setFocusedChart('pca')} />
                    {renderChart('pca')}
                </div>

                {/* 3. Correlation */}
                <div
                    className="bg-card/30 border border-border/40 rounded-2xl p-4 cursor-pointer hover:border-accent/30 transition-all group"
                    onClick={() => setFocusedChart('correlation')}
                >
                    <ChartHeader title={CHART_DETAILS.correlation.title} subtitle={CHART_DETAILS.correlation.subtitle} onExpand={() => setFocusedChart('correlation')} />
                    {renderChart('correlation')}
                </div>

                {/* 4. Risk / Return */}
                <div
                    className="bg-card/30 border border-border/40 rounded-2xl p-4 cursor-pointer hover:border-accent/30 transition-all group"
                    onClick={() => setFocusedChart('riskReturn')}
                >
                    <ChartHeader title={CHART_DETAILS.riskReturn.title} subtitle={CHART_DETAILS.riskReturn.subtitle} onExpand={() => setFocusedChart('riskReturn')} />
                    {renderChart('riskReturn')}
                </div>
            </div>
        </div>
    );
}
