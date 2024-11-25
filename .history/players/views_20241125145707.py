from django.http import HttpResponse
from django.shortcuts import render

from team.models import PLayers, Teams


# Create your views here.
def players_index (request):
    players = PLayers.objects.all()
    return render(request, 'players/index.html', {'players': players})

def dynamics_css(request):
    teams = Teams.objects.all()
    css = ""
    for team in teams:
        css += f"""
        .team-{team.id} {{
            background-color: {team.colorOne or "#FFFFFF"};
            color: white
        }}
        """
        print 
    return HttpResponse(css, content_type="text/css")