import { useState, useCallback, useEffect } from "react";
import { Session, Message } from "./TerminalConstants";
import { usePortfolio } from "../../context/PortfolioContext";

export function useTerminalSession() {
    const [sessions, setSessions] = useState<Session[]>([{
        id: '1',
        history: [{ type: 'output', text: 'MMAM Intelligence · OpenBB Engine\nType "help" for available commands.\n' }],
        input: '',
        isExecuting: false,
        historyIndex: -1,
        pendingCmd: null,
    }]);
    const [activeId, setActiveId] = useState('1');
    const { refreshPortfolio } = usePortfolio();

    const updateSession = useCallback((id: string, update: Partial<Session>) => {
        setSessions(prev => prev.map(s => s.id === id ? { ...s, ...update } : s));
    }, []);

    const runCommand = useCallback(async (sessionId: string, cmd: string, baseHistory: Message[]) => {
        const newHistory: Message[] = [...baseHistory, { type: 'input', text: cmd }];
        updateSession(sessionId, { history: newHistory, input: '', historyIndex: -1, isExecuting: true, pendingCmd: null });

        if (cmd.toLowerCase() === 'clear') {
            updateSession(sessionId, { history: [], isExecuting: false });
            return;
        }

        try {
            const response = await fetch('http://127.0.0.1:8282/openbb/cli', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command: cmd })
            });
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            const data = await response.json();

            if (data.type === 'chart_window' && data.html) {
                const win = window.open('', '_blank', 'width=1440,height=820,menubar=no,toolbar=no,location=no,status=no');
                if (win) { win.document.open(); win.document.write(data.html); win.document.close(); }
                updateSession(sessionId, {
                    history: [...newHistory, { type: 'output', text: '📊 Chart opened in new window.' }],
                    isExecuting: false,
                });
                window.dispatchEvent(new CustomEvent('terminal-success', { detail: { command: cmd } }));
            } else {
                updateSession(sessionId, {
                    history: [...newHistory, { type: data.type === 'error' ? 'error' : 'output', text: data.output ?? data.error ?? 'OK' }],
                    isExecuting: false,
                });
                if (data.type === 'error') {
                    window.dispatchEvent(new CustomEvent('terminal-error', { detail: { command: cmd, error: data.error ?? data.output ?? 'Unknown error' } }));
                } else {
                    window.dispatchEvent(new CustomEvent('terminal-success', { detail: { command: cmd } }));
                }
                if (data.output && data.output.includes('LIQUIDATION COMPLETE')) {
                    refreshPortfolio();
                }
            }
        } catch (error: any) {
            updateSession(sessionId, {
                history: [...newHistory, { type: 'error', text: `Connection failed: ${error.message}` }],
                isExecuting: false,
            });
        }
    }, [updateSession, refreshPortfolio]);

    useEffect(() => {
        sessions.forEach(s => {
            if (!s.isExecuting && s.pendingCmd) {
                runCommand(s.id, s.pendingCmd, s.history);
            }
        });
    }, [sessions, runCommand]);

    return {
        sessions, setSessions,
        activeId, setActiveId,
        updateSession,
        runCommand
    };
}
