from curses.ascii import US
import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "quanye"
AUTH_TOKEN = "ACsjdhfasdkfhadoiufhadifuas"

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



































