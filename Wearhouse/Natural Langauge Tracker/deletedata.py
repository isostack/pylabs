from urllib import request
import requests
import json
inbound = open("/home/baremetal/Dev Ops/all_tokens.json")
TOKENS =  json.load(inbound)
#******************************** VARIABLES  *****************************#
ROW_ID = "4"
SHEET_ENDPOINT = F"https://api.sheety.co/c2508c72b1a9443966fca6445ff27747/workoutTracker/workouts/{ROW_ID}"

#******************************** GOOGLE SHEEET UPDATE/SHEETY  *****************************#

response = requests.delete(SHEET_ENDPOINT)












































