import json
import os
import sys
import asyncio
import logging
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional
from confluent_kafka import Consumer, Producer, KafkaException

# Asegurar que el stdout use UTF-8 para evitar errores en Windows
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Configurar logs básicos
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("StrategyEngineLive")

# Añadir la raíz del backend al path para permitir importaciones de 'app'
backend_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if backend_root not in sys.path:
    sys.path.append(backend_root)

# Importaciones de la aplicación
from app.agents.strategies.engine import StrategyFactory, StrategyConfig, TradeSignal
from app.services.intraday_repository import intraday_repository, CandleRow

# Configuración de Kafka
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
CONSUMER_GROUP_ID = "strategy-engine-live-group"
TICK_TOPIC_PATTERN = r'^market\.ticks\..*'
SIGNAL_TOPIC = "trade.signals"

class CandleAggregator:
    """
    Agrega ticks en velas de 1m y 5m en memoria.
    """
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.m1_candles: List[dict] = []
        self.m5_candles: List[dict] = []
        
        # Velas en construcción
        self.current_m1: Optional[dict] = None
        self.current_m5: Optional[dict] = None

    def update(self, price: float, timestamp: datetime):
        # Normalizar timestamp al inicio del minuto
        m1_ts = timestamp.replace(second=0, microsecond=0)
        m5_ts = timestamp.replace(minute=(timestamp.minute // 5) * 5, second=0, microsecond=0)
        
        # --- Update M1 ---
        if not self.current_m1 or self.current_m1["timestamp"] != m1_ts.isoformat() + "Z":
            if self.current_m1:
                self.m1_candles.append(self.current_m1)
                # Mantener solo las últimas 200 velas para rendimiento
                if len(self.m1_candles) > 200: self.m1_candles.pop(0)
            
            self.current_m1 = {
                "symbol": self.symbol,
                "timestamp": m1_ts.isoformat() + "Z",
                "open": price, "high": price, "low": price, "close": price,
                "volume": 0
            }
        else:
            self.current_m1["high"] = max(self.current_m1["high"], price)
            self.current_m1["low"] = min(self.current_m1["low"], price)
            self.current_m1["close"] = price

        # --- Update M5 ---
        if not self.current_m5 or self.current_m5["timestamp"] != m5_ts.isoformat() + "Z":
            if self.current_m5:
                self.m5_candles.append(self.current_m5)
                if len(self.m5_candles) > 100: self.m5_candles.pop(0)
            
            self.current_m5 = {
                "symbol": self.symbol,
                "timestamp": m5_ts.isoformat() + "Z",
                "open": price, "high": price, "low": price, "close": price,
                "volume": 0
            }
        else:
            self.current_m5["high"] = max(self.current_m5["high"], price)
            self.current_m5["low"] = min(self.current_m5["low"], price)
            self.current_m5["close"] = price

    def get_context(self):
        """Devuelve las velas cerradas + la actual para el motor."""
        # Se añade la actual para que el motor vea el precio en vivo
        m1 = self.m1_candles + ([self.current_m1] if self.current_m1 else [])
        m5 = self.m5_candles + ([self.current_m5] if self.current_m5 else [])
        return m1, m5

class StrategyRuntime:
    """
    Gestiona el ciclo de vida de una estrategia para un símbolo.
    """
    def __init__(self, symbol: str, strategy_name: str, producer: Producer):
        self.symbol = symbol
        self.strategy_name = strategy_name
        self.producer = producer
        self.aggregator = CandleAggregator(symbol)
        self.engine = StrategyFactory.create(strategy_name)
        self.config = StrategyConfig.default()
        self.last_signal_id: Optional[str] = None
        self.initialized = False

    async def initialize_history(self):
        """Carga datos históricos del día desde DuckDB."""
        logger.info(f"💾 [{self.symbol}] Cargando historial de DuckDB...")
        today = datetime.now().strftime("%Y-%m-%d")
        start_ts = f"{today} 00:00:00"
        end_ts = f"{today} 23:59:59"
        
        # Nota: intraday_repository usa hilos internamente para DuckDB
        m1 = await asyncio.to_thread(intraday_repository.get, self.symbol, "1m", start_ts, end_ts)
        m5 = await asyncio.to_thread(intraday_repository.get, self.symbol, "5m", start_ts, end_ts)
        
        # Poblar el agregador
        if m1:
            self.aggregator.m1_candles = m1
            logger.info(f"✅ [{self.symbol}] {len(m1)} velas M1 cargadas.")
        if m5:
            self.aggregator.m5_candles = m5
            logger.info(f"✅ [{self.symbol}] {len(m5)} velas M5 cargadas.")
        
        self.initialized = True

    def process_tick(self, price: float, ts: datetime):
        if not self.initialized: return
        
        # Actualizar velas
        self.aggregator.update(price, ts)
        
        # Obtener contexto
        m1, m5 = self.aggregator.get_context()
        if not m1 or not m5: return

        # Ejecutar motor (Sincrónico, es CPU pure math)
        try:
            signal = self.engine.run_session(
                m5_candles=m5,
                m1_candles=m1,
                account_size=10000.0, # TODO: Vincular a equity real
                config=self.config
            )
            
            if signal and signal.signal_id != self.last_signal_id:
                self.last_signal_id = signal.signal_id
                self._publish_signal(signal)
                
        except Exception as e:
            logger.error(f"Error en motor [{self.symbol}]: {e}")

    def _publish_signal(self, signal: TradeSignal):
        msg = {
            "symbol": self.symbol,
            "strategy": self.strategy_name,
            "signal_id": signal.signal_id,
            "direction": signal.direction,
            "entry": signal.entry,
            "stop": signal.stop,
            "tp": signal.tp,
            "timestamp": signal.timestamp,
            "position_size": signal.position_size,
            "confidence": signal.confidence
        }
        self.producer.produce(
            SIGNAL_TOPIC,
            key=self.symbol,
            value=json.dumps(msg).encode('utf-8')
        )
        self.producer.flush()
        logger.info(f"🎯 [SIGNAL] -> {self.symbol} {signal.direction} @ {signal.entry} (SL: {signal.stop})")

async def run_strategy_engine():
    logger.info("⚙️ Iniciando Motor de Estrategias en Vivo (Kafka-driven)...")
    
    # Setup Kafka
    consumer_config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'group.id': CONSUMER_GROUP_ID,
        'auto.offset.reset': 'latest',
        'enable.auto.commit': True
    }
    producer_config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS
    }
    
    consumer = Consumer(consumer_config)
    producer = Producer(producer_config)
    
    # Iniciar Runtimes (Solo ORB_FVG_ENGULFING por ahora por simplicidad)
    symbols = ['AAPL', 'MSFT', 'TSLA', 'SPY', 'BTC/USD']
    runtimes: Dict[str, StrategyRuntime] = {}
    
    for sym in symbols:
        rt = StrategyRuntime(sym, "ORB_FVG_ENGULFING", producer)
        await rt.initialize_history()
        runtimes[sym] = rt

    try:
        consumer.subscribe([TICK_TOPIC_PATTERN])
        logger.info(f"🎧 Escuchando ticks para {len(symbols)} símbolos...")
        
        while True:
            msg = await asyncio.to_thread(consumer.poll, 0.5)
            
            if msg is None: continue
            if msg.error(): continue
            
            try:
                data = json.loads(msg.value().decode('utf-8'))
                symbol = data.get("symbol")
                if symbol not in runtimes: continue
                
                price = data.get("price")
                ts_raw = data.get("timestamp")
                ts = datetime.fromtimestamp(ts_raw)
                
                # Procesar en el runtime correspondiente
                runtimes[symbol].process_tick(price, ts)
                
            except Exception as e:
                logger.error(f"Error procesando tick: {e}")
                
    except KeyboardInterrupt:
        logger.info("🛑 Apagando...")
    finally:
        consumer.close()
        producer.flush()

if __name__ == "__main__":
    asyncio.run(run_strategy_engine())
