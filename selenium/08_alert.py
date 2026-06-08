# alert_Popup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver=webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Alerts.html')
driver.maximize_window()
simple_btn=driver.find_element(By.XPATH,"//button[@class='btn btn-danger']").click()
time.sleep(3)
alert=driver.switch_to.alert
alert.accept()
time.sleep(5)
# Alert with OK & Cancel tab
driver.find_element(By.XPATH,"//a[text()='Alert with OK & Cancel ']").click()
time.sleep(3)
confir_btn=driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
time.sleep(3)
# alert=driver.switch_to.alert
alert.dismiss()
time.sleep(5)
# Alert with Textbox 
driver.find_element(By.XPATH,"//a[contains(text(),'Textbox')]").click()
time.sleep(3)
prompt_btn=driver.find_element(By.XPATH,"//button[@class='btn btn-info']")
prompt_btn.click()
alert=driver.switch_to.alert
alert.send_keys("Rajesh")
alert.text
time.sleep(3)
alert.accept()
time.sleep(3)