import requests

aiti_data =  ["PAR","BER","TYO","SYD","IST","KUL","NYC","SFO","CPT","ACC"]

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/c2508c72b1a9443966fca6445ff27747/flightDealz/prices"
        self.response = ""
        self.transfer = ""
        
    def read_api(self):
        self.response = requests.get(self.endpoint)
        print(self.response.json())
        
    def test_sheet(self):
        id = 2
        for item in aiti_data:         
            urlin = f"{self.endpoint}/{id}"
            meta = {
                "price": {"iataCode": item}
            }
            transfer = requests.put(url = urlin , json=meta)
            print(transfer.status_code)
            id += 1




    
