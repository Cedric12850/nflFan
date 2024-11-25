from django.shortcuts import render
from team.models import Teams
from . import views

# Create your views here.
def index(request):
    teams = Teams.objects.all()
    return render(request,'team/index.html', {'teams': teams})
