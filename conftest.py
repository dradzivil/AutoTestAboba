import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    browser = webdriver.Edge()
    browser.maximize_window()
    yield browser
    browser.quit()
