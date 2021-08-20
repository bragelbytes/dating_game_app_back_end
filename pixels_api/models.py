from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=32)
    image = models.URLField()
    genre = models.CharField(max_length=32)

class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    image = models.URLField()
    name = models.CharField(max_length=32)
    age = models.CharField(max_length=32)
    fav_console = models.CharField(max_length=32)
    fav_games = models.ManyToManyField(Games)
