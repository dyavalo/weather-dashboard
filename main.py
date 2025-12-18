import requests

API_KEY = 'YOUR_API_KEY_HERE'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city: ")

params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f"Temperature in {city}: {temp}°C")
    print(f"Description: {desc}")
else:
    print("couldnt find city or wrong key")
