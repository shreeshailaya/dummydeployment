from email.policy import default
from django.db import models
from django.forms import CharField, IntegerField
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100, default='')
    quantity = models.IntegerField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='images/', default='default_product.png')
    seller = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
        
