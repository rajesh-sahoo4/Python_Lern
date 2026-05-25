'''Navigation Scenario
Step 1: Open Chrome browser
Step 2: Navigate to Google
Step 3: Navigate to YouTube
Step 4: go back to Google.
Step 5: go forward to YouTube.
Step 6: refresh the current page (YouTube).
Step 7: Close the browser'''
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://www.google.com')
time.sleep(5)
driver.get('https://www.youtube.com')
time.sleep(5)
driver.back()
driver.refresh()
driver.forward()
driver.quit()

