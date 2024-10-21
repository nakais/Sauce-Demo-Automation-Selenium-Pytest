# Sauce Demo Automation Project

This project automates various functionalities of the [Sauce Demo](https://www.saucedemo.com/) website using Selenium, PyTest, and Allure reporting.

## Project Structure

```bash
.
├── pages/
│   ├── base_page.py                # Base page class
│   ├── cart_and_checkout_page.py    # Page object for cart and checkout
│   ├── footer_page.py               # Page object for footer social media links
│   ├── login_page.py                # Page object for login functionality
│   ├── logout_page.py               # Page object for logout functionality
│   ├── product_page.py              # Page object for product-related actions
├── reports/
│   ├── allure-results/              # Allure results directory for test reports
├── tests/
│   ├── test_checkout.py             # Test script for checkout functionality
│   ├── test_footer.py               # Test script for social media footer links
│   ├── test_login.py                # Test script for login functionality
│   ├── test_logout.py               # Test script for logout functionality
│   ├── test_product.py              # Test script for product-related tests
├── utils/
│   ├── config.py                    # Configuration file
│   ├── driver_factory.py            # WebDriver setup and management
├── venv/                            # Python virtual environment
├── conftest.py                      # PyTest fixture configuration
├── requirements.txt                 # Python dependencies

```
## Prerequisites
- Python 3.x
- Selenium WebDriver
- PyTest
- Allure Framework

## Installation

### Clone the repository:

  ```bash
  git clone https://github.com/your-repo/sauce-demo-automation.git
  cd sauce-demo-automation
  ```
## Set up the virtual environment and install dependencies
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```

## Running Tests
### To execute the tests and generate an Allure report:

1. Run the test suite
  ```bash
  pytest tests/ --alluredir=reports/allure-results
  ```
2. Generate and view the Allure report
  ```bash
  allure serve reports/allure-results
  ```
## Additional Information
- Test Execution Video: https://www.loom.com/share/35840d06555f4378ab5f3e86ec27df40?sid=0c194732-640d-47f1-a13f-5d3b6a5f0d5d
## Allure Report Screenshot:
![image](https://github.com/user-attachments/assets/24d548b4-4b27-4b5a-804d-293f14eeeff2)
![image](https://github.com/user-attachments/assets/550d7a18-0e1c-4adc-8c1a-d34007c9b1c5)



