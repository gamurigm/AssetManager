const FOREX_CODES = new Set([
    "USD", "EUR", "GBP", "JPY", "CHF", "CAD", "AUD", "NZD",
    "MXN", "SEK", "NOK", "DKK", "CNH", "CNY", "HKD", "SGD",
    "ZAR", "TRY", "PLN", "HUF", "CZK",
]);

interface AssetFormatContext {
    symbol?: string;
    sector?: string;
    assetType?: string;
    price?: number;
}

export function isForexSymbol(symbol?: string, sector?: string, assetType?: string) {
    if (sector?.toLowerCase() === "forex" || assetType?.toLowerCase() === "forex") {
        return true;
    }

    const normalized = (symbol || "")
        .toUpperCase()
        .replace("=X", "")
        .replace(/[^A-Z]/g, "");

    if (normalized.length !== 6) {
        return false;
    }

    const base = normalized.slice(0, 3);
    const quote = normalized.slice(3, 6);
    return FOREX_CODES.has(base) && FOREX_CODES.has(quote);
}

export function getAssetPriceDecimals({ symbol, sector, assetType, price }: AssetFormatContext) {
    if (isForexSymbol(symbol, sector, assetType)) {
        return 5;
    }

    if (typeof price === "number") {
        if (Math.abs(price) < 1) return 5;
        if (Math.abs(price) < 100) return 4;
        if (Math.abs(price) < 10000) return 3;
    }

    return 2;
}

export function formatAssetPrice(value: number, context: AssetFormatContext = {}) {
    const decimals = getAssetPriceDecimals({ ...context, price: value });
    return value.toLocaleString("en-US", {
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals,
    });
}

export function formatAssetPriceFixed(value: number, context: AssetFormatContext = {}) {
    return value.toFixed(getAssetPriceDecimals({ ...context, price: value }));
}

export function getChartPriceFormat(context: AssetFormatContext = {}) {
    const precision = getAssetPriceDecimals(context);
    return {
        type: "price" as const,
        precision,
        minMove: Number((1 / (10 ** precision)).toFixed(precision)),
    };
}