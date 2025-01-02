from django.db import models
from Adminapp.models import*
# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email=models.EmailField()
    phone = models.IntegerField()

class Cart(models.Model):
    userid=models.ForeignKey(Register,on_delete=models.CASCADE)
    productid=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()
    status=models.IntegerField(default=0)

class Checkout(models.Model):
    userid=models.ForeignKey(Register,on_delete=models.CASCADE)
    cartid=models.ForeignKey(Cart, on_delete=models.CASCADE)
    address=models.TextField()
    pincode=models.IntegerField()
    country=models.TextField()

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()