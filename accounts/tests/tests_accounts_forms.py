from accounts.models import Account
import pytest
from .fixtures import joe_doe_account
from accounts.forms import UserRegisterForm

@pytest.mark.django_db
def test_user_register_form_valid():
    form = UserRegisterForm({"email": "joe@doe.com", "username":"joe_doe"})
    assert form.is_valid()

@pytest.mark.django_db
def test_user_register_form_invalid_email():
    form = UserRegisterForm({"email": "joe@doe", "username":"joe_doe"})
    assert not form.is_valid()
    assert "email" in form.errors


@pytest.mark.django_db
@pytest.mark.usefixtures("joe_doe_account")
def test_user_register_form_invalid_duplicated_email():
    # question: is this test resistant to changes?
    form = UserRegisterForm({"email": "joe@doe.com", "username":"joe_doe_11"})
    assert not form.is_valid()
    assert form.errors["email"] == ["User with this Email address already exists."]
