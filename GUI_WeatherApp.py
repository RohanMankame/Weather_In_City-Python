import tkinter as tk
import requests
#_____________________________________________________________________________________________________________________________
# get the weather information function
def get_weather_info(event):
    city_name = city_entry.get()
    # API call to the WeatherAPI.
    url = f"https://api.weatherapi.com/v1/current.json?key=b7761a8837d242f687a190252232405&q={city_name}&aqi=no"
    r = requests.get(url).json()
    # Get the current temperature from the weather JASON .
    current_temperature = r['current']['temp_f']
    temperature_entry.insert(0, current_temperature)


#__________________________________________________________________________________________________________________________

# Create a GUI.
window = tk.Tk()
city_label = tk.Label(text="City Name")
city_entry = tk.Entry()
temperature_label = tk.Label(text="Current Temperature")
temperature_entry = tk.Entry()
get_weather_button = tk.Button(text="Get Weather Information")
get_weather_button.bind("<Button-1>", get_weather_info)

# Layout in the GUI.
city_label.grid(row=0, column=0)
city_entry.grid(row=0, column=1)
temperature_label.grid(row=1, column=0)
temperature_entry.grid(row=1, column=1)
get_weather_button.grid(row=2, column=0)

#STARTING THE LOOP
window.mainloop()