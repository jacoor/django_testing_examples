import pytest
from selenium.webdriver import FirefoxOptions
from selenium import webdriver

@pytest.fixture
def selenium():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    selenium = webdriver.Firefox(options=opts)
    yield selenium
    selenium.quit()
