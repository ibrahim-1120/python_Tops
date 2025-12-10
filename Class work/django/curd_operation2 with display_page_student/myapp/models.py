from django.db import models

# Create your models here.

class student(models.Model):
    name= models.CharField(max_length=10)
    email= models.EmailField()
    age = models.PositiveIntegerField()
    phone = models.IntegerField()