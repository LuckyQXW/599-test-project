import requests

API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
API_TOKEN = "<API KEY>"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": "年兽的故事：",
})
print(output)