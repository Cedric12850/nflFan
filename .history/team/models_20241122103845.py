from django.db import models

# Create your models here.

class Conferences(models.Model):
    name = models.CharField(max_length=80)
    shortName = models.CharField(max)
    def __str__(self):
        return self.name

# NB: Pour que la foreignKey fonctionne il faut que la class associé soit au-dessus
class Divisions(models.Model):
    name = models.CharField(max_length=50)
    conferences = models.ForeignKey(
        Conferences,
        on_delete=models.SET_NULL,   # Définit la valeur sur NULL si l'équipe est supprimée
        null=True,                   # Permet d'avoir des joueurs sans équipe
        blank=True,                  # Rend le champ facultatif dans les formulaires
        related_name="divisions"       # Facilite l'accès aux joueurs depuis une équipe
    )
    def __str__(self):
        return self.name

class Teams(models.Model):
    name = models.CharField(max_length=60)
    town = models.CharField(max_length=60)
    thumbnail = models.ImageField(upload_to="logo", null=True, blank=True)  #si on ne veut pas que l'image soit obligatoire il faut ajoutter dans les param (blank=True, null=True)
    stadium = models.CharField(max_length=60, null=True, blank=True)
    founded = models.DateField(default="1950-01-01")
    division = models.ForeignKey(
        Divisions,
        on_delete=models.SET_NULL,   # Définit la valeur sur NULL si l'équipe est supprimée
        null=True,                   # Permet d'avoir des joueurs sans équipe
        blank=True,                  # Rend le champ facultatif dans les formulaires
        related_name="teams"       # Facilite l'accès aux joueurs depuis une équipe
    )
    def __str__(self):
        return self.name


class PLayers(models.Model):
    name = models.CharField(max_length=60)
    firstName = models.CharField(max_length=60)
    poste = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="photo", null=True, blank=True)
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
    thumbnail = models.ImageField(upload_to="photo", null=True, blank=True)
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

    
class Superbowls(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    year = models.DateField
    town = models.CharField(max_length=60)
    stadium = models.CharField(max_length=60)
    winner = models.ForeignKey(
        Teams,
        on_delete=models.SET_NULL,   # Définit la valeur sur NULL si l'équipe est supprimée
        null=True,                   # Permet d'avoir des joueurs sans équipe
        blank=True,                  # Rend le champ facultatif dans les formulaires
        related_name="superbowls_winner"       # Facilite l'accès aux joueurs depuis une équipe
    )
    teamOne = models.ForeignKey(
        Teams,
        on_delete=models.SET_NULL,   # Définit la valeur sur NULL si l'équipe est supprimée
        null=True,                   # Permet d'avoir des joueurs sans équipe
        blank=True,                  # Rend le champ facultatif dans les formulaires
        related_name="superbowls_teamOne"       # Facilite l'accès aux joueurs depuis une équipe
    )
    teamTwo = models.ForeignKey(
        Teams,
        on_delete=models.SET_NULL,   # Définit la valeur sur NULL si l'équipe est supprimée
        null=True,                   # Permet d'avoir des joueurs sans équipe
        blank=True,                  # Rend le champ facultatif dans les formulaires
        related_name="superbowls_teamTwo"       # Facilite l'accès aux joueurs depuis une équipe
    )
    def __str__(self):
        return f"{self.name} ({self.year}"