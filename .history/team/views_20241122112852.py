from django.shortcuts import render

#import des models
from team.models import Teams

# Create your views here.
def index(request):
    teams = Teams.objects.all()
    return render(request,'team/index.html', {'teams': teams})

def index(request):
    players = Players.objects