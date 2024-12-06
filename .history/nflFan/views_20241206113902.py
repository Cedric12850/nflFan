from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import F

from team import models
from team.models import PlayGame, Teams


# Create your views here.
def home(request):
    teams = Teams.objects.all()
    results = []
    for team in teams:
    wins, losses = get_team_results(team_id)
    results.append({
        'team': team
    })
    return render(request,'index.html', context)

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