driver_location = "/home/baremetal/baremetals/chromedriver"
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver.get("https://www.linkedin.com")
#========================= Login =========================#
sign_in_btn = driver.find_element(By.XPATH , '/html/body/nav/div/a[2]')
sign_in_btn.click()
mail_inpt = driver.find_element(By.XPATH , '//*[@id="username"]')
mail_inpt.send_keys("")
pass_inpt = driver.find_element(By.XPATH , '//*[@id="password"]')
pass_inpt.send_keys("")
log_in_btn = driver.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[3]/button')
log_in_btn.click()

#========================= Make job search ===============#
search = driver.find_element(By.XPATH , '//*[@id="global-nav-typeahead"]/input')
search.send_keys("Php developer")
search.send_keys(Keys.RETURN)

import time
time.sleep(5)

# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# # get the path of ChromeDriverServer
# chrome_driver_path = "/home/baremetal/baremetals/chromedriver"

# # create a new Chrome session
# driver = webdriver.Chrome(chrome_driver_path)
# driver.implicitly_wait(30)
# driver.maximize_window()

# # navigate to the application home page
# driver.get("http://www.google.com")

# # get the search textbox
# search_field = driver.find_element(By.NAME, "q")

# # enter search keyword and submit
# search_field.send_keys("Selenium WebDriver Interview questions")
# search_field.submit()



