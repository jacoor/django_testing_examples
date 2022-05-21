
from selenium.webdriver import FirefoxOptions
from selenium import webdriver
import pytest

@pytest.fixture
def selenium():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    selenium = webdriver.Firefox(options=opts)
    yield selenium
    selenium.quit()

@pytest.mark.usefixtures("selenium")
def test_pytest_live_server(live_server, selenium):
    # Arrange
    # in fixture

    #Action
    selenium.get('%s%s' % (live_server.url, '/admin/'))

    # Assert
    assert 'Django' in selenium.title

# interesting fact here is pytest found fixture and used it by itself
def test_pytest_live_server_no_mark(live_server, selenium):
    # Arrange
    # in fixture

    #Action
    selenium.get('%s%s' % (live_server.url, '/admin/'))

    # Assert
    assert 'Django' in selenium.title

