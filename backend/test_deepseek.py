import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("NVIDIA_NIM_API_KEY")
url = "https://integrate.api.nvidia.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

model = "deepseek-ai/deepseek-v3"
payload = {
    "model": model,
    "messages": [{"role": "user", "content": "hi"}],
    "max_tokens": 5
}
print(f"Testing {model}...")
try:
    r = requests.post(url, headers=headers, json=payload, timeout=10)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text}")
except Exception as e:
    print(f"Error: {e}")
