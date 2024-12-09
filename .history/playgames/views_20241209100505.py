from django.shortcuts import render
from requests import request

# Create your views here.
def playgames_index():
    return render(request, 'playgamesindex.html')