from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from itertools import groupby
from operator import attrgetter
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView

from playgames.forms import PlaygamesForm

from .models import PlayGame, Season, Week


# Create your views here.

class PlaygameIndexVue(ListView):
    model = PlayGame
    template_name = "playgames/index.html"
    context_object_name = "playgames"
    
    def get_context_data(self, **kwargs):
        # Appel de la méthode parent pour récupérer le contexte par défaut
        context = super().get_context_data(**kwargs)
        
         # Ajouter les saisons pour le premier select
        context['seasons'] = Season.objects.all()
        
        # Récupérer les paramètres GET pour la saison et la semaine
        selected_season_id = self.request.GET.get('season_id')
        selected_week_id = self.request.GET.get('week_id')

        # Initialiser les variables
        weeks = None
        grouped_playgames = None

        # Si une saison est sélectionnée, récupérer les semaines associées
        if selected_season_id:
            weeks = Week.objects.filter(season_id=selected_season_id)
            context['selected_season_id'] = int(selected_season_id)
            context['weeks'] = weeks

        # Si une semaine est sélectionnée, récupérer les matchs associés
        if selected_week_id:
            playgames = PlayGame.objects.filter(week_id=selected_week_id).order_by('played_at')
            grouped_playgames = {
                date: list(games) for date, games in groupby(playgames, attrgetter('played_at'))
            }
            context['selected_week_id'] = int(selected_week_id)
            context['grouped_playgames'] = grouped_playgames

        # Ajouter d'autres informations supplémentaires
        context['message'] = "Bienvenue sur la page des matchs!"
        context['playgame_count'] = PlayGame.objects.count()  # Nombre total de matchs
        
        return context
    
   
class PlaygameCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = PlayGame
    template_name = "playgames/addplaygame.html"
    form_class = PlaygamesForm
    success_url = reverse_lazy('playgames_index')

    # Vérifie si l'utilisateur est un superadmin
    def test_func(self):
        return self.request.user.is_superuser

    # Optionnel : Si l'utilisateur échoue au test
    def handle_no_permission(self):
        return redirect('playgames_index')

def ajax_load_weeks(request):
    season_id = request.GET.get("season")
    weeks = Week.objects.filter(season_id=season_id).order_by("week_number")
    return JsonResponse(list(weeks.values("id", "week_number")), safe=False)


class PlaygameDetailView(DetailView):
    model = PlayGame
    template_name = "playgames/playgame_detail.html"
    context_object_name = "post"

class PlaygameUpdateView(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = PlayGame
    template_name = "playgames/edit.html"
    form_class = PlaygamesForm

    def get_success_url(self):
        return reverse_lazy('playgame_detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ["submit_text"] = "Modifier"
        return context
    
    # Vérifie si l'utilisateur est un superadmin
    def test_func(self):
        return self.request.user.is_superuser

    # Optionnel : Si l'utilisateur échoue au test
    def handle_no_permission(self):
        return redirect('playgames_index')
    
class PlaygameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = PlayGame
    template_name = "playgame/delete.html"
    success_url = reverse_lazy('playgame_index')

    # Vérifie si l'utilisateur est un superadmin
    def test_func(self):
        return self.request.user.is_superuser

    # Optionnel : Si l'utilisateur échoue au test
    def handle_no_permission(self):
        return redirect('playgames_index')