from urllib import request
import requests
import datetime
#******************************** VARIABLES  *****************************#

SHEET_ENDPOINT = "https://api.sheety.co/c2508c72b1a9443966fca6445ff27747/workoutTracker/workouts"

#******************************** GET SHEETY API  *****************************#

inbound = requests.get(SHEET_ENDPOINT)
RESULT = inbound.json()

drum = []

for exercise in RESULT["workouts"]:
    date = exercise["date"]
    time = exercise["time"]
    name = exercise["exercise"]
    duration = exercise["duration"]
    calories = exercise["calories"]
    g = f"Date:{date}\nTime:{time}\nExercise:{name}\nDuration:{duration}\nCalories:{calories}"
    drum.append(g)
for item in drum:
    print(item)
        













































