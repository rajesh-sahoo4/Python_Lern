# open chrome
# open google
# find search bar
# Type FB Login
# press enter
# click facebook link
# facebook page open
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
time.sleep(5)
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("FB Login")
search_box.send_keys(Keys.ENTER)
time.sleep(3)
driver.get("https://www.facebook.com/")
time.sleep(3)

