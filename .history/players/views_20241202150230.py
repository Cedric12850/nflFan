from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from players.forms import PlayerForm
from players.models import PLayers
from team.models import Teams


# Create your views here.
def players_index (request):
    players = PLayers.objects.all()
    for player in players:
        player.team = Teams.objects.get(id=player.team_id)
    player_filter = PlayerFilter(request.GET)
    return render(request, 'players/index.html', {'players': players})

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


# Ne fonctionne pas à corriger POur le moement j'utilise le css dynamique de team
def dynamics_css(request):
    teams = Teams.objects.all()
    css = ""
    for team in teams:
        css += f"""
        .teamColorOne-{{player.team.id}} {{
            background-color: {team.colorOne or "#FFFFFF"};
            color: white
        }}
        .teamColorTwo-{{player.team.id}} {{
            background-color: {team.colorTwo or "#FFFFFF"}
        }}

        .borderTeamColorOne-{{player.team.id}} {{
            border: 0.7rem solid {team.colorOne or "#FFFFFF"};
        }}
        .borderTeamColorTwo-{{player.team.id}} {{
            border: 0.7rem solid {team.colorTwo or "#FFFFFF"};
        }}
        """
    return HttpResponse(css, content_type="text/css")