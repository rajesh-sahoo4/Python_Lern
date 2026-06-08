# iframe Pratice
from selenium import webdriver #selenium webdriver import
from selenium.webdriver.common.by import By #by locator import 
import time #time import 
driver=webdriver.Chrome() 
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
frame1=driver.find_element(By.ID,"courses-iframe") #page main iframe search
driver.switch_to.frame(frame1) #switch to iframe 
print("switch to frame")
time.sleep(3)
header=driver.find_element(By.XPATH,"//h2")
print(header.text)
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Mentorship").click()
print('clicked mentorship')
time.sleep(3)
heading_mentor=driver.find_element(By.TAG_NAME,'h1')
print(heading_mentor.text)
driver.switch_to.default_content()
print("back to main page")
