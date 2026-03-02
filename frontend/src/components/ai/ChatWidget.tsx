"use client"

import { useState, useRef, useEffect, useCallback } from "react";
import {
    X, Sparkles, BrainCircuit, Maximize2, Minimize2,
    Trash2, Menu, Plus
} from "lucide-react";

import { usePortfolio } from "@/context/PortfolioContext";
import ChatPane from "./ChatPane";

type Model = "general" | "mistral" | "mixtral" | "kimi" | "deepseek" | "nemotron";

interface Session {
    id: string;
    title: string;
    agent?: string;
    messages: { role: string; content: string; reasoning?: string }[];
}

export default function ChatWidget() {
    const { holdings, totalValue, totalPnL, pnlPercent } = usePortfolio();

    // UI States
    const [isOpen, setIsOpen] = useState(false);
    const [isMaximized, setIsMaximized] = useState(false);
    const [isDarkMode, setIsDarkMode] = useState(true);
    const [isStellarMode, setIsStellarMode] = useState(false);
    const [selectedModel, setSelectedModel] = useState<Model>("general");

    // Multi-conversation grid state
    const [sessions, setSessions] = useState<Session[]>([
        { id: "default", title: "Main", messages: [] },
    ]);
    const [activeSessionIds, setActiveSessionIds] = useState<string[]>(["default"]);
    const [showSessionMenu, setShowSessionMenu] = useState(false);

    // Floating icon mechanics
    const [iconPos, setIconPos] = useState({ x: 40, y: 40 });
    const [isDragging, setIsDragging] = useState(false);
    const dragRef = useRef<{ startX: number; startY: number; startPosX: number; startPosY: number; moved: boolean; } | null>(null);
    const inactivityTimer = useRef<NodeJS.Timeout | null>(null);

    // ── Persistence removed as requested by user
    // "solo recordar la sesion actual luego al desconcetar borrar automaticamente hata nuevo aviso"

    // We only keep selectedModel and activeSessions persistence if desired, or remove all. 
    // Usually keeping model preference is good, but NOT messages.
    useEffect(() => {
        try {
            const savedModel = localStorage.getItem("mmam_chat_model");
            if (savedModel) setSelectedModel(savedModel as Model);
        } catch { }
    }, []);

    useEffect(() => { localStorage.setItem("mmam_chat_model", selectedModel); }, [selectedModel]);

    // Theme sync
    useEffect(() => {
        const check = () => setIsDarkMode(!document.documentElement.classList.contains("light"));
        check();
        const obs = new MutationObserver(check);
        obs.observe(document.documentElement, { attributes: true, attributeFilter: ["class"] });
        return () => obs.disconnect();
    }, []);

    // Stellar Mode & Inactivity
    const resetInactivityTimer = useCallback(() => {
        if (inactivityTimer.current) clearTimeout(inactivityTimer.current);
        if (!isOpen && !isStellarMode) inactivityTimer.current = setTimeout(() => setIsStellarMode(true), 60000);
    }, [isOpen, isStellarMode]);

    useEffect(() => {
        resetInactivityTimer();
        const events = ["mousedown", "mousemove", "keypress", "scroll", "touchstart"];
        events.forEach(e => document.addEventListener(e, resetInactivityTimer));
        return () => {
            if (inactivityTimer.current) clearTimeout(inactivityTimer.current);
            events.forEach(e => document.removeEventListener(e, resetInactivityTimer));
        };
    }, [resetInactivityTimer]);

    // Dragging Logic
    const handleMouseDownIcon = (e: React.MouseEvent) => {
        if (isOpen || isStellarMode) return;
        setIsDragging(true);
        dragRef.current = { startX: e.clientX, startY: e.clientY, startPosX: iconPos.x, startPosY: iconPos.y, moved: false };
    };

    const handleMouseDownHeader = (e: React.MouseEvent) => {
        if (!isOpen || isMaximized || isStellarMode) return;
        setIsDragging(true);
        dragRef.current = { startX: e.clientX, startY: e.clientY, startPosX: iconPos.x, startPosY: iconPos.y, moved: false };
    };

    useEffect(() => {
        const handleResize = () => {
            if (!isDragging && !isStellarMode) {
                setIconPos(prev => ({
                    x: Math.min(prev.x, window.innerWidth - (isOpen ? 400 : 80)),
                    y: Math.min(prev.y, window.innerHeight - (isOpen ? 600 : 80)),
                }));
            }
        };
        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, [isDragging, isOpen, isStellarMode]);

    useEffect(() => {
        const handleMouseMove = (e: MouseEvent) => {
            if (!isDragging || !dragRef.current) return;
            const dX = dragRef.current.startX - e.clientX;
            const dY = dragRef.current.startY - e.clientY;
            if (Math.abs(dX) > 5 || Math.abs(dY) > 5) dragRef.current.moved = true;

            // Define bounds based on whether it's open (it's much larger) or closed (just an icon)
            const padding = 20;
            const curWidth = isOpen ? (activeSessionIds.length > 1 ? Math.min(1200, window.innerWidth * 0.95) : Math.min(520, window.innerWidth)) : 70;
            const curHeight = isOpen ? Math.min(800, window.innerHeight - 80) : 70;

            const maxRight = window.innerWidth - curWidth - padding;
            const maxBottom = window.innerHeight - curHeight - padding;

            // X and Y are relative to bottom-right in the old CSS, 
            // but it's easier to keep them as "Offset from bottom right" 
            setIconPos({
                x: Math.min(Math.max(padding, dragRef.current.startPosX + dX), Math.max(padding, maxRight)),
                y: Math.min(Math.max(padding, dragRef.current.startPosY + dY), Math.max(padding, maxBottom)),
            });
        };
        const handleMouseUp = () => {
            if (!isDragging) return;
            setIsDragging(false);
            // If dragging icon, not moved -> open it
            if (!isOpen && dragRef.current && !dragRef.current.moved) {
                setIsOpen(true);
            }
            dragRef.current = null;
        };
        if (isDragging) {
            window.addEventListener("mousemove", handleMouseMove);
            window.addEventListener("mouseup", handleMouseUp);
        }
        return () => {
            window.removeEventListener("mousemove", handleMouseMove);
            window.removeEventListener("mouseup", handleMouseUp);
        };
    }, [isDragging, isOpen, activeSessionIds.length]);

    // ── Session Management
    const createSession = () => {
        const id = `session_${Date.now()}`;
        const newSession: Session = { id, title: `Chat ${sessions.length + 1}`, messages: [] };
        setSessions(prev => [...prev, newSession]);

        // Open it and automatically maximize if multiple
        setActiveSessionIds(prev => {
            const next = Array.from(new Set([...prev, id]));
            if (next.length > 1) setIsMaximized(true);
            return next;
        });
        setShowSessionMenu(false);
    };

    const toggleSessionView = (id: string) => {
        setActiveSessionIds(prev => {
            if (prev.includes(id)) {
                if (prev.length === 1) return prev; // Don't close the last one
                return prev.filter(s => s !== id);
            } else {
                const next = [...prev, id];
                if (next.length > 1) setIsMaximized(true); // Split-screen benefits from max mode
                return next;
            }
        });
    };

    const deleteSession = (id: string, e?: React.MouseEvent) => {
        if (e) e.stopPropagation();
        if (sessions.length <= 1) return;
        setSessions(prev => prev.filter(s => s.id !== id));
        setActiveSessionIds(prev => {
            const next = prev.filter(p => p !== id);
            return next.length > 0 ? next : [sessions.filter(s => s.id !== id)[0].id];
        });
        fetch(`http://127.0.0.1:8282/api/v1/agents/chat/sessions/${id}`, { method: "DELETE" }).catch(() => { });
    };

    const onUpdateMessages = useCallback((id: string, updater: (prev: Session["messages"]) => Session["messages"]) => {
        setSessions(prev => prev.map(s => s.id === id ? { ...s, messages: updater(s.messages) } : s));
    }, []);

    const onUpdateTitle = useCallback((id: string, title: string) => {
        setSessions(prev => prev.map(s => s.id === id ? { ...s, title } : s));
    }, []);

    const onUpdateAgent = useCallback((id: string, agent: string) => {
        setSessions(prev => prev.map(s => s.id === id ? { ...s, agent } : s));
    }, []);

    // The grid calculates equal column widths
    const gridColumnsClass =
        activeSessionIds.length === 1 ? "grid-cols-1" :
            activeSessionIds.length === 2 ? "grid-cols-2" :
                activeSessionIds.length === 3 ? "grid-cols-3" :
                    "grid-cols-2 md:grid-cols-4"; // 4+ goes into multiple rows or 4 cols

    const activeSessions = activeSessionIds.map(id => sessions.find(s => s.id === id)).filter(Boolean) as Session[];

    // ── RENDER ──────────────────────────────────────────────────────
    return (
        <div
            className={`fixed z-[9999] flex flex-col items-end transition-all ease-[cubic-bezier(0.2,0.8,0.2,1)] duration-700 ${isDragging ? "select-none transition-none shadow-2xl" : ""}`}
            style={{
                right: isStellarMode ? 20 : (isMaximized ? 0 : iconPos.x),
                top: isStellarMode ? 20 : "auto",
                bottom: isStellarMode ? "auto" : (isMaximized ? 0 : iconPos.y),
                width: isStellarMode ? "12px" : (isMaximized ? "100%" : (isOpen ? (activeSessionIds.length > 1 ? "min(1200px, 95vw)" : "min(520px, 100vw)") : "56px")),
                height: isStellarMode ? "12px" : (isMaximized ? "100%" : (isOpen ? (window.innerWidth < 640 ? "100vh" : "min(800px, calc(100vh - 80px))") : "56px")),
            }}
        >
            {isStellarMode ? (
                <button onClick={() => { setIsStellarMode(false); setIsOpen(true); resetInactivityTimer(); }} className="w-5 h-5 rounded-full relative cursor-pointer group flex items-center justify-center transition-transform hover:scale-125">
                    <div className={`w-3 h-3 rounded-full z-10 animate-stellar shadow-[0_0_20px_2px] ${isDarkMode ? "bg-fuchsia-400 shadow-fuchsia-500/80" : "bg-indigo-600 shadow-indigo-600/60"}`} />
                    <div className={`absolute inset-0 rounded-full animate-shockwave ${isDarkMode ? "bg-fuchsia-500/30" : "bg-indigo-600/30"}`} />
                </button>
            ) : isOpen ? (
                <div className={`w-full h-full flex flex-col overflow-hidden transition-all duration-700 glass
                    ${isDarkMode ? "bg-zinc-950/80 border border-white/10 shadow-[0_40px_100px_-20px_rgba(0,0,0,0.8)]" : "bg-white/90 border border-zinc-200 shadow-[0_40px_100px_-20px_rgba(0,0,0,0.15)]"}
                    ${isMaximized || (typeof window !== "undefined" && window.innerWidth < 640) ? "rounded-none border-none" : "rounded-[32px]"} ring-1 ring-black/5`}>

                    {/* ── HEADER ─────────────────────────────────── */}
                    <header
                        onMouseDown={handleMouseDownHeader}
                        className={`px-5 py-3.5 flex justify-between items-center border-b transition-colors relative z-10 ${!isMaximized ? "cursor-grab active:cursor-grabbing" : ""}
                        ${isDarkMode ? "bg-white/[0.04] border-white/5" : "bg-white/40 border-zinc-100"}`}>
                        <div className="flex items-center gap-3">
                            <div className={`h-9 w-9 rounded-xl flex items-center justify-center text-white shadow-lg
                                ${isDarkMode ? "bg-fuchsia-600 shadow-fuchsia-500/20" : "bg-indigo-600 shadow-indigo-500/20"}`}>
                                <BrainCircuit size={18} />
                            </div>
                            <div className="flex flex-col">
                                <h3 className={`font-black text-sm tracking-tight flex items-center gap-2 ${isDarkMode ? "text-white" : "text-zinc-900"}`}>
                                    Intelligence Grid
                                    {activeSessions.length > 1 && <span className="text-[10px] bg-accent/20 text-accent px-1.5 py-0.5 rounded-full uppercase">Workspace</span>}
                                </h3>
                                <div className="flex items-center gap-2">
                                    <div className="h-1.5 w-1.5 rounded-full bg-emerald-500 animate-pulse shadow-[0_0_6px_#10b981]" />
                                    <select
                                        value={selectedModel}
                                        onChange={(e) => setSelectedModel(e.target.value as Model)}
                                        className={`bg-transparent text-[9px] border-none p-0 focus:ring-0 cursor-pointer transition-all uppercase tracking-[0.2em] font-black outline-none
                                            ${isDarkMode ? "text-zinc-500 hover:text-fuchsia-400" : "text-zinc-400 hover:text-indigo-600"}`}
                                    >
                                        <option value="general" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>Hybrid Core</option>
                                        <option value="mistral" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>Mistral-L3</option>
                                        <option value="mixtral" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>MoE-8x22B</option>
                                        <option value="kimi" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>Kimi K2.5</option>
                                        <option value="deepseek" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>DeepSeek V3</option>
                                        <option value="nemotron" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>Nemotron-253B</option>
                                    </select>
                                </div>
                            </div>
                        </div>

                        <div className="flex items-center gap-1.5">
                            <button
                                onClick={() => setShowSessionMenu(true)}
                                className={`h-8 px-3 flex items-center gap-2 rounded-lg text-[10px] font-black uppercase tracking-wider transition-all
                                    ${isDarkMode ? "bg-white/5 text-zinc-400 hover:bg-white/10 hover:text-white" : "bg-zinc-100 text-zinc-600 hover:bg-zinc-200"}`}
                            >
                                <Menu size={13} /> Grid Manager
                            </button>

                            <button onClick={() => setIsMaximized(!isMaximized)}
                                className={`h-8 w-8 flex items-center justify-center rounded-lg transition-all ${isDarkMode ? "bg-white/5 text-zinc-400 hover:bg-white/10" : "bg-zinc-100 text-zinc-600 hover:bg-zinc-200"}`}>
                                {isMaximized ? <Minimize2 size={13} /> : <Maximize2 size={13} />}
                            </button>
                            <button onClick={() => setIsOpen(false)}
                                className={`h-8 w-8 flex items-center justify-center rounded-lg transition-all ${isDarkMode ? "bg-white/5 text-zinc-400 hover:bg-white/10" : "bg-zinc-100 text-zinc-600 hover:bg-zinc-200"}`}>
                                <X size={16} />
                            </button>
                        </div>
                    </header>

                    {/* ── SESSIONS SIDEBAR OVERLAY ─────────────────────────────────── */}
                    <div className={`absolute inset-0 z-50 transition-all duration-300 ${showSessionMenu ? "opacity-100 pointer-events-auto" : "opacity-0 pointer-events-none"}`}>
                        <div className={`absolute inset-0 transition-opacity duration-300 ${isDarkMode ? "bg-black/40" : "bg-zinc-900/20"} backdrop-blur-[2px]`}
                            onClick={() => setShowSessionMenu(false)} />

                        <div className={`absolute top-0 right-0 w-[280px] h-full shadow-[-20px_0_40px_rgba(0,0,0,0.3)] flex flex-col transition-transform duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] ${showSessionMenu ? "translate-x-0" : "translate-x-full"}
                            ${isDarkMode ? "bg-zinc-950/95 border-l border-white/5" : "bg-white/95 border-l border-zinc-200"}`}>

                            <div className={`p-6 border-b flex justify-between items-center ${isDarkMode ? "border-white/5" : "border-zinc-100"}`}>
                                <h3 className={`font-black uppercase tracking-widest text-[11px] ${isDarkMode ? "text-zinc-500" : "text-zinc-400"}`}>Split View Grid</h3>
                                <button onClick={() => setShowSessionMenu(false)} className={`transition-all ${isDarkMode ? "text-zinc-500 hover:text-white" : "text-zinc-400 hover:text-black"}`}>
                                    <X size={16} />
                                </button>
                            </div>

                            <div className="flex-1 overflow-y-auto p-4 space-y-2 scrollbar-none">
                                <p className={`px-2 pb-2 text-[10px] font-medium opacity-60 ${isDarkMode ? "text-white" : "text-zinc-500"}`}>Toggle sessions to split-screen</p>
                                {sessions.map(s => {
                                    const isActive = activeSessionIds.includes(s.id);
                                    return (
                                        <div
                                            key={s.id}
                                            onClick={() => toggleSessionView(s.id)}
                                            className={`p-3.5 rounded-2xl text-[13px] border cursor-pointer flex items-center justify-between group transition-all
                                                ${isActive
                                                    ? (isDarkMode ? "border-fuchsia-500/50 bg-fuchsia-600/10 text-fuchsia-400 shadow-[0_0_15px_-3px_rgba(217,70,239,0.3)]" : "border-indigo-400 bg-indigo-50 text-indigo-700 shadow-sm")
                                                    : (isDarkMode ? "border-transparent hover:bg-white/5 text-zinc-400" : "border-transparent hover:bg-zinc-50 text-zinc-600")}`}
                                        >
                                            <div className="flex items-center gap-2 truncate">
                                                <div className={`h-2 w-2 rounded-full transition-colors ${isActive ? (isDarkMode ? "bg-fuchsia-400" : "bg-indigo-500") : "bg-zinc-600"}`} />
                                                <span className="truncate font-bold tracking-tight">{s.title}</span>
                                            </div>
                                            {sessions.length > 1 && (
                                                <button onClick={(e) => deleteSession(s.id, e)} className="opacity-0 group-hover:opacity-100 hover:scale-110 transition-all p-1">
                                                    <Trash2 size={13} className="text-red-400 hover:text-red-500" />
                                                </button>
                                            )}
                                        </div>
                                    );
                                })}
                            </div>

                            <div className={`p-5 border-t ${isDarkMode ? "border-white/5" : "border-zinc-100"}`}>
                                <button
                                    onClick={createSession}
                                    className={`w-full py-3.5 rounded-xl text-[11px] font-black uppercase tracking-widest flex items-center justify-center gap-2 transition-all shadow-lg active:scale-95
                                        ${isDarkMode ? "bg-white text-black hover:bg-zinc-200" : "bg-zinc-900 text-white hover:bg-zinc-800"}`}
                                >
                                    <Plus size={15} /> New Split Chat
                                </button>
                            </div>
                        </div>
                    </div>

                    {/* ── GRID OF ACTIVE CHATS ───────────────────────────────── */}
                    <div className={`flex-1 grid ${gridColumnsClass} overflow-hidden bg-transparent divide-x transition-colors
                                     ${isDarkMode ? "divide-white/5" : "divide-zinc-200"}`}>
                        {activeSessions.map((session) => (
                            <ChatPane
                                key={session.id}
                                session={session}
                                isDarkMode={isDarkMode}
                                isMaximized={isMaximized}
                                selectedModel={selectedModel}
                                holdings={holdings}
                                totalValue={totalValue}
                                totalPnL={totalPnL}
                                pnlPercent={pnlPercent}
                                onUpdateMessages={onUpdateMessages}
                                onUpdateTitle={onUpdateTitle}
                                onUpdateAgent={onUpdateAgent}
                            />
                        ))}
                    </div>

                </div>
            ) : (
                /* ── FLOATING ICON ──────────────────────────── */
                <button
                    onMouseDown={handleMouseDownIcon}
                    className={`h-14 w-14 flex items-center justify-center transition-all duration-500 group overflow-hidden relative shadow-2xl
                        ${isDarkMode
                            ? "bg-zinc-950 border-2 border-fuchsia-500/50 rounded-[22px] ring-4 ring-fuchsia-500/10 shadow-[0_0_30px_-5px_#d946ef80]"
                            : "bg-gradient-to-br from-indigo-600 via-violet-600 to-indigo-700 rounded-[22px] shadow-[0_15px_35px_-5px_rgba(79,70,229,0.5)] border border-white/20"}
                        ${isDragging ? "cursor-grabbing scale-110" : "cursor-grab"}`}
                >
                    <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000" />
                    {!isDarkMode && (
                        <div className="absolute inset-0 rounded-full bg-indigo-400/20 animate-ping [animation-duration:3s]" />
                    )}
                    <div className={`absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity ${isDarkMode ? "bg-fuchsia-600/10" : "bg-white/10"}`} />
                    <Sparkles size={22} className="text-white drop-shadow-[0_2px_4px_rgba(0,0,0,0.3)] relative z-10" />
                </button>
            )}
        </div>
    );
}
