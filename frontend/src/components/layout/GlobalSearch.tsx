"use client"

import { useState, useEffect, useRef, useCallback } from "react";
import { useRouter } from "next/navigation";
import { Search, X, TrendingUp, Clock, Star } from "lucide-react";

/* ─── Popular / Default Suggestions ──────────────────────────────────── */
const POPULAR_SYMBOLS = [
    { symbol: "AAPL", name: "Apple Inc.", sector: "Technology" },
    { symbol: "MSFT", name: "Microsoft Corp.", sector: "Technology" },
    { symbol: "NVDA", name: "NVIDIA Corp.", sector: "Technology" },
    { symbol: "TSLA", name: "Tesla Inc.", sector: "Automotive" },
    { symbol: "GOOG", name: "Alphabet Inc.", sector: "Technology" },
    { symbol: "AMZN", name: "Amazon.com Inc.", sector: "Consumer" },
    { symbol: "META", name: "Meta Platforms", sector: "Technology" },
    { symbol: "JPM", name: "JPMorgan Chase", sector: "Finance" },
    { symbol: "GS", name: "Goldman Sachs", sector: "Finance" },
    { symbol: "COIN", name: "Coinbase Global", sector: "Crypto" },
    { symbol: "EURUSD=X", name: "EUR/USD", sector: "Forex" },
    { symbol: "GC=F", name: "Gold Futures", sector: "Commodities" },
    { symbol: "BTC-USD", name: "Bitcoin USD", sector: "Crypto" },
    { symbol: "ETH-USD", name: "Ethereum USD", sector: "Crypto" },
    { symbol: "^GSPC", name: "S&P 500", sector: "Index" },
    { symbol: "^DJI", name: "Dow Jones", sector: "Index" },
    { symbol: "^N225", name: "Nikkei 225", sector: "Index" },
    { symbol: "SPY", name: "SPDR S&P 500 ETF", sector: "ETF" },
    { symbol: "QQQ", name: "Invesco QQQ Trust", sector: "ETF" },
    { symbol: "LMT", name: "Lockheed Martin", sector: "Defense" },
    { symbol: "PLTR", name: "Palantir Technologies", sector: "Technology" },
    { symbol: "ZT=F", name: "US 2-Year T-Note", sector: "Bonds" },
    { symbol: "CHFJPY=X", name: "CHF/JPY", sector: "Forex" },
];

const SECTOR_COLORS: Record<string, string> = {
    Technology: "text-blue-400",
    Finance: "text-emerald-400",
    Forex: "text-purple-400",
    Crypto: "text-orange-400",
    Commodities: "text-yellow-400",
    Index: "text-cyan-400",
    ETF: "text-teal-400",
    Automotive: "text-red-400",
    Consumer: "text-pink-400",
    Defense: "text-slate-400",
    Bonds: "text-amber-400",
};

// In-memory frontend cache to deliver instant results for repeated queries
const globalResultsCache = new Map<string, any[]>();

export default function GlobalSearch() {
    const [isOpen, setIsOpen] = useState(false);
    const [query, setQuery] = useState("");
    const [apiResults, setApiResults] = useState<any[]>([]);
    const [isSearching, setIsSearching] = useState(false);

    const [selectedIndex, setSelectedIndex] = useState(0);
    const [recentSearches, setRecentSearches] = useState<string[]>([]);
    const [theme, setTheme] = useState<'light' | 'dark'>('dark');
    const inputRef = useRef<HTMLInputElement>(null);
    const router = useRouter();

    useEffect(() => {
        const checkTheme = () => setTheme(document.documentElement.classList.contains('light') ? 'light' : 'dark');
        checkTheme();
        const observer = new MutationObserver(checkTheme);
        observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
        return () => observer.disconnect();
    }, []);

    const isLight = theme === 'light';

    // Load recent searches from localStorage
    useEffect(() => {
        try {
            const saved = localStorage.getItem("mmam_recent_searches");
            if (saved) setRecentSearches(JSON.parse(saved));
        } catch { }
    }, []);

    // Global keyboard shortcut: Ctrl+K or Cmd+K
    useEffect(() => {
        const handleKeyDown = (e: KeyboardEvent) => {
            if ((e.ctrlKey || e.metaKey) && e.key === "k") {
                e.preventDefault();
                setIsOpen(true);
            }
            if (e.key === "Escape") {
                setIsOpen(false);
                setQuery("");
                setApiResults([]);
            }
        };
        window.addEventListener("keydown", handleKeyDown);
        return () => window.removeEventListener("keydown", handleKeyDown);
    }, []);

    // Focus input when modal opens
    useEffect(() => {
        if (isOpen) {
            setTimeout(() => inputRef.current?.focus(), 50);
        }
    }, [isOpen]);

    // Fetch from backend — only triggered manually (Enter key)
    const fetchResults = useCallback(async (q: string) => {
        if (!q) return;

        const queryKey = q.toLowerCase();

        // Instantly return from in-memory cache if available
        if (globalResultsCache.has(queryKey)) {
            setApiResults(globalResultsCache.get(queryKey)!);
            return;
        }

        setIsSearching(true);
        try {
            const res = await fetch(`http://127.0.0.1:8282/api/v1/market/search?query=${encodeURIComponent(q)}&limit=15`);
            if (res.ok) {
                const data = await res.json();
                const results = data || [];
                globalResultsCache.set(queryKey, results);
                setApiResults(results);
            } else {
                setApiResults([]);
            }
        } catch {
            setApiResults([]);
        } finally {
            setIsSearching(false);
        }
    }, []);

    // Format local fallback
    const localResults = query.trim()
        ? POPULAR_SYMBOLS.filter(
            (s) =>
                s.symbol.toLowerCase().includes(query.toLowerCase()) ||
                s.name.toLowerCase().includes(query.toLowerCase())
        )
        : [];

    // Prioritize API results if available, else local filtered, else nothing
    const displayResults = apiResults.length > 0
        ? apiResults.map(r => ({ symbol: r.symbol, name: r.name, sector: r.type || "MARKET" }))
        : localResults;

    // If query doesn't match any known symbol, allow custom entry
    const showCustomEntry = query.trim().length > 0 && displayResults.length === 0 && !isSearching;

    // Reset selected index when results change
    useEffect(() => {
        setSelectedIndex(0);
    }, [query, displayResults.length]);

    const navigateToSymbol = useCallback((symbol: string) => {
        // Save to recent
        const updated = [symbol, ...recentSearches.filter((s) => s !== symbol)].slice(0, 8);
        setRecentSearches(updated);
        try { localStorage.setItem("mmam_recent_searches", JSON.stringify(updated)); } catch { }

        // Fire-and-forget: ensure historical data is being persisted to DuckDB
        fetch(`http://127.0.0.1:8282/api/v1/market/prefetch/${encodeURIComponent(symbol)}`, { method: "POST" }).catch(() => { });

        setIsOpen(false);
        setQuery("");
        setApiResults([]);
        router.push(`/chart/${encodeURIComponent(symbol)}`);
    }, [recentSearches, router]);

    // Keyboard navigation
    const handleKeyDown = useCallback(async (e: React.KeyboardEvent) => {
        const totalItems = showCustomEntry ? 1 : displayResults.length || recentSearches.length;

        if (e.key === "ArrowDown") {
            e.preventDefault();
            setSelectedIndex((prev) => Math.min(prev + 1, totalItems - 1));
        } else if (e.key === "ArrowUp") {
            e.preventDefault();
            setSelectedIndex((prev) => Math.max(prev - 1, 0));
        } else if (e.key === "Enter") {
            e.preventDefault();
            const trimmed = query.trim();
            if (!trimmed) return;

            // If we already have API/local results selected, navigate directly
            if (displayResults.length > 0) {
                navigateToSymbol(displayResults[selectedIndex]?.symbol || trimmed.toUpperCase());
                return;
            }

            // Otherwise: search first, then navigate to top result or exact query
            await fetchResults(trimmed);

            // After fetch, check if we now have results
            const cached = globalResultsCache.get(trimmed.toLowerCase());
            if (cached && cached.length > 0) {
                navigateToSymbol(cached[0].symbol);
            } else {
                navigateToSymbol(trimmed.toUpperCase());
            }
        }
    }, [displayResults, selectedIndex, query, showCustomEntry, recentSearches, navigateToSymbol, fetchResults]);

    const clearRecent = () => {
        setRecentSearches([]);
        try { localStorage.removeItem("mmam_recent_searches"); } catch { }
    };

    if (!isOpen) {
        return (
            <button
                onClick={() => setIsOpen(true)}
                className={`fixed top-3 left-1/2 -translate-x-1/2 z-50 flex items-center gap-2.5 px-4 py-2 
                    backdrop-blur-xl border transition-all duration-200 cursor-pointer group
                    shadow-[0_2px_20px_-4px_rgba(0,0,0,0.5)] rounded-xl
                    ${isLight
                        ? "bg-black/5 border-black/10 text-zinc-500 hover:text-zinc-900 hover:bg-black/[0.08]"
                        : "bg-white/[0.03] border-white/[0.06] text-white/40 hover:text-white/60 hover:bg-white/[0.07] shadow-[0_2px_20px_-4px_rgba(0,0,0,0.5)]"}`}
                style={{ minWidth: 280 }}
            >
                <Search size={14} className={isLight ? "text-zinc-400 group-hover:text-accent" : "text-white/30 group-hover:text-accent transition-colors"} />
                <span className="text-xs font-medium tracking-wide">Search global assets...</span>
                <kbd className={`ml-auto text-[10px] font-mono px-1.5 py-0.5 rounded border ${isLight ? "bg-black/5 border-black/5 text-zinc-400" : "bg-white/[0.06] border-white/[0.08] text-white/25"}`}>
                    Ctrl K
                </kbd>
            </button>
        );
    }

    return (
        <>
            {/* Backdrop */}
            <div
                className="fixed inset-0 z-[9998] bg-black/60 backdrop-blur-sm animate-fade-in"
                onClick={() => { setIsOpen(false); setQuery(""); setApiResults([]); }}
            />

            {/* Search Modal */}
            <div className="fixed top-[15vh] left-1/2 -translate-x-1/2 z-[9999] w-[560px] max-w-[90vw]">
                <div className={`border rounded-2xl shadow-[0_25px_60px_-12px_rgba(0,0,0,0.8)] overflow-hidden animate-scale-in
                    ${isLight ? "bg-white border-zinc-200" : "bg-[#111111] border-white/[0.08]"}`}>
                    {/* Search Input */}
                    <div className={`flex items-center gap-3 px-5 py-4 border-b ${isLight ? "border-zinc-100" : "border-white/[0.06]"}`}>
                        {isSearching ? <div className="h-4 w-4 border-2 border-accent border-t-transparent rounded-full animate-spin shrink-0" /> : <Search size={18} className="text-accent shrink-0" />}
                        <input
                            ref={inputRef}
                            type="text"
                            value={query}
                            onChange={(e) => setQuery(e.target.value)}
                            onKeyDown={handleKeyDown}
                            placeholder="Type symbol or name, press Enter to search..."
                            className={`flex-1 bg-transparent text-sm font-medium outline-none ${isLight ? "text-zinc-900 placeholder:text-zinc-400" : "text-white placeholder:text-white/25"}`}
                            spellCheck={false}
                            autoComplete="off"
                        />
                        {query && (
                            <button onClick={() => { setQuery(""); setApiResults([]); }} className="text-white/30 hover:text-white/60 transition-colors">
                                <X size={16} />
                            </button>
                        )}
                        <kbd className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-white/[0.06] border border-white/[0.08] text-white/20">
                            ESC
                        </kbd>
                    </div>

                    {/* Results */}
                    <div className="max-h-[50vh] overflow-y-auto">
                        {/* Display Results */}
                        {displayResults.length > 0 && (
                            <div className="py-2">
                                <p className={`px-5 py-1.5 text-[10px] font-black uppercase tracking-[0.2em] ${isLight ? "text-zinc-400" : "text-white/20"}`}>
                                    {apiResults.length > 0 ? "Global Market" : "Popular"}
                                </p>
                                {displayResults.map((item, i) => (
                                    <button
                                        key={item.symbol + i}
                                        onClick={() => navigateToSymbol(item.symbol)}
                                        onMouseEnter={() => setSelectedIndex(i)}
                                        className={`w-full flex items-center gap-4 px-5 py-3 text-left transition-all ${selectedIndex === i
                                            ? "bg-accent/10 border-l-2 border-accent"
                                            : "hover:bg-white/[0.03] border-l-2 border-transparent"
                                            }`}
                                    >
                                        <div className="h-8 w-8 rounded-lg bg-white/[0.04] flex items-center justify-center shrink-0">
                                            <TrendingUp size={14} className="text-accent" />
                                        </div>
                                        <div className="flex-1 min-w-0">
                                            <div className="flex items-center gap-2">
                                                <span className={`text-sm font-bold ${isLight ? "text-zinc-900" : "text-white"}`}>{item.symbol}</span>
                                                <span className={`text-[9px] font-black uppercase tracking-wider px-1.5 py-0.5 rounded-full ${isLight ? "bg-zinc-100" : "bg-white/[0.04]"} ${SECTOR_COLORS[item.sector] || (isLight ? "text-zinc-500" : "text-white/40")}`}>
                                                    {item.sector}
                                                </span>
                                            </div>
                                            <span className={`text-xs truncate block ${isLight ? "text-zinc-500" : "text-white/30"}`}>{item.name}</span>
                                        </div>
                                        <span className={`text-[10px] font-mono ${isLight ? "text-zinc-300" : "text-white/15"}`}>Enter ↵</span>
                                    </button>
                                ))}
                            </div>
                        )}

                        {/* Custom Entry */}
                        {showCustomEntry && (
                            <div className="py-2">
                                <p className="px-5 py-1.5 text-[10px] font-black uppercase tracking-[0.2em] text-white/20">
                                    Direct Search
                                </p>
                                <button
                                    onClick={() => navigateToSymbol(query.trim().toUpperCase())}
                                    className="w-full flex items-center gap-4 px-5 py-3 text-left bg-accent/10 border-l-2 border-accent"
                                >
                                    <div className="h-8 w-8 rounded-lg bg-accent/20 flex items-center justify-center shrink-0">
                                        <Search size={14} className="text-accent" />
                                    </div>
                                    <div className="flex-1">
                                        <span className={`text-sm font-bold ${isLight ? "text-zinc-900" : "text-white"}`}>{query.trim().toUpperCase()}</span>
                                        <span className={`text-xs block ${isLight ? "text-zinc-500" : "text-white/30"}`}>Open exact symbol globally</span>
                                    </div>
                                    <span className={`text-[10px] font-mono ${isLight ? "text-zinc-300" : "text-white/15"}`}>Enter ↵</span>
                                </button>
                            </div>
                        )}

                        {/* Recent Searches */}
                        {!query.trim() && recentSearches.length > 0 && (
                            <div className="py-2 border-t border-white/5">
                                <div className="flex items-center justify-between px-5 py-1.5">
                                    <p className="text-[10px] font-black uppercase tracking-[0.2em] text-white/20">
                                        Recent
                                    </p>
                                    <button onClick={clearRecent} className="text-[10px] text-white/20 hover:text-white/40 transition-colors">
                                        Clear
                                    </button>
                                </div>
                                {recentSearches.map((sym, i) => (
                                    <button
                                        key={sym}
                                        onClick={() => navigateToSymbol(sym)}
                                        onMouseEnter={() => setSelectedIndex(i + (apiResults.length || 0))} // Only if active
                                        className={`w-full flex items-center gap-4 px-5 py-2.5 text-left transition-all hover:bg-black/[0.02] border-l-2 border-transparent`}
                                    >
                                        <Clock size={14} className={isLight ? "text-zinc-300" : "text-white/20 shrink-0"} />
                                        <span className={`text-sm font-medium ${isLight ? "text-zinc-600" : "text-white/60"}`}>{sym}</span>
                                    </button>
                                ))}
                            </div>
                        )}

                        {/* Popular when empty & no recents */}
                        {!query.trim() && recentSearches.length === 0 && (
                            <div className="py-2">
                                <p className="px-5 py-1.5 text-[10px] font-black uppercase tracking-[0.2em] text-white/20">
                                    Trending Assets
                                </p>
                                {POPULAR_SYMBOLS.slice(0, 8).map((item, i) => (
                                    <button
                                        key={item.symbol}
                                        onClick={() => navigateToSymbol(item.symbol)}
                                        onMouseEnter={() => setSelectedIndex(i)}
                                        className={`w-full flex items-center gap-4 px-5 py-2.5 text-left transition-all ${selectedIndex === i
                                            ? (isLight ? "bg-black/[0.04] border-l-2 border-accent" : "bg-white/[0.04] border-l-2 border-accent/50")
                                            : "hover:bg-black/[0.01] border-l-2 border-transparent"
                                            }`}
                                    >
                                        <Star size={12} className="text-yellow-500/50 shrink-0" />
                                        <span className={`text-sm font-bold ${isLight ? "text-zinc-700" : "text-white/60"}`}>{item.symbol}</span>
                                        <span className={`text-xs truncate ${isLight ? "text-zinc-400" : "text-white/20"}`}>{item.name}</span>
                                    </button>
                                ))}
                            </div>
                        )}
                    </div>

                    {/* Footer */}
                    <div className="flex items-center gap-4 px-5 py-2.5 border-t border-white/[0.06] text-[10px] text-white/15">
                        <span><kbd className="font-mono px-1 py-0.5 rounded bg-white/[0.04] border border-white/[0.06]">↑↓</kbd> Navigate</span>
                        <span><kbd className="font-mono px-1 py-0.5 rounded bg-white/[0.04] border border-white/[0.06]">↵</kbd> Open</span>
                        <span><kbd className="font-mono px-1 py-0.5 rounded bg-white/[0.04] border border-white/[0.06]">ESC</kbd> Close</span>
                    </div>
                </div>
            </div>
        </>
    );
}
