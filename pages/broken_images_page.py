from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BrokenImagesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.image_1 = (By.CSS_SELECTOR, "img[src='asdf.jpg']")
        self.image_2 = (By.CSS_SELECTOR, "img[src='hjkl.jpg']")
        self.image_3 = (By.CSS_SELECTOR, "img[src='img/avatar-blank.jpg']")

    def get_image_width(self, img_src):
        locator = (By.CSS_SELECTOR, f"img[src='{img_src}']")
        image = self.driver.find_element(*locator)
        width = self.driver.execute_script("return arguments[0].naturalWidth;", image)
        return width