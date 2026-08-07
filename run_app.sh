#!/bin/bash

# run_app.sh
# Script inteligente para correr AssetManager en WSL/Linux
# PUERTOS: OpenBB API (6900), Portfolio C++ (9092), Backend (8282), Frontend (3309)

# Colores
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

clear
echo -e "${YELLOW}==========================================${NC}"
echo -e "${CYAN}   AssetManager: Sistema Inteligente      ${NC}"
echo -e "${YELLOW}==========================================${NC}"

ROOT_PATH=$(pwd)
BACKEND_PATH="$ROOT_PATH/backend"
FRONTEND_PATH="$ROOT_PATH/frontend"
OPENBB_PATH="$ROOT_PATH/external_repos/OpenBB/OpenBB"
PORTFOLIO_CPP_PORT=9092
PORTFOLIO_CPP_URL="http://127.0.0.1:$PORTFOLIO_CPP_PORT"

# Función para verificar si un puerto está en uso
test_port_in_use() {
    ss -tuln | grep -q ":$1 "
    return $?
}

# --- OpenBB API Server (Puerto 6900) ---
echo -e "\n${WHITE}[1/4] Verificando OpenBB API Server (Puerto 6900)...${NC}"
OPENBB_VENV="$OPENBB_PATH/.venv/bin/activate"

if [ -f "$OPENBB_VENV" ]; then
    if test_port_in_use 6900; then
        echo -e " - OpenBB API ya corriendo en puerto 6900."
    else
        echo -e " - Iniciando OpenBB API Server en nueva pestaña..."
        wt.exe nt --title "OpenBB API" wsl.exe -d Ubuntu bash -c "cd '$OPENBB_PATH' && source '$OPENBB_VENV' && uvicorn openbb_core.api.rest_api:app --host 0.0.0.0 --port 6900; read"
        echo -e " - OpenBB API se está calentando (puede tardar ~10s)."
        sleep 3
    fi
else
    echo -e " - AVISO: OpenBB .venv no encontrado en $OPENBB_VENV"
    echo -e "   El terminal usará el modo subprocess como fallback."
fi

# --- Portfolio C++ Service (Puerto 9092) ---
echo -e "\n${WHITE}[2/4] Verificando Portfolio C++ Service (Puerto 9092)...${NC}"
if test_port_in_use 9092; then
    echo -e " - Portfolio C++ Service ya corriendo."
    PORTFOLIO_CPP_READY=true
else
    echo -e " - AVISO: Portfolio C++ Service no detectado en el puerto 9092."
    PORTFOLIO_CPP_READY=false
fi

# --- Backend (Puerto 8282) ---
echo -e "\n${WHITE}[3/4] Verificando Backend (Puerto 8282)...${NC}"
if test_port_in_use 8282; then
    echo -e " - ¡Puerto 8282 ocupado! Matando proceso anterior..."
    fuser -k 8282/tcp 2>/dev/null
    sleep 2
fi

echo -e " - Iniciando Backend (FastAPI) en nueva pestaña..."
BACKEND_PYTHON="$BACKEND_PATH/venv/bin/python"
if [ -f "$BACKEND_PYTHON" ]; then
    BACKEND_ENV_VAR=""
    if [ "$PORTFOLIO_CPP_READY" = true ]; then
        BACKEND_ENV_VAR="export PORTFOLIO_CPP_SERVICE_URL=$PORTFOLIO_CPP_URL && "
    fi
    wt.exe nt --title "AssetManager Backend" wsl.exe -d Ubuntu bash -c "cd '$BACKEND_PATH' && ${BACKEND_ENV_VAR} ./venv/bin/python -m uvicorn app.main:sio_app --reload --host 0.0.0.0 --port 8282; read"
    echo -e " - Pestaña de Backend abierta."
else
    echo -e " - ${RED}ERROR: No se encontró el Python del entorno virtual en $BACKEND_PYTHON${NC}"
fi

# --- Frontend (Puerto 3309) ---
echo -e "\n${WHITE}[4/4] Verificando Frontend (Puerto 3309)...${NC}"
if test_port_in_use 3309; then
    echo -e " - ¡Puerto 3309 ocupado! Matando proceso anterior..."
    fuser -k 3309/tcp 2>/dev/null
    sleep 2
fi

echo -e " - Iniciando Frontend y Electron en nueva pestaña..."
if [ -d "$FRONTEND_PATH" ]; then
    wt.exe nt --title "AssetManager UI & Electron" wsl.exe -d Ubuntu bash -c "cd '$FRONTEND_PATH' && npm run electron; read"
    echo -e " - Pestaña de Frontend abierta."
else
    echo -e " - ${RED}ERROR: No se encontró el directorio frontend en $FRONTEND_PATH${NC}"
fi

echo -e "\n${YELLOW}¡Chequeo completado!${NC}"
echo -e "------------------------------------------"
echo -e "OpenBB API: http://localhost:6900"
echo -e "Backend:    http://localhost:8282"
echo -e "Frontend:   http://localhost:3309"
echo -e "------------------------------------------"
