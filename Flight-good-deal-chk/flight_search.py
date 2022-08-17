import json

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        filr = open('prices.json' , 'r')
        self.meta = json.load(filr)
        filr.close()
    def list(self):
        list = self.meta["outbound"]
        return list 
