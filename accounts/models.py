from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Account(AbstractUser):
    email = models.EmailField("email address", max_length=255, blank=False, null=False, unique=True)


class ContactMessage(models.Model):
    name = models.CharField(verbose_name="imię", max_length=50, blank=False, null=False)
    email = models.EmailField(verbose_name="adres email", help_text="help text do pola adres email", max_length=255, blank=False, null=False)
    message = models.TextField(verbose_name="wiadomość", blank=False, null=False)

    def __str__(self):
        return f"wiadomość od {self.name}({self.email})"