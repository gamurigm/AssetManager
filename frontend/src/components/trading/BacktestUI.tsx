"use client";

import React from "react";
import { LucideIcon } from "lucide-react";

/**
 * ── METRIC CARD ──────────────────────────────────────────────────────────────
 * Consistent KPI display with theme-aware colors and hover effects.
 */
interface MetricCardProps {
  label: string;
  value: string | number;
  subValue?: string;
  trend?: "up" | "down" | "neutral";
  icon?: LucideIcon;
  variant?: "cyan" | "rose" | "amber" | "emerald" | "default";
}

export const MetricCard = ({ label, value, subValue, trend, icon: Icon, variant = "default" }: MetricCardProps) => {
  const variantMap = {
    cyan: "border-cyan-500/20 bg-cyan-500/5 text-cyan-200",
    rose: "border-red/20 bg-red/5 text-red",
    amber: "border-amber-500/20 bg-amber-500/5 text-amber-200",
    emerald: "border-green/20 bg-green/5 text-green",
    default: "border-border bg-card",
  };

  const trendColor = trend === "up" ? "text-green" : trend === "down" ? "text-red" : "text-muted";

  return (
    <div className={`rounded-2xl border ${variantMap[variant]} p-4 flex flex-col justify-between transition-all hover:border-accent/40 hover:shadow-lg`}>
      <div className="flex items-center justify-between mb-2">
        <span className="text-[10px] font-black uppercase tracking-widest text-muted">{label}</span>
        {Icon && <Icon size={14} className="text-muted/60" />}
      </div>
      <div className="flex items-baseline gap-2">
        <span className={`text-xl font-black ${variant === "default" ? "text-foreground" : ""}`}>{value}</span>
        {subValue && <span className={`text-[10px] font-bold ${trendColor}`}>{subValue}</span>}
      </div>
    </div>
  );
};

/**
 * ── BACKTEST PANEL CONTAINER ───────────────────────────────────────────────
 * Main container with glassmorphism or deep-dark-frosted look.
 */
interface BacktestPanelProps {
  title: string;
  subtitle?: string;
  headerIcon?: LucideIcon;
  headerRight?: React.ReactNode;
  children: React.ReactNode;
  variant?: "cyan" | "purple" | "default";
}

export const BacktestPanel = ({ title, subtitle, headerIcon: Icon, headerRight, children, variant = "default" }: BacktestPanelProps) => {
  const variantMap = {
    cyan: "border-cyan-500/20 bg-[radial-gradient(circle_at_top_left,rgba(34,211,238,0.08),transparent_40%),linear-gradient(180deg,rgba(0,0,0,0.6),rgba(0,0,0,0.3))]",
    purple: "border-purple-500/20 bg-[radial-gradient(circle_at_top_left,rgba(168,85,247,0.08),transparent_40%),linear-gradient(180deg,rgba(0,0,0,0.6),rgba(0,0,0,0.3))]",
    default: "border-border bg-card",
  };

  return (
    <div className={`rounded-3xl border ${variantMap[variant]} backdrop-blur-xl overflow-hidden shadow-2xl transition-all`}>
      <div className="px-6 py-5 border-b border-white/5 flex items-start justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            {Icon && <Icon size={16} className={`text-muted ${variant === 'cyan' ? 'text-cyan-300' : variant === 'purple' ? 'text-purple-300' : ''}`} />}
            <span className={`text-[10px] font-black uppercase tracking-[0.3em] ${variant === 'cyan' ? 'text-cyan-200/80' : 'text-muted'}`}>{title}</span>
          </div>
          {subtitle && <h3 className="text-lg font-black tracking-tight text-foreground mt-1">{subtitle}</h3>}
        </div>
        {headerRight && <div className="shrink-0">{headerRight}</div>}
      </div>
      <div className="p-6">{children}</div>
    </div>
  );
};

/**
 * ── DATA SECTION ──────────────────────────────────────────────────────────
 * Sub-panels used within a backtest layout to group results/settings.
 */
interface DataSectionProps {
  title: string;
  children: React.ReactNode;
}

export const DataSection = ({ title, children }: DataSectionProps) => (
  <div className="space-y-4">
    <div className="flex items-center gap-2">
      <div className="h-px flex-1 bg-border/40" />
      <span className="text-[10px] font-black uppercase tracking-widest text-muted/60">{title}</span>
      <div className="h-px flex-1 bg-border/40" />
    </div>
    {children}
  </div>
);
