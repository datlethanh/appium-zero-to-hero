import pytest
from pages.login_page import LoginPage

class TestLogin:
    
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        # Add assertions here, e.g.:
        # assert "Home" in driver.page_source