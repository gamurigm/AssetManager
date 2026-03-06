"use client";

import { useEffect, useState, useCallback, useRef } from "react";
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
    const [progressOverride, setProgressOverride] = useState<number | null>(null);
    const mountTime = useRef(Date.now());

    const checkBackend = useCallback(async () => {
        try {
            const res = await fetch(`${BACKEND_URL}/`, {
                method: "GET",
                signal: AbortSignal.timeout(3000),
            });
            if (res.ok) {
                setStatus("Systems online. Appreciating 3D aesthetics...");

                // Ensure at least 4 seconds of loading screen (User requested 4s)
                const elapsed = Date.now() - mountTime.current;
                const remaining = Math.max(0, 4000 - elapsed);
                setProgressOverride(100);

                setTimeout(() => {
                    setStatus("Launching terminal...");
                    setTimeout(() => setReady(true), 400);
                }, remaining);
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

            {/* Central Glassmorphism Card */}
            <div className="relative z-10 flex flex-col items-center gap-5 px-10 py-8 rounded-2xl bg-black/25 backdrop-blur-xl border border-white/10 shadow-[0_0_60px_rgba(212,175,55,0.1),0_0_150px_rgba(212,175,55,0.04)] transition-all duration-700 ease-out">

                {/* Logo & Spinning Rings */}
                <div className="relative w-16 h-16 flex items-center justify-center">
                    <div className="absolute inset-0 rounded-full border border-white/15 animate-[spin_6s_linear_infinite]" />
                    <div className="absolute inset-1.5 rounded-full border border-yellow-500/25 animate-[spin_4s_linear_infinite_reverse]" />
                    <div className="absolute inset-3 rounded-full border border-yellow-400/20 animate-[spin_3s_linear_infinite]" />
                    <div className="absolute inset-3.5 rounded-full bg-gradient-to-tr from-yellow-600 to-orange-400 opacity-15 blur-sm animate-pulse" />
                    <span className="text-2xl font-black tracking-tighter text-transparent bg-clip-text bg-gradient-to-b from-white to-yellow-500/60 drop-shadow-[0_0_15px_rgba(212,175,55,0.4)]">G</span>
                </div>

                {/* Brand */}
                <div className="flex flex-col items-center gap-0.5">
                    <span className="text-lg font-black tracking-[0.2em] uppercase text-white drop-shadow-[0_0_10px_rgba(255,255,255,0.3)]">Gravity</span>
                    <span className="text-[8px] font-bold tracking-[0.3em] uppercase text-yellow-500/70">Asset Manager</span>
                </div>

                {/* Progress section */}
                <div className="w-48 flex flex-col items-center gap-2">
                    <p className="text-[8px] font-mono uppercase tracking-widest text-white/50 h-3 text-center animate-pulse" key={status}>
                        {status}
                    </p>
                    <div className="w-full h-[2px] bg-white/10 rounded-full overflow-hidden">
                        <div
                            className="h-full bg-gradient-to-r from-orange-500 via-yellow-400 to-amber-300 transition-all duration-1000 ease-out rounded-full shadow-[0_0_8px_rgba(251,191,36,0.5)]"
                            style={{
                                width: `${progressOverride !== null ? progressOverride : Math.min((attempt / 8) * 100, 95)}%`,
                            }}
                        />
                    </div>
                </div>
            </div>
        </div>
    );
}
