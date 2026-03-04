import sys
import os
sys.path.append(os.getcwd())
from app.services.knowledge_base_service import kb_service

query = "efficient frontier"
results = kb_service.search(query, limit=3)

print(f"Buscando: '{query}'...")
for r in results:
    print("-" * 20)
    print(f"Libro: {r['file']}")
    print(f"Línea: {r['line']}")
    print(f"Extracto: {r['snippet']}")
