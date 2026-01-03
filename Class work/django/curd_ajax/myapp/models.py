from django.db import models

# Create your models here.

class students (models.Model):
    name = models.CharField()
    email = models.CharField()
    phone = models.CharField()
