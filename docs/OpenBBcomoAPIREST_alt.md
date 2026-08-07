# Guía: Usar OpenBB como API REST 

Esta guía explica cómo levantar la plataforma OpenBB como un servidor REST local. Esto permite interactuar con OpenBB desde cualquier otro lenguaje de programación (Node.js, C#, Go, etc.) o software externo mediante solicitudes HTTP y usarlo como una excelente interfaz para Agentes de IA.

## 1. Requisitos previos

Asegúrate de tener instalado el paquete base de OpenBB y un servidor ASGI como `uvicorn` en tu entorno de Python (si instalaste OpenBB Platform, es probable que ya los tengas):

```bash
pip install openbb uvicorn
```

## 2. Levantar el servidor de la API

FastAPI genera rutinariamente una API por debajo de toda la plataforma OpenBB. Para iniciar el servidor de manera local ejecuta el siguiente comando en tu terminal:

```bash
# Estando en el entorno virtual de openbb (.venv)
uvicorn openbb_core.api.router:app --host 0.0.0.0 --port 8000
```

*Nota: Dependiendo de tu instalación de OpenBB, el path exacto de la aplicación FastAPI puede variar. En las versiones más recientes de la Plataforma OpenBB (v4+), la API se sirve a través del paquete `openbb-core`.*

## 3. Documentación interactiva (Swagger UI)

Una vez que el servidor esté en ejecución, abre tu navegador web y ve a:

*   **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
*   **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

Aquí verás todos los endpoints generados automáticamente a partir de los comandos de OpenBB. Podrás testearlos directamente desde el navegador y ver qué parámetros requiere cada uno.

## 4. Ejemplos de Consumo de la API

### Desde la línea de comandos (cURL)

Obtener la cotización de Apple (AAPL) usando el proveedor de finanzas predeterminado:

```bash
curl -X 'GET' \
  'http://localhost:8000/api/v1/equity/price/quote?symbol=AAPL' \
  -H 'accept: application/json'
```

### Desde Node.js / JavaScript (Fetch API)

```javascript
async function obtenerPrecio(symbol) {
  try {
    const response = await fetch(`http://localhost:8000/api/v1/equity/price/quote?symbol=${symbol}`);
    if (!response.ok) {
      throw new Error(`Error HTTP: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error("Error al obtener datos:", error);
  }
}

obtenerPrecio("MSFT");
```

## 5. Integración con Agentes de IA

Si tienes agentes externos (ej. escritos en TypeScript con LangChain.js, AutoGen, CrewAI, o desde otra red de tu servidor), proveerles este servidor como interfaz es la forma más estructurada:

### Las Ventajas:
1.  **Desacoplamiento:** El agente y OpenBB no necesitan estar en el mismo entorno ni lenguaje.
2.  **Seguridad:** Puedes usar un Reverse Proxy delante de uvicorn para restringir y securizar a qué endpoints (rutas HTTP) tiene acceso el agente.
3.  **Llamada a la Acción Perfecta (Function Calling):** Al usar FastAPI/Swagger, OpenBB expone un esquema OpenAPI oficial en `http://localhost:8000/openapi.json`. Puedes descargar o apuntar tu framework de LLM a este JSON para generar **automáticamente** cientos de herramientas (tools) compatibles con los modelos más recientes (OpenAI, Anthropic, Ollama, etc) sin que tengas que programar ni wrappear comandos de una CLI manualmente.

### Ejemplo conceptual con LangChain:
Ciertas librerías como LangChain soportan la ingesta de JSON de OpenAPI para convertir los Endpoints de REST al Formato de Herramientas Estructuradas de la IA automáticamente.

```python
from langchain.agents.agent_toolkits.openapi import planner
from langchain.requests import RequestsWrapper

requests_wrapper = RequestsWrapper()
# Tu agente leerá el esquema y sabrá todos los endpoints de Openbb disponibles.
agent = planner.create_openapi_agent(
    openapi_url="http://localhost:8000/openapi.json",
    requests_wrapper=requests_wrapper,
    llm=tu_llm_model 
)

agent.invoke("What is the current stock price of AAPL through the OpenBB rest api?")
```
