"use client"

import { useState, useRef, useEffect } from "react";

type Model = "general" | "mistral" | "mixtral" | "glm5";

export default function ChatWidget() {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState<{ role: string, content: string, reasoning?: string }[]>([]);
    const [input, setInput] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [selectedModel, setSelectedModel] = useState<Model>("general");
    const scrollRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (scrollRef.current) {
            scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
        }
    }, [messages]);

    const handleSend = async () => {
        if (!input) return;

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

            if (selectedModel === "general") {
                // Non-streaming fallback for general agent
                const response = await fetch(endpoint, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: input, user_id: 1 })
                });
                const data = await response.json();
                setMessages(prev => {
                    const updated = [...prev];
                    updated[assistantMsgIndex] = { role: "assistant", content: data.response };
                    return updated;
                });
            } else {
                const response = await fetch(endpoint, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: input, user_id: 1 })
                });

                if (!response.body) throw new Error("No body");
                const reader = response.body.getReader();
                const decoder = new TextDecoder();

                let accumulatedContent = "";
                let accumulatedReasoning = "";

                while (true) {
                    const { done, value } = await reader.read();
                    if (done) break;

                    const chunk = decoder.decode(value, { stream: true });

                    if (selectedModel === "glm5") {
                        // GLM-5 sends JSON lines
                        const lines = chunk.split("\n");
                        for (const line of lines) {
                            if (!line.trim()) continue;
                            try {
                                const data = JSON.parse(line);
                                accumulatedReasoning += data.reasoning || "";
                                accumulatedContent += data.content || "";
                            } catch (e) {
                                console.error("Error parsing NDJSON", e);
                            }
                        }
                    } else {
                        // Other models send raw text chunks
                        accumulatedContent += chunk;
                    }

                    setMessages(prev => {
                        const updated = [...prev];
                        updated[assistantMsgIndex] = {
                            role: "assistant",
                            content: accumulatedContent,
                            reasoning: accumulatedReasoning
                        };
                        return updated;
                    });
                }
            }
        } catch (error) {
            console.error(error);
            setMessages(prev => {
                const updated = [...prev];
                updated[assistantMsgIndex] = { role: "assistant", content: "Error communicating with AI. Check backend." };
                return updated;
            });
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="fixed bottom-6 right-6 z-50">
            {isOpen ? (
                <div className="w-[400px] h-[500px] bg-zinc-950 border border-zinc-800 rounded-3xl shadow-[0_20px_50px_rgba(0,0,0,0.5)] flex flex-col overflow-hidden animate-in fade-in zoom-in duration-200">
                    <header className="p-5 border-b border-zinc-800 bg-zinc-900/50 flex justify-between items-center backdrop-blur-md">
                        <div className="flex flex-col">
                            <span className="font-bold text-sm text-zinc-100">Asset Manager AI</span>
                            <select
                                value={selectedModel}
                                onChange={(e) => setSelectedModel(e.target.value as Model)}
                                className="bg-transparent text-[10px] text-zinc-400 border-none p-0 focus:ring-0 cursor-pointer hover:text-blue-400 transition-colors uppercase tracking-widest font-semibold"
                            >
                                <option value="general" className="bg-zinc-900">General Assistant</option>
                                <option value="mistral" className="bg-zinc-900">Mistral Large 3</option>
                                <option value="mixtral" className="bg-zinc-900">Mixtral 8x22B</option>
                                <option value="glm5" className="bg-zinc-900">GLM-5 (Thinking)</option>
                            </select>
                        </div>
                        <button onClick={() => setIsOpen(false)} className="h-8 w-8 flex items-center justify-center rounded-full hover:bg-zinc-800 text-zinc-400 hover:text-white transition-all">✕</button>
                    </header>

                    <div ref={scrollRef} className="flex-1 overflow-y-auto p-5 space-y-6 text-sm scroll-smooth">
                        {messages.map((m, i) => (
                            <div key={i} className={`flex ${m.role === "user" ? "justify-end" : "justify-start"}`}>
                                <div className={`max-w-[85%] flex flex-col ${m.role === "user" ? "items-end" : "items-start"}`}>
                                    {m.reasoning && (
                                        <div className="mb-2 p-3 rounded-2xl bg-zinc-900/30 border border-zinc-800/50 text-[11px] text-zinc-500 italic font-light italic leading-relaxed">
                                            <span className="block text-[9px] uppercase tracking-tighter mb-1 opacity-50 not-italic">Thought Process</span>
                                            {m.reasoning}
                                        </div>
                                    )}
                                    <div className={`p-3.5 rounded-2xl ${m.role === "user"
                                        ? "bg-blue-600 text-white rounded-tr-none shadow-lg shadow-blue-900/20"
                                        : "bg-zinc-800/60 text-zinc-100 rounded-tl-none border border-zinc-700/30"
                                        }`}>
                                        {m.content || (isLoading && i === messages.length - 1 ? <span className="animate-pulse">...</span> : null)}
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>

                    <div className="p-5 border-t border-zinc-800 bg-zinc-900/20">
                        <div className="relative flex items-center">
                            <input
                                value={input}
                                onChange={(e) => setInput(e.target.value)}
                                onKeyDown={(e) => e.key === "Enter" && !isLoading && handleSend()}
                                className="w-full bg-zinc-800/50 border border-zinc-700 rounded-2xl p-4 pr-14 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/50 transition-all placeholder:text-zinc-500"
                                placeholder="Write a message..."
                                disabled={isLoading}
                            />
                            <button
                                onClick={handleSend}
                                disabled={isLoading || !input}
                                className="absolute right-2 p-2 px-4 rounded-xl text-sm font-semibold transition-all bg-blue-600 hover:bg-blue-500 text-white shadow-lg disabled:opacity-50 disabled:grayscale"
                            >
                                Send
                            </button>
                        </div>
                    </div>
                </div>
            ) : (
                <button
                    onClick={() => setIsOpen(true)}
                    className="h-16 w-16 bg-gradient-to-tr from-blue-700 to-blue-500 rounded-full shadow-[0_10px_30px_rgba(37,99,235,0.4)] flex items-center justify-center hover:scale-110 hover:rotate-3 active:scale-95 transition-all duration-300 group"
                >
                    <span className="text-3xl group-hover:drop-shadow-[0_0_10px_rgba(255,255,255,0.5)]">🤖</span>
                </button>
            )}
        </div>
    );
}
