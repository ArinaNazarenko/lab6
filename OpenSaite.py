import time 
from selenium import webdriver 
driver = webdriver.Chrome()
time.sleep(5) 
driver.get("https://portal.edu.asu.ru/")
time.sleep(5)
driver.quit()