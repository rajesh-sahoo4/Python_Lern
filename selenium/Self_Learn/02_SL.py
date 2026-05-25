# Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver=webdriver.Chrome()
# driver=webdriver.Edge()
driver.get('https://www.saucedemo.com/')
username=driver.find_element(By.ID,'user-name')
username.send_keys('locked_out_user')
time.sleep(5)

driver.quit()