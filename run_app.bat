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

:: --- Backend (Puerto 8282) ---
echo.
echo %White%[1/2] Verificando Backend (Puerto 8282)...%Reset%
netstat -ano | findstr :8282 | findstr LISTENING >nul
if %errorlevel% equ 0 (
    echo %Red% - ¡Puerto 8282 ocupado! Matando proceso anterior...%Reset%
    for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8282 ^| findstr LISTENING') do taskkill /F /PID %%a >nul 2>&1
    timeout /t 2 /nobreak >nul
)

echo %Green% - Iniciando Backend (FastAPI)...%Reset%
if exist "backend\venv\Scripts\activate.bat" (
    start "AssetManager Backend" cmd /k "cd backend && venv\Scripts\activate && uvicorn app.main:sio_app --reload --host 0.0.0.0 --port 8282"
) else (
    echo %Red% - ERROR: No se encontró el entorno virtual en backend\venv%Reset%
)

:: --- Frontend (Puerto 3309) ---
echo.
echo %White%[2/2] Verificando Frontend (Puerto 3309)...%Reset%
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

echo.
echo %Yellow%¡Chequeo completado!%Reset%
echo ------------------------------------------
echo %Cyan%Backend: http://localhost:8282%Reset%
echo %Cyan%Frontend: http://localhost:3309%Reset%
echo ------------------------------------------
pause
