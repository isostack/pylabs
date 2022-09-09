
import bs4 
import requests

#------------------------- Scrape Site for data ---------------------------#

URL = "https://housepaging.com/en/gh/?gclid=EAIaIQobChMItrWG8daF-gIVVIjVCh3UBggEEAAYASAAEgKRHvD_BwE"

# Scrape website for rent information/data
response = requests.get(URL)
webpage = response.text
soup = bs4.BeautifulSoup(webpage , "html.parser")
raw_links = soup.select(".listing__content h3 a")
raw_prices = soup.select(".listing__price")
raw_prices = raw_prices[:len(raw_links)]

# Transform data into Names , links and prices
rent_links = [f"https://housepaging.com/en/gh/{item.get('href')}" for item in raw_links]
rent_description = [item.text for item in raw_links]
rent_prices = [item.text for item in raw_prices]

#------------------------- Automated browser for data entry [Selenium] ---------------------------#
DRIVER_PATH = "/home/baremetal/Dev Ops/chromedriver"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSeLNfl7KSO79mpNGTmqiLTX3nsYQBafW--gbFKtTqbNa8wHZA/viewform?usp=sf_link"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(DRIVER_PATH)
driver.implicitly_wait(30)
driver.maximize_window()

driver.get(FORM)

for number in range(len(rent_links)):
    address_inpt = driver.find_element(By.CLASS_NAME , "whs0na")
    address_inpt.send_keys(rent_description[number])

    price_inpt = driver.find_element(By.CLASS_NAME , "whs0nb")
    price_inpt.send_keys(rent_prices[number])

    link_inpt = driver.find_element(By.CLASS_NAME , "whs0nc")
    link_inpt.send_keys(rent_links[number])

    send_btn = driver.find_element(By.CLASS_NAME , "send_btn")
    send_btn.send_keys(Keys.RETURN)



























