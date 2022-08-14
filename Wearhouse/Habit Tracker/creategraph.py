from curses.ascii import US
import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
import json
inbound = open("/home/baremetal/Dev Ops/all_tokens.json")
TOKENS =  json.load(inbound)

USERNAME = TOKENS["pixela.com user"]
AUTH_TOKEN = TOKENS["pixela.com auth"]

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_params = {
    "id":"graph1",
    "name":"Piano Lessons",
    "unit":"Commits",
    "type":"float",
    "color":"ajisai",
} 

headers_data = {
    "X-USER-TOKEN":AUTH_TOKEN
}

graph_create_response  = requests.post(url = GRAPH_ENDPOINT , json=graph_params , headers = headers_data)
print(graph_create_response.text)



































