from django.contrib import admin
from .models import *

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('profile_picture','name','email','age','registration')

admin.site.register(Student, StudentsAdmin)
