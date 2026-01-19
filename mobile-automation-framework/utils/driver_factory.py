from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import Config

class DriverFactory:
    @staticmethod
    def get_driver():
        if Config.PLATFORM_NAME.lower() == 'android':
            options = UiAutomator2Options()
            options.platform_name = Config.PLATFORM_NAME
            options.device_name = Config.DEVICE_NAME
            options.app = Config.APP_PATH
            options.automation_name = Config.AUTOMATION_NAME
            
            # Initialize driver with options
            driver = webdriver.Remote(Config.APPIUM_SERVER_URL, options=options)
            return driver
        
        elif Config.PLATFORM_NAME.lower() == 'ios':
            raise NotImplementedError("iOS Driver not implemented yet.")
        else:
            raise Exception(f"Platform {Config.PLATFORM_NAME} not supported")