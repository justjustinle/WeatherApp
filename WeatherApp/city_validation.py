from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import logging

# Setup the geolocator
geolocator = Nominatim(user_agent="city_validator")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

def validate_city(city_name: str) -> bool:
    """
    Validate the city name using geopy's geolocator.

    Args:
        city_name (str): The name of the city to validate.

    Returns:
        bool: True if the city is valid, False otherwise.
    """
    try:
        location = geocode(city_name, exactly_one=True, timeout=10)
        if location:
            logging.info(f"Valid city: {location.address}")
            return True
        else:
            logging.warning(f"Invalid city: {city_name}")
            return False
    except Exception as e:
        logging.error(f"An error occurred during city validation: {e}")
        return False