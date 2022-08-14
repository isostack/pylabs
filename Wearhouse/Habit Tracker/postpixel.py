from curses.ascii import US
import requests
import datetime
import json
inbound = open("/home/baremetal/Dev Ops/all_tokens.json")
TOKENS =  json.load(inbound)

USERNAME = TOKENS["pixela.com user"]
AUTH_TOKEN = TOKENS["pixela.com auth"]

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
 
headers_data = {
    "X-USER-TOKEN":AUTH_TOKEN
}

pixel_params = {
    "date":datetime.datetime.now().strftime("%Y%m%d"),
    "quantity": '9',
}

pixel_create_response  = requests.post(url = PIXEL_ENDPOINT , json=pixel_params , headers = headers_data)
print(pixel_create_response.text)


 
































