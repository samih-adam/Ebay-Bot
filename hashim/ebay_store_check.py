from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import selenium
import os

chromedriver = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(chromedriver)
url = "https://www.ebay.com/signin/"

driver.implicitly_wait(9)
driver.get(url)
driver.maximize_window()
time.sleep(3)

user = driver.find_element(By.ID, "userid")
user.send_keys("abdels6375@gmail.com")
time.sleep(1)
password = driver.find_element(By.ID, "pass")
password.send_keys("Middleeast98!")
signIn = driver.find_element(By.ID, "sgnBT")
signIn.click()


