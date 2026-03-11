# run_app.ps1
# Script inteligente para correr AssetManager (OpenBB API + Portfolio C++ + Backend + Frontend)
# PUERTOS: OpenBB API (6900), Portfolio C++ (9092), Backend (8282), Frontend (3309)

Clear-Host
$host.UI.RawUI.WindowTitle = "AssetManager - Smart Launcher"

Write-Host "==========================================" -ForegroundColor Yellow
Write-Host "   AssetManager: Sistema Inteligente      " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Yellow

$rootPath = $PSScriptRoot
$backendPath = Join-Path $rootPath "backend"
$frontendPath = Join-Path $rootPath "frontend"
$openbbPath = Join-Path $rootPath "external_repos" | Join-Path -ChildPath "OpenBB" | Join-Path -ChildPath "OpenBB"
$portfolioCppScript = Join-Path $rootPath "run_portfolio_cpp_service.ps1"
$portfolioCppPort = 9095
$portfolioCppUrl = "http://127.0.0.1:$portfolioCppPort"
$portfolioCppReady = $false

# Detectar Plataforma
$myIsLinux = $IsLinux -or (Test-Path /proc/version -ErrorAction SilentlyContinue)
$venvBin = if ($myIsLinux) { "bin" } else { "Scripts" }
$pythonExt = if ($myIsLinux) { "" } else { ".exe" }
$activateScript = if ($myIsLinux) { "activate" } else { "Activate.ps1" }

# Función para verificar si un puerto está en uso
function Test-PortInUse($port) {
    if ($myIsLinux) {
        # En Linux/WSL usamos ss o netstat
        return $null -ne (ss -tuln | Select-String ":$port ")
    } else {
        return Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue
    }
}

# --- OpenBB API Server (Puerto 6900) ---
Write-Host "`n[1/7] Verificando OpenBB API Server (Puerto 6900)..." -ForegroundColor White
$openbbVenv = $openbbPath | Join-Path -ChildPath ".venv" | Join-Path -ChildPath $venvBin | Join-Path -ChildPath $activateScript

if (Test-Path $openbbVenv) {
    if (Test-PortInUse 6900) {
        Write-Host " - OpenBB API ya corriendo en puerto 6900." -ForegroundColor Green
    }
    else {
        Write-Host " - Iniciando OpenBB API Server..." -ForegroundColor Green
        if ($myIsLinux) {
            # En WSL, iniciamos en segundo plano
            bash -c "cd '$openbbPath' && source '$openbbVenv' && uvicorn openbb_core.api.rest_api:app --host 0.0.0.0 --port 6900 > /dev/null 2>&1 &"
        } else {
            Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$openbbPath'; & '$openbbVenv'; uvicorn openbb_core.api.rest_api:app --host 0.0.0.0 --port 6900" -WindowStyle Minimized
        }
        Write-Host " - OpenBB API se está calentando (puede tardar ~10s la primera vez)." -ForegroundColor DarkYellow
        Start-Sleep -Seconds 3
    }
}
else {
    Write-Host " - AVISO: OpenBB .venv no encontrado en $openbbVenv" -ForegroundColor DarkYellow
    Write-Host "   El terminal usará el modo subprocess como fallback." -ForegroundColor DarkYellow
}

# --- Portfolio C++ Service (Puerto 9095) ---
Write-Host "`n[2/7] Verificando Portfolio C++ Service (Puerto 9095)..." -ForegroundColor White
if (Test-Path $portfolioCppScript) {
    try {
        & $portfolioCppScript -Port $portfolioCppPort -WindowStyle Minimized | Out-Null
        $portfolioCppReady = $true
    }
    catch {
        Write-Host " - AVISO: No se pudo iniciar portfolio_cpp_service: $($_.Exception.Message)" -ForegroundColor DarkYellow
        Write-Host "   El backend seguira con fallback a C++ embebido o Python." -ForegroundColor DarkYellow
    }
}
else {
    Write-Host " - AVISO: No se encontro $portfolioCppScript" -ForegroundColor DarkYellow
}

# --- Backend (Puerto 8282) ---
Write-Host "`n[3/7] Verificando Backend (Puerto 8282)..." -ForegroundColor White
if (Test-PortInUse 8282) {
    Write-Host " - ¡Puerto 8282 ocupado! Matando proceso anterior..." -ForegroundColor Red
    if ($myIsLinux) {
        fuser -k 8282/tcp 2>/dev/null
    } else {
        Get-NetTCPConnection -LocalPort 8282 -ErrorAction SilentlyContinue | ForEach-Object { 
            Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue 
        }
    }
    Start-Sleep -Seconds 2
}

Write-Host " - Iniciando Backend (FastAPI)..." -ForegroundColor Green
$backendPython = $backendPath | Join-Path -ChildPath "venv" | Join-Path -ChildPath $venvBin | Join-Path -ChildPath "python$pythonExt"
if (Test-Path $backendPython) {
    $backendEnvVar = if ($portfolioCppReady) { "PORTFOLIO_CPP_SERVICE_URL=$portfolioCppUrl " } else { "" }

    if ($myIsLinux) {
        bash -c "cd '$backendPath' && ${backendEnvVar}'$backendPython' -m uvicorn app.main:sio_app --reload --reload-dir app --host 0.0.0.0 --port 8282 > /dev/null 2>&1 &"
    } else {
        $backendEnvCommand = if ($portfolioCppReady) { "`$env:PORTFOLIO_CPP_SERVICE_URL = '$portfolioCppUrl'; " } else { "Remove-Item Env:PORTFOLIO_CPP_SERVICE_URL -ErrorAction SilentlyContinue; " }
        Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$backendPath'; $backendEnvCommand& '$backendPython' -m uvicorn app.main:sio_app --reload --reload-dir app --host 0.0.0.0 --port 8282" -WindowStyle Normal
    }
}
else {
    Write-Host " - ERROR: No se encontró el Python del entorno virtual en $backendPython" -ForegroundColor Red
}

# --- Frontend (Puerto 3309) ---
Write-Host "[4/7] Verificando Frontend (Puerto 3309)..." -ForegroundColor White
if (Test-PortInUse 3309) {
    Write-Host " - ¡Puerto 3309 ocupado! Matando proceso anterior..." -ForegroundColor Red
    if ($myIsLinux) {
        fuser -k 3309/tcp 2>/dev/null
    } else {
        Get-NetTCPConnection -LocalPort 3309 -ErrorAction SilentlyContinue | ForEach-Object { 
            Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue 
        }
    }
    
    # Smart Wait: Esperar hasta que el puerto se libere realmente
    Write-Host " - Esperando liberación de recursos..." -NoNewline
    $retries = 0
    while ((Test-PortInUse 3309) -and ($retries -lt 10)) {
        Start-Sleep -Seconds 1
        Write-Host "." -NoNewline
        $retries++
    }
    Write-Host " Listo." -ForegroundColor Green
}

Write-Host " - Iniciando Frontend y Electron..." -ForegroundColor Green
if (Test-Path $frontendPath) {
    if ($myIsLinux) {
        bash -c "cd '$frontendPath' && npm run dev > /dev/null 2>&1 &"
        Write-Host " - Frontend iniciado en segundo plano." -ForegroundColor Green
    } else {
        Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$frontendPath'; npm run electron" -WindowStyle Normal
    }
}
else {
    Write-Host " - ERROR: No se encontró el directorio frontend en $frontendPath" -ForegroundColor Red
}

# --- Microservicios de Mercado (Kafka-aware) ---
Write-Host "`n[5/7] Verificando Market Data Gateway..." -ForegroundColor White
$gatewayFile = Join-Path $backendPath "services" | Join-Path -ChildPath "market_data_gateway" | Join-Path -ChildPath "main.py"
if (Test-Path $gatewayFile) {
    Write-Host " - Iniciando Market Data Gateway..." -ForegroundColor Green
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "`$env:PYTHONUTF8=1; Set-Location '$backendPath'; & '$backendPython' '$gatewayFile'" -WindowStyle Minimized
}

Write-Host "[6/7] Verificando Storage Service (Data Lake)..." -ForegroundColor White
$storageFile = Join-Path $backendPath "services" | Join-Path -ChildPath "storage_service" | Join-Path -ChildPath "main.py"
if (Test-Path $storageFile) {
    Write-Host " - Iniciando Storage Service..." -ForegroundColor Green
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "`$env:PYTHONUTF8=1; Set-Location '$backendPath'; & '$backendPython' '$storageFile'" -WindowStyle Minimized
}

Write-Host "[7/7] Verificando Strategy Engine (Live Trading)..." -ForegroundColor White
$strategyFile = Join-Path $backendPath "services" | Join-Path -ChildPath "strategy_engine" | Join-Path -ChildPath "main.py"
if (Test-Path $strategyFile) {
    Write-Host " - Iniciando Strategy Engine..." -ForegroundColor Green
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "`$env:PYTHONUTF8=1; Set-Location '$backendPath'; & '$backendPython' '$strategyFile'" -WindowStyle Minimized
}

Write-Host "`n¡Chequeo completado!" -ForegroundColor Yellow
Write-Host "------------------------------------------"
Write-Host "OpenBB API: http://localhost:6900" -ForegroundColor Magenta
if ($portfolioCppReady) {
    Write-Host "Portfolio C++: http://localhost:$portfolioCppPort" -ForegroundColor Green
}
else {
    Write-Host "Portfolio C++: fallback to embedded C++ / Python" -ForegroundColor DarkYellow
}
Write-Host "Backend:    http://localhost:8282" -ForegroundColor Cyan
Write-Host "Frontend:   http://localhost:3309" -ForegroundColor Cyan
Write-Host "Swagger UI: http://localhost:6900/docs" -ForegroundColor DarkCyan
Write-Host "------------------------------------------"
