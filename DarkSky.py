import datetime
import requests
import sys
import time
import winsound
from os import system, name

from colorama import init, Style
from geopy.geocoders import Nominatim

# sync test

init(convert=True)


def clear():
    # for windows 
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def loading(Delay):
    waiting = Delay * 10
    animation = "|/-\\"
    for i in range(waiting):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()


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
    if (337.5 < bearing_angle < 360) or (0 <= bearing_angle <= 22.5):
        direction.direct = "N"
        print("↑", end=" ")
    elif 22.5 < bearing_angle <= 67.5:
        direction.direct = "NE"
        print("↗", end=" ")
    elif 67.5 < bearing_angle <= 112.5:
        direction.direct = "E"
        print("→", end=" ")
    elif 112.5 < bearing_angle <= 157.5:
        direction.direct = "SE"
        print("↘", end=" ")
    elif 157.5 < bearing_angle <= 202.5:
        direction.direct = "S"
        print("↓", end=" ")
    elif 202.5 < bearing_angle <= 247.5:
        direction.direct = "SW"
        print("↙", end=" ")
    elif 247.5 < bearing_angle <= 292.5:
        direction.direct = "W"
        print("←", end=" ")
    elif 292.5 < bearing_angle <= 337.5:
        direction.direct = "NW"
        print("↖", end=" ")
    else:
        pass


def wind_speed(Speed, Direction):
    if Speed >= 64:  # 11-12 BNo.
        print("Wind Speed: " + str(Speed) + Style.RESET_ALL + " mph " + Direction)
    elif 47 <= Speed < 64:  # 9-10 Bno.
        print("Wind Speed: " + str(Speed) + Style.RESET_ALL + " mph " + Direction)
    elif 32 <= Speed < 47:  # 7-8 BNo.
        print("Wind Speed: " + str(Speed) + Style.RESET_ALL + " mph " + Direction)
    elif 19 <= Speed < 32:  # 5-6 BNo.
        print("Wind Speed: " + str(Speed) + Style.RESET_ALL + " mph " + Direction)
    elif 8 <= Speed < 19:  # 3-4 BNo.
        print("Wind Speed: " + str(Speed) + Style.RESET_ALL + " mph " + Direction)
    elif 0 <= Speed < 8:  # 0-2 BNo.
        print("Wind Speed: " + str(Speed) + Style.RESET_ALL + " mph " + Direction)
    else:
        pass


def temperature(Temp_value):
    if Temp_value >= 30:  # very hot
        print("Temp: " + str(Temp_value) + Style.RESET_ALL + " °C")
    elif 23 <= Temp_value < 30:  # hot
        print("Temp: " + str(Temp_value) + Style.RESET_ALL + " °C")
    elif 17 <= Temp_value < 23:  # warm
        print("Temp: " + str(Temp_value) + Style.RESET_ALL + " °C")
    elif 10 <= Temp_value < 17:  # mild
        print("Temp: " + str(Temp_value) + Style.RESET_ALL + " °C")
    elif 1 <= Temp_value < 10:  # cold
        print("Temp: " + str(Temp_value) + Style.RESET_ALL + " °C")
    elif Temp_value < 1:  # very cold
        print("Temp: " + str(Temp_value) + Style.RESET_ALL + " °C")
    else:
        pass


delay = 2

loading(delay)

winsound.PlaySound("open.wav", winsound.SND_ASYNC)

clear()

print("""                                                                            
█ █           █ █   █ █ █ █ █ █ █     █ █ █ █ █    █ █ █ █ █ █ █ █   █ █       █ █   █ █ █ █ █ █ █   █ █ █ █ █ █  
█ █           █ █   █ █             █ █       █ █        █ █         █ █       █ █   █ █             █ █       █ █ 
█ █     █     █ █   █ █ █ █ █       █ █ █ █ █ █ █        █ █         █ █ █ █ █ █ █   █ █ █ █ █       █ █ █ █ █ █   
█ █   █ █ █   █ █   █ █             █ █       █ █        █ █         █ █       █ █   █ █             █ █       █ █ 
  █ █ █   █ █ █     █ █ █ █ █ █ █   █ █       █ █        █ █         █ █       █ █   █ █ █ █ █ █ █   █ █       █ █                                                                                         
""")

address = input("Search: ")
geo_locator = Nominatim(user_agent="Hurleybird Weather")
location = geo_locator.geocode(address)

print(location)
print(location.latitude, location.longitude)

response = requests.get(
    "https://api.darksky.net/forecast/f6c96a08e26624b0fbe900747666a05f/" + str(location.latitude) + "," + str(
        location.longitude) + "?units=uk2")
data = response.json()

# print(response.status_code)
if response.status_code == "200":
    pass
elif response.status_code == "301":
    print("API Server has been redirected.")
elif response.status_code == "401":
    print("User not authenticated to access API.")
    time.sleep(0.5)
    print("Check Secret Key is valid.")
elif response.status_code == "400":
    print("User sent bad request.")
elif response.status_code == "403":
    print("Access to API resources forbidden.")
elif response.status_code == "404":
    print("API resource requested doesn't exist.")
else:
    pass

print("\n")
timeInput = data["currently"]["time"]
epoch(timeInput)
print("Weather: " + data["currently"]["summary"])
rainChance = int(data["currently"]["precipProbability"]) * 100
print("Chance of rain: " + str(rainChance) + "%")
temp2 = data["currently"]["temperature"]
temp = round(temp2, 0)
temperature(temp)
bearing = data["currently"]["windBearing"]
direction(bearing)
windSpeed = data["currently"]["windSpeed"]
speed = round(windSpeed, 0)
wind_speed(int(speed), direction.direct)

input("\nPress ENTER to exit.")
