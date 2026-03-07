export interface PortfolioPolicyHolding {
    symbol: string;
    name: string;
    shares: number;
    price: number;
    entryPrice: number;
    factor: number;
    sector: string;
    type: string;
    source?: string;
    change?: number;
    changePercent?: number;
    purchaseDate?: string;
}

export interface PolicyAllocation {
    symbol: string;
    name: string;
    sector: string;
    type?: string;
    action: string;
    rationale: string;
    shares?: number;
    price?: number;
    factor?: number;
    current_weight_pct: number;
    target_weight_pct: number;
    weight_delta_pct: number;
    target_notional?: number;
    expected_return_pct: number;
    expected_value_pct: number;
    volatility_pct: number;
    momentum_pct: number;
    confidence: number;
    delta_notional: number;
    delta_shares: number;
    has_data: boolean;
}

export interface PortfolioPolicyStreamMeta {
    reason: string;
    changed_symbol?: string | null;
    changed_symbols?: string[];
    tracked_symbols: string[];
    transport: string;
}

export interface PortfolioPolicyDeltaEvent {
    portfolio_id: string;
    generated_at: string;
    summary: PortfolioPolicyResponse["summary"];
    objective: PortfolioPolicyResponse["objective"];
    allocations: PolicyAllocation[];
    stream?: PortfolioPolicyStreamMeta;
}

export interface PortfolioPolicyResponse {
    portfolio_id: string;
    generated_at: string;
    summary: {
        rebalance_required: boolean;
        confidence_pct: number;
        coverage_percent: number;
        high_conviction_symbols: string[];
        target_cash_buffer_pct: number;
    };
    objective: {
        current_expected_return_pct: number;
        target_expected_return_pct: number;
        ev_delta_pct: number;
        current_risk_pct: number;
        target_risk_pct: number;
        risk_delta_pct: number;
        realized_trade_ev: number;
    };
    allocations: PolicyAllocation[];
    stream?: PortfolioPolicyStreamMeta;
}

export interface PortfolioPolicyOptions {
    benchmark: string;
    lookback_days: number;
    risk_aversion: number;
    turnover_penalty: number;
    max_weight: number;
    gross_limit: number;
}