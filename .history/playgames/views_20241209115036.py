from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView

from .models import PlayGame


# Create your views here.
def playgames_index(request):
    return render(request, 'playgamesindex.html')

class PlaygameIndexVue(ListView):
    model = PlayGame
    template_name = "playgames/index.html"
    context_object_name = "playgames"

def get_queryset(self):
        # Vous pouvez ici filtrer ou personnaliser la requête si nécessaire
        queryset = super().get_queryset()

        # Par exemple, vous pouvez afficher toutes les entrées de PlayGame
        print(queryset)  # Affiche toutes les entrées de PlayGame dans la console

        # Ou afficher un détail spécifique
        for playgame in queryset:
            print(f"Match {playgame.team_local} vs {playgame.team_visitor} à {playgame.played_at}")

        return queryset