"""
Module used for defining page functions.

Page functions are the interaction done on the page using the locators on the site and performing interactions such
as typing and clicking on links.

These will also return Booleans meant to be read as a PASS or FAIL
"""

import pdb  # Use pdb.set_trace() to check the contents of the web element during test case creation

from locator import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class BasePage(object):
    """Base class object for inheriting the web driver"""
    def __init__(self, driver) -> None:
        self.driver = driver
        super().__init__()


class MainPage(BasePage):
    """
    Class for functions to be used when testing the main page.

    Test Cases to write:
        - Hover over cart shows items
    """

    def does_title_match(self, to_match="") -> bool:
        return to_match in self.driver.title

    def does_site_header_match(self, to_match) -> bool:
        element = self.driver.find_element(*MainPageLocators.SITE_HEADER)
        return to_match in element.text
    
    def enter_first_name(self, text) -> None:
        element = self.driver.find_element(*MainPageLocators.FIRST_NAME_BOX)
        element.send_keys(text)
    
    def get_text_box_first_name_text(self) -> str:
        element = self.driver.find_element(*MainPageLocators.FIRST_NAME_BOX)
        return element.get_attribute("value")
    
    def enter_last_name(self, text) -> None:
        element = self.driver.find_element(*MainPageLocators.LAST_NAME_BOX)
        element.send_keys(text)
        
    def get_text_box_last_name_text(self) -> str:
        element = self.driver.find_element(*MainPageLocators.LAST_NAME_BOX)
        return element.get_attribute("value")
            