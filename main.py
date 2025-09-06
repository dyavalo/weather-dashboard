import requests
import json

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius; change to "imperial" for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels Like: {data['main']['feels_like']}°C")
        print(f"Description: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    elif response.status_code == 404:
        print("City not found. Please check the spelling.")
    else:
        print(f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")

if __name__ == "__main__":
    while True:
        city = input("Enter city name (or 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            break
        get_weather(city)
