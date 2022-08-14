import requests
import git 

APP_ID = "9070a68a"
API_AUTH = "7c6cee291957061f22bb037c8cf9ee84"
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

text = input("Enter your exercise: ")

p_params = {
    "query": text
}

h_param = {
    "x-app-id":APP_ID,
    "x-app-key":API_AUTH,
}

track_response = requests.post(URL, json=p_params, headers=h_param)
result = track_response.json()

drum = []

for exercise in result["exercises"]:
    name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    meta = f"Workout:{name}\nDuration:{duration}\nCalories Burnt: {calories}"
    drum.append(meta)

for item in drum:
    print(item)
    print("\n")











































