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
    css = ""
    for team in teams:
        css += f"""
        .team-{team.id} {{
            background-color: {team.colorOne or ""};
            color: white
        }}
        """
    return HttpResponse(css, content_type="text/css")