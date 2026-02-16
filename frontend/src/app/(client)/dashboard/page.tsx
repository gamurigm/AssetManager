"use client"

import { useSocket } from "@/hooks/useSocket";
import { useEffect, useState } from "react";

export default function ClientDashboard() {
    const { socket, isConnected } = useSocket();
    const [portfolioValue, setPortfolioValue] = useState(125430.25);
    const [pnl, setPnl] = useState(1205.40);

    useEffect(() => {
        if (socket) {
            socket.on('portfolio:update', (data) => {
                setPortfolioValue(data.total_value);
                setPnl(data.pnl);
            });
        }
    }, [socket]);

    return (
        <div className="p-8 space-y-8">
            <header className="flex justify-between items-center">
                <h1 className="text-3xl font-bold">Client Dashboard</h1>
                <div className="flex items-center space-x-2">
                    <span className={`h-3 w-3 rounded-full ${isConnected ? "bg-green-500" : "bg-red-500"}`}></span>
                    <span className="text-sm text-gray-500">{isConnected ? "Live Connection" : "Offline"}</span>
                </div>
            </header>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="p-6 bg-zinc-900 border border-zinc-800 rounded-xl shadow-sm">
                    <p className="text-sm text-gray-400">Total Portfolio Value</p>
                    <p className="text-3xl font-mono mt-1">${portfolioValue.toLocaleString()}</p>
                </div>
                <div className="p-6 bg-zinc-900 border border-zinc-800 rounded-xl shadow-sm">
                    <p className="text-sm text-gray-400">Today's P&L</p>
                    <p className={`text-3xl font-mono mt-1 ${pnl >= 0 ? "text-green-500" : "text-red-500"}`}>
                        {pnl >= 0 ? "+" : ""}${pnl.toLocaleString()}
                    </p>
                </div>
                <div className="p-6 bg-zinc-900 border border-zinc-800 rounded-xl shadow-sm">
                    <p className="text-sm text-gray-400">AUM Rank</p>
                    <p className="text-3xl font-mono mt-1">#14</p>
                </div>
            </div>

            <div className="p-6 bg-zinc-900 border border-zinc-800 rounded-xl">
                <h2 className="text-xl font-semibold mb-4">Your AI Advisor</h2>
                <div className="h-64 flex items-center justify-center border border-dashed border-zinc-700 rounded-lg text-gray-500">
                    AI Chat Insight will appear here...
                </div>
            </div>
        </div>
    );
}
