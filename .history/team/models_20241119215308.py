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
    founded = models.DateField(default="1950-01-01")

class PLayers(models.Model):
    name = models.CharField(max_length=60)
    firstName = models.CharField(max_length=60)
    poste = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="photo")
    age = models.DateField(default=)
    actif = models.BooleanField()
    injury = models.BooleanField()
    team = models.ForeignKey(
    Teams,
    on_delete=models.SET_NULL,   # Définit la valeur sur NULL si l'équipe est supprimée
    null=True,                   # Permet d'avoir des joueurs sans équipe
    blank=True,                  # Rend le champ facultatif dans les formulaires
    related_name="players"       # Facilite l'accès aux joueurs depuis une équipe
    )


