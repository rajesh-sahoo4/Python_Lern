from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# driver.save_screenshot('homepage.png')   #whole_page_screenshot
driver.save_screenshot(r"C:\Users\VICTUS\Desktop\python\selenium\image\homepage.png")
# time.sleep(3)
text_box=driver.find_element(By.ID,'name')
# text_box.screenshot('textbox.png')  #Perticular element screenshot
text_box.screenshot(r"C:\Users\VICTUS\Desktop\python\selenium\image\img2.png")
# text_box.screenshot(r"C:\Users\VICTUS\Pictures\Screenshots\text.png") #pertucular folder save
driver.quit()