import pytest
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def setup():
    driver = DriverFactory.get_driver("chrome")
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_login(setup):
    # Instantiate the LoginPage with just the driver
    login_page = LoginPage(setup)
    
    # Call the login method to perform login
    login_page.login("standard_user", "secret_sauce")
    
    # Validate that the login is successful by checking the URL
    assert "inventory.html" in setup.current_url, "Login failed!"
