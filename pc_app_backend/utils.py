import requests

BASE_URL = "http://localhost:8081"

def get(endpoint, headers=None):
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud GET: {e}")
        return {"error": str(e)}

def post(endpoint, data, headers=None):
    if headers is None:
        headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(f"{BASE_URL}/{endpoint}", json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud POST: {e}")
        return {"error": str(e)}