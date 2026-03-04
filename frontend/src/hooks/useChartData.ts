"use client";

import { useState, useEffect } from "react";
import type { CandleData, QuoteData } from "@/types/dashboard";

const API_BASE = "http://127.0.0.1:8282";

/**
 * Hook: fetches historical candles + quote for a single symbol.
 * Encapsulates theme detection for chart rendering.
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
        const fetchData = async () => {
            try {
                const [histRes, quoteRes] = await Promise.all([
                    fetch(`${API_BASE}/api/v1/market/historical/${encodeURIComponent(symbol)}?limit=10000`),
                    fetch(`${API_BASE}/api/v1/market/quote/${encodeURIComponent(symbol)}`),
                ]);
                const histData = await histRes.json();
                if (histData.historical?.length > 0) {
                    setCandles(histData.historical.sort((a: any, b: any) => a.date.localeCompare(b.date)));
                } else {
                    setCandles([]);
                }
                const q = await quoteRes.json();
                if (q && !q.error) setQuote({ price: q.price, changePercentage: q.changePercentage });
            } catch (err) {
                console.error("Chart data fetch error:", err);
                setCandles([]);
            } finally {
                setLoading(false);
            }
        };
        setLoading(true);
        fetchData();
    }, [symbol]);

    return { candles, quote, loading, theme, isLight: theme === 'light' };
}
