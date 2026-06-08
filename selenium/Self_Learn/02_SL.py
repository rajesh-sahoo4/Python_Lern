# Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
# driver=webdriver.Chrome()
driver=webdriver.Edge()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
username=driver.find_element(By.ID,'user-name')
username.send_keys('standard_user')
password=driver.find_element(By.ID,'password')
password.send_keys('secret_sauce')
time.sleep(2)
login=driver.find_element(By.ID,'login-button')
login.click()
time.sleep(2)
# add_to_cart=driver.find_element(By.XPATH,"//button[contains(@id,'add-to-cart-sauce-labs-backpack')]").click()
# time.sleep(4)
# multiple element click
# add_to_carts=driver.find_elements(By.TAG_NAME,'button')
# for add_to_cart in add_to_carts:
#     add_to_cart.click()
#     # print(len(add_to_cart))
# time.sleep(5)


driver.quit() 