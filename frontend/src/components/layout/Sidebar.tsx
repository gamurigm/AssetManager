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
} from "lucide-react";
import { useState, useEffect } from "react";

const unifiedNav = [
    { label: "Overview", href: "/manager/dashboard", icon: LayoutDashboard },
    { label: "Portfolios", href: "/client/dashboard", icon: PieChart },
    { label: "Backtest Lab", href: "/client/trading", icon: ArrowLeftRight },
    { label: "Strategies", href: "/manager/clients", icon: Briefcase },
];

export default function Sidebar({ expanded }: { expanded: boolean }) {
    const pathname = usePathname();
    const [isDarkMode, setIsDarkMode] = useState(true);

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
