from base.selenium_driver import SeleniumDriver
import time

class PlayerPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
