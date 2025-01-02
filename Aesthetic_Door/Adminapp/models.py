from django.db import models

# Create your models here.
class Category(models.Model):
    cname=models.CharField(max_length=20)
    cdesc=models.CharField(max_length=100)
    cimage=models.ImageField(upload_to='cimages')

class Product(models.Model):
    pname=models.CharField(max_length=20)
    pcat=models.CharField(max_length=100)
    pprice=models.IntegerField()
    pstock=models.IntegerField()
    pimage=models.ImageField(upload_to='pimages')