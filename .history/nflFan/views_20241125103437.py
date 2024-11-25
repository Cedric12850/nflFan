from django.shortcuts import render

#import des models
from team.models import PLayers, Teams

# Create your views here.
def index(request):
    return render(request,'nflFab/index.html', {'teams': teams})