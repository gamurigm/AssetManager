"use client"

import { useState, useRef, useEffect, useCallback } from "react";
import { Maximize2, Minimize2, Plus, X, ChevronDown, Terminal as TerminalIcon, Loader2 } from "lucide-react";
import { usePortfolio } from "../../context/PortfolioContext";

type Message = { type: 'input' | 'output' | 'error'; text: string };

type Session = {
    id: string;
    history: Message[];
    input: string;
    isExecuting: boolean;
    historyIndex: number;
    pendingCmd: string | null;  // queued while executing
};

export default function OpenBBTerminal() {
    const [isOpen, setIsOpen] = useState(false);
    const [isFullscreen, setIsFullscreen] = useState(false);
    const [sessions, setSessions] = useState<Session[]>([{
        id: '1',
        history: [{ type: 'output', text: 'MMAM Intelligence · OpenBB Engine\nType "help" for available commands.\n' }],
        input: '',
        isExecuting: false,
        historyIndex: -1,
        pendingCmd: null,
    }]);
    const [activeId, setActiveId] = useState('1');
    const [isFocused, setIsFocused] = useState(false);
    const [isDark, setIsDark] = useState(true);
    const [isStellar, setIsStellar] = useState(false);
    const [panelHeight, setPanelHeight] = useState(260);

    const inputRef = useRef<HTMLInputElement>(null);
    const endRef = useRef<HTMLDivElement>(null);
    const inactivityTimer = useRef<NodeJS.Timeout | null>(null);

    const { refreshPortfolio } = usePortfolio();

    // Draggable icon state
    const [termIconPos, setTermIconPos] = useState({ x: 24, y: 24 });
    const [termDragging, setTermDragging] = useState(false);
    const termDragRef = useRef<{ startX: number; startY: number; startPosX: number; startPosY: number; moved: boolean } | null>(null);

    const snapToSafePosition = useCallback(() => {
        setTermIconPos({ x: 24, y: 24 });
    }, []);

    // Drag handler for the floating terminal icon
    useEffect(() => {
        const handleMouseMove = (e: MouseEvent) => {
            if (!termDragging || !termDragRef.current) return;
            const dX = termDragRef.current.startX - e.clientX;
            const dY = termDragRef.current.startY - e.clientY;
            if (Math.abs(dX) > 5 || Math.abs(dY) > 5) termDragRef.current.moved = true;
            const padding = 20;
            const maxRight = window.innerWidth - 80 - padding;
            const maxBottom = window.innerHeight - 80 - padding;
            setTermIconPos({
                x: Math.min(Math.max(padding, termDragRef.current.startPosX + dX), Math.max(padding, maxRight)),
                y: Math.min(Math.max(padding, termDragRef.current.startPosY + dY), Math.max(padding, maxBottom)),
            });
        };
        const handleMouseUp = () => {
            if (!termDragging) return;
            setTermDragging(false);
            if (termDragRef.current && !termDragRef.current.moved) {
                snapToSafePosition();
                setIsOpen(true); setIsStellar(false); resetInactivity();
            }
            termDragRef.current = null;
        };
        if (termDragging) {
            window.addEventListener('mousemove', handleMouseMove);
            window.addEventListener('mouseup', handleMouseUp);
        }
        return () => {
            window.removeEventListener('mousemove', handleMouseMove);
            window.removeEventListener('mouseup', handleMouseUp);
        };
    }, [termDragging]);

    const activeSession = sessions.find(s => s.id === activeId) || sessions[0];
    const lineCount = activeSession.history.length + 1;

    /** Generic updater that applies a partial patch to any session by id */
    const updateSession = useCallback((id: string, update: Partial<Session>) => {
        setSessions(prev => prev.map(s => s.id === id ? { ...s, ...update } : s));
    }, []);

    const updateActiveSession = (update: Partial<Session>) => updateSession(activeId, update);

    // Theme detection
    useEffect(() => {
        const check = () => setIsDark(!document.documentElement.classList.contains('light'));
        check();
        const obs = new MutationObserver(check);
        obs.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
        return () => obs.disconnect();
    }, []);

    // Stellar mode (shrink to glowing dot after inactivity)
    const resetInactivity = useCallback(() => {
        if (inactivityTimer.current) clearTimeout(inactivityTimer.current);
        if (!isOpen && !isStellar) {
            inactivityTimer.current = setTimeout(() => setIsStellar(true), 45000);
        }
    }, [isOpen, isStellar]);

    useEffect(() => {
        resetInactivity();
        const events = ["mousedown", "mousemove", "keypress", "scroll", "touchstart"];
        events.forEach(e => document.addEventListener(e, resetInactivity));
        return () => {
            if (inactivityTimer.current) clearTimeout(inactivityTimer.current);
            events.forEach(e => document.removeEventListener(e, resetInactivity));
        };
    }, [resetInactivity]);

    // Signal layout to adjust content padding
    useEffect(() => {
        const effectiveHeight = isOpen && !isFullscreen ? panelHeight : 0;
        window.dispatchEvent(new CustomEvent('terminal-resize', { detail: { height: effectiveHeight } }));
    }, [isOpen, isFullscreen, panelHeight]);

    // Cleanup: signal 0 on unmount
    useEffect(() => {
        return () => {
            window.dispatchEvent(new CustomEvent('terminal-resize', { detail: { height: 0 } }));
        };
    }, []);

    // ── Agent Bridge: listen for 'terminal-execute' events from chat agents ──
    useEffect(() => {
        const handler = (e: Event) => {
            const cmd = (e as CustomEvent).detail?.command;
            if (!cmd || typeof cmd !== 'string') return;

            // Open terminal if closed, exit stellar mode
            setIsOpen(true);
            setIsStellar(false);

            // Use the active session to inject the command
            setSessions(prev => {
                const sid = activeId;
                const session = prev.find(s => s.id === sid);
                if (!session) return prev;

                // Add a visual marker showing this was agent-dispatched
                const agentMarker: Message = { type: 'output', text: '🤖 Agent executed:' };
                const newHistory = [...session.history, agentMarker];

                // If already executing, queue it
                if (session.isExecuting) {
                    return prev.map(s => s.id === sid
                        ? { ...s, history: newHistory, pendingCmd: cmd }
                        : s
                    );
                }

                // Otherwise execute immediately via runCommand (we'll trigger it via state)
                return prev.map(s => s.id === sid
                    ? { ...s, history: newHistory, pendingCmd: cmd }
                    : s
                );
            });
        };

        window.addEventListener('terminal-execute', handler);
        return () => window.removeEventListener('terminal-execute', handler);
    }, [activeId]);

    useEffect(() => {
        if (isOpen && inputRef.current) inputRef.current.focus();
        if (endRef.current) endRef.current.scrollIntoView({ behavior: 'smooth' });
    }, [activeSession?.history, isOpen, activeId]);

    const runCommand = useCallback(async (sessionId: string, cmd: string, baseHistory: Message[]) => {
        const newHistory: Message[] = [...baseHistory, { type: 'input', text: cmd }];
        updateSession(sessionId, { history: newHistory, input: '', historyIndex: -1, isExecuting: true, pendingCmd: null });

        if (cmd.toLowerCase() === 'clear') {
            updateSession(sessionId, { history: [], isExecuting: false });
            return;
        }

        try {
            const response = await fetch('http://127.0.0.1:8282/openbb/cli', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command: cmd })
            });
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            const data = await response.json();
            if (data.type === 'chart_window' && data.html) {
                const win = window.open('', '_blank', 'width=1440,height=820,menubar=no,toolbar=no,location=no,status=no');
                if (win) { win.document.open(); win.document.write(data.html); win.document.close(); }
                updateSession(sessionId, {
                    history: [...newHistory, { type: 'output', text: '📊 Chart opened in new window.' }],
                    isExecuting: false,
                });
                window.dispatchEvent(new CustomEvent('terminal-success', { detail: { command: cmd } }));
            } else {
                updateSession(sessionId, {
                    history: [...newHistory, { type: data.type === 'error' ? 'error' : 'output', text: data.output ?? data.error ?? 'OK' }],
                    isExecuting: false,
                });
                if (data.type === 'error') {
                    window.dispatchEvent(new CustomEvent('terminal-error', { detail: { command: cmd, error: data.error ?? data.output ?? 'Unknown error' } }));
                } else {
                    window.dispatchEvent(new CustomEvent('terminal-success', { detail: { command: cmd } }));
                }
                // If liquidation completed successfully, refresh the frontend portfolio state
                if (data.output && data.output.includes('LIQUIDATION COMPLETE')) {
                    refreshPortfolio();
                }
            }
        } catch (error: any) {
            updateSession(sessionId, {
                history: [...newHistory, { type: 'error', text: `Connection failed: ${error.message}` }],
                isExecuting: false,
            });
        }
    }, [updateSession]);

    // When a session finishes, auto-run pending command if queued
    useEffect(() => {
        sessions.forEach(s => {
            if (!s.isExecuting && s.pendingCmd) {
                runCommand(s.id, s.pendingCmd, s.history);
            }
        });
    }, [sessions, runCommand]);

    const handleCommand = async (e: React.FormEvent) => {
        e.preventDefault();
        const sessionId = activeId;
        const session = sessions.find(s => s.id === sessionId)!;
        const cmd = session.input.trim();
        if (!cmd) return;

        if (session.isExecuting) {
            // Queue the command — will run automatically when current finishes
            updateSession(sessionId, { pendingCmd: cmd, input: '' });
            return;
        }
        await runCommand(sessionId, cmd, session.history);
    };

    // Tab-completion candidates (top-level OpenBB namespaces)
    const TAB_COMPLETIONS = [
        // ── Core aliases ──────────────────────────────────────────────────
        'quote --symbol ', 'historical --symbol ', 'profile --symbol ',
        'search --query ', 'news', 'income --symbol ', 'balance --symbol ',
        'calendar', 'cpi', 'gdp', 'treasury', 'options --symbol ',
        // ── Equity charts ─────────────────────────────────────────────────
        'equity price historical --symbol ', 'equity price performance --symbol ',
        'equity historical_market_cap --symbol ',
        // ── Crypto charts ─────────────────────────────────────────────────
        'crypto price historical --symbol BTC-USD --chart true',
        'crypto price historical --symbol ETH-USD --chart true',
        'crypto price historical --symbol ',
        // ── Currency / Forex ──────────────────────────────────────────────
        'currency price historical --symbol EURUSD=X --chart true',
        'currency price historical --symbol ',
        // ── ETF ───────────────────────────────────────────────────────────
        'etf historical --symbol SPY --chart true',
        'etf historical --symbol ', 'etf holdings --symbol ', 'etf price_performance --symbol ',
        // ── Derivatives ───────────────────────────────────────────────────
        'derivatives futures curve --symbol CL --chart true',
        'derivatives futures historical --symbol ',
        'derivatives options surface --symbol SPY --chart true',
        // ── Fixed Income ──────────────────────────────────────────────────
        'fixedincome government yield_curve --chart true',
        'fixedincome government yield_curve --date ',
        // ── Index ─────────────────────────────────────────────────────────
        'index price historical --symbol ^GSPC --chart true',
        'index price historical --symbol ^NDX --chart true',
        'index price historical --symbol ',
        // ── Economy / Macro ───────────────────────────────────────────────
        'economy fred_series --symbol GDP --chart true',
        'economy fred_series --symbol CPIAUCSL --chart true',
        'economy fred_series --symbol FEDFUNDS --chart true',
        'economy fred_series --symbol ',
        'economy shipping chokepoint_info --chart true',
        'economy shipping port_info --chart true',
        'economy survey bls_series --symbol ',
        // ── Technical ─────────────────────────────────────────────────────
        'technical macd --symbol ', 'technical rsi --symbol ',
        'technical ema --symbol ', 'technical sma --symbol ',
        'technical wma --symbol ', 'technical hma --symbol ', 'technical zlma --symbol ',
        'technical adx --symbol ', 'technical aroon --symbol ',
        'technical cones --symbol ',
        'technical relative_rotation --symbol ',
        // ── System ────────────────────────────────────────────────────────
        'help', 'clear',
    ];

    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        const inputs = activeSession.history.filter(m => m.type === 'input');
        const val = activeSession.input;

        // ── History navigation ────────────────────────────────────────
        if (e.key === 'ArrowUp') {
            e.preventDefault();
            if (inputs.length === 0) return;
            const newIndex = activeSession.historyIndex === -1 ? inputs.length - 1 : Math.max(0, activeSession.historyIndex - 1);
            updateActiveSession({ historyIndex: newIndex, input: inputs[newIndex].text });
            // Move caret to end after state update
            setTimeout(() => { const el = inputRef.current; if (el) el.setSelectionRange(el.value.length, el.value.length); }, 0);
            return;
        }
        if (e.key === 'ArrowDown') {
            e.preventDefault();
            if (activeSession.historyIndex === -1) return;
            const newIndex = activeSession.historyIndex + 1;
            if (newIndex >= inputs.length) {
                updateActiveSession({ historyIndex: -1, input: '' });
            } else {
                updateActiveSession({ historyIndex: newIndex, input: inputs[newIndex].text });
                setTimeout(() => { const el = inputRef.current; if (el) el.setSelectionRange(el.value.length, el.value.length); }, 0);
            }
            return;
        }

        // ── Tab completion ────────────────────────────────────────────
        if (e.key === 'Tab') {
            e.preventDefault();
            const trimmed = val.trimStart().toLowerCase();
            const matches = TAB_COMPLETIONS.filter(c => c.startsWith(trimmed));
            if (matches.length === 1) {
                updateActiveSession({ input: matches[0] });
            } else if (matches.length > 1) {
                // Show matches as output hint
                updateSession(activeId, {
                    history: [...activeSession.history, { type: 'output', text: matches.join('   ') }],
                });
            }
            return;
        }

        // ── Ctrl shortcuts ────────────────────────────────────────────
        if (e.ctrlKey) {
            // Ctrl+V — let browser handle paste natively
            if (e.key === 'v' || e.key === 'V') return;
            // Ctrl+A — let browser handle (select all in input)
            if (e.key === 'a' || e.key === 'A') return;
            if (e.key === 'l' || e.key === 'L') {
                e.preventDefault();
                updateActiveSession({ history: [], input: val });
                return;
            }
            if (e.key === 'c' || e.key === 'C') {
                // Only intercept Ctrl+C when there's nothing selected (otherwise browser copies selection)
                if (window.getSelection()?.toString()) return;
                e.preventDefault();
                if (activeSession.isExecuting) {
                    updateActiveSession({
                        isExecuting: false, pendingCmd: null,
                        history: [...activeSession.history, { type: 'error', text: '^C' }]
                    });
                } else {
                    updateActiveSession({
                        input: '',
                        history: val ? [...activeSession.history, { type: 'input', text: val + '^C' }] : activeSession.history
                    });
                }
                return;
            }
            if (e.key === 'u' || e.key === 'U') {
                e.preventDefault();
                updateActiveSession({ input: '' });
                return;
            }
        }

        // ── Escape — clear input ──────────────────────────────────────
        if (e.key === 'Escape') {
            e.preventDefault();
            updateActiveSession({ input: '', historyIndex: -1 });
            return;
        }
    };

    const newSession = () => {
        const id = Math.random().toString(36).substring(7);
        setSessions(prev => [...prev, {
            id,
            history: [{ type: 'output', text: 'Buffer initialized.' }],
            input: '',
            isExecuting: false,
            historyIndex: -1,
            pendingCmd: null,
        }]);
        setActiveId(id);
    };

    const closeSession = (e: React.MouseEvent, id: string) => {
        e.stopPropagation();
        if (sessions.length === 1) { setIsOpen(false); return; }
        const rest = sessions.filter(s => s.id !== id);
        setSessions(rest);
        if (activeId === id) setActiveId(rest[rest.length - 1].id);
    };

    // ─── Theme Tokens ─────────────────────────────────────────────────
    const t = isDark ? {
        // High-contrast, glowing cyberpunk aesthetic
        bg: 'bg-zinc-950/80',
        bgSolid: 'bg-black/90',
        bgTab: 'bg-zinc-900/60',
        bgTabActive: 'bg-cyan-950/30',
        border: 'border-cyan-500/30',
        borderTab: 'border-cyan-900/40',
        text: 'text-zinc-100',
        textBright: 'text-white',
        textDim: 'text-cyan-500/60',
        textInput: 'text-cyan-300 drop-shadow-[0_0_5px_rgba(103,232,249,0.4)]',
        textCmd: 'text-cyan-400 font-bold',
        textError: 'text-rose-400 font-bold drop-shadow-[0_0_8px_rgba(244,63,94,0.4)]',
        textOutput: 'text-zinc-200',
        gutter: 'text-cyan-900/70',
        gutterActive: 'text-cyan-400 bg-cyan-950/20 shadow-[inset_-2px_0_0_0_rgba(34,211,238,0.5)]',
        gutterBg: 'bg-zinc-950/40',
        modeNormal: 'bg-cyan-600 text-white font-bold',
        modeInsert: 'bg-teal-400 text-black font-bold shadow-[0_0_15px_rgba(45,212,191,0.5)]',
        statusBg: 'bg-zinc-900/90 border-t border-cyan-900/30',
        statusBg2: 'bg-cyan-950/80 text-cyan-200',
        statusBg3: 'bg-black/90',
        cursor: 'bg-cyan-400',
        cursorBorder: 'border-cyan-400',
        accentGlow: 'shadow-[0_0_15px_rgba(34,211,238,0.6)]',
        warn: 'text-amber-400 drop-shadow-[0_0_8px_rgba(251,191,36,0.6)]',
        warnDot: 'bg-amber-400 shadow-[0_0_12px_rgba(251,191,36,0.8)]',
        panelBlur: 'backdrop-blur-3xl',
        tabIndicator: 'bg-cyan-400',
    } : {
        bg: 'bg-[#eff1f5]/80',
        bgSolid: 'bg-[#e6e9ef]/90',
        bgTab: 'bg-[#e6e9ef]/60',
        bgTabActive: 'bg-teal-50/80',
        border: 'border-teal-500/30',
        borderTab: 'border-[#ccd0da]/60',
        text: 'text-slate-800',
        textBright: 'text-black',
        textDim: 'text-slate-500',
        textInput: 'text-teal-700 font-bold',
        textCmd: 'text-teal-600 font-bold',
        textError: 'text-red-600 font-bold',
        textOutput: 'text-slate-800',
        gutter: 'text-slate-400',
        gutterActive: 'text-teal-600 font-bold border-r-2 border-teal-500',
        gutterBg: 'bg-slate-100/50',
        modeNormal: 'bg-teal-600 text-white',
        modeInsert: 'bg-emerald-500 text-white shadow-sm',
        statusBg: 'bg-slate-200/90',
        statusBg2: 'bg-slate-300',
        statusBg3: 'bg-slate-100/90',
        cursor: 'bg-teal-600',
        cursorBorder: 'border-teal-600',
        accentGlow: 'shadow-[0_0_12px_rgba(20,184,166,0.3)]',
        warn: 'text-[#df8e1d]',
        warnDot: 'bg-[#df8e1d]',
        panelBlur: 'backdrop-blur-3xl',
        tabIndicator: 'bg-teal-500',
    };

    // ─── Stellar Mode: Tiny glowing orb ───────────────────────────────
    if (isStellar && !isOpen) {
        return (
            <button
                onClick={() => { setIsStellar(false); snapToSafePosition(); setIsOpen(true); resetInactivity(); }}
                className="fixed z-[9999] cursor-pointer group flex items-center justify-center transition-transform hover:scale-150"
                style={{ top: 20, right: 90 }}
            >
                <div className={`w-3 h-3 rounded-full z-10 animate-pulse shadow-[0_0_20px_2px] ${isDark ? 'bg-cyan-400 shadow-cyan-500/80' : 'bg-teal-500 shadow-teal-500/60'}`} />
                <div className={`absolute inset-0 rounded-full animate-ping [animation-duration:3s] ${isDark ? 'bg-cyan-500/30' : 'bg-teal-500/30'}`} />
            </button>
        );
    }

    // ─── Closed: Draggable icon button ─────
    if (!isOpen) {
        return (
            <div
                className={`fixed z-[9999] transition-all ease-[cubic-bezier(0.2,0.8,0.2,1)] duration-700 ${termDragging ? 'select-none transition-none' : ''}`}
                style={{ right: termIconPos.x, bottom: termIconPos.y }}
            >
                <button
                    onMouseDown={(e) => {
                        setTermDragging(true);
                        termDragRef.current = { startX: e.clientX, startY: e.clientY, startPosX: termIconPos.x, startPosY: termIconPos.y, moved: false };
                    }}
                    className={`h-14 w-14 flex items-center justify-center transition-all duration-500 group overflow-hidden relative shadow-2xl
                        ${isDark
                            ? 'bg-zinc-950 border-2 border-cyan-500/50 rounded-[22px] ring-4 ring-cyan-500/10 shadow-[0_0_30px_-5px_#22d3ee80]'
                            : 'bg-gradient-to-br from-teal-500 via-cyan-600 to-teal-700 rounded-[22px] shadow-[0_15px_35px_-5px_rgba(20,184,166,0.5)] border border-white/20'
                        }
                        ${termDragging ? 'cursor-grabbing scale-110' : 'cursor-grab'}`}
                >
                    <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000" />
                    {!isDark && <div className="absolute inset-0 rounded-full bg-teal-400/20 animate-ping [animation-duration:3s]" />}
                    <div className={`absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity ${isDark ? 'bg-cyan-600/10' : 'bg-white/10'}`} />
                    <TerminalIcon size={22} className="text-white drop-shadow-[0_2px_4px_rgba(0,0,0,0.3)] relative z-10" />
                </button>
            </div>
        );
    }

    // ─── Open: Embedded panel at bottom (does NOT overlap main content) ─
    const containerBase = isFullscreen
        ? `fixed inset-0 z-[200] ${t.bg} ${t.panelBlur} flex flex-col p-6 transition-all duration-500`
        : `fixed bottom-0 left-[68px] right-0 z-[150] flex flex-col transition-all duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] ${t.bg} ${t.panelBlur} border-t ${t.border}`;

    return (
        <div
            className={containerBase}
            style={!isFullscreen ? { height: `${panelHeight}px` } : {}}
        >
            {/* Resizer Handle */}
            {!isFullscreen && (
                <div
                    className={`absolute top-0 left-0 w-full h-3 cursor-ns-resize z-20 flex items-center justify-center group transition-colors ${isDark ? 'hover:bg-cyan-500/20' : 'hover:bg-teal-500/15'}`}
                    title="Drag to resize"
                    onMouseDown={(e) => {
                        e.preventDefault();
                        const startY = e.clientY;
                        const startH = panelHeight;
                        const move = (ev: MouseEvent) => {
                            const next = Math.max(120, Math.min(Math.floor(window.innerHeight * 0.92), startH + startY - ev.clientY));
                            setPanelHeight(next);
                        };
                        const up = () => { window.removeEventListener('mousemove', move); window.removeEventListener('mouseup', up); };
                        window.addEventListener('mousemove', move);
                        window.addEventListener('mouseup', up);
                    }}
                >
                    <div className={`w-16 h-1 rounded-full transition-all duration-150 group-hover:w-28 group-active:w-36 ${isDark ? 'bg-cyan-500/40 group-hover:bg-cyan-400/70' : 'bg-teal-500/30 group-hover:bg-teal-500/60'}`} />
                </div>
            )}

            <div className={`flex flex-col h-full w-full font-mono ${isFullscreen ? `border ${t.border} rounded-xl overflow-hidden` : ''}`} data-terminal-panel>
                {/* Tab Bar */}
                <div className={`flex items-center justify-between ${t.bgTab} shrink-0 border-b ${t.borderTab} select-none`}>
                    <div className="flex items-center">
                        {sessions.map((s, i) => (
                            <div
                                key={s.id}
                                onClick={(e) => { e.stopPropagation(); setActiveId(s.id); }}
                                className={`group flex items-center gap-3 px-6 py-3 text-[12px] tracking-wider cursor-pointer transition-all border-r ${t.borderTab} relative ${activeId === s.id ? `${t.textCmd} ${t.bgTabActive} font-bold shadow-inner` : `${t.textDim} ${isDark ? 'hover:bg-zinc-800' : 'hover:bg-slate-200'}`}`}
                            >
                                {activeId === s.id && <div className={`absolute bottom-0 left-0 w-full h-[2px] ${t.tabIndicator} ${t.accentGlow}`} />}
                                <span>{i + 1}:openbb</span>
                                {/* Per-tab executing spinner visible on inactive tabs */}
                                {s.isExecuting && s.id !== activeId && (
                                    <Loader2 size={10} className={`animate-spin ${t.warn}`} />
                                )}
                                {sessions.length > 1 && (
                                    <button onClick={(e) => closeSession(e, s.id)} className={`opacity-0 group-hover:opacity-100 p-0.5 ${t.textError} rounded transition-all`}>
                                        <X size={10} />
                                    </button>
                                )}
                            </div>
                        ))}
                        <button onClick={(e) => { e.stopPropagation(); newSession(); }} className={`px-5 py-2.5 ${t.textDim} transition-colors border-r ${t.borderTab} ${isDark ? 'hover:text-cyan-400 hover:bg-zinc-800/50' : 'hover:text-teal-600 hover:bg-slate-200/50'}`}>
                            <Plus size={14} />
                        </button>
                    </div>

                    <div className={`flex items-center gap-5 px-5 ${t.textDim}`}>
                        <div className="hidden sm:flex items-center gap-4 mr-4 text-[10px] font-bold tracking-[0.2em] uppercase opacity-70">
                            <span>{isFullscreen ? 'fullscreen' : 'split'}</span>
                            <span>{sessions.length} buf</span>
                        </div>
                        <div className="flex items-center gap-1.5">
                            <button onClick={(e) => { e.stopPropagation(); setIsFullscreen(!isFullscreen); }}
                                className={`p-2 rounded transition-colors ${isDark ? 'hover:text-cyan-400 hover:bg-zinc-800' : 'hover:text-teal-600 hover:bg-slate-300'}`}>
                                {isFullscreen ? <Minimize2 size={15} /> : <Maximize2 size={15} />}
                            </button>
                            <button onClick={(e) => { e.stopPropagation(); setIsOpen(false); setIsFullscreen(false); }}
                                className={`p-2 rounded transition-colors ${isDark ? 'hover:text-rose-400 hover:bg-zinc-800' : 'hover:text-red-500 hover:bg-slate-300'}`}>
                                <ChevronDown size={17} />
                            </button>
                        </div>
                    </div>
                </div>

                {/* Buffer Area */}
                <div className="flex-1 flex min-h-0 overflow-hidden">
                    <div className={`w-12 ${t.gutterBg} border-r ${t.borderTab} flex flex-col items-end py-3 px-2 ${t.gutter} text-xs select-none overflow-hidden`}>
                        {activeSession.history.map((_, i) => (
                            <div key={i} className={`leading-[1.85] ${i === activeSession.history.length - 1 ? t.gutterActive + ' font-bold' : ''}`}>{i + 1}</div>
                        ))}
                        {Array.from({ length: 8 }).map((_, i) => (
                            <div key={`t${i}`} className={`${t.gutter} font-bold leading-[1.85]`}>~</div>
                        ))}
                    </div>

                    <div className="flex-1 flex flex-col overflow-hidden relative">
                        <div
                            className={`flex-1 overflow-y-auto py-4 px-5 text-[14px] leading-relaxed tracking-wide antialiased ${t.textOutput} select-text cursor-text`}
                            onClick={() => {
                                // Re-focus input only when clicking without a text selection
                                if (!window.getSelection()?.toString()) {
                                    inputRef.current?.focus();
                                }
                            }}
                        >
                            {activeSession.history.map((line, i) => (
                                <div key={i} className={`whitespace-pre-wrap ${line.type === 'input' ? `${t.textCmd} font-semibold` : line.type === 'error' ? t.textError : t.textOutput}`}>
                                    {line.type === 'input' && <span className={`${t.textCmd} opacity-50 mr-3`}>:</span>}
                                    {line.text}
                                </div>
                            ))}
                            {activeSession.isExecuting && (
                                <div className={`flex items-center gap-3 ${t.warn} font-bold tracking-[0.15em] text-[10px] uppercase py-3`}>
                                    <span className={`w-2 h-2 ${t.warnDot} rounded-full animate-pulse`} />
                                    -- executing --
                                </div>
                            )}
                            <div ref={endRef} />
                        </div>

                        {/* ── Command Input (BOTTOM) ─────────────────────────────── */}
                        <div className={`h-11 border-t-2 ${isDark ? 'border-cyan-500/40 shadow-[0_-5px_15px_rgba(6,182,212,0.1)]' : 'border-teal-500/30'} shrink-0 flex items-center px-5 gap-3 ${isDark ? 'bg-black/80' : 'bg-slate-200/80'} backdrop-blur-md`}>
                            {/* Prompt glyph */}
                            <span className={`shrink-0 select-none font-bold text-[16px] leading-none ${isFocused ? t.textCmd : t.textDim}`}>❯</span>
                            <form onSubmit={handleCommand} className="flex-1 flex items-center h-full min-w-0">
                                <input
                                    ref={inputRef}
                                    type="text"
                                    value={activeSession.input}
                                    onChange={e => updateActiveSession({ input: e.target.value, historyIndex: -1 })}
                                    onKeyDown={handleKeyDown}
                                    onFocus={() => setIsFocused(true)}
                                    onBlur={(e) => {
                                        const panel = e.currentTarget.closest('[data-terminal-panel]');
                                        if (panel && panel.contains(e.relatedTarget as Node)) return;
                                        setIsFocused(false);
                                    }}
                                    onPaste={(e) => {
                                        const text = e.clipboardData.getData('text');
                                        if (text.includes('\n')) {
                                            e.preventDefault();
                                            const cleaned = text.replace(/\r?\n/g, ' ').trim();
                                            const el = e.currentTarget;
                                            const start = el.selectionStart ?? el.value.length;
                                            const end = el.selectionEnd ?? el.value.length;
                                            const next = el.value.slice(0, start) + cleaned + el.value.slice(end);
                                            updateActiveSession({ input: next, historyIndex: -1 });
                                        }
                                    }}
                                    className={`w-full bg-transparent border-none outline-none ${t.textInput} focus:ring-0 py-0 px-0 tracking-wider text-[15px] font-semibold antialiased`}
                                    style={{ caretColor: isDark ? '#22d3ee' : '#0f766e' }}
                                    spellCheck={false}
                                    autoComplete="off"
                                    autoCorrect="off"
                                    autoCapitalize="off"
                                    placeholder={activeSession.isExecuting && activeSession.pendingCmd
                                        ? `queued: ${activeSession.pendingCmd}`
                                        : activeSession.isExecuting ? 'executing…' : ''}
                                />
                            </form>
                            {activeSession.isExecuting && (
                                <div className={`shrink-0 flex items-center gap-1.5 text-[9px] font-bold tracking-widest uppercase ${t.warn}`}>
                                    <Loader2 size={10} className="animate-spin" />
                                    {activeSession.pendingCmd ? 'queued' : 'running'}
                                </div>
                            )}
                            <span className={`shrink-0 text-[9px] select-none ${t.textDim} hidden sm:block`}>
                                ↑↓ history · Tab · Ctrl+L · Ctrl+C
                            </span>
                        </div>

                        {/* Statusline */}
                        <div className="flex text-[11px] font-bold select-none h-7 shrink-0 tracking-wide">
                            <div className={`${isFocused ? t.modeInsert : t.modeNormal} px-4 flex items-center tracking-widest leading-none`}>
                                {isFocused ? 'INSERT' : 'NORMAL'}
                            </div>
                            <div className={`${t.statusBg} ${t.text} px-5 flex items-center font-medium gap-2 shadow-inner`}>
                                <TerminalIcon size={12} className="opacity-70" /> openbb.cli
                            </div>
                            <div className={`flex-1 ${t.statusBg}`} />
                            <div className={`${t.statusBg3} ${t.textDim} px-4 flex items-center shadow-inner`}>utf-8</div>
                            <div className={`${t.statusBg2} ${t.textBright} px-5 flex items-center tracking-tight shadow-inner`}>{lineCount}:1</div>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    );
}
