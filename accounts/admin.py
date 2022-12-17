from django.contrib import admin

# Register your models here.

from .models import ContactMessage,  StudentCard, Student

admin.site.register(ContactMessage)
admin.site.register(Student)
admin.site.register(StudentCard)