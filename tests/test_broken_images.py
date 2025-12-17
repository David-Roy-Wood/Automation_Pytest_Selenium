import pytest
from utils.driver_factory import create_driver
from pages.broken_images_page import BrokenImagesPage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_broken_image_asdf(driver):
    driver.get("https://the-internet.herokuapp.com/broken_images")
    broken_image_page = BrokenImagesPage(driver)
    width = broken_image_page.get_image_width('asdf.jpg')
    #This image is broken on the demo site - expect the test to FAIL
    assert width  > 0

def test_broken_image_hjkl(driver):
    driver.get("https://the-internet.herokuapp.com/broken_images")
    broken_image_page = BrokenImagesPage(driver)
    width = broken_image_page.get_image_width('hjkl.jpg')
    # This image is broken on the demo site - expect the test to FAIL
    assert width  > 0

def test_broken_image_avatar(driver):
    driver.get("https://the-internet.herokuapp.com/broken_images")
    broken_image_page = BrokenImagesPage(driver)
    width = broken_image_page.get_image_width('img/avatar-blank.jpg')
    # This image is NOT broken on the demo site - expect the test to PASS
    assert width  > 0