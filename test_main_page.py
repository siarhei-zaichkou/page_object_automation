import pytest
from selenium.webdriver.common.by import By
import time
from .pages.main_page import MainPage


@pytest.mark.skip
def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, url=link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, url=link)
    page.open()
    page.should_be_login_link()
