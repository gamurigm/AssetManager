"use client"

import { useState, useRef, useEffect, useCallback } from "react";
import { Maximize2, Minimize2, Plus, X, ChevronDown, Terminal as TerminalIcon, Loader2 } from "lucide-react";
import { usePortfolio } from "../../context/PortfolioContext";

import { TAB_COMPLETIONS, getTerminalTheme, Session, Message } from "./TerminalConstants";
import { useTerminalSession } from "./useTerminalSession";
import { useTerminalDrag } from "./useTerminalDrag";

export default function OpenBBTerminal() {
    const [isOpen, setIsOpen] = useState(false);
    const [isFullscreen, setIsFullscreen] = useState(false);
    const [isFocused, setIsFocused] = useState(false);
    const [isDark, setIsDark] = useState(true);
    const [isStellar, setIsStellar] = useState(false);
    const [panelHeight, setPanelHeight] = useState(260);

    const inputRef = useRef<HTMLInputElement>(null);
    const endRef = useRef<HTMLDivElement>(null);
    const inactivityTimer = useRef<NodeJS.Timeout | null>(null);

    const { sessions, setSessions, activeId, setActiveId, updateSession, runCommand } = useTerminalSession();

    const activeSession = sessions.find(s => s.id === activeId) || sessions[0];
    const updateActiveSession = (update: Partial<Session>) => updateSession(activeId, update);

    const resetInactivity = useCallback(() => {
        if (inactivityTimer.current) clearTimeout(inactivityTimer.current);
        if (!isOpen && !isStellar) {
            inactivityTimer.current = setTimeout(() => setIsStellar(true), 45000);
        }
    }, [isOpen, isStellar]);

    const snapToSafePosition = useCallback(() => { }, []); // Simplified

    const { termIconPos, termDragging, setTermDragging, termDragRef } = useTerminalDrag(
        snapToSafePosition, setIsOpen, setIsStellar, resetInactivity
    );

    // Theme detection
    useEffect(() => {
        const check = () => setIsDark(!document.documentElement.classList.contains('light'));
        check();
        const obs = new MutationObserver(check);
        obs.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
        return () => obs.disconnect();
    }, []);

    useEffect(() => {
        resetInactivity();
        const events = ["mousedown", "mousemove", "keypress", "scroll", "touchstart"];
        events.forEach(e => document.addEventListener(e, resetInactivity));
        return () => {
            if (inactivityTimer.current) clearTimeout(inactivityTimer.current);
            events.forEach(e => document.removeEventListener(e, resetInactivity));
        };
    }, [resetInactivity]);

    useEffect(() => {
        const effectiveHeight = isOpen && !isFullscreen ? panelHeight : 0;
        window.dispatchEvent(new CustomEvent('terminal-resize', { detail: { height: effectiveHeight } }));
    }, [isOpen, isFullscreen, panelHeight]);

    useEffect(() => {
        return () => { window.dispatchEvent(new CustomEvent('terminal-resize', { detail: { height: 0 } })); };
    }, []);

    // Agent Bridge
    useEffect(() => {
        const handler = (e: Event) => {
            const cmd = (e as CustomEvent).detail?.command;
            if (!cmd || typeof cmd !== 'string') return;
            setIsOpen(true);
            setIsStellar(false);
            setSessions(prev => {
                const session = prev.find(s => s.id === activeId);
                if (!session) return prev;
                const newHistory: Message[] = [...session.history, { type: 'output', text: '🤖 Agent executed:' }];
                return prev.map(s => s.id === activeId ? { ...s, history: newHistory, pendingCmd: cmd } : s);
            });
        };
        window.addEventListener('terminal-execute', handler);
        return () => window.removeEventListener('terminal-execute', handler);
    }, [activeId, setSessions]);

    useEffect(() => {
        if (isOpen && inputRef.current) inputRef.current.focus();
        if (endRef.current) endRef.current.scrollIntoView({ behavior: 'smooth' });
    }, [activeSession?.history, isOpen, activeId]);

    const handleCommand = async (e: React.FormEvent) => {
        e.preventDefault();
        const cmd = activeSession.input.trim();
        if (!cmd) return;
        if (activeSession.isExecuting) {
            updateActiveSession({ pendingCmd: cmd, input: '' });
            return;
        }
        await runCommand(activeId, cmd, activeSession.history);
    };

    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        const inputs = activeSession.history.filter(m => m.type === 'input');
        const val = activeSession.input;

        if (e.key === 'ArrowUp') {
            e.preventDefault();
            if (inputs.length === 0) return;
            const newIndex = activeSession.historyIndex === -1 ? inputs.length - 1 : Math.max(0, activeSession.historyIndex - 1);
            updateActiveSession({ historyIndex: newIndex, input: inputs[newIndex].text });
            setTimeout(() => inputRef.current?.setSelectionRange(inputRef.current.value.length, inputRef.current.value.length), 0);
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
                setTimeout(() => inputRef.current?.setSelectionRange(inputRef.current.value.length, inputRef.current.value.length), 0);
            }
            return;
        }

        if (e.key === 'Tab') {
            e.preventDefault();
            const trimmed = val.trimStart().toLowerCase();
            const matches = TAB_COMPLETIONS.filter(c => c.startsWith(trimmed));
            if (matches.length === 1) {
                updateActiveSession({ input: matches[0] });
            } else if (matches.length > 1) {
                updateSession(activeId, { history: [...activeSession.history, { type: 'output', text: matches.join('   ') }] });
            }
            return;
        }

        if (e.ctrlKey) {
            if (e.key === 'l' || e.key === 'L') {
                e.preventDefault();
                updateActiveSession({ history: [], input: val });
                return;
            }
            if (e.key === 'c' || e.key === 'C') {
                if (window.getSelection()?.toString()) return;
                e.preventDefault();
                if (activeSession.isExecuting) {
                    updateActiveSession({ isExecuting: false, pendingCmd: null, history: [...activeSession.history, { type: 'error', text: '^C' }] });
                } else {
                    updateActiveSession({ input: '', history: val ? [...activeSession.history, { type: 'input', text: val + '^C' }] : activeSession.history });
                }
                return;
            }
            if (e.key === 'u' || e.key === 'U') {
                e.preventDefault();
                updateActiveSession({ input: '' });
                return;
            }
        }

        if (e.key === 'Escape') {
            e.preventDefault();
            updateActiveSession({ input: '', historyIndex: -1 });
            return;
        }
    };

    const newSession = () => {
        const id = Math.random().toString(36).substring(7);
        setSessions(prev => [...prev, { id, history: [{ type: 'output', text: 'Buffer initialized.' }], input: '', isExecuting: false, historyIndex: -1, pendingCmd: null }]);
        setActiveId(id);
    };

    const closeSession = (e: React.MouseEvent, id: string) => {
        e.stopPropagation();
        if (sessions.length === 1) { setIsOpen(false); return; }
        const rest = sessions.filter(s => s.id !== id);
        setSessions(rest);
        if (activeId === id) setActiveId(rest[rest.length - 1].id);
    };

    const t = getTerminalTheme(isDark);
    const lineCount = activeSession.history.length + 1;

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
                    className={`h-16 w-16 flex items-center justify-center transition-all duration-500 group overflow-hidden relative shadow-2xl backdrop-blur-xl
                        ${isDark ? 'bg-zinc-950/40 border-[1.5px] border-cyan-500/30 rounded-[24px] shadow-[0_0_40px_-10px_rgba(34,211,238,0.4)] hover:border-cyan-400' : 'bg-white/40 border-[1.5px] border-teal-500/30 rounded-[24px] shadow-[0_20px_40px_-10px_rgba(20,184,166,0.3)] hover:border-teal-500'}
                        ${termDragging ? 'cursor-grabbing scale-105 rotate-12' : 'cursor-grab hover:scale-110 hover:-rotate-6 active:scale-95'}`}
                >
                    <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/10 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000" />
                    {!isDark && <div className="absolute inset-0 rounded-full bg-teal-400/10 animate-ping [animation-duration:3s]" />}
                    <div className={`absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 ${isDark ? 'bg-cyan-500/10' : 'bg-teal-500/10'}`} />
                    <TerminalIcon size={24} className={`${isDark ? 'text-cyan-400' : 'text-teal-600'} drop-shadow-[0_0_8px_rgba(34,211,238,0.5)] relative z-10 transition-transform group-hover:scale-110`} />
                </button>
            </div>
        );
    }

    const containerBase = isFullscreen
        ? `fixed inset-0 z-[200] ${t.bg} ${t.panelBlur} flex flex-col transition-all duration-700`
        : `relative w-full z-[150] flex flex-col transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] ${t.bg} ${t.panelBlur} border-t ${t.border}`;

    return (
        <div className={containerBase} style={!isFullscreen ? { height: `${panelHeight}px` } : {}}>
            {!isFullscreen && (
                <div
                    className={`absolute top-0 left-0 w-full h-3 cursor-ns-resize z-20 flex items-center justify-center group transition-colors ${isDark ? 'hover:bg-cyan-500/20' : 'hover:bg-teal-500/15'}`}
                    onMouseDown={(e) => {
                        e.preventDefault();
                        const startY = e.clientY;
                        const startH = panelHeight;
                        const move = (ev: MouseEvent) => setPanelHeight(Math.max(120, Math.min(Math.floor(window.innerHeight * 0.92), startH + startY - ev.clientY)));
                        const up = () => { window.removeEventListener('mousemove', move); window.removeEventListener('mouseup', up); };
                        window.addEventListener('mousemove', move); window.addEventListener('mouseup', up);
                    }}
                >
                    <div className={`w-16 h-1 rounded-full transition-all duration-150 group-hover:w-28 group-active:w-36 ${isDark ? 'bg-cyan-500/40 group-hover:bg-cyan-400/70' : 'bg-teal-500/30 group-hover:bg-teal-500/60'}`} />
                </div>
            )}

            <div className={`flex flex-col h-full w-full font-mono ${isFullscreen ? `border ${t.border} m-6 rounded-2xl overflow-hidden shadow-2xl` : 'rounded-t-[32px]'}`} data-terminal-panel>
                <div className={`flex items-center justify-between ${t.bgTab} shrink-0 border-b ${t.borderTab} select-none`}>
                    <div className="flex items-center">
                        {sessions.map((s, i) => (
                            <div key={s.id} onClick={() => setActiveId(s.id)} className={`group flex items-center gap-3 px-8 py-3.5 text-[11px] font-bold tracking-[0.2em] uppercase cursor-pointer transition-all border-r ${t.borderTab} relative ${activeId === s.id ? `${t.textBright} ${t.bgTabActive}` : `${t.textDim} hover:bg-white/5`}`}>
                                {activeId === s.id && <div className={`absolute bottom-0 left-0 w-full h-[2px] ${t.tabIndicator} ${t.accentGlow}`} />}
                                <span>{i + 1}:openbb</span>
                                {s.isExecuting && s.id !== activeId && <Loader2 size={10} className={`animate-spin ${t.warn}`} />}
                                {sessions.length > 1 && <button onClick={(e) => closeSession(e, s.id)} className={`ml-2 opacity-0 group-hover:opacity-100 p-0.5 ${t.textError} hover:bg-rose-500/10 rounded-full transition-all`}><X size={10} /></button>}
                            </div>
                        ))}
                        <button onClick={newSession} className={`px-6 py-2.5 ${t.textDim} transition-all border-r ${t.borderTab} hover:text-white hover:bg-white/5`}><Plus size={14} /></button>
                    </div>
                    <div className={`flex items-center gap-5 px-5 ${t.textDim}`}>
                        <div className="hidden sm:flex items-center gap-1.5">
                            <button onClick={() => setIsFullscreen(!isFullscreen)} className={`p-2 rounded transition-colors ${isDark ? 'hover:text-cyan-400 hover:bg-zinc-800' : 'hover:text-teal-600 hover:bg-slate-300'}`}>{isFullscreen ? <Minimize2 size={15} /> : <Maximize2 size={15} />}</button>
                            <button onClick={() => { setIsOpen(false); setIsFullscreen(false); }} className={`p-2 rounded transition-colors ${isDark ? 'hover:text-rose-400 hover:bg-zinc-800' : 'hover:text-red-500 hover:bg-slate-300'}`}><ChevronDown size={17} /></button>
                        </div>
                    </div>
                </div>

                <div className="flex-1 flex min-h-0 overflow-hidden">
                    <div className={`w-12 ${t.gutterBg} border-r ${t.borderTab} flex flex-col items-end py-3 px-2 ${t.gutter} text-xs select-none overflow-hidden`}>
                        {activeSession.history.map((_, i) => <div key={i} className={`leading-[1.85] ${i === activeSession.history.length - 1 ? t.gutterActive : ''}`}>{i + 1}</div>)}
                        {Array.from({ length: 8 }).map((_, i) => <div key={`t${i}`} className={`${t.gutter} leading-[1.85]`}>~</div>)}
                    </div>
                    <div className="flex-1 flex flex-col overflow-hidden relative">
                        <div className={`flex-1 overflow-y-auto py-4 px-5 text-[14px] leading-relaxed tracking-wide ${t.textOutput} select-text cursor-text`} onClick={() => !window.getSelection()?.toString() && inputRef.current?.focus()}>
                            {activeSession.history.map((line, i) => (
                                <div key={i} className={`whitespace-pre-wrap ${line.type === 'input' ? `${t.textCmd} font-semibold` : line.type === 'error' ? t.textError : t.textOutput}`}>
                                    {line.type === 'input' && <span className={`${t.textCmd} opacity-50 mr-3`}>:</span>}
                                    {line.text}
                                </div>
                            ))}
                            {activeSession.isExecuting && <div className={`flex items-center gap-3 ${t.warn} font-bold tracking-[0.15em] text-[10px] uppercase py-3`}><span className={`w-2 h-2 ${t.warnDot} rounded-full animate-pulse`} />-- executing --</div>}
                            <div ref={endRef} />
                        </div>
                        <div className={`h-14 border-t ${t.border} shrink-0 flex items-center px-6 gap-4 bg-black/20 backdrop-blur-xl group/input`}>
                            <span className={`shrink-0 select-none font-bold text-[18px] transition-transform duration-300 ${isFocused ? `${t.textCmd} scale-110` : t.textDim}`}>❯</span>
                            <form onSubmit={handleCommand} className="flex-1 flex items-center h-full min-w-0">
                                <input ref={inputRef} type="text" value={activeSession.input} onChange={e => updateActiveSession({ input: e.target.value, historyIndex: -1 })} onKeyDown={handleKeyDown} onFocus={() => setIsFocused(true)} onBlur={() => setIsFocused(false)} className={`w-full bg-transparent border-none outline-none ${t.textInput} focus:ring-0 py-0 px-0 tracking-wider text-[15px] font-semibold antialiased`} spellCheck={false} autoComplete="off" placeholder={activeSession.isExecuting && activeSession.pendingCmd ? `queued: ${activeSession.pendingCmd}` : activeSession.isExecuting ? 'executing…' : ''} />
                            </form>
                            {activeSession.isExecuting && <div className={`shrink-0 flex items-center gap-1.5 text-[9px] font-bold tracking-widest uppercase ${t.warn}`}><Loader2 size={10} className="animate-spin" />{activeSession.pendingCmd ? 'queued' : 'running'}</div>}
                        </div>
                        <div className="flex text-[11px] font-bold select-none h-7 shrink-0 tracking-wide">
                            <div className={`${isFocused ? t.modeInsert : t.modeNormal} px-4 flex items-center tracking-widest`}>{isFocused ? 'INSERT' : 'NORMAL'}</div>
                            <div className={`${t.statusBg} ${t.text} px-5 flex items-center font-medium gap-2`}><TerminalIcon size={12} className="opacity-70" /> openbb.cli</div>
                            <div className={`flex-1 ${t.statusBg}`} />
                            <div className={`${t.statusBg3} ${t.textDim} px-4 flex items-center`}>utf-8</div>
                            <div className={`${t.statusBg2} ${t.textBright} px-5 flex items-center tracking-tight`}>{lineCount}:1</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
