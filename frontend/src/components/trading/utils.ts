import { LiveTrade, EquityPoint, KpiSnapshot } from "./types";

export function formatCurrency(value: number) {
    return value.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

export function formatRatio(value: number) {
    if (!Number.isFinite(value)) return "Inf";
    return value.toFixed(2);
}

export function formatFractionPercent(value: number) {
    return `${(value * 100).toFixed(2)}%`;
}

export function formatTimestampLabel(value?: string, index?: number) {
    if (!value) return index === 0 ? "Start" : `Trade ${index}`;
    return value.replace("T", " ").slice(5, 16);
}

export function buildEquityCurve(trades: LiveTrade[], initialEquity: number): EquityPoint[] {
    const points: EquityPoint[] = [{ label: "Start", equity: initialEquity }];
    let runningEquity = initialEquity;

    trades.forEach((trade, index) => {
        runningEquity += Number(trade.pnl_usd || 0);
        points.push({
            label: formatTimestampLabel(trade.exit_timestamp || trade.timestamp, index + 1),
            equity: Number(runningEquity.toFixed(2)),
        });
    });

    return points;
}

export function deriveLiveKpis(trades: LiveTrade[], initialEquity: number): KpiSnapshot {
    if (trades.length === 0) {
        return {
            total_trades: 0,
            wins: 0,
            losses: 0,
            win_rate: 0,
            expectancy_r: 0,
            profit_factor: 0,
            max_drawdown_pct: 0,
            sharpe_ratio: 0,
            avg_rr_realized: 0,
            total_r: 0,
            final_equity: initialEquity,
            cagr: 0,
        };
    }

    const wins = trades.filter((trade) => trade.pnl_usd > 0);
    const losses = trades.filter((trade) => trade.pnl_usd < 0);
    const totalTrades = trades.length;
    const winRate = wins.length / totalTrades;
    const avgWinR = wins.length ? wins.reduce((sum, trade) => sum + trade.pnl_r, 0) / wins.length : 0;
    const avgLossR = losses.length ? losses.reduce((sum, trade) => sum + Math.abs(trade.pnl_r), 0) / losses.length : 0;
    const expectancy = (winRate * avgWinR) - ((1 - winRate) * avgLossR);
    const grossProfit = wins.reduce((sum, trade) => sum + trade.pnl_usd, 0);
    const grossLoss = losses.reduce((sum, trade) => sum + Math.abs(trade.pnl_usd), 0);
    const profitFactor = grossLoss > 0 ? grossProfit / grossLoss : (grossProfit > 0 ? Number.POSITIVE_INFINITY : 0);

    let equity = initialEquity;
    let peak = initialEquity;
    let maxDrawdown = 0;
    const returns: number[] = [];

    trades.forEach((trade) => {
        const previousEquity = equity;
        equity += trade.pnl_usd;
        returns.push(previousEquity > 0 ? (equity - previousEquity) / previousEquity : 0);
        if (equity > peak) peak = equity;
        const drawdown = peak > 0 ? (peak - equity) / peak : 0;
        if (drawdown > maxDrawdown) maxDrawdown = drawdown;
    });

    let sharpe = 0;
    if (returns.length > 1) {
        const avg = returns.reduce((sum, value) => sum + value, 0) / returns.length;
        const variance = returns.reduce((sum, value) => sum + ((value - avg) ** 2), 0) / (returns.length - 1);
        const std = Math.sqrt(variance);
        sharpe = std > 0 ? (avg / std) * Math.sqrt(252) : 0;
    }

    const totalR = trades.reduce((sum, trade) => sum + trade.pnl_r, 0);
    const avgRR = wins.length ? wins.reduce((sum, trade) => sum + Math.abs(trade.pnl_r), 0) / wins.length : 0;

    return {
        total_trades: totalTrades,
        wins: wins.length,
        losses: losses.length,
        win_rate: Number(winRate.toFixed(4)),
        expectancy_r: Number(expectancy.toFixed(4)),
        profit_factor: Number.isFinite(profitFactor) ? Number(profitFactor.toFixed(4)) : Number.POSITIVE_INFINITY,
        max_drawdown_pct: Number(maxDrawdown.toFixed(4)),
        sharpe_ratio: Number(sharpe.toFixed(4)),
        avg_rr_realized: Number(avgRR.toFixed(4)),
        total_r: Number(totalR.toFixed(4)),
        final_equity: Number(equity.toFixed(2)),
        cagr: 0,
    };
}

export function buildHistogramData(samples: number[], bins = 18) {
    if (samples.length === 0) return [];

    const min = Math.min(...samples);
    const max = Math.max(...samples);
    if (min === max) {
        return [{ label: min.toFixed(0), count: samples.length, color: min >= 0 ? "#22c55e" : "#ef4444" }];
    }

    const width = (max - min) / bins;
    const histogram = Array.from({ length: bins }, (_, index) => ({
        from: min + index * width,
        to: min + (index + 1) * width,
        count: 0,
    }));

    samples.forEach((sample) => {
        const bucket = Math.min(bins - 1, Math.floor((sample - min) / width));
        histogram[bucket].count += 1;
    });

    return histogram.map((bucket) => ({
        label: bucket.from.toFixed(0),
        count: bucket.count,
        color: (bucket.from + bucket.to) / 2 >= 0 ? "#00ffa3" : "#ff2e2e",
    }));
}

export function buildRegimeRuns(
    sequence: { date: string; state: number }[],
    startDate: string,
    endDate: string,
): { x1: string; x2: string; state: number }[] {
    const filtered = sequence.filter(p => p.date >= startDate && p.date <= endDate);
    if (filtered.length === 0) return [];
    const runs: { x1: string; x2: string; state: number }[] = [];
    let runStart = filtered[0].date.substring(5);
    let runState = filtered[0].state;
    for (let i = 1; i < filtered.length; i++) {
        if (filtered[i].state !== runState) {
            runs.push({ x1: runStart, x2: filtered[i - 1].date.substring(5), state: runState });
            runStart = filtered[i].date.substring(5);
            runState = filtered[i].state;
        }
    }
    runs.push({ x1: runStart, x2: filtered[filtered.length - 1].date.substring(5), state: runState });
    return runs;
}

export const REGIME_FILL: Record<number, string> = { 0: "#10b981", 1: "#f59e0b", 2: "#ef4444" };
