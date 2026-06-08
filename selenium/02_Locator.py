# Locator_Partical
from selenium import webdriver  #selenium se webdriver import
from selenium.webdriver.common.by import By  #by locator  import kar raha hai
import time      #time module import
driver=webdriver.Chrome() #open chrome browser driver
driver.maximize_window() # maximize  the browser window
driver.get('https://rahulshettyacademy.com/AutomationPractice/') #open webpage 
# time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='autocomplete']").send_keys('India')#find element in webpage through XPATH Locato & send value automatic
time.sleep(3) #open for 3 second
driver.find_element(By.XPATH,"//input[@id='name']").send_keys('Raju') 
time.sleep(3)
driver.quit() #close the webpage
