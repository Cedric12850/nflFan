import requests

def fetch_data_from_api():
    url = 'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/franchises?limit=50'
    headers = {
        "Auth"
    }