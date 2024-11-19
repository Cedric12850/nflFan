from django.db import models

# Create your models here.

class Teams(models.Model):
    name = models.CharField(max_length=60)
    town = models.CharField(max_length=60)
    thumbnail = models.ImageField(upload_to="thumbnail/logo", null=True, blank=True)  #si on ne veut pas que l'image soit obligatoire il faut ajoutter dans les param (blank=True, null=True)
    stadium = models.CharField(max_length=60, null=True, blank=True)
    founded = models.DateField(default="1950-01-01")
    division = models.ForeignKey
    def __str__(self):
        return self.name


class PLayers(models.Model):
    name = models.CharField(max_length=60)
    firstName = models.CharField(max_length=60)
    poste = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="thumbnail/photo", null=True, blank=True)
    age = models.DateField(default="1980-01-01")
    actif = models.BooleanField()
    injury = models.BooleanField()
    team = models.ForeignKey(
    Teams,
    on_delete=models.SET_NULL,   # Définit la valeur sur NULL si l'équipe est supprimée
    null=True,                   # Permet d'avoir des joueurs sans équipe
    blank=True,                  # Rend le champ facultatif dans les formulaires
    related_name="players"       # Facilite l'accès aux joueurs depuis une équipe
    )
    def __str__(self):           # Formate l'affichage en BdD
        return f"{self.name} {self.firstName}"


class Coachs(models.Model):
    name = models.CharField(max_length=60)
    firstName = models.CharField(max_length=60)
    poste = models.CharField(max_length=50, null=True, blank=True)
    thumbnail = models.ImageField(upload_to="thumbnail/photo", null=True, blank=True)
    actif = models.BooleanField()
    team = models.ForeignKey(
    Teams,
    on_delete=models.SET_NULL,   # Définit la valeur sur NULL si l'équipe est supprimée
    null=True,                   # Permet d'avoir des joueurs sans équipe
    blank=True,                  # Rend le champ facultatif dans les formulaires
    related_name="coachs"       # Facilite l'accès aux joueurs depuis une équipe
    )
    def __str__(self):           # Formate l'affichage en BdD
        return f"{self.name} {self.firstName}"


class Divisions(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Conferences(models.Model):