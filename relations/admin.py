from django.contrib import admin
from relations.models import Album, Song, Post, Author, Book, Car, Vehicle

# Register your models here.
'''
@admin.register(Album)
class Album(admin.ModelAdmin):
    pass

@admin.register(Song)
class Song(admin.ModelAdmin):
    pass


@admin.register(Author)
class Author(admin.ModelAdmin):
    pass

@admin.register(Book)
class Book(admin.ModelAdmin):
    pass
'''

@admin.register(Car)
class Car(admin.ModelAdmin):
    pass

@admin.register(Vehicle)
class Vehicle(admin.ModelAdmin):
    pass

@admin.register(Post)
class Post(admin.ModelAdmin):
    pass