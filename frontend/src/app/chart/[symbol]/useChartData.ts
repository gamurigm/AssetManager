import { useState, useEffect, useCallback } from "react";
import { ColorType } from "lightweight-charts";

export function useChartData(symbol: string, timeframe: string, isLight: boolean) {
    const [loading, setLoading] = useState(true);
    const [quote, setQuote] = useState<{ price: number; changePercentage: number } | null>(null);
    const [rawData, setRawData] = useState<any[]>([]);

    const isIntradayTF = ["5m", "15m", "1h", "4h"].includes(timeframe);

    const normalizeTime = (dateStr: string) => {
        if (!dateStr) return 0;
        if (dateStr.includes(' ') || dateStr.includes('T')) {
            return Math.floor(new Date(dateStr).getTime() / 1000);
        }
        return dateStr;
    };

    const chartOpts = useCallback((height?: number) => ({
        layout: {
            background: { type: ColorType.Solid as const, color: 'transparent' },
            textColor: isLight ? '#3f3f46' : '#d1d5db',
            fontSize: 12,
            fontFamily: "'Inter', sans-serif",
        },
        grid: {
            vertLines: { color: isLight ? '#f4f4f5' : '#141414' },
            horzLines: { color: isLight ? '#f4f4f5' : '#141414' },
        },
        timeScale: { borderColor: isLight ? '#e4e4e7' : '#1f1f1f', timeVisible: isIntradayTF },
        rightPriceScale: { borderColor: isLight ? '#e4e4e7' : '#1f1f1f' },
        crosshair: {
            vertLine: { labelBackgroundColor: '#2962FF' },
            horzLine: { labelBackgroundColor: '#2962FF' },
        },
        ...(height ? { height } : {}),
    }), [isIntradayTF, isLight]);

    useEffect(() => {
        if (!symbol) return;
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
                const data = await res.json();
                if (data.historical && Array.isArray(data.historical)) {
                    const mapped = data.historical
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
                    setRawData(mapped);
                } else {
                    setRawData([]);
                }
                const q = await qRes.json();
                if (q && !q.error && typeof q.price === 'number') {
                    setQuote({ price: q.price, changePercentage: q.changePercentage ?? 0 });
                }
            } catch (err) {
                console.error("Fetch error:", err);
                setRawData([]);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [symbol, timeframe]);

    useEffect(() => {
        if (!symbol) return;
        const t = setInterval(async () => {
            try {
                const qRes = await fetch(`http://localhost:8282/api/v1/market/quote/${encodeURIComponent(symbol)}`);
                const q = await qRes.json();
                if (q && !q.error && typeof q.price === 'number') {
                    setQuote({ price: q.price, changePercentage: q.changePercentage ?? 0 });
                }
            } catch (err) { }
        }, 3000);
        return () => clearInterval(t);
    }, [symbol]);

    return { loading, quote, rawData, chartOpts };
}
