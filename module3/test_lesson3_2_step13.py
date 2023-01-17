import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestClass3(unittest.TestCase):
    def test_1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your first name')]")
            input1.send_keys("q")
            input2 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your last name')]")
            input2.send_keys("q")
            input3 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your email')]")
            input3.send_keys("q")
            input4 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your phone:')]")
            input4.send_keys("q")
            input5 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your address:')]")
            input5.send_keys("q")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(2)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your first name')]")
            input1.send_keys("q")
            input2 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your last name')]")
            input2.send_keys("q")
            input3 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your email')]")
            input3.send_keys("q")
            input4 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your phone:')]")
            input4.send_keys("q")
            input5 = browser.find_element(By.XPATH, "//*[contains(@placeholder, 'Input your address:')]")
            input5.send_keys("q")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(2)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == '__main__':
    unittest.main()
