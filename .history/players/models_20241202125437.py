from django.db import models

from team.models import Teams

# Create your models here.
class Player_position(models.Model):
    abrev = models.CharField(max_length=10)
    name = models.CharField(max_length=60)
    def __str__(self):
        return f"{self.name} ({self.abrev})"

    
class PLayers(models.Model):
    name = models.CharField(max_length=60)
    firstName = models.CharField(max_length=60)
    poste = models.ForeignKey(
        Player_position,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="players"
    )
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
    
    class Meta:
        db_table = 'team_players'  # Utilise l'ancienne table existante
