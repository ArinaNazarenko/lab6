import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://yandex.ru/")
time.sleep(3)

# Ищем поле для ввода текста
textinput = driver.find_element_by_css_selector(".input__input")

textinput.send_keys("Алтайский государственный университет")
time.sleep(3)

submit_button = driver.find_element_by_css_selector(".suggest2-form__button")

submit_button.click()
time.sleep(10)

driver.quit()