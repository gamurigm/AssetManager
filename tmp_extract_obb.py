import sys, json
from openbb import obb

def get_all_endpoints(obj, prefix=""):
    endpoints = []
    for attr in dir(obj):
        if not attr.startswith("_"):
            child = getattr(obj, attr)
            path = f"{prefix}.{attr}" if prefix else attr
            # If it's a function, it's an endpoint
            if callable(child) and hasattr(child, "__wrapped__") or "openbb" in str(type(child)):
                if callable(child):
                    endpoints.append(path)
                # Recurse into modules
                get_all_endpoints(child, path)
    return endpoints

try:
    all_endpoints = []
    # Base modules to explore
    modules = ["equity", "crypto", "currency", "fixedincome", "index", "economy", "derivatives", "technical"]
    for mod_name in modules:
        if hasattr(obb, mod_name):
            mod = getattr(obb, mod_name)
            all_endpoints.extend(get_all_endpoints(mod, mod_name))
    
    # Filter for unique and common patterns
    unique_endpoints = sorted(list(set(all_endpoints)))
    print(json.dumps(unique_endpoints))
except Exception as e:
    print(json.dumps({"error": str(e)}))
