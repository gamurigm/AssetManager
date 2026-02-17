"use client"

import { useState, useRef, useEffect, useCallback } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import "katex/dist/katex.min.css";

import {
    Send,
    X,
    Sparkles,
    BrainCircuit,
    Bot,
    Terminal,
    Maximize2,
    Minimize2,
    Sun,
    Moon,
    ShieldCheck
} from "lucide-react";

type Model = "general" | "mistral" | "mixtral" | "glm5";

export default function ChatWidget() {
    const [isOpen, setIsOpen] = useState(false);
    const [isMaximized, setIsMaximized] = useState(false);
    const [isDarkMode, setIsDarkMode] = useState(true);
    const [isStellarMode, setIsStellarMode] = useState(false); // Mode where it becomes a tiny spark
    const [messages, setMessages] = useState<{ role: string, content: string, reasoning?: string }[]>([]);
    const [input, setInput] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [selectedModel, setSelectedModel] = useState<Model>("general");
    const [showReasoning, setShowReasoning] = useState<Record<number, boolean>>({});

    // Position state
    const [iconPos, setIconPos] = useState({ x: 40, y: 40 });
    const [isDragging, setIsDragging] = useState(false);
    const dragRef = useRef<{ startX: number, startY: number, startPosX: number, startPosY: number, moved: boolean } | null>(null);
    const inactivityTimer = useRef<NodeJS.Timeout | null>(null);

    const scrollRef = useRef<HTMLDivElement>(null);

    // Sync theme with global document class
    useEffect(() => {
        const checkTheme = () => {
            setIsDarkMode(!document.documentElement.classList.contains('light'));
        };
        checkTheme();

        const observer = new MutationObserver(checkTheme);
        observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
        return () => observer.disconnect();
    }, []);

    // Activity tracker for auto-spark mode
    const resetInactivityTimer = useCallback(() => {
        if (inactivityTimer.current) clearTimeout(inactivityTimer.current);
        if (!isOpen && !isStellarMode) {
            inactivityTimer.current = setTimeout(() => {
                setIsStellarMode(true);
            }, 60000); // 1 minute
        }
    }, [isOpen, isStellarMode]);

    useEffect(() => {
        resetInactivityTimer();
        const events = ['mousedown', 'mousemove', 'keypress', 'scroll', 'touchstart'];
        events.forEach(name => document.addEventListener(name, resetInactivityTimer));
        return () => {
            if (inactivityTimer.current) clearTimeout(inactivityTimer.current);
            events.forEach(name => document.removeEventListener(name, resetInactivityTimer));
        };
    }, [resetInactivityTimer]);

    useEffect(() => {
        if (scrollRef.current) {
            scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
        }
    }, [messages, isOpen, isMaximized]);

    const handleMouseDown = (e: React.MouseEvent) => {
        if (isOpen || isStellarMode) return;
        setIsDragging(true);
        dragRef.current = {
            startX: e.clientX,
            startY: e.clientY,
            startPosX: iconPos.x,
            startPosY: iconPos.y,
            moved: false
        };
    };

    useEffect(() => {
        const handleResize = () => {
            if (!isDragging && !isOpen && !isStellarMode) {
                setIconPos(prev => ({
                    x: Math.min(prev.x, window.innerWidth - 80),
                    y: Math.min(prev.y, window.innerHeight - 80)
                }));
            }
        };
        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, [isDragging, isOpen, isStellarMode]);

    useEffect(() => {
        const handleMouseMove = (e: MouseEvent) => {
            if (!isDragging || !dragRef.current) return;

            // Calculate how far the mouse has moved from the start point
            const deltaX = dragRef.current.startX - e.clientX;
            const deltaY = dragRef.current.startY - e.clientY;

            // If the mouse has moved more than 5px, it's a drag, not a click
            if (Math.abs(deltaX) > 5 || Math.abs(deltaY) > 5) {
                dragRef.current.moved = true;
            }

            // New position is StartPosition + Delta
            const newX = dragRef.current.startPosX + deltaX;
            const newY = dragRef.current.startPosY + deltaY;

            setIconPos({
                x: Math.min(Math.max(20, newX), window.innerWidth - 70),
                y: Math.min(Math.max(20, newY), window.innerHeight - 70)
            });
        };

        const handleMouseUp = () => {
            if (!isDragging) return;
            setIsDragging(false);
            if (dragRef.current && !dragRef.current.moved) setIsOpen(true);
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
    }, [isDragging]);

    const preprocessMarkdown = (text: string) => {
        if (!text) return "";
        return text
            .replace(/\\\[/g, "\n$$\n").replace(/\\\]/g, "\n$$\n")
            .replace(/\\\(/g, " $").replace(/\\\)/g, "$ ")
            .replace(/\$\$([\s\S]+?)\$\$/g, (match, p1) => `\n$$\n${p1.trim()}\n$$\n`)
            .replace(/\\(_|\^|{|}|%|&|\$)/g, "$1");
    };

    const handleSend = async () => {
        if (!input.trim()) return;
        const userMsg = { role: "user", content: input };
        setMessages(prev => [...prev, userMsg]);
        setInput("");
        setIsLoading(true);
        const assistantMsgIndex = messages.length + 1;
        setMessages(prev => [...prev, { role: "assistant", content: "", reasoning: "" }]);

        try {
            const endpoint = selectedModel === "general"
                ? "http://127.0.0.1:8000/api/v1/agents/chat"
                : `http://127.0.0.1:8000/api/v1/agents/chat/${selectedModel}`;

            const response = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: input,
                    user_id: 1,
                    history: messages.map(m => ({ role: m.role, content: m.content }))
                })
            });

            if (false) { // Old non-streaming logic for reference, disabled
                const data = await response.json();
                setMessages(prev => {
                    const updated = [...prev];
                    updated[assistantMsgIndex] = { role: "assistant", content: data.response };
                    return updated;
                });
            } else {
                if (!response.body) throw new Error("No body");
                const reader = response.body.getReader();
                const decoder = new TextDecoder();
                let accC = ""; let accR = "";
                while (true) {
                    const { done, value } = await reader.read();
                    if (done) break;
                    const chunk = decoder.decode(value, { stream: true });
                    if (selectedModel === "glm5") {
                        const lines = chunk.split("\n");
                        for (const line of lines) {
                            if (!line.trim()) continue;
                            try {
                                const data = JSON.parse(line);
                                accR += data.reasoning || "";
                                accC += data.content || "";
                            } catch (e) { }
                        }
                    } else accC += chunk;
                    setMessages(prev => {
                        const updated = [...prev];
                        updated[assistantMsgIndex] = { role: "assistant", content: accC, reasoning: accR };
                        return updated;
                    });
                }
            }
        } catch (error) {
            setMessages(prev => {
                const updated = [...prev];
                updated[assistantMsgIndex] = { role: "assistant", content: "⚠️ **Link Error.**" };
                return updated;
            });
        } finally { setIsLoading(false); }
    };

    const wakeUp = () => {
        setIsStellarMode(false);
        setIsOpen(true);
        resetInactivityTimer();
    };

    return (
        <div
            className={`fixed z-[9999] flex flex-col items-end transition-all ${isDragging ? "select-none scale-105" : ""}`}
            style={{
                right: isStellarMode ? 20 : (isMaximized ? 0 : (isOpen ? (window.innerWidth < 640 ? 0 : 40) : iconPos.x)),
                top: isStellarMode ? 20 : 'auto',
                bottom: isStellarMode ? 'auto' : (isMaximized ? 0 : (isOpen ? (window.innerWidth < 640 ? 0 : 40) : iconPos.y)),
                width: isStellarMode ? "12px" : (isMaximized ? "100%" : (isOpen ? "min(480px, 100vw)" : "56px")),
                height: isStellarMode ? "12px" : (isMaximized ? "100%" : (isOpen ? (window.innerWidth < 640 ? "100vh" : "min(800px, calc(100vh - 80px))") : "56px")),
                transition: isDragging ? "none" : "all 0.8s cubic-bezier(0.2, 0.8, 0.2, 1)"
            }}
        >
            {isStellarMode ? (
                <button
                    onClick={wakeUp}
                    className="w-5 h-5 rounded-full relative cursor-pointer group flex items-center justify-center transition-transform hover:scale-125"
                >
                    {/* Unified Nucleus */}
                    <div className={`w-3 h-3 rounded-full z-10 animate-stellar shadow-[0_0_20px_2px]
                        ${isDarkMode
                            ? "bg-fuchsia-400 shadow-fuchsia-500/80"
                            : "bg-indigo-600 shadow-indigo-600/60"}`}
                    />

                    {/* Singular Cinematic Shockwave */}
                    <div className={`absolute inset-0 rounded-full animate-shockwave
                        ${isDarkMode ? "bg-fuchsia-500/30" : "bg-indigo-600/30"}`}
                    />
                </button>
            ) : isOpen ? (
                <div className={`w-full h-full flex flex-col overflow-hidden transition-colors duration-500
                    ${isDarkMode
                        ? "bg-zinc-950/98 backdrop-blur-3xl border border-white/10 shadow-[0_40px_100px_-20px_rgba(0,0,0,0.8)]"
                        : "bg-white/95 backdrop-blur-3xl border border-zinc-200 shadow-[0_40px_100px_-20px_rgba(0,0,0,0.15)]"}
                    ${isMaximized || (typeof window !== 'undefined' && window.innerWidth < 640) ? "rounded-none border-none" : "rounded-[32px]"} ring-1 ring-black/5`}>

                    <header className={`${typeof window !== 'undefined' && window.innerWidth < 640 ? "px-4 py-3" : "px-6 py-4"} flex justify-between items-center border-b transition-colors
                        ${isDarkMode ? "bg-white/[0.03] border-white/5" : "bg-zinc-50 border-zinc-100"}`}>
                        <div className="flex items-center gap-3">
                            <div className={`h-9 w-9 rounded-xl flex items-center justify-center text-white shadow-lg
                                ${isDarkMode ? "bg-fuchsia-600" : "bg-indigo-600"}`}>
                                <Terminal size={16} />
                            </div>
                            <div className="flex flex-col">
                                <h3 className={`font-bold text-base tracking-tight ${isDarkMode ? "text-white" : "text-zinc-900"}`}>
                                    Intelligence Core
                                </h3>
                                <div className="flex items-center gap-1.5">
                                    <div className="h-1 w-1 rounded-full bg-emerald-500 animate-pulse" />
                                    <select
                                        value={selectedModel}
                                        onChange={(e) => setSelectedModel(e.target.value as Model)}
                                        className={`bg-transparent text-xs border-none p-0 focus:ring-0 cursor-pointer transition-all uppercase tracking-[0.2em] font-black outline-none
                                            ${isDarkMode ? "text-zinc-500 hover:text-fuchsia-400" : "text-zinc-400 hover:text-indigo-600"}`}
                                    >
                                        <option value="general" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>Hybrid Core</option>
                                        <option value="mistral" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>Mistral-L3</option>
                                        <option value="mixtral" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>MoE-8x22B</option>
                                        <option value="glm5" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>GLM-5 Deep</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div className="flex items-center gap-1.5">
                            <button onClick={() => setIsMaximized(!isMaximized)} className={`h-8 w-8 flex items-center justify-center rounded-lg ${isDarkMode ? "bg-white/5 text-zinc-400" : "bg-zinc-200/50 text-zinc-600"}`}>
                                {isMaximized ? <Minimize2 size={14} /> : <Maximize2 size={14} />}
                            </button>
                            <button onClick={() => setIsOpen(false)} className={`h-8 w-8 flex items-center justify-center rounded-lg ${isDarkMode ? "bg-white/5 text-zinc-400" : "bg-zinc-200/50 text-zinc-600"}`}>
                                <X size={16} />
                            </button>
                        </div>
                    </header>

                    <div ref={scrollRef} className={`flex-1 overflow-y-auto ${typeof window !== 'undefined' && window.innerWidth < 640 ? "px-4 pt-4" : "px-6 pt-6"} space-y-8 scrollbar-none pb-4 transition-colors
                        ${isDarkMode ? "bg-transparent" : "bg-zinc-50/30"}`}>
                        {messages.map((m, i) => (
                            <div key={i} className={`flex ${m.role === "user" ? "justify-end" : "justify-start"}`}>
                                <div className={`${isMaximized ? "max-w-[70%]" : "max-w-full"} space-y-2`}>
                                    <div className={`py-4 px-6 rounded-[22px] transition-all duration-300 shadow-sm
                                        ${m.role === "user"
                                            ? (isDarkMode ? "bg-white text-black rounded-tr-none" : "bg-indigo-600 text-white rounded-tr-none")
                                            : (isDarkMode ? "bg-white/[0.04] text-zinc-100 rounded-tl-none border border-white/10" : "bg-white text-zinc-900 rounded-tl-none border border-zinc-200")
                                        }`}>
                                        <div
                                            style={{ fontSize: '106%' }}
                                            className={`prose prose-sm max-w-full break-normal
                                            ${m.role === "user" ? (isDarkMode ? "prose-zinc" : "prose-invert") : (isDarkMode ? "prose-invert" : "prose-zinc")}
                                            prose-p:leading-relaxed prose-p:mb-3 last:prose-p:mb-0
                                            prose-strong:font-bold prose-code:px-1.5 prose-code:rounded-md
                                            ${isDarkMode ? "prose-strong:text-fuchsia-400 prose-code:text-emerald-400 prose-code:bg-emerald-400/5" : "prose-strong:text-indigo-600 prose-code:text-emerald-600 prose-code:bg-emerald-50"}
                                        `}>
                                            {m.reasoning && (
                                                <div className={`mb-4 p-3 rounded-xl border italic text-[11px] leading-relaxed
                                                    ${isDarkMode ? "bg-white/[0.03] border-white/5 text-zinc-400" : "bg-zinc-50 border-zinc-100 text-zinc-500"}`}>
                                                    <div className="flex items-center gap-2 mb-1.5 opacity-70">
                                                        <div className="w-1.5 h-1.5 rounded-full bg-accent animate-pulse" />
                                                        <span className="font-bold uppercase tracking-widest text-[9px]">Internal Cognition</span>
                                                    </div>
                                                    {m.reasoning}
                                                </div>
                                            )}
                                            {m.content === "" && m.role === "assistant" && isLoading ? (
                                                <div className="flex gap-2 items-center h-8 px-1">
                                                    <div className="w-2 h-2 bg-current rounded-full animate-bounce [animation-delay:-0.3s]"></div>
                                                    <div className="w-2 h-2 bg-current rounded-full animate-bounce [animation-delay:-0.15s]"></div>
                                                    <div className="w-2 h-2 bg-current rounded-full animate-bounce"></div>
                                                </div>
                                            ) : (
                                                <ReactMarkdown remarkPlugins={[remarkGfm, remarkMath]} rehypePlugins={[[rehypeKatex, { strict: false, throwOnError: false }]]}>
                                                    {preprocessMarkdown(m.content)}
                                                </ReactMarkdown>
                                            )}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>

                    <div className={`px-6 py-6 border-t bg-gradient-to-t
                        ${isDarkMode ? "from-black to-transparent border-white/5" : "from-zinc-100 to-transparent border-zinc-100"}`}>
                        <div className={`relative flex items-center rounded-2xl border transition-all duration-300
                            ${isDarkMode ? "bg-white/[0.04] border-white/10" : "bg-white border-zinc-200 shadow-sm"}`}>
                            <input
                                value={input}
                                onChange={(e) => setInput(e.target.value)}
                                onKeyDown={(e) => e.key === "Enter" && !isLoading && handleSend()}
                                style={{ fontSize: '106%' }}
                                className={`w-full bg-transparent py-4 px-6 text-sm font-medium focus:outline-none
                                    ${isDarkMode ? "text-white placeholder:text-zinc-700" : "text-zinc-900 placeholder:text-zinc-400"}`}
                                placeholder="Sync directive..."
                                disabled={isLoading}
                            />
                            <button onClick={handleSend} className={`mr-2 h-10 w-10 rounded-xl text-white flex items-center justify-center transition-all ${isDarkMode ? "bg-fuchsia-600 hover:bg-fuchsia-500" : "bg-indigo-600 hover:bg-indigo-500"}`}>
                                <Send size={18} />
                            </button>
                        </div>
                    </div>
                </div>
            ) : (
                <button
                    onMouseDown={handleMouseDown}
                    className={`h-14 w-14 flex items-center justify-center transition-all duration-500 group overflow-hidden relative shadow-2xl
                        ${isDarkMode
                            ? "bg-zinc-950 border-2 border-fuchsia-500/50 rounded-[22px] ring-4 ring-fuchsia-500/10 shadow-[0_0_30px_-5px_#d946ef80]"
                            : "bg-gradient-to-br from-indigo-600 via-violet-600 to-indigo-700 rounded-[22px] shadow-[0_15px_35px_-5px_rgba(79,70,229,0.5)] border border-white/20"}
                        ${isDragging ? "cursor-grabbing scale-110" : "cursor-grab"}`}
                >
                    {/* Animated Shine Effect */}
                    <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000" />

                    {/* Pulsing Aura (Light Mode Only) */}
                    {!isDarkMode && (
                        <div className="absolute inset-0 rounded-full bg-indigo-400/20 animate-ping [animation-duration:3s]" />
                    )}

                    <div className={`absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity
                        ${isDarkMode ? "bg-fuchsia-600/10" : "bg-white/10"}`} />

                    <Sparkles size={22} className="text-white drop-shadow-[0_2px_4px_rgba(0,0,0,0.3)] relative z-10" />
                </button>
            )}
        </div>
    );
}
