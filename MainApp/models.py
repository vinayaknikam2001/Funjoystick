from os import link
from django.db import models
from django.db.models.base import Model

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=60)
    query = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from '+self.name+' '+self.email

class Game(models.Model):
    gamefile = models.FileField(upload_to='media')
    image = models.ImageField(upload_to='images',default=None)
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Playgame(models.Model):
    image = models.ImageField(upload_to='images',default=None)
    name = models.CharField(max_length=50)
    game = models.CharField(max_length=250)
    def __str__(self):
        return self.name