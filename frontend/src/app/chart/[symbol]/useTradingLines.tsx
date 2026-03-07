import React, { useEffect, useRef } from "react";
import { ISeriesApi, IChartApi } from "lightweight-charts";
import { formatAssetPriceFixed } from "@/lib/marketFormatting";

export function useTradingLines(
    symbol: string,
    holdings: any[],
    quote: { price: number } | null,
    slPrice: string,
    setSlPrice: (v: string) => void,
    tpPrice: string,
    setTpPrice: (v: string) => void,
    mainChartApi: React.MutableRefObject<IChartApi | null>,
    mainChartRef: React.MutableRefObject<HTMLDivElement | null>,
    candleSeriesRef: React.MutableRefObject<ISeriesApi<"Candlestick"> | null>,
    updatePositionLevels: (symbol: string, sl?: number, tp?: number) => void,
    closePosition: (symbol: string) => void
) {
    const posLineRef = useRef<any>(null);
    const slLineRef = useRef<any>(null);
    const tpLineRef = useRef<any>(null);

    // Use refs for current SL/TP to use inside event listeners without re-binding
    const currentSlRef = useRef(slPrice);
    const currentTpRef = useRef(tpPrice);
    useEffect(() => { currentSlRef.current = slPrice; }, [slPrice]);
    useEffect(() => { currentTpRef.current = tpPrice; }, [tpPrice]);

    // Dragging logic
    useEffect(() => {
        if (!mainChartApi.current || !mainChartRef.current || !candleSeriesRef.current || !holdings.find(h => h.symbol === symbol)) return;

        const container = mainChartRef.current;
        const series = candleSeriesRef.current;
        let dragging: 'SL' | 'TP' | null = null;

        const handleMouseDown = (e: MouseEvent) => {
            if (e.button !== 0) return;
            const sl = parseFloat(currentSlRef.current);
            const tp = parseFloat(currentTpRef.current);

            const rect = container.getBoundingClientRect();
            const y = e.clientY - rect.top;

            const slY = !isNaN(sl) ? series.priceToCoordinate(sl) : null;
            const tpY = !isNaN(tp) ? series.priceToCoordinate(tp) : null;

            if (slY !== null && Math.abs(y - slY) < 15) {
                dragging = 'SL';
                e.preventDefault();
                e.stopPropagation();
            } else if (tpY !== null && Math.abs(y - tpY) < 15) {
                dragging = 'TP';
                e.preventDefault();
                e.stopPropagation();
            }
        };

        const handleMouseMove = (e: MouseEvent) => {
            if (!dragging) return;
            const rect = container.getBoundingClientRect();
            let y = e.clientY - rect.top;
            y = Math.max(0, Math.min(y, rect.height));

            const price = series.coordinateToPrice(y as any);
            if (price !== null) {
                if (dragging === 'SL') setSlPrice(formatAssetPriceFixed(price, { symbol }));
                if (dragging === 'TP') setTpPrice(formatAssetPriceFixed(price, { symbol }));
            }
        };

        const handleMouseUp = () => {
            if (dragging) {
                const sl = parseFloat(currentSlRef.current);
                const tp = parseFloat(currentTpRef.current);
                updatePositionLevels(symbol, isNaN(sl) ? undefined : sl, isNaN(tp) ? undefined : tp);
            }
            dragging = null;
        };

        container.addEventListener('mousedown', handleMouseDown, true);
        window.addEventListener('mousemove', handleMouseMove, true);
        window.addEventListener('mouseup', handleMouseUp, true);
        return () => {
            container.removeEventListener('mousedown', handleMouseDown, true);
            window.removeEventListener('mousemove', handleMouseMove, true);
            window.removeEventListener('mouseup', handleMouseUp, true);
        };
    }, [symbol, holdings, mainChartApi, mainChartRef, candleSeriesRef, updatePositionLevels, setSlPrice, setTpPrice]);

    // Position & SL/TP Lines drawing
    useEffect(() => {
        const holding = holdings.find(h => h.symbol === symbol);
        const candleSeries = candleSeriesRef.current;
        if (!candleSeries || !quote) return;

        const safeRemove = (line: any) => {
            try {
                if (line && candleSeriesRef.current && mainChartApi.current) {
                    candleSeriesRef.current.removePriceLine(line);
                }
            } catch (err) { }
        };

        if (!holding) {
            if (posLineRef.current) { safeRemove(posLineRef.current); posLineRef.current = null; }
            if (slLineRef.current) { safeRemove(slLineRef.current); slLineRef.current = null; }
            if (tpLineRef.current) { safeRemove(tpLineRef.current); tpLineRef.current = null; }
            return;
        }

        const ep = holding.entryPrice;
        const isLong = holding.shares > 0;
        const unrealized = (quote.price - ep) * holding.shares;
        const pnlStr = `${unrealized >= 0 ? '+' : ''}${unrealized.toFixed(2)}`;
        const formattedEntry = formatAssetPriceFixed(ep, { symbol });

        if (!posLineRef.current) {
            posLineRef.current = candleSeries.createPriceLine({
                price: ep, color: '#3b82f6', lineWidth: 2, lineStyle: 0,
                axisLabelVisible: true, title: `POSITION: AVG ${formattedEntry} (${pnlStr} USD)`
            });
        } else {
            posLineRef.current.applyOptions({ title: `POSITION: AVG ${formattedEntry} (${pnlStr} USD)`, price: ep });
        }

        const slVal = parseFloat(slPrice);
        if (!isNaN(slVal) && slVal > 0) {
            const slPnl = (slVal - ep) * holding.shares;
            const slPnlStr = `${slPnl >= 0 ? '+' : ''}${slPnl.toFixed(2)}`;
            const formattedSl = formatAssetPriceFixed(slVal, { symbol });
            if (!slLineRef.current) {
                slLineRef.current = candleSeries.createPriceLine({
                    price: slVal, color: '#ff1744', lineWidth: 2, lineStyle: 2,
                    axisLabelVisible: true, title: `STOP LOSS: ${formattedSl} (${slPnlStr} USD)`
                });
            } else {
                slLineRef.current.applyOptions({ title: `STOP LOSS: ${formattedSl} (${slPnlStr} USD)`, price: slVal });
            }

            if ((isLong && quote.price <= slVal) || (!isLong && quote.price >= slVal)) {
                closePosition(symbol);
                setSlPrice('');
                alert(`Stop Loss Hit! Closed ${symbol} at ${quote.price}`);
            }
        } else if (slLineRef.current) {
            safeRemove(slLineRef.current); slLineRef.current = null;
        }

        const tpVal = parseFloat(tpPrice);
        if (!isNaN(tpVal) && tpVal > 0) {
            const tpPnl = (tpVal - ep) * holding.shares;
            const tpPnlStr = `${tpPnl >= 0 ? '+' : ''}${tpPnl.toFixed(2)}`;
            const formattedTp = formatAssetPriceFixed(tpVal, { symbol });
            if (!tpLineRef.current) {
                tpLineRef.current = candleSeries.createPriceLine({
                    price: tpVal, color: '#00e676', lineWidth: 2, lineStyle: 2,
                    axisLabelVisible: true, title: `TAKE PROFIT: ${formattedTp} (${tpPnlStr} USD)`
                });
            } else {
                tpLineRef.current.applyOptions({ title: `TAKE PROFIT: ${formattedTp} (${tpPnlStr} USD)`, price: tpVal });
            }

            if ((isLong && quote.price >= tpVal) || (!isLong && quote.price <= tpVal)) {
                closePosition(symbol);
                setTpPrice('');
                alert(`Take Profit Hit! Closed ${symbol} at ${quote.price}`);
            }
        } else if (tpLineRef.current) {
            safeRemove(tpLineRef.current); tpLineRef.current = null;
        }

        return () => {
            // Usually we'd cleanup here, but standard LW Charts practice with React 
            // often prefers allowing the parent to clear all series at once or checking validity.
        };
    }, [holdings, symbol, quote, slPrice, tpPrice, closePosition, candleSeriesRef]);
}
