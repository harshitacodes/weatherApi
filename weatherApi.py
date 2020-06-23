import requests
import json

city_name = input("enter the name of city: ")
weatherapi_url = "http://api.openweathermap.org/data/2.5/weather?q=" + str(city_name) + "&appid=05964be4af2fc2a2b7525c680828da7c&units=metric"
def apiCall(url):
    res = requests.get(url)
    return res.text
res_text = apiCall(weatherapi_url)
weather_data = json.loads(res_text)
dict_data = weather_data["main"]["temp"]
print(dict_data)