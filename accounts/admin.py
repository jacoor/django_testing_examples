from django.contrib import admin

# Register your models here.

from .models import ContactMessage,  StudentCard, Student, Course, StudentCourseMembership

admin.site.register(Course)

class CourseTabularInline(admin.TabularInline):
    model = StudentCourseMembership
    verbose_name_plural = "Courses"
    readonly_fields = ["enrollment_date", "passed"]
    # Extra pozwala określić ile "pustych" wierszy będzie widoczne w panelu.
    # Domyślnie są to 3.
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    # dodaje inlines do modelu
    inlines = [CourseTabularInline]


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentCourseMembership)



admin.site.register(ContactMessage)

admin.site.register(StudentCard)


from .models import Employee, Department

class EmployeeTabularInline(admin.TabularInline):
    model = Employee
    verbose_name_plural = "Employees TabularInline"
    # Extra pozwala określić ile "pustych" wierszy będzie widoczne w panelu.
    # Domyślnie są to 3.
    extra = 1

class EmployeeStackedInline(admin.StackedInline):
    model = Employee
    verbose_name_plural = "Employees StackedInline"
    multi_page = True
    list_per_page = 1
    extra = 1


class DepartmentAdmin(admin.ModelAdmin):
    # dodaje inlines do modelu
    inlines = [EmployeeTabularInline, EmployeeStackedInline]

admin.site.register(Employee)
# rejestruje DepartmentAdmin jako klasę wyświetlającją Department
admin.site.register(Department, DepartmentAdmin)