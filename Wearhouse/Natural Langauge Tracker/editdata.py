import requests
import json

inbound = open("/home/baremetal/Dev Ops/all_tokens.json" , "r")
TOKENS =  json.load(inbound)

#******************************** VARIABLES  *****************************#
APP_ID = TOKENS["nutritionix.com id"]
API_AUTH = TOKENS["nutritionix.com auth"]
NLP_ENPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
ROW_ID = "4"
SHEET_ENDPOINT = F"https://api.sheety.co/c2508c72b1a9443966fca6445ff27747/workoutTracker/workouts/{ROW_ID}"

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
        "workout":{
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
        }
    }
    transfer = requests.put(SHEET_ENDPOINT, json=meta)












































