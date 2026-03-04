"use client";

import { useEffect, useState, useCallback } from "react";
import GoldenBlackHole from "@/components/ui/GoldenBlackHole";

const BACKEND_URL = "http://127.0.0.1:8282";
const POLL_INTERVAL = 1500; // ms between health checks
const MAX_RETRIES = 60;     // ~90 seconds timeout

interface BackendGateProps {
    children: React.ReactNode;
}

export default function BackendGate({ children }: BackendGateProps) {
    const [ready, setReady] = useState(false);
    const [attempt, setAttempt] = useState(0);
    const [status, setStatus] = useState("Initializing systems...");

    const checkBackend = useCallback(async () => {
        try {
            const res = await fetch(`${BACKEND_URL}/`, {
                method: "GET",
                signal: AbortSignal.timeout(3000),
            });
            if (res.ok) {
                setStatus("Systems online. Launching terminal...");
                // Brief pause for the transition animation
                setTimeout(() => setReady(true), 400);
                return true;
            }
        } catch {
            // Backend not ready yet
        }
        return false;
    }, []);

    useEffect(() => {
        let timer: ReturnType<typeof setInterval>;
        let retryCount = 0;

        const poll = async () => {
            const isReady = await checkBackend();
            if (isReady) {
                clearInterval(timer);
                return;
            }
            retryCount++;
            setAttempt(retryCount);


            if (retryCount >= MAX_RETRIES) {
                setStatus("Backend unreachable. Please start the server.");
                clearInterval(timer);
            }
        };

        // First check immediately
        poll();
        timer = setInterval(poll, POLL_INTERVAL);

        return () => clearInterval(timer);
    }, [checkBackend]);



    if (ready) {
        return <div className="animate-gate-reveal">{children}</div>;
    }

    return (
        <div className="relative w-screen h-screen flex items-center justify-center overflow-hidden bg-black text-white font-sans">
            {/* 3D Background */}
            <GoldenBlackHole />

            {/* Central content - Glassmorphism overlay */}
            <div className="relative z-10 flex flex-col items-center justify-center p-12 rounded-3xl bg-black/40 backdrop-blur-xl border border-white/10 shadow-[0_0_50px_rgba(212,175,55,0.1)] transition-all duration-700 ease-out transform hover:scale-105">
                {/* Logo / Brand */}
                <div className="relative w-24 h-24 mb-6 flex items-center justify-center">
                    <div className="absolute inset-0 rounded-full border border-white/20 animate-[spin_4s_linear_infinite]" />
                    <div className="absolute inset-2 rounded-full border border-yellow-500/30 animate-[spin_3s_linear_infinite_reverse]" />
                    <div className="absolute inset-x-4 inset-y-4 rounded-full bg-gradient-to-tr from-yellow-600 to-orange-400 opacity-20 blur-md animate-pulse" />
                    <span className="text-4xl font-black tracking-tighter text-transparent bg-clip-text bg-gradient-to-b from-white to-yellow-500/50">G</span>
                </div>

                {/* Title */}
                <h1 className="flex flex-col items-center gap-1 mb-8">
                    <span className="text-3xl font-black tracking-[0.2em] uppercase text-white drop-shadow-[0_0_10px_rgba(255,255,255,0.5)]">Gravity</span>
                    <span className="text-xs font-bold tracking-[0.3em] uppercase text-yellow-500/80">Asset Manager U</span>
                </h1>

                {/* Progress section */}
                <div className="w-64 flex flex-col items-center gap-4">
                    {/* Progress bar */}
                    <div className="w-full h-1 bg-white/10 rounded-full overflow-hidden relative">
                        <div
                            className="h-full bg-gradient-to-r from-orange-500 to-yellow-400 transition-all duration-500 ease-out"
                            style={{
                                width: `${Math.min((attempt / 8) * 100, 95)}%`,
                            }}
                        />
                    </div>

                    {/* Status text */}
                    <p className="text-[10px] font-mono uppercase tracking-widest text-white/50 h-4 text-center animate-pulse" key={status}>
                        {status}
                    </p>
                </div>
            </div>
        </div>
    );
}
