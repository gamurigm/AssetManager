"use client";

import React, { createContext, useContext, useEffect, useState, useRef, useCallback } from "react";
import { io, Socket } from "socket.io-client";

interface SocketContextType {
    socket: Socket | null;
    connected: boolean;
    reconnect: () => void;
}

const SocketContext = createContext<SocketContextType>({ socket: null, connected: false, reconnect: () => {} });

export const useSocket = () => useContext(SocketContext);

export const SocketProvider = ({ children }: { children: React.ReactNode }) => {
    const [socket, setSocket] = useState<Socket | null>(null);
    const [connected, setConnected] = useState(false);
    const socketRef = useRef<Socket | null>(null);

    const createSocket = useCallback(() => {
        // Close any existing socket cleanly before creating a new one
        if (socketRef.current) {
            socketRef.current.removeAllListeners();
            socketRef.current.close();
        }

        const s = io("http://127.0.0.1:8282", {
            // Try WebSocket first, fall back to long-polling automatically
            transports: ["websocket", "polling"],
            reconnection: true,
            reconnectionAttempts: Infinity,
            reconnectionDelay: 1000,
            reconnectionDelayMax: 10000,
            timeout: 10000,
        });

        s.on("connect", () => {
            console.log("[Socket] Connected to backend");
            setConnected(true);
        });

        s.on("disconnect", (reason) => {
            console.log("[Socket] Disconnected:", reason);
            setConnected(false);
        });

        s.on("connect_error", (err) => {
            console.warn("[Socket] Connection error:", err.message);
            setConnected(false);
        });

        socketRef.current = s;
        setSocket(s);
        return s;
    }, []);

    useEffect(() => {
        const s = createSocket();
        return () => {
            s.removeAllListeners();
            s.close();
        };
    }, [createSocket]);

    // Manual reconnect: forcefully cycles the connection
    const reconnect = useCallback(() => {
        createSocket();
    }, [createSocket]);

    return (
        <SocketContext.Provider value={{ socket, connected, reconnect }}>
            {children}
        </SocketContext.Provider>
    );
};
