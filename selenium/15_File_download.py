from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os
driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/download')
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'Notes20thApril.pdf').click()
file_path=r"C:\Users\VICTUS\Downloads\Notes20thApril.pdf"
print(os.path.exists(file_path))
