"use client";

import { useState, useEffect } from "react";
import type { CandleData, QuoteData } from "@/types/dashboard";

const API_BASE = "http://127.0.0.1:8282";
const CACHE_PREFIX = "symbolChart_";

function readCache(symbol: string): CandleData[] | null {
    try {
        const raw = localStorage.getItem(`${CACHE_PREFIX}${symbol}`);
        if (!raw) return null;
        const parsed = JSON.parse(raw);
        if (Array.isArray(parsed) && parsed.length > 0) return parsed;
    } catch { }
    return null;
}

function writeCache(symbol: string, data: CandleData[]) {
    try {
        if (data.length === 0) return;
        localStorage.setItem(`${CACHE_PREFIX}${symbol}`, JSON.stringify(data));
    } catch {
        // localStorage full — evict oldest
        try {
            const keys = Object.keys(localStorage).filter(k => k.startsWith(CACHE_PREFIX));
            if (keys.length > 30) keys.slice(0, 10).forEach(k => localStorage.removeItem(k));
            localStorage.setItem(`${CACHE_PREFIX}${symbol}`, JSON.stringify(data));
        } catch { }
    }
}

/**
 * Hook: fetches historical candles + quote for a single symbol.
 * Persistent: never wipes existing data on API error.
 */
export function useChartData(symbol: string) {
    const [candles, setCandles] = useState<CandleData[]>([]);
    const [quote, setQuote] = useState<QuoteData | null>(null);
    const [loading, setLoading] = useState(true);
    const [theme, setTheme] = useState<'light' | 'dark'>('dark');

    // Theme observer
    useEffect(() => {
        const checkTheme = () =>
            setTheme(document.documentElement.classList.contains('light') ? 'light' : 'dark');
        checkTheme();
        const observer = new MutationObserver(checkTheme);
        observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
        return () => observer.disconnect();
    }, []);

    // Fetch historical + quote in parallel
    useEffect(() => {
        // Instantly hydrate from localStorage
        const cached = readCache(symbol);
        if (cached && cached.length > 0) {
            setCandles(cached);
            setLoading(false);
        }

        const fetchData = async () => {
            try {
                const [histRes, quoteRes] = await Promise.all([
                    fetch(`${API_BASE}/api/v1/market/historical/${encodeURIComponent(symbol)}?limit=10000`),
                    fetch(`${API_BASE}/api/v1/market/quote/${encodeURIComponent(symbol)}`),
                ]);

                if (histRes.ok) {
                    const histData = await histRes.json();
                    if (histData.historical?.length > 0) {
                        const sorted = histData.historical.sort((a: any, b: any) => a.date.localeCompare(b.date));
                        setCandles(sorted);
                        writeCache(symbol, sorted);
                    }
                    // If API returned empty historical, keep existing (DON'T wipe)
                }
                // If HTTP error — keep existing data

                if (quoteRes.ok) {
                    const q = await quoteRes.json();
                    if (q && !q.error) setQuote({ price: q.price, changePercentage: q.changePercentage });
                }
            } catch (err) {
                console.warn("[SymbolChart] Network error, keeping cached data:", err);
                // *** NEVER setCandles([]) — keep whatever we have ***
            } finally {
                setLoading(false);
            }
        };
        setLoading(true);
        fetchData();
    }, [symbol]);

    return { candles, quote, loading, theme, isLight: theme === 'light' };
}
