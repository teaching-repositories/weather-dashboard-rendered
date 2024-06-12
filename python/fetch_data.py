import requests


def fetch_data(url):
    """
    Fetch data from the provided URL.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        dict or None: The data fetched from the URL in JSON format if the request was successful,
                      otherwise None.
    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None


def fetch_weather_data(api_key, location):
    """
    Fetch current weather and forecast data for a given location.

    Args:
        api_key (str): The API key for authenticating with the OpenWeatherMap API.
        location (str): The location (city name) to fetch weather data for.

    Returns:
        tuple: A tuple containing two elements:
            - dict or None: The current weather data.
            - dict or None: The weather forecast data.
    """
    current_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
    current_data = fetch_data(current_url)

    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}'
    forecast_data = fetch_data(forecast_url)

    return current_data, forecast_data
