from curses.ascii import US
import requests
import json
inbound = open("/home/baremetal/Dev Ops/all_tokens.json")
TOKENS =  json.load(inbound)

USERNAME = TOKENS["pixela.com user"]
AUTH_TOKEN = TOKENS["pixela.com auth"]
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

GRAPH_ID = "graph1"
DAY = "20220812"

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
 
headers_data = {
    "X-USER-TOKEN":AUTH_TOKEN
}


pixel_create_response  = requests.delete(url = PIXEL_ENDPOINT , headers = headers_data)
print(pixel_create_response.text)


 
































