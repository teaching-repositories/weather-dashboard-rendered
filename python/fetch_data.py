import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def fetch_weather_data(api_key, location):
    current_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
    current_data = fetch_data(current_url)
    
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}'
    forecast_data = fetch_data(forecast_url)
    
    return current_data, forecast_data
