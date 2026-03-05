import { useState, useRef, useEffect, useCallback } from "react";

export function useTerminalDrag(snapToSafePosition: () => void, setIsOpen: (open: boolean) => void, setIsStellar: (stellar: boolean) => void, resetInactivity: () => void) {
    const [termIconPos, setTermIconPos] = useState({ x: 24, y: 24 });
    const [termDragging, setTermDragging] = useState(false);
    const termDragRef = useRef<{ startX: number; startY: number; startPosX: number; startPosY: number; moved: boolean } | null>(null);

    useEffect(() => {
        const handleMouseMove = (e: MouseEvent) => {
            if (!termDragging || !termDragRef.current) return;
            const dX = termDragRef.current.startX - e.clientX;
            const dY = termDragRef.current.startY - e.clientY;
            if (Math.abs(dX) > 5 || Math.abs(dY) > 5) termDragRef.current.moved = true;
            const padding = 20;
            const maxRight = window.innerWidth - 80 - padding;
            const maxBottom = window.innerHeight - 80 - padding;
            setTermIconPos({
                x: Math.min(Math.max(padding, termDragRef.current.startPosX + dX), Math.max(padding, maxRight)),
                y: Math.min(Math.max(padding, termDragRef.current.startPosY + dY), Math.max(padding, maxBottom)),
            });
        };
        const handleMouseUp = () => {
            if (!termDragging) return;
            setTermDragging(false);
            if (termDragRef.current && !termDragRef.current.moved) {
                snapToSafePosition();
                setIsOpen(true);
                setIsStellar(false);
                resetInactivity();
            }
            termDragRef.current = null;
        };
        if (termDragging) {
            window.addEventListener('mousemove', handleMouseMove);
            window.addEventListener('mouseup', handleMouseUp);
        }
        return () => {
            window.removeEventListener('mousemove', handleMouseMove);
            window.removeEventListener('mouseup', handleMouseUp);
        };
    }, [termDragging, snapToSafePosition, setIsOpen, setIsStellar, resetInactivity]);

    return {
        termIconPos, setTermIconPos,
        termDragging, setTermDragging,
        termDragRef
    };
}
