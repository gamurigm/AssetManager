import React, { useEffect } from "react";
import { ISeriesApi, IChartApi } from "lightweight-charts";
import { calcVolumeProfile } from "./chartMath";

export function useVolumeProfile(
    showVP: boolean,
    rawData: any[],
    mainChartApi: React.MutableRefObject<IChartApi | null>,
    candleSeriesRef: React.MutableRefObject<ISeriesApi<"Candlestick"> | null>,
    vpCanvasRef: React.MutableRefObject<HTMLCanvasElement | null>,
    mainChartRef: React.MutableRefObject<HTMLDivElement | null>
) {
    useEffect(() => {
        const vpData = showVP && rawData.length > 20 ? (() => {
            const highs = rawData.map((d: any) => d.high);
            const lows = rawData.map((d: any) => d.low);
            const volumes = rawData.map((d: any) => d.volume ?? 0);
            return calcVolumeProfile(highs, lows, volumes);
        })() : null;

        if (!showVP || !vpData || !candleSeriesRef.current || !mainChartApi.current) {
            // Cleanup VP lines if any (poc, vah, val are usually created as price lines)
            // Note: LightWeight charts doesn't easily let us find all price lines to remove them unless we track them.
            // For now we assume they are recreated on redraw or ignored if showVP is false.
            return;
        }

        const candleSeries = candleSeriesRef.current;
        const chart = mainChartApi.current;

        // POC, VAH, VAL lines
        const pocLine = candleSeries.createPriceLine({ price: vpData.poc, color: '#FFD70090', lineWidth: 1, lineStyle: 2, axisLabelVisible: true, title: 'POC' });
        const vahLine = candleSeries.createPriceLine({ price: vpData.vah, color: '#FF6D0060', lineWidth: 1, lineStyle: 2, axisLabelVisible: true, title: 'VAH' });
        const valLine = candleSeries.createPriceLine({ price: vpData.val, color: '#FF6D0060', lineWidth: 1, lineStyle: 2, axisLabelVisible: true, title: 'VAL' });

        const drawVP = () => {
            const canvas = vpCanvasRef.current;
            if (!canvas || !mainChartRef.current || !vpData.bins || vpData.bins.length === 0) return;
            const container = mainChartRef.current;
            const dpr = window.devicePixelRatio || 1;
            canvas.width = container.clientWidth * dpr;
            canvas.height = container.clientHeight * dpr;
            canvas.style.width = container.clientWidth + 'px';
            canvas.style.height = container.clientHeight + 'px';

            const ctx = canvas.getContext('2d');
            if (!ctx) return;
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.scale(dpr, dpr);

            const maxBinVol = Math.max(...vpData.bins);
            if (maxBinVol === 0) return;

            const maxBarWidth = container.clientWidth * 0.22;
            const rightPadding = 55;

            for (let i = 0; i < vpData.bins.length; i++) {
                const vol = vpData.bins[i];
                if (vol <= 0) continue;

                const priceLo = vpData.minP + i * vpData.binSize;
                const priceHi = priceLo + vpData.binSize;
                const yLo = candleSeries.priceToCoordinate(priceHi);
                const yHi = candleSeries.priceToCoordinate(priceLo);
                if (yLo === null || yHi === null) continue;

                const y = Math.min(yLo, yHi);
                const h = Math.max(Math.abs(yHi - yLo) - 1, 1.5);
                const w = (vol / maxBinVol) * maxBarWidth;

                ctx.fillStyle = (priceLo >= vpData.poc) ? 'rgba(38, 166, 153, 0.25)' : 'rgba(239, 83, 80, 0.25)';
                if (priceLo >= vpData.val && priceHi <= vpData.vah) {
                    ctx.fillStyle = (priceLo >= vpData.poc) ? 'rgba(38, 166, 153, 0.45)' : 'rgba(239, 83, 80, 0.45)';
                }
                ctx.fillRect(container.clientWidth - rightPadding - w, y, w, h);
            }
        };

        drawVP();
        window.addEventListener('resize', drawVP);
        return () => {
            window.removeEventListener('resize', drawVP);
            try {
                if (mainChartApi.current && candleSeriesRef.current) {
                    candleSeriesRef.current.removePriceLine(pocLine);
                    candleSeriesRef.current.removePriceLine(vahLine);
                    candleSeriesRef.current.removePriceLine(valLine);
                }
            } catch (err) {
                // Ignore "Object is disposed" errors as they are expected when parent chart is destroyed
            }
        };
    }, [showVP, rawData, mainChartApi, candleSeriesRef, vpCanvasRef, mainChartRef]);
}
