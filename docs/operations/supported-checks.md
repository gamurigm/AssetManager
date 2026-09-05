# Supported Checks

Run these checks from the repository root. They use the project virtual
environment and keep optional brokers, Kafka and schedulers disabled.

## Backend

```powershell
$env:PYTHONPATH=(Resolve-Path "backend").Path
$env:API_ENABLE_KAFKA_FANOUT="false"
$env:API_ENABLE_SCHEDULER="false"
$env:API_ENABLE_BROKER_CONNECTIONS="false"
& "backend\venv\Scripts\python.exe" -m pytest backend\tests -q
```

Import and health checks:

```powershell
& "backend\venv\Scripts\python.exe" -c "import app.main; print('API_IMPORT_OK')"
```

## Frontend

```powershell
Push-Location frontend
npm run typecheck
npm run lint:critical
npm run test
npm run build
Pop-Location
```

Files under `backend/tests/` that are excluded by `conftest.py` are manual,
live-provider, optional-native-extension or diagnostic checks. Run those
explicitly only when their external prerequisites are configured.