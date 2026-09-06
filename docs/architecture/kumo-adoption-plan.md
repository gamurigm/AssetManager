# Plan de adopción de Kumo en AssetManager

Estado: propuesta, pendiente de implementación.

Este documento recoge el plan elaborado a partir de la revisión de AssetManager y de `C:\Users\gamur\Documents\API_Server`. La arquitectura objetivo considera a AssetManager consumidor de las APIs publicadas por API_Server. Kumo se incorpora para emular S3 en desarrollo y pruebas, almacenando reportes y artefactos de simulación mediante un adaptador intercambiable.

La revisión cubre código y documentación local; no verifica la configuración desplegada, el catálogo activo, credenciales ni llamadas reales entre ambos proyectos. Las variables y clases propuestas aquí están pendientes de implementación.

## 1. Diagnóstico del repositorio

AssetManager ya tiene una arquitectura distribuida:

```text
market-data :8291
    ├── adaptadores de proveedores (consumo vía API_Server por verificar)
    ├── DuckDB market_data.duckdb
    └── Kafka outbox

analysis :8292
    └── estrategias y señales

api :8282
    ├── FastAPI
    ├── Socket.IO
    ├── reportes PDF
    └── simulaciones en memoria

execution-gateway :8293
    └── MT5, idempotencia y reconciliación
```

Hallazgos relevantes:

- Kafka ya es el bus de eventos, con confirmación manual, reintentos y DLQ.
- `MarketDataStore` implementa un outbox transaccional sobre DuckDB.
- La arquitectura exige un único escritor para `market_data.duckdb`.
- Las simulaciones usan `asyncio.create_task()` e `InMemorySimulationJobStore`.
- Los reportes PDF se generan en `reports/` y se sirven mediante `/view-reports/{filename}`.
- Las credenciales cuentan con `SecureIntegrationStore`, cifrado AES-256-GCM y el volumen `secure_config`.
- Docker Compose administra Kafka, `market-data`, `analysis` y `api`.
- Los archivos de dependencias revisados no incluyen un SDK de AWS.

Referencias locales:

- [Arquitectura de microservicios](microservices.md).
- [Seguridad y calidad](security-and-quality.md).
- [Docker Compose](../../docker-compose.yml).
- [Servicio de simulaciones](../../backend/app/services/simulation_service.py).
- [Estado de simulaciones](../../backend/app/services/simulation_jobs.py).
- [Servicio de reportes](../../backend/app/services/report_service.py).
- [API y descarga de reportes](../../backend/app/main.py).
- [Persistencia de ticks y outbox](../../backend/services/market_data_gateway/store.py).
- [Infraestructura Kafka](../../backend/services/platform/kafka.py).

### 1.1. API_Server y el contrato de consumo

API_Server es un gateway federado implementado con Next.js, PostgreSQL y Supabase. Sus responsabilidades verificadas son:

- Autenticar aplicaciones mediante una clave propia del gateway o JWT RS256 de un emisor registrado.
- Publicar el catálogo autorizado en `GET /api/v1/providers`.
- Enrutar llamadas por `/api/v1/gateway/{provider}/{path}` según métodos, rutas y scopes registrados.
- Recuperar credenciales de proveedores desde Supabase Vault e inyectarlas al enviar la solicitud upstream.
- Aplicar cuotas por aplicación/proveedor, límites de streams, controles de red y auditoría.
- Conservar status, cuerpo y `Content-Type` de la respuesta upstream; los errores propios del gateway usan `error.code`, `error.message` y `error.requestId`.

El proxy admite solicitudes con cuerpo JSON y streaming SSE en rutas configuradas. No implementa un transporte general de archivos, multipart o WebSocket. `proxy-utils.ts` elimina el `Authorization` del consumidor antes de inyectar la credencial upstream; los tipos de autenticación revisados no incluyen firma AWS SigV4.

Evidencia en el repositorio hermano, mediante enlaces relativos a esta ubicación:

- [README de API_Server](../../../API_Server/README.md).
- [Ejemplos de consumo](../../../API_Server/docs/client-examples.md).
- [Procesamiento del gateway](../../../API_Server/src/lib/gateway-handler.ts).
- [Construcción de URLs, headers y credenciales](../../../API_Server/src/lib/proxy-utils.ts).
- [Tipos y límites de cuerpos](../../../API_Server/src/lib/body-limits.ts).
- [Verificación de claves de aplicaciones](../../../API_Server/src/lib/api-keys.ts).
- [Catálogo de proveedores](../../../API_Server/src/app/api/v1/providers/route.ts).

Estos enlaces requieren que ambos repositorios estén en directorios hermanos.

### 1.2. Diferencia entre la arquitectura objetivo y el código revisado

Se toma el consumo de API_Server como requisito del proyecto. En los archivos revisados de AssetManager, `config.py` todavía define URLs upstream por proveedor; `fmp_service.py` y `twelve_data_service.py` añaden `apikey` a las solicitudes. Esos puntos no prueban un consumo autenticado de API_Server. Podría existir configuración externa o integración adicional fuera de lo revisado; debe confirmarse antes de migrar llamadas.

Cambiar únicamente la URL base no completa la integración: la solicitud al gateway necesita su Bearer token y un slug/ruta permitido, mientras API_Server incorpora la credencial del proveedor. También hay que revisar las comprobaciones locales que deshabilitan un proveedor cuando falta su API key original.

### 1.3. Responsabilidades y recorrido objetivo

```text
Frontend :3309 → API/BFF :8282
                     ├── servicios de mercado/IA
                     │      → API_Server → APIs externas
                     │           └── PostgreSQL + Supabase Vault
                     └── generación/descarga de reportes
                            → ArtifactStore → filesystem o S3/Kumo :4566

Market Data :8291 → API_Server para proveedores HTTP compatibles
       └── DuckDB + outbox → Kafka → Analysis/API
Execution Gateway :8293 → integraciones de ejecución locales
```

| Componente | Responsabilidad |
| --- | --- |
| API_Server | Acceso a proveedores externos, credenciales upstream, catálogo, scopes, cuotas y auditoría del gateway |
| AssetManager | Identidad del usuario, propiedad de reportes, datos y lógica financiera, simulaciones y experiencia del frontend |
| ArtifactStore de AssetManager | Guardado y recuperación de reportes mediante filesystem o SDK S3 |
| Kumo | Endpoint S3 emulado para desarrollo y pruebas de artefactos |
| Supabase de API_Server | Estado, identidad administrativa y Vault del gateway |

Kumo no sustituye el gateway ni emula automáticamente las APIs financieras o Supabase. El SDK S3 se conecta directamente desde el backend al almacenamiento: el proxy actual de API_Server no ofrece el contrato necesario para subir PDF y firmar llamadas AWS.

## 2. Decisión de alcance

El primer uso de Kumo será emular S3 para almacenar reportes y artefactos de simulación. El consumo HTTP de proveedores se organiza a través de API_Server para las integraciones compatibles y autorizadas. Kafka y DuckDB conservan sus responsabilidades; las credenciales upstream de proveedores migrados pertenecen al Vault de API_Server.

Kumo será una dependencia opcional de desarrollo y CI. La compatibilidad con S3 se comprobará mediante las operaciones concretas utilizadas por AssetManager; superar las pruebas del emulador no garantiza por sí solo paridad con AWS.

Fuera del alcance inicial:

- Reemplazar Kafka por SQS o EventBridge.
- Reemplazar DuckDB por DynamoDB.
- Migrar `SecureIntegrationStore` a Secrets Manager.
- Subir automáticamente datos de mercado.
- Separar la ejecución de simulaciones en nuevos workers.
- Ejecutar Kumo en producción.
- Convertir API_Server en proxy S3 o añadirle subida de PDF en este entregable.

### 2.1. Fase 0 — Confirmar y completar el contrato con API_Server

Esta fase precede a la conexión de los flujos de reportes con datos obtenidos a través del gateway. La prueba aislada de S3 puede avanzar en paralelo.

1. Inventariar las llamadas de los adaptadores de mercado e IA: proceso consumidor, método, URL, query, cuerpo, autenticación, timeout y uso de streaming. Registrar qué rutas ya pasan por API_Server y cuáles siguen directas.
2. Consultar el catálogo autorizado con una identidad de prueba. Mapear cada operación a un slug y ruta existentes; el gateway mantiene el contrato original del proveedor y no crea una API financiera unificada.
3. Usar FMP o Twelve Data con respuestas sintéticas como primer caso de contrato. Verificar que la base registrada en el gateway contiene el prefijo upstream correcto y que el cliente no duplica segmentos como `/stable`.
4. Definir un transporte compartido, propuesto como `backend/app/infrastructure/http/api_server_client.py`, que reciba proveedor, ruta relativa, parámetros y cuerpo. La configuración local debe usar destinos permitidos, sin aceptar una URL arbitraria del usuario.
5. Inyectar `Authorization: Bearer <clave-del-gateway>` desde el backend. La opción inicial es una clave de aplicación con scopes mínimos; JWT RS256 queda disponible si ya existe federación validada. Una clave de aplicación no sustituye el control de propiedad del usuario dentro de AssetManager.
6. Adaptar los servicios uno por uno: retirar la inyección de claves upstream en modo gateway, conservar el parser de la respuesta del proveedor y revisar sus condiciones de disponibilidad.
7. Validar SSE de IA y cancelación cuando corresponda. Inventariar por separado `yfinance`, scraping, clientes que firman solicitudes y conexiones de brokers: no se consideran compatibles solo por cambiar una URL.

Configuración propuesta para AssetManager, exclusiva del servidor:

```env
API_SERVER_BASE_URL=http://127.0.0.1:3006
API_SERVER_AUTH_MODE=api_key
API_SERVER_API_KEY=<secreto-de-la-aplicacion-consumidora>
```

El puerto `3006` corresponde al script `dev:local` de API_Server; su `dev` habitual utiliza el puerto de Next.js. Usar el origen realmente configurado en cada entorno. No crear variables `NEXT_PUBLIC_*` para esta clave.

Los modos `direct` o `gateway` deben declararse por proveedor durante la transición. En modo gateway, un `401`, `403`, `429` o una caída de API_Server no habilita una llamada directa con una clave antigua: se respeta la política y se devuelve un error explícito. Una alternativa entre proveedores solo se utiliza si está autorizada y mantiene la prioridad de mercado del proyecto.

Tratamiento del contrato:

- Conservar `X-Gateway-Request-Id` para diagnóstico y distinguir errores del gateway de los cuerpos upstream.
- No reintentar automáticamente fallos de identidad o scopes. Para `429`, respetar `Retry-After` y un presupuesto acotado.
- Acotar reintentos de lecturas idempotentes ante indisponibilidad; evitar reintentos ciegos de POST, llamadas facturables o streams.
- Coordinar timeout del consumidor y del proveedor en el gateway. Respetar límites de tamaño y paginar históricos según las operaciones autorizadas.
- Considerar que las claves de una misma aplicación comparten cuota por proveedor; iniciar varios workers no multiplica esa cuota.
- Registrar expresamente excepciones de transporte como sesiones de brokers locales. El gateway existente no transporta sus protocolos.

Salida de fase: matriz de operaciones aprobada por pruebas de contrato, un caso de consumo autenticado completo y diagnóstico de fallos sin credenciales upstream en AssetManager para ese caso.

## 3. Fase 1 — Perfil opcional de Docker

Añadir el servicio `kumo` al archivo `docker-compose.yml`, bajo el perfil `aws-emulator`, con un volumen independiente.

Configuración propuesta; sustituir la referencia de imagen por una versión o digest verificado antes de implementar:

```yaml
services:
  kumo:
    image: ghcr.io/sivchari/kumo:<version-o-digest-verificado>
    profiles: ["aws-emulator"]
    ports:
      - "127.0.0.1:4566:4566"
    environment:
      KUMO_LOG_LEVEL: info
      KUMO_DATA_DIR: /data
    volumes:
      - kumo_data:/data

volumes:
  kumo_data:
```

Arranque local:

```powershell
docker compose --profile aws-emulator up -d kumo
```

Criterios de aceptación:

- El puerto publicado queda limitado a `127.0.0.1`.
- El arranque habitual de AssetManager funciona sin Kumo.
- Kumo no comparte los volúmenes de Kafka, DuckDB o credenciales.
- La versión de imagen queda fijada para reproducir las pruebas.
- La comprobación de disponibilidad utiliza un endpoint u operación verificado en la versión seleccionada.
- API_Server y su Supabase se gestionan desde su propio proyecto. El perfil de Kumo no reinicializa ni comparte esas bases de datos.
- Si API_Server corre en el host y AssetManager en Docker Desktop, configurar el origen accesible mediante `host.docker.internal` y verificar el binding del servidor. `127.0.0.1` dentro del contenedor apunta al propio contenedor.

## 4. Fase 2 — Adaptador de almacenamiento de artefactos

Los puntos de integración actuales son `SimulationService._generate_pdf_report()`, `ReportService`, `settings.REPORTS_DIR` y la ruta `/view-reports/{filename}`.

Crear una abstracción con dos implementaciones:

```text
backend/app/infrastructure/artifacts/
├── __init__.py
├── artifact_store.py
├── filesystem_artifact_store.py
└── s3_artifact_store.py
```

Interfaz conceptual:

```python
class ArtifactStore(Protocol):
    async def put(
        self,
        key: str,
        content: bytes,
        content_type: str,
    ) -> None: ...

    async def get(self, key: str) -> bytes: ...

    async def delete(self, key: str) -> None: ...
```

La firma definitiva deberá incluir los metadatos necesarios para la descarga y permitir streaming o archivos temporales si el tamaño de los artefactos lo exige. Las operaciones de un SDK síncrono deberán ejecutarse fuera del bucle asíncrono de FastAPI.

`ReportService` y el generador de backtests seguirán generando los PDF. El adaptador se encargará de guardar y recuperar el artefacto final. Se debe definir la limpieza de archivos temporales y el comportamiento ante un fallo de subida antes de conectar el backend S3.

## 5. Fase 3 — Integración S3 para reportes

Configuración propuesta:

```env
ARTIFACT_STORAGE_BACKEND=filesystem
S3_ENDPOINT_URL=http://127.0.0.1:4566
S3_REGION=us-east-1
S3_BUCKET=assetmanager-reports
S3_ACCESS_KEY_ID=test
S3_SECRET_ACCESS_KEY=test
```

Estas variables son propuestas nuevas; todavía no están implementadas. Las credenciales de ejemplo son exclusivas del emulador. Para AWS real se definirá el uso de la cadena de credenciales del SDK y los roles del despliegue.

La configuración S3 es independiente de `API_SERVER_BASE_URL` y de la clave del gateway. No enviar la clave de API_Server a Kumo/S3 ni credenciales S3 al gateway. Los procesos consumidores HTTP de API_Server reciben su configuración propia; solo los procesos que almacenan artefactos necesitan acceso S3.

Desde el host, el endpoint será `http://127.0.0.1:4566`. Desde un contenedor de la misma red de Compose será `http://kumo:4566`. Verificar el direccionamiento S3 por ruta con el SDK seleccionado.

Flujo previsto:

```text
POST /portfolios/report o simulación
        ↓
Generación del PDF
        ↓
ArtifactStore.put()
        ↓
Filesystem o S3/Kumo
        ↓
URL de descarga autenticada
```

El frontend conservará el contrato de descarga del backend. La elección de almacenamiento será interna.

Antes de implementar:

- Seleccionar y fijar versiones compatibles del SDK y sus dependencias.
- Añadir la dependencia únicamente a los entornos que usan el adaptador.
- Mantener filesystem como opción predeterminada.
- Definir errores de almacenamiento y el tratamiento de reportes cuya subida falle.
- Evitar un cambio silencioso a filesystem cuando S3 esté configurado y no responda.

## 6. Fase 4 — Contrato de descarga y propiedad

Adaptar `/view-reports/{filename}` para recuperar archivos mediante `ArtifactStore` y conservar compatibilidad con las URL existentes.

```text
GET /view-reports/{filename}
        ↓
Verificar identidad y propiedad
        ↓
Resolver clave interna del artefacto
        ↓
ArtifactStore.get()
        ↓
Respuesta de descarga
```

Criterios de aceptación:

- La propiedad se resuelve en el servidor a partir del usuario autenticado.
- Se rechazan rutas arbitrarias y secuencias como `../`.
- Un usuario no puede descargar reportes de otro usuario.
- El bucket no se expone directamente al navegador.
- Los reportes existentes en disco siguen siendo accesibles durante la transición.
- Se conservan nombre de descarga, tipo de contenido y manejo de archivos inexistentes.
- Se define cómo localizar el backend de cada artefacto cuando conviven reportes locales y S3.

## 7. Fase 5 — Pruebas de contrato

Suite propuesta:

```text
backend/tests/integrations/
├── test_artifact_store_contract.py
├── test_filesystem_artifact_store.py
└── test_s3_artifact_store.py
```

Ejecutar el contrato compartido contra filesystem y Kumo:

- Guardado y lectura íntegra de un PDF.
- Conservación de metadatos y `Content-Type`.
- Política explícita de sobrescritura o rechazo de duplicados.
- Eliminación y consulta de un archivo inexistente.
- Archivos de tamaño representativo y límites definidos.
- Fallo de conexión y recuperación sin resultados inconsistentes.
- Reinicio de Kumo con persistencia en una prueba local específica.

Las pruebas de API deben cubrir autenticación, acceso cruzado entre usuarios, rutas inválidas y compatibilidad de URL. Reutilizar las pruebas existentes de reportes, seguridad, simulaciones y topología cuando corresponda.

Criterio principal: los flujos de reportes producen el mismo resultado visible usando cualquiera de los dos adaptadores, salvo diferencias de infraestructura declaradas.

Todos los comandos Python locales deben utilizar `backend/venv/Scripts/python.exe`. Las pruebas usarán datos sintéticos y directorios o buckets aislados.

### 7.1. Pruebas conjuntas con API_Server

Reutilizar como base las fixtures de proveedor e issuer incluidas en `API_Server/scripts/`, ajustando los datos de prueba necesarios sin llamar a proveedores pagos. Kumo cubre el almacenamiento; la fixture HTTP cubre las respuestas de mercado o IA.

| Prueba | Recorrido | Resultado esperado |
| --- | --- | --- |
| Consumo autorizado | AssetManager → API_Server → fixture upstream | Método, path, query y JSON correctos; credencial del gateway no llega al upstream |
| Clave revocada o scope ausente | AssetManager → API_Server | Error de autenticación/autorización sin acceso directo alternativo |
| Cuota y disponibilidad | AssetManager → API_Server → fixture | Tratamiento de `429`, `Retry-After`, `502` y `504` con reintentos acotados |
| Reporte completo | Datos vía API_Server → reporte → Kumo → descarga en AssetManager | Artefacto íntegro y acceso limitado al propietario |
| Aislamiento de fallos | API_Server caído, S3 disponible; y situación inversa | Descarga de reportes existentes independiente del gateway; consultas de mercado independientes de S3 |
| Streaming, si se integra IA | AssetManager → API_Server → fixture SSE | Procesamiento incremental y cancelación propagada |

No afirmar validación integral hasta ejecutar el recorrido con ambos servicios y Kumo. El trabajo actual solo actualiza este plan.

## 8. Fase 6 — Integración en CI

Secuencia de la tarea de integración:

1. Iniciar la versión fijada de Kumo con estado efímero.
2. Esperar disponibilidad mediante una comprobación verificada.
3. Crear un bucket aislado para la ejecución.
4. Ejecutar pruebas del adaptador S3 y de la API de reportes.
5. Recoger diagnósticos si hay fallos, sin credenciales ni contenido sensible.
6. Detener el servicio y limpiar únicamente los recursos de esa ejecución.

Las pruebas unitarias ordinarias deben seguir ejecutándose sin Kumo. La persistencia `KUMO_DATA_DIR` se reservará para el perfil de desarrollo y pruebas específicas de reinicio; CI comenzará con estado limpio.

Añadir una tarea separada de compatibilidad entre repositorios que fije también la revisión de API_Server, prepare Supabase y sus fixtures en un entorno desechable y ejecute el recorrido completo. Usar una clave de aplicación de prueba con scopes mínimos. Los comandos de preparación que reinicializan bases solo son válidos sobre ese entorno desechable; nunca sobre la base de desarrollo compartida. Las pruebas S3 aisladas no necesitan iniciar API_Server.

## 9. Fase posterior — Evaluar trabajos de simulación con SQS

Esta fase requiere una decisión separada tras completar S3. El repositorio ya cuenta con Kafka; se debe justificar el beneficio de operar una segunda tecnología de mensajería para trabajos.

Las simulaciones actuales tienen límite de trabajos activos, historial acotado, estado en memoria, tareas dentro del proceso API y eventos Socket.IO. Antes de incorporar SQS se deben resolver:

- Un repositorio persistente de trabajos y resultados.
- Serialización de configuración y resultados de backtest.
- Recuperación tras reinicio y estados de trabajos interrumpidos.
- Idempotencia y control de duplicados bajo entrega al menos una vez.
- Reintentos, límites de ejecución y cola de mensajes fallidos.
- Propagación fiable de progreso al frontend.
- Propiedad del trabajo y propagación de `owner_id`.
- Acceso a datos respetando el único escritor de DuckDB.
- Generación y almacenamiento del reporte fuera del proceso API.

Flujo candidato, sujeto a esa evaluación:

```text
API
  ↓
Repositorio persistente de trabajos + publicación recuperable
  ↓
SQS/Kumo
  ↓
Worker de simulaciones
  ↓
Resultados y artefactos
  ↓
Eventos de progreso → API → Socket.IO
```

La publicación y el guardado del trabajo deben tolerar fallos entre ambos pasos. No se promete ejecución exactamente una vez por el mero uso de una cola.

## 10. Secretos y otros servicios AWS

Para proveedores consumidos mediante API_Server, Supabase Vault será la fuente de las credenciales upstream. AssetManager conservará únicamente la identidad de aplicación necesaria para llamar al gateway y la configuración no secreta de sus rutas. Adaptar su catálogo de integraciones para mostrar el modo gateway sin exigir la API key original.

`SecureIntegrationStore` conserva su función para secretos propios y conexiones directas explícitas de AssetManager; puede ampliarse para guardar la clave de API_Server, pero ese campo aún no existe en el catálogo revisado. La revocación de esa clave corresponde a API_Server. Su rotación implica crear una nueva, actualizar los procesos consumidores y revocar la anterior.

Las claves upstream antiguas se retirarán del entorno de AssetManager después de validar cada migración, mediante un cambio coordinado y recuperable. No migrarlas a Kumo ni duplicar el Vault del gateway con Secrets Manager. El uso futuro de Secrets Manager requiere una necesidad de despliegue AWS independiente.

DynamoDB, EventBridge, Lambda y API Gateway quedan fuera del primer entregable. Cada incorporación posterior necesitará un caso de uso y pruebas de las operaciones específicas.

## 11. Validación contra AWS y despliegue

| Entorno | Almacenamiento previsto |
| --- | --- |
| Desarrollo habitual | Filesystem |
| Desarrollo con emulador | S3 en Kumo |
| Pruebas unitarias | Adaptador local o dobles de prueba |
| CI de integración | S3 en Kumo con estado efímero |
| Staging, si se adopta AWS | S3 real en bucket aislado |
| Producción | S3 real o filesystem según el despliegue elegido |

Antes de desplegar S3 real, ejecutar pruebas de contrato representativas contra AWS y comprobar permisos, cifrado y descarga autenticada. El resultado contra Kumo valida el flujo local; la validación de AWS comprueba las diferencias del servicio real.

La vuelta a filesystem requiere conservar la localización de artefactos previos o migrarlos de forma verificable. Cambiar una variable no debe dejar inaccesibles los reportes ya guardados en S3.

## 12. Orden de implementación

1. Confirmar el inventario de llamadas y el catálogo autorizado de API_Server.
2. Validar el transporte autenticado de AssetManager con una fixture de proveedor; completar los puntos pendientes del cliente y su configuración.
3. Fijar la versión de Kumo y verificar sus operaciones S3 con el SDK seleccionado.
4. Añadir el perfil `aws-emulator` a Compose, con conectividad independiente hacia API_Server.
5. Añadir configuración del backend de artefactos y crear `ArtifactStore` con filesystem.
6. Extraer el almacenamiento de reportes de los puntos actuales.
7. Implementar S3 y el aprovisionamiento del bucket de pruebas.
8. Adaptar la descarga con propiedad y compatibilidad de URL.
9. Añadir pruebas de contrato del gateway, S3 y el recorrido completo de reporte.
10. Incorporar tareas separadas de integración S3 y compatibilidad entre repositorios en CI.
11. Documentar arranque, diagnóstico, migración de credenciales y reversión de almacenamiento.
12. Evaluar por separado persistencia de simulaciones y necesidad de SQS.

Primer entregable: consumir una operación de proveedor a través de API_Server con credenciales de aplicación, generar un reporte en AssetManager, guardarlo en filesystem o S3 emulado por Kumo y descargarlo desde la API de AssetManager con pruebas de integridad y aislamiento por usuario.

## 13. Referencias externas

- [Repositorio oficial de Kumo](https://github.com/sivchari/kumo).
- [README y persistencia de Kumo](https://github.com/sivchari/kumo/blob/main/README.md).
- [Historial de cambios](https://github.com/sivchari/kumo/blob/main/CHANGELOG.md).
- [Incidencias de compatibilidad](https://github.com/sivchari/kumo/issues).

Las capacidades y limitaciones de Kumo deben revisarse nuevamente al seleccionar la versión de implementación.
