from django.shortcuts import render

#import des models
from team.models import Teams
from team.services import fetch_data_from_api  # import API service

# Create your views here.
def index(request):
    # teams = Teams.objects.all()
    # return render(request,'team/index.html', {'teams': teams})

    
