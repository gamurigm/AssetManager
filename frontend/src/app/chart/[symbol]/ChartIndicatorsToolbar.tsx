import React from "react";
import { BarChart2, ChevronDown, ChevronUp, X } from "lucide-react";
import { MAChip } from "./ChartUIComponents";
import { MAConfig, MAType } from "./chartMath";

export interface ChartIndicatorsToolbarProps {
    indicatorsOpen: boolean;
    setIndicatorsOpen: (open: boolean) => void;
    showVP: boolean;
    setShowVP: (show: boolean) => void;
    mas: MAConfig[];
    addMA: () => void;
    updateMA: (id: string, updated: MAConfig) => void;
    removeMA: (id: string) => void;
    showMACD: boolean;
    setShowMACD: (show: boolean) => void;
    macdFast: number;
    macdSlow: number;
    macdSignal: number;
    showStoch: boolean;
    setShowStoch: (show: boolean) => void;
    stochK: number;
    stochD: number;
    stochSmooth: number;
    showFib: boolean;
    setShowFib: (show: boolean) => void;
    fibLookback: number;
    setFibLookback: (val: number) => void;
    showBB: boolean;
    setShowBB: (show: boolean) => void;
    bbPeriod: number;
    setBbPeriod: (val: number) => void;
    bbMult: number;
    setBbMult: (val: number) => void;
    showATR: boolean;
    setShowATR: (show: boolean) => void;
    atrPeriod: number;
    setAtrPeriod: (val: number) => void;
    showPSAR: boolean;
    setShowPSAR: (show: boolean) => void;
    psarStep: number;
    setPsarStep: (val: number) => void;
    psarMax: number;
    setPsarMax: (val: number) => void;
    showSupertrend: boolean;
    setShowSupertrend: (show: boolean) => void;
    supertrendPeriod: number;
    setSupertrendPeriod: (val: number) => void;
    supertrendMult: number;
    setSupertrendMult: (val: number) => void;
    showWilliams: boolean;
    setShowWilliams: (show: boolean) => void;
    williamsPeriod: number;
    setWilliamsPeriod: (val: number) => void;
    showMFI: boolean;
    setShowMFI: (show: boolean) => void;
    mfiPeriod: number;
    setMfiPeriod: (val: number) => void;
    showCMF: boolean;
    setShowCMF: (show: boolean) => void;
    cmfPeriod: number;
    setCmfPeriod: (val: number) => void;
    showRSI: boolean;
    setShowRSI: (show: boolean) => void;
    rsiPeriod: number;
    setRsiPeriod: (val: number) => void;
    showCCI: boolean;
    setShowCCI: (show: boolean) => void;
    cciPeriod: number;
    setCciPeriod: (val: number) => void;
    showADX: boolean;
    setShowADX: (show: boolean) => void;
    adxPeriod: number;
    setAdxPeriod: (val: number) => void;
}

export function ChartIndicatorsToolbar(props: ChartIndicatorsToolbarProps) {
    return (
        <div className="px-4 border-b border-white/5 bg-[#0d0d0d] flex items-center gap-2 flex-shrink-0 flex-wrap" style={{ minHeight: 38 }} onClick={e => e.stopPropagation()}>
            {/* Indicators button */}
            <button
                onClick={() => props.setIndicatorsOpen(!props.indicatorsOpen)}
                className="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-white/5 border border-white/10 text-white/60 hover:text-white hover:bg-white/10 transition-all text-[11px] font-bold uppercase tracking-wide"
            >
                <BarChart2 size={13} />
                Indicators
                {props.indicatorsOpen ? <ChevronUp size={11} /> : <ChevronDown size={11} />}
            </button>

            <button
                onClick={() => props.setShowVP(!props.showVP)}
                className={`flex items-center gap-1.5 px-2.5 py-1 rounded-md border transition-all text-[11px] font-bold uppercase tracking-wide ${props.showVP ? "bg-accent/20 border-accent/40 text-accent" : "bg-white/5 border-white/10 text-white/60 hover:text-white hover:bg-white/10"}`}
            >
                VP
            </button>

            {/* Indicator add panel (dropdown) */}
            {props.indicatorsOpen && (
                <div className="absolute top-[86px] left-4 z-50 bg-[#0f0f0f] border border-white/10 rounded-xl p-4 shadow-2xl flex flex-col gap-3 w-72">
                    <div className="flex items-center justify-between">
                        <span className="text-[11px] font-black uppercase tracking-widest text-white/60">Moving Averages</span>
                        <button onClick={props.addMA} className="text-[10px] font-bold text-accent hover:text-white transition-colors px-2 py-0.5 bg-accent/10 rounded">+ Add</button>
                    </div>
                    {props.mas.map(ma => (
                        <div key={ma.id} className="flex items-center gap-2">
                            <div className="h-2.5 w-2.5 rounded-full flex-shrink-0" style={{ backgroundColor: ma.color, boxShadow: `0 0 6px ${ma.color}` }} />
                            <div className="flex gap-1 flex-1">
                                {(["EMA", "SMA", "LWMA"] as MAType[]).map(t => (
                                    <button key={t} onClick={() => props.updateMA(ma.id, { ...ma, type: t })}
                                        className={`flex-1 py-0.5 text-[10px] font-bold rounded transition-all ${ma.type === t ? "bg-accent text-black" : "bg-white/5 text-white/40 hover:bg-white/10"}`}>{t}</button>
                                ))}
                            </div>
                            <input type="number" value={ma.period} min={1} max={1000}
                                onChange={e => props.updateMA(ma.id, { ...ma, period: Number(e.target.value) || 1 })}
                                className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                            <input type="color" value={ma.color}
                                onChange={e => props.updateMA(ma.id, { ...ma, color: e.target.value })}
                                className="w-6 h-6 cursor-pointer bg-transparent border-0" />
                            <button onClick={() => props.updateMA(ma.id, { ...ma, visible: !ma.visible })}
                                className={`w-6 h-6 rounded flex items-center justify-center text-[10px] font-bold transition-all ${ma.visible ? "bg-accent/20 text-accent" : "bg-white/5 text-white/30"}`}>
                                {ma.visible ? "●" : "○"}
                            </button>
                            <button onClick={() => props.removeMA(ma.id)} className="text-white/20 hover:text-red-400 transition-colors">
                                <X size={12} />
                            </button>
                        </div>
                    ))}

                    <div className="pt-2 border-t border-white/5 flex flex-col gap-2">
                        <span className="text-[11px] font-black uppercase tracking-widest text-white/60">Oscillators &amp; Overlays</span>
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">VP (POC, VAH/VAL)</span>
                            <button onClick={() => props.setShowVP(!props.showVP)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showVP ? "bg-accent/20 text-accent" : "bg-white/5 text-white/30"}`}>{props.showVP ? "ON" : "OFF"}</button>
                        </div>
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">MACD ({props.macdFast},{props.macdSlow},{props.macdSignal})</span>
                            <button onClick={() => props.setShowMACD(!props.showMACD)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showMACD ? "bg-accent/20 text-accent" : "bg-white/5 text-white/30"}`}>{props.showMACD ? "ON" : "OFF"}</button>
                        </div>
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">STOCH ({props.stochK},{props.stochD},{props.stochSmooth})</span>
                            <button onClick={() => props.setShowStoch(!props.showStoch)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showStoch ? "bg-accent/20 text-accent" : "bg-white/5 text-white/30"}`}>{props.showStoch ? "ON" : "OFF"}</button>
                        </div>
                    </div>

                    <div className="pt-2 border-t border-white/5 flex flex-col gap-2">
                        <span className="text-[11px] font-black uppercase tracking-widest text-amber-400/80">Advanced Indicators</span>
                        {/* Fibonacci */}
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">Fibonacci Retracement</span>
                            <button onClick={() => props.setShowFib(!props.showFib)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showFib ? "bg-amber-500/20 text-amber-400" : "bg-white/5 text-white/30"}`}>{props.showFib ? "ON" : "OFF"}</button>
                        </div>
                        {props.showFib && (
                            <div className="flex items-center gap-2 pl-2">
                                <span className="text-[9px] text-white/30 uppercase font-bold">Lookback</span>
                                <input type="number" value={props.fibLookback} min={10} max={1000}
                                    onChange={e => props.setFibLookback(Math.max(10, Number(e.target.value) || 120))}
                                    className="w-16 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                            </div>
                        )}
                        {/* Bollinger Bands */}
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">Bollinger Bands ({props.bbPeriod},{props.bbMult}x)</span>
                            <button onClick={() => props.setShowBB(!props.showBB)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showBB ? "bg-blue-500/20 text-blue-400" : "bg-white/5 text-white/30"}`}>{props.showBB ? "ON" : "OFF"}</button>
                        </div>
                        {props.showBB && (
                            <div className="flex items-center gap-3 pl-2">
                                <div className="flex items-center gap-1">
                                    <span className="text-[9px] text-white/30 uppercase font-bold">Period</span>
                                    <input type="number" value={props.bbPeriod} min={5} max={200}
                                        onChange={e => props.setBbPeriod(Math.max(5, Number(e.target.value) || 20))}
                                        className="w-12 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                                </div>
                                <div className="flex items-center gap-1">
                                    <span className="text-[9px] text-white/30 uppercase font-bold">Mult</span>
                                    <input type="number" value={props.bbMult} min={0.5} max={5} step={0.1}
                                        onChange={e => props.setBbMult(Math.max(0.5, Number(e.target.value) || 2))}
                                        className="w-12 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                                </div>
                            </div>
                        )}
                        {/* ATR */}
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">ATR ({props.atrPeriod})</span>
                            <button onClick={() => props.setShowATR(!props.showATR)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showATR ? "bg-purple-500/20 text-purple-400" : "bg-white/5 text-white/30"}`}>{props.showATR ? "ON" : "OFF"}</button>
                        </div>
                        {props.showATR && (
                            <div className="flex items-center gap-2 pl-2">
                                <span className="text-[9px] text-white/30 uppercase font-bold">Period</span>
                                <input type="number" value={props.atrPeriod} min={1} max={100}
                                    onChange={e => props.setAtrPeriod(Math.max(1, Number(e.target.value) || 14))}
                                    className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                            </div>
                        )}
                        {/* Parabolic SAR */}
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">Parabolic SAR</span>
                            <button onClick={() => props.setShowPSAR(!props.showPSAR)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showPSAR ? "bg-amber-500/20 text-amber-400" : "bg-white/5 text-white/30"}`}>{props.showPSAR ? "ON" : "OFF"}</button>
                        </div>
                        {props.showPSAR && (
                            <div className="flex flex-col gap-2 pl-2">
                                <div className="flex items-center justify-between">
                                    <span className="text-[9px] text-white/30 uppercase font-bold">Step</span>
                                    <input type="number" step="0.01" value={props.psarStep} onChange={e => props.setPsarStep(Number(e.target.value))} className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                                </div>
                                <div className="flex items-center justify-between">
                                    <span className="text-[9px] text-white/30 uppercase font-bold">Max</span>
                                    <input type="number" step="0.01" value={props.psarMax} onChange={e => props.setPsarMax(Number(e.target.value))} className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                                </div>
                            </div>
                        )}
                        {/* Supertrend */}
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">Supertrend</span>
                            <button onClick={() => props.setShowSupertrend(!props.showSupertrend)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showSupertrend ? "bg-emerald-500/20 text-emerald-400" : "bg-white/5 text-white/30"}`}>{props.showSupertrend ? "ON" : "OFF"}</button>
                        </div>
                        {props.showSupertrend && (
                            <div className="flex flex-col gap-2 pl-2">
                                <div className="flex items-center justify-between">
                                    <span className="text-[9px] text-white/30 uppercase font-bold">Period</span>
                                    <input type="number" value={props.supertrendPeriod} onChange={e => props.setSupertrendPeriod(Number(e.target.value))} className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                                </div>
                                <div className="flex items-center justify-between">
                                    <span className="text-[9px] text-white/30 uppercase font-bold">Mult</span>
                                    <input type="number" step="0.1" value={props.supertrendMult} onChange={e => props.setSupertrendMult(Number(e.target.value))} className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                                </div>
                            </div>
                        )}
                        {/* Williams %R */}
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">Will %R ({props.williamsPeriod})</span>
                            <button onClick={() => props.setShowWilliams(!props.showWilliams)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showWilliams ? "bg-cyan-500/20 text-cyan-400" : "bg-white/5 text-white/30"}`}>{props.showWilliams ? "ON" : "OFF"}</button>
                        </div>
                        {props.showWilliams && (
                            <div className="flex items-center gap-2 pl-2">
                                <span className="text-[9px] text-white/30 uppercase font-bold">Period</span>
                                <input type="number" value={props.williamsPeriod} min={1} max={100}
                                    onChange={e => props.setWilliamsPeriod(Math.max(1, Number(e.target.value) || 14))}
                                    className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                            </div>
                        )}
                        {/* MFI */}
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">MFI ({props.mfiPeriod})</span>
                            <button onClick={() => props.setShowMFI(!props.showMFI)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showMFI ? "bg-violet-500/20 text-violet-400" : "bg-white/5 text-white/30"}`}>{props.showMFI ? "ON" : "OFF"}</button>
                        </div>
                        {props.showMFI && (
                            <div className="flex items-center gap-2 pl-2">
                                <span className="text-[9px] text-white/30 uppercase font-bold">Period</span>
                                <input type="number" value={props.mfiPeriod} min={1} max={100}
                                    onChange={e => props.setMfiPeriod(Math.max(1, Number(e.target.value) || 14))}
                                    className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                            </div>
                        )}
                        {/* CMF */}
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">CMF ({props.cmfPeriod})</span>
                            <button onClick={() => props.setShowCMF(!props.showCMF)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showCMF ? "bg-blue-500/20 text-blue-400" : "bg-white/5 text-white/30"}`}>{props.showCMF ? "ON" : "OFF"}</button>
                        </div>
                        {props.showCMF && (
                            <div className="flex items-center gap-2 pl-2">
                                <span className="text-[9px] text-white/30 uppercase font-bold">Period</span>
                                <input type="number" value={props.cmfPeriod} min={1} max={100}
                                    onChange={e => props.setCmfPeriod(Math.max(1, Number(e.target.value) || 20))}
                                    className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                            </div>
                        )}
                        {/* RSI */}
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">RSI ({props.rsiPeriod})</span>
                            <button onClick={() => props.setShowRSI(!props.showRSI)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showRSI ? "bg-rose-500/20 text-rose-400" : "bg-white/5 text-white/30"}`}>{props.showRSI ? "ON" : "OFF"}</button>
                        </div>
                        {props.showRSI && (
                            <div className="flex items-center gap-2 pl-2">
                                <span className="text-[9px] text-white/30 uppercase font-bold">Period</span>
                                <input type="number" value={props.rsiPeriod} min={1} max={100}
                                    onChange={e => props.setRsiPeriod(Math.max(1, Number(e.target.value) || 14))}
                                    className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                            </div>
                        )}
                        {/* CCI */}
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">CCI ({props.cciPeriod})</span>
                            <button onClick={() => props.setShowCCI(!props.showCCI)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showCCI ? "bg-lime-500/20 text-lime-400" : "bg-white/5 text-white/30"}`}>{props.showCCI ? "ON" : "OFF"}</button>
                        </div>
                        {props.showCCI && (
                            <div className="flex items-center gap-2 pl-2">
                                <span className="text-[9px] text-white/30 uppercase font-bold">Period</span>
                                <input type="number" value={props.cciPeriod} min={1} max={100}
                                    onChange={e => props.setCciPeriod(Math.max(1, Number(e.target.value) || 20))}
                                    className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                            </div>
                        )}
                        {/* ADX */}
                        <div className="flex items-center justify-between">
                            <span className="text-[11px] text-white/50 font-mono">ADX ({props.adxPeriod})</span>
                            <button onClick={() => props.setShowADX(!props.showADX)} className={`text-[10px] font-bold px-2 py-0.5 rounded ${props.showADX ? "bg-fuchsia-500/20 text-fuchsia-400" : "bg-white/5 text-white/30"}`}>{props.showADX ? "ON" : "OFF"}</button>
                        </div>
                        {props.showADX && (
                            <div className="flex items-center gap-2 pl-2">
                                <span className="text-[9px] text-white/30 uppercase font-bold">Period</span>
                                <input type="number" value={props.adxPeriod} min={1} max={100}
                                    onChange={e => props.setAdxPeriod(Math.max(1, Number(e.target.value) || 14))}
                                    className="w-14 px-1 py-0.5 bg-white/5 border border-white/10 rounded text-[11px] text-white font-mono text-center focus:outline-none" />
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* MA chips inline */}
            {props.mas.filter(m => m.visible).map(ma => (
                <div key={ma.id} className="flex items-center gap-1 px-2 py-0.5 rounded bg-white/3 border border-white/8 text-[11px] font-bold" style={{ color: ma.color }}>
                    <div className="h-1.5 w-1.5 rounded-full" style={{ backgroundColor: ma.color }} />
                    <MAChip ma={ma} onChange={updated => props.updateMA(ma.id, updated)} onRemove={() => props.removeMA(ma.id)} />
                </div>
            ))}
        </div>
    );
}
