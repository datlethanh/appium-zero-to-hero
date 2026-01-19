from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators (Update these IDs based on your specific app via Appium Inspector)
    USERNAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "username_input")
    PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "password_input")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "login_button")
    ERROR_MESSAGE = (AppiumBy.XPATH, "//android.widget.TextView[@text='Invalid credentials']")

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    # Add methods to verify login success or failure here