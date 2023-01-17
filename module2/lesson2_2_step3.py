from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.select import Select

link = "https://suninjuly.github.io/selects1.html"


def calc(a, b):
    return str(a+b)


try:
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element(By.ID, "num1")
    b_element = browser.find_element(By.ID, "num2")

    select = Select(browser.find_element(By.TAG_NAME, "select"))

    val = calc(int(a_element.text), int(b_element.text))
    select.select_by_value(val)

    button = browser.find_element(By.XPATH, "//*[contains(@type, 'submit')]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла
