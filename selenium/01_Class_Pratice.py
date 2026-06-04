# Navigation
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://google.com')
# time.sleep(2)
# driver.get('https://amazon.in')
# time.sleep(2)
# driver.minimize_window()
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# driver.quit()

#google  

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Open Chrome Browser
# driver = webdriver.Chrome()

# # Open Google
# driver.get("https://www.google.com")

# # Maximize window
# driver.maximize_window()

# # Find Google search box
# search_box = driver.find_element(By.NAME, "q")

# # Search for iPhone models
# search_box.send_keys("iPhone all models")
# search_box.send_keys(Keys.ENTER)

# # Wait for results to load
# time.sleep(3)

# # Click on iPhone 15 link
# iphone15 = driver.find_element(
#     By.XPATH,
#     "//h3[contains(text(),'iPhone 15')]"
# )

# iphone15.click()

# # Wait to see result
# time.sleep(5)

# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
# for check single checkbox
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
# checkbox=driver.find_element(By.NAME,"checkBoxOption1")
# checkbox.click()
# print(checkbox.is_selected())
# time.sleep(2)

# for multiple checkbox
# checkboxes=driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
# for checkbox in checkboxes:
#  checkbox.click()
# #  print(checkboxes.is_selected())
# time.sleep(3)
# driver.quit()
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# print(len(checkboxes))

# radio btn
# for single radio btn
rd_btn=driver.find_element(By.XPATH,"//input[@value='radio1']")
rd_btn.click()
print(rd_btn.is_selected())
time.sleep(2)

