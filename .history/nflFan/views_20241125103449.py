from django.shortcuts import render

#import des models
from team.models import PLayers

# Create your views here.
def index(request):
    return render(request,'nflFan/index.html')