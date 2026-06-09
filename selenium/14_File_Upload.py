# 01
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/upload')
driver.maximize_window()
driver.find_element(By.ID,'file-upload').send_keys(r"C:\Users\VICTUS\Downloads\API_Testing_Cheat_Sheet.pdf")
# submit
driver.find_element(By.ID,'file-submit').submit()
print('upload done')
time.sleep(3)

# 02
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time 
# driver=webdriver.Chrome()
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()
# driver.find_element(By.ID,"singleFileInput").send_keys(r"C:\Users\VICTUS\Downloads\LLM_AI_Study_Notes.pdf")
# driver.find_element(By.XPATH,"//button[text()='Upload Single File']").click()
# print('upload sucessfully')
# time.sleep(3)
# driver.quit()
