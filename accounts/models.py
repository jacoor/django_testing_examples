from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Account(AbstractUser):
    email = models.EmailField("email address", max_length=255, blank=False, null=False, unique=True)