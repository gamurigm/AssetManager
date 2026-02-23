"use client"

import React, { createContext, useContext, useState, ReactNode } from "react";

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

    const updateHoldings = (newHoldings: Holding[]) => {
        const timestamp = new Date().toLocaleTimeString();
        console.log(`[${timestamp}] [PORTFOLIO] Updating holdings data | Assets: ${newHoldings.length}`);
        setHoldings(newHoldings);
    };

    const totalPnL = holdings.reduce((sum, h) => sum + h.change, 0);
    const totalValue = totalPnL;
    const pnlPercent = 0; // Relative P&L doesn't apply without a principle balance

    return (
        <PortfolioContext.Provider value={{ holdings, totalValue, totalPnL, pnlPercent, setHoldings: updateHoldings }}>
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
