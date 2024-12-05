from django.http import HttpResponse
from django.shortcuts import render

from team.models import Teams


# Create your views here.
def home(request):
    return render(request,'index.html')

