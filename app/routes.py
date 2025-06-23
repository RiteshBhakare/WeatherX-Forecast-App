from flask import Blueprint, render_template, request
from .weather_api import get_current_weather, get_forecast
#from app.weather_api import get_current_weather, get_forecast


main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Homepage route
    return render_template('index.html')

@main.route('/live-weather')
def live_weather():
    city = request.args.get('city', 'Pune')  # Optionally get city from query parameter, default Pune
    weather_data = get_current_weather(city)

    # Check if API response is valid and contains expected data
    if weather_data and weather_data.get('cod') == 200:
        return render_template('live_weather.html', weather=weather_data)
    else:
        error_msg = weather_data.get('message', 'Unable to fetch weather data') if weather_data else 'No data received'
        return render_template('live_weather.html', weather=None, error=error_msg)

@main.route('/forecast')
def forecast():
    city = request.args.get('city', 'Pune')  # Optionally get city from query parameter, default Pune
    forecast_data = get_forecast(city)

    # Validate forecast data similarly
    if forecast_data and forecast_data.get('cod') == "200":  # note: forecast API returns cod as string "200"
        return render_template('forecast.html', forecast=forecast_data)
    else:
        error_msg = forecast_data.get('message', 'Unable to fetch forecast data') if forecast_data else 'No data received'
        return render_template('forecast.html', forecast=None, error=error_msg)
    
@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/air-quality')
def air_quality():
    return render_template('air_quality.html')


@main.route('/maps')
def maps():
    return render_template('maps.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')

