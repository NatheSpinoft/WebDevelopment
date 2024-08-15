import requests

API_KEY = '0352b9d3715c43c7b234f348c2e8f032'
URL = 'http://api.openweathermap.org/data/2.5/weather?q=Ottawa&appid={API_KEY}'

response = requests.get(URL)
data = response.json()

print("Status Code:", response.status_code)
print("Response Data:", data)
