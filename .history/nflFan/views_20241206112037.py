from django.http import HttpResponse
from django.shortcuts import render

from team.models import PlayGame, Teams


# Create your views here.
def home(request):
    return render(request,'index.html')

# Récupération des réusltats et calcul du bilan de l'équipe
def get_team_results(request, team_id):
    # Nombre de victoire en local
    local_wins = PlayGame.objects.filter(
        team_local_id = 5,
        score_local__gt=F("score_visitor")
    ).count()

    # Idem en visitor
    visitor_wins =PlayGame.objects.filter(
        team_visitor_id = 5,
        score_visitor__gt=F("score_local")
    ).count()
    # Total
    total_wins = local_wins + visitor_wins
    print(total_wins)
    return render(request, 'index.html')