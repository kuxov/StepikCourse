import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
class TestClass:
    def test_1(self, browser, link):
        browser.get(link)

        auth_button = WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(@id, 'ember33')]"))
        )
        auth_button.click()

        email_field = WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located((By.ID, "id_login_email"))
        )
        email_field.send_keys("grigoriy@kuksov.com")
        password_field = browser.find_element(By.ID, "id_login_password")
        password_field.send_keys("lu7Mohin")
        login_button = browser.find_element(By.XPATH, "//*[contains(@class, 'sign-form__btn button_with-loader')]")
        login_button.click()

        WebDriverWait(browser, 10).until(
            expected_conditions.invisibility_of_element((By.ID, "id_login_email"))
        )

        answer_field = WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'ember-text-area "
                                                                         "ember-view textarea "
                                                                         "string-quiz__textarea')]"))
        )
        answer = math.log(int(time.time()))
        answer_field.send_keys(answer)

        submit_button = WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "submit-submission"))
        )
        submit_button.click()

        result = WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )

        assert "Correct!" == result.text
