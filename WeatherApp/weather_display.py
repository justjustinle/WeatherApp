def display_weather_report(city: str, weather_report: dict):
    """
    Display the weather report for the city.

    Args:
        city (str): The name of the city.
        weather_report (dict): The weather data for the city.
    """
    feels_like = int(weather_report['current_condition'][0]['FeelsLikeC'])
    chance_of_rain = int(weather_report['weather'][0]['hourly'][0]['chanceofrain'])
    weather_desc = weather_report['current_condition'][0]['weatherDesc'][0]['value'].lower()

    print(f'\n------------------------------ Weather Report for : {city} ------------------------------\n')
    print(f"It's {weather_desc} today\n")
    if chance_of_rain > 75:
        print("It's gonna rain for sure, definitely bring an umbrella today!\n")
    elif 50 < chance_of_rain < 75:
        print("It's probably going to rain, bring an umbrella\n")
    elif 25 < chance_of_rain < 50:
        print("There's a chance of rain, consider an umbrella or hoodie\n")
    elif 0 <= chance_of_rain < 25:
        print("Very unlikely to rain today, you don't need an umbrella\n")

    print(f'Today feels like: {feels_like}°C\n')
    if feels_like > 25:
        print("Oh boy, it's hot outside, wear a t-shirt\n")
    elif 20 < feels_like < 25:
        print("It's not cold, you don't need a jacket\n")
    elif 15 < feels_like < 20:
        print("It's a little chilly, consider bringing a jacket\n")
    elif 10 < feels_like < 15:
        print("It's cold out, bring a light jacket\n")
    elif feels_like < 10:
        print("It's freezing outside, bring a thick jacket!\n")