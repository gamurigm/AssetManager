"use client";

import { useState, useEffect, useMemo } from "react";
import { usePortfolio } from "@/context/PortfolioContext";
import { logger } from "@/lib/logger";
import { SECTOR_COLORS } from "@/lib/colors";
import type { TransactionRecord, TreemapItem, SectorItem } from "@/types/dashboard";

const API_BASE = "http://127.0.0.1:8282";

/**
 * Hook: fetches and manages all dashboard-level data.
 * Encapsulates history polling, risk metrics, price sync, and derived data.
 */
export function useDashboardData() {
    const { holdings, setHoldings, totalValue, accountEquity, totalPnL, pnlPercent, closePosition, activePortfolio } = usePortfolio();

    const [loading, setLoading] = useState(true);
    const [transactions, setTransactions] = useState<TransactionRecord[]>([]);
    const [riskData, setRiskData] = useState<any>(null);

    // ─── Transaction History (polled) ────────────────────────────
    useEffect(() => {
        const fetchHistory = async () => {
            try {
                const res = await fetch(`${API_BASE}/api/v1/trading/history?portfolio_id=${activePortfolio}`);
                if (!res.ok) throw new Error(`HTTP ${res.status}`);
                const data = await res.json();
                setTransactions(data);
            } catch {
                console.warn("Retrying history fetch... (Backend may be initializing)");
            }
        };
        fetchHistory();
        const interval = setInterval(fetchHistory, 10000);
        return () => clearInterval(interval);
    }, [activePortfolio]);

    // ─── Risk Metrics (polled) ───────────────────────────────────
    useEffect(() => {
        const fetchRisk = async () => {
            try {
                const res = await fetch(`${API_BASE}/api/v1/portfolios/risk?portfolio_id=${activePortfolio}`);
                if (!res.ok) return;
                const data = await res.json();
                if (!data.error) setRiskData(data);
            } catch { /* backend may be offline */ }
        };
        fetchRisk();
        const interval = setInterval(fetchRisk, 120000);
        return () => clearInterval(interval);
    }, [activePortfolio]);

    // ─── Logger ──────────────────────────────────────────────────
    useEffect(() => {
        logger.info("Dashboard", "Terminal Main Dashboard initialized");
    }, []);

    // ─── Price Sync ──────────────────────────────────────────────
    useEffect(() => {
        const fetchPrices = async () => {
            if (holdings.length === 0) { setLoading(false); return; }
            let newHoldings = [...holdings];
            let changed = false;

            for (let i = 0; i < newHoldings.length; i++) {
                const h = newHoldings[i];
                try {
                    const res = await fetch(`${API_BASE}/api/v1/market/quote/${encodeURIComponent(h.symbol)}`);
                    if (!res.ok) continue;
                    const data = await res.json();
                    if (data && !data.error) {
                        const currentPrice = data.price;
                        const totalProfit = (currentPrice - (h as any).entryPrice) * h.shares * (h as any).factor;
                        const changePercent = (h as any).entryPrice !== 0
                            ? ((currentPrice - (h as any).entryPrice) / (h as any).entryPrice) * 100
                            : 0;
                        newHoldings[i] = { ...h, price: currentPrice, change: totalProfit, changePercent, source: data.source || "Unknown" };
                        changed = true;
                    }
                } catch {
                    console.warn(`Failed to sync ${h.symbol}`);
                }
            }
            if (changed) setHoldings([...newHoldings]);
            setLoading(false);
        };

        fetchPrices();
        const interval = setInterval(fetchPrices, 600000);
        return () => clearInterval(interval);
    }, [holdings.length]);

    // ─── Derived Data ────────────────────────────────────────────
    const activeHoldings = useMemo(() => holdings.filter(h => h.price > 0), [holdings]);

    const treemapData: TreemapItem[] = useMemo(() => {
        return activeHoldings
            .map(h => ({
                name: h.name,
                symbol: h.symbol,
                value: Math.abs(h.shares) * h.price * h.factor,
                change: h.changePercent,
                sector: (h as any).sector || "Other",
                baseColor: SECTOR_COLORS[(h as any).sector] || "#64748b",
            }))
            .sort((a, b) => b.value - a.value);
    }, [activeHoldings]);

    const sectorData: SectorItem[] = useMemo(() => {
        const sectors: Record<string, number> = {};
        activeHoldings.forEach(h => {
            const sector = (h as any).sector || "Other";
            const value = Math.abs(h.shares) * h.price * h.factor;
            sectors[sector] = (sectors[sector] || 0) + value;
        });
        const totalVal = Object.values(sectors).reduce((a, b) => a + b, 0);
        return Object.entries(sectors)
            .filter(([_, value]) => value > 0)
            .map(([name, value]) => ({
                name,
                value,
                percent: totalVal > 0 ? (value / totalVal) * 100 : 0,
                color: SECTOR_COLORS[name] || "#64748b",
            }));
    }, [activeHoldings]);

    return {
        holdings,
        setHoldings,
        activeHoldings,
        totalValue,
        accountEquity,
        totalPnL,
        pnlPercent,
        closePosition,
        loading,
        transactions,
        riskData,
        treemapData,
        sectorData,
    };
}
