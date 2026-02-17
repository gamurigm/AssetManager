"use client"

import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from 'recharts';

interface AllocationData {
    name: string;
    value: number;
}

const COLORS = ['#3b82f6', '#10b981', '#8b5cf6', '#f59e0b', '#06b6d4', '#ec4899'];

const CustomTooltip = ({ active, payload }: any) => {
    if (active && payload && payload.length) {
        return (
            <div className="bg-[#0f0f0f]/95 border border-white/10 p-3 rounded-xl shadow-2xl backdrop-blur-md">
                <p className="text-[10px] font-bold text-muted uppercase tracking-widest mb-1">{payload[0].name}</p>
                <p className="text-white font-mono font-bold">${payload[0].value.toLocaleString()}</p>
            </div>
        );
    }
    return null;
};

export default function AllocationDonut({ data }: { data: AllocationData[] }) {
    return (
        <div className="w-full h-full min-h-[250px] relative">
            <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                    <Pie
                        data={data}
                        cx="50%"
                        cy="50%"
                        innerRadius={60}
                        outerRadius={80}
                        paddingAngle={5}
                        dataKey="value"
                    >
                        {data.map((entry, index) => (
                            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} stroke="rgba(0,0,0,0.1)" />
                        ))}
                    </Pie>
                    <Tooltip content={<CustomTooltip />} />
                    <Legend
                        verticalAlign="bottom"
                        height={36}
                        content={({ payload }) => (
                            <div className="flex flex-wrap justify-center gap-x-4 gap-y-1 mt-4">
                                {payload?.map((entry: any, index: number) => (
                                    <div key={index} className="flex items-center gap-1.5 leading-none">
                                        <div className="w-2 h-2 rounded-full" style={{ backgroundColor: entry.color }} />
                                        <span className="text-[10px] font-bold uppercase tracking-tighter text-muted">
                                            {entry.value}
                                        </span>
                                    </div>
                                ))}
                            </div>
                        )}
                    />
                </PieChart>
            </ResponsiveContainer>
            {/* Center Label */}
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-center pointer-events-none">
                <p className="text-[10px] text-muted font-bold uppercase tracking-widest">Total</p>
                <p className="text-sm font-black font-mono">
                    ${data.reduce((a, b) => a + b.value, 0).toLocaleString(undefined, { maximumSignificantDigits: 3 })}
                </p>
            </div>
        </div>
    );
}
