from django.shortcuts import render

# Create your views here.
def playgames_index(req):
    return render(request, 'playgamesindex.html')