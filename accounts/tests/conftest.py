import pytest
from accounts.models import Account

@pytest.fixture
def joe_doe_account():
    Account.objects.create(first_name="Joe", email="joe@doe.com")
