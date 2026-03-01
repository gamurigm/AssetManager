import { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import "katex/dist/katex.min.css";

import {
    Send, Sparkles, Bot, Activity, FileText, Copy, Check, ShieldCheck, Loader2, Trash2
} from "lucide-react";

interface Session {
    id: string;
    title: string;
    agent?: string;
    messages: { role: string; content: string; reasoning?: string }[];
}

interface ChatPaneProps {
    session: Session;
    isDarkMode: boolean;
    isMaximized: boolean;
    selectedModel: string;
    holdings: any[];
    totalValue: number;
    totalPnL: number;
    pnlPercent: number;
    onUpdateMessages: (id: string, updater: (prev: Session["messages"]) => Session["messages"]) => void;
    onUpdateTitle: (id: string, title: string) => void;
    onUpdateAgent: (id: string, agent: string) => void;
}

export default function ChatPane({
    session, isDarkMode, isMaximized, selectedModel,
    holdings, totalValue, totalPnL, pnlPercent,
    onUpdateMessages, onUpdateTitle, onUpdateAgent
}: ChatPaneProps) {
    const [input, setInput] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [copiedIdx, setCopiedIdx] = useState<number | null>(null);
    const scrollRef = useRef<HTMLDivElement>(null);

    const selectedAgent = session.agent || "auto";
    const messages = session.messages;

    useEffect(() => {
        if (scrollRef.current) scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }, [messages, isMaximized]);

    const preprocessMarkdown = (text: string) => {
        if (!text) return "";
        let p = text;
        p = p.replace(/\\\[/g, "\n$$\n").replace(/\\\]/g, "\n$$\n");
        p = p.replace(/\\\(/g, " $ ").replace(/\\\)/g, " $ ");
        p = p.replace(/(^|\n)\s*\$\s*\n([\s\S]+?)\n\s*\$\s*(\n|$)/g, "$1\n$$\n$2\n$$\n$3");
        p = p.replace(/\$\$([\s\S]+?)\$\$/g, (_, p1) => `\n\n$$\n${p1.trim()}\n$$\n\n`);
        return p;
    };

    const copyToClipboard = (text: string, idx: number) => {
        navigator.clipboard.writeText(text);
        setCopiedIdx(idx);
        setTimeout(() => setCopiedIdx(null), 2000);
    };

    const handleGenerateReport = async () => {
        setIsLoading(true);
        const reportMsg = {
            role: "user",
            content: "Generate a comprehensive risk analysis report (PDF) for my current portfolio. Include all metrics: VaR, Sharpe Ratio, Expected Value, Risk Adjusted Return, Momentum analysis, hedging strategy, and equity trend projections."
        };
        onUpdateMessages(session.id, prev => [...prev, reportMsg, { role: "assistant", content: "", reasoning: "" }]);

        const assistantIdx = messages.length + 1;

        try {
            const endpoint = "http://127.0.0.1:8282/api/v1/agents/chat";
            const res = await fetch(endpoint, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    message: reportMsg.content,
                    user_id: 1,
                    session_id: session.id,
                    portfolio: {
                        holdings: holdings.filter(h => h.price > 0),
                        total_value: totalValue,
                        total_pnl: totalPnL,
                        pnl_percent: pnlPercent,
                        timestamp: new Date().toISOString(),
                    },
                }),
            });

            if (!res.body) throw new Error("No body");
            const reader = res.body.getReader();
            const decoder = new TextDecoder();
            let acc = "";

            while (true) {
                const { done, value } = await reader.read();
                if (done) break;
                acc += decoder.decode(value, { stream: true });
                onUpdateMessages(session.id, prev => {
                    const u = [...prev];
                    u[assistantIdx] = { role: "assistant", content: acc };
                    return u;
                });
            }

            const pdfRes = await fetch("http://127.0.0.1:8282/api/v1/portfolios/report", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    holdings: holdings.filter(h => h.price > 0),
                    total_value: totalValue,
                    total_pnl: totalPnL,
                }),
            });

            if (pdfRes.ok) {
                const data = await pdfRes.json();
                const pdfLink = `\n\n📄 **[Download PDF Report](${data.url})**`;
                onUpdateMessages(session.id, prev => {
                    const u = [...prev];
                    u[assistantIdx] = { ...u[assistantIdx], content: u[assistantIdx].content + pdfLink };
                    return u;
                });
            }
        } catch {
            onUpdateMessages(session.id, prev => {
                const u = [...prev];
                u[assistantIdx] = { role: "assistant", content: "⚠️ **Report generation failed. Check backend connection.**" };
                return u;
            });
        } finally {
            setIsLoading(false);
        }
    };

    const handleSend = async () => {
        if (!input.trim()) return;
        const userMsg = { role: "user", content: input };
        onUpdateMessages(session.id, prev => [...prev, userMsg]);
        setInput("");
        setIsLoading(true);
        const assistantMsgIndex = messages.length + 1;
        onUpdateMessages(session.id, prev => [...prev, { role: "assistant", content: "", reasoning: "" }]);

        if (messages.length === 0 && session.title.startsWith("Chat")) {
            onUpdateTitle(session.id, input.slice(0, 30) + (input.length > 30 ? "…" : ""));
        }

        try {
            const endpoint = (selectedModel === "general" || selectedAgent !== "auto")
                ? "http://127.0.0.1:8282/api/v1/agents/chat"
                : `http://127.0.0.1:8282/api/v1/agents/chat/${selectedModel}`;

            const response = await fetch(endpoint, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    message: userMsg.content,
                    user_id: 1,
                    session_id: session.id,
                    target_agent: selectedAgent,
                    history: messages.map(m => ({ role: m.role, content: m.content })),
                    portfolio: {
                        holdings: holdings.filter(h => h.price > 0),
                        total_value: totalValue,
                        total_pnl: totalPnL,
                        pnl_percent: pnlPercent,
                        timestamp: new Date().toISOString(),
                    },
                }),
            });

            if (!response.body) throw new Error("No body");
            const reader = response.body.getReader();
            const decoder = new TextDecoder();
            let accC = ""; let accR = "";

            while (true) {
                const { done, value } = await reader.read();
                if (done) break;
                const chunk = decoder.decode(value, { stream: true });

                if (selectedModel === "deepseek") {
                    for (const line of chunk.split("\n")) {
                        if (!line.trim()) continue;
                        try {
                            const data = JSON.parse(line);
                            accR += data.reasoning || "";
                            accC += data.content || "";
                        } catch {
                            accC += line;
                        }
                    }
                } else {
                    accC += chunk;
                }

                if (accC.includes("<think>")) {
                    const parts = accC.split("</think>");
                    if (parts.length > 1) {
                        accR += (parts[0].split("<think>")[1] || "");
                        accC = parts[1].trim();
                    } else {
                        const op = accC.split("<think>");
                        accC = op[0].trim();
                        accR += op[1] || "";
                    }
                }

                onUpdateMessages(session.id, prev => {
                    const u = [...prev];
                    u[assistantMsgIndex] = { role: "assistant", content: accC, reasoning: accR };
                    return u;
                });
            }
        } catch {
            onUpdateMessages(session.id, prev => {
                const u = [...prev];
                u[assistantMsgIndex] = { role: "assistant", content: "⚠️ **Link Error.**" };
                return u;
            });
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className={`flex-1 flex flex-col min-h-0 border-r last:border-r-0 transition-colors ${isDarkMode ? "border-white/5 bg-transparent" : "border-zinc-200 bg-zinc-50/50"}`}>

            {/* ── AGENT SELECTOR HEADER (PER PANE) ────────────────────── */}
            <div className={`px-4 py-2 border-b flex justify-between items-center z-20 ${isDarkMode ? "border-white/5 bg-white/[0.02]" : "border-zinc-200/50 bg-white/50"} shadow-sm`}>
                <div className={`text-[11px] font-black uppercase tracking-widest ${isDarkMode ? "text-white" : "text-black"}`}>
                    {session.title}
                </div>
                <div className="flex items-center gap-2">
                    <Bot size={11} className={isDarkMode ? "text-fuchsia-400" : "text-indigo-500"} />
                    <select
                        value={selectedAgent}
                        onChange={(e) => onUpdateAgent(session.id, e.target.value)}
                        className={`bg-transparent text-[11px] border-none p-0 focus:ring-0 cursor-pointer font-bold outline-none
                            ${isDarkMode ? "text-zinc-400 hover:text-fuchsia-400" : "text-zinc-500 hover:text-indigo-600"}`}
                        title="Select Sub-Agent Specialist"
                    >
                        <option value="auto" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>🤖 Auto (Orchestrator)</option>
                        <option value="Quantitative Analyst" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>📈 Quant Analyst</option>
                        <option value="Fundamental Analyst" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>🏢 Fundamental Analyst</option>
                        <option value="Risk Manager" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>🛡️ Risk Manager</option>
                        <option value="Macro Analyst" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>🌍 Macro Analyst</option>
                        <option value="Strategy Analyst" className={isDarkMode ? "bg-zinc-950" : "bg-white text-zinc-900"}>⚡ Strategy Analyst</option>
                    </select>
                    <button
                        onClick={() => onUpdateMessages(session.id, () => [])}
                        title="Clear Chat"
                        className={`h-7 w-7 rounded-lg flex items-center justify-center transition-all 
                        ${isDarkMode ? "bg-white/5 text-zinc-400 hover:bg-red-500/20 hover:text-red-400" : "bg-zinc-100 text-zinc-500 hover:bg-red-50 hover:text-red-500"}`}
                    >
                        <Trash2 size={12} />
                    </button>
                </div>
            </div>

            {/* ── MESSAGES ───────────────────────────────── */}
            <div ref={scrollRef} className="flex-1 overflow-y-auto px-5 pt-5 space-y-6 scrollbar-none pb-6 relative">

                {/* Session Title subtle floating label in background */}
                <div className={`absolute top-4 left-5 right-5 text-center text-[10px] uppercase font-black tracking-widest pointer-events-none transition-opacity
                    ${messages.length > 0 ? "opacity-5" : "opacity-0"} ${isDarkMode ? "text-white" : "text-black"}`}>
                    {selectedAgent !== "auto" ? selectedAgent : "Orchestrator"}
                </div>

                {messages.length === 0 && (
                    <div className="h-full flex flex-col items-center justify-center text-center opacity-40 py-16 px-8 relative z-10">
                        <div className="h-16 w-16 rounded-2xl bg-accent/10 flex items-center justify-center mb-5 animate-float">
                            <Sparkles size={32} className="text-accent" />
                        </div>
                        <h4 className={`text-base font-black tracking-tight mb-2 ${isDarkMode ? "text-white" : "text-zinc-900"}`}>Omni-Agent Strategy Terminal</h4>
                        <p className={`text-[11px] font-medium max-w-[220px] leading-relaxed mb-6 ${isDarkMode ? "text-white/70" : "text-zinc-500"}`}>System ready for market directive or portfolio analysis.</p>

                        <div className="flex flex-wrap gap-2 justify-center max-w-[320px]">
                            <button onClick={handleGenerateReport}
                                className={`px-3 py-1.5 rounded-xl text-[10px] font-bold flex items-center gap-1.5 border transition-all
                                    ${isDarkMode ? "border-accent/20 text-accent hover:bg-accent/10" : "border-indigo-200 text-indigo-600 hover:bg-indigo-50"}`}>
                                <FileText size={11} /> Generate Risk Report
                            </button>
                            <button onClick={() => { setInput("Analyze my portfolio risk and suggest hedging strategies"); }}
                                className={`px-3 py-1.5 rounded-xl text-[10px] font-bold flex items-center gap-1.5 border transition-all
                                    ${isDarkMode ? "border-white/10 text-zinc-400 hover:bg-white/5" : "border-zinc-200 text-zinc-500 hover:bg-zinc-50"}`}>
                                <ShieldCheck size={11} /> Hedging Analysis
                            </button>
                        </div>
                    </div>
                )}

                {messages.map((m, i) => (
                    <div key={i} className={`flex relative z-10 ${m.role === "user" ? "justify-end" : "justify-start"} message-animate`}>
                        <div className={`${isMaximized ? "max-w-[85%]" : "max-w-[92%]"} space-y-2`}>

                            {m.role === "user" ? (
                                <div className={`py-3 px-5 rounded-2xl rounded-tr-sm text-[15.2px] leading-relaxed font-bold shadow-md
                                    ${isDarkMode
                                        ? "bg-gradient-to-br from-fuchsia-600 to-violet-700 text-white shadow-fuchsia-600/20"
                                        : "bg-gradient-to-br from-indigo-600 to-violet-600 text-white shadow-indigo-600/20"}`}>
                                    {m.content}
                                </div>
                            ) : (
                                <div className={`relative rounded-2xl rounded-tl-sm overflow-hidden transition-all duration-300 shadow-lg
                                    ${isDarkMode
                                        ? "bg-gradient-to-b from-white/[0.06] to-white/[0.02] border border-white/[0.08]"
                                        : "bg-white border border-zinc-200/80 shadow-xl"}`}>

                                    <div className={`flex items-center gap-2 px-4 py-2 border-b
                                        ${isDarkMode ? "border-white/5 bg-white/[0.02]" : "border-zinc-100 bg-zinc-50/50"}`}>
                                        <div className={`h-5 w-5 rounded-md flex items-center justify-center
                                            ${isDarkMode ? "bg-fuchsia-500/20 text-fuchsia-400" : "bg-indigo-100 text-indigo-600"}`}>
                                            <Bot size={11} />
                                        </div>
                                        <div className="flex flex-col">
                                            <span className={`text-[9px] font-black uppercase tracking-[0.15em] leading-tight
                                                ${isDarkMode ? "text-zinc-500" : "text-zinc-400"}`}>
                                                {selectedAgent !== "auto" ? selectedAgent : "Alpha Intelligence"}
                                            </span>
                                            {selectedModel !== "general" && (
                                                <span className={`text-[8px] font-bold uppercase
                                                    ${isDarkMode ? "text-fuchsia-500/50" : "text-indigo-400"}`}>
                                                    {selectedModel} model
                                                </span>
                                            )}
                                        </div>
                                        <div className="flex-1" />
                                        <button onClick={() => copyToClipboard(m.content, i)} className="opacity-0 group-hover:opacity-100 transition-opacity"
                                            title="Copy">
                                            {copiedIdx === i
                                                ? <Check size={11} className="text-emerald-400" />
                                                : <Copy size={11} className={isDarkMode ? "text-zinc-600 hover:text-zinc-400" : "text-zinc-400 hover:text-zinc-600"} />}
                                        </button>
                                    </div>

                                    {m.reasoning && (
                                        <div className={`mx-3 mt-3 p-3 rounded-xl text-[10px] leading-relaxed font-mono
                                            ${isDarkMode ? "bg-amber-500/5 border border-amber-500/10 text-amber-300/60" : "bg-amber-50 border border-amber-100 text-amber-700/50"}`}>
                                            <div className="flex items-center gap-1.5 mb-1.5 opacity-60">
                                                <Activity size={9} className="animate-pulse" />
                                                <span className="font-black uppercase tracking-[0.2em] text-[8px]">Neural Synthesis</span>
                                            </div>
                                            <div className="whitespace-pre-wrap">{m.reasoning}</div>
                                        </div>
                                    )}

                                    <div className={`px-4 py-3 text-[15.2px] leading-[1.8] group
                                        prose prose-base max-w-full break-normal
                                        ${isDarkMode ? "prose-invert" : "prose-zinc"}
                                        prose-p:mb-4 last:prose-p:mb-0
                                        prose-headings:font-black prose-headings:tracking-tight
                                        prose-strong:font-extrabold
                                        prose-code:px-1.5 prose-code:py-0.5 prose-code:rounded-md prose-code:font-mono prose-code:text-[11px]
                                        prose-table:text-[11px]
                                        prose-th:px-3 prose-th:py-2 prose-td:px-3 prose-td:py-1.5
                                        prose-a:text-accent prose-a:no-underline prose-a:font-bold hover:prose-a:underline
                                        ${isDarkMode
                                            ? "prose-strong:text-fuchsia-300 prose-code:text-emerald-400 prose-code:bg-emerald-400/5 prose-th:bg-white/5 prose-th:text-zinc-400"
                                            : "prose-strong:text-indigo-700 prose-code:text-emerald-700 prose-code:bg-emerald-50 prose-th:bg-zinc-50 prose-th:text-zinc-500"}`}>

                                        {m.content === "" && isLoading ? (
                                            <div className="flex items-center gap-3 h-8 px-1">
                                                <Loader2 size={14} className="animate-spin text-accent" />
                                                <span className={`text-[10px] font-black uppercase tracking-widest animate-pulse ${isDarkMode ? "text-zinc-600" : "text-zinc-400"}`}>
                                                    Processing…
                                                </span>
                                            </div>
                                        ) : (
                                            <ReactMarkdown
                                                remarkPlugins={[remarkGfm, remarkMath]}
                                                rehypePlugins={[[rehypeKatex, { strict: false, throwOnError: false }]]}
                                                components={{
                                                    a: ({ node, ...props }) => <a target="_blank" rel="noopener noreferrer" {...props} />
                                                }}
                                            >
                                                {preprocessMarkdown(m.content)}
                                            </ReactMarkdown>
                                        )}
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>
                ))}
            </div>

            {/* ── INPUT BAR ──────────────────────────────── */}
            <div className={`px-5 py-4 border-t ${isDarkMode ? "bg-black/40 border-white/5" : "bg-white/80 border-zinc-100"}`}>

                {messages.length > 0 && !isLoading && (
                    <div className="flex gap-2 mb-3 overflow-x-auto scrollbar-none pb-1">
                        <button onClick={handleGenerateReport}
                            className={`shrink-0 px-3 py-1 rounded-full text-[9px] font-bold flex items-center gap-1 border transition-all
                                ${isDarkMode ? "border-accent/20 text-accent/70 hover:bg-accent/10 hover:text-accent" : "border-indigo-200 text-indigo-500 hover:bg-indigo-50"}`}>
                            <FileText size={9} /> Report PDF
                        </button>
                    </div>
                )}

                <div className={`relative flex items-center rounded-2xl border transition-all duration-300
                    ${isDarkMode ? "bg-white/[0.04] border-white/10 focus-within:border-fuchsia-500/30 focus-within:shadow-[0_0_20px_-5px_#d946ef30]"
                        : "bg-white border-zinc-200 shadow-sm focus-within:border-indigo-400 focus-within:shadow-[0_0_20px_-5px_#6366f130]"}`}>
                    <input
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyDown={(e) => e.key === "Enter" && !isLoading && handleSend()}
                        className={`w-full bg-transparent py-3.5 px-5 text-[16.5px] font-medium focus:outline-none
                            ${isDarkMode ? "text-white placeholder:text-zinc-700" : "text-zinc-900 placeholder:text-zinc-400"}`}
                        placeholder={`Type a directive for ${session.title}…`}
                        disabled={isLoading}
                    />
                    <button
                        onClick={handleSend}
                        disabled={isLoading}
                        className={`mr-2 h-9 w-9 rounded-xl text-white flex items-center justify-center transition-all flex-shrink-0
                            ${isLoading ? "opacity-40 cursor-not-allowed" : ""}
                            ${isDarkMode ? "bg-fuchsia-600 hover:bg-fuchsia-500" : "bg-indigo-600 hover:bg-indigo-500"}`}
                    >
                        {isLoading ? <Loader2 size={16} className="animate-spin" /> : <Send size={16} />}
                    </button>
                </div>
            </div>
        </div>
    );
}
