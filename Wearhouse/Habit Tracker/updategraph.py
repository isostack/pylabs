from curses.ascii import US
import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "quanye"
AUTH_TOKEN = "ACsjdhfasdkfhadoiufhadifuas"

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"

new_params = {
    "unit":"Lessons",
}
headers_data = {
    "X-USER-TOKEN":AUTH_TOKEN
}

graph_create_response  = requests.put(url = GRAPH_ENDPOINT , json=new_params , headers = headers_data)
print(graph_create_response.text)



































