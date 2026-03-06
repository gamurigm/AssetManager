"use client"

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
    LayoutDashboard,
    ArrowLeftRight,
    PieChart,
    Briefcase,
    Sun,
    Moon,
    Wallet,
    Bitcoin,
    Cpu,
    Crosshair,
    Globe2,
    Landmark,
    Leaf,
    LineChart,
    Building2,
    Cog
} from "lucide-react";
import { useState, useEffect } from "react";
import { usePortfolio } from "@/context/PortfolioContext";

// Define the full list of portfolios requested by user + 3 suggestions
const PORTFOLIOS = [
    { id: "main", label: "Main Fund", icon: Wallet, color: "blue", activeBgDark: "bg-blue-500/20", activeTextDark: "text-blue-400", activeBorderDark: "border-blue-500/20", activeBgLight: "bg-blue-100", activeTextLight: "text-blue-600", activeBorderLight: "border-blue-300" },
    { id: "crypto", label: "Crypto Assets", icon: Bitcoin, color: "orange", activeBgDark: "bg-orange-500/20", activeTextDark: "text-orange-400", activeBorderDark: "border-orange-500/20", activeBgLight: "bg-orange-100", activeTextLight: "text-orange-600", activeBorderLight: "border-orange-300" },
    { id: "tech", label: "Technology", icon: Cpu, color: "indigo", activeBgDark: "bg-indigo-500/20", activeTextDark: "text-indigo-400", activeBorderDark: "border-indigo-500/20", activeBgLight: "bg-indigo-100", activeTextLight: "text-indigo-600", activeBorderLight: "border-indigo-300" },
    { id: "med", label: "Medicine", icon: Crosshair, color: "rose", activeBgDark: "bg-rose-500/20", activeTextDark: "text-rose-400", activeBorderDark: "border-rose-500/20", activeBgLight: "bg-rose-100", activeTextLight: "text-rose-600", activeBorderLight: "border-rose-300" },
    { id: "asian", label: "Asian Mkts", icon: Globe2, color: "red", activeBgDark: "bg-red-500/20", activeTextDark: "text-red-400", activeBorderDark: "border-red-500/20", activeBgLight: "bg-red-100", activeTextLight: "text-red-600", activeBorderLight: "border-red-300" },
    { id: "europe", label: "Europe Mkts", icon: Globe2, color: "blue", activeBgDark: "bg-blue-600/20", activeTextDark: "text-blue-500", activeBorderDark: "border-blue-600/20", activeBgLight: "bg-blue-200", activeTextLight: "text-blue-700", activeBorderLight: "border-blue-400" },
    { id: "emergin", label: "Emerging", icon: Leaf, color: "emerald", activeBgDark: "bg-emerald-500/20", activeTextDark: "text-emerald-400", activeBorderDark: "border-emerald-500/20", activeBgLight: "bg-emerald-100", activeTextLight: "text-emerald-600", activeBorderLight: "border-emerald-300" },
    { id: "bonds", label: "Bonds", icon: Landmark, color: "slate", activeBgDark: "bg-slate-500/20", activeTextDark: "text-slate-400", activeBorderDark: "border-slate-500/20", activeBgLight: "bg-slate-200", activeTextLight: "text-slate-600", activeBorderLight: "border-slate-300" },
    { id: "test1", label: "Test 1", icon: Cog, color: "zinc", activeBgDark: "bg-zinc-500/20", activeTextDark: "text-zinc-400", activeBorderDark: "border-zinc-500/20", activeBgLight: "bg-zinc-200", activeTextLight: "text-zinc-600", activeBorderLight: "border-zinc-300" },
    { id: "test2", label: "Test 2", icon: Cog, color: "zinc", activeBgDark: "bg-zinc-500/20", activeTextDark: "text-zinc-400", activeBorderDark: "border-zinc-500/20", activeBgLight: "bg-zinc-200", activeTextLight: "text-zinc-600", activeBorderLight: "border-zinc-300" },
    // 3 Suggestions
    { id: "options", label: "Options/Deriv.", icon: LineChart, color: "purple", activeBgDark: "bg-purple-500/20", activeTextDark: "text-purple-400", activeBorderDark: "border-purple-500/20", activeBgLight: "bg-purple-100", activeTextLight: "text-purple-600", activeBorderLight: "border-purple-300" },
    { id: "real_estate", label: "Real Estate", icon: Building2, color: "amber", activeBgDark: "bg-amber-500/20", activeTextDark: "text-amber-400", activeBorderDark: "border-amber-500/20", activeBgLight: "bg-amber-100", activeTextLight: "text-amber-600", activeBorderLight: "border-amber-300" },
    { id: "ai_driven", label: "AI Driven", icon: Cpu, color: "cyan", activeBgDark: "bg-cyan-500/20", activeTextDark: "text-cyan-400", activeBorderDark: "border-cyan-500/20", activeBgLight: "bg-cyan-100", activeTextLight: "text-cyan-600", activeBorderLight: "border-cyan-300" },
];


const unifiedNav = [
    { label: "Overview", href: "/manager/dashboard", icon: LayoutDashboard },
    { label: "Portfolios", href: "/client/dashboard", icon: PieChart },
    { label: "Backtest Lab", href: "/client/trading", icon: ArrowLeftRight },
    { label: "Strategies", href: "/manager/clients", icon: Briefcase },
];

export default function Sidebar({ expanded }: { expanded: boolean }) {
    const pathname = usePathname();
    const [isDarkMode, setIsDarkMode] = useState(true);
    const { activePortfolio, setActivePortfolio } = usePortfolio();

    useEffect(() => {
        const savedTheme = localStorage.getItem("mmam_theme");
        if (savedTheme === "light") {
            setIsDarkMode(false);
        }
    }, []);

    useEffect(() => {
        if (isDarkMode) {
            document.documentElement.classList.remove("light");
            document.documentElement.classList.add("dark");
            localStorage.setItem("mmam_theme", "dark");
        } else {
            document.documentElement.classList.remove("dark");
            document.documentElement.classList.add("light");
            localStorage.setItem("mmam_theme", "light");
        }
    }, [isDarkMode]);

    const isCollapsed = !expanded;

    return (
        <aside
            suppressHydrationWarning
            className={`h-screen flex flex-col border-r transition-[width] ease-[cubic-bezier(0.16,1,0.3,1)] duration-500 group ${expanded ? "w-[240px]" : "w-[68px]"
                } ${isDarkMode
                    ? "bg-zinc-950/70 backdrop-blur-3xl border-white/5"
                    : "bg-white/70 backdrop-blur-3xl border-slate-200 shadow-[20px_0_40px_rgba(0,0,0,0.03)]"
                }`}
        >
            {/* Logo */}
            <div className={`flex items-center gap-3 px-[15px] h-16 border-b shrink-0 overflow-hidden relative ${isDarkMode ? "border-white/5" : "border-slate-100"}`}>
                <div className="h-9 w-9 rounded-full overflow-hidden flex items-center justify-center shrink-0 shadow-[0_0_20px_-5px_#3b82f6] border border-white/10">
                    <img src="/logoMM.png" alt="MMAM Logo" className="h-[28px] w-[28px] object-contain" />
                </div>
                <div className={`w-[140px] shrink-0 ${isCollapsed ? "opacity-0 invisible" : "opacity-100 visible delay-100"} transition-all duration-300 ease-[cubic-bezier(0.16,1,0.3,1)]`}>
                    <span className={`text-sm font-bold uppercase tracking-tight truncate ${isDarkMode ? "text-white/90" : "text-slate-800"}`}>
                        MMAM <span className="text-accent underline decoration-accent/30 underline-offset-4">Intelligence</span>
                    </span>
                </div>
            </div>

            {/* Navigation */}
            <nav className="flex-1 px-3 py-6 space-y-2 overflow-y-auto overflow-x-hidden">
                <p className={`text-[10px] uppercase tracking-[0.2em] px-2 pb-2 font-bold whitespace-nowrap ${isCollapsed ? "opacity-0 invisible" : "opacity-100 visible delay-100"} transition-all duration-300 ease-[cubic-bezier(0.16,1,0.3,1)] ${isDarkMode ? "text-white/30" : "text-slate-400"}`}>
                    Management
                </p>
                {unifiedNav.map((item) => {
                    const isActive = pathname === item.href;
                    return (
                        <Link
                            key={item.href}
                            href={item.href}
                            className={`flex items-center gap-3 px-3 py-3 rounded-xl text-sm font-bold transition-all relative ${isActive
                                ? (isDarkMode
                                    ? "bg-accent/20 text-accent shadow-[inset_0_0_10px_rgba(59,130,246,0.1)] border border-accent/20"
                                    : "bg-accent/15 text-accent border border-accent/30 shadow-sm")
                                : (isDarkMode
                                    ? "text-white/40 hover:text-white hover:bg-white/5"
                                    : "text-slate-500 hover:text-slate-900 hover:bg-slate-50")
                                }`}
                        >
                            {isActive && (
                                <div className="absolute left-[-12px] top-1/2 -translate-y-1/2 w-[4px] h-6 bg-accent rounded-r-full shadow-[0_0_15px_#3b82f6]" />
                            )}
                            <item.icon
                                size={18}
                                className={`shrink-0 transition-transform ${isActive
                                    ? (isDarkMode ? "text-accent drop-shadow-[0_0_8px_#3b82f6]" : "text-accent")
                                    : (isDarkMode ? "text-white/40" : "text-slate-400")}`}
                            />
                            <span className={`truncate tracking-tight whitespace-nowrap ${isCollapsed ? "opacity-0 invisible w-0" : "opacity-100 visible w-auto delay-100"} transition-all duration-300 ease-[cubic-bezier(0.16,1,0.3,1)]`}>
                                {item.label}
                            </span>
                        </Link>
                    );
                })}
            </nav>

            {/* Portfolio Selector */}
            <div className={`px-3 py-4 border-t ${isDarkMode ? "border-white/5" : "border-slate-100"}`}>
                <p className={`text-[10px] uppercase tracking-[0.2em] px-2 pb-2 font-bold whitespace-nowrap ${isCollapsed ? "opacity-0 invisible" : "opacity-100 visible delay-100"} transition-all duration-300 ease-[cubic-bezier(0.16,1,0.3,1)] ${isDarkMode ? "text-white/30" : "text-slate-400"}`}>
                    Active Portfolio
                </p>

                <div className={`flex flex-col gap-1 max-h-[300px] overflow-y-auto pr-1 custom-scrollbar ${isCollapsed ? "items-center" : ""}`}>
                    {PORTFOLIOS.map((p) => {
                        const isActive = activePortfolio === p.id;
                        return (
                            <button
                                key={p.id}
                                onClick={() => setActivePortfolio(p.id)}
                                className={`flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-bold transition-all relative ${isActive
                                        ? (isDarkMode
                                            ? `${p.activeBgDark} ${p.activeTextDark} shadow-[inset_0_0_10px_rgba(255,255,255,0.05)] border ${p.activeBorderDark}`
                                            : `${p.activeBgLight} ${p.activeTextLight} border ${p.activeBorderLight} shadow-sm`)
                                        : (isDarkMode
                                            ? "text-white/40 hover:text-white hover:bg-white/5 border border-transparent"
                                            : "text-slate-500 hover:text-slate-900 hover:bg-slate-50 border border-transparent")
                                    }`}
                                title={p.label}
                            >
                                <p.icon size={16} className={`shrink-0 ${isActive ? (isDarkMode ? p.activeTextDark : p.activeTextLight) : ""}`} />
                                <span className={`truncate tracking-tight whitespace-nowrap ${isCollapsed ? "opacity-0 invisible w-0 hidden" : "opacity-100 visible w-auto"} transition-all duration-300`}>
                                    {p.label}
                                </span>
                            </button>
                        );
                    })}
                </div>
            </div>

            {/* Bottom */}
            <div className={`px-3 pb-4 space-y-1 border-t pt-3 ${isDarkMode ? "border-white/5" : "border-slate-100"}`}>
                <button
                    onClick={() => setIsDarkMode(!isDarkMode)}
                    className={`w-full flex items-center gap-3 px-3 py-3 rounded-xl text-sm font-bold transition-all overflow-hidden ${isDarkMode
                        ? "text-white/40 hover:text-white hover:bg-white/5"
                        : "text-slate-500 hover:text-slate-900 hover:bg-slate-50"}`}
                >
                    {isDarkMode ? <Sun size={18} className="text-yellow-400 drop-shadow-[0_0_8px_#facc15] shrink-0" /> : <Moon size={18} className="text-slate-600 shrink-0" />}
                    <span className={`truncate tracking-tight whitespace-nowrap ${isCollapsed ? "opacity-0 invisible w-0" : "opacity-100 visible w-auto delay-100"} transition-all duration-300 ease-[cubic-bezier(0.16,1,0.3,1)]`}>
                        {isDarkMode ? "Light Mode" : "Dark Mode"}
                    </span>
                </button>
            </div>
        </aside>
    );
}
