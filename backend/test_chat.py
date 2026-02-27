import requests
import json

url = "http://127.0.0.1:8000/api/v1/agents/chat/mistral"
payload = {
    "message": "Hello, can you tell me the current price of AAPL?",
    "user_id": 1,
    "portfolio": {}
}

response = requests.post(url, json=payload, stream=True)
if response.status_code == 200:
    for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
        if chunk:
            print(chunk, end="", flush=True)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
