from django.shortcuts import render

# Create your views here.
def playgames_index():
    return render(request, 'playgamesindex.html', context)