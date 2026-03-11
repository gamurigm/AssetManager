import json
import os
import sys
import time
import asyncio
from datetime import datetime
from confluent_kafka import Consumer, KafkaException

# Añadir la raíz del backend al path para permitir importaciones de 'app'
backend_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if backend_root not in sys.path:
    sys.path.append(backend_root)

from app.infrastructure.persistence.duckdb_repository import DuckDBRepository

# Configuración
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_GROUP_ID = "storage-service-group"

# Instanciar el repositorio (esto activará la creación de la tabla market_ticks si no existe)
db_repo = DuckDBRepository()

def create_consumer():
    config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'group.id': KAFKA_GROUP_ID,
        'auto.offset.reset': 'latest', # 'latest' para desarrollo, 'earliest' para producción real
        'enable.auto.commit': True
    }
    return Consumer(config)

async def run_storage_service():
    print(f"🔋 [Storage Service] Conectando a Kafka en {KAFKA_BOOTSTRAP_SERVERS}...")
    consumer = create_consumer()
    
    try:
        consumer.subscribe([r'^market\.ticks\..*'])
        print("🎧 [Storage Service] Escuchando tópicos market.ticks.* para el Data Lake...")
        
        tick_count = 0
        while True:
            # poll() es bloqueante, lo corremos en un hilo para no congelar el loop
            msg = await asyncio.to_thread(consumer.poll, 1.0)
            
            if msg is None:
                continue
            if msg.error():
                # Ignorar errores de tópico inexistente (Kafka 3.x+ los maneja bien tras sub automático)
                continue
                
            try:
                data = json.loads(msg.value().decode('utf-8'))
                symbol = data.get("symbol")
                price = data.get("price")
                timestamp_raw = data.get("timestamp")
                source = data.get("source", "unknown")
                
                if not symbol or price is None:
                    continue

                # Convertir timestamp (asumimos float de time.time())
                ts = datetime.fromtimestamp(timestamp_raw)
                
                # Persistencia en DuckDB
                success = db_repo.save_tick(symbol, price, ts, source)
                
                if success:
                    tick_count += 1
                    if tick_count % 50 == 0:
                        print(f"💾 [Storage Service] Total ticks guardados: {tick_count} (Last: {symbol} @ ${price})")
                
            except Exception as e:
                print(f"⚠️ [Storage Service] Error procesando mensaje: {e}")
                
    except KeyboardInterrupt:
        print("🛑 [Storage Service] Deteniendo...")
    except Exception as e:
        print(f"❌ [Storage Service] Error crítico: {e}")
    finally:
        consumer.close()
        print("👋 [Storage Service] Cerrado.")

if __name__ == "__main__":
    # Asegurar que el stdout use UTF-8 para evitar errores en Windows
    if sys.platform == "win32":
        import codecs
        sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
        
    try:
        asyncio.run(run_storage_service())
    except KeyboardInterrupt:
        pass
