from distutils.command.upload import upload
from email.mime import image
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()
    img = models.ImageField(upload_to='person')

    