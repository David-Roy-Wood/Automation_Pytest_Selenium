import pytest
from utils.driver_factory import create_driver
from pages.checkboxes_page import CheckboxesPage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_check_checkbox(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkbox_page = CheckboxesPage(driver)

    #Test the first checkbox, which starts unchecked
    assert checkbox_page.check_checkbox(0) is False
    checkbox_page.click_checkbox(0)
    assert checkbox_page.check_checkbox(0) is True

    #Test the second checkbox, which starts checked
    assert checkbox_page.check_checkbox(1) is True
    checkbox_page.click_checkbox(1)
    assert checkbox_page.check_checkbox(1) is False