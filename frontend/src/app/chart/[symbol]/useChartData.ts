import { useState, useEffect, useCallback, useRef } from "react";
import { ColorType } from "lightweight-charts";
import { useSocket } from "@/context/SocketContext";

/* ─── Local persistence helpers ──────────────────────────────────────── */

const CACHE_PREFIX = "chartData_v2_";

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

const INTRADAY_BUCKETS: Record<string, number> = {
    "1m": 60,
    "5m": 5 * 60,
    "15m": 15 * 60,
    "1h": 60 * 60,
    "4h": 4 * 60 * 60,
};

function toUtcEpochSeconds(value: unknown) {
    if (typeof value === "number") {
        if (!Number.isFinite(value) || value <= 0) return 0;
        return value > 1_000_000_000_000 ? Math.floor(value / 1000) : Math.floor(value);
    }

    const raw = String(value ?? "").trim();
    if (!raw) return 0;

    const dateOnly = /^\d{4}-\d{2}-\d{2}$/.test(raw);
    if (dateOnly) {
        const ms = Date.parse(`${raw}T00:00:00Z`);
        return Number.isFinite(ms) ? Math.floor(ms / 1000) : 0;
    }

    const normalized = raw.replace(" ", "T");
    const hasTimezone = /(?:Z|[+-]\d{2}:\d{2})$/.test(normalized);
    const ms = Date.parse(hasTimezone ? normalized : `${normalized}Z`);
    return Number.isFinite(ms) ? Math.floor(ms / 1000) : 0;
}

function shiftUtcToLocalChartSeconds(utcSeconds: number) {
    const offsetSeconds = new Date(utcSeconds * 1000).getTimezoneOffset() * 60;
    return utcSeconds - offsetSeconds;
}

function normalizeRealtimeTimestamp(timestamp?: number) {
    const utcSeconds = timestamp ? toUtcEpochSeconds(timestamp) : Math.floor(Date.now() / 1000);
    return shiftUtcToLocalChartSeconds(utcSeconds);
}

function getSortKey(time: string | number) {
    return typeof time === "number" ? time : time;
}

function sanitizeCandles(candles: any[], timeframe: string) {
    const isIntraday = timeframe in INTRADAY_BUCKETS;
    const bucketSize = INTRADAY_BUCKETS[timeframe];

    const normalized = candles
        .map((d: any) => {
            const hasChartReadyNumericTime = typeof d.time === "number" && Number.isFinite(d.time);
            const hasChartReadyDateTime = typeof d.time === "string" && /^\d{4}-\d{2}-\d{2}$/.test(d.time);
            const rawTime = d.timestamp || d.date || d.ts || d.time || "";
            const time = isIntraday
                ? (hasChartReadyNumericTime ? d.time : shiftUtcToLocalChartSeconds(toUtcEpochSeconds(rawTime)))
                : (hasChartReadyDateTime ? d.time : String(rawTime).slice(0, 10));

            const snappedTime = isIntraday && typeof time === "number"
                ? Math.floor(time / bucketSize) * bucketSize
                : time;

            return {
                ...d,
                date: d.date || rawTime,
                time: snappedTime,
                open: Number(d.open),
                high: Number(d.high),
                low: Number(d.low),
                close: Number(d.close),
                volume: Number(d.volume || d.unadjustedVolume || 0),
            };
        })
        .filter((d: any) => {
            if (typeof d.time === "number") return d.time > 0 && Number.isFinite(d.close);
            return !!d.time && Number.isFinite(d.close);
        })
        .sort((a: any, b: any) => {
            const ta = getSortKey(a.time);
            const tb = getSortKey(b.time);
            if (ta < tb) return -1;
            if (ta > tb) return 1;
            return 0;
        });

    const deduped: any[] = [];
    for (const candle of normalized) {
        const prev = deduped[deduped.length - 1];
        if (prev && prev.time === candle.time) {
            deduped[deduped.length - 1] = candle;
            continue;
        }
        deduped.push(candle);
    }

    return deduped;
}

function applyRealtimePrice(prevData: any[], price: number, timestamp: number, timeframe: string) {
    if (prevData.length === 0) return prevData;

    const last = prevData[prevData.length - 1];
    const anchor = Number(last.close || price);

    if (timeframe in INTRADAY_BUCKETS) {
        const bucketSize = INTRADAY_BUCKETS[timeframe];
        const bucketTime = Math.floor(timestamp / bucketSize) * bucketSize;
        if (typeof last.time === "number" && bucketTime < last.time) {
            return prevData;
        }

        if (typeof last.time === "number" && last.time === bucketTime) {
            return [
                ...prevData.slice(0, -1),
                {
                    ...last,
                    close: price,
                    high: Math.max(Number(last.high), price),
                    low: Math.min(Number(last.low), price),
                },
            ];
        }

        return [
            ...prevData,
            {
                ...last,
                date: new Date(bucketTime * 1000).toISOString(),
                time: bucketTime,
                open: anchor,
                high: Math.max(anchor, price),
                low: Math.min(anchor, price),
                close: price,
                volume: 0,
            },
        ];
    }

    const bucketDate = new Date(timestamp * 1000).toISOString().slice(0, 10);
    const lastDate = String(last.date || last.time || "").slice(0, 10);
    if (lastDate === bucketDate) {
        return [
            ...prevData.slice(0, -1),
            {
                ...last,
                close: price,
                high: Math.max(Number(last.high), price),
                low: Math.min(Number(last.low), price),
            },
        ];
    }

    return [
        ...prevData,
        {
            ...last,
            date: bucketDate,
            time: bucketDate,
            open: anchor,
            high: Math.max(anchor, price),
            low: Math.min(anchor, price),
            close: price,
            volume: 0,
        },
    ];
}

export function useChartData(symbol: string, timeframe: string, isLight: boolean) {
    const [loading, setLoading] = useState(true);
    const [quote, setQuote] = useState<{ price: number; changePercentage: number } | null>(null);
    const [rawData, setRawData] = useState<any[]>([]);
    const prevSymbolRef = useRef<string>("");
    const { socket, connected } = useSocket();

    const isIntradayTF = ["1m", "5m", "15m", "1h", "4h"].includes(timeframe);

    const mapCandles = useCallback((historical: any[]) => {
        return sanitizeCandles(historical, timeframe);
    }, [timeframe]);

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
        const cacheId = cacheKey(symbol, timeframe);

        // 1. Immediately restore from localStorage if switching symbol
        if (prevSymbolRef.current !== cacheId) {
            const cached = readCache(symbol, timeframe);
            if (cached && cached.length > 0) {
                const sanitizedCached = sanitizeCandles(cached, timeframe);
                if (sanitizedCached.length > 0) {
                    setRawData(sanitizedCached);
                }
                setLoading(false); // show cached data instantly
            }
            prevSymbolRef.current = cacheId;
        }

        const fetchData = async () => {
            try {
                const isIntraday = ["1m", "5m", "15m", "1h", "4h"].includes(timeframe);
                const periodMap: Record<string, string> = { "1m": "7d", "5m": "5d", "15m": "5d", "1h": "1mo", "4h": "3mo" };
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

    // ─── Real-time socket updates ───────────────────────────────────────
    useEffect(() => {
        if (!symbol || !socket || !connected) return;

        socket.emit("join_symbol", symbol);

        const onPriceUpdate = (data: any) => {
            if (String(data?.symbol || "").toUpperCase() !== symbol.toUpperCase()) return;
            if (typeof data?.price !== "number") return;

            setQuote({
                price: data.price,
                changePercentage: data.changePercent ?? 0,
            });

            const tickTimestamp = normalizeRealtimeTimestamp(data.timestamp);
            setRawData(prev => applyRealtimePrice(prev, data.price, tickTimestamp, timeframe));
        };

        socket.on("price_update", onPriceUpdate);

        return () => {
            socket.emit("leave_symbol", symbol);
            socket.off("price_update", onPriceUpdate);
        };
    }, [socket, connected, symbol, timeframe]);

    // ─── Polling fallback when socket is unavailable ────────────────────
    useEffect(() => {
        if (!symbol || (socket && connected)) return;

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
    }, [symbol, socket, connected]);

    return { loading, quote, rawData, chartOpts };
}
