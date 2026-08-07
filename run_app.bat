@echo off
SETLOCAL EnableDelayedExpansion
TITLE AssetManager - Smart Launcher

:: ANSI Colors (Windows 10+)
set "ESC="
set "Yellow=%ESC%[33m"
set "Cyan=%ESC%[36m"
set "White=%ESC%[37m"
set "Red=%ESC%[31m"
set "Green=%ESC%[32m"
set "Reset=%ESC%[0m"

echo %Yellow%==========================================%Reset%
echo %Cyan%   AssetManager: Sistema Inteligente      %Reset%
echo %Yellow%==========================================%Reset%

set "PORTFOLIO_CPP_SERVICE_URL="

:: --- Portfolio C++ Service (Puerto 9095) ---
echo.
echo %White%[1/6] Verificando Portfolio C++ Service (Puerto 9095)...%Reset%
powershell -ExecutionPolicy Bypass -File "%~dp0run_portfolio_cpp_service.ps1" -Port 9095 -WindowStyle Minimized >nul
if %errorlevel% equ 0 (
    set "PORTFOLIO_CPP_SERVICE_URL=http://127.0.0.1:9095"
    echo %Green% - Portfolio C++ listo en %PORTFOLIO_CPP_SERVICE_URL%%Reset%
) else (
    echo %Yellow% - AVISO: No se pudo iniciar portfolio_cpp_service. Se usara fallback embebido o Python.%Reset%
)

:: --- Backend (Puerto 8282) ---
echo.
echo %White%[2/6] Verificando Backend (Puerto 8282)...%Reset%
netstat -ano | findstr :8282 | findstr LISTENING >nul
if %errorlevel% equ 0 (
    echo %Red% - ¡Puerto 8282 ocupado! Matando proceso anterior...%Reset%
    for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8282 ^| findstr LISTENING') do taskkill /F /PID %%a >nul 2>&1
    timeout /t 2 /nobreak >nul
)

echo %Green% - Iniciando Backend (FastAPI)...%Reset%
if exist "backend\venv\Scripts\python.exe" (
    start "AssetManager Backend" cmd /k "cd backend && set PORTFOLIO_CPP_SERVICE_URL=%PORTFOLIO_CPP_SERVICE_URL% && venv\Scripts\python.exe -m uvicorn app.main:sio_app --reload --host 0.0.0.0 --port 8282"
) else (
    echo %Red% - ERROR: No se encontró backend\venv\Scripts\python.exe%Reset%
)

:: --- Frontend (Puerto 3309) ---
echo.
echo %White%[3/6] Verificando Frontend (Puerto 3309)...%Reset%
netstat -ano | findstr :3309 | findstr LISTENING >nul
if %errorlevel% equ 0 (
    echo %Red% - ¡Puerto 3309 ocupado! Matando proceso anterior...%Reset%
    for /f "tokens=5" %%a in ('netstat -aon ^| findstr :3309 ^| findstr LISTENING') do taskkill /F /PID %%a >nul 2>&1
    
    <nul set /p="%White% - Esperando liberacion de recursos...%Reset%"
    set /a retries=0
)

:wait_loop
netstat -ano | findstr :3309 | findstr LISTENING >nul
if %errorlevel% equ 0 (
    if !retries! lss 10 (
        set /a retries+=1
        <nul set /p="."
        timeout /t 1 /nobreak >nul
        goto wait_loop
    )
)
if "!retries!" neq "" (
    echo %Green% Listo.%Reset%
)

echo %Green% - Iniciando Frontend y Electron...%Reset%
if exist "frontend" (
    start "AssetManager Frontend" cmd /k "cd frontend && npm run electron"
) else (
    echo %Red% - ERROR: No se encontró el directorio frontend%Reset%
)

:: --- Microservicios de Mercado ---
echo.
echo %White%[4/6] Iniciando Market Data Gateway...%Reset%
start "Market Gateway" cmd /k "set PYTHONUTF8=1 && cd backend && venv\Scripts\python.exe services\market_data_gateway\main.py"

echo %White%[5/6] Iniciando Storage Service (Data Lake)...%Reset%
start "Storage Service" cmd /k "set PYTHONUTF8=1 && cd backend && venv\Scripts\python.exe services\storage_service\main.py"

echo %White%[6/6] Iniciando Strategy Engine (Live Trading)...%Reset%
start "Strategy Engine" cmd /k "set PYTHONUTF8=1 && cd backend && venv\Scripts\python.exe services\strategy_engine\main.py"

echo.
echo %Yellow%¡Chequeo completado!%Reset%
echo ------------------------------------------
if defined PORTFOLIO_CPP_SERVICE_URL (
    echo %Cyan%Portfolio C++: %PORTFOLIO_CPP_SERVICE_URL%%Reset%
) else (
    echo %Yellow%Portfolio C++: fallback a C++ embebido / Python%Reset%
)
echo %Cyan%Backend: http://localhost:8282%Reset%
echo %Cyan%Frontend: http://localhost:3309%Reset%
echo ------------------------------------------
pause
