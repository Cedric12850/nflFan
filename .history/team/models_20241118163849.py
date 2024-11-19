from django.db import models

# Create your models here.
"""
teams: nom de la table
    - name: nom de l'équipe
    - town: ville de l'équipe
    - thumbnail: logo de l'équipe
"""

class Teams(models.Model):
    name = models.CharField()