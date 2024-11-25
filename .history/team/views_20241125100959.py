from django.shortcuts import render
from . import 
# Create your views here.
def index(request):
    teams = Teams.objects.all()
    return render(request,'team/index.html', {'teams': teams})
