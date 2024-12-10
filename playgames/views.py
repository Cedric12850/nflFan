from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView

from playgames.forms import PlaygamesForm

from .models import PlayGame


# Create your views here.
def playgames_index(request):
    return render(request, 'playgamesindex.html')

class PlaygameIndexVue(ListView):
    model = PlayGame
    template_name = "playgames/index.html"
    context_object_name = "playgames"
    
    def get_context_data(self, **kwargs):
        # Appel de la méthode parent pour récupérer le contexte par défaut
        context = super().get_context_data(**kwargs)
        
        # Ajouter des informations supplémentaires au contexte
        context['message'] = "Bienvenue sur la page des matchs!"
        context['playgame_count'] = PlayGame.objects.count()  # Nombre total de matchs
        
        return context
    
class PlaygameCreateView(CreateView):
    model = PlayGame
    template_name = "playgames/addplaygame.html"
    form_class = PlaygamesForm
    success_url = reverse_lazy('playgames_index')