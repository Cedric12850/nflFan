from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import F

from playgames.models import PlayGame
from team import models
from team.models import Teams


# Create your views here.
def home(request):
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
    return render(request,'index.html', {'results': results})

# Récupération des réusltats et calcul du bilan de l'équipe
def get_team_results(team_id):
    # Nombre de victoires en tant qu'équipe locale
    local_wins = PlayGame.objects.filter(
        team_local_id=team_id, 
        score_local__gt=F("score_visitor")  # Victoire si le score_local est supérieur au score_visitor
    ).count()

    # Nombre de victoires en tant qu'équipe visiteuse
    visitor_wins = PlayGame.objects.filter(
        team_visitor_id=team_id, 
        score_visitor__gt=F("score_local")  # Victoire si le score_visitor est supérieur au score_local
    ).count()

    # Total des victoires
    total_wins = local_wins + visitor_wins

    # Nombre de défaites en tant qu'équipe locale
    local_losses = PlayGame.objects.filter(
        team_local_id=team_id, 
        score_local__lt=F("score_visitor")  # Défaite si le score_local est inférieur au score_visitor
    ).count()

    # Nombre de défaites en tant qu'équipe visiteuse
    visitor_losses = PlayGame.objects.filter(
        team_visitor_id=team_id, 
        score_visitor__lt=F("score_local")  # Défaite si le score_visitor est inférieur au score_local
    ).count()

    # Total des défaites
    total_losses = local_losses + visitor_losses

    return total_wins, total_losses


from utils import get_playgame_data

def my_view(request):
    playgame_data = get_playgame_data()
    return render(request, 'some_template.html', {'playgame_data': playgame_data})