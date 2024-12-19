from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView
from numpy import number

from players.filters import PLayersFilter
from players.forms import PlayerForm
from players.models import PLayers
from team.models import Teams


# Vue pour afficher tous les joueurs de la BdD et les filtrer dans la recherche
class PlayerListView(ListView):
    model = PLayers
    template_name = 'players/index.html'
    context_object_name = 'players'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |  # Recherche par nom (insensible à la casse)
                Q(firstName__icontains=search_query) |  # Recherche par prénom
                Q(team__name__icontains=search_query) | # Recherche par équipe
                Q(number__icontains=search_query) | # Recherche par numéro
                Q(poste__abrev__icontains=search_query) # Recherche par poste
            )
        # Appliquer l'ordre (order_by) par poste (abrev de poste, par exemple)
        queryset = queryset.order_by('number')  # Tri par poste (abrev)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')  # Passer la recherche au template
        return context

from django.http import JsonResponse

def player_autocomplete(request):
    search_query = request.GET.get('term', '')
    results = []
    if search_query:
        players = PLayers.objects.filter(
            Q(name__icontains=search_query) |  # Recherche par nom (insensible à la casse)
            Q(firstName__icontains=search_query) |  # Recherche par prénom
            Q(team__name__icontains=search_query) | # Recherche par équipe
            Q(number__icontains=search_query) | # Recherche par numéro
            Q(poste__abrev__icontains=search_query) # Recherche par poste
        )[:10]  # Limitez les résultats pour éviter de surcharger les réponses
        results = [{'id': player.id, 'label': f"{player.name} {player.firstName}", 'value': player.name} for player in players]
    return JsonResponse(results, safe=False)

class PlayerCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = PLayers
    template_name = "players/addplayer.html"
    form_class = PlayerForm
    success_url = reverse_lazy("players_index")

    def form_invalid(self, form):
        # Afficher les erreurs du formulaire dans la console
        print(form.errors)
        return super().form_invalid(form)
    
    # Vérifie si l'utilisateur est un superadmin
    def test_func(self):
        return self.request.user.is_superuser

    # Optionnel : Si l'utilisateur échoue au test
    def handle_no_permission(self):
        return redirect('players_index')

# Vue pour afficher un joueur en détail
def player_detail(request, pk):
    player = get_object_or_404(PLayers, pk=pk) # On récupère les joueurs par leurs id
    return render(request, 'players/player_detail.html', {'player': player})

# Class for update player
class PlayerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = PLayers
    template_name = "players/edit.html"
    form_class = PlayerForm
    
    def get_success_url(self):
        return reverse_lazy('player_detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["submit_text"] = "Modifier"
        return context
    
    # Vérifie si l'utilisateur est un superadmin
    def test_func(self):
        return self.request.user.is_superuser

    # Optionnel : Si l'utilisateur échoue au test
    def handle_no_permission(self):
        return redirect('players_index')

# Class for delete player
class PlayerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = PLayers
    template_name = "players/delete.html"
    success_url = reverse_lazy('players_index')

    # Vérifie si l'utilisateur est un superadmin
    def test_func(self):
        return self.request.user.is_superuser

    # Optionnel : Si l'utilisateur échoue au test
    def handle_no_permission(self):
        return redirect('players_index')


# Ne fonctionne pas à corriger Pour le moment j'utilise le css dynamique de team
def dynamics_css(request):
    teams = Teams.objects.all()
    css = ""
    for team in teams:
        css += f"""
        .detailTopViewteamColorOne-{{player.team.id}} {{
            background-color: {team.colorOne or "#FFFFFF"};
            color: white
        }}
        
        .detailTopViewborderTeamColorTwo-{{player.team.id}} {{
            border: 0.7rem solid {team.colorTwo or "#FFFFFF"};
        }}
        """
    return HttpResponse(css, content_type="text/css")