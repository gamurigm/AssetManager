import asyncio
import pandas as pd
from app.services.finviz_service import finviz_service

async def fetch_finviz_data_as_df(url_path: str) -> pd.DataFrame:
    """
    Scrape any Finviz page and return the data as a Pandas DataFrame.
    Ideal for data analysis.
    
    Args:
        url_path (str): The Finviz URL or path (e.g. 'insidertrading.ashx', 'screener.ashx?v=111')
        
    Returns:
        pd.DataFrame: The scraped table data.
    """
    print(f"Scrapeando datos de: {url_path}...")
    result = await finviz_service.scrape_generic(url_path)
    
    if "error" in result:
        print(f"Error: {result['error']}")
        return pd.DataFrame()
        
    rows = result.get("rows", [])
    if not rows:
        print("No se encontraron datos en esa página.")
        return pd.DataFrame()
        
    df = pd.DataFrame(rows)
    print(f"¡Éxito! Logrados {len(df)} registros.")
    
    # Close session if running as standalone
    await finviz_service.close()
    
    return df

# == Ejemplos de Uso ==
if __name__ == "__main__":
    async def run_examples():
        # 1. Scrape a la página de Insider Trading
        df_insider = await fetch_finviz_data_as_df("insidertrading.ashx?tc=7")
        if not df_insider.empty:
            print("\n--- Primeros 3 registros de Insider Trading ---")
            print(df_insider.head(3).to_string())

        # 2. Puedes hacer scrape a CUALQUIER otra página, ej: un Screener de Top Gainers
        # Top Gainers: screener.ashx?v=111&s=ta_topgainers
        print("\n\n")
        df_gainers = await fetch_finviz_data_as_df("screener.ashx?v=111&s=ta_topgainers")
        if not df_gainers.empty:
            print("\n--- Primeros 3 registros de Top Gainers ---")
            print(df_gainers.head(3).to_string())

    asyncio.run(run_examples())
