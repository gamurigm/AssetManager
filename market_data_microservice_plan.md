# Pasos para Extraer el Market Data Gateway

El objetivo es extraer el módulo [backend/app/services/market_data.py](file:///c:/AssetManager/backend/app/services/market_data.py) de FastAPI y convertirlo en un microservicio de ingestión (Ingestor) que corra en su propio proceso independiente y publique exclusivamente hacia el bus de Kafka.

## Nivel 1: El Publicador (Productor)

El primer paso no es borrar el código actual, sino crear un script paralelo (el microservicio) que use el código existente pero en un bucle infinito ("Daemon"):

1. **Crear el Microservicio:**
   Crearemos una carpeta nueva `backend/services/market_data_gateway/` con un script principal `main.py`.
   
2. **Ciclo de Ingestión (El "Heartbeat"):**
   Este script tendrá una lista de símbolos suscritos (ej. `['AAPL', 'TSLA', 'SPY']`).
   Cada N segundos, hará la llamada [get_price(symbol)](file:///c:/AssetManager/backend/app/services/market_data.py#104-209) usando el `market_data_service` existente.

3. **Publicación en Kafka:**
   En lugar de devolver el precio con un `return` para que FastAPI lo responda en una petición HTTP, el microservicio tomará el diccionario de precio, lo convertirá a JSON, y hará un `producer.produce(topic=f"market.ticks.{symbol}", value=json)`.

## Nivel 2: Refactorizar el Monolito (FastAPI)

Una vez que el microservicio de Market Data está corriendo de fondo llenando Kafka de precios frescos como un río, el backend actual (FastAPI) debe dejar de llamar a Yahoo Finance / Polygon directamente.

1. **El Consumidor del Backend:**
   En FastAPI, cuando un cliente abra la página web y por WebSockets pida "Dime el precio de Apple", FastAPI ya no ejecutará [get_price("AAPL")](file:///c:/AssetManager/backend/app/services/market_data.py#104-209).
   En su lugar, FastAPI tendrá un hilo secundario trabajando como consumidor de Kafka (`consumer.subscribe(['market.ticks.*'])`).
   Cada vez que FastAPI escuche un precio nuevo por Kafka, simplemente lo reenviará (broadcast) por Socket.IO al frontend.

## Nivel 3: Aislamiento Físico

1. **Separación de Dependencias:**
   Actualmente el `market_data_service` importa el `duckdb_store`. En una arquitectura de microservicios pura, el **Market Data Gateway** NO debería hablar con la base de datos.
   Su único trabajo es "escupir" datos a Kafka.
   El encargado de guardar en DuckDB será el **Storage Service** (otro microservicio que solo escucha a Kafka y guarda en disco).

2. **Contenedorización:**
   Se creará un `Dockerfile` específico para el Market Data Gateway. Podremos encenderlo y apagarlo independientemente de FastAPI y de la Base de Datos.

---

### Siguiente Acción Recomendada:
Te propongo que comencemos con el **Nivel 1**. Programaré el daemon del Market Data Gateway para que empiece a streamear (transmitir) automáticamente los precios en vivo de algunas acciones a nuestro nuevo servidor de Kafka que instalaste. ¿Procedemos?
