from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView


# Create your views here.
def playgames_index(request):
    return render(request, 'playgamesindex.html')

class PlaygameIndexVue(ListView):
    model = Pl