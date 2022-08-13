from curses.ascii import US
import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "quanye"
AUTH_TOKEN = "ACsjdhfasdkfhadoiufhadifuas"
GRAPH_ID = "graph1"
DAY = "20220812"

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{DAY}"
 
headers_data = {
    "X-USER-TOKEN":AUTH_TOKEN
}


pixel_create_response  = requests.delete(url = PIXEL_ENDPOINT , headers = headers_data)
print(pixel_create_response.text)


 
































