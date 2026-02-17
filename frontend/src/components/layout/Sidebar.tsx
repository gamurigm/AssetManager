"use client"

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
    LayoutDashboard,
    ArrowLeftRight,
    Users,
    PieChart,
    Briefcase,
    Bot,
    Settings,
    ChevronLeft,
    ChevronRight,
    Sun,
    Moon,
} from "lucide-react";
import { useState, useEffect } from "react";

const unifiedNav = [
    { label: "Overview", href: "/manager/dashboard", icon: LayoutDashboard },
    { label: "Portfolios", href: "/client/dashboard", icon: PieChart },
    { label: "Simulator", href: "/client/trading", icon: ArrowLeftRight },
    { label: "Strategies", href: "/manager/clients", icon: Briefcase },
];

export default function Sidebar() {
    const pathname = usePathname();
    const [collapsed, setCollapsed] = useState(false);
    const [isDarkMode, setIsDarkMode] = useState(true);
    const [mounted, setMounted] = useState(false);

    useEffect(() => {
        setMounted(true);
        const handleResize = () => {
            if (window.innerWidth < 1024) setCollapsed(true);
        };
        handleResize();
        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, []);

    // Sync theme with document
    useEffect(() => {
        if (!mounted) return;
        if (isDarkMode) {
            document.documentElement.classList.remove("light");
            document.documentElement.classList.add("dark");
        } else {
            document.documentElement.classList.remove("dark");
            document.documentElement.classList.add("light");
        }
    }, [isDarkMode, mounted]);

    if (!mounted) {
        return (
            <aside className="fixed top-0 left-0 h-screen z-40 w-[240px] border-r border-border bg-card" />
        );
    }

    return (
        <aside
            suppressHydrationWarning
            className={`fixed top-0 left-0 h-screen z-40 flex flex-col border-r transition-all duration-300 ${collapsed ? "w-[68px]" : "w-[240px]"} 
                ${isDarkMode
                    ? "bg-background/40 backdrop-blur-2xl border-white/5"
                    : "bg-white/70 backdrop-blur-2xl border-slate-200 shadow-xl"}`}
        >
            {/* Logo */}
            <div className={`flex items-center gap-3 px-5 h-16 border-b shrink-0 ${isDarkMode ? "border-white/5" : "border-slate-100"}`}>
                <div className="h-9 w-9 rounded-xl bg-gradient-to-br from-accent via-blue-500 to-indigo-600 flex items-center justify-center text-white font-black text-sm shrink-0 shadow-[0_0_20px_-5px_#3b82f6] border border-white/10">
                    MM
                </div>
                {!collapsed && (
                    <span className={`text-sm font-black uppercase tracking-tighter truncate animate-fade-in ${isDarkMode ? "text-white/90" : "text-slate-800"}`}>
                        MMAM <span className="text-accent underline decoration-accent/30 underline-offset-4">Intelligence</span>
                    </span>
                )}
            </div>

            {/* Navigation */}
            <nav className="flex-1 px-3 py-6 space-y-2 stagger overflow-y-auto">
                {!collapsed && (
                    <p className={`text-[10px] uppercase tracking-[0.2em] px-2 pb-2 font-black ${isDarkMode ? "text-white/30" : "text-slate-400"}`}>
                        Management
                    </p>
                )}
                {unifiedNav.map((item) => {
                    const isActive = pathname === item.href;
                    return (
                        <Link
                            key={item.href}
                            href={item.href}
                            className={`flex items-center gap-3 px-3 py-3 rounded-xl text-sm font-bold transition-all group relative ${isActive
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
                                className={`shrink-0 transition-transform group-hover:scale-110 ${isActive
                                    ? (isDarkMode ? "text-accent drop-shadow-[0_0_8px_#3b82f6]" : "text-accent")
                                    : (isDarkMode ? "text-white/40 group-hover:text-white" : "text-slate-400 group-hover:text-slate-900")}`}
                            />
                            {!collapsed && <span className="truncate tracking-tight">{item.label}</span>}
                        </Link>
                    );
                })}
            </nav>

            {/* Bottom */}
            <div className={`px-3 pb-4 space-y-1 border-t pt-3 ${isDarkMode ? "border-white/5" : "border-slate-100"}`}>
                <button
                    onClick={() => setIsDarkMode(!isDarkMode)}
                    className={`w-full flex items-center gap-3 px-3 py-3 rounded-xl text-sm font-bold transition-all ${isDarkMode
                        ? "text-white/40 hover:text-white hover:bg-white/5"
                        : "text-slate-500 hover:text-slate-900 hover:bg-slate-50"}`}
                >
                    {isDarkMode ? <Sun size={18} className="text-yellow-400 drop-shadow-[0_0_8px_#facc15]" /> : <Moon size={18} className="text-slate-600" />}
                    {!collapsed && <span>{isDarkMode ? "Light Mode" : "Dark Mode"}</span>}
                </button>
                <button
                    onClick={() => setCollapsed(!collapsed)}
                    className={`w-full flex items-center gap-3 px-3 py-3 rounded-xl text-sm font-bold transition-all ${isDarkMode
                        ? "text-white/40 hover:text-white hover:bg-white/5"
                        : "text-slate-500 hover:text-slate-900 hover:bg-slate-50"}`}
                >
                    {collapsed ? <ChevronRight size={18} /> : <ChevronLeft size={18} />}
                    {!collapsed && <span>Collapse</span>}
                </button>
            </div>
        </aside>
    );
}
