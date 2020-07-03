import requests
import json

city_name = input("enter the name of city: ")
try:
    weatherapi_url = "http://api.openweathermap.org/data/2.5/weather?q=" + str(city_name) + "&appid=05964be4af2fc2a2b7525c680828da7c&units=metric"
    res = requests.get(weatherapi_url)
    r_text = res.text
    weather_data = json.loads(r_text)
    dict_data = weather_data["main"]["temp"]
    print(dict_data)
except KeyError:
    print("incorrect city name")

except Exception as e:
    print("error",e)

