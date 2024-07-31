import requests
try:
    from src.app.config import API_URL
except ModuleNotFoundError:
    from config import API_URL


def fetch_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    
    print(f'Error fetching data: {response.status_code}')
    return None
        