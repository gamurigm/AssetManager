
import asyncio
import sys
from ib_insync import IB, Stock, MarketOrder

async def test_order():
    ib = IB()
    print(">>> Conectando a TWS (Puerto 7497)...")
    try:
        await ib.connectAsync('127.0.0.1', 7497, clientId=150, timeout=10)
        print(">>> OK: Conectado!")
        
        contract = Stock('AAPL', 'SMART', 'USD')
        print(">>> Verificando contrato AAPL...")
        qualified = await ib.qualifyContractsAsync(contract)
        if not qualified:
            print(">>> ERROR: No se pudo calificar AAPL.")
            return
            
        print(f">>> Contrato verificado: {qualified[0].symbol} en {qualified[0].exchange}")
        
        # OJO: Esto intenta una orden real si estás conectado a una cuenta real
        # Pero si es Paper Trading (7497), es seguro.
        print(">>> Intentando orden de simulación (Market Order 1 share AAPL)...")
        order = MarketOrder('BUY', 1)
        trade = ib.placeOrder(qualified[0], order)
        
        print(">>> Esperando ejecución...")
        while not trade.isDone():
            await asyncio.sleep(0.1)
            
        print(f">>> RESULTADO: {trade.orderStatus.status}")
        print(f">>> PRECIO PROM: {trade.orderStatus.avgFillPrice}")
        
    except Exception as e:
        print(f">>> ERROR FATAL: {e}")
    finally:
        ib.disconnect()

if __name__ == "__main__":
    asyncio.run(test_order())
