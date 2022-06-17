from django.db import models

# Create your models here.
# Many-to-one fields:

class Album(models.Model):
    title = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

    

class Song(models.Model):
    title = models.CharField(max_length = 100)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

# MANY-to-MANY



class Author(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.TextField(max_length = 300)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.TextField(max_length = 300)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


from django.db import models

class Vehicle(models.Model):
    reg_no = models.IntegerField()
    owner = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.reg_no)

class Car(models.Model):
    vehicle = models.OneToOneField(Vehicle,
		on_delete = models.CASCADE, primary_key = True)
    car_model = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.car_model)

from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content= models.TextField()
    def __str__(self):
	    return self.title

