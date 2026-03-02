# run_app.ps1
# Script inteligente para correr AssetManager (OpenBB API + Backend + Frontend)
# PUERTOS: OpenBB API (6900), Backend (8282), Frontend (3309)

Clear-Host
$host.UI.RawUI.WindowTitle = "AssetManager - Smart Launcher"

Write-Host "==========================================" -ForegroundColor Yellow
Write-Host "   AssetManager: Sistema Inteligente      " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Yellow

$rootPath = $PSScriptRoot
$backendPath = Join-Path $rootPath "backend"
$frontendPath = Join-Path $rootPath "frontend"
$openbbPath = Join-Path $rootPath "external_repos\OpenBB\OpenBB"

# Función para verificar si un puerto está en uso
function Test-PortInUse($port) {
    return Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue
}

# --- OpenBB API Server (Puerto 6900) ---
Write-Host "`n[0/2] Verificando OpenBB API Server (Puerto 6900)..." -ForegroundColor White
$openbbVenv = Join-Path $openbbPath ".venv\Scripts\Activate.ps1"
if (Test-Path $openbbVenv) {
    if (Test-PortInUse 6900) {
        Write-Host " - OpenBB API ya corriendo en puerto 6900." -ForegroundColor Green
    }
    else {
        Write-Host " - Iniciando OpenBB API Server..." -ForegroundColor Green
        Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$openbbPath'; & '$openbbVenv'; uvicorn openbb_core.api.router:app --host 0.0.0.0 --port 6900" -WindowStyle Minimized
        Write-Host " - OpenBB API se está calentando (puede tardar ~10s la primera vez)." -ForegroundColor DarkYellow
        Start-Sleep -Seconds 3
    }
}
else {
    Write-Host " - AVISO: OpenBB .venv no encontrado en $openbbVenv" -ForegroundColor DarkYellow
    Write-Host "   El terminal usará el modo subprocess como fallback." -ForegroundColor DarkYellow
}

# --- Backend (Puerto 8282) ---
Write-Host "`n[1/2] Verificando Backend (Puerto 8282)..." -ForegroundColor White
if (Test-PortInUse 8282) {
    Write-Host " - ¡Puerto 8282 ocupado! Matando proceso anterior..." -ForegroundColor Red
    Get-NetTCPConnection -LocalPort 8282 -ErrorAction SilentlyContinue | ForEach-Object { 
        Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue 
    }
    Start-Sleep -Seconds 2
}

Write-Host " - Iniciando Backend (FastAPI)..." -ForegroundColor Green
$venvPath = Join-Path $backendPath "venv\Scripts\Activate.ps1"
if (Test-Path $venvPath) {
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$backendPath'; & '$venvPath'; uvicorn app.main:sio_app --reload --host 0.0.0.0 --port 8282" -WindowStyle Normal
}
else {
    Write-Host " - ERROR: No se encontró el entorno virtual en $venvPath" -ForegroundColor Red
}


# --- Frontend (Puerto 3309) ---
Write-Host "[2/2] Verificando Frontend (Puerto 3309)..." -ForegroundColor White
if (Test-PortInUse 3309) {
    Write-Host " - ¡Puerto 3309 ocupado! Matando proceso anterior..." -ForegroundColor Red
    Get-NetTCPConnection -LocalPort 3309 -ErrorAction SilentlyContinue | ForEach-Object { 
        Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue 
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
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$frontendPath'; npm run electron" -WindowStyle Normal
}
else {
    Write-Host " - ERROR: No se encontró el directorio frontend en $frontendPath" -ForegroundColor Red
}

Write-Host "`n¡Chequeo completado!" -ForegroundColor Yellow
Write-Host "------------------------------------------"
Write-Host "OpenBB API: http://localhost:6900" -ForegroundColor Magenta
Write-Host "Backend:    http://localhost:8282" -ForegroundColor Cyan
Write-Host "Frontend:   http://localhost:3309" -ForegroundColor Cyan
Write-Host "Swagger UI: http://localhost:6900/docs" -ForegroundColor DarkCyan
Write-Host "------------------------------------------"
