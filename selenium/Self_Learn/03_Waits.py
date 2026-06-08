from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.firefox()
print('Browser opened')

driver.maximize_window()
print('Browser maximized')
driver.get('https://www.duckduckgo.com')
print('Browser opened')

search_box=driver.find_element(By.NAME,'q')
search_box.send_keys("selenium")
search_box.send_keys()
