
import requests
import json

URL = "http://localhost:8282/api/v1/trading/status/ibkr"

try:
    resp = requests.get(URL)
    print(json.dumps(resp.json(), indent=2))
except Exception as e:
    print(f"Error querying status: {e}")
