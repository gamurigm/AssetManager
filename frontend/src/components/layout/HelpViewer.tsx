"use client"

import { useState, useEffect, useRef } from "react";
import { X, HelpCircle, BookOpen, ChevronRight, Search, LayoutDashboard, PieChart, ArrowLeftRight, Briefcase, List, Info, Settings, ShieldCheck, Terminal as TerminalIcon, GraduationCap, Code, Zap, Play, Microscope, TrendingUp, BarChart, Activity, Copy, Check, Database } from "lucide-react";
import ReactMarkdown from "react-markdown";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { atomDark } from "react-syntax-highlighter/dist/esm/styles/prism";
import "katex/dist/katex.min.css";

interface HelpSection {
    id: string;
    title: string;
    icon: any;
    content: string;
    category: 'docs' | 'education';
}

const HELP_DATA: HelpSection[] = [
    // --- DOCS CATEGORY ---
    {
        id: "intro",
        title: "System Architecture",
        icon: LayoutDashboard,
        category: 'docs',
        content: `
# System Intelligence Architecture
The MMAM platform is a distributed quantitative ecosystem designed for high-frequency analysis and robust execution.

### High-Throughput Backbone
* **Microservices Layer**: Asynchronous service mesh handling market data, portfolio accounting, and AI reasoning.
* **Unified Data Model**: Standardized data structures for cross-asset analysis (Equities, Crypto, FX, Options).

### Performance Metrics
The system is optimized for **Low Latency** ($L < 100ms$) and **High Availability** ($99.99\%$).
`
    },
    {
        id: "broker-integration",
        title: "Broker & Connectivity",
        icon: ShieldCheck,
        category: 'docs',
        content: `
# Broker Connectivity & Execution
The platform bridges the gap between analysis and live markets through enterprise-grade API integrations.

### Interactive Brokers (IBKR)
* **TWS/Gateway Integration**: Native connection using the IB API for deep liquidity access.
* **SmartRouting℠**: Automated routing to the venue with the best price and likelihood of execution.

### cTrader Integration
* **FIX Protocol**: High-speed execution through the FIX (Financial Information eXchange) gateway for FX and CFDs.
* **Quoting Engine**: Real-time bid/ask streaming with sub-millisecond price updates.
`
    },
    {
        id: "data-engine",
        title: "Alpha Data Engine",
        icon: Database,
        category: 'docs',
        content: `
# Alpha Data Engine
Our data persistence layer is engineered for rapid backtesting and real-time visualization.

### Storage Architecture
* **DuckDB Core**: Utilization of an in-process analytical database for columnar storage of tick and candle data.
* **Parquet Integration**: Efficient data serialization for long-term historical storage.

### Real-Time Streaming
* **WebSockets (WSS)**: Low-latency push notifications for price changes and order state updates.
* **Event-Driven Buffering**: Intelligent memory management to prevent data loss during high-volatility spikes.
`
    },
    {
        id: "backtest-lab-docs",
        title: "Simulation & Backtest",
        icon: Activity,
        category: 'docs',
        content: `
# Simulation & Backtest Lab
The Backtest Lab allows for rigorous validation of alpha hypotheses before capital allocation.

### High-Fidelity Simulator
* **Slippage Models**: Realistic execution modeling based on average daily volume (ADV) and bid-ask spreads.
* **Latency Simulation**: Configurable delay parameters to test strategy robustness against network latency.

### Reporting Engine
Comprehensive KPIs including **Max Drawdown**, **Sharpe/Sortino**, and **Equity Curve Analysis**.
`
    },
    // --- EDUCATION CATEGORY (DETAILED CURRICULUM) ---
    {
        id: "step-1-fundamentals",
        title: "1. Quant Fundamentals",
        icon: TrendingUp,
        category: 'education',
        content: `
# Step 1: Quantitative Fundamentals
Understanding returns and volatility measurement is the bedrock of quantitative modeling.

### Logarithmic Returns
We prefer **Log Returns** ($r_t$) over arithmetic returns for their time-additivity and statistical properties.
$$r_t = \\ln\\left(\\frac{S_t}{S_{t-1}}\\right)$$

### Annualized Volatility
To normalize risk across time, we scale the standard deviation by the square root of trading days:
$$\\sigma_{\\text{ann}} = \\sigma_{\\text{daily}} \\times \\sqrt{252}$$

### Risk-Adjusted Ratios
The **Sharpe Ratio** defines the efficiency of the capital allocation:
$$\\text{Sharpe} = \\frac{\\mathbb{E}[R_p - R_f]}{\\sigma_p}$$
`
    },
    {
        id: "step-2-stochastic",
        title: "2. Stochastic Processes",
        icon: Activity,
        category: 'education',
        content: `
# Step 2: Stochastic Calculus
Asset prices move according to random continuous-time processes.

### Geometric Brownian Motion (GBM)
The standard SDE used to model asset prices ensures that price $S_t$ stays positive:
$$dS_t = \\mu S_t dt + \\sigma S_t dW_t$$

### Itô's Lemma 
The fundamental theorem of stochastic calculus. For a function $f(S, t)$, its differential $df$ is:
$$df = \\left( \\frac{\\partial f}{\\partial t} + \\mu S \\frac{\\partial f}{\\partial S} + \\frac{1}{2} \\sigma^2 S^2 \\frac{\\partial^2 f}{\\partial S^2} \\right) dt + \\sigma S \\frac{\\partial f}{\\partial S} dW_t$$

\`\`\`python
# Simple GBM Path Simulation
import numpy as np

def simulate_gbm(S0, mu, sigma, T, dt):
    N = int(T/dt)
    t = np.linspace(0, T, N)
    W = np.random.standard_normal(size=N)
    W = np.cumsum(W) * np.sqrt(dt)
    X = (mu - 0.5 * sigma**2) * t + sigma * W
    return S0 * np.exp(X)
\`\`\`
`
    },
    {
        id: "step-3-pricing",
        title: "3. Option Pricing & Greeks",
        icon: Zap,
        category: 'education',
        content: `
# Step 3: Option Pricing & Risk Sensitivity
Derivatives pricing relies on the principle of No-Arbitrage.

### The Black-Scholes PDE
$$ \\frac{\\partial V}{\\partial t} + \\frac{1}{2}\\sigma^2 S^2 \\frac{\\partial^2 V}{\\partial S^2} + rS \\frac{\\partial V}{\\partial S} - rV = 0 $$

### The Greeks (Partial Derivatives)
* **Delta ($\\Delta$)**: The Hedge Ratio.
$$ \\Delta = \\frac{\\partial V}{\\partial S} = N(d_1) $$
* **Gamma ($\\Gamma$)**: The acceleration of price sensitivity.
$$ \\Gamma = \\frac{\\partial^2 V}{\\partial S^2} = \\frac{N'(d_1)}{S\\sigma\\sqrt{T}} $$
* **Vega ($\\nu$)**: Sensitivity to the Volatility Surface.
$$ \\nu = \\frac{\\partial V}{\\partial \\sigma} = S\\sqrt{T}N'(d_1) $$
`
    },
    {
        id: "step-4-risk",
        title: "4. Risk & Money Mgmt",
        icon: ShieldCheck,
        category: 'education',
        content: `
# Step 4: Quantitative Risk Management
Controlling tail risk is vital for long-term solvency.

### Value at Risk (VaR)
The threshold loss that will not be exceeded with probability $\\alpha$:
$$ \\text{VaR}_{\\alpha} = \\inf \\{ L : P(Loss > L) \\le 1 - \\alpha \\} $$

### The Kelly Criterion
The optimal fraction of wealth to invest to maximize logarithmic growth:
$$ f^* = \\frac{\\mu - r}{\\sigma^2} $$

\`\`\`python
def kelly_criterion(mu, r, sigma):
    """Calculate optimal leverage f*"""
    return (mu - r) / (sigma ** 2)
\`\`\`
`
    },
    {
        id: "step-5-advanced",
        title: "5. Advanced Modeling",
        icon: Microscope,
        category: 'education',
        content: `
# Step 5: Advanced Volatility & Regimes

### Heston Stochastic Volatility
Captures the observation that volatility itself is a random, mean-reverting process:
$$ dS_t = \\mu S_t dt + \\sqrt{\\nu_t} S_t dW_{1,t} $$
$$ d\\nu_t = \\kappa(\\theta - \\nu_t)dt + \\xi\\sqrt{\\nu_t} dW_{2,t} $$

### Jump Diffusion (Merton)
Incorporates sudden discontinuities (news/shocks) into the standard GBM model:
$$ dS_t = (\\mu - \\lambda \\bar{J}) S_t dt + \\sigma S_t dW_t + S_t d\\left(\\sum_{i=1}^{N_t} (J_i - 1)\\right) $$
`
    }
];

const DEFAULT_PLAYGROUND_CONTENT = `
# Live Quant Notebook
Experiment with models and syntax here.

### Stochastic Differential Equation:
$$ dX_t = \\kappa(\\theta - X_t)dt + \\sigma dW_t $$

### Complex Derivative:
$$ \\frac{\\partial f}{\\partial t} + \\mathcal{A}f = 0 $$

### Code Snippet:
\`\`\`python
import math

class OptionPricer:
    def __init__(self, spot, strike, vol):
        self.S = spot
        self.K = strike
        self.sigma = vol
\`\`\`
`.trim();

export default function HelpViewer({ isOpen, onClose, mode = 'docs' }: { isOpen: boolean; onClose: () => void; mode?: 'docs' | 'education' }) {
    const [selectedTab, setSelectedTab] = useState<string>("intro");
    const [eduSubTab, setEduSubTab] = useState<'manual' | 'playground'>('manual');
    const [playgroundContent, setPlaygroundContent] = useState(DEFAULT_PLAYGROUND_CONTENT);
    const [searchQuery, setSearchQuery] = useState("");
    const [mounted, setMounted] = useState(false);
    const contentRef = useRef<HTMLDivElement>(null);
    const [toc, setToc] = useState<{ id: string, text: string, level: number }[]>([]);

    useEffect(() => {
        setMounted(true);
    }, []);

    const activeSection = HELP_DATA.find(s => s.id === selectedTab) || HELP_DATA[0];
    const filteredSections = HELP_DATA.filter(s =>
        s.category === mode && (
            s.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
            s.content.toLowerCase().includes(searchQuery.toLowerCase())
        )
    );

    useEffect(() => {
        if (mode === 'education') {
            setSelectedTab("step-1-fundamentals");
        } else {
            setSelectedTab("intro");
        }
    }, [mode]);

    // TOC Extraction
    useEffect(() => {
        if (isOpen && activeSection && eduSubTab === 'manual') {
            const headings: { id: string, text: string, level: number }[] = [];
            const lines = activeSection.content.split('\n');
            lines.forEach((line, index) => {
                const match = line.match(/^(#{1,3})\s+(.*)/);
                if (match) {
                    const level = match[1].length;
                    const text = match[2].trim();
                    const id = `heading-${index}`;
                    headings.push({ id, text, level });
                }
            });
            setToc(headings);
        }
    }, [selectedTab, isOpen, activeSection, eduSubTab]);

    if (!mounted || !isOpen) return null;

    const scrollToHeading = (index: number) => {
        if (contentRef.current) {
            const headings = contentRef.current.querySelectorAll('h1, h2, h3');
            if (headings[index]) {
                headings[index].scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    };

    const MarkdownComponents = {
        h1: ({ ...props }: any) => <h1 className="text-5xl font-black tracking-tight text-foreground mb-14 border-b border-border pb-10 leading-none" {...props} />,
        h3: ({ ...props }: any) => <h3 className="text-[13px] font-black uppercase tracking-[0.4em] text-accent mt-20 mb-8 flex items-center gap-4 before:h-[1px] before:w-10 before:bg-accent/30" {...props} />,
        p: ({ ...props }: any) => <p className="text-xl text-foreground/80 leading-[2] mb-10 font-medium font-serif" {...props} />,
        ul: ({ ...props }: any) => <ul className="space-y-8 mb-12 list-none p-0" {...props} />,
        li: ({ ...props }: any) => (
            <li className="flex gap-8 text-xl text-foreground/75 m-0 bg-background/40 p-8 rounded-[32px] border border-border/60 hover:border-accent/40 hover:bg-background/60 transition-all duration-300 shadow-sm group">
                <div className="shrink-0 mt-2.5 h-2.5 w-2.5 rounded-full bg-accent group-hover:scale-125 transition-transform" />
                <div className="leading-relaxed" {...props} />
            </li>
        ),
        code: ({ inline, className, children, ...props }: any) => {
            const match = /language-(\w+)/.exec(className || '');
            return !inline && match ? (
                <div className="my-10 rounded-2xl overflow-hidden border border-border shadow-2xl group relative">
                    <div className="flex items-center justify-between px-4 py-2 bg-background/80 border-b border-border">
                        <span className="text-[10px] font-black uppercase tracking-widest text-muted">{match[1]} execution context</span>
                        <div className="flex gap-1.5">
                            <div className="h-2.5 w-2.5 rounded-full bg-red-500/20" />
                            <div className="h-2.5 w-2.5 rounded-full bg-yellow-500/20" />
                            <div className="h-2.5 w-2.5 rounded-full bg-green-500/20" />
                        </div>
                    </div>
                    <SyntaxHighlighter
                        style={atomDark}
                        language={match[1]}
                        PreTag="div"
                        customStyle={{
                            margin: 0,
                            padding: '1.5rem',
                            fontSize: '13px',
                            backgroundColor: 'transparent',
                            fontFamily: 'var(--font-mono)'
                        }}
                        {...props}
                    >
                        {String(children).replace(/\n$/, '')}
                    </SyntaxHighlighter>
                </div>
            ) : (
                <code className="bg-accent/10 border border-accent/20 text-accent px-2 py-0.5 rounded-md font-mono text-[14px] font-bold" {...props}>
                    {children}
                </code>
            )
        },
        strong: ({ ...props }: any) => <strong className="text-foreground font-black" {...props} />,
        em: ({ ...props }: any) => <em className="text-accent italic font-serif" {...props} />,
    };

    return (
        <div className="fixed inset-0 z-[200] flex items-center justify-center p-4 md:p-8">
            {/* Global LaTeX Style override for elegance */}
            <style dangerouslySetInnerHTML={{
                __html: `
                .katex-display {
                    font-size: 1.8em !important;
                    margin: 3rem 0 !important;
                    padding: 2.5rem !important;
                    background: linear-gradient(to bottom right, rgba(var(--accent-rgb), 0.05), transparent) !important;
                    border-radius: 2rem !important;
                    border: 1px solid rgba(var(--accent-rgb), 0.15) !important;
                    color: var(--foreground) !important;
                    box-shadow: inset 0 0 40px rgba(0,0,0,0.1) !important;
                    overflow-x: auto !important;
                    overflow-y: hidden !important;
                }
                .katex {
                    color: inherit !important;
                    font-size: 1.1em;
                }
                .prose-elegant h1, .prose-elegant h2, .prose-elegant h3 {
                    font-family: var(--font-sans);
                }
            ` }} />

            <div className="absolute inset-0 bg-background/70 backdrop-blur-2xl transition-opacity duration-300" onClick={onClose} />

            <div className="relative bg-card border border-border rounded-[40px] w-full max-w-[95%] h-full max-h-[920px] flex flex-col overflow-hidden shadow-[0_64px_256px_-32px_rgba(0,0,0,0.6)] animate-in zoom-in-95 duration-700 ease-[cubic-bezier(0.16,1,0.3,1)]">
                {/* Header */}
                <div className="flex items-center justify-between px-10 py-7 border-b border-border shrink-0 bg-card/60 backdrop-blur-xl">
                    <div className="flex items-center gap-6">
                        <div className="h-14 w-14 rounded-3xl bg-accent/20 flex items-center justify-center text-accent shadow-lg shadow-accent/10 border border-accent/30 scale-110">
                            {mode === 'docs' ? <BookOpen size={28} /> : <GraduationCap size={28} />}
                        </div>
                        <div>
                            <h2 className="text-xl font-black uppercase tracking-tight text-foreground leading-none mb-1">
                                {mode === 'docs' ? "Intelligence Repository" : "Advanced Quant Curriculum"}
                            </h2>
                            <div className="flex items-center gap-3">
                                <span className="h-2 w-2 rounded-full bg-accent animate-pulse shadow-[0_0_10px_rgba(var(--accent-rgb),1)]" />
                                <p className="text-[11px] text-muted uppercase tracking-[0.4em] font-black opacity-60">
                                    {mode === 'docs' ? "Terminal Manual v4" : "Pedagogical Theory v1.1"}
                                </p>
                            </div>
                        </div>
                    </div>

                    {mode === 'education' && (
                        <div className="flex items-center bg-background/80 border border-border rounded-2xl p-1.5 gap-2 shadow-inner">
                            <button
                                onClick={() => setEduSubTab('manual')}
                                className={`px-6 py-2.5 rounded-xl text-[11px] font-black uppercase tracking-widest transition-all duration-500 ${eduSubTab === 'manual' ? "bg-accent text-white shadow-xl translate-y-[-1px]" : "text-muted hover:text-foreground"}`}
                            >
                                Curriculum Path
                            </button>
                            <button
                                onClick={() => setEduSubTab('playground')}
                                className={`px-6 py-2.5 rounded-xl text-[11px] font-black uppercase tracking-widest transition-all duration-500 ${eduSubTab === 'playground' ? "bg-accent text-white shadow-xl translate-y-[-1px]" : "text-muted hover:text-foreground"}`}
                            >
                                Live Workspace
                            </button>
                        </div>
                    )}

                    <button
                        onClick={onClose}
                        className="h-12 w-12 flex items-center justify-center rounded-2xl bg-background/50 hover:bg-card-hover border border-border text-muted hover:text-foreground transition-all duration-500 shadow-sm hover:rotate-90"
                    >
                        <X size={24} />
                    </button>
                </div>

                <div className="flex-1 flex overflow-hidden">
                    {/* Sidebar */}
                    {eduSubTab === 'manual' && (
                        <div className="w-[340px] border-r border-border flex flex-col shrink-0 bg-background/30 backdrop-blur-md">
                            <div className="p-8">
                                <div className="relative group">
                                    <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-muted/60 group-focus-within:text-accent transition-all duration-300" size={16} />
                                    <input
                                        type="text"
                                        placeholder="Scan intelligence modules..."
                                        value={searchQuery}
                                        onChange={(e) => setSearchQuery(e.target.value)}
                                        className="w-full bg-background/90 border border-border rounded-[20px] py-4 pl-12 pr-6 text-sm font-bold focus:outline-none focus:ring-4 focus:ring-accent/10 transition-all placeholder:text-muted/40 text-foreground"
                                    />
                                </div>
                            </div>

                            <div className="flex-1 overflow-y-auto px-5 space-y-2 py-4 custom-scrollbar">
                                <p className="text-[10px] uppercase tracking-[0.4em] px-6 pb-6 font-black text-accent/60">Module Hierarchy</p>
                                {filteredSections.map((section) => (
                                    <button
                                        key={section.id}
                                        onClick={() => setSelectedTab(section.id)}
                                        className={`w-full flex items-center justify-between px-6 py-5 rounded-[24px] transition-all duration-500 group border ${selectedTab === section.id
                                            ? "bg-accent text-white border-accent shadow-xl shadow-accent/20 translate-x-3 scale-[1.02]"
                                            : "text-muted hover:text-foreground hover:bg-card hover:border-border/60 border-transparent"
                                            }`}
                                    >
                                        <div className="flex items-center gap-5">
                                            <div className={`p-2.5 rounded-[14px] transition-all duration-500 ${selectedTab === section.id ? "bg-white/20" : "bg-muted/5 group-hover:bg-accent/10"}`}>
                                                <section.icon size={20} className={selectedTab === section.id ? "text-white" : "text-muted group-hover:text-accent"} />
                                            </div>
                                            <span className="text-sm font-black tracking-tight">{section.title}</span>
                                        </div>
                                        <ChevronRight size={18} className={`transition-all duration-700 ${selectedTab === section.id ? "opacity-100 rotate-90" : "opacity-0 -translate-x-4 group-hover:opacity-100 group-hover:translate-x-0"}`} />
                                    </button>
                                ))}
                            </div>
                        </div>
                    )}

                    {/* Main Content */}
                    <div className="flex-1 flex overflow-hidden relative">
                        {eduSubTab === 'manual' ? (
                            <>
                                <main ref={contentRef} className="flex-1 overflow-y-auto bg-card scroll-smooth p-16 md:p-24 custom-scrollbar">
                                    <div className="max-w-4xl mx-auto animate-in fade-in slide-in-from-bottom-12 duration-1000 prose-elegant">
                                        <ReactMarkdown
                                            remarkPlugins={[remarkMath]}
                                            rehypePlugins={[rehypeKatex]}
                                            components={MarkdownComponents as any}
                                        >
                                            {activeSection.content}
                                        </ReactMarkdown>
                                    </div>
                                </main>

                                <div className="w-[280px] border-l border-border bg-background/20 backdrop-blur-md p-10 hidden 2xl:flex flex-col shrink-0">
                                    <div className="flex items-center gap-3 mb-10 text-accent">
                                        <List size={18} />
                                        <span className="text-[11px] font-black uppercase tracking-[0.3em]">Module Index</span>
                                    </div>
                                    <div className="space-y-4 overflow-y-auto custom-scrollbar pr-4">
                                        {toc.map((heading, idx) => (
                                            <button
                                                key={heading.id}
                                                onClick={() => scrollToHeading(idx)}
                                                className={`w-full text-left py-3 px-4 rounded-xl text-xs transition-all duration-300 hover:bg-accent/10 hover:text-accent group flex gap-3 ${heading.level === 1 ? "font-black text-foreground bg-accent/5 border border-accent/20" :
                                                    heading.level === 2 ? "pl-6 font-bold text-muted border border-transparent" : "pl-8 text-muted/60 border border-transparent"
                                                    }`}
                                            >
                                                <span className="opacity-20 group-hover:opacity-100 transition-opacity font-mono">#</span>
                                                <span className="truncate">{heading.text}</span>
                                            </button>
                                        ))}
                                    </div>
                                    <div className="mt-auto pt-10 border-t border-border">
                                        <div className="p-6 rounded-[28px] bg-gradient-to-br from-accent/10 to-transparent border border-accent/20 flex flex-col gap-4">
                                            <ShieldCheck size={24} className="text-accent" />
                                            <p className="text-[10px] text-muted-foreground leading-relaxed font-bold uppercase tracking-widest">
                                                All models are validated via Monte Carlo stress tests.
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </>
                        ) : (
                            <div className="flex-1 flex flex-col bg-background/40 p-8 gap-8">
                                <div className="flex-1 flex gap-8 overflow-hidden">
                                    <div className="flex-1 flex flex-col bg-card border border-border rounded-[32px] overflow-hidden shadow-2xl">
                                        <div className="flex items-center justify-between px-8 py-4 border-b border-border bg-background/40">
                                            <div className="flex items-center gap-3 text-muted">
                                                <Code size={16} className="text-accent" />
                                                <span className="text-[11px] font-black uppercase tracking-[0.2em]">Source Code</span>
                                            </div>
                                        </div>
                                        <textarea
                                            value={playgroundContent}
                                            onChange={(e) => setPlaygroundContent(e.target.value)}
                                            className="flex-1 p-10 bg-transparent font-mono text-sm resize-none focus:outline-none text-foreground/80 custom-scrollbar leading-relaxed"
                                        />
                                    </div>

                                    <div className="flex-1 flex flex-col bg-card border border-border rounded-[32px] overflow-hidden shadow-2xl">
                                        <div className="flex items-center gap-3 px-8 py-4 border-b border-border bg-background/40">
                                            <Play size={16} className="text-green-500" />
                                            <span className="text-[11px] font-black uppercase tracking-[0.2em]">Theorem Preview</span>
                                        </div>
                                        <div className="flex-1 overflow-y-auto p-12 custom-scrollbar markdown-preview prose-elegant">
                                            <ReactMarkdown
                                                remarkPlugins={[remarkMath]}
                                                rehypePlugins={[rehypeKatex]}
                                                components={MarkdownComponents as any}
                                            >
                                                {playgroundContent}
                                            </ReactMarkdown>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
