# 🧠 HMM Market Regime Detection

> Documentación técnica del módulo de detección de regímenes de mercado usando Hidden Markov Models (HMM).

---

## ¿Qué es esto?

Este módulo implementa un **Hidden Markov Model (HMM)** para detectar automáticamente el **régimen de mercado actual** de cualquier activo financiero. Clasifica el mercado en uno de tres estados latentes:

| Régimen | Descripción |
|---|---|
| 🟢 **Bullish** | Retornos positivos, volatilidad baja/media. Tendencia alcista. |
| 🔴 **Bearish** | Retornos negativos, volatilidad alta. Tendencia bajista o crash. |
| 🟡 **Neutral/Choppy** | Retornos cercanos a cero, volatilidad mixta. Mercado lateral. |

El modelo aprende estos estados de forma **no supervisada** a partir de datos históricos OHLCV, sin necesidad de etiquetas manuales.

---

## Arquitectura

```
backend/
├── app/
│   ├── analytics/
│   │   ├── __init__.py
│   │   └── models/
│   │       ├── __init__.py
│   │       └── hmm.py                  ← Lógica central del HMM
│   ├── api/
│   │   └── routes/
│   │       └── analytics.py            ← Endpoint REST
│   └── agents/
│       └── team/
│           └── orchestrator.py         ← Inyección de contexto al AI Agent
```

---

## Cómo funciona

### 1. Features de entrada

El modelo extrae **3 features** de los datos OHLCV para cada barra diaria:

| Feature | Fórmula | Descripción |
|---|---|---|
| **Log Return** | `ln(Pt / Pt-1)` | Retorno logarítmico diario |
| **Range Volatility** | `(High - Low) / Close` | Volatilidad intradía normalizada |
| **Volume Change** | `ln(Vt / Vt-1)` | Cambio logarítmico en volumen |

### 2. Modelo

- **Tipo**: `GaussianHMM` (distribuciones de emisión Gaussianas)
- **Componentes**: 3 estados ocultos (Bull, Bear, Neutral)
- **Covarianza**: `full` (matriz de covarianza completa por estado)
- **Iteraciones**: 100 pasos de Baum-Welch (EM)

### 3. Interpretación de estados

Después del entrenamiento, los estados se etiquetan **dinámicamente** analizando las medias de cada estado:

```
Estado con mayor retorno medio  → Bullish
Estado con menor retorno medio  → Bearish
Estado restante                 → Neutral/Choppy
```

Esto hace que el modelo sea **adaptativo**: cada activo define sus propios umbrales de régimen según su historia de volatilidad.

---

## API REST

### Endpoint

```
GET /api/v1/analytics/regime/{symbol}
```

### Parámetros

| Parámetro | Tipo | Descripción |
|---|---|---|
| `symbol` | `string` (path) | Ticker del activo (ej: `AAPL`, `BTC-USD`, `SPY`) |

### Ejemplo de request

```bash
curl http://localhost:8282/api/v1/analytics/regime/AAPL
```

### Ejemplo de respuesta

```json
{
  "symbol": "AAPL",
  "regime_analysis": {
    "current_regime": "Bullish",
    "current_state_id": 2,
    "regime_probs": {
      "Bearish": 0.03,
      "Neutral/Choppy": 0.11,
      "Bullish": 0.86
    },
    "state_definitions": {
      "0": "Bearish",
      "1": "Neutral/Choppy",
      "2": "Bullish"
    },
    "means": [
      [-0.012, 0.031, -0.05],
      [0.001, 0.018, 0.02],
      [0.009, 0.015, 0.04]
    ]
  },
  "data_source": "DuckDB (Synced)",
  "data_points_analyzed": 500
}
```

### Campos de la respuesta

| Campo | Descripción |
|---|---|
| `current_regime` | Régimen actual: `"Bullish"`, `"Bearish"` o `"Neutral/Choppy"` |
| `current_state_id` | ID numérico del estado (0, 1 o 2) |
| `regime_probs` | Probabilidades posteriores para cada régimen en el último día |
| `state_definitions` | Mapeo de ID → nombre de régimen aprendido por el modelo |
| `means` | Medias de cada feature por estado (para interpretación) |
| `data_points_analyzed` | Número de velas usadas para el análisis |

---

## Integración con el AI Agent

El régimen de mercado se puede inyectar como **contexto** al AI Agent para que sus respuestas sean conscientes del estado actual del mercado.

### Flujo completo

```
Frontend → GET /analytics/regime/AAPL → Obtiene régimen
Frontend → POST /agents/chat           → Envía régimen en el body
Orchestrator → Inyecta en system prompt → AI responde con contexto
```

### Body del chat con régimen

```json
POST /api/v1/agents/chat
{
  "message": "¿Debería aumentar mi posición en AAPL?",
  "user_id": 1,
  "portfolio": {
    "total_value": 50000,
    "total_pnl": 3200,
    "pnl_percent": 6.8,
    "holdings": [
      {
        "symbol": "AAPL",
        "shares": 10,
        "price": 195.50,
        "changePercent": 1.2
      }
    ]
  },
  "market_regime": {
    "symbol": "AAPL",
    "regime_analysis": {
      "current_regime": "Bullish",
      "regime_probs": {
        "Bearish": 0.03,
        "Neutral/Choppy": 0.11,
        "Bullish": 0.86
      }
    }
  }
}
```

El AI Agent recibirá en su system prompt algo como:

```
## 🧠 MARKET REGIME ANALYSIS (AAPL)
**Current State:** Bullish
**Details:** {
  "current_regime": "Bullish",
  "regime_probs": { "Bearish": 0.03, "Neutral/Choppy": 0.11, "Bullish": 0.86 }
}
```

---

## Integración en el Frontend (Next.js)

### Ejemplo de hook

```typescript
// hooks/useMarketRegime.ts
import { useState, useEffect } from 'react';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8282';

export function useMarketRegime(symbol: string) {
  const [regime, setRegime] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!symbol) return;
    setLoading(true);
    fetch(`${API_BASE}/api/v1/analytics/regime/${symbol}`)
      .then(res => res.json())
      .then(data => setRegime(data))
      .finally(() => setLoading(false));
  }, [symbol]);

  return { regime, loading };
}
```

### Ejemplo de uso en el chat

```typescript
// Cuando el usuario envía un mensaje al AI Agent
const sendMessage = async (message: string) => {
  const regimeData = await fetch(`${API_BASE}/api/v1/analytics/regime/${activeSymbol}`)
    .then(res => res.json());

  const response = await fetch(`${API_BASE}/api/v1/agents/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message,
      user_id: currentUser.id,
      portfolio: portfolioData,
      market_regime: regimeData  // ← Inyectar régimen aquí
    })
  });

  // Leer stream de respuesta...
};
```

---

## Dependencias

Añadidas a `requirements.txt`:

```
hmmlearn      # Implementación de HMM (Baum-Welch, Viterbi)
scikit-learn  # Preprocesamiento y utilidades estadísticas
```

Instalar:

```bash
cd backend
pip install -r requirements.txt
```

---

## Limitaciones y consideraciones

| Consideración | Detalle |
|---|---|
| **Datos mínimos** | Se requieren al menos **50 velas** para entrenar el modelo. |
| **Re-entrenamiento** | El modelo se re-entrena en cada request. No hay persistencia del modelo. Esto es intencional: cada activo define sus propios regímenes relativos. |
| **Estacionariedad** | El HMM asume que las transiciones son estacionarias. En mercados extremos (COVID crash, etc.) los estados pueden ser inestables. |
| **Etiquetado dinámico** | Las etiquetas (Bull/Bear/Neutral) se asignan por heurística de retornos. En activos muy volátiles (crypto), el "Bullish" puede tener alta volatilidad también. |
| **Latencia** | El entrenamiento tarda ~100-500ms dependiendo del número de velas. Se recomienda llamar al endpoint antes de abrir el chat. |

---

## Archivos modificados

| Archivo | Cambio |
|---|---|
| `backend/requirements.txt` | Añadido `hmmlearn`, `scikit-learn` |
| `backend/app/analytics/__init__.py` | Nuevo módulo |
| `backend/app/analytics/models/__init__.py` | Nuevo módulo |
| `backend/app/analytics/models/hmm.py` | **Nuevo** — Lógica del HMM |
| `backend/app/api/routes/analytics.py` | **Nuevo** — Endpoint REST |
| `backend/app/main.py` | Registro del router de analytics |
| `backend/app/api/routes/agents.py` | `ChatRequest` + `_build_context` actualizados |
| `backend/app/agents/team/orchestrator.py` | `run_stream` actualizado para inyectar régimen |
