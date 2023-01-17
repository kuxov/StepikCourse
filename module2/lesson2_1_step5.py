from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    element1 = browser.find_element(By.ID, "answer")
    element1.send_keys(y)

    element2 = browser.find_element(By.ID, "robotCheckbox")
    element2.click()

    element3 = browser.find_element(By.ID, "robotsRule")
    element3.click()

    button = browser.find_element(By.XPATH, "//*[contains(@type, 'submit')]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла
