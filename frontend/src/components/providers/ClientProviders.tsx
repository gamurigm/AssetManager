"use client";

import dynamic from "next/dynamic";
import { PortfolioProvider } from "@/context/PortfolioContext";
import BackendGate from "@/components/layout/BackendGate";

// Lazy-load heavy components that aren't needed for initial render
const ChatWidget = dynamic(() => import("@/components/ai/ChatWidget"), {
    ssr: false,
    loading: () => null,
});
const GlobalSearch = dynamic(() => import("@/components/layout/GlobalSearch"), {
    ssr: false,
    loading: () => null,
});

export default function ClientProviders({ children }: { children: React.ReactNode }) {
    return (
        <BackendGate>
            <PortfolioProvider>
                <GlobalSearch />
                {children}
                <ChatWidget />
            </PortfolioProvider>
        </BackendGate>
    );
}
