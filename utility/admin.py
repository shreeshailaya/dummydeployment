from django.contrib import admin
from utility.models import Products

# Register your models here.
@admin.register(Products)
class Products(admin.ModelAdmin):
    #search_fields = ['name']
    #list_filter = ['price']
    #list_display =['name','price', 'quantity']
    pass
