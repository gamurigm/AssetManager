import requests
import json
import sys

# Flush output to console in real-time
url = "http://127.0.0.1:8000/api/v1/agents/chat"
payload = {
    "message": "Hi team! Ask the Quant Analyst for the price of AAPL and the Fundamental Analyst for some news on it.",
    "user_id": 1,
    "portfolio": {}
}

response = requests.post(url, json=payload, stream=True)
if response.status_code == 200:
    for chunk in response.iter_content(chunk_size=10, decode_unicode=True):
        if chunk:
            sys.stdout.write(chunk)
            sys.stdout.flush()
else:
    print(f"Error: {response.status_code}")
    print(response.text)
