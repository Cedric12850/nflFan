from django.shortcuts import render

#import des models

# Create your views here.
def index(request):
    return render(request,'nflFan/index.html')