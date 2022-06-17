from django import forms
from django.forms import ModelForm
from utility.models import Products
from django.contrib.auth.models import User


 
 
# creating a form
class ProductForm(ModelForm):
    class Meta:
        # specify model to be used
        model = Products
 
        # specify fields to be used
        fields = [
            'name',
            'price', 
            'quantity',
            'img'
        ]



'''
fields = [
            "name",
            "price",
        ]
'''