from urllib import response
import requests


AGE_URL = "https://api.agify.io"
GENDER_URL = "https://api.genderize.io"

age_response = requests.get(AGE_URL, params={"name": "Kevin"})
gender_response = requests.get(GENDER_URL, params={"name": "Kevin"})

print(age_response.json()["age"])
print(gender_response.json()["gender"])