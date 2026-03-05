"use client";

import React from "react";
import dynamic from "next/dynamic";
import {
    TrendingUp, Activity, Bell, Settings, Pin, PinOff,
    History as HistoryIcon,
    LineChart, BarChart2, Zap, Layers, Maximize2, Repeat, Target, Sliders, Hash
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
    showBollinger: boolean;
    setShowBollinger: (v: boolean) => void;
    showIchimoku: boolean;
    setShowIchimoku: (v: boolean) => void;
    showVwap: boolean;
    setShowVwap: (v: boolean) => void;
    showRsi: boolean;
    setShowRsi: (v: boolean) => void;
    showAtr: boolean;
    setShowAtr: (v: boolean) => void;
    showKeltner: boolean;
    setShowKeltner: (v: boolean) => void;
    showCci: boolean;
    setShowCci: (v: boolean) => void;
    showAdx: boolean;
    setShowAdx: (v: boolean) => void;
    showPsar: boolean;
    setShowPsar: (v: boolean) => void;
    showSupertrend: boolean;
    setShowSupertrend: (v: boolean) => void;
    showWilliams: boolean;
    setShowWilliams: (v: boolean) => void;
    showMfi: boolean;
    setShowMfi: (v: boolean) => void;
    showCmf: boolean;
    setShowCmf: (v: boolean) => void;
    transactions: TransactionRecord[];
    onSelectSymbol: (symbol: string) => void;
}

// ─── Component ──────────────────────────────────────────────────────
export default function DashboardSidebar({
    pinned, setPinned, activeTab, setActiveTab,
    showFib, setShowFib, showBollinger, setShowBollinger, showIchimoku, setShowIchimoku,
    showVwap, setShowVwap, showRsi, setShowRsi, showAtr, setShowAtr,
    showKeltner, setShowKeltner, showCci, setShowCci, showAdx, setShowAdx,
    showPsar, setShowPsar, showSupertrend, setShowSupertrend,
    showWilliams, setShowWilliams, showMfi, setShowMfi, showCmf, setShowCmf,
    transactions, onSelectSymbol,
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

                    {activeTab === 'indicators' && <IndicatorsPanel showFib={showFib} setShowFib={setShowFib} showBollinger={showBollinger} setShowBollinger={setShowBollinger} showIchimoku={showIchimoku} setShowIchimoku={setShowIchimoku} showVwap={showVwap} setShowVwap={setShowVwap} showRsi={showRsi} setShowRsi={setShowRsi} showAtr={showAtr} setShowAtr={setShowAtr} showKeltner={showKeltner} setShowKeltner={setShowKeltner} showCci={showCci} setShowCci={setShowCci} showAdx={showAdx} setShowAdx={setShowAdx} showPsar={showPsar} setShowPsar={setShowPsar} showSupertrend={showSupertrend} setShowSupertrend={setShowSupertrend} showWilliams={showWilliams} setShowWilliams={setShowWilliams} showMfi={showMfi} setShowMfi={setShowMfi} showCmf={showCmf} setShowCmf={setShowCmf} />}

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

function IndicatorsPanel({ showFib, setShowFib, showBollinger, setShowBollinger, showIchimoku, setShowIchimoku, showVwap, setShowVwap, showRsi, setShowRsi, showAtr, setShowAtr, showKeltner, setShowKeltner, showCci, setShowCci, showAdx, setShowAdx, showPsar, setShowPsar, showSupertrend, setShowSupertrend, showWilliams, setShowWilliams, showMfi, setShowMfi, showCmf, setShowCmf }: {
    showFib: boolean; setShowFib: (v: boolean) => void;
    showBollinger: boolean; setShowBollinger: (v: boolean) => void;
    showIchimoku: boolean; setShowIchimoku: (v: boolean) => void;
    showVwap: boolean; setShowVwap: (v: boolean) => void;
    showRsi: boolean; setShowRsi: (v: boolean) => void;
    showAtr: boolean; setShowAtr: (v: boolean) => void;
    showKeltner: boolean; setShowKeltner: (v: boolean) => void;
    showCci: boolean; setShowCci: (v: boolean) => void;
    showAdx: boolean; setShowAdx: (v: boolean) => void;
    showPsar: boolean; setShowPsar: (v: boolean) => void;
    showSupertrend: boolean; setShowSupertrend: (v: boolean) => void;
    showWilliams: boolean; setShowWilliams: (v: boolean) => void;
    showMfi: boolean; setShowMfi: (v: boolean) => void;
    showCmf: boolean; setShowCmf: (v: boolean) => void;
}) {
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

            <p className="text-[9px] text-muted/60 font-bold uppercase tracking-widest mb-2">Overlays</p>
            <div className="space-y-3">
                <IndicatorToggle active={showFib} onClick={() => setShowFib(!showFib)} name="Fibonacci Auto-Levels" desc="Golden ratio retracements (23.6 - 78.6%)" activeColor="cyan" Icon={Hash} />
                <IndicatorToggle active={showBollinger} onClick={() => setShowBollinger(!showBollinger)} name="Bollinger Bands" desc="20 Period SMA ± 2.0 Standard Deviations" activeColor="purple" Icon={Layers} />
                <IndicatorToggle active={showKeltner} onClick={() => setShowKeltner(!showKeltner)} name="Keltner Channels" desc="EMA ± Multiplier × ATR" activeColor="blue" Icon={Maximize2} />
                <IndicatorToggle active={showIchimoku} onClick={() => setShowIchimoku(!showIchimoku)} name="Ichimoku Cloud" desc="Tenkan (9) / Kijun (26) / Senkou / Chikou" activeColor="orange" Icon={LineChart} />
                <IndicatorToggle active={showVwap} onClick={() => setShowVwap(!showVwap)} name="VWAP" desc="Volume Weighted Average Price (institutional)" activeColor="yellow" Icon={BarChart2} />
                <IndicatorToggle active={showPsar} onClick={() => setShowPsar(!showPsar)} name="Parabolic SAR" desc="Stop and Reverse trend tracking" activeColor="pink" Icon={Target} />
                <IndicatorToggle active={showSupertrend} onClick={() => setShowSupertrend(!showSupertrend)} name="Supertrend" desc="ATR-based trailing stop trend identifier" activeColor="teal" Icon={TrendingUp} />
            </div>

            <p className="text-[9px] text-muted/60 font-bold uppercase tracking-widest mt-6 mb-2">Oscillators & Volatility</p>
            <div className="space-y-3">
                <IndicatorToggle active={showRsi} onClick={() => setShowRsi(!showRsi)} name="RSI (14)" desc="Relative Strength Index — Overbought 70 / Oversold 30" activeColor="amber" Icon={Activity} />
                <IndicatorToggle active={showWilliams} onClick={() => setShowWilliams(!showWilliams)} name="Williams %R" desc="Momentum oscillator measuring overbought/oversold levels" activeColor="cyan" Icon={Sliders} />
                <IndicatorToggle active={showAtr} onClick={() => setShowAtr(!showAtr)} name="ATR (14)" desc="Average True Range — Wilder's Volatility Metric" activeColor="teal" Icon={Zap} />
                <IndicatorToggle active={showCci} onClick={() => setShowCci(!showCci)} name="CCI (20)" desc="Commodity Channel Index — Cyclical turns" activeColor="violet" Icon={Repeat} />
                <IndicatorToggle active={showAdx} onClick={() => setShowAdx(!showAdx)} name="ADX (14)" desc="Average Directional Index — Trend Strength" activeColor="pink" Icon={TrendingUp} />

                <IndicatorToggle active={showMfi} onClick={() => setShowMfi(!showMfi)} name="MFI (14)" desc="Money Flow Index — Volume-weighted RSI" activeColor="purple" Icon={Activity} />
                <IndicatorToggle active={showCmf} onClick={() => setShowCmf(!showCmf)} name="CMF (20)" desc="Chaikin Money Flow — Institutional accumulation" activeColor="blue" Icon={BarChart2} />
            </div>

            <div className="mt-8 pt-6 border-t border-white/5">
                <h4 className="text-[10px] font-black uppercase tracking-[0.2em] text-cyan-400/50 mb-3">AI Command</h4>
                <div className="p-3 rounded-xl bg-background/50 border border-white/5 text-[10px] text-muted font-mono leading-relaxed">
                    Ask the agent in Chat to apply custom indicators like <strong>RSI</strong> or <strong>MACD</strong> with specific parameters.
                </div>
            </div>
        </div>
    );
}

function IndicatorToggle({ active, onClick, name, desc, activeColor, Icon }: {
    active: boolean; onClick: () => void; name: string; desc: string; activeColor: string; Icon?: any;
}) {
    const colorMap: Record<string, { bg: string; border: string; text: string; glow: string; hoverBg: string; hoverBorder: string }> = {
        cyan: { bg: 'bg-cyan-400/10', border: 'border-cyan-400/30', text: 'text-cyan-400', glow: 'shadow-[0_0_12px_rgba(34,211,238,0.8)]', hoverBg: 'hover:bg-cyan-400/5', hoverBorder: 'hover:border-cyan-400/30' },
        purple: { bg: 'bg-purple-400/10', border: 'border-purple-400/30', text: 'text-purple-400', glow: 'shadow-[0_0_12px_rgba(168,85,247,0.8)]', hoverBg: 'hover:bg-purple-400/5', hoverBorder: 'hover:border-purple-400/30' },
        orange: { bg: 'bg-orange-400/10', border: 'border-orange-400/30', text: 'text-orange-400', glow: 'shadow-[0_0_12px_rgba(251,146,60,0.8)]', hoverBg: 'hover:bg-orange-400/5', hoverBorder: 'hover:border-orange-400/30' },
        yellow: { bg: 'bg-yellow-400/10', border: 'border-yellow-400/30', text: 'text-yellow-400', glow: 'shadow-[0_0_12px_rgba(250,204,21,0.8)]', hoverBg: 'hover:bg-yellow-400/5', hoverBorder: 'hover:border-yellow-400/30' },
        amber: { bg: 'bg-amber-400/10', border: 'border-amber-400/30', text: 'text-amber-400', glow: 'shadow-[0_0_12px_rgba(251,191,36,0.8)]', hoverBg: 'hover:bg-amber-400/5', hoverBorder: 'hover:border-amber-400/30' },
        teal: { bg: 'bg-teal-400/10', border: 'border-teal-400/30', text: 'text-teal-400', glow: 'shadow-[0_0_12px_rgba(45,212,191,0.8)]', hoverBg: 'hover:bg-teal-400/5', hoverBorder: 'hover:border-teal-400/30' },
        blue: { bg: 'bg-blue-400/10', border: 'border-blue-400/30', text: 'text-blue-400', glow: 'shadow-[0_0_12px_rgba(59,130,246,0.8)]', hoverBg: 'hover:bg-blue-400/5', hoverBorder: 'hover:border-blue-400/30' },
        violet: { bg: 'bg-violet-400/10', border: 'border-violet-400/30', text: 'text-violet-400', glow: 'shadow-[0_0_12px_rgba(139,92,246,0.8)]', hoverBg: 'hover:bg-violet-400/5', hoverBorder: 'hover:border-violet-400/30' },
        pink: { bg: 'bg-pink-400/10', border: 'border-pink-400/30', text: 'text-pink-400', glow: 'shadow-[0_0_12px_rgba(236,72,153,0.8)]', hoverBg: 'hover:bg-pink-400/5', hoverBorder: 'hover:border-pink-400/30' },
    };
    const c = colorMap[activeColor] || colorMap.cyan;
    return (
        <div
            onClick={onClick}
            className={`flex items-center gap-4 p-4 rounded-2xl border transition-all cursor-pointer group ${active ? `${c.bg} ${c.border}` : `bg-white/5 border-white/10 ${c.hoverBg} ${c.hoverBorder}`
                }`}
        >
            {Icon && (
                <div className={`p-2 rounded-xl transition-colors ${active ? `bg-[${c.text}]/20 ${c.text}` : `bg-white/5 text-muted group-hover:${c.text}`}`}>
                    <Icon size={16} />
                </div>
            )}
            <div className="flex items-center justify-between flex-1">
                <div>
                    <div className={`text-xs font-black transition-colors ${active ? c.text : `text-white group-hover:${c.text}`}`}>{name}</div>
                    <div className="text-[9px] text-muted font-bold mt-1 line-clamp-1">{desc}</div>
                </div>
                <div className={`h-2.5 w-2.5 rounded-full transition-all ${active ? `bg-current ${c.text} ${c.glow}` : 'bg-white/10 group-hover:bg-white/30'}`} />
            </div>
        </div>
    );
}


function AlertsPanel() {
    const alerts = [
        {
            id: 1,
            symbol: "VVIX",
            name: "CBOE VIX VOLATILITY INDEX",
            condition: "Crosses Above",
            value: 139.00,
            current: 116.02,
            action: "Monitor Volatility Risk",
            active: true,
            highPriority: true
        },
        {
            id: 2,
            symbol: "SPX",
            name: "S&P 500 INDEX",
            condition: "Crosses Below",
            value: 5000.00,
            action: "Hedge Portfolio",
            active: false,
            highPriority: false
        }
    ];

    return (
        <div className="flex-1 overflow-hidden flex flex-col items-center">
            <div className="w-full px-6 py-4 border-b border-white/5 bg-white/5 flex items-center justify-between">
                <div className="flex items-center gap-2">
                    <Bell size={16} className="text-yellow-400" />
                    <h3 className="text-xs font-black uppercase tracking-widest text-white">Active Alerts</h3>
                </div>
                <span className="text-[9px] bg-yellow-500/20 text-yellow-400 px-2 py-0.5 rounded border border-yellow-500/30 font-black uppercase">Live</span>
            </div>

            <div className="w-full flex-1 overflow-y-auto p-4 space-y-3">
                {alerts.map(alert => (
                    <div key={alert.id} className={`p-4 rounded-xl border relative overflow-hidden backdrop-blur-sm ${alert.active ? 'bg-white/5 border-white/10' : 'bg-transparent border-white/5 opacity-50'}`}>
                        {alert.active && alert.highPriority && (
                            <div className="absolute top-0 left-0 w-1 h-full bg-red shadow-[0_0_10px_#ef4444]" />
                        )}
                        {!alert.highPriority && alert.active && (
                            <div className="absolute top-0 left-0 w-1 h-full bg-accent" />
                        )}

                        <div className="flex justify-between items-start mb-2 pl-2">
                            <div>
                                <span className="text-xs font-black uppercase tracking-wider text-white">{alert.symbol}</span>
                                <p className="text-[9px] font-bold text-muted mt-0.5">{alert.name}</p>
                            </div>
                            <div className={`px-2 py-1 rounded text-[9px] font-black tracking-widest uppercase ${alert.active ? 'bg-red/10 text-red border border-red/20' : 'bg-white/5 text-muted'}`}>
                                {alert.condition}
                            </div>
                        </div>

                        <div className="flex items-baseline gap-2 mt-3 pl-2">
                            <span className="text-lg font-mono font-black text-white">{alert.value.toFixed(2)}</span>
                            {alert.current && (
                                <span className="text-[10px] font-mono font-bold text-muted/60">
                                    (Cur: {alert.current.toFixed(2)})
                                </span>
                            )}
                        </div>

                        <div className="mt-3 pl-2 pt-3 border-t border-white/5 flex items-center justify-between">
                            <span className="text-[10px] font-bold text-muted/80">{alert.action}</span>
                            <div className={`h-2 w-2 rounded-full ${alert.active ? 'bg-red animate-pulse shadow-[0_0_8px_#ef4444]' : 'bg-muted'}`} />
                        </div>
                    </div>
                ))}
            </div>

            <div className="w-full p-4 border-t border-white/5 bg-white/5 flex-shrink-0">
                <button className="w-full py-2.5 bg-accent/10 hover:bg-accent/20 text-accent font-black uppercase tracking-widest text-[10px] rounded-lg transition-all border border-accent/20 shadow-[0_0_15px_rgba(59,130,246,0.1)]">
                    + Create Alert
                </button>
            </div>
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
