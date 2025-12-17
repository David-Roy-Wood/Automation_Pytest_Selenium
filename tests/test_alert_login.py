import pytest

from pages.alert_login_page import AlertLoginPage
from utils.driver_factory import create_driver
from pages.checkboxes_page import CheckboxesPage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_alert_login(driver):
    alert_login_page = AlertLoginPage(driver)
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth") #passing the credentials via URL to browser alert
    assert alert_login_page.get_page_text() == "Congratulations! You must have the proper credentials."