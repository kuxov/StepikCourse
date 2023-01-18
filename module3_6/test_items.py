from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestClassButtonAddToCartExist:
    def test_ButtonAddToCartExists(self, browser):
        browser.get(link)

        button = WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(@type, 'submit')]"))
        )

        assert button is not None
