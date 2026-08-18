import requests

def fetch_swapi_data():
    url = f"https://swapi.info/api/people/24"
    try:
        response = requests.get(url)
        response.raise_for_status() # Check for HTTP errors
        data = response.json()
        status = response.status_code
        headers = response.headers
        print(headers)
        print(data)
        print(status)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

fetch_swapi_data()