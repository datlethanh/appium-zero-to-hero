# *Step 1: Prerequisites & Installation*
## **1.Node.js & Appium Server:**
npm install -g appium

appium driver install uiautomator2 # Android

appium driver install xcuitest # iOS

## **2.Python Dependencies:** 
Create a virtual environment and install necessary client libraries.

pip install Appium-Python-Client pytest pytest-html

## **3.Appium Inspector:** 
Download and install GUI tool to inspect mobile elements.

# *Step 2: Project Structure*
A clean directory is crucial. We will separate configuration, page logic, and test execution.


mobile-automation-framework/

├── config/

│   └── config.py             # Global settings (timeouts, app paths)

├── pages/

│   ├── base_page.py          # Wrapper for common driver actions

│   └── login_page.py         # Page specific logic

├── tests/

│   ├── conftest.py           # Pytest fixtures (Setup/Teardown)

│   └── test_login.py         # Actual test cases

├── utils/

│   └── driver_factory.py     # Logic to spin up the driver

└── pytest.ini                # Pytest configuration


