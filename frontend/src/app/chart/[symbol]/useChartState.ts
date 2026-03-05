import { useState } from "react";
import { MAConfig, DEFAULT_MAS } from "./chartMath";

export function useChartState() {
    const [mas, setMas] = useState<MAConfig[]>(DEFAULT_MAS);
    const [indicatorsOpen, setIndicatorsOpen] = useState(false);

    // Oscillator visibility
    const [showMACD, setShowMACD] = useState(true);
    const [showStoch, setShowStoch] = useState(true);

    // Volume Profile visibility
    const [showVP, setShowVP] = useState(false);

    // MACD params
    const [macdFast, setMacdFast] = useState(12);
    const [macdSlow, setMacdSlow] = useState(26);
    const [macdSignal, setMacdSignal] = useState(9);

    // Stochastic params
    const [stochK, setStochK] = useState(14);
    const [stochD, setStochD] = useState(3);
    const [stochSmooth, setStochSmooth] = useState(3);

    // Fibonacci params
    const [showFib, setShowFib] = useState(false);
    const [fibLookback, setFibLookback] = useState(120);

    // Bollinger Bands params
    const [showBB, setShowBB] = useState(false);
    const [bbPeriod, setBbPeriod] = useState(20);
    const [bbMult, setBbMult] = useState(2.0);

    // ATR params
    const [showATR, setShowATR] = useState(false);
    const [atrPeriod, setAtrPeriod] = useState(14);

    // Parabolic SAR
    const [showPSAR, setShowPSAR] = useState(false);

    // Supertrend
    const [showSupertrend, setShowSupertrend] = useState(false);

    // Williams %R
    const [showWilliams, setShowWilliams] = useState(false);

    // MFI
    const [showMFI, setShowMFI] = useState(false);

    // CMF
    const [showCMF, setShowCMF] = useState(false);

    return {
        mas, setMas,
        indicatorsOpen, setIndicatorsOpen,
        showMACD, setShowMACD,
        showStoch, setShowStoch,
        showVP, setShowVP,
        macdFast, setMacdFast,
        macdSlow, setMacdSlow,
        macdSignal, setMacdSignal,
        stochK, setStochK,
        stochD, setStochD,
        stochSmooth, setStochSmooth,
        showFib, setShowFib,
        fibLookback, setFibLookback,
        showBB, setShowBB,
        bbPeriod, setBbPeriod,
        bbMult, setBbMult,
        showATR, setShowATR,
        atrPeriod, setAtrPeriod,
        showPSAR, setShowPSAR,
        showSupertrend, setShowSupertrend,
        showWilliams, setShowWilliams,
        showMFI, setShowMFI,
        showCMF, setShowCMF
    };
}
