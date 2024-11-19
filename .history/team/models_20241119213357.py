from django.db import models

# Create your models here.
"""
teams: nom de la table
    - name: nom de l'équipe
    - town: ville de l'équipe
    - thumbnail: logo de l'équipe
    - year: année de création
    - stadium : nom du stade de l'équipe
"""

class Teams(models.Model):
    name = models.CharField(max_length=60)
    town = models.CharField(max_length=60)
    thumbnail = models.ImageField(upload_to="logo")  #si on ne veut pas que l'image soit obligatoire il faut ajoutter dans les param (blank=True, null=True)
    stadium = models.CharField(max_length=60)

class PLayers(models.Model)
    name = models.CharField(max_length=60)
    firstName = models.CharField(max_length=60)
    poste = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="photo")
    age = models.DateField()
    actif = models.BooleanField()
    injury = models.BooleanField()
    team = models.a


