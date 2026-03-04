"use client";

import React from "react";
import dynamic from "next/dynamic";
import {
    TrendingUp, Activity, Bell, Settings, Pin, PinOff,
    Lock as LockIcon, History as HistoryIcon
} from "lucide-react";
import type { SidebarTab, TransactionRecord } from "@/types/dashboard";

const Watchlist = dynamic(() => import("@/components/watchlist/Watchlist"), {
    ssr: false,
    loading: () => <div className="p-4 text-muted text-xs">Loading watchlist...</div>,
});

// ─── Props ──────────────────────────────────────────────────────────
interface DashboardSidebarProps {
    pinned: boolean;
    setPinned: (v: boolean) => void;
    activeTab: SidebarTab;
    setActiveTab: (tab: SidebarTab) => void;
    showFib: boolean;
    setShowFib: (v: boolean) => void;
    transactions: TransactionRecord[];
    onSelectSymbol: (symbol: string) => void;
}

// ─── Component ──────────────────────────────────────────────────────
export default function DashboardSidebar({
    pinned, setPinned, activeTab, setActiveTab,
    showFib, setShowFib, transactions, onSelectSymbol,
}: DashboardSidebarProps) {
    const expanded = pinned;

    const selectTab = (tab: SidebarTab) => {
        setActiveTab(tab);
        if (!pinned) setPinned(true);
    };

    return (
        <div
            className={`absolute right-0 top-0 h-full transition-[transform,width] ease-[cubic-bezier(0.16,1,0.3,1)] duration-500 z-50 flex ${expanded ? 'translate-x-0 w-[400px]' : 'translate-x-[calc(100%-40px)] w-[40px]'}`}
        >
            {/* Vertical Toggle Rail */}
            <div className="w-[40px] bg-card/60 backdrop-blur-2xl flex flex-col items-center py-4 gap-4 h-full border-l border-border/20 shadow-[-8px_0_20px_rgba(0,0,0,0.08)]">
                <button
                    onClick={() => { setPinned(!pinned); if (!pinned) setActiveTab('watchlist'); }}
                    className={`p-1.5 rounded-xl transition-all duration-500 ${pinned
                        ? 'bg-accent/15 text-accent shadow-[0_0_12px_rgba(59,130,246,0.15)]'
                        : 'text-muted/50 hover:text-foreground hover:bg-card-hover/50'}`}
                    title={pinned ? "Unpin Sidebar" : "Pin Sidebar"}
                >
                    {pinned ? <PinOff size={15} /> : <Pin size={15} />}
                </button>

                <div className="w-5 h-px bg-border/20" />

                <RailButton active={activeTab === 'watchlist' && pinned} onClick={() => selectTab('watchlist')} title="Watchlist"
                    activeClass="bg-accent/10 text-accent"><TrendingUp size={15} /></RailButton>

                <RailButton active={activeTab === 'indicators' && pinned} onClick={() => selectTab('indicators')} title="Technicals & Indicators"
                    activeClass="bg-cyan-400/10 text-cyan-400" hoverClass="hover:text-cyan-400"><Activity size={15} /></RailButton>

                <RailButton active={activeTab === 'alerts' && pinned} onClick={() => selectTab('alerts')} title="Alerts"
                    activeClass="bg-yellow-400/10 text-yellow-400" hoverClass="hover:text-yellow-400"><Bell size={15} /></RailButton>

                <RailButton active={activeTab === 'history' && pinned} onClick={() => selectTab('history')} title="Trade History"
                    activeClass="bg-purple-400/10 text-purple-400" hoverClass="hover:text-purple-400"><HistoryIcon size={15} /></RailButton>

                <div className="mt-auto w-5 h-px bg-border/20" />

                <button onClick={() => alert('Layout settings')} className="text-muted/40 hover:text-foreground transition-all duration-300 p-1.5 rounded-lg hover:bg-card-hover/40" title="Settings">
                    <Settings size={14} />
                </button>
            </div>

            {/* Panel Content */}
            {pinned && (
                <div className="flex-1 bg-card/50 backdrop-blur-3xl border-l border-border/15 flex flex-col h-full shadow-[-25px_0_50px_rgba(0,0,0,0.1)] overflow-hidden animate-in slide-in-from-right duration-500">
                    {activeTab === 'watchlist' && <Watchlist onSelectSymbol={onSelectSymbol} />}

                    {activeTab === 'indicators' && <IndicatorsPanel showFib={showFib} setShowFib={setShowFib} />}

                    {activeTab === 'alerts' && <AlertsPanel />}

                    {activeTab === 'history' && <HistoryPanel transactions={transactions} />}
                </div>
            )}
        </div>
    );
}

// ─── Sub-Components (SRP) ───────────────────────────────────────────

function RailButton({ active, onClick, title, children, activeClass, hoverClass = "hover:text-foreground" }: {
    active: boolean; onClick: () => void; title: string; children: React.ReactNode;
    activeClass: string; hoverClass?: string;
}) {
    return (
        <button onClick={onClick} title={title}
            className={`p-1.5 rounded-xl transition-all duration-300 ${active ? activeClass : `text-muted/40 ${hoverClass}`}`}>
            {children}
        </button>
    );
}

function IndicatorsPanel({ showFib, setShowFib }: { showFib: boolean; setShowFib: (v: boolean) => void }) {
    return (
        <div className="flex-1 p-6 overflow-y-auto">
            <div className="flex items-center gap-3 mb-8">
                <div className="h-10 w-10 rounded-2xl bg-cyan-400/10 flex items-center justify-center text-cyan-400 shadow-lg shadow-cyan-400/5 border border-cyan-400/20">
                    <Activity size={20} />
                </div>
                <div>
                    <h3 className="text-sm font-black uppercase tracking-widest text-white">Technicals</h3>
                    <p className="text-[10px] text-muted font-bold mt-0.5">Gravity Engine</p>
                </div>
            </div>

            <div className="space-y-3">
                <div
                    onClick={() => setShowFib(!showFib)}
                    className={`p-4 rounded-2xl border transition-all cursor-pointer group ${showFib ? 'bg-cyan-400/10 border-cyan-400/30' : 'bg-white/5 border-white/10 hover:bg-cyan-400/5 hover:border-cyan-400/30'}`}
                >
                    <div className="flex items-center justify-between">
                        <div>
                            <div className={`text-xs font-black transition-colors ${showFib ? 'text-cyan-400' : 'text-white group-hover:text-cyan-400'}`}>Fibonacci Auto-Levels</div>
                            <div className="text-[9px] text-muted font-bold mt-1 line-clamp-1">Golden ratio retracements (23.6 - 78.6%)</div>
                        </div>
                        <div className={`h-2.5 w-2.5 rounded-full transition-all ${showFib ? 'bg-cyan-400 shadow-[0_0_12px_rgba(34,211,238,0.8)]' : 'bg-zinc-700'}`} />
                    </div>
                </div>

                <LockedIndicator name="Bollinger Bands" desc="2.0 Standard Deviations / 20 Period" hoverColor="purple" />
                <LockedIndicator name="Ichimoku Cloud" desc="Equilibrium Chart / Trend Cloud" hoverColor="orange" />
            </div>

            <div className="mt-12 pt-6 border-t border-white/5">
                <h4 className="text-[10px] font-black uppercase tracking-[0.2em] text-cyan-400/50 mb-3">AI Command</h4>
                <div className="p-3 rounded-xl bg-background/50 border border-white/5 text-[10px] text-muted font-mono leading-relaxed">
                    Ask the agent in Chat to apply custom indicators like <strong>RSI</strong> or <strong>MACD</strong> with specific parameters.
                </div>
            </div>
        </div>
    );
}

function LockedIndicator({ name, desc, hoverColor }: { name: string; desc: string; hoverColor: string }) {
    return (
        <div className={`p-4 rounded-2xl bg-white/5 border border-white/10 hover:bg-${hoverColor}-400/5 hover:border-${hoverColor}-400/30 transition-all cursor-pointer group opacity-60`}>
            <div className="flex items-center justify-between">
                <div>
                    <div className={`text-xs font-black text-zinc-400 group-hover:text-${hoverColor}-400 transition-colors`}>{name}</div>
                    <div className="text-[9px] text-zinc-600 font-bold mt-1">{desc}</div>
                </div>
                <LockIcon size={12} className="text-zinc-700" />
            </div>
        </div>
    );
}

function AlertsPanel() {
    return (
        <div className="flex-1 p-10 flex flex-col items-center justify-center text-center">
            <div className="h-16 w-16 rounded-full bg-yellow-400/5 border border-yellow-400/10 flex items-center justify-center mb-6">
                <Bell size={24} className="text-yellow-400/40" />
            </div>
            <h3 className="text-xs font-black uppercase tracking-widest text-muted">Price Alerts</h3>
            <p className="text-[10px] font-bold text-muted/60 mt-4 max-w-[180px]">Real-time volatility and threshold triggers are under development.</p>
        </div>
    );
}

function HistoryPanel({ transactions }: { transactions: TransactionRecord[] }) {
    return (
        <div className="flex-1 overflow-hidden flex flex-col">
            <div className="px-6 py-4 border-b border-border/15 flex items-center justify-between bg-white/3">
                <h3 className="text-xs font-black uppercase tracking-widest text-white">Execution Logs</h3>
                <span className="text-[9px] bg-purple-500/20 text-purple-400 px-2 py-0.5 rounded border border-purple-500/30 font-black uppercase">Historical</span>
            </div>
            <div className="flex-1 overflow-y-auto p-4 space-y-2">
                {transactions.slice(0, 20).map((t, idx) => (
                    <div key={idx} className="p-3 rounded-xl bg-white/5 border border-white/5 flex items-center justify-between">
                        <div className="flex flex-col">
                            <span className="text-[10px] font-black">{t.symbol}</span>
                            <span className="text-[8px] text-muted font-bold uppercase">{t.date}</span>
                        </div>
                        <span className={`text-[10px] font-mono font-bold ${t.type === 'BUY' ? 'text-green' : 'text-red'}`}>
                            {t.type === 'BUY' ? '+' : '-'}{t.shares}
                        </span>
                    </div>
                ))}
                <div className="text-[10px] text-muted/40 font-bold uppercase tracking-widest text-center py-8">End of Records</div>
            </div>
        </div>
    );
}
