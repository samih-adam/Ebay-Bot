from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.ebay.com/signin/"
driver = webdriver.GoogleChrome()
driver.implicitly_wait(9)
driver.get(url)
driver.maximize_window()
time.sleep(3)

user = driver.find_element(By.ID, "userid")
user.send_keys("Add your email client")
time.sleep(1)
password = driver.find_element(By.ID, "pass")
password.send_keys("Add your password client")
signIn = driver.find_element(By)

