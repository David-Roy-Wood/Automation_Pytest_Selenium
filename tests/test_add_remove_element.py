from time import sleep

import pytest
from pages.login_page import LoginPage
from pages.add_remove_elements_page import AddRemoveElements
from pages.secure_page import SecurePage
from utils.driver_factory import create_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_add_remove_element(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")  # Public demo site
    add_remove_elements = AddRemoveElements(driver)
    add_remove_elements.add()
    remove_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(add_remove_elements.remove_button))
    assert remove_button.is_displayed()
    add_remove_elements.remove()
    assert not add_remove_elements.is_visible(add_remove_elements.remove_button)

def test_add_many_remove_second_element(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_remove_elements = AddRemoveElements(driver)
    add_remove_elements.add()
    add_remove_elements.add()
    remove_buttons = add_remove_elements.get_remove_buttons()
    assert len(remove_buttons) == 2
    add_remove_elements.remove_by_index(1)  # delete second button
    assert len(add_remove_elements.get_remove_buttons()) == 1