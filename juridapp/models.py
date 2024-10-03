from django.db import models

class Student(models.Model):
    profile_picture = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    registration = models.PositiveIntegerField(unique=True)