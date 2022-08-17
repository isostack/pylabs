#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
import pandas 

data_mgr = DataManager()
# data_mgr.read_api()
# data_mgr.test_sheet()
searchtool = FlightSearch()
price_data = searchtool.list()
my_prices = pandas.read_csv('main.csv')
deals = []

for index,row in my_prices.iterrows():
    preset_city = row['city']
    preset_price = row['lowestprice']
    for item in price_data:
        if preset_city == item["Arrival City Name"] and preset_price > item["Price"]:
           deals.append(item)
           
out_list = FlightData(deals).stringify()

for item in out_list:
    print(item)      
        
















