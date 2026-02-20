"use client"

import AppLayout from "@/components/layout/AppLayout";
import { useState } from "react";
import { ArrowUpRight, ArrowDownRight, Search, CandlestickChart, Zap, Play, FileTerminal, Activity, Loader2, Link as externalLinkIcon } from "lucide-react";

export default function BacktestLab() {
    const [symbol, setSymbol] = useState("AAPL");
    const [startDate, setStartDate] = useState("2024-01-01");
    const [endDate, setEndDate] = useState("2024-03-31");
    const [account, setAccount] = useState("10000");
    const [bootstrap, setBootstrap] = useState(true);
    const [iterations, setIterations] = useState("1000");

    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState<any>(null);

    const handleRunBacktest = async () => {
        setLoading(true);
        setResult(null);
        try {
            const reqUrl = 'http://localhost:8282/api/v1/simulation/run';
            const reqBody = {
                symbol: symbol,
                start_date: startDate,
                end_date: endDate,
                account_size: parseFloat(account),
                strategy_name: "ORB_FVG_ENGULFING",
                run_bootstrap: bootstrap,
                bootstrap_iterations: parseInt(iterations)
            };

            const response = await fetch(reqUrl, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(reqBody)
            });

            const data = await response.json();
            if (response.ok) {
                setResult(data);
            } else {
                alert(`Error: ${data.detail}`);
            }
        } catch (error) {
            console.error("Backtest Error:", error);
            alert("Failed to connect to backend.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <AppLayout>
            <div className="p-6 lg:p-8 space-y-6 animate-fade-in relative">
                {/* Header */}
                <div className="flex items-center justify-between">
                    <div className="flex items-center gap-4">
                        <div className="h-10 w-10 rounded-xl bg-accent/10 flex items-center justify-center">
                            <CandlestickChart size={20} className="text-accent" />
                        </div>
                        <div>
                            <h1 className="text-2xl font-bold tracking-tight">Strategy Backtest Lab</h1>
                            <p className="text-sm text-muted">Test ORB FVG Engulfing with C++ Engine</p>
                        </div>
                    </div>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">

                    {/* Left: Input Form */}
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
                                    onChange={(e) => setSymbol(e.target.value.toUpperCase())}
                                    className="w-full bg-background border border-border rounded-xl p-3 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all uppercase"
                                    placeholder="AAPL"
                                />
                            </div>

                            <div className="grid grid-cols-2 gap-4">
                                <div>
                                    <label className="text-[10px] text-muted uppercase tracking-widest font-semibold block mb-2">Start Date</label>
                                    <input
                                        type="date"
                                        value={startDate}
                                        onChange={(e) => setStartDate(e.target.value)}
                                        className="w-full bg-background border border-border rounded-xl p-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all text-muted"
                                    />
                                </div>
                                <div>
                                    <label className="text-[10px] text-muted uppercase tracking-widest font-semibold block mb-2">End Date</label>
                                    <input
                                        type="date"
                                        value={endDate}
                                        onChange={(e) => setEndDate(e.target.value)}
                                        className="w-full bg-background border border-border rounded-xl p-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all text-muted"
                                    />
                                </div>
                            </div>

                            <div>
                                <label className="text-[10px] text-muted uppercase tracking-widest font-semibold block mb-2">Initial Capital ($)</label>
                                <input
                                    type="number"
                                    min="100"
                                    value={account}
                                    onChange={(e) => setAccount(e.target.value)}
                                    className="w-full bg-background border border-border rounded-xl p-3 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-accent/30 transition-all"
                                />
                            </div>

                            {/* Bootstrap Section */}
                            <div className="p-4 rounded-xl border border-accent/20 bg-accent/5 space-y-4">
                                <div className="flex items-center justify-between">
                                    <div className="flex items-center gap-2">
                                        <Zap size={14} className="text-yellow-400" />
                                        <label className="text-sm font-semibold">Bootstrap Resampling</label>
                                    </div>
                                    <button
                                        onClick={() => setBootstrap(!bootstrap)}
                                        className={`w-10 h-5 rounded-full relative transition-colors ${bootstrap ? 'bg-accent' : 'bg-card-hover'}`}
                                    >
                                        <div className={`w-4 h-4 rounded-full bg-white absolute top-0.5 transition-all ${bootstrap ? 'left-5' : 'left-0.5'}`} />
                                    </button>
                                </div>

                                {bootstrap && (
                                    <div className="animate-fade-in space-y-2">
                                        <label className="text-[10px] text-accent uppercase tracking-widest font-bold block">Monte Carlo Iterations</label>
                                        <select
                                            value={iterations}
                                            onChange={(e) => setIterations(e.target.value)}
                                            className="w-full bg-background border border-border rounded-xl p-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-accent/30 text-muted"
                                        >
                                            <option value="1000">1,000 (Fast)</option>
                                            <option value="5000">5,000 (Detailed)</option>
                                            <option value="10000">10,000 (Deep Analysis)</option>
                                        </select>
                                        <p className="text-[10px] text-muted text-justify">
                                            Utiliza el motor nativo en C++ para mezclar la secuencia de retornos y generar un Intervalo de Confianza (95%) aislando el factor suerte.
                                        </p>
                                    </div>
                                )}
                            </div>

                            <button
                                onClick={handleRunBacktest}
                                disabled={loading || !symbol || !startDate || !endDate}
                                className={`w-full py-3.5 rounded-xl font-bold text-sm transition-all shadow-lg flex justify-center items-center gap-2
                                    ${loading ? "bg-accent/50 cursor-not-allowed text-white" : "bg-accent hover:bg-accent-hover text-white shadow-accent/20"}`}
                            >
                                {loading ? <Loader2 size={16} className="animate-spin" /> : <Play fill="currentColor" size={14} />}
                                {loading ? "Running C++ Engine..." : "Run Backtest Analysis"}
                            </button>
                        </div>
                    </div>

                    {/* Right: Results Panel */}
                    <div className="lg:col-span-8 flex flex-col gap-6">

                        {!result && !loading && (
                            <div className="flex-1 bg-card border border-border border-dashed rounded-2xl flex flex-col items-center justify-center text-muted p-10 min-h-[500px]">
                                <Activity size={48} className="text-muted/30 mb-4" />
                                <h3 className="text-lg font-semibold text-foreground">Awaiting Simulation</h3>
                                <p className="text-sm mt-2 max-w-sm text-center">Configure the parameters and hit Run Backtest to execute the strategy natively against historical M1/M5 ticks.</p>
                            </div>
                        )}

                        {loading && (
                            <div className="flex-1 bg-card border border-border rounded-2xl flex flex-col items-center justify-center p-10 min-h-[500px]">
                                <Loader2 size={40} className="animate-spin text-accent mb-4" />
                                <p className="text-sm font-mono text-accent animate-pulse uppercase tracking-widest">Compiling historical ticks & executing logic</p>
                            </div>
                        )}

                        {result && !loading && (
                            <>
                                {/* KPI Cards */}
                                <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 stagger">
                                    <div className="bg-card border border-border rounded-xl p-4">
                                        <p className="text-[10px] text-muted uppercase tracking-wider font-semibold">Net Profit</p>
                                        <p className={`text-xl font-mono font-bold mt-1 ${result.kpis.final_equity - parseFloat(account) >= 0 ? 'text-green' : 'text-red'}`}>
                                            ${(result.kpis.final_equity - parseFloat(account)).toLocaleString(undefined, { minimumFractionDigits: 2 })}
                                        </p>
                                    </div>
                                    <div className="bg-card border border-border rounded-xl p-4">
                                        <p className="text-[10px] text-muted uppercase tracking-wider font-semibold">Win Rate</p>
                                        <p className="text-xl font-mono font-bold mt-1 text-white">{(result.kpis.win_rate * 100).toFixed(1)}%</p>
                                        <p className="text-xs text-muted mt-1">{result.kpis.wins}W / {result.kpis.losses}L</p>
                                    </div>
                                    <div className="bg-card border border-border rounded-xl p-4">
                                        <p className="text-[10px] text-muted uppercase tracking-wider font-semibold">Profit Factor</p>
                                        <p className="text-xl font-mono font-bold mt-1 text-purple-400">{result.kpis.profit_factor}</p>
                                    </div>
                                    <div className="bg-card border border-border rounded-xl p-4">
                                        <p className="text-[10px] text-muted uppercase tracking-wider font-semibold">Max Drawdown</p>
                                        <p className="text-xl font-mono font-bold mt-1 text-red">{result.kpis.max_drawdown_pct}%</p>
                                    </div>
                                </div>

                                {/* Bootstrap Results & Report Link */}
                                <div className="bg-card border border-border rounded-2xl p-6 relative overflow-hidden flex-1 shadow-sm">

                                    <h3 className="text-lg font-semibold mb-6">Detailed Analysis</h3>

                                    {result.bootstrap ? (
                                        <div className="space-y-6">
                                            <div className="flex gap-2 items-center text-sm font-semibold text-green bg-green/10 px-3 py-1.5 w-fit rounded-lg border border-green/20">
                                                <Zap size={14} />
                                                Bootstrap Confidence Metrics (95%)
                                            </div>

                                            <div className="grid grid-cols-2 gap-6 bg-background rounded-xl p-5 border border-border">
                                                <div>
                                                    <p className="text-xs text-muted uppercase tracking-wider mb-1">Expected Profit Range</p>
                                                    <p className="text-lg font-mono font-bold text-white">
                                                        ${result.bootstrap.net_profit_95_ci[0].toLocaleString(undefined, { maximumFractionDigits: 0 })}
                                                        <span className="text-muted mx-2">to</span>
                                                        ${result.bootstrap.net_profit_95_ci[1].toLocaleString(undefined, { maximumFractionDigits: 0 })}
                                                    </p>
                                                </div>
                                                <div>
                                                    <p className="text-xs text-muted uppercase tracking-wider mb-1">Worst Case Drawdown</p>
                                                    <p className="text-lg font-mono font-bold text-red">
                                                        Up to {result.bootstrap.max_drawdown_95_ci_pct[1].toFixed(2)}%
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                    ) : (
                                        <div className="text-sm text-muted mb-6">
                                            Resampling was off. Only historical baseline calculated.
                                        </div>
                                    )}

                                    {/* Open Report Button */}
                                    {result.report_url && (
                                        <div className="mt-8 pt-6 border-t border-border">
                                            <a
                                                href={result.report_url}
                                                target="_blank"
                                                rel="noreferrer"
                                                className="w-full flex items-center justify-center gap-3 py-4 bg-zinc-800 hover:bg-zinc-700 text-white font-bold rounded-xl transition-all border border-zinc-600 hover:border-accent group"
                                            >
                                                <Activity className="group-hover:text-accent transition-colors" size={20} />
                                                View Interactive Plotly HTML Report
                                                <externalLinkIcon size={16} className="text-muted group-hover:text-white" />
                                            </a>
                                            <p className="text-center text-xs text-muted mt-3">Opens in a new window with full charts and distributions.</p>
                                        </div>
                                    )}
                                </div>
                            </>
                        )}
                    </div>
                </div>
            </div>
        </AppLayout>
    );
}
