import requests
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("NVIDIA_NIM_API_KEY")
url = "https://integrate.api.nvidia.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

# The ID from the list: meta/llama-3.3-70b-instruct
model = "meta/llama-3.3-70b-instruct"
payload = {
    "model": model,
    "messages": [{"role": "user", "content": "hi"}],
    "max_tokens": 5
}
print(f"Testing {model}...")
try:
    r = requests.post(url, headers=headers, json=payload, timeout=10)
    print(f"Status: {r.status_code}")
except Exception as e:
    print(f"Error: {e}")

# The ID from the list: nvidia/Llama-3_1-Nemotron-Ultra-253B-v1
model2 = "nvidia/Llama-3_1-Nemotron-Ultra-253B-v1"
payload2 = {
    "model": model2,
    "messages": [{"role": "user", "content": "hi"}],
    "max_tokens": 5
}
print(f"\nTesting {model2}...")
try:
    r = requests.post(url, headers=headers, json=payload2, timeout=10)
    print(f"Status: {r.status_code}")
except Exception as e:
    print(f"Error: {e}")
