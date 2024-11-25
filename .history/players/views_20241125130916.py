from django.shortcuts import render

from team.models import Players

# Create your views here.
def players_index (request):
    players = Players.object.all()
    return render(request, 'players/index.html', {'players': players})