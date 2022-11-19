from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Account(AbstractUser):
    email = models.EmailField("email address", max_length=255, blank=False, null=False, unique=True)


class ContactMessage(models.Model):
    name = models.CharField("imię", max_length=50, blank=False, null=False)
    email = models.EmailField("email", max_length=255, blank=False, null=False)
    message = models.TextField("wiadomość", blank=False, null=False)