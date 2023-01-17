from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = int(browser.find_element(By.ID, "input_value").text)
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(calc(x_element))
    cb = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", cb)
    cb.click()
    rb = browser.find_element(By.ID, "robotsRule")
    rb.click()

    button = browser.find_element(By.XPATH, "//*[contains(@type, 'submit')]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла
