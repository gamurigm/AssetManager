import os

file_path = "c:/AssetManager/frontend/src/app/chart/[symbol]/page.tsx"
out_comp_path = "c:/AssetManager/frontend/src/app/chart/[symbol]/ChartSubPanels.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

hooks_start = 0
hooks_end = 0
panels_start = 0
panels_end = 0

for i, line in enumerate(lines):
    if '// MACD' in line and i+1 < len(lines) and 'useEffect' in lines[i+1]:
        hooks_start = i
    if '// Zoom helpers' in line and hooks_end == 0:
        hooks_end = i
    if '{/* ─── MACD Panel ─────────────────────────────────────────────── */}' in line:
        panels_start = i
    if '{/* ─── CMF Panel ──────────────────────────────────────────────── */}' in line:
        for j in range(i, len(lines)):
            if '</div>' in lines[j] and ')}' in lines[j+1]:
                panels_end = j + 2
                break

print(f"Hooks: {hooks_start} -> {hooks_end}")
print(f"Panels: {panels_start} -> {panels_end}")

hooks_block = "".join(lines[hooks_start:hooks_end])
panels_block = "".join(lines[panels_start:panels_end+1])

# Write ChartSubPanels.tsx
with open(out_comp_path, "w", encoding="utf-8") as f:
    f.write('''import React, { useEffect, useRef } from "react";
import { createChart, IChartApi, HistogramSeries, LineSeries } from "lightweight-charts";
import { Plus, Minus } from "lucide-react";
import { ParamInput } from "./ChartUIComponents";
import { calcMACD, calcStochastic, calcATR, calcWilliamsR, calcMFI, calcCMF } from "./chartMath";

export interface ChartSubPanelsProps {
    rawData: any[];
    chartOpts: (h?: number) => any;
    mainChartApi: React.MutableRefObject<IChartApi | null>;

    showMACD: boolean; setShowMACD: (v: boolean) => void;
    macdFast: number; setMacdFast: (v: number) => void;
    macdSlow: number; setMacdSlow: (v: number) => void;
    macdSignal: number; setMacdSignal: (v: number) => void;

    showStoch: boolean; setShowStoch: (v: boolean) => void;
    stochK: number; setStochK: (v: number) => void;
    stochD: number; setStochD: (v: number) => void;
    stochSmooth: number; setStochSmooth: (v: number) => void;

    showATR: boolean; setShowATR: (v: boolean) => void;
    atrPeriod: number; setAtrPeriod: (v: number) => void;

    showWilliams: boolean; 
    showMFI: boolean; 
    showCMF: boolean; 
}

export function ChartSubPanels({
    rawData, chartOpts, mainChartApi,
    showMACD, setShowMACD, macdFast, setMacdFast, macdSlow, setMacdSlow, macdSignal, setMacdSignal,
    showStoch, setShowStoch, stochK, setStochK, stochD, setStochD, stochSmooth, setStochSmooth,
    showATR, setShowATR, atrPeriod, setAtrPeriod,
    showWilliams, showMFI, showCMF
}: ChartSubPanelsProps) {

    const macdChartRef = useRef<HTMLDivElement>(null);
    const macdChartApi = useRef<IChartApi | null>(null);

    const stochChartRef = useRef<HTMLDivElement>(null);
    const stochChartApi = useRef<IChartApi | null>(null);

    const atrChartRef = useRef<HTMLDivElement>(null);
    const atrChartApi = useRef<IChartApi | null>(null);

    const williamsChartRef = useRef<HTMLDivElement>(null);
    const williamsChartApi = useRef<IChartApi | null>(null);

    const mfiChartRef = useRef<HTMLDivElement>(null);
    const mfiChartApi = useRef<IChartApi | null>(null);

    const cmfChartRef = useRef<HTMLDivElement>(null);
    const cmfChartApi = useRef<IChartApi | null>(null);

''')
    f.write(hooks_block)
    f.write("\n    return (\n        <>\n")
    f.write(panels_block.replace("setShowWilliams(!showWilliams)", "console.log('toggle')").replace("setShowMFI(!showMFI)", "console.log('toggle')").replace("setShowCMF(!showCMF)", "console.log('toggle')"))
    f.write("\n        </>\n    );\n}\n")

# Now strip out the blocks from page.tsx and add import / component call
# Also remove the refs for these charts from page.tsx since they are now in the sub component
# Finding ref hook rows
new_lines = []
skip = False
for i, line in enumerate(lines):
    if hooks_start <= i < hooks_end:
        continue
    if panels_start <= i <= panels_end:
        # replace with the component tag
        if i == panels_start:
            new_lines.append("""
            <ChartSubPanels
                rawData={rawData} chartOpts={chartOpts} mainChartApi={mainChartApi}
                showMACD={showMACD} setShowMACD={setShowMACD} macdFast={macdFast} setMacdFast={setMacdFast} macdSlow={macdSlow} setMacdSlow={setMacdSlow} macdSignal={macdSignal} setMacdSignal={setMacdSignal}
                showStoch={showStoch} setShowStoch={setShowStoch} stochK={stochK} setStochK={setStochK} stochD={stochD} setStochD={setStochD} stochSmooth={stochSmooth} setStochSmooth={setStochSmooth}
                showATR={showATR} setShowATR={setShowATR} atrPeriod={atrPeriod} setAtrPeriod={setAtrPeriod}
                showWilliams={showWilliams} showMFI={showMFI} showCMF={showCMF}
            />
""")
        continue
    
    # Strip the refs
    if "ChartRef = useRef<HTMLDivElement>(null);" in line and ('macd' in line or 'stoch' in line or 'atr' in line or 'williams' in line or 'mfi' in line or 'cmf' in line):
        continue
    if "ChartApi = useRef<IChartApi | null>(null);" in line and ('macd' in line or 'stoch' in line or 'atr' in line or 'williams' in line or 'mfi' in line or 'cmf' in line):
        continue
        
    # Also strip out the imports of subchart indicator calcs since they are only used in ChartSubPanels
    if "calcMACD, calcStochastic, calcFibLevels" in line:
        new_lines.append(line.replace("calcMACD, calcStochastic, ", ""))
        continue
    if "calcBollingerBands, calcATR, calcParabolicSAR" in line:
        new_lines.append(line.replace("calcATR, ", ""))
        continue
    if "calcWilliamsR, calcMFI, calcCMF, calcVolumeProfile" in line:
        new_lines.append(line.replace("calcWilliamsR, calcMFI, calcCMF, ", ""))
        continue
        
    new_lines.append(line)

# Add import
import_stmt = 'import { ChartSubPanels } from "./ChartSubPanels";\n'
for i, line in enumerate(new_lines):
    if '/* ─── Main Component' in line:
        new_lines.insert(i, import_stmt)
        break

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Done refactoring page.tsx")
