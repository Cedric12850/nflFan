from django.shortcuts import render

#import des models
from team.models import Teams

# Create your views here.
def index(request):
    teams = Teams.objects.all()
    data = fetch_data_from_api()  
    return render(request,'team/index.html', {'teams': teams})
