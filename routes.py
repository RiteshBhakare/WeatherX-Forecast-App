from flask import Blueprint, render_template, request
from app.weather_api import get_current_weather, get_forecast


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/live-weather')
def live_weather():
    weather_data = get_current_weather("Pune")
    return render_template('live_weather.html', weather=weather_data)

@main.route('/forecast')
def forecast():
    forecast_data = get_forecast("Pune")
    return render_template('forecast.html', forecast=forecast_data)