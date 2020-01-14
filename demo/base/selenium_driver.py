from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *


class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, locator_type="id"):
        locator_type = locator_type.lower()
        type_map = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "class": By.CLASS_NAME,
            "link": By.LINK_TEXT
        }
        assert locator_type in type_map, "Locator type {} not correct/supported".format(
            locator_type)
        sel_type = type_map.get(locator_type)
        element = None
        try:
            element = self.driver.find_element(sel_type, locator)
            print("Element found with locator: " + locator + " and locator_type: "
                  + locator_type)
        except:
            print(
                "Element not found with locator: " + locator + " and  locatorType: " + locator_type)
            raise
        return element

    def element_click(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            print("Clicked on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            print("Cannot click on the element with locator: " + locator + " locator_type: "
                  + locator_type)

    def send_keys(self, data, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            print("Sent data on element with locator: " + locator + " locator_type: "
                  + locator_type)
        except:
            print("Cannot send data on the element with locator: " + locator +
                  " locator_type: " + locator_type)

    def is_element_present(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locator, by_type):
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def wait_for_element(self, locator, locator_type="id", timeout=10):
        element = None
        try:
            by_type = self.get_element(locator, locator_type)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((by_type,
                                                             locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element
