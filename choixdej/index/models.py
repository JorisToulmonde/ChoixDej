from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Groupes(models.Model):
    nom_utilisateur = models.ForeignKey(User)
    nom_groupes = models.CharField(max_length=45, default="")  # Field name made lowercase.
    descriptif = models.CharField(max_length=144, default="") 
    favori = models.BooleanField(default=False)
    present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('nom_utilisateur', 'nom_groupes',)

class Restaurant(models.Model):
    nom_groupes = models.CharField(max_length=50)
    nom_restaurant = models.CharField(max_length=45)  # Field name made lowercase.
    adresse_restaurant = models.CharField(max_length=45)  # Field name made lowercase.
    ville_restaurant = models.CharField(max_length=45)  # Field name made lowercase.
    frequence = models.IntegerField(blank=True, null=False, default=0)  # Field name made lowercase.
    anciennete = models.IntegerField(blank=True, null=False, default=10)  # Field name made lowercase.
    score = models.IntegerField(blank=True, default=999)  # Field name made lowercase.
    image = models.ImageField(upload_to='images')

    class Meta:
        unique_together = ('nom_groupes', 'adresse_restaurant',)
