🧪 Eyego Internship Task — SauceDemo Automation & Manual Testing
This project was completed as part of the Eyego internship program. It includes both manual testing documentation and a Selenium-based automation script for the SauceDemo web application.
🚀 Automation Scenario
The automation script simulates a full user journey:
- Login with valid credentials
- Add an item to the cart
- Proceed to checkout
- Complete the order
- Log out
The script is built using Python and Selenium WebDriver, following the Page Object Model (POM) design pattern for modularity and maintainability.

🧠 Tools & Technologies Used
- Python 3.11 — scripting language
- Selenium WebDriver — browser automation
- WebDriver Manager — automatic driver handling
- Pytest — test execution framework
- Page Object Model (POM) — clean code structure
- ChromeOptions — used to suppress password breach alerts
📋 Manual Testing Scope
Manual testing was performed on the SauceDemo website to validate:
- ✅ Login functionality (valid & invalid credentials)
- ✅ Inventory page UI and responsiveness
- ✅ Sorting and filtering of products
- ✅ Add to cart and remove from cart actions
- ✅ Checkout flow and form validation
Test cases were documented clearly and executed to verify expected behavior across multiple scenarios.

📌 Assumptions Made
- The test uses SauceDemo’s public credentials:
- Username: standard_user
- Password: secret_sauce
- Chrome browser is installed and accessible
- Internet connection is available during test execution
- No CAPTCHA or multi-factor authentication is required
- Chrome security alerts (e.g., password breach warnings) are disabled via ChromeOptions
👨‍💻 Author
Muhammad Salah — Aspiring QA Automation Engineer
Focused on clean automation frameworks, detailed manual testing, and professional documentation.
📜 License
This project is for educational and internship evaluation purposes.
