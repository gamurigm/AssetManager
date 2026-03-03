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

    const [particles, setParticles] = useState<{ left: string; top: string; delay: string; duration: string }[]>([]);

    useEffect(() => {
        // Generate random values only on the client after mounting to avoid hydration mismatch
        setParticles(
            Array.from({ length: 20 }).map(() => ({
                left: `${Math.random() * 100}%`,
                top: `${Math.random() * 100}%`,
                delay: `${Math.random() * 5}s`,
                duration: `${3 + Math.random() * 4}s`,
            }))
        );
    }, []);

    if (ready) {
        return <div className="animate-gate-reveal">{children}</div>;
    }

    return (
        <div className="gate-container">
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
                            animationDelay: p.delay,
                            animationDuration: p.duration,
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
