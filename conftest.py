import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Edge(options=options)
    # browser = webdriver.Edge()
    # browser.maximize_window()
    yield browser
    browser.quit()
