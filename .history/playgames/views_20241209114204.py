from django.shortcuts import render

# Create your views here.
def playgames_index(request):
    return render(request, 'playgamesindex.html')

class Playgame