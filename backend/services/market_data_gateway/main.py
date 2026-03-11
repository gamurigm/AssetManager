import sys
import os
import json
import time
import asyncio
import logging

# Permitir imprimir emojis en consolas de Windows sin colapsar
sys.stdout.reconfigure(encoding='utf-8')

# Agregar la raíz de 'backend' al path para poder importar módulos de 'app'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from confluent_kafka import Producer
from app.services.market_data import market_data_service

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("MarketDataGateway")

KAFKA_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'market-data-gateway-live'
}

# Lista de símbolos de los cuales alimentaremos el sistema de trading y la web
SYMBOLS_TO_TRACK = ['AAPL', 'MSFT', 'TSLA', 'SPY', 'BTC/USD']
POLL_INTERVAL_SEC = 5

def delivery_report(err, msg):
    """Callback disparado cuando Kafka avisa si el mensaje llegó bien o falló."""
    if err is not None:
        logger.error(f"Fallo al entregar mensaje a Kafka: {err}")
    # Nota: omitimos log exitoso por rendimiento para no saturar la consola en cada tick

async def fetch_and_publish(producer: Producer, symbol: str):
    """Obtiene el precio más reciente usando nuestro router y lo inyecta a Kafka."""
    try:
        data = await market_data_service.get_price(symbol)
        
        if data and "error" not in data:
            # Normalizar el formato del Tick para nuestro Bus de Eventos
            tick_data = {
                "symbol": symbol,
                "price": data.get("price", 0.0),
                "volume": data.get("volume", 0),
                "source": data.get("source", "Unknown"),
                "timestamp": time.time()
            }
            
            # Nombre del canal en Kafka (ej: market.ticks.AAPL)
            clean_symbol = symbol.replace('/', '_').replace('=', '')
            topic = f"market.ticks.{clean_symbol}"
            
            # Publicar al aire!
            producer.produce(
                topic=topic,
                key=symbol,
                value=json.dumps(tick_data),
                callback=delivery_report
            )
            logger.info(f"📡 [OUT] -> [{topic}] : ${tick_data['price']} ({tick_data['source']})")
            
        else:
            logger.warning(f"Error o Límite de API en {symbol}: {data.get('error', 'Error Desconocido')}")
            
    except Exception as e:
        logger.error(f"Excepción obteniendo {symbol}: {str(e)}")

async def run_gateway():
    logger.info("🚀 Iniciando el Market Data Gateway Microservice...")
    producer = Producer(KAFKA_CONFIG)
    
    try:
        while True:
            logger.info(f"🔄 Consultando batch de {len(SYMBOLS_TO_TRACK)} símbolos...")
            
            # Ejecutar todas las llamadas de red asíncronas en paralelo
            tasks = [fetch_and_publish(producer, sym) for sym in SYMBOLS_TO_TRACK]
            await asyncio.gather(*tasks)
            
            # Forzar el envío masivo de todos los ticks al broker de Kafka
            producer.flush()
            
            logger.info(f"Zzz... Esperando {POLL_INTERVAL_SEC}s para el siguiente ciclo.")
            await asyncio.sleep(POLL_INTERVAL_SEC)
            
    except KeyboardInterrupt:
        logger.info("⚠️ Recibida señal de apagado. Cerrando Gateway...")
    finally:
        producer.flush()

if __name__ == "__main__":
    # Arrancar el Loop Asíncrono
    asyncio.run(run_gateway())
