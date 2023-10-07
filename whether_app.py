import requests
import json

# Constants for the API
API_KEY = " 862076cbfe7636f46375c65c38404792" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
def get_current_weather(location):
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Error fetching weather data.")
        return None
def display_weather(weather_data):
    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        weather_condition = weather_data['weather'][0]['description']

        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} m/s')
        print(f'Weather Condition: {weather_condition}')
    else:
        print('No weather data available.')
def main():
    while True:
        location = input("Enter a location (city, country): ")

        if location.lower() == 'exit':
            break

        weather_data = get_current_weather(location)

        if weather_data:
            display_weather(weather_data)


if __name__ == "__main__":
    main()

