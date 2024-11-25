from django.http import HttpResponse
from django.shortcuts import render

from team.models import PLayers, Teams


# Create your views here.
def players_index (request):
    players = PLayers.objects.all()
    return render(request, 'players/index.html', {'players': players})

def dynamics_cssColorOne(request):
    teams = Teams.objects.all()
    colorOne = ""
    colorTwo = ""
    for team in teams:
        colorOne += f"""
        .teamColorOne-{team.id} {{
            background-color: {team.colorOne or "#FFFFFF"};
            color: white
        }}
        """
        colorTwo += """
        .teamColorTwo-{team.id} {{
            background-color: {team.colorOne or "#FFFFFF"};
            color: white
        }}
        """
    return HttpResponse(colorOne, colorTwo, content_type="text/css")

def dynamics_cssColorOne(request):
    teams = Teams.objects.all()
    colorOne = ""
    colorTwo = ""
    for team in teams:
        colorOne += f"""
        .teamColorOne-{team.id} {{
            background-color: {team.colorOne or "#FFFFFF"};
            color: white
        }}
        """
        colorTwo += """
        .teamColorTwo-{team.id} {{
            background-color: {team.colorOne or "#FFFFFF"};
            color: white
        }}
        """
    return HttpResponse(colorOne, colorTwo, content_type="text/css")