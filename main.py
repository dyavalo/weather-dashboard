import requests
import json

API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
    else:
        print("City not found or API error.")

city = input("Enter city name: ")
get_weather(Almaty)
