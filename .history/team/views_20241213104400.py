from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView

#import des models
from nflFan.services import get_division_classement, get_team_results
from team import models
from team.forms import TeamForm
from team.models import Divisions, Teams

# Fonction pour afficher toutes les équipes (remplacer par la classe en-dessous)
# def teams_index(request):
#     teams = Teams.objects.all()
#     return render(request,'team/index.html', {'teams': teams})

# Class for list Team
class TeamIndexView(ListView):
    model = Teams
    template_name = "team/index.html"
    context_object_name = "teams"

# Fonction pour afficher une équipes par son id (remplacer par la classe en-dessous)
# def team_detail_view(request, pk):
#     team = get_object_or_404(Teams, pk=pk)
#     stadium = team.stadium  # Récupération du stade associé
#     coaches = team.coachs.all()
#     return render(request, 'team/team_detail.html', {
#         'team': team,
#         'coaches': coaches,
#         'stadium': stadium})

# Class for detail Team
class teamDetailView(DetailView):
    model = Teams
    template_name = "team/team_detail.html"
    context_object_name = "team"  # permet d'appeler l'objet dans le template pour l'afficher (à defaut il faut utiliser 'object')

    def get_context_data(self, **kwargs):
        # context par défault
        context = super().get_context_data(**kwargs)
        # id team
        team = self.object
        # appel service results
        total_wins, total_losses = get_team_results(team.id)
        # appel service classement
        classement = get_division_classement(team.id)
        # edition du context
        context["total_wins"] = total_wins
        context["total_losses"] = total_losses
        
        if classement:
            context["rank"] = classement["ran"]
        return context      # utiliser total_wins et total_losses dans le templates
    
# Class for update Team
class UpdateTeamView(UpdateView):
    model = Teams
    template_name = "team/edit.html"
    form_class = TeamForm

    def get_success_url(self):
        return reverse_lazy('team_detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["submit_text"] = "Modifier"
        return context
    
# Récupération des équipes par division pour afficher dans la navBar
def division_team(request):
    divisions = Divisions.objects.prefetch_related('teams').all()

    # Structure les données pour les envoyer en JSON
    data = []
    for division in divisions:
        data.append({
            "division": division.name,
            "teams": list(division.teams.values()),  # Champs pertinents pour chaque équipe
        })

    # print("Données envoyées :", data)  # Debug dans le terminal
    return JsonResponse(data, safe=False)  # Renvoie la réponse JSON



# --------------------------------------------------------------------------------------------------------------- #
def dynamics_css(request):
    teams = Teams.objects.all()
    css = ""
    for team in teams:
        css += f"""
        .teamColorOne-{team.id} {{
            background-color: {team.colorOne or "#FFFFFF"};
            color: white;
            box-shadow: 1px 1px 2px 2px {team.colorTwo or "#FFFFFF"};
        }}
        .teamColorTwo-{team.id} {{
            background-color: {team.colorTwo or "#FFFFFF"};
        }}

        .detailbackgroundteamColorOne-{team.id} {{
            background-color: {team.colorOne or "#FFFFFF"};
            color: white
        }}
        .detailbackgroundteamColorTwo-{team.id} {{
            background-color: {team.colorTwo or "#FFFFFF"};
            color: white
        }}
        """
    return HttpResponse(css, content_type="text/css")