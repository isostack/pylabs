import requests
import datetime
import json

# inbound = open("/home/baremetal/Dev Ops/all_tokens.json")
# TOKENS =  json.load(inbound)


#******************************** VARIABLES  *****************************#
APP_ID = "9070a68a"
API_AUTH = "7c6cee291957061f22bb037c8cf9ee84"
NLP_ENPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/c2508c72b1a9443966fca6445ff27747/workoutTracker/workouts"
DATE = datetime.datetime.now().strftime("%Y-%m-%d")
TIME = datetime.datetime.now().strftime("%H:%M:%S")
#******************************** LANGUAGE PROCESSOR  *****************************#
text = input("Enter your exercise: ")
p_params = {
    "query": text
}
h_param = {
    "x-app-id":APP_ID,
    "x-app-key":API_AUTH,
}
track_response = requests.post(NLP_ENPOINT, json=p_params, headers=h_param)
result = track_response.json()

#******************************** GOOGLE SHEEET UPDATE/SHEETY  *****************************#
for exercise in result["exercises"]:
    meta = {
        "workout":{"date": DATE,
        "time": TIME,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
        }
    }
    transfer = requests.post(SHEET_ENDPOINT, json=meta)












































