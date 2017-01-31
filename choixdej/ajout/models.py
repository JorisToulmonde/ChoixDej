from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Restaurant(models.Model):
    titre = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    score = models.IntegerField(default=999)
