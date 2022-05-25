import pytest
from accounts.forms import UserRegisterForm

@pytest.mark.django_db
def test_user_register_form_valid():
    # Arrange 
    form = UserRegisterForm({"email": "joe@doe.com", "username":"joe_doe"})

    # Action 
    result = form.is_valid()

    # Assert
    assert result == True

@pytest.mark.django_db
def test_user_register_form_invalid_email():
    # Arrange
    form = UserRegisterForm({"email": "joe@doe", "username":"joe_doe"})

    # Action
    result = form.is_valid()

    # Assert
    assert result == False
    assert "email" in form.errors


@pytest.mark.django_db
@pytest.mark.usefixtures("joe_doe_account")
def test_user_register_form_invalid_duplicated_email():
    # question: is this test resistant to changes?
    # Arrange
    form = UserRegisterForm({"email": "joe@doe.com", "username":"joe_doe_11"})

    # Action
    result = form.is_valid()

    # Assert
    assert result == False
    assert form.errors["email"] == ["User with this Email address already exists."]

