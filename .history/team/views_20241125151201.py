from django.http import HttpResponse
from django.shortcuts import render

#import des models
from team.models import Teams

# Create your views here.
def teams_index(request):
    teams = Teams.objects.all()
    return render(request,'team/index.html', {'teams': teams})

def dynamics_cssColorOne(request):
    teams = Teams.objects.all()
    css = ""
    for team in teams:
        css+= f"""
        .teamColorOne-{team.id} {{
            background-color: {team.colorOne or "#FFFFFF"};
            color: white
        }}
        """
    return HttpResponse(css, content_type="text/css")

def dynamics_cssColorTwo(request):
    teams = Teams.objects.all()
    css = ""
    for team in teams:
       
        css += """
        .teamColorTwo-{team.id} {{
            background-color: {team.colorTwo or "#FFFFFF"};
            color: white
        }}
        """
    return HttpResponse(css, content_type="text/css")