from django.shortcuts import render

from team.models import PLayers

# Create your views here.
def players_index (request):
    players = PLayers.object.all()
    return render(request, 'players/index.html', {pla})