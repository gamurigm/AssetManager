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

model = "z-ai/glm4.7" # Test if 4.7 works
payload = {
    "model": model,
    "messages": [{"role": "user", "content": "hello"}],
    "max_tokens": 10,
    "stream": False
}

print(f"Testing {model}...")
try:
    response = requests.post(url, headers=headers, json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")

model2 = "z-ai/glm5"
payload2 = {
    "model": model2,
    "messages": [{"role": "user", "content": "hello"}],
    "max_tokens": 10,
    "stream": False
}
print(f"\nTesting {model2}...")
try:
    response = requests.post(url, headers=headers, json=payload2)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
