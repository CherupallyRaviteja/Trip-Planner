import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return {
            "error": "Weather unavailable"
        }

    data = response.json()

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["main"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }