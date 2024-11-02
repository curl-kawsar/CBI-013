from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('university_name', 'name', 'dept', 'std_id', 'course')

admin.site.register(Student, StudentAdmin)