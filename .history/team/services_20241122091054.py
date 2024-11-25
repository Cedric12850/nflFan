import requests

def fetch_data_from_api():
    url = 'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/franchises?limit=50'
    headers = {
        "Authorization": "Bearer your_api_token",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  #exception en cas d'erreur
        