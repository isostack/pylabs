import requests
import datetime as dt

MY_LAT = 5.602860
MY_LONG = -0.231150
SUNSET = "2022-08-04T18:18:36+00:00" 
SUNRISE = "2022-08-04T05:55:29+00:00"

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# is_data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# position = (longitude, latitude)

# print(position)

# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0
# }

# response = requests.get(url="https://api.sunrise-sunset.org/json", params = parameters, verify=False )
# response.raise_for_status()

# sunrise_data = response.json()
# sunrise = sunrise_data["results"]["sunrise"]
# sunset = sunrise_data["results"]["sunset"]

time_now = dt.datetime.now()
green = SUNSET[11:13]

print(time_now.hour)

