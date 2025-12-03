from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button.radius")

    def login(self, username, password):
        self.send_keys(self.username_input, username)
        self.send_keys(self.password_input, password)
        self.click(self.login_button)