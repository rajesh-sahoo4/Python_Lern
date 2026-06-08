from  selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://demoqa.com/buttons')
rght_btn=driver.find_element(By.ID,'rightClickBtn')
print(rght_btn.text)
action=ActionChains(driver)
action.context_click(rght_btn).perform()
time.sleep(3)
print(driver.title)
# elements = driver.find_elements(By.ID, "rightClickMessage")
# print("Total Elements =", len(elements))
# time.sleep(5)
messege=driver.find_element(By.ID,'rightClickMessage')
print(messege.text)

# DEBUG
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.maximize_window()

# driver.get("https://demoqa.com/buttons")

# right_btn = WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.ID,"rightClickBtn")))

# ActionChains(driver).context_click(right_btn).perform()

# message = WebDriverWait(driver,10).until(
#     EC.visibility_of_element_located((By.ID,"rightClickMessage")))

# print(message.text)



# Mouse_Hover

# driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# driver.maximize_window()
# action=ActionChains(driver)
# element=driver.find_element(By.ID,'mousehover')
# time.sleep(3)
# action.move_to_element(element).perform()
# print('mouse hover')


