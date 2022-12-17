from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=255)
    addres_street = models.CharField(max_length=255)
    address_city = models.CharField(max_length=255)
    address_zipcode = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class StudentCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    card_id = models.CharField(max_length=20)
    expiration_date = models.DateField()
    creation_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to="student_photos")



class Account(AbstractUser):
    email = models.EmailField("email address", max_length=255, blank=False, null=False, unique=True)


class ContactMessage(models.Model):
    name = models.CharField(verbose_name="imię", max_length=50, blank=False, null=False)
    email = models.EmailField(verbose_name="adres email", help_text="help text do pola adres email", max_length=255, blank=False, null=False)
    message = models.TextField(verbose_name="wiadomość", blank=False, null=False)

    def __str__(self):
        return f"wiadomość od {self.name}({self.email})"