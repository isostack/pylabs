driver_location = "/home/baremetal/baremetals/chromedriver"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org/")

events = driver.find_elements(By.CSS_SELECTOR , '.event-widget .menu a')
dates = driver.find_elements(By.CSS_SELECTOR , '.event-widget .menu time')

drum = { number: {'time':dates[number].text , 'name':events[number].text} for number in range(len(events)) }

print(drum)

driver.quit()




