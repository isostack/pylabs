import config
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import sys
import os

browser = webdriver.Edge('C:\msedgedriver.exe')

#browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1%2526wlexpsignin%253d1%26sig%3d01D7E673413C617A0FA2F703409A604F&wp=MBI_SSL&lc=1033&CSRFToken=46e07320-9163-4417-beba-331c374dff51&aadredir=1')

browser.get('https://www.bing.com/?cc=fr')

# email = browser.find_element_by_xpath('//*[@id="i0116"]')

# email.send_keys('dezynarh@gmail.com')

# time.sleep(1)

# next = browser.find_element_by_xpath('//*[@id="idSIButton9"]')

# next.click()

# time.sleep(1)

# password = browser.find_element_by_xpath('//*[@id="i0118"]')

# password.send_keys('Tylenol123')

# time.sleep(1)

# next = browser.find_element_by_xpath('//*[@id="idSIButton9"]')

# next.click()

# time.sleep(1)

# next = browser.find_element_by_xpath('//*[@id="idSIButton9"]')

# next.click()

words1 = ['alpha', 'the', 'beta', 'an', 'fries', 'can', 'game', 'jack', 'of',
          'ink', 'is', 'gamma', 'to', 'charlie', 'a', 'hog', 'so', 'into', 'lick', 'that']

time.sleep(1)


for i in range(5):

    searchbar = browser.find_element_by_xpath('//*[@id="sb_form_q"]')

    some = words1[random.randint(0, 19)] + ' '

    searchbar.send_keys(some)

    time.sleep(2) 

    searchbar.send_keys(Keys.ENTER)

os.system("taskkill /im msedge.exe /f")

os.system("taskkill /im py.exe /f")
