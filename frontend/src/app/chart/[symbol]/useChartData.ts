import { useState, useEffect, useCallback, useRef } from "react";
import { ColorType } from "lightweight-charts";

/* ─── Local persistence helpers ──────────────────────────────────────── */

const CACHE_PREFIX = "chartData_";

function cacheKey(symbol: string, tf: string) {
    return `${CACHE_PREFIX}${symbol}_${tf}`;
}

function readCache(symbol: string, tf: string): any[] | null {
    try {
        const raw = localStorage.getItem(cacheKey(symbol, tf));
        if (!raw) return null;
        const parsed = JSON.parse(raw);
        if (Array.isArray(parsed) && parsed.length > 0) return parsed;
    } catch { }
    return null;
}

function writeCache(symbol: string, tf: string, data: any[]) {
    try {
        if (data.length === 0) return; // NEVER persist empty
        localStorage.setItem(cacheKey(symbol, tf), JSON.stringify(data));
    } catch {
        // localStorage full — silently drop oldest caches
        try {
            const keys = Object.keys(localStorage).filter(k => k.startsWith(CACHE_PREFIX));
            if (keys.length > 20) {
                keys.slice(0, 5).forEach(k => localStorage.removeItem(k));
                localStorage.setItem(cacheKey(symbol, tf), JSON.stringify(data));
            }
        } catch { }
    }
}

/* ─── Hook ───────────────────────────────────────────────────────────── */

export function useChartData(symbol: string, timeframe: string, isLight: boolean) {
    const [loading, setLoading] = useState(true);
    const [quote, setQuote] = useState<{ price: number; changePercentage: number } | null>(null);
    const [rawData, setRawData] = useState<any[]>([]);
    const prevSymbolRef = useRef<string>("");

    const isIntradayTF = ["5m", "15m", "1h", "4h"].includes(timeframe);

    const normalizeTime = (dateStr: string) => {
        if (!dateStr) return 0;
        if (dateStr.includes(' ') || dateStr.includes('T')) {
            return Math.floor(new Date(dateStr).getTime() / 1000);
        }
        return dateStr;
    };

    const mapCandles = useCallback((historical: any[]) => {
        return historical
            .map((d: any) => {
                const dateStr = d.date || d.timestamp || d.time || d.ts || "";
                const timeVal = normalizeTime(dateStr);
                return {
                    ...d,
                    date: dateStr,
                    time: timeVal,
                    open: Number(d.open),
                    high: Number(d.high),
                    low: Number(d.low),
                    close: Number(d.close),
                    volume: Number(d.volume || d.unadjustedVolume || 0)
                };
            })
            .filter((d: any) => d.time !== 0 && !isNaN(d.close))
            .sort((a: any, b: any) => {
                const ta = typeof a.time === 'number' ? a.time : new Date(a.time).getTime();
                const tb = typeof b.time === 'number' ? b.time : new Date(b.time).getTime();
                return ta - tb;
            });
    }, []);

    const chartOpts = useCallback((height?: number) => ({
        layout: {
            background: { type: ColorType.Solid as const, color: 'transparent' },
            textColor: isLight ? '#3f3f46' : '#d1d5db',
            fontSize: 12,
            fontFamily: "'Inter', sans-serif",
        },
        grid: {
            vertLines: { visible: false },
            horzLines: { visible: false },
        },
        timeScale: { borderColor: isLight ? '#e4e4e7' : '#1f1f1f', timeVisible: isIntradayTF },
        rightPriceScale: { borderColor: isLight ? '#e4e4e7' : '#1f1f1f' },
        crosshair: {
            vertLine: { labelBackgroundColor: '#2962FF' },
            horzLine: { labelBackgroundColor: '#2962FF' },
        },
        ...(height ? { height } : {}),
    }), [isIntradayTF, isLight]);

    // ─── Main data fetch ────────────────────────────────────────────────
    useEffect(() => {
        if (!symbol) return;

        // 1. Immediately restore from localStorage if switching symbol
        if (prevSymbolRef.current !== symbol) {
            const cached = readCache(symbol, timeframe);
            if (cached && cached.length > 0) {
                setRawData(cached);
                setLoading(false); // show cached data instantly
            }
            prevSymbolRef.current = symbol;
        }

        const fetchData = async () => {
            try {
                const isIntraday = ["5m", "15m", "1h", "4h"].includes(timeframe);
                const periodMap: Record<string, string> = { "5m": "5d", "15m": "5d", "1h": "1mo", "4h": "3mo" };
                const dataUrl = isIntraday
                    ? `http://localhost:8282/api/v1/market/intraday/${encodeURIComponent(symbol)}?interval=${timeframe}&period=${periodMap[timeframe] || "1mo"}`
                    : `http://localhost:8282/api/v1/market/historical/${encodeURIComponent(symbol)}?limit=10000`;

                const [res, qRes] = await Promise.all([
                    fetch(dataUrl),
                    fetch(`http://localhost:8282/api/v1/market/quote/${encodeURIComponent(symbol)}`)
                ]);

                if (res.ok) {
                    const data = await res.json();
                    if (data.historical && Array.isArray(data.historical) && data.historical.length > 0) {
                        const mapped = mapCandles(data.historical);
                        if (mapped.length > 0) {
                            setRawData(mapped);
                            writeCache(symbol, timeframe, mapped);
                        }
                        // If API returned data but mapping produced 0, keep existing
                    }
                    // If API returned no historical array, keep existing data (DON'T wipe)
                }
                // If res not ok (404, 500) — keep existing data (DON'T wipe)

                if (qRes.ok) {
                    const q = await qRes.json();
                    if (q && !q.error && typeof q.price === 'number') {
                        setQuote({ price: q.price, changePercentage: q.changePercentage ?? 0 });
                    }
                }
            } catch (err) {
                console.warn("[ChartData] Network error, keeping cached data:", err);
                // *** NEVER setRawData([]) on error — keep whatever we have ***
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [symbol, timeframe, mapCandles]);

    // ─── Real-time quote polling ────────────────────────────────────────
    useEffect(() => {
        if (!symbol) return;
        const t = setInterval(async () => {
            try {
                const qRes = await fetch(`http://localhost:8282/api/v1/market/quote/${encodeURIComponent(symbol)}`);
                if (qRes.ok) {
                    const q = await qRes.json();
                    if (q && !q.error && typeof q.price === 'number') {
                        setQuote({ price: q.price, changePercentage: q.changePercentage ?? 0 });
                    }
                }
            } catch { }
        }, 3000);
        return () => clearInterval(t);
    }, [symbol]);

    return { loading, quote, rawData, chartOpts };
}
