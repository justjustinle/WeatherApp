import requests
import logging

def get_weather(city: str) -> dict:
    """
    Fetch the weather information for a specified city.

    Args:
        city (str): The name of the city to get the weather for.

    Returns:
        dict: The weather report for the city.
    """
    try:
        response = requests.get(f'https://wttr.in/{city}?format=j1')
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve weather data: {e}")
        return None
