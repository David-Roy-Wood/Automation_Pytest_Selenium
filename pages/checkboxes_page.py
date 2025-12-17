from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckboxesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkboxes = (By.CSS_SELECTOR, "input[type='checkbox']")

    def click_checkbox(self, index):
        checkboxes = self.driver.find_elements(*self.checkboxes)
        checkboxes[index].click()

    def check_checkbox(self, index):
        checkboxes = self.driver.find_elements(*self.checkboxes)
        checkbox = checkboxes[index]
        return checkbox.is_selected()