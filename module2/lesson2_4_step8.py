from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    answer = browser.find_element(By.XPATH, "//*[contains(@id, 'answer')]")
    x = int(browser.find_element(By.ID, "input_value").text)
    answer.send_keys(calc(x))

    submit = browser.find_element(By.XPATH, "//*[contains(text(), 'Submit')]")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла
