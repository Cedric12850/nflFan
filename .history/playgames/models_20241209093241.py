from django.db import models

from team.models import Teams

# Create your models here.
class Season(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    

class week(models.Model):
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        related_name="weeks"
    )
    week_number = models.PositiveIntegerField()
    is_playoff = models.BooleanField(default=False)

    def __str__(self):
        playoff = "(playoff)"

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
    def __string__(self):
        return f"{self.team_local} vs {self.team_visitor}"