"use client"

import { useState, useRef, useEffect, useCallback } from "react";
import { Maximize2, Minimize2, Plus, X, ChevronDown, Terminal as TerminalIcon, Loader2 } from "lucide-react";

type Message = { type: 'input' | 'output' | 'error', text: string };

type Session = {
    id: string;
    history: Message[];
    input: string;
    isExecuting: boolean;
    historyIndex: number;
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
    }]);
    const [activeId, setActiveId] = useState('1');
    const [isFocused, setIsFocused] = useState(false);
    const [isDark, setIsDark] = useState(true);
    const [isStellar, setIsStellar] = useState(false);
    const [panelHeight, setPanelHeight] = useState(320);

    const inputRef = useRef<HTMLInputElement>(null);
    const endRef = useRef<HTMLDivElement>(null);
    const inactivityTimer = useRef<NodeJS.Timeout | null>(null);

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

    useEffect(() => {
        if (isOpen && inputRef.current) inputRef.current.focus();
        if (endRef.current) endRef.current.scrollIntoView({ behavior: 'smooth' });
    }, [activeSession?.history, isOpen, activeId]);

    const handleCommand = async (e: React.FormEvent) => {
        e.preventDefault();
        // Capture the session id at command-dispatch time so async closures
        // always write back to the correct tab even if the user switches.
        const sessionId = activeId;
        const session = sessions.find(s => s.id === sessionId)!;
        const cmd = session.input.trim();
        if (!cmd || session.isExecuting) return;

        const newHistory: Message[] = [...session.history, { type: 'input', text: cmd }];
        updateSession(sessionId, { history: newHistory, input: '', historyIndex: -1, isExecuting: true });

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
            updateSession(sessionId, {
                history: [...newHistory, { type: data.type === 'error' ? 'error' : 'output', text: data.output }],
                isExecuting: false,
            });
        } catch (error: any) {
            updateSession(sessionId, {
                history: [...newHistory, { type: 'error', text: `Connection failed: ${error.message}` }],
                isExecuting: false,
            });
        }
    };

    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        const inputs = activeSession.history.filter(m => m.type === 'input');
        if (e.key === 'ArrowUp') {
            e.preventDefault();
            if (inputs.length === 0) return;
            const newIndex = activeSession.historyIndex === -1 ? inputs.length - 1 : Math.max(0, activeSession.historyIndex - 1);
            updateActiveSession({ historyIndex: newIndex, input: inputs[newIndex].text });
        } else if (e.key === 'ArrowDown') {
            e.preventDefault();
            if (activeSession.historyIndex === -1) return;
            const newIndex = activeSession.historyIndex + 1;
            if (newIndex >= inputs.length) {
                updateActiveSession({ historyIndex: -1, input: '' });
            } else {
                updateActiveSession({ historyIndex: newIndex, input: inputs[newIndex].text });
            }
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
        bg: 'bg-[#1a1b26]/50',
        bgSolid: 'bg-[#16161e]/60',
        bgTab: 'bg-[#16161e]/50',
        bgTabActive: 'bg-[#1a1b26]/80',
        border: 'border-[#292e42]/40',
        borderTab: 'border-[#292e42]/30',
        text: 'text-[#a9b1d6]',
        textBright: 'text-[#c0caf5]',
        textDim: 'text-[#565f89]',
        textInput: 'text-[#c0caf5]',
        textCmd: 'text-[#7aa2f7]',
        textError: 'text-[#f7768e]',
        textOutput: 'text-[#a9b1d6]',
        gutter: 'text-[#3b4261]',
        gutterActive: 'text-[#7aa2f7]',
        gutterBg: 'bg-[#16161e]/30',
        modeNormal: 'bg-[#7aa2f7] text-[#1a1b26]',
        modeInsert: 'bg-[#9ece6a] text-[#1a1b26]',
        statusBg: 'bg-[#292e42]/80',
        statusBg2: 'bg-[#3b4261]',
        statusBg3: 'bg-[#16161e]/80',
        cursor: 'bg-[#c0caf5]',
        cursorBorder: 'border-[#c0caf5]',
        accentGlow: 'shadow-[0_0_12px_#7aa2f7]',
        warn: 'text-[#e0af68]',
        warnDot: 'bg-[#e0af68]',
        panelBlur: 'backdrop-blur-2xl',
        tabIndicator: 'bg-[#7aa2f7]',
    } : {
        bg: 'bg-[#eff1f5]/60',
        bgSolid: 'bg-[#e6e9ef]/70',
        bgTab: 'bg-[#e6e9ef]/50',
        bgTabActive: 'bg-[#f4f5f8]/90',
        border: 'border-[#ccd0da]/60',
        borderTab: 'border-[#ccd0da]/40',
        text: 'text-[#4c4f69]',
        textBright: 'text-[#1e1e2e]',
        textDim: 'text-[#9ca0b0]',
        textInput: 'text-[#1e1e2e]',
        textCmd: 'text-[#1e66f5]',
        textError: 'text-[#d20f39]',
        textOutput: 'text-[#4c4f69]',
        gutter: 'text-[#bcc0cc]',
        gutterActive: 'text-[#1e66f5]',
        gutterBg: 'bg-[#e6e9ef]/40',
        modeNormal: 'bg-[#1e66f5] text-white',
        modeInsert: 'bg-[#40a02b] text-white',
        statusBg: 'bg-[#dce0e8]/80',
        statusBg2: 'bg-[#ccd0da]',
        statusBg3: 'bg-[#e6e9ef]/80',
        cursor: 'bg-[#4c4f69]',
        cursorBorder: 'border-[#4c4f69]',
        accentGlow: 'shadow-[0_0_12px_rgba(30,102,245,0.3)]',
        warn: 'text-[#df8e1d]',
        warnDot: 'bg-[#df8e1d]',
        panelBlur: 'backdrop-blur-2xl',
        tabIndicator: 'bg-[#1e66f5]',
    };

    // ─── Stellar Mode: Tiny glowing orb ───────────────────────────────
    if (isStellar && !isOpen) {
        return (
            <button
                onClick={() => { setIsStellar(false); setIsOpen(true); resetInactivity(); }}
                className="fixed z-[9999] cursor-pointer group flex items-center justify-center transition-transform hover:scale-150"
                style={{ top: 20, right: 90 }}
            >
                <div className={`w-3 h-3 rounded-full z-10 animate-pulse shadow-[0_0_20px_2px] ${isDark ? 'bg-cyan-400 shadow-cyan-500/80' : 'bg-teal-500 shadow-teal-500/60'}`} />
                <div className={`absolute inset-0 rounded-full animate-ping [animation-duration:3s] ${isDark ? 'bg-cyan-500/30' : 'bg-teal-500/30'}`} />
            </button>
        );
    }

    // ─── Closed: Icon button (aligned top-right, next to chat) ─────
    if (!isOpen) {
        return (
            <button
                onClick={() => { setIsOpen(true); setIsStellar(false); resetInactivity(); }}
                className={`fixed z-[9999] h-12 w-12 flex items-center justify-center transition-all duration-500 group overflow-hidden relative shadow-2xl cursor-pointer
                    ${isDark
                        ? 'bg-zinc-950 border-2 border-cyan-500/50 rounded-[18px] ring-4 ring-cyan-500/10 shadow-[0_0_30px_-5px_#22d3ee80]'
                        : 'bg-gradient-to-br from-teal-500 via-cyan-600 to-teal-700 rounded-[18px] shadow-[0_15px_35px_-5px_rgba(20,184,166,0.5)] border border-white/20'
                    }`}
                style={{ top: 14, right: 86 }}
            >
                <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000" />
                {!isDark && <div className="absolute inset-0 rounded-full bg-teal-400/20 animate-ping [animation-duration:3s]" />}
                <div className={`absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity ${isDark ? 'bg-cyan-600/10' : 'bg-white/10'}`} />
                <TerminalIcon size={20} className="text-white drop-shadow-[0_2px_4px_rgba(0,0,0,0.3)] relative z-10" />
            </button>
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
            onMouseDown={() => inputRef.current?.focus()}
        >
            {/* Resizer */}
            {!isFullscreen && (
                <div
                    className={`absolute top-0 left-0 w-full h-1.5 cursor-ns-resize z-10 transition-colors ${isDark ? 'hover:bg-[#7aa2f7]/30' : 'hover:bg-[#1e66f5]/20'}`}
                    onMouseDown={(e) => {
                        e.preventDefault();
                        const startY = e.clientY;
                        const startH = panelHeight;
                        const move = (ev: MouseEvent) => setPanelHeight(Math.max(180, Math.min(window.innerHeight - 100, startH + startY - ev.clientY)));
                        const up = () => { window.removeEventListener('mousemove', move); window.removeEventListener('mouseup', up); };
                        window.addEventListener('mousemove', move);
                        window.addEventListener('mouseup', up);
                    }}
                />
            )}

            <div className={`flex flex-col h-full w-full font-mono ${isFullscreen ? `border ${t.border} rounded-xl overflow-hidden` : ''}`}>
                {/* Tab Bar */}
                <div className={`flex items-center justify-between ${t.bgTab} shrink-0 border-b ${t.borderTab} select-none`}>
                    <div className="flex items-center">
                        {sessions.map((s, i) => (
                            <div
                                key={s.id}
                                onClick={(e) => { e.stopPropagation(); setActiveId(s.id); }}
                                className={`group flex items-center gap-2.5 px-6 py-2.5 text-[11px] tracking-wide cursor-pointer transition-all border-r ${t.borderTab} relative ${activeId === s.id ? `${t.textCmd} ${t.bgTabActive} font-bold` : `${t.textDim} ${isDark ? 'hover:bg-[#1a1b26]/30' : 'hover:bg-[#dce0e8]'}`}`}
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
                        <button onClick={(e) => { e.stopPropagation(); newSession(); }} className={`px-5 py-2.5 ${t.textDim} transition-colors border-r ${t.borderTab} ${isDark ? 'hover:text-[#7aa2f7]' : 'hover:text-[#1e66f5]'}`}>
                            <Plus size={14} />
                        </button>
                    </div>

                    <div className={`flex items-center gap-5 px-5 ${t.textDim}`}>
                        <div className="hidden sm:flex items-center gap-4 mr-4 text-[9px] font-bold tracking-[0.15em] uppercase opacity-50">
                            <span>{isFullscreen ? 'fullscreen' : 'split'}</span>
                            <span>{sessions.length} buf</span>
                        </div>
                        <div className="flex items-center gap-1.5">
                            <button onClick={(e) => { e.stopPropagation(); setIsFullscreen(!isFullscreen); }}
                                className={`p-2 rounded transition-colors ${isDark ? 'hover:text-[#7aa2f7] hover:bg-[#292e42]' : 'hover:text-[#1e66f5] hover:bg-[#dce0e8]'}`}>
                                {isFullscreen ? <Minimize2 size={14} /> : <Maximize2 size={14} />}
                            </button>
                            <button onClick={(e) => { e.stopPropagation(); setIsOpen(false); setIsFullscreen(false); }}
                                className={`p-2 rounded transition-colors ${isDark ? 'hover:text-[#f7768e] hover:bg-[#292e42]' : 'hover:text-[#d20f39] hover:bg-[#dce0e8]'}`}>
                                <ChevronDown size={16} />
                            </button>
                        </div>
                    </div>
                </div>

                {/* Buffer Area */}
                <div className="flex-1 flex min-h-0 overflow-hidden">
                    <div className={`w-14 ${t.gutterBg} border-r ${t.borderTab} flex flex-col items-end py-5 px-3 ${t.gutter} text-xs select-none overflow-hidden`}>
                        {activeSession.history.map((_, i) => (
                            <div key={i} className={`leading-[1.85] ${i === activeSession.history.length - 1 ? t.gutterActive + ' font-bold' : ''}`}>{i + 1}</div>
                        ))}
                        {Array.from({ length: 8 }).map((_, i) => (
                            <div key={`t${i}`} className={`${t.gutter} font-bold leading-[1.85]`}>~</div>
                        ))}
                    </div>

                    <div className="flex-1 flex flex-col overflow-hidden">
                        <div className={`flex-1 overflow-y-auto py-5 px-6 text-[13px] leading-[1.85] ${t.textOutput}`}>
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

                        {/* Statusline */}
                        <div className="flex text-[10px] font-bold select-none h-6 shrink-0">
                            <div className={`${isFocused ? t.modeInsert : t.modeNormal} px-4 flex items-center tracking-widest`}>
                                {isFocused ? 'INSERT' : 'NORMAL'}
                            </div>
                            <div className={`${t.statusBg} ${t.text} px-4 flex items-center font-normal gap-2`}>
                                <TerminalIcon size={10} /> openbb.cli
                            </div>
                            <div className={`flex-1 ${t.statusBg}`} />
                            <div className={`${t.statusBg3} ${t.textDim} px-3 flex items-center`}>utf-8</div>
                            <div className={`${t.statusBg2} ${t.textBright} px-4 flex items-center tracking-tight`}>{lineCount}:1</div>
                        </div>

                        {/* Command Line */}
                        <div className={`h-9 border-t ${t.borderTab} shrink-0 flex items-center px-4 ${isDark ? 'bg-[#1a1b26]/60' : 'bg-[#eff1f5]/60'}`}>
                            <form onSubmit={handleCommand} className="flex-1 flex items-center h-full">
                                <span className={`${t.textBright} font-bold mr-2 text-[15px]`}>:</span>
                                <div className="relative flex-1 flex items-center">
                                    <input
                                        ref={inputRef}
                                        type="text"
                                        value={activeSession.input}
                                        onChange={e => updateActiveSession({ input: e.target.value })}
                                        onKeyDown={handleKeyDown}
                                        onFocus={() => setIsFocused(true)}
                                        onBlur={() => setIsFocused(false)}
                                        className={`w-full bg-transparent border-none outline-none ${t.textInput} focus:ring-0 py-0 px-0 caret-transparent tracking-wide text-[14px] font-medium`}
                                        spellCheck="false"
                                        autoComplete="off"
                                        disabled={activeSession.isExecuting}
                                    />
                                    <div className="absolute top-0 left-0 pointer-events-none flex h-full items-center">
                                        <span className="opacity-0 whitespace-pre text-[14px]">{activeSession.input}</span>
                                        <span className={`w-[9px] h-[17px] ${isFocused ? `${t.cursor} animate-pulse` : `border ${t.cursorBorder} bg-transparent`}`} />
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
