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
    const [psarStep, setPsarStep] = useState(0.02);
    const [psarMax, setPsarMax] = useState(0.2);

    // Supertrend
    const [showSupertrend, setShowSupertrend] = useState(false);
    const [supertrendPeriod, setSupertrendPeriod] = useState(10);
    const [supertrendMult, setSupertrendMult] = useState(3);

    // Williams %R
    const [showWilliams, setShowWilliams] = useState(false);
    const [williamsPeriod, setWilliamsPeriod] = useState(14);

    // MFI
    const [showMFI, setShowMFI] = useState(false);
    const [mfiPeriod, setMfiPeriod] = useState(14);

    // CMF
    const [showCMF, setShowCMF] = useState(false);
    const [cmfPeriod, setCmfPeriod] = useState(20);

    // RSI
    const [showRSI, setShowRSI] = useState(false);
    const [rsiPeriod, setRsiPeriod] = useState(14);

    // CCI
    const [showCCI, setShowCCI] = useState(false);
    const [cciPeriod, setCciPeriod] = useState(20);

    // ADX
    const [showADX, setShowADX] = useState(false);
    const [adxPeriod, setAdxPeriod] = useState(14);

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
        psarStep, setPsarStep,
        psarMax, setPsarMax,
        showSupertrend, setShowSupertrend,
        supertrendPeriod, setSupertrendPeriod,
        supertrendMult, setSupertrendMult,
        showWilliams, setShowWilliams,
        williamsPeriod, setWilliamsPeriod,
        showMFI, setShowMFI,
        mfiPeriod, setMfiPeriod,
        showCMF, setShowCMF,
        cmfPeriod, setCmfPeriod,
        showRSI, setShowRSI,
        rsiPeriod, setRsiPeriod,
        showCCI, setShowCCI,
        cciPeriod, setCciPeriod,
        showADX, setShowADX,
        adxPeriod, setAdxPeriod,
    };
}
