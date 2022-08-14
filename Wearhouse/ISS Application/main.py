import requests
from datetime import datetime
import smtplib
import json
inbound = open("/home/baremetal/Dev Ops/all_tokens.json")
TOKENS =  json.load(inbound)

USERNAME = TOKENS["outlook.com mail"]
AUTH_TOKEN = TOKENS["outlook.com pass"]

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
SUNSET = "2022-08-04T07:18:36+00:00" 
SUNRISE = "2022-08-04T05:55:29+00:00"
sunrise = int(SUNRISE[11:13])
sunset = int(SUNSET[11:13])

M_GATEWAY = "ezea739@gmail.com"
SMTP = "smtp-mail.outlook.com"
PORT = 587

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude <= MY_LAT-5 or iss_latitude >= MY_LAT+5 and iss_longitude <= MY_LONG-5 or iss_longitude >= MY_LONG+5:
        return True
    else:
        return True

#Your position is within +5 or -5 degrees of the ISS position.

# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0,
# }

# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def is_night():
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False

if is_overhead() and is_night():
    server = smtplib.SMTP(SMTP, PORT)
    server.ehlo()
    server.starttls()
    server.login(USERNAME, AUTH_TOKEN)
    server.sendmail(USERNAME, M_GATEWAY, "Subject: ISS is overhead.\n\nThe ISS is overhead.")
    print("Email sent.")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



