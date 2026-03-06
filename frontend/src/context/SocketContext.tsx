"use client";

import React, { createContext, useContext, useEffect, useState } from "react";
import { io, Socket } from "socket.io-client";

interface SocketContextType {
    socket: Socket | null;
    connected: boolean;
}

const SocketContext = createContext<SocketContextType>({ socket: null, connected: false });

export const useSocket = () => useContext(SocketContext);

export const SocketProvider = ({ children }: { children: React.ReactNode }) => {
    const [socket, setSocket] = useState<Socket | null>(null);
    const [connected, setConnected] = useState(false);

    useEffect(() => {
        const s = io("http://127.0.0.1:8282", {
            transports: ["websocket"],
            reconnectionAttempts: 5,
        });

        s.on("connect", () => {
            console.log("[Socket] Connected to backend");
            setConnected(true);
        });

        s.on("disconnect", () => {
            console.log("[Socket] Disconnected from backend");
            setConnected(false);
        });

        setSocket(s);

        return () => {
            s.close();
        };
    }, []);

    return (
        <SocketContext.Provider value={{ socket, connected }}>
            {children}
        </SocketContext.Provider>
    );
};
