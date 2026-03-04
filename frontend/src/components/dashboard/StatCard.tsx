"use client";

import React from "react";
import { STAT_ACCENT_COLORS } from "@/lib/colors";

interface StatCardProps {
    label: string;
    value: string;
    sub?: string;
    icon: React.ReactNode;
    accent: string;
}

export default function StatCard({ label, value, sub, icon, accent }: StatCardProps) {
    return (
        <div className="glass-card rounded-[24px] p-6 hover:translate-y-[-4px] transition-all duration-500 group relative overflow-hidden shadow-2xl">
            <div className="absolute top-0 left-0 w-full h-[2px] bg-gradient-to-r from-transparent via-current to-transparent opacity-20" style={{ color: STAT_ACCENT_COLORS[accent]?.split(' ')[0].replace('text-', '') }} />

            <div className="relative z-10">
                <div className="flex items-center justify-between mb-4">
                    <span className="text-[10px] text-muted font-black uppercase tracking-[0.2em] opacity-60">{label}</span>
                    <div className={`h-10 w-10 rounded-2xl flex items-center justify-center border animate-pulse-glow ${STAT_ACCENT_COLORS[accent] || STAT_ACCENT_COLORS.blue}`}>
                        {React.cloneElement(icon as React.ReactElement<any>, { size: 18 })}
                    </div>
                </div>
                <p className="text-3xl font-black tracking-tighter leading-none mb-2">{value}</p>
                {sub && (
                    <div className="flex items-center gap-2">
                        <span className={`text-xs font-black px-2 py-0.5 rounded-lg ${accent === "red" ? "bg-red/10 text-red" : "bg-green/10 text-green"}`}>
                            {sub}
                        </span>
                        <span className="text-[9px] text-muted font-bold uppercase tracking-widest opacity-40">Period Delta</span>
                    </div>
                )}
            </div>

            {/* Subtle background glow */}
            <div className={`absolute -bottom-10 -right-10 w-32 h-32 rounded-full blur-[60px] opacity-10 transition-opacity group-hover:opacity-20
                ${accent === 'blue' ? 'bg-blue-500' : accent === 'green' ? 'bg-green' : accent === 'red' ? 'bg-red' : accent === 'purple' ? 'bg-purple-500' : 'bg-emerald-500'}`} />
        </div>
    );
}
