from django.db import models

# Create your models here.
class User(models.Model):
    student_name=models.CharField(max_length=25)
    teacher_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=10)