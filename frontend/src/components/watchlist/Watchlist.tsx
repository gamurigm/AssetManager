"use client"

import { useState, useEffect, useRef } from "react";
import { Plus, MoreHorizontal, ChevronDown, ChevronRight, ExternalLink, LayoutGrid, Pencil, X } from "lucide-react";
import styles from "./Watchlist.module.css";

declare global {
    interface Window {
        electronAPI: {
            openChart: (symbol: string) => void;
        };
    }
}

interface WatchlistItem {
    symbol: string;
    price: number;
    change: number;
    changePercent: number;
}

interface WatchlistGroup {
    name: string;
    expanded: boolean;
    symbols: string[];
}

// ── Icon map for popular symbols ──────────────────────────────────
const SYMBOL_ICONS: Record<string, { bg: string; label: string; textColor?: string }> = {
    "BTC/USD": { bg: "#F7931A", label: "₿" },
    "BTCUSD": { bg: "#F7931A", label: "₿" },
    "USDX": { bg: "#26A69A", label: "$" },
    "OILUSD": { bg: "#1a1a1a", label: "●", textColor: "#fff" },
    "CHFUSD": { bg: "#D32F2F", label: "+" },
    "USDMXN": { bg: "#D32F2F", label: "$" },
    "CHFEUR": { bg: "#D32F2F", label: "+" },
    "TLT": { bg: "#1565C0", label: "i" },
    "NASDAQ": { bg: "#1565C0", label: "N" },
    "SOLANA": { bg: "#9945FF", label: "S" },
    "SOL/USD": { bg: "#9945FF", label: "S" },
    "RSP": { bg: "#E91E63", label: "R" },
    "GOOG": { bg: "#4285F4", label: "G" },
    "EURGBP": { bg: "#3949AB", label: "€" },
    "ETH/USD": { bg: "#627EEA", label: "Ξ" },
    "NVDA": { bg: "#76B900", label: "N" },
    "AAPL": { bg: "#555555", label: "" },
    "MSFT": { bg: "#00A4EF", label: "M" },
    "AMZN": { bg: "#FF9900", label: "A" },
    "TSLA": { bg: "#CC0000", label: "T" },
    "META": { bg: "#0081FB", label: "M" },
};

function getSymbolIcon(symbol: string) {
    const key = symbol.toUpperCase().replace("/", "");
    const match = SYMBOL_ICONS[symbol] || SYMBOL_ICONS[key] || Object.entries(SYMBOL_ICONS).find(([k]) => key.includes(k))?.[1];
    if (match) return match;
    let hash = 0;
    for (let i = 0; i < symbol.length; i++) hash = symbol.charCodeAt(i) + ((hash << 5) - hash);
    const hue = Math.abs(hash) % 360;
    return { bg: `hsl(${hue}, 55%, 50%)`, label: symbol[0]?.toUpperCase() || "?" };
}

// ── Format price with superscript last digits ──────────────────────
function PriceDisplay({ price }: { price: number }) {
    if (price === 0) return <span className={styles.wlPriceZero}>—</span>;
    let decimals = 2;
    if (price < 1) decimals = 5;
    else if (price < 100) decimals = 4;
    else if (price < 10000) decimals = 3;

    const str = price.toFixed(decimals);
    const [whole, dec] = str.split(".");
    if (!dec) return <span>{whole}</span>;
    const mainDec = dec.substring(0, Math.max(0, dec.length - 2));
    const superDec = dec.substring(Math.max(0, dec.length - 2));
    return (
        <span className={styles.wlPrice}>
            {whole}.{mainDec}
            <sup className={styles.wlPriceSuper}>{superDec}</sup>
        </span>
    );
}

export default function Watchlist({ onSelectSymbol }: { onSelectSymbol: (s: string) => void }) {
    const [items, setItems] = useState<WatchlistItem[]>([]);
    const [selectedSymbol, setSelectedSymbol] = useState<string | null>(null);
    const [newSymbol, setNewSymbol] = useState("");
    const [showAddInput, setShowAddInput] = useState(false);
    const addInputRef = useRef<HTMLInputElement>(null);

    const [groups, setGroups] = useState<WatchlistGroup[]>([
        { name: "CRIPTO", expanded: true, symbols: ["BTC/USD", "ETH/USD", "SOL/USD"] },
        { name: "FOREX", expanded: true, symbols: ["USDMXN", "EURGBP", "CHFEUR"] },
        { name: "STOCKS", expanded: true, symbols: ["AAPL", "NVDA", "GOOG", "MSFT"] },
        { name: "INDICES", expanded: true, symbols: ["NASDAQ", "RSP"] },
    ]);

    const allSymbols = groups.flatMap(g => g.symbols);

    // Fetch quote data
    useEffect(() => {
        const fetchAll = async () => {
            const data = await Promise.all(
                allSymbols.map(async (s) => {
                    try {
                        const res = await fetch(`http://127.0.0.1:8282/api/v1/market/quote/${encodeURIComponent(s)}`);
                        const d = await res.json();
                        const prc = d.price || 0;
                        const chgPct = d.changePercentage || 0;
                        return {
                            symbol: s,
                            price: prc,
                            change: prc * (chgPct / 100),
                            changePercent: chgPct,
                        };
                    } catch {
                        return { symbol: s, price: 0, change: 0, changePercent: 0 };
                    }
                })
            );
            setItems(data);
        };
        fetchAll();
        const timer = setInterval(fetchAll, 30000);
        return () => clearInterval(timer);
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [allSymbols.join(",")]);

    const toggleGroup = (name: string) => {
        setGroups(prev => prev.map(g => g.name === name ? { ...g, expanded: !g.expanded } : g));
    };

    const addSymbol = () => {
        if (!newSymbol.trim()) return;
        const sym = newSymbol.toUpperCase().trim();
        if (allSymbols.includes(sym)) { setNewSymbol(""); return; }
        setGroups(prev => {
            const copy = [...prev];
            if (copy.length > 0) {
                copy[0] = { ...copy[0], symbols: [...copy[0].symbols, sym] };
            }
            return copy;
        });
        setNewSymbol("");
        setShowAddInput(false);
    };

    const handleSelectSymbol = (symbol: string) => {
        setSelectedSymbol(symbol);
        onSelectSymbol(symbol);
    };

    const selectedItem = items.find(i => i.symbol === selectedSymbol);

    useEffect(() => {
        if (showAddInput && addInputRef.current) {
            addInputRef.current.focus();
        }
    }, [showAddInput]);

    const formatChange = (val: number) => {
        const abs = Math.abs(val);
        if (abs === 0) return "0.00";
        if (abs < 0.01) return val.toFixed(5);
        if (abs < 1) return val.toFixed(4);
        if (abs < 100) return val.toFixed(3);
        return val.toFixed(1);
    };

    return (
        <div className={styles.wlRoot}>
            {/* ── Header Bar ────────────────────────────── */}
            <div className={styles.wlHeader}>
                <div className={styles.wlHeaderLeft}>
                    <span className={styles.wlTitle}>Lista de seguimiento</span>
                    <ChevronDown size={12} className={styles.wlTitleArrow} />
                </div>
                <div className={styles.wlHeaderActions}>
                    <button
                        className={styles.wlHeaderBtn}
                        title="Agregar símbolo"
                        onClick={() => setShowAddInput(!showAddInput)}
                    >
                        <Plus size={16} />
                    </button>
                    <button className={styles.wlHeaderBtn} title="Vista">
                        <LayoutGrid size={16} />
                    </button>
                    <button className={styles.wlHeaderBtn} title="Más opciones">
                        <MoreHorizontal size={16} />
                    </button>
                </div>
            </div>

            {/* ── Add Symbol Input ──────────────────────── */}
            {showAddInput && (
                <div className={styles.wlAddBar}>
                    <input
                        ref={addInputRef}
                        type="text"
                        value={newSymbol}
                        onChange={(e) => setNewSymbol(e.target.value)}
                        onKeyDown={(e) => {
                            if (e.key === "Enter") addSymbol();
                            if (e.key === "Escape") setShowAddInput(false);
                        }}
                        placeholder="Buscar símbolo... (ej: AAPL)"
                        className={styles.wlAddInput}
                    />
                    <button onClick={addSymbol} className={styles.wlAddBtn}>Agregar</button>
                    <button onClick={() => setShowAddInput(false)} className={styles.wlAddClose}>
                        <X size={14} />
                    </button>
                </div>
            )}

            {/* ── Column Headers ───────────────────────── */}
            <div className={styles.wlColHeaders}>
                <span>Symbol</span>
                <span className={styles.wlColLast}>Last</span>
                <span className={styles.wlColChg}>Chg</span>
                <span className={styles.wlColChgpct}>Chg%</span>
            </div>

            {/* ── Scrollable List ──────────────────────── */}
            <div className={styles.wlList}>
                {groups.map((group) => (
                    <div key={group.name}>
                        {/* Group Header */}
                        <div
                            className={styles.wlGroupHeader}
                            onClick={() => toggleGroup(group.name)}
                        >
                            {group.expanded
                                ? <ChevronDown size={12} className={styles.wlGroupArrow} />
                                : <ChevronRight size={12} className={styles.wlGroupArrow} />
                            }
                            <span className={styles.wlGroupName}>{group.name}</span>
                        </div>

                        {/* Group Items */}
                        {group.expanded && group.symbols.map((sym) => {
                            const item = items.find(i => i.symbol === sym);
                            const iconInfo = getSymbolIcon(sym);
                            const isPositive = (item?.changePercent || 0) >= 0;
                            const colorClass = isPositive ? styles.wlPositive : styles.wlNegative;
                            const isSelected = selectedSymbol === sym;

                            return (
                                <div
                                    key={sym}
                                    className={`${styles.wlRow} ${isSelected ? styles.wlRowSelected : ""}`}
                                    onClick={() => handleSelectSymbol(sym)}
                                >
                                    <div className={styles.wlRowSymbol}>
                                        <div
                                            className={styles.wlIcon}
                                            style={{ backgroundColor: iconInfo.bg, color: iconInfo.textColor || "#fff" }}
                                        >
                                            {iconInfo.label}
                                        </div>
                                        <span className={styles.wlSymName}>{sym}</span>
                                    </div>
                                    <span className={styles.wlRowLast}>
                                        {item ? <PriceDisplay price={item.price} /> : "—"}
                                    </span>
                                    <span className={`${styles.wlRowChg} ${colorClass}`}>
                                        {item ? formatChange(item.change) : "—"}
                                    </span>
                                    <span className={`${styles.wlRowChgpct} ${colorClass}`}>
                                        {item ? `${item.changePercent.toFixed(2)}%` : "—"}
                                    </span>
                                </div>
                            );
                        })}
                    </div>
                ))}
            </div>

            {/* ── Bottom Detail Panel (selected symbol) ── */}
            {selectedItem && selectedItem.price > 0 && (
                <div className={styles.wlDetail}>
                    <div className={styles.wlDetailHeader}>
                        <div className={styles.wlDetailLeft}>
                            <div
                                className={styles.wlDetailIcon}
                                style={{ backgroundColor: getSymbolIcon(selectedItem.symbol).bg, color: getSymbolIcon(selectedItem.symbol).textColor || "#fff" }}
                            >
                                {getSymbolIcon(selectedItem.symbol).label}
                            </div>
                            <span className={styles.wlDetailSym}>{selectedItem.symbol}</span>
                        </div>
                        <div className={styles.wlDetailActions}>
                            <button className={styles.wlDetailBtn}><LayoutGrid size={14} /></button>
                            <button className={styles.wlDetailBtn}><Pencil size={14} /></button>
                            <button className={styles.wlDetailBtn}><MoreHorizontal size={14} /></button>
                        </div>
                    </div>
                    <div className={styles.wlDetailMeta}>
                        <span className={styles.wlDetailName}>{selectedItem.symbol}</span>
                        <ExternalLink size={10} className={styles.wlDetailExtlink} />
                    </div>
                    <div className={styles.wlDetailPriceRow}>
                        <span className={styles.wlDetailPrice}>
                            {selectedItem.price.toLocaleString("en-US", { minimumFractionDigits: 3, maximumFractionDigits: 3 })}
                        </span>
                        <span className={styles.wlDetailCurrency}>USD</span>
                        <span className={`${styles.wlDetailChg} ${selectedItem.changePercent >= 0 ? styles.wlPositive : styles.wlNegative}`}>
                            {selectedItem.change >= 0 ? "+" : ""}{formatChange(selectedItem.change)}
                        </span>
                        <span className={`${styles.wlDetailChgpct} ${selectedItem.changePercent >= 0 ? styles.wlPositive : styles.wlNegative}`}>
                            {selectedItem.changePercent >= 0 ? "+" : ""}{selectedItem.changePercent.toFixed(2)}%
                        </span>
                    </div>
                    <div className={styles.wlDetailStatus}>
                        <span className={styles.wlDetailDot} />
                        <span>Market open</span>
                    </div>
                </div>
            )}
        </div>
    );
}
