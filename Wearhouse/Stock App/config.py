
import json


#***************************** EQUITY DATA ****************************************#
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
import requests

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_AUTH
}
stock_endpoint = 'https://www.alphavantage.co/query'
stock_r = requests.get(stock_endpoint, params = stock_params)
stock_api = stock_r.json()["Time Series (Daily)"]
stock_list = [value for  key,value in stock_api.items()]
data_one = stock_list[0]
data_one_closing = float(data_one["4. close"])
data_two = stock_list[1]
data_two_closing = float(data_two["4. close"])
    

difference = abs(data_one_closing - data_two_closing)
diff_percent = int((difference / data_one_closing) * 100)

     
#***************************** NEWS DATA ****************************************#

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


if diff_percent > 1:
    news_params = {
    "apiKey":NEWS_AUTH,
    "qInTitle":COMPANY_NAME
    }
    news_url = f'https://newsapi.org/v2/everything'
    news_r = requests.get(news_url , params = news_params)
    news_api = news_r.json()['articles']
    news_list = news_api[:3]
    paragraph = [f"Headline:{item['title']}\nDescription:{item['description']}" for item in news_list]
    news_paragraph = "\n\n".join(paragraph)
up = "🔺"
down = "🔻"

if data_one_closing - data_two_closing > 0:
    final_paragraph = f"{STOCK}: {up}{diff_percent}%\n\n{news_paragraph}"
else:
    final_paragraph = f"Miami\n{STOCK}: {down}{diff_percent}%\n\n{news_paragraph}"

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
from twilio.rest import Client

client = Client(TWILIO_SID, TWILIO_AUTH)

message = client.messages \
                .create(
                     body=final_paragraph,
                     from_='+14255841393',
                     to='+233203053368'
                 )

print(message.status)
print(final_paragraph)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


