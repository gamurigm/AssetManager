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
            className={`fixed top-0 left-0 h-screen z-40 flex flex-col border-r border-border bg-card transition-all duration-300 ${collapsed ? "w-[68px]" : "w-[240px]"
                }`}
        >
            {/* Logo */}
            <div className="flex items-center gap-3 px-5 h-16 border-b border-border shrink-0">
                <div className="h-8 w-8 rounded-lg bg-gradient-to-br from-accent to-blue-400 flex items-center justify-center text-white font-bold text-sm shrink-0">
                    A
                </div>
                {!collapsed && (
                    <span className="text-sm font-bold tracking-tight truncate animate-fade-in">
                        Asset Manager
                    </span>
                )}
            </div>

            {/* Navigation */}
            <nav className="flex-1 px-3 py-6 space-y-1 stagger overflow-y-auto">
                {!collapsed && (
                    <p className="text-[10px] uppercase tracking-widest text-muted px-2 pb-2 font-semibold">
                        Management
                    </p>
                )}
                {unifiedNav.map((item) => {
                    const isActive = pathname === item.href;
                    return (
                        <Link
                            key={item.href}
                            href={item.href}
                            className={`flex items-center gap-3 px-3 py-3 rounded-xl text-sm font-medium transition-all group relative ${isActive
                                ? "bg-accent/10 text-accent"
                                : "text-muted hover:text-foreground hover:bg-card"
                                }`}
                        >
                            {isActive && (
                                <div className="absolute left-0 top-1/2 -translate-y-1/2 w-[3px] h-5 bg-accent rounded-r-full" />
                            )}
                            <item.icon
                                size={18}
                                className={`shrink-0 ${isActive ? "text-accent" : "text-muted group-hover:text-foreground"}`}
                            />
                            {!collapsed && <span className="truncate">{item.label}</span>}
                        </Link>
                    );
                })}
            </nav>

            {/* Bottom */}
            <div className="px-3 pb-4 space-y-1 border-t border-border pt-3">
                <button
                    onClick={() => setIsDarkMode(!isDarkMode)}
                    className="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium text-muted hover:text-foreground hover:bg-card transition-all"
                >
                    {isDarkMode ? <Sun size={18} /> : <Moon size={18} />}
                    {!collapsed && <span>{isDarkMode ? "Light Mode" : "Dark Mode"}</span>}
                </button>
                <button
                    onClick={() => setCollapsed(!collapsed)}
                    className="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium text-muted hover:text-foreground hover:bg-card transition-all"
                >
                    {collapsed ? <ChevronRight size={18} /> : <ChevronLeft size={18} />}
                    {!collapsed && <span>Collapse</span>}
                </button>
            </div>
        </aside>
    );
}
