from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class DropdownPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.dropdown = (By.ID, "dropdown")

    def select_option(self, visible_text):
        select_element = self.driver.find_element(*self.dropdown)
        select = Select(select_element)
        select.select_by_visible_text(visible_text)

    def dropdown_text(self):
        dropdown_element = self.driver.find_element(*self.dropdown) #finds the dropdown element and stores it in a variable
        dropdown = Select(dropdown_element) # creates a Select object from the Selenium helper class, giving us access to dropdown-specific methods (actions/data)
        dropdown_option = dropdown.first_selected_option.text #uses the selenium method to get the currently selected option as text
        return dropdown_option