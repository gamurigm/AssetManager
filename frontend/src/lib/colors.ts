// ─── Color Utilities ────────────────────────────────────────────────
// Centralized color maps — prevents duplication across components.

/**
 * Sector → Color mapping for charts and heatmaps
 */
export const SECTOR_COLORS: Record<string, string> = {
    "Technology": "#3b82f6",
    "Digital Assets": "#06b6d4",
    "Forex": "#f97316",
    "Commodities": "#eab308",
    "Financials": "#10b981",
    "Energy": "#f59e0b",
    "Health Care": "#ef4444",
    "Consumer Discretionary": "#ec4899",
};

/**
 * Maps a percent-change value to a heatmap color.
 * Used in the holdings table and treemap.
 */
export function getHeatmapColor(cv: number): string {
    if (cv > 5) return '#065f46';
    if (cv > 2.5) return '#10b981';
    if (cv > 1) return '#4ade80';
    if (cv >= 0.5) return '#fde047';
    if (cv >= 0.1) return '#facc15';
    if (cv > -0.1) return '#71717a';
    if (cv >= -0.5) return '#fbbf24';
    if (cv >= -1) return '#f97316';
    if (cv >= -3) return '#f43f5e';
    return '#ef4444';
}

/** Colors considered "bright" for text contrast decisions */
export const BRIGHT_BADGE_COLORS = ['#fde047', '#facc15', '#fbbf24', '#4ade80'];

/** StatCard accent color classes */
export const STAT_ACCENT_COLORS: Record<string, string> = {
    blue: "text-blue-400 bg-blue-500/10 border-blue-500/20 shadow-blue-500/5",
    green: "text-green bg-green/10 border-green/20 shadow-green/5",
    red: "text-red bg-red/10 border-red/20 shadow-red/5",
    purple: "text-purple-400 bg-purple-500/10 border-purple-500/20 shadow-purple-500/5",
    emerald: "text-emerald-400 bg-emerald-500/10 border-emerald-500/20 shadow-emerald-500/5",
};
