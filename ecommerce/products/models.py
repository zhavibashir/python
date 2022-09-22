from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Product(models.Model):

    title= models.CharField(max_length=200);
    desc= models.CharField(max_length=10000)
    price=models.FloatField(null=False)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='product_pic')
    def __str__(self):
        return self.title






