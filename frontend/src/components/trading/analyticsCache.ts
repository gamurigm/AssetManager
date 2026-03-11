/**
 * In-memory analytics cache — avoids re-fetching static data like
 * IV smile, ARCH/GARCH, Kalman filter, OHLCV and regime data for
 * symbols that have already been loaded during this browser session.
 * 
 * TTL = 5 minutes (300 000 ms). After that the data is considered
 * stale and will be re-fetched on next request.
 */

import type { ArchVolData, IvSmileData, KalmanFilterData, RegimeData } from "./types";

const TTL_MS = 5 * 60 * 1000; // 5 minutes

type CacheEntry<T> = {
    data: T;
    timestamp: number;
};

function isStale<T>(entry: CacheEntry<T> | undefined): boolean {
    if (!entry) return true;
    return Date.now() - entry.timestamp > TTL_MS;
}

// ── IV Smile cache ───────────────────────────────────────────────────
const ivCache = new Map<string, CacheEntry<IvSmileData>>();

export function getCachedIvSmile(symbol: string): IvSmileData | null {
    const entry = ivCache.get(symbol);
    if (isStale(entry)) return null;
    return entry!.data;
}
export function setCachedIvSmile(symbol: string, data: IvSmileData): void {
    ivCache.set(symbol, { data, timestamp: Date.now() });
}

// ── ARCH / GARCH cache ───────────────────────────────────────────────
const archCache = new Map<string, CacheEntry<ArchVolData>>();

export function getCachedArchVol(symbol: string): ArchVolData | null {
    const entry = archCache.get(symbol);
    if (isStale(entry)) return null;
    return entry!.data;
}
export function setCachedArchVol(symbol: string, data: ArchVolData): void {
    archCache.set(symbol, { data, timestamp: Date.now() });
}

// ── Kalman Filter cache ──────────────────────────────────────────────
const kalmanCache = new Map<string, CacheEntry<KalmanFilterData>>();

export function getCachedKalman(symbol: string): KalmanFilterData | null {
    const entry = kalmanCache.get(symbol);
    if (isStale(entry)) return null;
    return entry!.data;
}
export function setCachedKalman(symbol: string, data: KalmanFilterData): void {
    kalmanCache.set(symbol, { data, timestamp: Date.now() });
}

// ── OHLCV (historical prices) cache ──────────────────────────────────
// Key: "SYMBOL"  (we cache the raw API response)
const ohlcvCache = new Map<string, CacheEntry<any[]>>();

export function getCachedOHLCV(symbol: string): any[] | null {
    const entry = ohlcvCache.get(symbol);
    if (isStale(entry)) return null;
    return entry!.data;
}
export function setCachedOHLCV(symbol: string, data: any[]): void {
    ohlcvCache.set(symbol, { data, timestamp: Date.now() });
}

// ── Regime data cache ────────────────────────────────────────────────
const regimeCache = new Map<string, CacheEntry<RegimeData>>();

export function getCachedRegime(symbol: string): RegimeData | null {
    const entry = regimeCache.get(symbol);
    if (isStale(entry)) return null;
    return entry!.data;
}
export function setCachedRegime(symbol: string, data: RegimeData): void {
    regimeCache.set(symbol, { data, timestamp: Date.now() });
}
