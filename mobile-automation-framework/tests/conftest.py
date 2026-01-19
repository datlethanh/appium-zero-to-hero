import pytest
from utils.driver_factory import DriverFactory
from config.config import Config

@pytest.fixture(scope="function")
def driver():
    # Setup
    driver_instance = DriverFactory.get_driver()
    driver_instance.implicitly_wait(Config.IMPLICIT_WAIT)
    
    yield driver_instance
    
    # Teardown
    driver_instance.quit()