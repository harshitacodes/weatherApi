# import requests
# import json


# city_name = input("enter the name of city: ")
# try:
#     weatherapi_url = "http://api.openweathermap.org/data/2.5/weather?q=" + str(city_name) + "&appid=05964be4af2fc2a2b7525c680828da7c&units=metric"
#     res_text = requests.get(weatherapi_url)
#     weather_data = json.loads(res_text)
#     temperature = weather_data["main"]["temp"]
#     print(temperature)
    
# #     # print(res_text)
# # except:
# #     print("internet is not working")
# # try:
# #     weather_data = json.loads(res_text)
# #     temperature = weather_data["main"]["temp"]
# #     print(temperature)
    
# except:
#     print("incorrect city name")


 
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

except:
    print("internet is not working")

