// ─── Dashboard Domain Types ─────────────────────────────────────────

export interface DashboardHolding {
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
    purchaseDate?: string;
}

export type SidebarTab = 'watchlist' | 'indicators' | 'alerts' | 'history' | 'trading' | 'experts';

export type PanelId = 'equity-curve' | 'holdings' | 'sector' | 'treemap' | 'economics' | 'activity' | 'factor-analysis';

export interface TreemapItem {
    name: string;
    symbol: string;
    value: number;
    change: number;
    sector: string;
    baseColor: string;
}

export interface SectorItem {
    name: string;
    value: number;
    percent: number;
    color: string;
}

export interface QuoteData {
    price: number;
    changePercentage: number;
}

export interface CandleData {
    date: string;
    open: number;
    high: number;
    low: number;
    close: number;
    volume?: number;
}

export interface TransactionRecord {
    symbol: string;
    type: 'BUY' | 'SELL';
    shares: number;
    price: number;
    date: string;
    time: string;
}
