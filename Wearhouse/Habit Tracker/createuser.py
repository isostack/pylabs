from curses.ascii import US
import requests
import json
inbound = open("/home/baremetal/Dev Ops/all_tokens.json")
TOKENS =  json.load(inbound)

USERNAME = TOKENS["pixela.com user"]
AUTH_TOKEN = TOKENS["pixela.com auth"]
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": AUTH_TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

user_create_response = requests.post(url = PIXELA_ENDPOINT , json=user_params)
print(user_create_response.text)






































