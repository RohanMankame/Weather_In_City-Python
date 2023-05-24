
# USED WeatherAPI for getting realtime weather infomation #
# !!!IMPORTANT MY API KEY expires on June 7th due to me using a free trial!!!#
import requests
#request user for the city they want to get info of
City_Name = input("Enter city name to check weather: ")
#set url from where API gets Info
url = f"https://api.weatherapi.com/v1/current.json?key=b7761a8837d242f687a190252232405&q={City_Name}&aqi=no"#allow city name to be passed from user

r = requests.get(url).json() #retrives all the data and accepts it as a json
#we now have a dictionary of the real time info at the city the user entered

Temp_Fahrenheit = r['current']['temp_f']
Temp_Celcius = r['current']['temp_c']
print(f"The temperature in {City_Name} is: " + str(Temp_Fahrenheit) + " Fahrenheit which is " + str(Temp_Celcius)+" Celcius")


