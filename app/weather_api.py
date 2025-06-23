import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/"

# Raise an error if the API key is not found
if not API_KEY:
    raise ValueError("No WEATHER_API_KEY found in environment variables. Please set it in your .env file or environment.")

def get_current_weather(city):
    """
    Fetches current weather data for the specified city.
    """
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching current weather: {e}")
        return None

def get_forecast(city):
    """
    Fetches weather forecast data for the specified city.
    """
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching forecast: {e}")
        return None
