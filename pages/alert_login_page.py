from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AlertLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_text = (By.XPATH, "//p[contains(., 'Congratulations!')]")

    def get_page_text(self):
        return self.driver.find_element(*self.page_text).text.strip()