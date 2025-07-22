from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")

    def fill_checkout_info(self, first: str, last: str, zip_code: str):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name)
        )
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def finish_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_button)
        )
        self.driver.find_element(*self.finish_button).click()
