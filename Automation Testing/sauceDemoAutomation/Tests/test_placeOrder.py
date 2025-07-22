from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
import time

def test_place_order(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")


    products = ProductsPage(driver)
    products.add_item_to_cart()
    products.go_to_cart()

    cart = CartPage(driver)
    cart.proceed_to_checkout()
    checkout = CheckoutPage(driver)

    checkout.fill_checkout_info("John", "Doe", "12345")

    checkout.finish_order()


    assert "checkout-complete" in driver.current_url
    driver.get("https://www.saucedemo.com/inventory.html")
    products.logout()

