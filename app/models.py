from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=25)
