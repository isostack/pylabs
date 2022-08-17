class FlightData():
    #This class is responsible for structuring the flight data.
    def __init__(self , deals):
        self.deals = deals
        self.brown = ["You have the following deals:\n"]
        
    def stringify(self):
        #This method will take the deals and stringify them.
        if len(self.deals) == 0:
            self.brown.clear()
            self.brown.append("There are no good deals found according to your prices.")
        else:
            for item in self.deals:
                indigo = f"Price: {item['Price']}\nDeparture City Name: {item['Departure City Name']}\nDeparture Airport IATA Code: {item['Departure Airport IATA Code']}\nArrival City Name: {item['Arrival City Name']}\nArrival Airport IATA Code: {item['Arrival Airport IATA Code']}\nOutbound Date: {item['Outbound Date']}\nInbound Date: {item['Inbound Date']}"
                self.brown.append(indigo)
        return self.brown


