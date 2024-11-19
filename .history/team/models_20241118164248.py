from django.db import models

# Create your models here.
"""
teams: nom de la table
    - name: nom de l'équipe
    - town: ville de l'équipe
    - thumbnail: logo de l'équipe
"""

class Teams(models.Model):
    name = models.CharField(max_length=60),
    town = models.CharField(max_length=60),
    thumbnail = models.ImageField(upload_to="logo")  #si on ne veut pas que l'image soit obligatoire il faut ajoutter dans les param