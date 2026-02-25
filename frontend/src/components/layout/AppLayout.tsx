"use client"

import Sidebar from "@/components/layout/Sidebar";
import { useState, useEffect } from "react";

export default function AppLayout({ children }: { children: React.ReactNode }) {
    const [collapsed, setCollapsed] = useState(false);

    useEffect(() => {
        const handleResize = () => {
            if (window.innerWidth < 1024) setCollapsed(true);
            else setCollapsed(false);
        };
        handleResize();
        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, []);

    return (
        <div className="flex min-h-screen">
            <Sidebar collapsed={collapsed} setCollapsed={setCollapsed} />
            <main
                className={`flex-1 transition-all duration-300 ${collapsed
                        ? "ml-[68px]"
                        : "lg:ml-[240px] ml-[68px]"
                    }`}
            >
                {children}
            </main>
        </div>
    );
}
