import sys
import os
sys.path.append(os.getcwd())
from app.services.knowledge_base_service import kb_service

queries = ["Modified VaR", "mVaR", "Cornish-Fisher", "Modified Expected Shortfall", "mES"]
for query in queries:
    results = kb_service.search(query, limit=5)
    print(f"\nResultados para: '{query}'")
    for r in results:
        if "Pfaff" in r['file'] or "risk-modelling" in r['file'].lower():
            print(f"- [{r['file']}] L{r['line']}: {r['snippet']}")
