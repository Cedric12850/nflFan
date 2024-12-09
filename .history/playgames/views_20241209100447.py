from django.shortcuts import render

# Create your views here.
def playgames_index():
    return render(request, 'players/index.html', context)