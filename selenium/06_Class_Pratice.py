# google search bar se iphone search then iphone 15 locate
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver=webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

search_bar=driver.find_element(By.NAME,"q")
time.sleep(3)
search_bar.send_keys("iphone")
search_bar.send_keys(Keys.ENTER)
time.sleep(3)

results = driver.find_elements(By.TAG_NAME, "h3")

for result in results:
    print(result.text)
    if "iPhone 15" in result.text:
        result.click()
        break
time.sleep(12)
driver.quit()
