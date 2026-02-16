# AI Asset Manager

Sistema de gestión de activos con arquitectura agéntica, backend en FastAPI, frontend en Next.js y núcleo de baja latencia en C++.

## Estructura
- `/frontend`: Next.js 15 + TSX + Socket.IO Client
- `/backend`: FastAPI + Pydantic AI + SQLAlchemy + Socket.IO Server
- `/core_engine`: C++ (pybind11 + Boost.Asio)

## Requisitos
- Python 3.10+
- Node.js 18+
- C++ Compiler (MSVC/GCC) + CMake (para el core engine)
- PostgreSQL (opcional, configurado en .env)

## Configuración Inicial
1. Copia `.env.example` a `.env` y añade tus keys (NVIDIA NIM es crucial para la IA).
2. **Backend**:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # o venv\Scripts\activate en Windows
   pip install -r requirements.txt
   python -m app.main
   ```
3. **Frontend**:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Estado Actual
- ✅ Scaffolding del monorepo completado.
- ✅ Backend: Modelos de DB, Auth, Socket.IO y Agente General listos.
- ✅ Frontend: Dashboard de cliente y Trading UI con integración real-time básica.
- ✅ Core Engine: Estructura C++ y bindings preparados.
