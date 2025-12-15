from django.db import models

# Create your models here.

class catt(models.Model):
    name = models.CharField(max_length=30,)

class product(models.Model):
    catt = models.ForeignKey(catt,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    cat= models.CharField(max_length=10)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='product/')