import requests

BASE_URL = "http://localhost:8081"

def get(endpoint, headers=None):
    response = requests.get(f"{BASE_URL}/{endpoint}", headers=headers)
    return response.json()

def post(endpoint, data, headers=None):
    response = requests.post(f"{BASE_URL}/{endpoint}", json=data, headers=headers)
    return response.json()