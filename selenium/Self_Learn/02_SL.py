# Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
# driver=webdriver.Chrome()
driver=webdriver.Edge()
driver.get('https://www.saucedemo.com/')
username=driver.find_element(By.ID,'user-name')
username.send_keys('standard_user')
password=driver.find_element(By.ID,'password')
password.send_keys('secret_sauce')
time.sleep(5)
login=driver.find_element(By.ID,'login-button')
login.click()
time.sleep(4)
driver.quit() 