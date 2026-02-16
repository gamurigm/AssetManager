"use client"

import Sidebar from "@/components/layout/Sidebar";

export default function AppLayout({ children }: { children: React.ReactNode }) {
    return (
        <div className="flex min-h-screen">
            <Sidebar />
            <main className="flex-1 ml-[240px] transition-all duration-300">
                {children}
            </main>
        </div>
    );
}
