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

# Try Mistral first to verify the key/url is correct
model_m = "mistralai/mistral-large-3-675b-instruct-2512"
payload_m = {
    "model": model_m,
    "messages": [{"role": "user", "content": "hi"}],
    "max_tokens": 5
}
print(f"Testing {model_m}...")
try:
    r = requests.post(url, headers=headers, json=payload_m, timeout=10)
    print(f"Mistral Status: {r.status_code}")
except Exception as e:
    print(f"Mistral Error: {e}")

# Try GLM 4.7
model_g = "z-ai/glm4.7"
payload_g = {
    "model": model_g,
    "messages": [{"role": "user", "content": "hi"}],
    "max_tokens": 5
}
print(f"\nTesting {model_g}...")
try:
    r = requests.post(url, headers=headers, json=payload_g, timeout=10)
    print(f"GLM 4.7 Status: {r.status_code}")
    if r.status_code != 200:
        print(f"Detail: {r.text}")
except Exception as e:
    print(f"GLM 4.7 Error: {e}")
