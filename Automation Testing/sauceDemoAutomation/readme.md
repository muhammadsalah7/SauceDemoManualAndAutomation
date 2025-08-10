# 🧪 SauceDemo Automation Project  
This project automates a full end-to-end user journey on [SauceDemo](https://www.saucedemo.com/) using **Selenium WebDriver**, **Python**, and the **Page Object Model (POM)** design pattern. It reflects clean architecture, modular design, and professional QA automation practices.

## 🚀 Scenario Automated  
A **standard user** logs in, adds a product to the cart, checks out, and logs out — simulating a complete purchase flow.

### ✅ Steps Covered:  
1. Login with valid credentials  
2. Add product to cart  
3. Proceed to checkout  
4. Fill in user information  
5. Complete the order  
6. Log out

## 🛠️ Technologies Used  
- Python 3.11  
- Selenium WebDriver  
- WebDriver Manager  
- Pytest  
- Page Object Model (POM)

## 📦 Installation & Setup  
1. **Clone the repository**  
   `git clone https://github.com/muhammadsalah7/sauceDemoAutomation.git`  
   `cd sauceDemoAutomation`

2. **Create and activate a virtual environment**  
   `python -m venv venv`  
   `venv\Scripts\activate`  *(on Windows)*

3. **Install dependencies**  
   `pip install -r requirements.txt`

4. **Run the test**  
   `pytest tests/test_place_order.py`  
   > This will launch Chrome, perform login, add to cart, checkout, and logout — all automatically.

## 📁 Requirements  
- selenium>=4.10.0  
- webdriver-manager>=4.0.0  
- pytest>=7.4.0

## 📌 Credentials Used  
- Username: `standard_user`  
- Password: `secret_sauce`

---






