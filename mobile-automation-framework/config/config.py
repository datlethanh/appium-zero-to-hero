import os

class Config:
    # Appium Server
    APPIUM_SERVER_URL = 'http://127.0.0.1:4723'

    # Android Capabilities
    PLATFORM_NAME = 'Android'
    DEVICE_NAME = 'Android Emulator'
    AUTOMATION_NAME = 'UiAutomator2'
    # Update this path to point to your actual APK file
    APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'apps', 'app-debug.apk'))

    # Timeouts
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20