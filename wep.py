import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = 'cc1c8c16dc414858a9e90359250303'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

def get_weather(city):
    params = {
        'key': API_KEY,
        'q': city
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def show_weather():
    city = city_entry.get()
    weather = get_weather(city)
    
    if 'error' in weather:
        messagebox.showerror("Error", weather['error']['message'])
        return
    
    temperature = weather['current']['temp_c']
    description = weather['current']['condition']['text']
    weather_label.config(text=f"{city} \n Temperature: {temperature}°C\nDescription: {description}")


root = tk.Tk()
root.title("Weather App")


city_label = tk.Label(root, text="Enter city name:")
city_label.pack(pady=5)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=show_weather)
get_weather_button.pack(pady=10)

weather_label = tk.Label(root, text="", font=("Helvetica", 14))
weather_label.pack(pady=20)


root.mainloop()