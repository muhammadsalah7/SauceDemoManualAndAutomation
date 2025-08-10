## 🧪 **SauceDemo Automation & Manual Testing**

This project  includes both **manual testing documentation** and a **Selenium-based automation script** for the [SauceDemo](https://www.saucedemo.com/) web application.

---

## 🚀 **Automation Scenario**

The automation script simulates a full user journey:

- Login with valid credentials  
- Add an item to the cart  
- Proceed to checkout  
- Complete the order  
- Log out  

The script is built using **Python** and **Selenium WebDriver**, following the **Page Object Model (POM)** design pattern for modularity and maintainability.

---
## 📦 How to Run the Automation Script
- Clone the repository:
git clone https://github.com/muhammadsalah7/SauceDemoManualAndAutomation.git
cd SauceDemoManualAndAutomation
- Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate (on Windows)
- Install dependencies:
pip install -r requirements.txt
- Run the test:
pytest tests/test_place_order.py
- The script will launch Chrome, perform login, add an item to the cart, complete checkout, and log out.


---
## 🧠 **Tools & Technologies Used**

- Python 3.11 — scripting language  
- Selenium WebDriver — browser automation  
- WebDriver Manager — automatic driver handling  
- Pytest — test execution framework  
- Page Object Model (POM) — clean code structure  
- ChromeOptions — used to suppress password breach alerts

---

## 📋 **Manual Testing Scope**

Manual testing was performed on the SauceDemo website to validate:

- ✅ Login functionality (valid & invalid credentials)  
- ✅ Inventory page UI and responsiveness  
- ✅ Sorting and filtering of products  
- ✅ Add to cart and remove from cart actions  
- ✅ Checkout flow and form validation  

Test cases were documented clearly and executed to verify expected behavior across multiple scenarios.

---

## 📌 **Assumptions Made**

- The test uses SauceDemo’s public credentials:  
  - Username: `standard_user`  
  - Password: `secret_sauce`  
- Chrome browser is installed and accessible  
- Internet connection is available during test execution  
- No CAPTCHA or multi-factor authentication is required  

---

## 👨‍💻 **Author**

**Muhammad Salah** — Aspiring QA Automation Engineer  
Focused on clean automation frameworks, detailed manual testing, and professional documentation.

---

## 📜 **License**

This project is for educational purposes.
