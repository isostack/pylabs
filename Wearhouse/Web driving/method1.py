import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# get the path of ChromeDriverServer
chrome_driver_path = "/home/baremetal/baremetals/chromedriver"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element(By.NAME, "q")

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

