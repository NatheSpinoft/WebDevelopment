import requests

API_KEY = '0352b9d3715c43c7b234f348c2e8f032'
CITY = 'Ottawa'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

response = requests.get(URL)
data = response.json()

kelvin_temp = data['main']['temp']
celsius_temp = kelvin_temp - 273.15

if response.status_code == 200:
    print(f"City: {data['name']}")
    print(f"Temperature: {celsius_temp:.2f}°C")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print(f"Error: {data['message']}")
