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
mail_inpt.send_keys("frederickohene007@gmail.com")
pass_inpt = driver.find_element(By.XPATH , '//*[@id="password"]')
pass_inpt.send_keys("Pradah123")
log_in_btn = driver.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[3]/button')
log_in_btn.click()

#========================= Make job search ===============#
search = driver.find_element(By.XPATH , '//*[@id="global-nav-typeahead"]/input')
search.send_keys("Php developer")
search.send_keys(Keys.RETURN)

import time
time.sleep(5)




