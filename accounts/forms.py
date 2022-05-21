from django.forms import ModelForm
from .models import Account

class UserRegisterForm(ModelForm):
    class Meta:
        model = Account
        fields = ["email", "username"]