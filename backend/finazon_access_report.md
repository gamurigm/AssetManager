# Finazon API Access & Limits Document
**Date:** 2026-02-23
**Dataset:** US Stocks Essential

Se ha ejecutado una verificación directa a la API (`/finazon/us_stocks_essential/api_usage`) usando tu API Key (`777a***`). Aquí detallamos exactamente a qué tienes acceso bajo este plan gratuito (Free Trial):

## 1. Tickers Disponibles (Símbolos)
Al ser una cuenta de nivel Trial (Prueba Gratuita), Finazon restringe el acceso a la base de datos completa. Sólo tienes permiso para consultar datos para los siguientes 3 símbolos de prueba:
- **AAPL** (Apple Inc.)
- **TSLA** (Tesla Inc.)
- **GOOG** (Alphabet Inc. - Google)

*Cualquier otro símbolo (como MSFT, SPY, EURUSD) devolverá un error `403 Forbidden: TRIAL_SYMBOL_UNAVAILABLE`.*

## 2. Límites de Peticiones (Quotas)
Los límites asignados a tu cuenta son **extremadamente restrictivos** (usualmente se renuevan por minuto o por hora dependiendo de las políticas de prueba de Finazon). Los límites actuales observados son:

| Tipo de Endpoint | Límite Máximo Asignado | Uso Actual | Qué permite hacer |
| :--- | :--- | :--- | :--- |
| **Price** (`/price`) | **10 peticiones** | 1 | Obtener el precio actual en vivo. |
| **Time Series** (`/time_series`) | **5 peticiones** | 0 | Descargar velas históricas (OHLCV). |
| **Reference** | **5 peticiones** | 1 | Obtener metadata sobre los activos. |
| **Snapshots** | **5 peticiones** | 0 | Obtener una vista de todo el mercado en un instante. |
| **Trades** | **5 peticiones** | 0 | Obtener la cinta de lectura de cada trade (Tick-by-tick). |

## 3. Conclusión y Recomendación
Debido a estos límites:
- El proveedor `FinazonProvider` funcionará perfectamente en el código para realizar pruebas técnicas.
- **No es apto para entornos de producción ni backtesting general** mientras estés en el tier Trial, ya que la cuota se agota tras sólo 5 consultas históricas y sólo te limitas a 3 acciones.
- Es recomendable seguir usando **Yahoo Finance (YFinance)**, **TwelveData**, o **Polygon.io** para tus cargas históricas principales, y mantener a Finazon desactivado o priorizado sólo para AAPL en caso de que lo necesites estrictamente para pruebas.
