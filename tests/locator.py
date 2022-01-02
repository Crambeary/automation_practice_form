"""
This module is for holding all of the locations of the web elements on the website.
It is imported by the page.py file for use in functions that want to interact with the website.
"""

from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """Class that holds the locations of elements for the Main page"""
    SITE_HEADER = (By.CSS_SELECTOR, "#Blog1 > div > article > div > div > h3")
    FIRST_NAME_BOX = (By.CSS_SELECTOR, "#post-body-3077692503353518311 > div:nth-child(1) > div > div:nth-child(3) > input")
