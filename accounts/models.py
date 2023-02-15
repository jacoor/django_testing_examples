from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.core.validators import MaxValueValidator 

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # middle_name = models.CharField(max_length=255, blank=True)
    # email = models.EmailField(max_length=255)
    # birth_date = models.DateField()
    # phone_number = models.CharField(max_length=255)
    # addres_street = models.CharField(max_length=255)
    # address_city = models.CharField(max_length=255)
    # address_zipcode = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(Student, through="StudentCourseMembership")

    def __str__(self):
        return self.name

# nowy model dla relacji ManyToMany
class StudentCourseMembership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField("Data zapisania studenta", auto_now_add=True)
    final_grade = models.PositiveIntegerField("Ocena końcowa", validators=[MaxValueValidator(5)], null=True, blank=True)

    def __str__(self):
        return f"{self.student}: {self.course}"

    @property
    def passed(self):
        return self.final_grade is not None and self.final_grade > 2



class StudentCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="card")
    card_id = models.CharField(max_length=20)
    expiration_date = models.DateField()
    creation_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to="student_photos")

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} {self.card_id}"



class Account(AbstractUser):
    email = models.EmailField("email address", max_length=255, blank=False, null=False, unique=True)


class ContactMessage(models.Model):
    name = models.CharField(verbose_name="imię", max_length=50, blank=False, null=False)
    email = models.EmailField(verbose_name="adres email", help_text="help text do pola adres email", max_length=255, blank=False, null=False)
    message = models.TextField(verbose_name="wiadomość", blank=False, null=False)

    def __str__(self):
        return f"wiadomość od {self.name}({self.email})"

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    # ponieważ Department jeszcze nie jest zadeklarowany, jego nazwa jest w cudzysłowiu
    department = models.ForeignKey("Department", related_name="employees", on_delete=models.DO_NOTHING)
    # dla uproszczenia pomijam pozostałe pola. 

    def __str__(self):
        return f"{self.first_name}"

class Department(models.Model):
    name = models.CharField(max_length=255)
    # dla uproszczenia pomijam pozostałe pola. 

    def __str__(self):
        return f"{self.name}"

