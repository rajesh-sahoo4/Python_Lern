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
rd_btn=driver.find_element(By.XPATH,"//input[@id='male']")
rd_btn.click()
print(rd_btn.is_selected())
time.sleep(3)
# alert 
simple_btn=driver.find_element(By.ID,"alertBtn").click()
time.sleep(2)
alert=driver.switch_to.alert
alert.accept()
time.sleep(3)
confir_btn=driver.find_element(By.ID,"confirmBtn").click()
time.sleep(5)
alert.dismiss()
time.sleep(3)
prompt_btn=driver.find_element(By.ID,"promptBtn").click()
alert.send_keys("rAJESH")
alert.text
time.sleep(5)
alert.accept()
time.sleep(5)