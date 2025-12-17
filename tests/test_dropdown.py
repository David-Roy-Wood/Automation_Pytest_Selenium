import pytest
from utils.driver_factory import create_driver
from pages.dropdown_page import DropdownPage
import time

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_dropdown_option1(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown_page = DropdownPage(driver)
    dropdown_page.select_option("Option 1")
    assert dropdown_page.dropdown_text()  == "Option 1"

def test_dropdown_option2(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown_page = DropdownPage(driver)
    dropdown_page.select_option("Option 1")
    assert dropdown_page.dropdown_text()  == "Option 2"