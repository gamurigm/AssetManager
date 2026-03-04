"use client";

import React, { useState } from "react";
import { X } from "lucide-react";
import AppLayout from "@/components/layout/AppLayout";
import { useDashboardData } from "@/hooks/useDashboardData";
import PortfolioView from "@/components/dashboard/PortfolioView";
import SymbolChart from "@/components/dashboard/SymbolChart";
import DashboardSidebar from "@/components/dashboard/DashboardSidebar";
import type { SidebarTab } from "@/types/dashboard";

// ─── Dashboard Composition Root ─────────────────────────────────────
export default function ClientDashboard() {
    // Data layer (all fetching & derived state encapsulated in hook)
    const {
        activeHoldings, totalValue, accountEquity, totalPnL, pnlPercent,
        closePosition, loading, transactions, riskData, treemapData, sectorData,
    } = useDashboardData();

    // Tab navigation
    const [activeTab, setActiveTab] = useState("portfolio");
    const [openTabs, setOpenTabs] = useState<{ id: string; title: string; symbol: string | null }[]>([
        { id: "portfolio", title: "My Portfolio", symbol: null },
    ]);

    // Panel collapse state
    const [collapsed, setCollapsed] = useState<Record<string, boolean>>({});
    const togglePanel = (id: string) => setCollapsed(prev => ({ ...prev, [id]: !prev[id] }));

    // Sidebar state
    const [watchlistPinned, setWatchlistPinned] = useState(false);
    const [activeSidebarTab, setActiveSidebarTab] = useState<SidebarTab>('watchlist');
    const [globalShowFib, setGlobalShowFib] = useState(false);
    const [globalShowBollinger, setGlobalShowBollinger] = useState(false);
    const [globalShowIchimoku, setGlobalShowIchimoku] = useState(false);
    const [globalShowVwap, setGlobalShowVwap] = useState(false);
    const [globalShowRsi, setGlobalShowRsi] = useState(false);
    const [globalShowAtr, setGlobalShowAtr] = useState(false);
    const [globalShowKeltner, setGlobalShowKeltner] = useState(false);
    const [globalShowCci, setGlobalShowCci] = useState(false);
    const [globalShowAdx, setGlobalShowAdx] = useState(false);
    const [globalShowPsar, setGlobalShowPsar] = useState(false);
    const [globalShowSupertrend, setGlobalShowSupertrend] = useState(false);
    const [globalShowWilliams, setGlobalShowWilliams] = useState(false);
    const [globalShowMfi, setGlobalShowMfi] = useState(false);
    const [globalShowCmf, setGlobalShowCmf] = useState(false);

    // Tab actions
    const openSymbolTab = (symbol: string) => {
        if (!openTabs.find(t => t.id === symbol)) {
            setOpenTabs(prev => [...prev, { id: symbol, title: symbol, symbol }]);
        }
        setActiveTab(symbol);
    };

    const closeTab = (e: React.MouseEvent, id: string) => {
        e.stopPropagation();
        if (id === "portfolio") return;
        setOpenTabs(prev => prev.filter(t => t.id !== id));
        if (activeTab === id) setActiveTab("portfolio");
    };

    return (
        <AppLayout>
            <div className="flex flex-col h-full bg-background animate-fade-in">
                {/* Tabs Bar */}
                <div className="flex items-center gap-1 px-4 pt-4 border-b border-border bg-card/30">
                    {openTabs.map((tab) => (
                        <div
                            key={tab.id}
                            onClick={() => setActiveTab(tab.id)}
                            className={`group flex items-center gap-2 px-4 py-2 text-xs font-bold uppercase tracking-wider cursor-pointer transition-all rounded-t-xl border-t border-x border-transparent translate-y-[1px] ${activeTab === tab.id
                                ? "bg-background border-border text-accent"
                                : "text-muted hover:text-foreground hover:bg-card/50"
                                }`}
                        >
                            {tab.id === "portfolio" ? "Portfolio Alpha" : tab.title}
                            {tab.id !== "portfolio" && (
                                <X size={12} onClick={(e) => closeTab(e, tab.id)}
                                    className="opacity-0 group-hover:opacity-100 hover:text-red transition-opacity p-0.5 rounded-md hover:bg-red/10" />
                            )}
                        </div>
                    ))}
                </div>

                {/* Main Content + Sidebar */}
                <div className="flex-1 flex overflow-hidden relative">
                    <div className={`flex-1 overflow-hidden p-4 lg:px-6 lg:py-4 flex flex-col gap-4 transition-[padding] ease-[cubic-bezier(0.16,1,0.3,1)] duration-500 ${watchlistPinned ? 'pr-[350px]' : 'pr-[52px]'}`}>
                        {activeTab === "portfolio" ? (
                            <PortfolioView
                                activeHoldings={activeHoldings}
                                totalValue={totalValue}
                                accountEquity={accountEquity}
                                totalPnL={totalPnL}
                                pnlPercent={pnlPercent}
                                riskData={riskData}
                                transactions={transactions}
                                treemapData={treemapData}
                                sectorData={sectorData}
                                collapsed={collapsed}
                                togglePanel={togglePanel}
                                onSelectSymbol={openSymbolTab}
                            />
                        ) : (
                            <div className="flex-1 min-h-0 rounded-2xl overflow-hidden border border-border bg-card">
                                <SymbolChart
                                    symbol={activeTab} showFib={globalShowFib} showBollinger={globalShowBollinger}
                                    showIchimoku={globalShowIchimoku} showVwap={globalShowVwap} showRsi={globalShowRsi}
                                    showAtr={globalShowAtr} showKeltner={globalShowKeltner} showCci={globalShowCci}
                                    showAdx={globalShowAdx} showPsar={globalShowPsar} showSupertrend={globalShowSupertrend}
                                    showWilliams={globalShowWilliams} showMfi={globalShowMfi} showCmf={globalShowCmf}
                                />
                            </div>
                        )}
                    </div>

                    {/* Sidebar */}
                    <DashboardSidebar
                        pinned={watchlistPinned}
                        setPinned={setWatchlistPinned}
                        activeTab={activeSidebarTab}
                        setActiveTab={setActiveSidebarTab}
                        showFib={globalShowFib}
                        setShowFib={setGlobalShowFib}
                        showBollinger={globalShowBollinger}
                        setShowBollinger={setGlobalShowBollinger}
                        showIchimoku={globalShowIchimoku}
                        setShowIchimoku={setGlobalShowIchimoku}
                        showVwap={globalShowVwap}
                        setShowVwap={setGlobalShowVwap}
                        showRsi={globalShowRsi}
                        setShowRsi={setGlobalShowRsi}
                        showAtr={globalShowAtr}
                        setShowAtr={setGlobalShowAtr}
                        showKeltner={globalShowKeltner}
                        setShowKeltner={setGlobalShowKeltner}
                        showCci={globalShowCci}
                        setShowCci={setGlobalShowCci}
                        showAdx={globalShowAdx}
                        setShowAdx={setGlobalShowAdx}
                        showPsar={globalShowPsar}
                        setShowPsar={setGlobalShowPsar}
                        showSupertrend={globalShowSupertrend}
                        setShowSupertrend={setGlobalShowSupertrend}
                        showWilliams={globalShowWilliams}
                        setShowWilliams={setGlobalShowWilliams}
                        showMfi={globalShowMfi}
                        setShowMfi={setGlobalShowMfi}
                        showCmf={globalShowCmf}
                        setShowCmf={setGlobalShowCmf}
                        transactions={transactions}
                        onSelectSymbol={openSymbolTab}
                    />
                </div>
            </div>
        </AppLayout>
    );
}
