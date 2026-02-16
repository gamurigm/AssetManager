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
} from "lucide-react";
import { useState } from "react";

const clientNav = [
    { label: "Portfolio", href: "/client/dashboard", icon: PieChart },
    { label: "Trading", href: "/client/trading", icon: ArrowLeftRight },
];

const managerNav = [
    { label: "AUM Overview", href: "/manager/dashboard", icon: Briefcase },
    { label: "Clients", href: "/manager/clients", icon: Users },
];

export default function Sidebar() {
    const pathname = usePathname();
    const [collapsed, setCollapsed] = useState(false);

    const isManager = pathname.startsWith("/manager");
    const navItems = isManager ? managerNav : clientNav;
    const roleLabel = isManager ? "Manager" : "Client";

    return (
        <aside
            className={`fixed top-0 left-0 h-screen z-40 flex flex-col border-r border-border bg-[#0c0c0f] transition-all duration-300 ${collapsed ? "w-[68px]" : "w-[240px]"
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

            {/* Role Switcher */}
            <div className="px-3 pt-4 pb-2">
                <div className="flex gap-1 bg-card rounded-lg p-1">
                    <Link
                        href="/client/dashboard"
                        className={`flex-1 text-center text-[11px] font-semibold py-1.5 rounded-md transition-all ${!isManager
                                ? "bg-accent text-white shadow-sm"
                                : "text-muted hover:text-foreground"
                            }`}
                    >
                        {collapsed ? "C" : "Client"}
                    </Link>
                    <Link
                        href="/manager/dashboard"
                        className={`flex-1 text-center text-[11px] font-semibold py-1.5 rounded-md transition-all ${isManager
                                ? "bg-accent text-white shadow-sm"
                                : "text-muted hover:text-foreground"
                            }`}
                    >
                        {collapsed ? "M" : "Manager"}
                    </Link>
                </div>
            </div>

            {/* Navigation */}
            <nav className="flex-1 px-3 py-2 space-y-1 stagger overflow-y-auto">
                {!collapsed && (
                    <p className="text-[10px] uppercase tracking-widest text-muted px-2 pb-1 pt-2 font-semibold">
                        {roleLabel}
                    </p>
                )}
                {navItems.map((item) => {
                    const isActive = pathname === item.href;
                    return (
                        <Link
                            key={item.href}
                            href={item.href}
                            className={`flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-all group relative ${isActive
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
