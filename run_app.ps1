# run_app.ps1
# Script inteligente para correr AssetManager (Backend + Frontend + Electron)
# PUERTOS ACTUALIZADOS: Backend (8282), Frontend (3309)

Clear-Host
$host.UI.RawUI.WindowTitle = "AssetManager - Smart Launcher"

Write-Host "==========================================" -ForegroundColor Yellow
Write-Host "   AssetManager: Sistema Inteligente      " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Yellow

$rootPath = $PSScriptRoot
$backendPath = Join-Path $rootPath "backend"
$frontendPath = Join-Path $rootPath "frontend"

# Función para verificar si un puerto está en uso
function Test-PortInUse($port) {
    return Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue
}

# --- Backend (Puerto 8282) ---
Write-Host "`n[1/2] Verificando Backend (Puerto 8282)..." -ForegroundColor White
if (Test-PortInUse 8282) {
    Write-Host " - ¡Backend ya está corriendo en el puerto 8282! Saltando..." -ForegroundColor Yellow
}
else {
    Write-Host " - Iniciando Backend (FastAPI)..." -ForegroundColor Green
    $venvPath = Join-Path $backendPath "venv\Scripts\Activate.ps1"
    if (Test-Path $venvPath) {
        Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$backendPath'; & '$venvPath'; uvicorn app.main:sio_app --reload --host 0.0.0.0 --port 8282" -WindowStyle Normal
    }
    else {
        Write-Host " - ERROR: No se encontró el entorno virtual en $venvPath" -ForegroundColor Red
    }
}

# --- Frontend (Puerto 3309) ---
Write-Host "[2/2] Verificando Frontend (Puerto 3309)..." -ForegroundColor White
if (Test-PortInUse 3309) {
    Write-Host " - ¡Frontend/Electron ya parece estar corriendo en el puerto 3309! Saltando..." -ForegroundColor Yellow
}
else {
    Write-Host " - Iniciando Frontend y Electron..." -ForegroundColor Green
    if (Test-Path $frontendPath) {
        Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$frontendPath'; npm run electron" -WindowStyle Normal
    }
    else {
        Write-Host " - ERROR: No se encontró el directorio frontend en $frontendPath" -ForegroundColor Red
    }
}

Write-Host "`n¡Chequeo completado!" -ForegroundColor Yellow
Write-Host "------------------------------------------"
Write-Host "Backend: http://localhost:8282" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:3309" -ForegroundColor Cyan
Write-Host "------------------------------------------"
