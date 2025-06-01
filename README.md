# 🌤️ Weather Forecast Web App

A simple Flask web application that displays the current weather and 5-day forecast for a city using the OpenWeatherMap API. Users can input a city name and view temperature, weather conditions, and forecast data in a visually appealing interface.

---

## 📁 Project Structure

```
weather-app/
│
├── static/
│   └── img/
│       └── background.jpg         # Background image for the app
│
├── templates/
│   └── index.html                 # Main HTML template
│
├── app.py                        # Flask application
├── .env                          # Environment variables (contains your API key)
└── README.md                     # This file
```

---

## ⚙️ Requirements

Install the following Python packages before running the app:

```bash
pip install flask requests python-dotenv
```

You can also use a `requirements.txt` file:

```text
flask
requests
python-dotenv
```

Save this as `requirements.txt`, then install using:

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup

1. **Clone the repository** (or download the folder):
   ```bash
   git clone https://github.com/JayanthSrinivas06/Weather_Forecast_Basic
   cd weather-app
   ```

2. **Add your API key** to the `.env` file:
   ```
   WEATHER_API_KEY=your_openweathermap_api_key
   ```

   You can get a free API key from: https://openweathermap.org/api

---

## 🚀 Running the App

Run the Flask application using:

```bash
python app.py
```
---

## 🖼️ Features

- Real-time weather data for any city
- 5-day forecast in 3-hour intervals
- Date formatting with filters
- Responsive UI with a background image

---

## 📝 Notes

- Ensure the `.env` file is present in the root directory with a valid API key.
- The background image must be placed in `static/img/` as `background.jpg` (or update the template if named differently).
- Debug mode is enabled by default (`debug=True`). Disable this in production.

---
