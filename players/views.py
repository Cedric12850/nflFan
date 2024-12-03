from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from players.filters import PLayersFilter
from players.forms import PlayerForm
from players.models import PLayers
from team.models import Teams


# Vue pour afficher tous les joueurs de la BdD et les filtrer dans la recherche
def players_index (request):
    players = PLayers.objects.all()
    for player in players:
        player.team = Teams.objects.get(id=player.team_id)
    player_filter = PLayersFilter(request.GET, queryset=players)
    context = {
        'filter': player_filter,  # Pour le formulaire de filtre
        'players': player_filter.qs,  # Résultats filtrés
    }
    return render(request, 'players/index.html', context)

# Vue pour ajoutter un joueur dans la BdD
def addplayer(request):
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Joueur ajouté avec succès à la base de données.")
            return redirect('/players/')
        else:
            return render(request, 'players/addplayer.html', {"form": form, "errors": form.errors})
    else:
        form = PlayerForm()
             
    return render(request, "players/addplayer.html", {"form": form})


# Vue pour afficher un joueur en détail
def player_detail(request, id):
    player = get_object_or_404(PLayers, id=id)
    return render(request, 'players/player_detail.html', {'player': player})


# Ne fonctionne pas à corriger Pour le moment j'utilise le css dynamique de team
def dynamics_css(request):
    teams = Teams.objects.all()
    css = ""
    for team in teams:
        css += f"""
        .detailTopViewteamColorOne-{{player.team.id}} {{
            background-color: {team.colorOne or "#FFFFFF"};
            color: white
        }}
        
        .detailTopViewborderTeamColorTwo-{{player.team.id}} {{
            border: 0.7rem solid {team.colorTwo or "#FFFFFF"};
        }}
        """
    return HttpResponse(css, content_type="text/css")