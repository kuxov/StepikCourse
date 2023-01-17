from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, "//*[contains(text(), 'I want to go on a magical journey!')]")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    answer = browser.find_element(By.XPATH, "//*[contains(@id, 'answer')]")
    x = int(browser.find_element(By.ID, "input_value").text)
    answer.send_keys(calc(x))

    submit = browser.find_element(By.XPATH, "//*[contains(@type, 'submit')]")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла
