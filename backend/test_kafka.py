import sys
import json
import time

sys.stdout.reconfigure(encoding='utf-8')
from confluent_kafka import Producer, Consumer

# Configuración básica para conectarnos a Kafka en localhost
KAFKA_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'assetmanager-demo'
}

def delivery_report(err, msg):
    """Callback que Kafka llama cuando un mensaje fue entregado con éxito o falló."""
    if err is not None:
        print(f"❌ Error entregando el mensaje: {err}")
    else:
        print(f"✅ ¡Mensaje entregado con éxito!")
        print(f"👉 Tópico: '{msg.topic()}' | Partición: [{msg.partition()}]")

def test_kafka():
    print("--- 📡 INICIANDO PRUEBA DE KAFKA ---")

    # 1. Crear el INGESTOR DE PRECIOS (Producer)
    print("\n[PRODUCER] Conectando al broker para emitir precios...")
    producer = Producer(KAFKA_CONFIG)
    topic_name = "market.ticks.AAPL"

    tick_data = {
        "symbol": "AAPL",
        "price": 185.32,
        "volume": 500,
        "timestamp": time.time()
    }

    # "Gritar al aire" convirtiendo el diccionario Python a un JSON genérico.
    producer.produce(
        topic=topic_name,
        key=tick_data["symbol"], 
        value=json.dumps(tick_data),
        callback=delivery_report
    )
    
    # IMPORTANTE: Kafka envía mensajes en lotes asíncronos por detrás. 
    # flush() lo obliga a enviarlos ahora mismo antes de seguir.
    producer.flush()

    # -----------------------------------------------------

    # 2. Crear el SUSCRIPTOR (Consumer)
    # Imaginemos que este es otro microservicio totalmente independiente (ej. Strategy Engine)
    print("\n[CONSUMER] Suscribiéndose como Motor de Estrategias al canal...")
    consumer_config = KAFKA_CONFIG.copy()
    consumer_config['group.id'] = 'strategy-engine-1'  # Cómo se identifica este servicio
    consumer_config['auto.offset.reset'] = 'earliest'  # Leer desde el principio si recién me conecto

    consumer = Consumer(consumer_config)
    
    # Sintonizar la "antena" a los dos tópicos que nos interesan (pueden ser muchos)
    consumer.subscribe(['market.ticks.AAPL'])

    print("🎧 Escuchando durante 5 segundos para recibir mensajes...")
    try:
        start_time = time.time()
        while time.time() - start_time < 5.0:
            # Pide mensajes al broker (espera hasta 1 segundo max cada pedido)
            msg = consumer.poll(1.0)
            
            if msg is None:
                continue
            elif msg.error():
                print(f"❌ Error leyendo mensaje: {msg.error()}")
                if msg.error().code() != msg.error().UNKNOWN_TOPIC_OR_PART:
                    pass # Ignore unknown topics for dynamic auto-creation to catch up
            else:
                # Des-empaquetamos el JSON bruto a nuestro diccionario de Python otra vez:
                tick_recibido = json.loads(msg.value().decode('utf-8'))
                print(f"\n📩 ¡NUEVO TICK RECIBIDO POR EL MOTOR DE ESTRATEGIAS!")
                print(f"💰 Símbolo: {tick_recibido['symbol']}")
                print(f"💵 Precio actual: ${tick_recibido['price']}")
                
                # Aquí llamaría a tu: IStrategyEngine.run_session(...)
                break # Success! We can exit early.
            
    except KeyboardInterrupt:
        pass
    finally:
        # Siempre cerrar limpiamente el consumidor para que Kafka sepa que nos fuimos
        consumer.close()
        print("\n👋 Consumidor desconectado.")

if __name__ == "__main__":
    test_kafka()
