"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";

import { useSocket } from "@/context/SocketContext";
import { cachedFetch } from "@/lib/cachedFetch";
import type {
    PolicyAllocation,
    PortfolioPolicyDeltaEvent,
    PortfolioPolicyHolding,
    PortfolioPolicyOptions,
    PortfolioPolicyResponse,
} from "@/types/portfolioPolicy";

const API_BASE = "http://127.0.0.1:8282";

const DEFAULT_OPTIONS: PortfolioPolicyOptions = {
    benchmark: "SPY",
    lookback_days: 252,
    risk_aversion: 0.35,
    turnover_penalty: 0.08,
    max_weight: 0.35,
    gross_limit: 1.0,
};

function normalizeHoldings(holdings: PortfolioPolicyHolding[]) {
    return holdings
        .filter((holding) => Math.abs(Number(holding.shares || 0)) > 0)
        .map((holding) => ({
            symbol: String(holding.symbol || "").toUpperCase(),
            name: holding.name,
            shares: Number(holding.shares || 0),
            price: Number(holding.price || holding.entryPrice || 0),
            entryPrice: Number(holding.entryPrice || holding.price || 0),
            factor: Number(holding.factor || 1),
            sector: holding.sector || "Unknown",
            type: holding.type || "asset",
            source: holding.source,
            change: holding.change,
            changePercent: holding.changePercent,
            purchaseDate: holding.purchaseDate,
        }))
        .filter((holding) => holding.symbol);
}

function buildHoldingsSignature(holdings: PortfolioPolicyHolding[]) {
    return holdings
        .map((holding) => `${holding.symbol}:${holding.shares}:${holding.factor}:${holding.price}`)
        .sort()
        .join("|");
}

function mergeAllocations(previous: PolicyAllocation[], incoming: PolicyAllocation[]) {
    const allocationMap = new Map(previous.map((allocation) => [allocation.symbol, allocation]));
    incoming.forEach((allocation) => {
        allocationMap.set(allocation.symbol, allocation);
    });
    return previous.map((allocation) => allocationMap.get(allocation.symbol) || allocation);
}

interface UsePortfolioPolicyArgs {
    holdings: PortfolioPolicyHolding[];
    portfolioId: string;
    enabled?: boolean;
    options?: Partial<PortfolioPolicyOptions>;
}

export function usePortfolioPolicy({
    holdings,
    portfolioId,
    enabled = true,
    options,
}: UsePortfolioPolicyArgs) {
    const { socket, connected } = useSocket();
    const [data, setData] = useState<PortfolioPolicyResponse | null>(null);
    const [loading, setLoading] = useState(enabled);
    const [refreshing, setRefreshing] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const mergedOptions = useMemo(() => ({ ...DEFAULT_OPTIONS, ...(options || {}) }), [options]);
    const normalizedHoldings = useMemo(() => normalizeHoldings(holdings), [holdings]);
    const holdingsSignature = useMemo(() => buildHoldingsSignature(normalizedHoldings), [normalizedHoldings]);
    const payload = useMemo(
        () => ({
            portfolio_id: portfolioId,
            holdings: normalizedHoldings,
            ...mergedOptions,
        }),
        [portfolioId, normalizedHoldings, mergedOptions],
    );
    const payloadRef = useRef(payload);

    useEffect(() => {
        payloadRef.current = payload;
    }, [payload]);

    const fetchFallback = useCallback(async (silent: boolean) => {
        if (!enabled) {
            return;
        }

        if (payloadRef.current.holdings.length === 0) {
            setData(null);
            setError(null);
            setLoading(false);
            setRefreshing(false);
            return;
        }

        if (silent) {
            setRefreshing(true);
        } else {
            setLoading(true);
        }

        try {
            const response = await fetch(`${API_BASE}/api/v1/portfolios/policy`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payloadRef.current),
            });
            const responseBody = await response.json().catch(() => ({}));
            if (!response.ok) {
                throw new Error(responseBody.detail || "Policy stream unavailable");
            }

            const snapshot = responseBody as PortfolioPolicyResponse;
            snapshot.stream = snapshot.stream || {
                reason: silent ? "http_refresh" : "http_fallback",
                changed_symbol: null,
                tracked_symbols: payloadRef.current.holdings.map((holding) => holding.symbol),
                transport: "http",
            };
            setData(snapshot);
            setError(null);
        } catch (requestError) {
            setError(requestError instanceof Error ? requestError.message : "Policy stream unavailable");
        } finally {
            setLoading(false);
            setRefreshing(false);
        }
    }, [enabled]);

    useEffect(() => {
        if (!enabled) {
            setData(null);
            setError(null);
            setLoading(false);
            setRefreshing(false);
            return;
        }

        if (normalizedHoldings.length === 0) {
            setData(null);
            setError(null);
            setLoading(false);
            setRefreshing(false);
            return;
        }

        if (!socket || !connected) {
            void fetchFallback(false);
            return;
        }

        const onUpdate = (snapshot: PortfolioPolicyResponse) => {
            setData(snapshot);
            setError(null);
            setLoading(false);
            setRefreshing(false);
        };

        const onDelta = (delta: PortfolioPolicyDeltaEvent) => {
            setData((previous) => {
                if (!previous) {
                    return previous;
                }
                return {
                    ...previous,
                    generated_at: delta.generated_at,
                    summary: delta.summary,
                    objective: delta.objective,
                    stream: delta.stream,
                    allocations: mergeAllocations(previous.allocations, delta.allocations),
                };
            });
            setError(null);
            setLoading(false);
            setRefreshing(false);
        };

        const onStreamError = (payloadError: { error?: string }) => {
            setError(payloadError?.error || "Policy stream unavailable");
            setLoading(false);
            setRefreshing(false);
        };

        socket.on("portfolio_policy_update", onUpdate);
        socket.on("portfolio_policy_delta", onDelta);
        socket.on("portfolio_policy_error", onStreamError);

        setRefreshing(Boolean(data));
        setLoading(!data);
        socket.emit("subscribe_portfolio_policy", payloadRef.current);

        return () => {
            socket.emit("unsubscribe_portfolio_policy");
            socket.off("portfolio_policy_update", onUpdate);
            socket.off("portfolio_policy_delta", onDelta);
            socket.off("portfolio_policy_error", onStreamError);
        };
    }, [socket, connected, enabled, portfolioId, holdingsSignature, fetchFallback]);

    return {
        data,
        loading,
        refreshing,
        error,
        connected,
        refresh: () => fetchFallback(Boolean(data)),
    };
}