from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categeory(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="cat_image")

    def __str__(self):
        return self.name

class product(models.Model):
    categeory = models.ForeignKey(Categeory,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to="pro_image")

class Cart(models.Model):
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qty = models.IntegerField()

    def total_price(self):
        return self.qty*self.products.price


  

    


  
  