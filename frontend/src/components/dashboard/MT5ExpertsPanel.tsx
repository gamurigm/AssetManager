"use client";

import React, { useEffect, useState } from "react";
import {
    Activity,
    Bot,
    CheckCircle2,
    KeyRound,
    Link,
    RefreshCw,
    ShieldAlert,
    ShieldCheck,
    Power,
    TerminalSquare,
} from "lucide-react";

const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8282";

interface MT5Status {
    connected: boolean;
    package_available: boolean;
    execution_mode: "disabled" | "paper" | "live";
    live_trading_enabled: boolean;
    live_armed: boolean;
    live_armed_until_epoch: number | null;
    gateway_token_configured: boolean;
    terminal_path: string;
    terminal: null | {
        name: string | null;
        build: number | null;
        connected: boolean | null;
        trade_allowed: boolean | null;
        tradeapi_disabled: boolean | null;
    };
    account: null | {
        login_masked: string | null;
        server: string | null;
        currency: string | null;
        trade_mode: string | null;
        balance: number | null;
        equity: number | null;
        margin_free: number | null;
        trade_allowed: boolean | null;
        trade_expert: boolean | null;
    };
    allowed_symbols: string[];
    allowed_experts: string[];
    limits: null | {
        max_open_positions: number;
        max_pending_orders: number;
        max_total_volume: number;
        max_symbol_volume: number;
        max_aggregate_risk_pct: number;
        max_orders_per_minute: number;
        max_orders_per_day: number;
    };
    last_error: string | null;
    kill_switch: {
        active: boolean;
        reason: string | null;
        updated_at: string | null;
    };
}

interface MT5OrderJournalEntry {
    signal_id: string;
    expert_id: string;
    symbol: string;
    side: string;
    volume: number;
    execution_mode: string;
    state: string;
    created_at: string;
}

function money(value: number | null | undefined, currency?: string | null) {
    if (value == null) return "—";
    return new Intl.NumberFormat("es-EC", {
        style: "currency",
        currency: currency || "USD",
        maximumFractionDigits: 2,
    }).format(value);
}

export default function MT5ExpertsPanel() {
    const [status, setStatus] = useState<MT5Status | null>(null);
    const [gatewayToken, setGatewayToken] = useState("");
    const [orders, setOrders] = useState<MT5OrderJournalEntry[]>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [reconciliationMessage, setReconciliationMessage] = useState<string | null>(null);

    useEffect(() => {
        let active = true;
        const refresh = async () => {
            try {
                const response = await fetch(`${API_BASE}/api/v1/trading/mt5/status`, {
                    headers: gatewayToken ? { "X-MT5-Gateway-Token": gatewayToken } : undefined,
                    cache: "no-store",
                });
                if (!response.ok) throw new Error("No fue posible leer el estado de MT5");
                const payload: MT5Status = await response.json();
                if (active) setStatus(payload);
            } catch (requestError) {
                if (active) setError(requestError instanceof Error ? requestError.message : "Error de red");
            }
        };
        void refresh();
        const timer = window.setInterval(refresh, 5000);
        return () => {
            active = false;
            window.clearInterval(timer);
        };
    }, [gatewayToken]);

    const authenticatedFetch = async (path: string, init?: RequestInit) => {
        if (!gatewayToken) throw new Error("Ingresa el token del gateway para esta sesión");
        return fetch(`${API_BASE}${path}`, {
            ...init,
            headers: {
                "X-MT5-Gateway-Token": gatewayToken,
                ...(init?.headers ?? {}),
            },
            cache: "no-store",
        });
    };

    const connect = async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await authenticatedFetch("/api/v1/trading/mt5/connect", { method: "POST" });
            const payload = await response.json();
            if (!response.ok) throw new Error(payload.detail || "MT5 rechazó la conexión");
            setStatus(payload as MT5Status);
        } catch (requestError) {
            setError(requestError instanceof Error ? requestError.message : "Error de conexión");
        } finally {
            setLoading(false);
        }
    };

    const loadOrders = async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await authenticatedFetch("/api/v1/trading/mt5/experts/orders?limit=30");
            const payload = await response.json();
            if (!response.ok) throw new Error(payload.detail || "No fue posible cargar las señales");
            setOrders((payload.orders ?? []) as MT5OrderJournalEntry[]);
        } catch (requestError) {
            setError(requestError instanceof Error ? requestError.message : "Error al cargar señales");
        } finally {
            setLoading(false);
        }
    };

    const reconcileOrders = async () => {
        setLoading(true);
        setError(null);
        setReconciliationMessage(null);
        try {
            const response = await authenticatedFetch("/api/v1/trading/mt5/reconcile", {
                method: "POST",
            });
            const payload = await response.json();
            if (!response.ok) throw new Error(payload.detail || "No fue posible reconciliar MT5");
            setReconciliationMessage(
                String(Number(payload.checked ?? 0)) +
                " revisadas · " +
                String(Number(payload.changed ?? 0)) +
                " actualizadas",
            );
            await loadOrders();
        } catch (requestError) {
            setError(requestError instanceof Error ? requestError.message : "Error de reconciliación");
            setLoading(false);
        }
    };

    const setKillSwitch = async (active: boolean) => {
        const confirmed = window.confirm(
            active
                ? "¿Activar la parada de emergencia? Ningún Expert podrá enviar órdenes."
                : "¿Restablecer la ejecución? Las demás protecciones seguirán activas.",
        );
        if (!confirmed) return;
        setLoading(true);
        setError(null);
        try {
            const response = await authenticatedFetch(
                active
                    ? "/api/v1/trading/mt5/kill-switch"
                    : "/api/v1/trading/mt5/kill-switch/reset",
                {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(
                        active
                            ? { reason: "Parada manual solicitada desde el panel MT5" }
                            : { confirm: "RESET" },
                    ),
                },
            );
            const payload = await response.json();
            if (!response.ok) throw new Error(payload.detail || "No fue posible cambiar la parada de emergencia");
            setStatus((current) => current ? { ...current, kill_switch: payload } : current);
        } catch (requestError) {
            setError(requestError instanceof Error ? requestError.message : "Error del kill switch");
        } finally {
            setLoading(false);
        }
    };

    const connected = status?.connected ?? false;
    const mode = status?.execution_mode ?? "disabled";
    const terminalReady = Boolean(
        connected &&
        status?.gateway_token_configured &&
        status.allowed_experts.length &&
        status.allowed_symbols.length &&
        status.account?.trade_allowed &&
        status.account?.trade_expert &&
        status.terminal?.trade_allowed &&
        status.terminal?.tradeapi_disabled === false
    );
    const readyForExecution = Boolean(
        terminalReady &&
        !status?.kill_switch?.active &&
        (
            (mode === "paper" && ["demo", "contest"].includes(status?.account?.trade_mode ?? "")) ||
            (mode === "live" && status?.account?.trade_mode === "real" && status.live_armed)
        )
    );

    return (
        <section className="flex-1 overflow-y-auto bg-background" aria-label="Monitor de Expert Advisors de MetaTrader 5">
            <header className="sticky top-0 z-10 border-b border-border/20 bg-background/95 px-5 py-4 backdrop-blur-xl">
                <div className="flex items-center justify-between gap-3">
                    <div className="flex items-center gap-3">
                        <div className={`flex h-10 w-10 items-center justify-center rounded-xl border ${connected ? "border-emerald-500/30 bg-emerald-500/10 text-emerald-400" : "border-amber-500/30 bg-amber-500/10 text-amber-400"}`}>
                            <Bot size={20} aria-hidden="true" />
                        </div>
                        <div>
                            <h2 className="text-sm font-bold text-foreground">MT5 Expert Gateway</h2>
                            <p className="mt-0.5 text-xs text-muted">
                                {connected ? "Terminal conectado" : "Terminal desconectado"} · modo {mode}
                            </p>
                        </div>
                    </div>
                    <span className={`rounded-full border px-2.5 py-1 text-xs font-semibold ${mode === "live" ? "border-red/30 bg-red/10 text-red" : mode === "paper" ? "border-emerald-500/30 bg-emerald-500/10 text-emerald-400" : "border-border/40 bg-card text-muted"}`}>
                        {mode.toUpperCase()}
                    </span>
                </div>
            </header>

            <div className="space-y-5 p-5">
                <div
                    className={`flex items-center justify-between gap-4 rounded-xl border p-4 ${status?.kill_switch?.active ? "border-red/40 bg-red/10" : "border-emerald-500/30 bg-emerald-500/10"}`}
                    role="status"
                    aria-live="polite"
                >
                    <div className="flex min-w-0 gap-3">
                        <Power className={`mt-0.5 shrink-0 ${status?.kill_switch?.active ? "text-red" : "text-emerald-400"}`} size={20} aria-hidden="true" />
                        <div className="min-w-0">
                            <h3 className="text-sm font-semibold">
                                {status?.kill_switch?.active ? "Parada de emergencia activa" : "Kill switch disponible"}
                            </h3>
                            <p className="mt-1 truncate text-xs text-muted">
                                {status?.kill_switch?.active
                                    ? status.kill_switch.reason || "La ejecución está bloqueada."
                                    : "Bloqueo duradero e inmediato para todos los Experts."}
                            </p>
                        </div>
                    </div>
                    <button
                        type="button"
                        onClick={() => void setKillSwitch(!status?.kill_switch?.active)}
                        disabled={loading || !gatewayToken || !status}
                        className={`shrink-0 rounded-lg border px-3 py-2 text-xs font-bold transition disabled:cursor-not-allowed disabled:opacity-40 ${status?.kill_switch?.active ? "border-emerald-500/40 text-emerald-400 hover:bg-emerald-500/10" : "border-red/40 text-red hover:bg-red/10"}`}
                    >
                        {status?.kill_switch?.active ? "Restablecer" : "Detener todo"}
                    </button>
                </div>

                {mode === "live" && (
                    <div className="flex gap-3 rounded-xl border border-red/30 bg-red/10 p-4 text-sm text-red" role="alert">
                        <ShieldAlert className="shrink-0" size={20} aria-hidden="true" />
                        <p>
                            {status?.live_armed
                                ? "Live armado hasta " + new Date((status.live_armed_until_epoch ?? 0) * 1000).toLocaleString("es-EC") + "."
                                : "Live desarmado o vencido."}
                            {" "}Cada orden mantiene allowlist, límites agregados y confirmación del EA.
                        </p>
                    </div>
                )}

                <div className="rounded-2xl border border-border/30 bg-card/50 p-4">
                    <label htmlFor="mt5-gateway-token" className="flex items-center gap-2 text-sm font-semibold text-foreground">
                        <KeyRound size={16} className="text-accent" aria-hidden="true" />
                        Token del gateway
                    </label>
                    <p className="mt-1 text-xs leading-5 text-muted">Solo vive en esta sesión del navegador; no se guarda localmente.</p>
                    <div className="mt-3 flex gap-2">
                        <input
                            id="mt5-gateway-token"
                            type="password"
                            autoComplete="off"
                            value={gatewayToken}
                            onChange={(event) => setGatewayToken(event.target.value)}
                            placeholder="X-MT5-Gateway-Token"
                            className="min-w-0 flex-1 rounded-xl border border-border/40 bg-background px-3 py-2.5 text-sm outline-none focus:border-accent focus:ring-2 focus:ring-accent/20"
                        />
                        <button
                            type="button"
                            onClick={connect}
                            disabled={loading || !gatewayToken}
                            className="inline-flex min-h-11 items-center gap-2 rounded-xl bg-accent px-4 text-sm font-semibold text-white disabled:cursor-not-allowed disabled:opacity-40"
                        >
                            {loading ? <RefreshCw size={16} className="animate-spin" /> : <Link size={16} />}
                            Conectar
                        </button>
                    </div>
                </div>

                {error && (
                    <div className="rounded-xl border border-red/30 bg-red/10 p-3 text-sm text-red" role="alert">
                        {error}
                    </div>
                )}

                <div className="grid grid-cols-2 gap-3">
                    <StatusCard label="Paquete Python" value={status?.package_available ? "Disponible" : "Falta instalar"} ok={Boolean(status?.package_available)} />
                    <StatusCard label="Cuenta" value={status?.account?.trade_mode ?? "Sin conexión"} ok={Boolean(status?.account)} />
                    <StatusCard label="Experts permitidos" value={String(status?.allowed_experts.length ?? 0)} ok={Boolean(status?.allowed_experts.length)} />
                    <StatusCard label="Símbolos permitidos" value={String(status?.allowed_symbols.length ?? 0)} ok={Boolean(status?.allowed_symbols.length)} />
                </div>

                {status?.account && (
                    <div className="rounded-2xl border border-border/30 bg-card/50 p-4">
                        <div className="mb-3 flex items-center gap-2">
                            <TerminalSquare size={17} className="text-emerald-400" aria-hidden="true" />
                            <h3 className="text-sm font-semibold">Cuenta {status.account.login_masked}</h3>
                        </div>
                        <dl className="grid grid-cols-2 gap-x-4 gap-y-3 text-xs">
                            <Metric label="Servidor" value={status.account.server ?? "—"} />
                            <Metric label="Moneda" value={status.account.currency ?? "—"} />
                            <Metric label="Balance" value={money(status.account.balance, status.account.currency)} />
                            <Metric label="Equity" value={money(status.account.equity, status.account.currency)} />
                            <Metric label="Margen libre" value={money(status.account.margin_free, status.account.currency)} />
                            <Metric label="Build" value={String(status.terminal?.build ?? "—")} />
                        </dl>
                    </div>
                )}

                <div className={`flex gap-3 rounded-xl border p-4 ${readyForExecution ? "border-emerald-500/30 bg-emerald-500/10" : "border-amber-500/30 bg-amber-500/10"}`}>
                    {readyForExecution ? <ShieldCheck size={20} className="shrink-0 text-emerald-400" /> : <ShieldAlert size={20} className="shrink-0 text-amber-400" />}
                    <div>
                        <h3 className="text-sm font-semibold">{readyForExecution ? (mode === "live" ? "Preparado para ejecución live" : "Preparado para forward test demo") : "Ejecución bloqueada"}</h3>
                        <p className="mt-1 text-xs leading-5 text-muted">
                            El gateway comprueba tick, spread, margen, stop, exposición total, frecuencia de órdenes e idempotencia.
                        </p>
                    </div>
                </div>

                {status?.limits && (
                    <div className="rounded-2xl border border-border/30 bg-card/50 p-4">
                        <h3 className="text-sm font-semibold">Límites agregados</h3>
                        <dl className="mt-3 grid grid-cols-2 gap-x-4 gap-y-3 text-xs">
                            <Metric label="Posiciones" value={String(status.limits.max_open_positions)} />
                            <Metric label="Órdenes/min" value={String(status.limits.max_orders_per_minute)} />
                            <Metric label="Órdenes/día" value={String(status.limits.max_orders_per_day)} />
                            <Metric label="Volumen total" value={String(status.limits.max_total_volume)} />
                            <Metric label="Riesgo por stops" value={String(status.limits.max_aggregate_risk_pct) + "%"} />
                        </dl>
                    </div>
                )}

                <div className="rounded-2xl border border-border/30 bg-card/50">
                    <div className="flex items-center justify-between border-b border-border/20 p-4">
                        <div className="flex items-center gap-2">
                            <Activity size={17} className="text-purple-400" aria-hidden="true" />
                            <h3 className="text-sm font-semibold">Journal de señales</h3>
                        </div>
                        <div className="flex items-center gap-2">
                            <button
                                type="button"
                                onClick={reconcileOrders}
                                disabled={loading || !gatewayToken || !connected}
                                className="rounded-lg border border-border/40 px-3 py-2 text-xs font-semibold text-muted transition hover:text-foreground disabled:opacity-40"
                            >
                                Reconciliar
                            </button>
                            <button
                                type="button"
                                onClick={loadOrders}
                                disabled={loading || !gatewayToken}
                                className="rounded-lg border border-border/40 p-2 text-muted transition hover:text-foreground disabled:opacity-40"
                                aria-label="Actualizar journal de señales"
                            >
                                <RefreshCw size={16} className={loading ? "animate-spin" : ""} />
                            </button>
                        </div>
                    </div>
                    {reconciliationMessage && (
                        <p className="border-b border-border/20 px-4 py-2 text-xs text-emerald-400">
                            {reconciliationMessage}
                        </p>
                    )}
                    <div className="max-h-72 overflow-y-auto p-3">
                        {orders.length === 0 ? (
                            <p className="py-8 text-center text-xs text-muted">Sin ejecuciones registradas.</p>
                        ) : orders.map((order) => (
                            <div key={order.signal_id} className="mb-2 rounded-xl border border-border/20 bg-background/60 p-3 last:mb-0">
                                <div className="flex items-center justify-between gap-2">
                                    <span className="text-sm font-semibold">{order.symbol} · {order.side}</span>
                                    <span className={`rounded-full px-2 py-0.5 text-xs ${order.state === "filled" ? "bg-emerald-500/10 text-emerald-400" : order.state === "rejected" ? "bg-red/10 text-red" : "bg-amber-500/10 text-amber-400"}`}>
                                        {order.state}
                                    </span>
                                </div>
                                <p className="mt-1 truncate font-mono text-xs text-muted">{order.expert_id} · {order.volume} lot · {order.signal_id}</p>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </section>
    );
}

function StatusCard({ label, value, ok }: { label: string; value: string; ok: boolean }) {
    return (
        <div className="rounded-xl border border-border/30 bg-card/50 p-3">
            <div className="flex items-center gap-2 text-xs text-muted">
                {ok ? <CheckCircle2 size={14} className="text-emerald-400" /> : <ShieldAlert size={14} className="text-amber-400" />}
                {label}
            </div>
            <p className="mt-2 truncate text-sm font-semibold capitalize text-foreground">{value}</p>
        </div>
    );
}

function Metric({ label, value }: { label: string; value: string }) {
    return (
        <div>
            <dt className="text-muted">{label}</dt>
            <dd className="mt-1 truncate font-mono font-semibold text-foreground">{value}</dd>
        </div>
    );
}
