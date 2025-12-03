from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class AddRemoveElements(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_button = (By.CSS_SELECTOR, "div.example > button")
        self.remove_button = (By.CSS_SELECTOR, "button.added-manually")

    def add(self):
        self.wait_for_visible(self.add_button)
        self.click(self.add_button)

    def remove(self):
        self.wait_for_visible(self.remove_button)
        self.click(self.remove_button)

    def get_remove_buttons(self):
        return self.driver.find_elements(*self.remove_button)

    def remove_by_index(self, index):
        buttons = self.get_remove_buttons()
        buttons[index].click()