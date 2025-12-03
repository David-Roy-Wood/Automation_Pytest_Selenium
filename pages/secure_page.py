from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SecurePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logout_button = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def click_logout(self):
        self.click(self.logout_button)