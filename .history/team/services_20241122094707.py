import requests

def fetch_data_from_api():
    url = 'https://api.sportsdata.io/v3/nfl/scores/json/AllTeams?key=8ba341ac919c419c808fe64f86b7ec23'
    headers = {
        
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  #exception en cas d'erreur
        return response.json()
    except requests.RequestException as exception:
        return {"error": f"Echec lors de l'appel API: {str(exception)}"}