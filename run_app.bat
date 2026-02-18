@echo off
TITLE AssetManager Smart Launcher
echo ==========================================
echo    AssetManager: Sistema Inteligente      
echo ==========================================

:: Verificar Backend (Puerto 8282)
netstat -ano | findstr :8282 | findstr LISTENING >nul
if %errorlevel% equ 0 (
    echo [1/2] Backend ya esta corriendo en el puerto 8282. Saltando...
) else (
    echo [1/2] Iniciando Backend en puerto 8282...
    start cmd /k "cd backend && venv\Scripts\activate && uvicorn app.main:sio_app --reload --host 0.0.0.0 --port 8282"
)

:: Verificar Frontend (Puerto 3309)
netstat -ano | findstr :3309 | findstr LISTENING >nul
if %errorlevel% equ 0 (
    echo [2/2] Frontend/Electron ya esta corriendo en el puerto 3309. Saltando...
) else (
    echo [2/2] Iniciando Frontend y Electron en puerto 3309...
    start cmd /k "cd frontend && npm run electron"
)

echo.
echo Chequeo completado.
echo Backend:  http://localhost:8282
echo Frontend: http://localhost:3309
echo ==========================================
pause
