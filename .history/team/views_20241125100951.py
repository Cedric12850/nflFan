from django.shortcuts import render

# Create your views here.
def index(request):
    teams = Teams.objects.all()
    return render(request,'team/index.html', {'teams': teams})
