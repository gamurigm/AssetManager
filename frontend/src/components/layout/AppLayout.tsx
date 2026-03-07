"use client"

import dynamic from "next/dynamic";
import { useState, useEffect } from "react";

// Lazy-load heavy layout components (deferred until after BackendGate)
const Sidebar = dynamic(() => import("@/components/layout/Sidebar"), {
    ssr: false,
    loading: () => <div className="fixed top-0 left-0 h-screen w-[68px] border-r border-border bg-card z-40" />,
});
const HelpViewer = dynamic(() => import("@/components/layout/HelpViewer"), {
    ssr: false,
});
const OpenBBTerminal = dynamic(() => import("@/components/layout/OpenBBTerminal"), {
    ssr: false,
    loading: () => null,
});

export default function AppLayout({ children }: { children: React.ReactNode }) {
    const [mounted, setMounted] = useState(false);
    const [terminalHeight, setTerminalHeight] = useState(0);
    const [isHelpOpen, setIsHelpOpen] = useState(false);
    const [modalMode, setModalMode] = useState<'docs' | 'education'>('docs');

    useEffect(() => {
        setMounted(true);
    }, []);

    // Listen for terminal open/close/resize events
    useEffect(() => {
        const handler = (e: Event) => {
            const h = (e as CustomEvent).detail?.height ?? 0;
            setTerminalHeight(h);
        };
        const docsHandler = () => {
            setModalMode('docs');
            setIsHelpOpen(true);
        };
        const eduHandler = () => {
            setModalMode('education');
            setIsHelpOpen(true);
        };

        window.addEventListener('terminal-resize', handler);
        window.addEventListener('open-docs', docsHandler);
        window.addEventListener('open-education', eduHandler);

        return () => {
            window.removeEventListener('terminal-resize', handler);
            window.removeEventListener('open-docs', docsHandler);
            window.removeEventListener('open-education', eduHandler);
        };
    }, []);

    // Sidebar permanently collapsed
    const expanded = false;

    if (!mounted) {
        return (
            <div className="flex min-h-screen bg-background">
                <div className="fixed top-0 left-0 h-screen z-40 w-[68px] border-r border-border bg-card" />
                <main className="flex-1 ml-[68px]">
                    {children}
                </main>
            </div>
        );
    }

    return (
        <div className="flex h-screen bg-background text-foreground overflow-hidden">
            {/* Left Sidebar - Fixed width 68px */}
            <div className="z-[100] h-full shrink-0 border-r border-border bg-card">
                <Sidebar expanded={expanded} />
            </div>

            {/* Right Container - Flex Column (Main + Terminal) */}
            <div className="flex-1 flex flex-col min-w-0 h-full">
                <main className="flex-1 overflow-auto min-h-0 relative">
                    {children}
                </main>
                <div className="shrink-0">
                    <OpenBBTerminal />
                </div>
            </div>

            <HelpViewer
                isOpen={isHelpOpen}
                onClose={() => setIsHelpOpen(false)}
                mode={modalMode}
            />
        </div>
    );
}
