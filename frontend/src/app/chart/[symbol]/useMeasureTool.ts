import { useEffect, useRef, useCallback } from "react";
import { IChartApi, ISeriesApi } from "lightweight-charts";

interface Pt { price: number; x: number; y: number }

/**
 * Measure tool – click two points on the chart to see % change.
 * Uses chart.subscribeClick so it never blocks pan / zoom / scroll.
 */
export function useMeasureTool(
    active: boolean,
    mainChartRef: React.MutableRefObject<HTMLDivElement | null>,
    mainChartApi: React.MutableRefObject<IChartApi | null>,
    candleSeriesRef: React.MutableRefObject<ISeriesApi<"Candlestick"> | null>,
    overlayRef: React.MutableRefObject<HTMLCanvasElement | null>,
) {
    const p1 = useRef<Pt | null>(null);
    const drawing = useRef(false);

    /* ── helpers ─────────────────────────────────────────── */

    const clear = useCallback(() => {
        const c = overlayRef.current;
        if (c) c.getContext("2d")?.clearRect(0, 0, c.width, c.height);
        p1.current = null;
        drawing.current = false;
    }, [overlayRef]);

    const paint = useCallback((a: Pt, b: Pt) => {
        const canvas = overlayRef.current;
        const box = mainChartRef.current;
        if (!canvas || !box) return;

        const dpr = devicePixelRatio || 1;
        canvas.width = box.clientWidth * dpr;
        canvas.height = box.clientHeight * dpr;
        canvas.style.width = box.clientWidth + "px";
        canvas.style.height = box.clientHeight + "px";

        const ctx = canvas.getContext("2d");
        if (!ctx) return;
        ctx.scale(dpr, dpr);

        const delta = b.price - a.price;
        const pct = a.price ? (delta / a.price) * 100 : 0;
        const up = delta >= 0;
        const col = up ? "rgba(34,197,94," : "rgba(239,68,68,";

        /* filled zone */
        ctx.fillStyle = col + "0.06)";
        ctx.fillRect(Math.min(a.x, b.x), Math.min(a.y, b.y),
            Math.abs(b.x - a.x) || 1, Math.abs(b.y - a.y) || 1);

        /* thin dashed border */
        ctx.strokeStyle = col + "0.35)";
        ctx.lineWidth = 0.75;
        ctx.setLineDash([3, 3]);
        ctx.strokeRect(Math.min(a.x, b.x), Math.min(a.y, b.y),
            Math.abs(b.x - a.x) || 1, Math.abs(b.y - a.y) || 1);
        ctx.setLineDash([]);

        /* diagonal */
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(b.x, b.y);
        ctx.strokeStyle = col + "0.6)";
        ctx.lineWidth = 1;
        ctx.stroke();

        /* dots */
        [a, b].forEach(p => {
            ctx.beginPath();
            ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
            ctx.fillStyle = col + "0.9)";
            ctx.fill();
        });

        /* label (small pill) */
        const sign = delta >= 0 ? "+" : "";
        const txt = `${sign}${pct.toFixed(2)}%  ${sign}${delta.toFixed(2)}`;
        ctx.font = "600 10px 'JetBrains Mono', monospace";
        const tw = ctx.measureText(txt).width;
        const pw = tw + 14;
        const ph = 20;
        const px = (a.x + b.x) / 2 - pw / 2;
        const py = Math.min(a.y, b.y) - ph - 6;

        ctx.fillStyle = "rgba(0,0,0,0.75)";
        ctx.beginPath();
        ctx.roundRect(px, py, pw, ph, 4);
        ctx.fill();

        ctx.strokeStyle = col + "0.4)";
        ctx.lineWidth = 0.5;
        ctx.beginPath();
        ctx.roundRect(px, py, pw, ph, 4);
        ctx.stroke();

        ctx.fillStyle = col + "1)";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(txt, px + pw / 2, py + ph / 2);
    }, [overlayRef, mainChartRef]);

    /* ── main effect ────────────────────────────────────── */

    useEffect(() => {
        if (!active) { clear(); return; }

        const chart = mainChartApi.current;
        const series = candleSeriesRef.current;
        if (!chart || !series) return;

        const resolve = (param: any): Pt | null => {
            if (!param.point || !param.seriesData) return null;
            const d = param.seriesData.get(series);
            if (!d) return null;
            const price = (d as any).close ?? (d as any).value ?? null;
            if (price === null) return null;
            return { price, x: param.point.x, y: param.point.y };
        };

        const onClick = (param: any) => {
            const pt = resolve(param);
            if (!pt) return;

            if (!drawing.current) {
                p1.current = pt;
                drawing.current = true;
            } else {
                paint(p1.current!, pt);
                drawing.current = false;
            }
        };

        const onMove = (param: any) => {
            if (!drawing.current || !p1.current) return;
            const pt = resolve(param);
            if (pt) paint(p1.current, pt);
        };

        const onKey = (e: KeyboardEvent) => {
            if (e.key === "Escape") clear();
        };

        chart.subscribeClick(onClick);
        chart.subscribeCrosshairMove(onMove);
        window.addEventListener("keydown", onKey);

        return () => {
            chart.unsubscribeClick(onClick);
            chart.unsubscribeCrosshairMove(onMove);
            window.removeEventListener("keydown", onKey);
        };
    }, [active, mainChartApi, candleSeriesRef, clear, paint]);

    return { clearMeasurement: clear };
}
