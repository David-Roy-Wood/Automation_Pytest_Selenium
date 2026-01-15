import pytest
from utils.driver_factory import create_driver
from pages.drag_and_drop_page import DragAndDropPage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_drag_a_to_b(driver):
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    drag_and_drop_page = DragAndDropPage(driver)

    column_a = drag_and_drop_page.check_column_a_header()
    column_b = drag_and_drop_page.check_column_b_header()
    assert column_a == "A"
    assert column_b == "B"

    drag_and_drop_page.drag_from_column_a_to_b()

    column_a = drag_and_drop_page.check_column_a_header()
    column_b = drag_and_drop_page.check_column_b_header()
    assert column_a == "B"
    assert column_b == "A"

def test_drag_b_to_a(driver):
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    drag_and_drop_page = DragAndDropPage(driver)

    column_a = drag_and_drop_page.check_column_a_header()
    column_b = drag_and_drop_page.check_column_b_header()
    assert column_a == "A"
    assert column_b == "B"

    drag_and_drop_page.drag_from_column_b_to_a()

    column_a = drag_and_drop_page.check_column_a_header()
    column_b = drag_and_drop_page.check_column_b_header()
    assert column_a == "B"
    assert column_b == "A"

def test_undo_drag_a_to_b(driver):
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    drag_and_drop_page = DragAndDropPage(driver)

    column_a = drag_and_drop_page.check_column_a_header()
    column_b = drag_and_drop_page.check_column_b_header()
    assert column_a == "A"
    assert column_b == "B"

    drag_and_drop_page.drag_from_column_a_to_b()

    column_a = drag_and_drop_page.check_column_a_header()
    column_b = drag_and_drop_page.check_column_b_header()
    assert column_a == "B"
    assert column_b == "A"

    drag_and_drop_page.drag_from_column_a_to_b()

    column_a = drag_and_drop_page.check_column_a_header()
    column_b = drag_and_drop_page.check_column_b_header()
    assert column_a == "A"
    assert column_b == "B"

def test_undo_drag_b_to_a(driver):
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    drag_and_drop_page = DragAndDropPage(driver)

    column_a = drag_and_drop_page.check_column_a_header()
    column_b = drag_and_drop_page.check_column_b_header()
    assert column_a == "A"
    assert column_b == "B"

    drag_and_drop_page.drag_from_column_b_to_a()

    column_a = drag_and_drop_page.check_column_a_header()
    column_b = drag_and_drop_page.check_column_b_header()
    assert column_a == "B"
    assert column_b == "A"

    drag_and_drop_page.drag_from_column_b_to_a()

    column_a = drag_and_drop_page.check_column_a_header()
    column_b = drag_and_drop_page.check_column_b_header()
    assert column_a == "A"
    assert column_b == "B"