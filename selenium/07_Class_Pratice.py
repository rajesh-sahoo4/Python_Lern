from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver=webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
# for single use 
# checkbox=driver.find_element(By.ID,'sunday')
# checkbox.click()
# print(checkbox.is_selected())
# time.sleep(3)

# for multiple use
days=driver.find_elements(By.XPATH,"//div[@class='form-group']//input[@type='checkbox']")
for day in days:
    day.click()
time.sleep(3)