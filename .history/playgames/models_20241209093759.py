from django.db import models

from team.models import Teams

# Create your models here.
class Season(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    

class Week(models.Model):
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        related_name="weeks"
    )
    week_number = models.PositiveIntegerField()
    is_playoff = models.BooleanField(default=False)

    def __str__(self):
        playoff = "(Playoff)" if self.is_playoff else ""
        return f"Week {self.week_number} - {self.season.name}{playoff}"
    

class PlayGame(models.Model):
    team_local = models.ForeignKey(
        Teams,
        on_delete= models.CASCADE,
        related_name='local_playGames'
    )
    team_visitor = models.ForeignKey(
        Teams,
        on_delete= models.CASCADE,
        related_name= 'visitor_playGames'
    )
    score_local = models.IntegerField(default=0)
    score_visitor = models.IntegerField(default=0)
    week = models.ForeignKey(
        Week,
        on_delete=models.CASCADE,
        related_name="games"
    )
    played_at = models.DateTimeField()
    def __string__(self):
        return f"{self.team_local} vs {self.team_visitor} ({self.week})"
    
    class Superbowls(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    year = models.DateField(null=True, blank=True)
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
        return f"{self.name} ({self.year})"