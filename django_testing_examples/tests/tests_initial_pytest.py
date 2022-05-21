
import pytest

# interesting fact here is pytest found fixture and used it by itself
def test_pytest_live_server_no_mark(live_server, selenium):
    # Arrange
    # in fixture

    #Action
    selenium.get('%s%s' % (live_server.url, '/admin/'))

    # Assert
    assert 'Django' in selenium.title

