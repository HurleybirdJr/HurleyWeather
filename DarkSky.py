# https://docs.python.org/3/library/time.html#time.struct_time

# TODO: Add comparison tool for 2 locations
#       > Add button to enable comparison mode
#       > Highlight difference with red and blue transparent

import datetime
import requests
import sys
import time
import json
import random

from geopy.geocoders import Nominatim


def animation_generator(length):
    while True:
        for n in range(length + 1):
            yield '[' + ' ' * n + '=' + ' ' * (length - n) + ']'
        for n in range(length + 1):
            yield '[' + ' ' * (length - n) + '=' + ' ' * n + ']'


def loading():
    animation = animation_generator(6)
    for i in range(random.randint(30, 120)):
        sys.stdout.write('\r')
        sys.stdout.write(animation.__next__())
        sys.stdout.flush()
        time.sleep(0.01667)


# class colours:
#   red = '\033[31m'
#   orange = '\033[32m'
#   yellow = '\033[93m'
#   green = '\033[92m'
#   lightBlue = '\033[94m'
#   blue = '\033[34m'

def epoch(time_input):
    timestamp = int(time_input)
    value = datetime.datetime.fromtimestamp(timestamp)
    print("Time = " + value.strftime('%H:%M:%S'))


def direction(bearing_angle):
    bearing_angle += 180
    if (337.5 < bearing_angle < 360) or (0 <= bearing_angle <= 22.5):
        return "↑"
    elif 22.5 < bearing_angle <= 67.5:
        return "↗"
    elif 67.5 < bearing_angle <= 112.5:
        return "→"
    elif 112.5 < bearing_angle <= 157.5:
        return "↘"
    elif 157.5 < bearing_angle <= 202.5:
        return "↓"
    elif 202.5 < bearing_angle <= 247.5:
        return "↙"
    elif 247.5 < bearing_angle <= 292.5:
        return "←"
    elif 292.5 < bearing_angle <= 337.5:
        return "↖"
    else:
        pass


def wind_speed(speed, bearing_value):
    if speed >= 64:  # 11-12 BNo.
        print("Wind: " + str(speed) + " mph " + str(direction(bearing_value)))
    elif 47 <= speed < 64:  # 9-10 Bno.
        print("Wind: " + str(speed) + " mph " + str(direction(bearing_value)))
    elif 32 <= speed < 47:  # 7-8 BNo.
        print("Wind: " + str(speed) + " mph " + str(direction(bearing_value)))
    elif 19 <= speed < 32:  # 5-6 BNo.
        print("Wind: " + str(speed) + " mph " + str(direction(bearing_value)))
    elif 8 <= speed < 19:  # 3-4 BNo.
        print("Wind: " + str(speed) + " mph " + str(direction(bearing_value)))
    elif 0 <= speed < 8:  # 0-2 BNo.
        print("Wind: " + str(speed) + " mph " + str(direction(bearing_value)))
    else:
        pass


# def temperature(Temp_value):
#     if Temp_value >= 30:  # very hot
#         print("Temp: " + str(Temp_value) + "°C")
#     elif 23 <= Temp_value < 30:  # hot
#         print("Temp: " + str(Temp_value) + "°C")
#     elif 17 <= Temp_value < 23:  # warm
#         print("Temp: " + str(Temp_value) + "°C")
#     elif 10 <= Temp_value < 17:  # mild
#         print("Temp: " + str(Temp_value) + "°C")
#     elif 1 <= Temp_value < 10:  # cold
#         print("Temp: " + str(Temp_value) + "°C")
#     elif Temp_value < 1:  # very cold
#         print("Temp: " + str(Temp_value) + "°C")
#     else:
#         pass


def get_status(api_response):
    print(response.status_code)  # Return code via console
    if api_response.status_code == 200:
        pass
    elif api_response.status_code == 301:
        print("API Server has been redirected.")
    elif api_response.status_code == 401:
        print("User not authenticated to access API.")
        time.sleep(0.5)
        print("Check Secret Key is valid.")
    elif api_response.status_code == 400:
        print("User sent bad request.")
    elif api_response.status_code == 403:
        print("Access to API resources forbidden.")
    elif api_response.status_code == 404:
        print("API resource requested doesn't exist.")
    else:
        print("get_status function logic error")
        pass


def standard_api(location):
    location_coords = obtain_coords(location)

    response = requests.get(
        "https://api.darksky.net/forecast/f6c96a08e26624b0fbe900747666a05f/" +
        str(location_coords.latitude) + "," +
        str(location_coords.longitude) +
        "?units=uk2"
    )

    return response


def time_machine_api(location):
    print("Format: [DAY]/[MONTH]/[YEAR] [24HOUR]:[MINUTE]:[SECOND]")
    print("Ex: 29/06/2018 15:34:10")

    user_time_input = input(">: ")

    try:
        time.strptime(user_time_input, "%d/%m/%Y %H:%M:%S")
        tt_time = 
    finally:
        print("done")

    location_coords = obtain_coords(location)

    response = requests.get(
        "https://api.darksky.net/forecast/f6c96a08e26624b0fbe900747666a05f/" +
        str(location_coords.latitude) + "," +
        str(location_coords.longitude) +
        "time" + "?units=uk2"
    )

    return response


def obtain_coords(location):
    geo_locator = Nominatim(user_agent="Hurleybird Weather")
    return geo_locator.geocode(location)


# print(location)
# print(location.latitude, location.longitude)

search_location = input("Location?: ")

data = response.json()

# Saves most recent search results in same directory for comparison
with open("recent_data.json", 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

get_status(response)

loading()

print("\n")
epoch(data["currently"]["time"])
print("Weather: " + data["currently"]["icon"])
print("Temp: " + str(int(round(data["currently"]["temperature"], 0))) + "°C")
print("Precip: " + str(int(data["currently"]["precipProbability"]) * 100) + "%")
wind_speed(int(round(data["currently"]["windSpeed"], 0)), data["currently"]["windBearing"])
print("Pressure: " + str(int(round(data["currently"]["pressure"], 0))) + " hPa")
print("Humidity: " + str(int(data["currently"]["humidity"]) * 100) + "%")
print("Dew Pt: " + str(int(round(data["currently"]["dewPoint"], 0))) + "°C")
print("UV Index: " + str(int(data["currently"]["uvIndex"])))
print("Visibility: " + str(int(data["currently"]["visibility"])))
