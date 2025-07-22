from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def logout(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        ).click()
