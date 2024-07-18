from django.contrib import admin
from .models import StudentData

# Register your models here.


@admin.register(StudentData)
class Student(admin.ModelAdmin):
    list_display = ['name','email','phone','address']