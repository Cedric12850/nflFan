from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView

from playgames.forms import PlaygamesForm

from .models import PlayGame, Week


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

def ajax_load_weeks(request):
    season_id = request.GET.get("season")
    weeks = Week.objects.filter(season_id=season_id).order_by("week_number")
    return JsonResponse(list(weeks.values("id", "week_number")), safe=False)


class PlaygameDetailView(DetailView):
    model = PlayGame
    template_name = "playgames/playgame_detail.html"
    context_object_name = "post"

class PlaygameUpdateView(UpdateView):
    model = PlayGame
    template_name = "playgames/edit.html"
    form_class = PlaygamesForm

    def get_success_url(self):
        return reverse_lazy('playgame_detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ["submit_text"] = "Modifier"
        return context
    
def get_weeks(request):
    season_id = request.GET.get("season")  # Récupère l'ID de la saison depuis la requête GET
    if not season_id:
        return JsonResponse([], safe=False)  # Retourne une liste vide si aucun ID

    # Récupère les semaines associées à la saison
    weeks = Week.objects.filter(season_id=season_id).order_by('week_number')
    data = [{"id": week.id, "name": str(week)} for week in weeks]
    return JsonResponse(data, safe=False)  # Retourne les données sous forme de JSON