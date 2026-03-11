import json
import asyncio
from confluent_kafka import Consumer, KafkaException
from app.core.logging import logger

class KafkaConsumerService:
    def __init__(self):
        self.config = {
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'fastapi-backend-cluster',
            'auto.offset.reset': 'latest',
            # Optimizations for fast real-time pulling
            'fetch.min.bytes': 1,
            'max.poll.interval.ms': 300000,
            'session.timeout.ms': 10000,
        }
        self.consumer = None
        self.sio = None
        self.loop = None
        self._running = False
        self._task = None

    def start(self, sio):
        """Inicializa el consumidor de Kafka en un bucle asíncrono secundario."""
        self.sio = sio
        self.loop = asyncio.get_running_loop()
        self.consumer = Consumer(self.config)
        
        # Nos suscribimos con una expresión regular a TODOS los tópicos de precios
        try:
            self.consumer.subscribe(['^market\.ticks\..*'])
            logger.info("[Kafka Consumer] Conectado y escuchando tópicos market.ticks.*")
        except Exception as e:
            logger.error(f"Error de suscripción: {e}")
            return
            
        self._running = True
        self._task = self.loop.create_task(self._consume_loop())

    def stop(self):
        """Apaga el consumidor de Kafka limpiamente."""
        self._running = False
        if self._task:
            self._task.cancel()
        if self.consumer:
            self.consumer.close()
            logger.info("[Kafka Consumer] Desconectado.")

    async def _consume_loop(self):
        """Bucle infinito que consume mensajes y los transmite vía WebSockets."""
        while self._running:
            try:
                # poll(timeout) es bloqueante a nivel de C (librería librdkafka).
                # Usamos asyncio.to_thread para no bloquear el Event Loop de FastAPI
                msg = await asyncio.to_thread(self.consumer.poll, 0.5)

                if msg is None:
                    continue
                if msg.error():
                    # Ignorar el error de que un tópico creado dinámicamente no exista momentáneamente
                    if msg.error().code() != msg.error().UNKNOWN_TOPIC_OR_PART:
                        logger.warning(f"[Kafka Consumer] Error: {msg.error()}")
                    continue

                # Procesar mensaje válido
                try:
                    tick = json.loads(msg.value().decode('utf-8'))
                    symbol = tick.get("symbol")
                    if symbol and self.sio:
                        # Formato compatible con el Frontend actual
                        frontend_payload = {
                            "symbol": symbol,
                            "price": tick.get("price", 0.0),
                            "change": 0.0,
                            "changePercent": 0.0,
                            "timestamp": tick.get("timestamp", 0),
                            "source": f"{tick.get('source', 'Kafka')} -> Kafka",
                            "live": True,
                        }
                        # Enviar el precio solo a los usuarios suscritos a esa "sala" / "cuarto"
                        await self.sio.emit("price_update", frontend_payload, room=symbol)
                        logger.debug(f"[Kafka Consumer] Reflected {symbol} @ {frontend_payload['price']}")
                except json.JSONDecodeError:
                    logger.error("[Kafka Consumer] Mensaje corrupto o no es JSON")

            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error inesperado en bucle: {e}")
                await asyncio.sleep(1) # Pausa de seguridad antes de reintentar

kafka_consumer_service = KafkaConsumerService()
