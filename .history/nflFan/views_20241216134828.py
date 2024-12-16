from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import F

from nflFan.services import get_team_results
from nflFan.utils import get_playgame_data
from playgames.models import PlayGame
from team import models
from team.models import Teams


# Create your views here.
def home(request):
    context_playgames = get_playgame_data()
    teams = Teams.objects.all()

    results = []
    # Utilisation de la fonctions qui calcul les résultats pour affichage dans navBar
    for team in teams:
        wins, losses = get_team_results(team.id)
        results.append({
        'team': team,
        'wins': wins,
        'losses': losses
    })
     # Fusionner les deux contextes (résultats des équipes et les données de playgames)
    context_playgames.update({'results': results})  # Ajoutez 'results' au contexte des playgames
    
    # Rendre la page avec le contexte mis à jour
    return render(request, 'index.html', context_playgames)

@shared_task
def update_playgame_display():
    playgame_data = get_playgame_data()
    # Vous pouvez maintenant mettre à jour la base de données ou envoyer des notifications
    # Par exemple, stocker le résultat dans un cache, ou notifier les utilisateurs
    print("Données de la semaine en cours :", playgame_data)