import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from utils.driver_factory import create_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")  # Public demo site
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "SuperSecretPassword!")
    flash = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success")))
    assert "You logged into a secure area!" in flash.text

def test_logout(driver):
    test_valid_login(driver)
    SecurePage(driver).click_logout()
    flash = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "flash")))
    assert "You logged out of the secure area!" in flash.text

def test_invalid_username_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")  # Public demo site
    login_page = LoginPage(driver)
    login_page.login("QA", "SuperSecretPassword!")
    flash = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "flash")))
    assert "Your username is invalid!" in flash.text

def test_invalid_password_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")  # Public demo site
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "Password1!")
    flash = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "flash")))
    assert "Your password is invalid!" in flash.text

def test_empty_username_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")  # Public demo site
    login_page = LoginPage(driver)
    login_page.login("", "SuperSecretPassword!")
    flash = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "flash")))
    assert "Your username is invalid!" in flash.text

def test_empty_password_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")  # Public demo site
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "")
    flash = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "flash")))
    assert "Your password is invalid!" in flash.text
    #test