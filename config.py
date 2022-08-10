import requests
import hourly

# endpoint = "https://api.openweathermap.org/data/3.0/onecall"
# api_key = '40e7987b75c52fe5f40c2e2ff17ac805'
# parameters = {
#     "lat": 5.551167,
#     "lon": 0.200450,
#     "appid": api_key,
# }

# response = requests.get(endpoint, params=parameters)
# response.raise_for_status() 
# print(response.json())

h_data_main = hourly.hour_data[:10]

will_rain = False

condition_codes = [item["weather"][0]["id"] for item in h_data_main]
for item in condition_codes:
    if item < 700:
        will_rain = True 

if will_rain:
    print("Bring an umbrella")

