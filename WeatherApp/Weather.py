from city_validation import validate_city
from weather_fetcher import get_weather
from weather_display import display_weather_report
import logging

# Create a custom logger
logger = logging.getLogger('weatherAppLogger')


def main():
    city = input("Which city would you like the weather report for?: ")

    if validate_city(city):
        weather_report = get_weather(city)
        if weather_report:
            display_weather_report(city, weather_report)
        else:
            logger.error("Failed to retrieve weather data. Please try again later.")
    else:
        logger.error(f"City '{city}' is not valid. Please enter a valid city name.")


main()