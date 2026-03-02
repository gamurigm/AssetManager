import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from dotenv import load_dotenv

# Load env vars
load_dotenv()

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

if not BYBIT_API_KEY or not BYBIT_API_SECRET:
    print("❌ ERROR: Bybit API keys missing from .env")
    sys.exit(1)

try:
    from pybit.unified_trading import HTTP
except ImportError:
    print("❌ ERROR: 'pybit' library not installed. Please run: pip install pybit")
    sys.exit(1)

# Initialize Session
print("🔗 Initializing Bybit API (v5 Unified Trading)...")
session = HTTP(
    testnet=False, # We assume mainnet based on how the user asked
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

print("\n" + "="*50)
print("🚀 BEGIN EXHAUSTIVE TESTING")
print("="*50)

# 1. PUBLIC ENDPOINTS (No auth required, just testing connection)
print("\n[✔] 1. PROBANDO ENDPOINTS PÚBLICOS")
try:
    print(" ↳ Obteniendo Tiempo del Servidor...", end=" ")
    server_time = session.get_server_time()
    print(f"OK ({server_time['time']})")
except Exception as e:
    print(f"FAILED: {e}")

try:
    print(" ↳ Obteniendo Tickers de Spot (BTCUSDT)...", end=" ")
    tickers = session.get_tickers(category="spot", symbol="BTCUSDT")
    print(f"OK | Precio: ${tickers['result']['list'][0]['lastPrice']}")
except Exception as e:
    print(f"FAILED: {e}")
    
try:
    print(" ↳ Obteniendo Tickers de Derivados (BTCUSDT)...", end=" ")
    tickers = session.get_tickers(category="linear", symbol="BTCUSDT")
    print(f"OK | Precio: ${tickers['result']['list'][0]['lastPrice']}")
except Exception as e:
    print(f"FAILED: {e}")

# 2. PRIVATE ENDPOINTS (Auth required) 
print("\n[✔] 2. PROBANDO ACCESO PRIVADO (API KEY)")
try:
    print(" ↳ Obteniendo Información de la Cuenta API...", end=" ")
    api_info = session.get_api_key_information()
    
    if api_info['retCode'] == 0:
        permissions = api_info['result']
        print(f"OK | ID Cuenta: {permissions.get('userID', 'N/A')}")
        print("\n   [!] Permisos de la API Key:")
        print(f"     - Lectura/Escritura (readonly): {permissions.get('readOnly', True)}")
        print(f"     - IP restringida: {permissions.get('ips', [])}")
        
        print("\n   [!] Permisos de Trading habilitados:")
        perms = permissions.get('permissions', {})
        for perm_type, details in perms.items():
            if details:
                print(f"     - {perm_type.capitalize()}: {', '.join(details)}")
            else:
                print(f"     - {perm_type.capitalize()}: Ninguno")
                
    else:
        print(f"FAILED: Error en la respuesta: {api_info['retMsg']}")
except Exception as e:
    print(f"FAILED: {type(e).__name__} - {e}")

# 3. WALLET & BALANCES
print("\n[✔] 3. PROBANDO BALANCES (WALLET)")
try:
    print(" ↳ Obteniendo Balance de Cuenta Unificada (UNIFIED)...", end=" ")
    balance = session.get_wallet_balance(accountType="UNIFIED")
    if balance['retCode'] == 0:
        unified_coins = balance['result']['list'][0].get('coin', [])
        if not unified_coins:
            print("OK | AccountType 'UNIFIED' vacío o no soportado.")
        else:
            print("OK")
            for coin in unified_coins:
                if float(coin.get('walletBalance', 0)) > 0:
                     print(f"     - {coin['coin']}: {coin['walletBalance']} (USD equiv: ${coin.get('usdValue', 0)})")
    else:
         print(f"FAILED: {balance['retMsg']}")
except Exception as e:
    print(f"FAILED: {e}")

try:
    print(" ↳ Obteniendo Balance de Cuenta de Financiación (FUND)...", end=" ")
    balance = session.get_wallet_balance(accountType="FUND")
    if balance['retCode'] == 0:
        fund_coins = balance['result']['list'][0].get('coin', [])
        if not fund_coins:
             print("OK | AccountType 'FUND' vacío.")
        else:
            print("OK")
            for coin in fund_coins:
                if float(coin.get('walletBalance', 0)) > 0:
                     print(f"     - {coin['coin']}: {coin['walletBalance']} (USD equiv: ${coin.get('usdValue', 0)})")
    else:
         print(f"FAILED: {balance['retMsg']}")
except Exception as e:
    print(f"FAILED: {e}")


# 4. POSITIONS & ORDERS
print("\n[✔] 4. PROBANDO DETALLES DE TRADING")
try:
    print(" ↳ Obteniendo Posiciones Abiertas (Derivados)...", end=" ")
    positions = session.get_positions(category="linear", settleCoin="USDT")
    if positions['retCode'] == 0:
        # Pydantic may complain if we just iterate 'positions' poorly
        pos_list = positions['result']['list']
        if not pos_list:
            print("OK | No hay posiciones abiertas usando USDT como colateral.")
        else:
            print(f"OK | Encontradas {len(pos_list)} posiciones.")
            for p in pos_list:
                 print(f"     - {p['symbol']}: Tamaño {p['size']} | Side: {p['side']} | PnL No Realizado: ${p['unrealisedPnl']}")
    else:
        print(f"FAILED: {positions['retMsg']}")
except Exception as e:
    print(f"FAILED: {e}")

try:
    print(" ↳ Obteniendo Historial de Órdenes Recientes (Derivados USDT)...", end=" ")
    orders = session.get_order_history(category="linear", settleCoin="USDT", limit=3)
    if orders['retCode'] == 0:
        order_list = orders['result']['list']
        if not order_list:
            print("OK | No hay historial de órdenes reciente.")
        else:
            print(f"OK | Últimas {len(order_list)} órdenes:")
            for o in order_list:
                print(f"     - {o['symbol']} | {o['side']} {o['orderType']} | Estado: {o['orderStatus']} | Qty: {o['qty']}")
    else:
        print(f"FAILED: {orders['retMsg']}")
except Exception as e:
    print(f"FAILED: {e}")

try:
    print(" ↳ Obteniendo Configuración de Fee...", end=" ")
    fees = session.get_fee_rates(category="linear", symbol="BTCUSDT")
    if fees['retCode'] == 0:
        f = fees['result']['list'][0]
        print(f"OK | Taker Fee: {f['takerFeeRate']} | Maker Fee: {f['makerFeeRate']}")
    else:
         print(f"FAILED: {fees['retMsg']}")
except Exception as e:
    print(f"FAILED: {e}")


print("\n" + "="*50)
print("🏁 PRUEBAS FINALIZADAS")
print("="*50)

