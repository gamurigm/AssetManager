import React, { useState } from "react";
import { X } from "lucide-react";
import { MAConfig, MAType } from "./chartMath";

/* ─── MA Chip (individual control in toolbar) ────────────────────────── */

export function MAChip({ ma, onChange, onRemove }: {
    ma: MAConfig;
    onChange: (updated: MAConfig) => void;
    onRemove: () => void;
}) {
    const [editing, setEditing] = useState(false);
    const types: MAType[] = ["EMA", "SMA", "LWMA"];

    return (
        <div className="relative flex items-center gap-1.5">
            <div
                onClick={() => setEditing(!editing)}
                className={`flex items-center gap-1.5 px-2.5 py-1 rounded-md border cursor-pointer select-none transition-all text-[11px] font-bold uppercase tracking-wide ${ma.visible ? "bg-white/5 border-white/10 text-white hover:bg-white/10" : "bg-transparent border-white/5 text-white/30"}`}
            >
                <div className="h-2 w-2 rounded-full flex-shrink-0" style={{ backgroundColor: ma.visible ? ma.color : "#333", boxShadow: ma.visible ? `0 0 6px ${ma.color}` : "none" }} />
                <span style={{ color: ma.visible ? ma.color : "#555" }}>{ma.type}({ma.period})</span>
            </div>

            {editing && (
                <div className="absolute top-8 left-0 z-50 bg-[#111] border border-white/10 rounded-lg p-3 shadow-2xl flex flex-col gap-3 min-w-[180px]" onClick={e => e.stopPropagation()}>
                    {/* Toggle visibility */}
                    <div className="flex items-center justify-between">
                        <span className="text-[9px] font-black text-white/40 uppercase tracking-widest">Visible</span>
                        <button
                            onClick={() => onChange({ ...ma, visible: !ma.visible })}
                            className={`relative w-8 h-4 rounded-full transition-all ${ma.visible ? "bg-accent" : "bg-white/10"}`}
                        >
                            <div className={`absolute top-0.5 h-3 w-3 rounded-full bg-white transition-all ${ma.visible ? "left-4.5" : "left-0.5"}`} />
                        </button>
                    </div>

                    {/* Type selector */}
                    <div>
                        <span className="text-[9px] font-black text-white/40 uppercase tracking-widest">Type</span>
                        <div className="flex gap-1 mt-1">
                            {types.map(t => (
                                <button
                                    key={t}
                                    onClick={() => onChange({ ...ma, type: t })}
                                    className={`flex-1 py-0.5 text-[10px] font-bold rounded transition-all ${ma.type === t ? "bg-accent text-black" : "bg-white/5 text-white/50 hover:bg-white/10"}`}
                                >{t}</button>
                            ))}
                        </div>
                    </div>

                    {/* Period */}
                    <div>
                        <span className="text-[9px] font-black text-white/40 uppercase tracking-widest">Period</span>
                        <input
                            type="number"
                            value={ma.period}
                            min={1}
                            max={1000}
                            onChange={e => onChange({ ...ma, period: Number(e.target.value) || 1 })}
                            className="mt-1 w-full px-2 py-1 bg-white/5 border border-white/10 rounded text-xs text-white font-mono text-center focus:outline-none focus:border-accent/50"
                        />
                    </div>

                    {/* Color + Remove */}
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-2">
                            <span className="text-[9px] font-black text-white/40 uppercase tracking-widest">Color</span>
                            <input
                                type="color"
                                value={ma.color}
                                onChange={e => onChange({ ...ma, color: e.target.value })}
                                className="w-6 h-6 rounded cursor-pointer border-0 bg-transparent"
                            />
                        </div>
                        <button onClick={onRemove} className="text-red-400 hover:text-red-300 transition-colors p-1">
                            <X size={12} />
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}

/* ─── Param Input ─────────────────────────────────────────────────────── */

export function ParamInput({ label, value, onChange, min = 1, max = 200 }: { label: string; value: number; onChange: (v: number) => void; min?: number; max?: number }) {
    return (
        <div className="flex items-center gap-1.5">
            <label className="text-[10px] font-bold uppercase tracking-wider text-white/40 whitespace-nowrap">{label}</label>
            <input
                type="number"
                value={value}
                min={min}
                max={max}
                onChange={(e) => onChange(Math.max(min, Math.min(max, Number(e.target.value) || min)))}
                className="w-14 px-1.5 py-0.5 bg-white/5 border border-white/10 rounded text-xs text-white font-mono text-center focus:outline-none focus:border-accent/50"
            />
        </div>
    );
}
