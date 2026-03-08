
import requests
import json

url = "http://localhost:8282/api/v1/trading/command/ibkr"
payload = {
    "command": "buy AAPL --shares 1 --venue ibkr",
    "portfolio_id": "main",
    "record_trade": True
}
headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
