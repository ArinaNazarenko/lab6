import time
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://google.ru/")
time.sleep(5)

# С помощью find_element_by_css_selector находим нужный нам элемент. у нас это поисковая строка
textinput = driver.find_element_by_css_selector(".gLFyf")

# Напишем текст для поиска в найденное поле
textinput.send_keys("АГУ")
time.sleep(3)

# Так же находим нужный нам элемент, теперь это кнопка поиска. 
submit_button = driver.find_element_by_css_selector(".gNO89b")

# Нажатие кнопки. 
submit_button.click()
time.sleep(10)

# Закрываем окно
driver.quit()