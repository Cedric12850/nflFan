from django.shortcuts import render

#import des models
from team.models import PLayers, Teams

# Create your views here.
def index(request):
    teams = Teams.objects.all()
    return render(request,'team/index.html', {'teams': teams})

def index(request):
    players = PLayers.objects.all()
    return render(request, 'player/index.html', {''})