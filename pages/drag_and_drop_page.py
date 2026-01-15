from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DragAndDropPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkboxes = (By.CSS_SELECTOR, "input[type='checkbox']")
        self.ColumnA = (By.ID, "column-a")
        self.ColumnB = (By.ID, "column-b")

    def drag_from_column_a_to_b(self):
        self.drag_and_drop(self.ColumnA, self.ColumnB)

    def drag_from_column_b_to_a(self):
        self.drag_and_drop(self.ColumnB, self.ColumnA)

    def check_column_a_header(self):
        header = self.driver.find_element(By.CSS_SELECTOR, "#column-a > header")
        return header.text

    def check_column_b_header(self):
        header = self.driver.find_element(By.CSS_SELECTOR, "#column-b > header")
        return header.text