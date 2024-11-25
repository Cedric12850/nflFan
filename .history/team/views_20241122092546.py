from django.shortcuts import render
from django.http import JsonResponse

#import des models
from team.models import Teams
from team.services import fetch_data_from_api  # import API service

# Create your views here.
def index(request):
    # teams = Teams.objects.all()
    # return render(request,'team/index.html', {'teams': teams})

    data = fetch_data_from_api()  # call API service 
    if 'error' in data:
        print(f"Erreur API : {data['error']}")
    else:
        print(f"Données API récupérées : {data}")
    # return 
    return render (request, 'team/index.html', {'api_data':data})
