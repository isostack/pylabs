from curses.ascii import US
import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": "ACsjdhfasdkfhadoiufhadifuas",
    "username":"quanye",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

user_create_response = requests.post(url = PIXELA_ENDPOINT , json=user_params)
print(user_create_response.text)






































