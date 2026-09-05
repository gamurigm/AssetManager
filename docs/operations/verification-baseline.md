# Línea base de verificación

Fecha: 2026-09-05.

Esta línea base registra la etapa P0 sin atribuir cambios previos del árbol a esta reorganización.

| Control | Resultado | Observación |
| --- | --- | --- |
| TypeScript (`frontend/npm run typecheck`) | Pasa | El frontend compila tipos sin emitir archivos. |
| ESLint crítico (`frontend/npm run lint:critical`) | Pasa | No se reportaron errores en los archivos protegidos por CI. |
| Import mínimo (`backend/venv/Scripts/python.exe -c "import app"`) | Pasa | El paquete base importa correctamente. |
| Import del entrypoint (`import app.main`) | Pasa | El import es offline y no carga Kafka ni APScheduler cuando esas funciones están deshabilitadas. |
| Suite backend (`pytest backend/tests -q`) | Pasa | 200 tests pasan sin credenciales externas; los diagnósticos manuales permanecen excluidos por `conftest.py`. |
| `git diff --check` | Pasa | Sin errores de espacios en los cambios visibles. |
| Referencias operativas a puerto 8000 | Corregidas | Las guías y diagnósticos operativos usan 8282; el diagnóstico de arquitectura conserva la mención histórica explicativa. |

## Reproducción segura

Desde la raíz del repositorio:

```powershell
Push-Location backend
& .\venv\Scripts\python.exe -c "import app; print('APP_IMPORT_OK')"
Pop-Location

Push-Location frontend
npm run typecheck
npm run lint:critical
Pop-Location
```

La importación de `app.main` y la recolección de pytest no deben ejecutarse con credenciales o servicios reales como solución al bloqueo. El siguiente trabajo P0 es aislar qué import del entrypoint deja el proceso activo, probablemente separando inicialización de recursos y adaptadores de broker del registro de rutas.
