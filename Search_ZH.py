import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://portal.edu.asu.ru/")
time.sleep(5)
textinput = driver.find_element_by_css_selector(".search-box__input")
textinput.send_keys("О.В. Журенков")
time.sleep(5)
submit_button = driver.find_element_by_css_selector(".search-box__button")
submit_button.click()
time.sleep(15)
driver.quit()