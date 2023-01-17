from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "//*[contains(@name, 'firstname')]")
    first_name.send_keys("a")
    last_name = browser.find_element(By.XPATH, "//*[contains(@name, 'lastname')]")
    last_name.send_keys("b")
    email = browser.find_element(By.XPATH, "//*[contains(@name, 'email')]")
    email.send_keys("c")

    file = browser.find_element(By.XPATH, "//*[contains(@id, 'file')]")
    file.send_keys("C:\\Users\\vnkuk\\PycharmProjects\\StepikCourse\\module2\\test.txt")

    button = browser.find_element(By.XPATH, "//*[contains(@type, 'submit')]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла
