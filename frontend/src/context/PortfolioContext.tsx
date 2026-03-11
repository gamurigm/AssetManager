"use client"

import React, { createContext, useContext, useState, ReactNode, useCallback } from "react";
import { useSocket } from "@/context/SocketContext";
import { cachedFetch } from "@/lib/cachedFetch";

interface Holding {
    symbol: string;
    name: string;
    shares: number;
    price: number;
    entryPrice: number;
    factor: number;
    change: number;
    changePercent: number;
    source: string;
    sector: string;
    type: string;
    purchaseDate: string;
    sl?: number;
    tp?: number;
}

interface PortfolioContextType {
    holdings: Holding[];
    totalValue: number;      // Current Market Value of Assets (Sum shares * price * factor)
    accountEquity: number;   // Total AUM (50000 + Realized + Unrealized)
    totalPnL: number;
    pnlPercent: number;
    realizedPnL: number;
    unrealizedPnL: number;
    setHoldings: (holdings: Holding[]) => void;
    closePosition: (symbol: string) => void;
    openTrade: (symbol: string, name: string, shares: number, price: number, factor: number, sector: string, type: string, sl?: number, tp?: number) => Promise<void>;
    updatePositionLevels: (symbol: string, sl?: number, tp?: number) => void;
    refreshPortfolio: () => Promise<void>;
    activePortfolio: string;
    setActivePortfolio: (portfolio: string) => void;
}

const PortfolioContext = createContext<PortfolioContextType | undefined>(undefined);

export function PortfolioProvider({ children }: { children: ReactNode }) {
    const { socket, connected } = useSocket();
    const [activePortfolio, setActivePortfolio] = useState<string>("main");
    const [holdings, setHoldings] = useState<Holding[]>([]);
    const [isInitialized, setIsInitialized] = useState(false);
    const [realizedPnL, setRealizedPnL] = useState(0);

    // Load from Backend
    const refreshPortfolio = useCallback(async () => {
        try {
            const [hRes, pnlRes] = await Promise.all([
                cachedFetch(`http://127.0.0.1:8282/api/v1/portfolios/?portfolio_id=${activePortfolio}`),
                cachedFetch(`http://127.0.0.1:8282/api/v1/trading/history?portfolio_id=${activePortfolio}`)
            ]);

            const hData = await hRes.json();
            if (Array.isArray(hData)) {
                const sanitized = hData.map(h => {
                    const price = h.price || h.entryPrice || 0;
                    const factor = h.factor || 1;
                    const change = h.change !== undefined ? h.change : (price - h.entryPrice) * h.shares * factor;
                    const changePercent = h.changePercent !== undefined ? h.changePercent :
                        (h.entryPrice !== 0 ? ((price - h.entryPrice) / h.entryPrice) * 100 : 0);
                    return {
                        ...h,
                        price,
                        factor,
                        change,
                        changePercent,
                        purchaseDate: h.purchaseDate || new Date().toISOString().split("T")[0]
                    };
                });
                setHoldings(sanitized);
            }

            const tData = await pnlRes.json();
            if (Array.isArray(tData)) {
                const totalR = tData.reduce((sum: number, t: any) => sum + (t.realized_pnl || 0), 0);
                setRealizedPnL(totalR);
            }
        } catch (err) {
            console.error("Failed to load initial data:", err);
        } finally {
            setIsInitialized(true);
        }
    }, [activePortfolio]);

    // Initial Load
    React.useEffect(() => {
        refreshPortfolio();
    }, [refreshPortfolio]);

    const subscribedSymbolsKey = React.useMemo(
        () => Array.from(new Set(holdings.map(h => h.symbol).filter(Boolean))).sort().join(","),
        [holdings]
    );

    React.useEffect(() => {
        if (!socket || !connected || !subscribedSymbolsKey) return;

        const symbols = subscribedSymbolsKey.split(",").filter(Boolean);
        symbols.forEach(symbol => socket.emit("join_symbol", symbol));

        const onPriceUpdate = (data: any) => {
            if (!data || typeof data.price !== "number") return;
            const incomingSymbol = String(data.symbol || "").toUpperCase();
            if (!incomingSymbol) return;

            setHoldings(prev => {
                let changed = false;
                const next = prev.map(holding => {
                    if (holding.symbol.toUpperCase() !== incomingSymbol) {
                        return holding;
                    }

                    const currentPrice = Number(data.price);
                    const totalProfit = (currentPrice - holding.entryPrice) * holding.shares * holding.factor;
                    const changePercent = holding.entryPrice !== 0
                        ? ((currentPrice - holding.entryPrice) / holding.entryPrice) * 100
                        : 0;

                    if (
                        holding.price === currentPrice &&
                        holding.change === totalProfit &&
                        holding.changePercent === changePercent &&
                        holding.source === (data.source || holding.source)
                    ) {
                        return holding;
                    }

                    changed = true;
                    return {
                        ...holding,
                        price: currentPrice,
                        change: totalProfit,
                        changePercent,
                        source: data.source || holding.source,
                    };
                });

                return changed ? next : prev;
            });
        };

        socket.on("price_update", onPriceUpdate);

        return () => {
            symbols.forEach(symbol => socket.emit("leave_symbol", symbol));
            socket.off("price_update", onPriceUpdate);
        };
    }, [socket, connected, subscribedSymbolsKey]);

    // Persist to Backend on Changes
    React.useEffect(() => {
        if (!isInitialized) return;
        const syncTimeout = setTimeout(async () => {
            try {
                await fetch(`http://127.0.0.1:8282/api/v1/portfolios/save?portfolio_id=${activePortfolio}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(holdings)
                });
            } catch (err) {
                console.error("Failed to sync holdings:", err);
            }
        }, 1000);
        return () => clearTimeout(syncTimeout);
    }, [holdings, isInitialized, activePortfolio]);

    const totalUnrealizedPnL = holdings.reduce((sum: number, h: Holding) => sum + h.change, 0);
    const totalPnL = realizedPnL + totalUnrealizedPnL;
    const totalValue = holdings.reduce((sum: number, h: Holding) => sum + (Math.abs(h.shares) * h.price * h.factor), 0);
    const accountEquity = 50000 + totalPnL;
    const pnlPercent = (totalPnL / 50000) * 100;

    const accountEquityRef = React.useRef(accountEquity);
    accountEquityRef.current = accountEquity;

    React.useEffect(() => {
        if (!isInitialized) return;
        const recordSnapshot = async () => {
            const equity = accountEquityRef.current;
            if (!equity || equity <= 0) return;
            try {
                await fetch(`http://127.0.0.1:8282/api/v1/portfolios/snapshot-equity?portfolio_id=${activePortfolio}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ total_value: equity }),
                    signal: AbortSignal.timeout(5000),
                });
            } catch { }
        };
        const initial = setTimeout(recordSnapshot, 10000);
        const interval = setInterval(recordSnapshot, 60000);
        return () => { clearTimeout(initial); clearInterval(interval); };
    }, [isInitialized, activePortfolio]);

    const updateHoldings = useCallback((newHoldings: Holding[]) => {
        setHoldings(newHoldings);
    }, []);

    const updatePositionLevels = useCallback((symbol: string, sl?: number, tp?: number) => {
        setHoldings(prev => prev.map(h => h.symbol === symbol ? { ...h, sl, tp } : h));
    }, []);

    const openTrade = async (symbol: string, name: string, shares: number, price: number, factor: number, sector: string, type: string, sl?: number, tp?: number) => {
        const today = new Date().toISOString().split("T")[0];
        const newHolding: Holding = {
            symbol,
            name,
            shares,
            entryPrice: price,
            price: price,
            factor,
            change: 0,
            changePercent: 0,
            source: "Terminal",
            sector,
            type,
            purchaseDate: today,
            sl,
            tp
        };

        try {
            await fetch('http://127.0.0.1:8282/api/v1/trading/record', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    type_str: 'BUY',
                    symbol: symbol,
                    shares: shares,
                    price: price,
                    realized_pnl: 0,
                    date: today,
                    portfolio_id: activePortfolio
                })
            });
            setHoldings(prev => [...prev, newHolding]);
        } catch (err) {
            console.error("Failed to record trade:", err);
        }
    };

    const closePosition = async (symbol: string) => {
        const holdingToClose = holdings.find(h => h.symbol === symbol);
        if (holdingToClose) {
            const realized = holdingToClose.change;
            try {
                await fetch('http://127.0.0.1:8282/api/v1/trading/record', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        type_str: 'SELL',
                        symbol: symbol,
                        shares: holdingToClose.shares,
                        price: holdingToClose.price,
                        realized_pnl: realized,
                        date: new Date().toISOString().split("T")[0],
                        portfolio_id: activePortfolio
                    })
                });
                setRealizedPnL(prev => prev + realized);
            } catch (err) {
                console.error("Failed to record transaction:", err);
            }
        }
        setHoldings(prev => prev.filter(h => h.symbol !== symbol));
    };

    return (
        <PortfolioContext.Provider value={{
            holdings,
            totalValue,
            accountEquity,
            totalPnL,
            pnlPercent,
            realizedPnL,
            unrealizedPnL: totalUnrealizedPnL,
            setHoldings: updateHoldings,
            closePosition,
            openTrade,
            updatePositionLevels,
            refreshPortfolio,
            activePortfolio,
            setActivePortfolio
        }}>
            {children}
        </PortfolioContext.Provider>
    );
}

export function usePortfolio() {
    const context = useContext(PortfolioContext);
    if (context === undefined) {
        throw new Error("usePortfolio must be used within a PortfolioProvider");
    }
    return context;
}
