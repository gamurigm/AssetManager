"use client"

import { useState } from "react";

export default function TradingPage() {
    const [symbol, setSymbol] = useState("AAPL");
    const [quantity, setQuantity] = useState(1);
    const [orderType, setOrderType] = useState("market");

    const handleTrade = (type: "buy" | "sell") => {
        alert(`${type.toUpperCase()} ${quantity} ${symbol} (${orderType}) executed.`);
    }

    return (
        <div className="p-8 space-y-8">
            <h1 className="text-3xl font-bold">Trading Center</h1>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                {/* Chart Placeholder */}
                <div className="bg-zinc-900 border border-zinc-800 rounded-xl h-96 flex items-center justify-center text-gray-500">
                    TradingView Chart will be integrated here
                </div>

                {/* Order Form */}
                <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 space-y-6">
                    <h2 className="text-xl font-semibold">Place Order</h2>
                    <div className="space-y-4">
                        <div>
                            <label className="text-xs text-gray-400 block mb-1">Symbol</label>
                            <input
                                value={symbol}
                                onChange={(e) => setSymbol(e.target.value.toUpperCase())}
                                className="w-full bg-zinc-800 border-none rounded-lg p-2 focus:ring-1 focus:ring-blue-500"
                            />
                        </div>
                        <div className="flex space-x-4">
                            <div className="flex-1">
                                <label className="text-xs text-gray-400 block mb-1">Order Type</label>
                                <select
                                    value={orderType}
                                    onChange={(e) => setOrderType(e.target.value)}
                                    className="w-full bg-zinc-800 border-none rounded-lg p-2 text-sm"
                                >
                                    <option value="market">Market</option>
                                    <option value="limit">Limit</option>
                                </select>
                            </div>
                            <div className="flex-1">
                                <label className="text-xs text-gray-400 block mb-1">Quantity</label>
                                <input
                                    type="number"
                                    value={quantity}
                                    onChange={(e) => setQuantity(Number(e.target.value))}
                                    className="w-full bg-zinc-800 border-none rounded-lg p-2"
                                />
                            </div>
                        </div>

                        <div className="flex space-x-4 pt-4">
                            <button
                                onClick={() => handleTrade("buy")}
                                className="flex-1 bg-green-600 hover:bg-green-700 p-3 rounded-lg font-bold transition"
                            >
                                Buy {symbol}
                            </button>
                            <button
                                onClick={() => handleTrade("sell")}
                                className="flex-1 bg-red-600 hover:bg-red-700 p-3 rounded-lg font-bold transition"
                            >
                                Sell {symbol}
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
