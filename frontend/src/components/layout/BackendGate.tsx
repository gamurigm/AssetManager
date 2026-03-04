"use client";

import { useEffect, useState, useCallback } from "react";

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
    const [phase, setPhase] = useState(0);

    const statusMessages = [
        "Initializing systems...",
        "Connecting to backend services...",
        "Loading market data engine...",
        "Synchronizing DuckDB schema...",
        "Warming up AI agents...",
        "Establishing provider connections...",
        "Calibrating risk models...",
        "Almost ready...",
    ];

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

            // Cycle through status messages
            const msgIndex = Math.min(
                Math.floor(retryCount / 3),
                statusMessages.length - 1
            );
            setStatus(statusMessages[msgIndex]);
            setPhase(msgIndex);

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

    const [particles, setParticles] = useState<{ left: string; top: string; delay: string; duration: string; size: number }[]>([]);
    const [ripples, setRipples] = useState<{ left: string; top: string; delay: string; duration: string }[]>([]);

    useEffect(() => {
        // Small dots only — lots of them
        setParticles(
            Array.from({ length: 90 }).map(() => ({
                left: `${Math.random() * 100}%`,
                top: `${Math.random() * 100}%`,
                delay: `${Math.random() * 8}s`,
                duration: `${2.5 + Math.random() * 5}s`,
                size: 1 + Math.random() * 3, // 1–4px only
            }))
        );
        // Ripple waves that expand outward
        setRipples(
            Array.from({ length: 6 }).map(() => ({
                left: `${15 + Math.random() * 70}%`,
                top: `${15 + Math.random() * 70}%`,
                delay: `${Math.random() * 10}s`,
                duration: `${4 + Math.random() * 4}s`,
            }))
        );
    }, []);

    if (ready) {
        return <div className="animate-gate-reveal">{children}</div>;
    }

    return (
        <div className="gate-container">
            {/* Background image — cinematic dark overlay */}
            <div
                className="absolute inset-0 bg-cover bg-center bg-no-repeat"
                style={{
                    backgroundImage: "url('/fondo-bg1.jpg')",
                    opacity: 1,
                    filter: 'saturate(1.4) contrast(1.15) brightness(0.75)'
                }}
            />
            {/* Rich vignette — dark edges, slightly open center */}
            <div className="absolute inset-0 pointer-events-none" style={{ background: 'radial-gradient(ellipse 70% 60% at 50% 50%, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.6) 100%)' }} />
            {/* Top & bottom hard black bars */}
            <div className="absolute inset-x-0 top-0 h-28 bg-gradient-to-b from-black to-transparent pointer-events-none" />
            <div className="absolute inset-x-0 bottom-0 h-28 bg-gradient-to-t from-black to-transparent pointer-events-none" />

            {/* Animated background grid */}
            <div className="gate-grid" />

            {/* Floating particles (hydrated safely) */}
            <div className="gate-particles">
                {particles.map((p, i) => (
                    <div
                        key={i}
                        className="gate-particle"
                        style={{
                            left: p.left,
                            top: p.top,
                            width: `${p.size}px`,
                            height: `${p.size}px`,
                            animationDelay: p.delay,
                            animationDuration: p.duration,
                            boxShadow: `0 0 ${p.size * 2}px rgba(255,248,160,0.75)`,
                        }}
                    />
                ))}
            </div>

            {/* Ripple waves */}
            <div className="gate-particles">
                {ripples.map((r, i) => (
                    <div
                        key={`ripple-${i}`}
                        className="gate-ripple"
                        style={{
                            left: r.left,
                            top: r.top,
                            animationDelay: r.delay,
                            animationDuration: r.duration,
                        }}
                    />
                ))}
            </div>

            {/* Central content */}
            <div className="gate-content">
                {/* Logo / Brand */}
                <div className="gate-logo-ring">
                    <div className="gate-ring gate-ring-outer" />
                    <div className="gate-ring gate-ring-middle" />
                    <div className="gate-ring gate-ring-inner" />
                    <div className="gate-logo-core">
                        <span className="gate-logo-text">M</span>
                    </div>
                </div>

                {/* Title */}
                <h1 className="gate-title">
                    <span className="gate-title-main">MMAM</span>
                    <span className="gate-title-sub">Intelligence Core</span>
                </h1>

                {/* Progress section */}
                <div className="gate-progress-section">
                    {/* Progress bar */}
                    <div className="gate-progress-track">
                        <div
                            className="gate-progress-fill"
                            style={{
                                width: `${Math.min((attempt / 8) * 100, 95)}%`,
                            }}
                        />
                        <div className="gate-progress-glow" />
                    </div>

                    {/* Status text */}
                    <p className="gate-status" key={status}>
                        {status}
                    </p>

                    {/* Phase indicators */}
                    <div className="gate-phases">
                        {statusMessages.slice(0, 5).map((_, i) => (
                            <div
                                key={i}
                                className={`gate-phase-dot ${i <= phase ? "gate-phase-active" : ""}`}
                            />
                        ))}
                    </div>
                </div>

                {/* Version / footer */}
                <p className="gate-footer">
                    Murillo Medina Asset Management • v4.0
                </p>
            </div>
        </div>
    );
}
