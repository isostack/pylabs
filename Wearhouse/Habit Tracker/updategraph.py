from curses.ascii import US
import requests
import json
inbound = open("/home/baremetal/Dev Ops/all_tokens.json")
TOKENS =  json.load(inbound)

USERNAME = TOKENS["pixela.com user"]
AUTH_TOKEN = TOKENS["pixela.com auth"]

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"

new_params = {
    "unit":"Lessons",
}
headers_data = {
    "X-USER-TOKEN":AUTH_TOKEN
}

graph_create_response  = requests.put(url = GRAPH_ENDPOINT , json=new_params , headers = headers_data)
print(graph_create_response.text)



































