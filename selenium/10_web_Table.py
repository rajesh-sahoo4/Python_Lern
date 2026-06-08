from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time #time import 
driver=webdriver.Chrome() 
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
price=driver.find_elements(By.XPATH,"//table[@name='courses']//tr/td[3]")
for prices in price:
    # print(prices.text)
    if int(prices.text)>=25:
        print(prices.text)
driver.quit()