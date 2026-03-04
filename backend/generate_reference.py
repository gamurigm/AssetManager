import os
import sys
import json
import asyncio

# Ensure backend dir is in PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.services.openbb_api_catalog import EndpointInfo, openbb_catalog

async def main():
    try:
        from openbb_core.api.rest_api import app
    except ImportError as e:
        print(f"Failed to import openbb_core.api.rest_api: {e}")
        return

    # Extract OpenAPI schema directly from the FastAPI app instance
    spec = app.openapi()

    paths = spec.get("paths", {})
    for path, methods in paths.items():
        for method, operation in methods.items():
            if method.lower() in ("get", "post", "put", "delete"):
                ep = EndpointInfo(path, method, operation)
                openbb_catalog._endpoints.append(ep)
                for tag in ep.tags:
                    openbb_catalog._categories.setdefault(tag, []).append(ep)

    print(f"Loaded {len(openbb_catalog._endpoints)} endpoints across {len(openbb_catalog._categories)} categories")

    ref = openbb_catalog.get_full_reference()
    
    # Path to reference file
    prompt_path = os.path.join(os.path.dirname(__file__), "app", "agents", "team", "prompts", "openbb_api_reference.md")
    
    content = f"""## OPENBB PLATFORM API — FULL REFERENCE (http://localhost:6900)
You have COMPLETE access to ALL OpenBB Platform API endpoints via your tools.
Use `discover_openbb_endpoints(query)` to search for ANY endpoint, then call it.

### HOW TO USE:
1. DISCOVER: `discover_openbb_endpoints(query="keyword")` → find the right endpoint
2. DETAILS: `get_openbb_endpoint_details(endpoint_path="/api/v1/...")` → see exact parameters  
3. EXECUTE GET: `query_openbb_api(endpoint="/api/v1/...", params={{...}})` → fetch data
4. EXECUTE POST: `query_openbb_api_post(endpoint="/api/v1/...", payload={{...}})` → for econometrics
5. TERMINAL: `execute_openbb_terminal_command(command_path="...", symbol="...", chart=True)` → charts

### AVAILABLE CATEGORIES & KEY ENDPOINTS:

{ref}

### IMPORTANT RULES:
- Most GET endpoints require a `provider` parameter (use "yfinance" as default for free data)
- Use `discover_openbb_endpoints` when unsure about an endpoint
- For technical analysis charts, prefer `execute_openbb_terminal_command` which auto-fetches data
- For econometrics (POST endpoints), fetch data first then pass it as payload
- ALWAYS specify the provider parameter when required
"""
    with open(prompt_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"DONE: Successfully wrote {len(openbb_catalog._endpoints)} endpoints to openbb_api_reference.md")

if __name__ == "__main__":
    asyncio.run(main())
