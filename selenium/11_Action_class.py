from  selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(10)
driver.get('https://demoqa.com/buttons')
action=ActionChains(driver)
# Right_click
# rght_btn=driver.find_element(By.ID,'rightClickBtn')
# print(rght_btn.text)
# action.context_click(rght_btn).perform()   #synatx
# time.sleep(3)
# print(driver.title)
# # elements = driver.find_elements(By.ID, "rightClickMessage")
# # print("Total Elements =", len(elements))
# # time.sleep(5)
# messege=driver.find_element(By.ID,'rightClickMessage')
# print(messege.text)

# Mouse_Hover
# driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# driver.maximize_window()
# action=ActionChains(driver)
# element=driver.find_element(By.ID,'mousehover')
# time.sleep(3)
# action.move_to_element(element).perform()  """synatx"""
# print('mouse hover')

# double_click
duble_btn=driver.find_element(By.ID,'doubleClickBtn')
print(duble_btn.text)
action.double_click(duble_btn).perform()
time.sleep(3)
messege_d=driver.find_element(By.ID,'doubleClickMessage')
Print(messege_d.text)







