from django import forms
from .models import Teams

class TeamGroupedSelect(forms.Select):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.choices = self.get_grouped_choices()

    def get_grouped_choices(self):
        # Grouper les équipes par division
        divisions = {}
        for team in Teams.objects.select_related('division').order_by('division__name', 'name'):
            divisions.setdefault(team.division.name, []).append((team.id, team.name))

        return [
            (division, teams) for division, teams in divisions.items()
        ]
def render(self, name, value, attrs=None, renderer=None):
        # Personnalisation de l'affichage en deux lignes de 4 divisions
        output = []
        output.append('<div class="team-select-container">')
        
        choices = list(self.choices)
        # Diviser les choix en deux groupes
        group1 = choices[:len(choices)//2]
        group2 = choices[len(choices)//2:]
        
        output.append('<div class="team-select-group">')
        for group in group1:
            division, teams = group
            output.append(f'<h3>{division}</h3>')
            for team in teams:
                output.append(f'<label><input type="checkbox" name="{name}" value="{team[0]}">{team[1]}</label><br>')
        output.append('</div>')

        output.append('<div class="team-select-group">')
        for group in group2:
            division, teams = group
            output.append(f'<h3>{division}</h3>')
            for team in teams:
                output.append(f'<label><input type="checkbox" name="{name}" value="{team[0]}">{team[1]}</label><br>')
        output.append('</div>')

        output.append('</div>')
        return ''.join(output)