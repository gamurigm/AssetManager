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
    ShieldCheck,
    Activity,
    Trash2,
    RefreshCcw
} from "lucide-react";
import { usePortfolio } from "@/context/PortfolioContext";

type Model = "general" | "mistral" | "mixtral" | "kimi" | "deepseek" | "nemotron";

export default function ChatWidget() {
    const { holdings, totalValue, totalPnL, pnlPercent } = usePortfolio();
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

    // Load session from localStorage on mount
    useEffect(() => {
        try {
            const savedMessages = localStorage.getItem("mmam_chat_history");
            const savedModel = localStorage.getItem("mmam_chat_model");

            if (savedMessages) setMessages(JSON.parse(savedMessages));
            if (savedModel) setSelectedModel(savedModel as Model);
        } catch (e) {
            console.error("Failed to load chat session:", e);
        }
    }, []);

    // Save session to localStorage on changes
    useEffect(() => {
        if (messages.length > 0) {
            localStorage.setItem("mmam_chat_history", JSON.stringify(messages));
        }
    }, [messages]);

    useEffect(() => {
        localStorage.setItem("mmam_chat_model", selectedModel);
    }, [selectedModel]);

    const clearChat = () => {
        if (confirm("Clear current intelligence session?")) {
            setMessages([]);
            localStorage.removeItem("mmam_chat_history");
        }
    };

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
        let processed = text;

        // 1. Normalize block delimiters \[ ... \] to $$
        processed = processed.replace(/\\\[/g, "\n$$\n").replace(/\\\]/g, "\n$$\n");

        // 2. Normalize inline delimiters \( ... \) to $
        processed = processed.replace(/\\\(/g, " $ ").replace(/\\\)/g, " $ ");

        // 3. Detect "lazy" multi-line single dollar blocks (common in AI outputs)
        // If a line is just $ followed by a newline, and later there is another such line, convert to $$
        // Regex: (newline or start) + (only possible whitespace and $) + (newline)
        processed = processed.replace(/(^|\n)\s*\$\s*\n([\s\S]+?)\n\s*\$\s*(\n|$)/g, "$1\n$$\n$2\n$$\n$3");

        // 4. Handle standard $$ ... $$ and ensure double-spacing/newlines for proper block detection
        processed = processed.replace(/\$\$([\s\S]+?)\$\$/g, (match, p1) => {
            const clean = p1.trim();
            return `\n\n$$\n${clean}\n$$\n\n`;
        });

        // 5. Final pass: ensure standard $...$ doesn't have spaces inside delimiters which can confuse some parsers
        // but wait, we want to BE lenient for AI. So we'll leave it or just trim.

        return processed;
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
                ? "http://127.0.0.1:8282/api/v1/agents/chat"
                : `http://127.0.0.1:8282/api/v1/agents/chat/${selectedModel}`;

            const response = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: input,
                    user_id: 1,
                    history: messages.map(m => ({ role: m.role, content: m.content })),
                    portfolio: {
                        holdings: holdings.filter(h => h.price > 0),
                        total_value: totalValue,
                        total_pnl: totalPnL,
                        pnl_percent: pnlPercent,
                        timestamp: new Date().toISOString()
                    }
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

                    if (selectedModel === "deepseek") {
                        const lines = chunk.split("\n");
                        for (const line of lines) {
                            if (!line.trim()) continue;
                            try {
                                const data = JSON.parse(line);
                                accR += data.reasoning || "";
                                accC += data.content || "";
                            } catch (e) {
                                // Fallback for raw chunks that might be mixed in
                                accC += line;
                            }
                        }
                    } else {
                        accC += chunk;
                    }

                    // Global Reasoner: Extract <think> tags from content if they leaked
                    // This handles models that don't use a separate reasoning field
                    if (accC.includes("<think>")) {
                        const parts = accC.split("</think>");
                        if (parts.length > 1) {
                            // Tag is closed
                            const thinkPart = parts[0].split("<think>")[1] || "";
                            accR += thinkPart;
                            accC = parts[1].trim();
                        } else {
                            // Tag is still open, extract what's inside to R, leave what's before in C
                            const openParts = accC.split("<think>");
                            accC = openParts[0].trim();
                            accR += openParts[1] || "";
                            // Note: This logic is slightly lossy for R during streaming 
                            // but keeps C clean. For a premium feel, we'll refine:
                        }
                    }

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
                <div className={`w-full h-full flex flex-col overflow-hidden transition-all duration-700 glass
                    ${isDarkMode
                        ? "border border-white/10 shadow-[0_40px_100px_-20px_rgba(0,0,0,0.8)]"
                        : "border border-zinc-200 shadow-[0_40px_100px_-20px_rgba(0,0,0,0.15)]"}
                    ${isMaximized || (typeof window !== 'undefined' && window.innerWidth < 640) ? "rounded-none border-none" : "rounded-[32px]"} ring-1 ring-black/5`}>

                    <header className={`${typeof window !== 'undefined' && window.innerWidth < 640 ? "px-4 py-3" : "px-6 py-5"} flex justify-between items-center border-b transition-colors relative overflow-hidden
                        ${isDarkMode ? "bg-white/[0.04] border-white/5" : "bg-white/40 border-zinc-100"}`}>
                        <div className="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-accent to-transparent opacity-50 shadow-[0_0_10px_var(--accent)]" />

                        <div className="flex items-center gap-4 relative z-10 text-gradient font-black">
                            <div className={`h-10 w-10 rounded-2xl flex items-center justify-center text-white shadow-lg animate-pulse-glow
                                ${isDarkMode ? "bg-fuchsia-600 shadow-fuchsia-500/20" : "bg-indigo-600 shadow-indigo-500/20"}`}>
                                <BrainCircuit size={20} />
                            </div>
                            <div className="flex flex-col">
                                <h3 className={`font-black text-lg tracking-tighter ${isDarkMode ? "text-white" : "text-zinc-900"}`}>
                                    Intelligence Core <span className="text-[10px] bg-accent/10 px-1.5 py-0.5 rounded ml-2 border border-accent/20">V2.4</span>
                                </h3>
                                <div className="flex items-center gap-2">
                                    <div className="h-1.5 w-1.5 rounded-full bg-emerald-500 animate-pulse shadow-[0_0_6px_#10b981]" />
                                    <select
                                        value={selectedModel}
                                        onChange={(e) => setSelectedModel(e.target.value as Model)}
                                        className={`bg-transparent text-[10px] border-none p-0 focus:ring-0 cursor-pointer transition-all uppercase tracking-[0.25em] font-black outline-none
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
                        <div className="flex items-center gap-2 relative z-10">
                            <button
                                onClick={clearChat}
                                title="Clear Session"
                                className={`h-9 w-9 flex items-center justify-center rounded-xl transition-all ${isDarkMode ? "bg-white/5 text-zinc-400 hover:bg-red-500/10 hover:text-red-400" : "bg-zinc-200/50 text-zinc-600 hover:bg-red-500/10 hover:text-red-600"}`}
                            >
                                <Trash2 size={15} />
                            </button>
                            <button onClick={() => setIsMaximized(!isMaximized)} className={`h-9 w-9 flex items-center justify-center rounded-xl transition-all ${isDarkMode ? "bg-white/5 text-zinc-400 hover:bg-white/10 hover:text-white" : "bg-zinc-200/50 text-zinc-600 hover:bg-zinc-200"}`}>
                                {isMaximized ? <Minimize2 size={15} /> : <Maximize2 size={15} />}
                            </button>
                            <button onClick={() => setIsOpen(false)} className={`h-9 w-9 flex items-center justify-center rounded-xl transition-all ${isDarkMode ? "bg-white/5 text-zinc-400 hover:bg-white/10 hover:text-white" : "bg-zinc-200/50 text-zinc-600 hover:bg-zinc-200"}`}>
                                <X size={18} />
                            </button>
                        </div>
                    </header>

                    <div ref={scrollRef} className={`flex-1 overflow-y-auto ${typeof window !== 'undefined' && window.innerWidth < 640 ? "px-4 pt-4" : "px-6 pt-6"} space-y-10 scrollbar-none pb-8 transition-colors
                        ${isDarkMode ? "bg-transparent" : "bg-zinc-50/50"}`}>
                        {messages.length === 0 && (
                            <div className="h-full flex flex-col items-center justify-center text-center opacity-40 py-20 px-10">
                                <div className="h-20 w-20 rounded-3xl bg-accent/10 flex items-center justify-center mb-6 animate-float">
                                    <Sparkles size={40} className="text-accent" />
                                </div>
                                <h4 className="text-lg font-black tracking-tight mb-2">Omni-Agent Strategy Terminal</h4>
                                <p className="text-xs font-medium max-w-[240px] leading-relaxed">System ready for market directive, quantitative analysis, or portfolio risk auditing.</p>
                            </div>
                        )}
                        {messages.map((m, i) => (
                            <div key={i} className={`flex ${m.role === "user" ? "justify-end" : "justify-start"} message-animate`}>
                                <div className={`${isMaximized ? "max-w-[75%]" : "max-w-full"} space-y-3`}>
                                    <div className={`py-5 px-6 rounded-[28px] transition-all duration-300 shadow-lg relative
                                        ${m.role === "user"
                                            ? (isDarkMode ? "bg-white text-black rounded-tr-none shadow-white/5" : "bg-indigo-600 text-white rounded-tr-none shadow-indigo-600/20")
                                            : (isDarkMode ? "bg-white/[0.05] text-zinc-100 rounded-tl-none border border-white/10" : "bg-white text-zinc-900 rounded-tl-none border border-zinc-200 shadow-xl")
                                        }`}>

                                        {m.role === "assistant" && (
                                            <div className={`absolute -top-3 -left-3 h-8 w-8 rounded-full border-4 border-background flex items-center justify-center shadow-lg
                                                ${isDarkMode ? "bg-zinc-800 text-fuchsia-400 border-zinc-950" : "bg-white text-indigo-600 border-zinc-50"}`}>
                                                <Bot size={14} />
                                            </div>
                                        )}

                                        <div
                                            style={{ fontSize: '108%', lineHeight: '1.7' }}
                                            className={`prose prose-sm max-w-full break-normal
                                            ${m.role === "user" ? (isDarkMode ? "prose-zinc" : "prose-invert") : (isDarkMode ? "prose-invert" : "prose-zinc")}
                                            prose-p:mb-5 last:prose-p:mb-0
                                            prose-strong:font-black prose-code:px-2 prose-code:py-0.5 prose-code:rounded-lg prose-code:font-mono
                                            ${isDarkMode ? "prose-strong:text-fuchsia-400 prose-code:text-emerald-400 prose-code:bg-emerald-400/5" : "prose-strong:text-indigo-600 prose-code:text-emerald-600 prose-code:bg-emerald-50"}
                                        `}>
                                            {m.reasoning && (
                                                <div className={`mb-6 p-4 rounded-2xl border italic text-[11px] leading-relaxed font-mono
                                                    ${isDarkMode ? "bg-white/[0.03] border-white/5 text-zinc-500" : "bg-zinc-50 border-zinc-100 text-zinc-400"}`}>
                                                    <div className="flex items-center gap-2 mb-2 opacity-50">
                                                        <Activity size={10} className="animate-pulse" />
                                                        <span className="font-black uppercase tracking-[0.2em] text-[9px]">Neural Synthesis Path</span>
                                                    </div>
                                                    {m.reasoning}
                                                </div>
                                            )}
                                            {m.content === "" && m.role === "assistant" && isLoading ? (
                                                <div className="flex gap-2.5 items-center h-10 px-2">
                                                    <div className="w-2.5 h-2.5 bg-accent/40 rounded-full animate-bounce [animation-delay:-0.3s]"></div>
                                                    <div className="w-2.5 h-2.5 bg-accent/60 rounded-full animate-bounce [animation-delay:-0.15s]"></div>
                                                    <div className="w-2.5 h-2.5 bg-accent rounded-full animate-bounce"></div>
                                                </div>
                                            ) : (
                                                <ReactMarkdown remarkPlugins={[remarkGfm, remarkMath]} rehypePlugins={[[rehypeKatex, { strict: false, throwOnError: false }]]}>
                                                    {preprocessMarkdown(m.content)}
                                                </ReactMarkdown>
                                            )}
                                        </div>
                                    </div>
                                    {m.role === "assistant" && (
                                        <div className="flex items-center gap-3 px-2 opacity-40 hover:opacity-100 transition-opacity">
                                            <span className="text-[9px] font-black tracking-widest uppercase flex items-center gap-1">
                                                <ShieldCheck size={10} /> Compliant Analysis
                                            </span>
                                            <span className="text-[9px] font-black tracking-widest uppercase">
                                                Ref: Core-{i}
                                            </span>
                                        </div>
                                    )}
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
