import requests


def get_weather(city):

    # Step 1: City ko latitude/longitude mein convert karna
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    geo_response = requests.get(geo_url, params=geo_params)
    geo_data = geo_response.json()

    if "results" not in geo_data:
        return f"Weather information nahi mili for {city}"

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]
    city_name = geo_data["results"][0]["name"]

    # Step 2: Weather API
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
        "timezone": "auto"
    }

    weather_response = requests.get(
        weather_url,
        params=weather_params
    )

    weather_data = weather_response.json()
    current = weather_data["current"]

    return {
        "city": city_name,
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "weather_code": current["weather_code"]
    }