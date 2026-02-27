import sys
import os
sys.path.append(os.getcwd())
from app.services.knowledge_base_service import kb_service

# Search for where mVaR or mES are explained in the text
target_file = "c:/AssetManager/data/quant_kb/Risk_and_Portfolio_Optimization/financial-risk-modelling-and-portfolio-optimization-with-r-2nd-edt.md"
query = "mVaR"
results = kb_service.search(query, limit=10)
for r in results:
    print(f"Match in {r['file']} at line {r['line']}: {r['snippet']}")
