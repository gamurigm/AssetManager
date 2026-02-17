"use client"

import React, { createContext, useContext, useState, ReactNode } from "react";

interface Holding {
    symbol: string;
    name: string;
    shares: number;
    price: number;
    change: number;
    changePercent: number;
    source: string;
    sector: string;
}

interface PortfolioContextType {
    holdings: Holding[];
    totalValue: number;
    totalPnL: number;
    pnlPercent: number;
    setHoldings: (holdings: Holding[]) => void;
}

const PortfolioContext = createContext<PortfolioContextType | undefined>(undefined);

export function PortfolioProvider({ children }: { children: ReactNode }) {
    const [holdings, setHoldings] = useState<Holding[]>([]);

    const totalValue = holdings.reduce((sum, h) => sum + h.shares * h.price, 0);
    const totalPnL = holdings.reduce((sum, h) => sum + h.shares * h.change, 0);
    const pnlPercent = totalValue > 0 ? (totalPnL / (totalValue - totalPnL)) * 100 : 0;

    return (
        <PortfolioContext.Provider value={{ holdings, totalValue, totalPnL, pnlPercent, setHoldings }}>
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
