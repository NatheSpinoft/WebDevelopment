import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(api_key, city):
    """Fetch the weather data from OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit, 'metric' for Celsius
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather():
    """Fetch and display the weather information."""
    api_key = '0352b9d3715c43c7b234f348c2e8f032'  # Replace with your OpenWeatherMap API key
    city = city_entry.get()
    
    if city:
        weather_data = get_weather(api_key, city)
        if weather_data and weather_data.get('cod') == 200:
            city_name = weather_data['name']
            temp = weather_data['main']['temp']
            weather = weather_data['weather'][0]['description']
            result_label.config(text=f"Weather in {city_name}:\nTemperature: {temp}°C\nCondition: {weather.capitalize()}")
        else:
            messagebox.showerror("Error", "City not found or unable to retrieve data.")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# Set up the GUI
root = tk.Tk()
root.title("Weather Application")

# Create and place widgets
tk.Label(root, text="Enter city name:").pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=display_weather).pack(pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=10)

# Run the GUI event loop
root.mainloop()
