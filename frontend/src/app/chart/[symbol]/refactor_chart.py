import os
import re

file_path = "C:/AssetManager/frontend/src/app/chart/[symbol]/page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add new imports
import_str = """import { MAChip, ParamInput } from "./ChartUIComponents";
import { ChartTopBar, TIMEFRAMES } from "./ChartTopBar";
import { ChartIndicatorsToolbar } from "./ChartIndicatorsToolbar";

/* ─── Main Component ──────────────────────────────────────────────────── */"""

if "ChartTopBar" not in content:
    content = content.replace("import { MAChip, ParamInput } from \"./ChartUIComponents\";\n\n/* ─── Main Component ──────────────────────────────────────────────────── */", import_str)

# 2. Remove TIMEFRAMES array
tf_pattern = re.compile(r'const TIMEFRAMES = \[\s*\{ label: "5m".*?\n\s*\];\n', re.DOTALL)
content = re.sub(tf_pattern, '', content)

# 3. Replace JSX Block
start_marker = "            {/* ─── Top Bar ──────────────────────────────────────────────── */}"
end_marker = "                ))}\n            </div>"

start_idx = content.find(start_marker)

# Find the end idx roughly after start_idx
end_idx = content.find(end_marker, start_idx)
if start_idx != -1 and end_idx != -1:
    end_idx += len(end_marker)
    
    replacement = """
            <ChartTopBar
                router={router}
                symbol={symbol}
                timeframe={timeframe}
                setTimeframe={setTimeframe}
                quote={quote}
                loading={loading}
                zoomIn={zoomIn}
                zoomOut={zoomOut}
            />

            <ChartIndicatorsToolbar
                indicatorsOpen={indicatorsOpen}
                setIndicatorsOpen={setIndicatorsOpen}
                showVP={showVP}
                setShowVP={setShowVP}
                mas={mas}
                addMA={addMA}
                updateMA={updateMA}
                removeMA={removeMA}
                showMACD={showMACD}
                setShowMACD={setShowMACD}
                macdFast={macdFast}
                macdSlow={macdSlow}
                macdSignal={macdSignal}
                showStoch={showStoch}
                setShowStoch={setShowStoch}
                stochK={stochK}
                stochD={stochD}
                stochSmooth={stochSmooth}
                showFib={showFib}
                setShowFib={setShowFib}
                fibLookback={fibLookback}
                setFibLookback={setFibLookback}
                showBB={showBB}
                setShowBB={setShowBB}
                bbPeriod={bbPeriod}
                setBbPeriod={setBbPeriod}
                bbMult={bbMult}
                setBbMult={setBbMult}
                showATR={showATR}
                setShowATR={setShowATR}
                atrPeriod={atrPeriod}
                setAtrPeriod={setAtrPeriod}
                showPSAR={showPSAR}
                setShowPSAR={setShowPSAR}
                showSupertrend={showSupertrend}
                setShowSupertrend={setShowSupertrend}
                showWilliams={showWilliams}
                setShowWilliams={setShowWilliams}
                showMFI={showMFI}
                setShowMFI={setShowMFI}
                showCMF={showCMF}
                setShowCMF={setShowCMF}
            />
    """
    
    content = content[:start_idx] + replacement.strip('\n') + "\n" + content[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("SUCCESS: Refactored page.tsx UI blocks.")
