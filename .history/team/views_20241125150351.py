from django.http import HttpResponse
from django.shortcuts import render

#import des models
from team.models import Teams

# Create your views here.
def teams_index(request):
    teams = Teams.objects.all()
    return render(request,'team/index.html', {'teams': teams})

def dynamics_css(request):
    teams = Teams.objects.all()
    colorOne = ""
    color
    for team in teams:
        colorOne += f"""
        .team-{team.id} {{
            background-color: {team.colorOne or "#FFFFFF"};
            color: white
        }}
        """
    return HttpResponse(css, content_type="text/css")