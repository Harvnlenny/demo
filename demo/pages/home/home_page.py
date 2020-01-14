from base.selenium_driver import SeleniumDriver
import time

class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_name = "search"
    _search_button = "//*[@id='header']/div[3]/form/input[1]"

    def enter_player_name(self, player_name):
        self.send_keys(player_name, self._search_name, locator_type="name")

    def click_search_button(self):
        self.element_click(self._search_button, locator_type="xpath")

    def player_search(self, player_name):
        self.enter_player_name(player_name)
        self.click_search_button()
