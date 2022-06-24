from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=40)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
