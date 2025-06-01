from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv('WEATHER_API_KEY')

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%a, %b %d'):
    """Format datetime string to given format (default: Wed, May 28)."""
    try:
        dt = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return dt.strftime(format)
    except Exception:
        return value

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    current_time = datetime.now().strftime("%A, %d %B %Y | %I:%M:%S %p")
    weather = None
    forecast = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather = get_weather(city)
            forecast = get_forecast(city)
            if not weather or not forecast:
                error = "Could not get weather data. Please check the city name."
        else:
            error = "Please enter a city name."

    return render_template('index.html', current_time=current_time, weather=weather, forecast=forecast, error=error)

if __name__ == '__main__':
    app.run(debug=True)
