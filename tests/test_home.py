"""
This module is where test cases are made for interactions on the main page.

Functions will start with test_ so they are detected by pytest. Test cases typically check one of the following or more:
    - UI updates
    - Images load
    - Audio plays
    - Text is accurate
    - Backend updates
    - Links are correct
"""

import pdb  # Use pdb.set_trace() to check the contents of the web element during test case creation
import time

import pytest
from selenium import webdriver
import page


class TestHome:

    @pytest.fixture  # This allows the test cases to find and run the function as a setup and teardown
    def setup_driver(self) -> None:
        """Function used for setting up the case with a fresh site load and for tearing down between cases."""
        self.driver = webdriver.Chrome(r"chromedriver")
        self.driver.maximize_window()
        self.driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        yield  # This allows the test functions to complete and ends with teardown.
        self.driver.close()

    def test_title(self, setup_driver):  # The setup_driver argument is used so that it acts as a test case wrapper
        """Basic case to make sure the site loads without going to the wrong page or other errors"""
        main_page = page.MainPage(self.driver)
        assert main_page.does_title_match()  # Simple check to make sure there is no major error before testing starts

    def test_main_elements_loaded(self, setup_driver):
        """Test case to check elements loaded on the main page"""
        main_page = page.MainPage(self.driver)
        assert main_page.does_site_header_match("Demo Sign-Up Selenium Automation Practice Form")

    def test_textbox_entry(self, setup_driver):
        """Test case to check that text can be entered into a textbox"""
        main_page = page.MainPage(self.driver)
        main_page.enter_first_name("John")
        assert main_page.get_text_box_first_name_text() == "John"
        main_page.enter_last_name("Smith")
        assert main_page.get_text_box_last_name_text() == "Smith"

    def test_radio_gender(self, setup_driver):
        """Test case selects the genders and checks that it is selected and deselected correctly"""
        main_page = page.MainPage(self.driver)
        main_page.select_male_gender()
        assert main_page.get_value_male_gender()
        assert not main_page.get_value_female_gender()
        main_page.select_female_gender()
        assert main_page.get_value_female_gender()
        assert not main_page.get_value_male_gender()
        
    def test_radio_experience(self, setup_driver):
        """Test case selects the experience radio buttons and checks that it is selected and deselected correctly"""
        main_page = page.MainPage(self.driver)
        main_page.select_experience_1()
        assert main_page.get_experience() == 1
        assert not main_page.get_experience() == 2
        assert not main_page.get_experience() == 3
        assert not main_page.get_experience() == 4
        assert not main_page.get_experience() == 5
        assert not main_page.get_experience() == 6
        assert not main_page.get_experience() == 7
        main_page.select_experience_2()
        assert main_page.get_experience() == 2
        assert not main_page.get_experience() == 1
        assert not main_page.get_experience() == 3
        assert not main_page.get_experience() == 4
        assert not main_page.get_experience() == 5
        assert not main_page.get_experience() == 6
        assert not main_page.get_experience() == 7
        main_page.select_experience_3()
        assert main_page.get_experience() == 3
        assert not main_page.get_experience() == 1
        assert not main_page.get_experience() == 2
        assert not main_page.get_experience() == 4
        assert not main_page.get_experience() == 5
        assert not main_page.get_experience() == 6
        assert not main_page.get_experience() == 7
        main_page.select_experience_4()
        assert main_page.get_experience() == 4
        assert not main_page.get_experience() == 1
        assert not main_page.get_experience() == 2
        assert not main_page.get_experience() == 3
        assert not main_page.get_experience() == 5
        assert not main_page.get_experience() == 6
        assert not main_page.get_experience() == 7
        main_page.select_experience_5()
        assert main_page.get_experience() == 5
        assert not main_page.get_experience() == 1
        assert not main_page.get_experience() == 2
        assert not main_page.get_experience() == 3
        assert not main_page.get_experience() == 4
        assert not main_page.get_experience() == 6
        assert not main_page.get_experience() == 7
        main_page.select_experience_6()
        assert main_page.get_experience() == 6
        assert not main_page.get_experience() == 1
        assert not main_page.get_experience() == 2
        assert not main_page.get_experience() == 3
        assert not main_page.get_experience() == 4
        assert not main_page.get_experience() == 5
        assert not main_page.get_experience() == 7
        main_page.select_experience_7()
        assert main_page.get_experience() == 7
        assert not main_page.get_experience() == 1
        assert not main_page.get_experience() == 2
        assert not main_page.get_experience() == 3
        assert not main_page.get_experience() == 4
        assert not main_page.get_experience() == 5
        assert not main_page.get_experience() == 6
    
        

if __name__ == "__main__":
    pytest.main()
